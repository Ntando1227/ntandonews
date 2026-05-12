from django.shortcuts import render
from articles.models import Article
from publishers.models import Publisher


def home(request):
    featured_articles = Article.objects.filter(approved=True)[:3]
    latest_articles = Article.objects.filter(approved=True)[3:9]
    publishers = Publisher.objects.all()[:6]

    context = {
        "featured_articles": featured_articles,
        "latest_articles": latest_articles,
        "publishers": publishers,
    }

    return render(request, "core/home.html", context)
