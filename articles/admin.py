from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "publisher",
        "approved",
        "created_at",
    )

    list_filter = (
        "approved",
        "publisher",
        "created_at",
    )

    search_fields = (
        "title",
        "summary",
        "content",
        "author__username",
        "publisher__name",
    )

    list_editable = ("approved",)
    date_hierarchy = "created_at"
