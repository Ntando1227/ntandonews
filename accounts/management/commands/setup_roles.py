from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

from articles.models import Article
from newsletters.models import Newsletter


class Command(BaseCommand):
    help = "Create Ntando's News user groups and assign permissions."

    def handle(self, *args, **options):
        reader_group, _ = Group.objects.get_or_create(name="Reader")
        journalist_group, _ = Group.objects.get_or_create(name="Journalist")
        editor_group, _ = Group.objects.get_or_create(name="Editor")

        article_ct = ContentType.objects.get_for_model(Article)
        newsletter_ct = ContentType.objects.get_for_model(Newsletter)

        article_perms = Permission.objects.filter(content_type=article_ct)
        newsletter_perms = Permission.objects.filter(content_type=newsletter_ct)

        view_article = article_perms.get(codename="view_article")
        add_article = article_perms.get(codename="add_article")
        change_article = article_perms.get(codename="change_article")
        delete_article = article_perms.get(codename="delete_article")

        view_newsletter = newsletter_perms.get(codename="view_newsletter")
        add_newsletter = newsletter_perms.get(codename="add_newsletter")
        change_newsletter = newsletter_perms.get(codename="change_newsletter")
        delete_newsletter = newsletter_perms.get(codename="delete_newsletter")

        reader_group.permissions.set([
            view_article,
            view_newsletter,
        ])

        journalist_group.permissions.set([
            view_article,
            add_article,
            change_article,
            delete_article,
            view_newsletter,
            add_newsletter,
            change_newsletter,
            delete_newsletter,
        ])

        editor_group.permissions.set([
            view_article,
            change_article,
            delete_article,
            view_newsletter,
            change_newsletter,
            delete_newsletter,
        ])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))
