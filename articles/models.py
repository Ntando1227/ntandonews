from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):

    SPORTS = "sports"
    POLITICS = "politics"
    FINANCE = "finance"
    CURRENT_AFFAIRS = "current_affairs"
    COMMUNITY = "community"

    CATEGORY_CHOICES = [
        (SPORTS, "Sports"),
        (POLITICS, "Politics"),
        (FINANCE, "Finance"),
        (CURRENT_AFFAIRS, "Current Affairs"),
        (COMMUNITY, "Community"),
    ]

    INTERNAL = "internal"
    AGGREGATED = "aggregated"

    ARTICLE_TYPE_CHOICES = [
        (INTERNAL, "Internal"),
        (AGGREGATED, "Aggregated"),
    ]

    title = models.CharField(max_length=255)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default=COMMUNITY,
    )

    article_type = models.CharField(
        max_length=30,
        choices=ARTICLE_TYPE_CHOICES,
        default=INTERNAL,
    )

    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="articles",
        limit_choices_to={"role": "journalist"},
        blank=True,
        null=True,
    )

    publisher = models.ForeignKey(
        "publishers.Publisher",
        on_delete=models.SET_NULL,
        related_name="articles",
        blank=True,
        null=True,
    )

    approved = models.BooleanField(default=False)

    source_name = models.CharField(
        max_length=200,
        blank=True,
    )

    external_url = models.URLField(
        blank=True,
        unique=True,
        null=True,
    )

    external_image_url = models.URLField(
        blank=True,
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    featured_image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "-published_at",
            "-created_at",
        ]

    def save(self, *args, **kwargs):

        if not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "article_detail",
            kwargs={"pk": self.pk},
        )

    def is_external(self):
        return self.article_type == self.AGGREGATED

    def __str__(self):
        return self.title
