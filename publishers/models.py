from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    editors = models.ManyToManyField(
        "accounts.CustomUser",
        related_name="editor_publishers",
        blank=True,
        limit_choices_to={"role": "editor"},
    )

    journalists = models.ManyToManyField(
        "accounts.CustomUser",
        related_name="journalist_publishers",
        blank=True,
        limit_choices_to={"role": "journalist"},
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
