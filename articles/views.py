from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm
from .models import Article


def article_list(request):
    articles = Article.objects.filter(approved=True)
    return render(request, "articles/article_list.html", {"articles": articles})


def articles_by_category(request, category):
    valid_categories = [choice[0] for choice in Article.CATEGORY_CHOICES]

    if category not in valid_categories:
        raise PermissionDenied("Invalid article category.")

    articles = Article.objects.filter(
        approved=True,
        category=category,
    )

    category_name = dict(Article.CATEGORY_CHOICES).get(category)

    return render(
        request,
        "articles/category_articles.html",
        {
            "articles": articles,
            "category": category,
            "category_name": category_name,
        },
    )


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, approved=True)
    related_articles = Article.objects.filter(
        approved=True,
        category=article.category,
    ).exclude(pk=article.pk)[:3]

    return render(
        request,
        "articles/article_detail.html",
        {
            "article": article,
            "related_articles": related_articles,
        },
    )


@login_required
def article_create(request):
    if not request.user.is_journalist():
        raise PermissionDenied("Only journalists can create articles.")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.approved = False
            article.save()

            messages.success(request, "Article submitted successfully. It is now awaiting editor approval.")
            return redirect("journalist_dashboard")
    else:
        form = ArticleForm()

    return render(request, "articles/article_form.html", {"form": form})


@login_required
def journalist_dashboard(request):
    if not request.user.is_journalist():
        raise PermissionDenied("Only journalists can view this dashboard.")

    articles = Article.objects.filter(author=request.user)

    return render(
        request,
        "articles/journalist_dashboard.html",
        {"articles": articles},
    )


@login_required
def editor_dashboard(request):
    if not request.user.is_editor():
        raise PermissionDenied("Only editors can view this dashboard.")

    pending_articles = Article.objects.filter(approved=False)
    approved_articles = Article.objects.filter(approved=True)[:10]

    return render(
        request,
        "articles/editor_dashboard.html",
        {
            "pending_articles": pending_articles,
            "approved_articles": approved_articles,
        },
    )


@login_required
def approve_article(request, pk):
    if not request.user.is_editor():
        raise PermissionDenied("Only editors can approve articles.")

    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.approved = True
        article.save()
        messages.success(request, f"'{article.title}' has been approved and published.")
        return redirect("editor_dashboard")

    return render(request, "articles/article_approve.html", {"article": article})
