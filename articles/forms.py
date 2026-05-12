from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "category",
            "summary",
            "content",
            "publisher",
            "featured_image",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Article headline"}),
            "summary": forms.Textarea(attrs={"rows": 3, "placeholder": "Short summary"}),
            "content": forms.Textarea(attrs={"rows": 10, "placeholder": "Write the full article here"}),
        }
