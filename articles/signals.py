from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article
from .utils import email_article_to_subscribers, post_article_to_x


@receiver(post_save, sender=Article)
def article_approval_actions(sender, instance, created, **kwargs):
    if created:
        return

    if instance.approved:
        email_article_to_subscribers(instance)
        post_article_to_x(instance)
