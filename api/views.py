from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from articles.models import Article
from newsletters.models import Newsletter
from publishers.models import Publisher

from .permissions import ArticleRolePermission
from .serializers import (
    ArticleSerializer,
    NewsletterSerializer,
    PublisherSerializer,
    UserSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [ArticleRolePermission]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.is_editor():
            return Article.objects.all()

        if user.is_authenticated and user.is_journalist():
            return Article.objects.filter(
                Q(approved=True) | Q(author=user)
            ).distinct()

        return Article.objects.filter(approved=True)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            approved=False,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        url_path="subscribed",
    )
    def subscribed(self, request):
        user = request.user

        publisher_ids = user.subscribed_publishers.values_list("id", flat=True)
        journalist_ids = user.subscribed_journalists.values_list("id", flat=True)

        articles = Article.objects.filter(
            approved=True
        ).filter(
            Q(publisher_id__in=publisher_ids)
            | Q(author_id__in=journalist_ids)
        ).distinct()

        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        return Newsletter.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
