from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ArticleViewSet, NewsletterViewSet, PublisherViewSet, UserViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="api_articles")
router.register("publishers", PublisherViewSet, basename="api_publishers")
router.register("newsletters", NewsletterViewSet, basename="api_newsletters")
router.register("users", UserViewSet, basename="api_users")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
