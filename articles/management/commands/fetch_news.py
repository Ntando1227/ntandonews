import requests

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime

from articles.models import Article
from publishers.models import Publisher


class Command(BaseCommand):
    help = "Fetch live South African news into Ntando's News."

    def add_arguments(self, parser):
        parser.add_argument(
            "--category",
            type=str,
            default="all",
            help="sports, politics, finance, current_affairs, or all",
        )

    def handle(self, *args, **options):

        if not settings.NEWS_API_KEY:
            self.stdout.write(
                self.style.ERROR("NEWS_API_KEY is missing.")
            )
            return

        requested_category = options["category"]

        category_map = {
            "sports": "sports",
            "politics": "general",
            "finance": "business",
            "current_affairs": "general",
        }

        if requested_category == "all":
            categories = category_map.keys()
        else:
            if requested_category not in category_map:
                self.stdout.write(
                    self.style.ERROR(
                        "Invalid category."
                    )
                )
                return

            categories = [requested_category]

        external_publisher, _ = Publisher.objects.get_or_create(
            name="External News Sources",
            defaults={
                "description": "Live external news aggregation source.",
                "website": "https://newsapi.org",
            },
        )

        total_created = 0
        total_updated = 0

        for category in categories:

            newsapi_category = category_map[category]

            response = requests.get(
                "https://newsapi.org/v2/top-headlines",
                params={
                    "apiKey": settings.NEWS_API_KEY,
                    "country": "za",
                    "category": newsapi_category,
                    "pageSize": 12,
                },
                timeout=20,
            )

            if response.status_code != 200:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed to fetch {category}: {response.text}"
                    )
                )
                continue

            data = response.json()

            fetched_articles = data.get("articles", [])

            for item in fetched_articles:

                title = item.get("title") or ""
                description = item.get("description") or ""
                url = item.get("url") or ""
                image_url = item.get("urlToImage") or ""

                source = item.get("source") or {}
                source_name = source.get("name") or "External Source"

                published_at = None

                if item.get("publishedAt"):
                    published_at = parse_datetime(
                        item.get("publishedAt")
                    )

                if not title or not url:
                    continue

                article, created = Article.objects.update_or_create(
                    external_url=url,
                    defaults={
                        "title": title[:255],
                        "category": category,
                        "article_type": Article.AGGREGATED,
                        "summary": description,
                        "content": description,
                        "author": None,
                        "publisher": external_publisher,
                        "approved": True,
                        "source_name": source_name,
                        "external_image_url": image_url,
                        "published_at": published_at,
                    },
                )

                if created:
                    total_created += 1
                else:
                    total_updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"News fetch complete. Created: {total_created}, Updated: {total_updated}"
            )
        )
