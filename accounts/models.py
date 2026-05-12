from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    READER = "reader"
    JOURNALIST = "journalist"
    EDITOR = "editor"

    ROLE_CHOICES = [
        (READER, "Reader"),
        (JOURNALIST, "Journalist"),
        (EDITOR, "Editor"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=READER,
    )

    subscribed_publishers = models.ManyToManyField(
        "publishers.Publisher",
        related_name="subscribers",
        blank=True,
    )

    subscribed_journalists = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="journalist_subscribers",
        blank=True,
    )

    bio = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    def is_reader(self):
        return self.role == self.READER

    def is_journalist(self):
        return self.role == self.JOURNALIST

    def is_editor(self):
        return self.role == self.EDITOR

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        role_group_map = {
            self.READER: "Reader",
            self.JOURNALIST: "Journalist",
            self.EDITOR: "Editor",
        }

        group_name = role_group_map.get(self.role)

        if group_name:
            self.groups.clear()
            group, _ = Group.objects.get_or_create(name=group_name)
            self.groups.add(group)

        if self.role == self.JOURNALIST:
            self.subscribed_publishers.clear()
            self.subscribed_journalists.clear()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
