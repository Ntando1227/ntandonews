from rest_framework import serializers

from accounts.models import CustomUser
from articles.models import Article
from newsletters.models import Newsletter
from publishers.models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            "id",
            "name",
            "description",
            "website",
            "created_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "role",
            "bio",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    publisher_name = serializers.CharField(source="publisher.name", read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "summary",
            "content",
            "author",
            "author_name",
            "publisher",
            "publisher_name",
            "approved",
            "featured_image",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "author",
            "approved",
            "created_at",
            "updated_at",
        ]


class NewsletterSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Newsletter
        fields = [
            "id",
            "title",
            "description",
            "author",
            "author_name",
            "articles",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "author",
            "created_at",
            "updated_at",
        ]
