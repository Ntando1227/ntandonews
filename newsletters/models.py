from django.conf import settings
from django.db import models


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="newsletters",
        limit_choices_to={"role": "journalist"},
    )

    articles = models.ManyToManyField(
        "articles.Article",
        related_name="newsletters",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
