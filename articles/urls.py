from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("category/<str:category>/", views.articles_by_category, name="articles_by_category"),
    path("create/", views.article_create, name="article_create"),
    path("journalist/dashboard/", views.journalist_dashboard, name="journalist_dashboard"),
    path("editor/dashboard/", views.editor_dashboard, name="editor_dashboard"),
    path("<int:pk>/approve/", views.approve_article, name="approve_article"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
]
