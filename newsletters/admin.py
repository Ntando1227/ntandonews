from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "author__username",
    )

    filter_horizontal = ("articles",)
    date_hierarchy = "created_at"
