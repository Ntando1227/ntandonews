from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import CustomUser
from articles.models import Article
from newsletters.models import Newsletter
from publishers.models import Publisher


class NewsApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.reader = CustomUser.objects.create_user(
            username="reader",
            email="reader@test.com",
            password="testpass123",
            role="reader",
        )

        self.journalist = CustomUser.objects.create_user(
            username="journalist",
            email="journalist@test.com",
            password="testpass123",
            role="journalist",
        )

        self.editor = CustomUser.objects.create_user(
            username="editor",
            email="editor@test.com",
            password="testpass123",
            role="editor",
        )

        self.publisher = Publisher.objects.create(
            name="Ntando Daily",
            description="Daily publisher for Ntando's News",
        )

        self.reader.subscribed_publishers.add(self.publisher)
        self.reader.subscribed_journalists.add(self.journalist)

        self.approved_article = Article.objects.create(
            title="Approved Article",
            summary="Approved summary",
            content="Approved content",
            author=self.journalist,
            publisher=self.publisher,
            approved=True,
        )

        self.unapproved_article = Article.objects.create(
            title="Pending Article",
            summary="Pending summary",
            content="Pending content",
            author=self.journalist,
            publisher=self.publisher,
            approved=False,
        )

    def test_public_can_view_only_approved_articles(self):
        response = self.client.get("/api/articles/")

        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data]

        self.assertIn("Approved Article", titles)
        self.assertNotIn("Pending Article", titles)

    def test_reader_can_view_subscribed_articles(self):
        self.client.force_authenticate(user=self.reader)

        response = self.client.get("/api/articles/subscribed/")

        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data]

        self.assertIn("Approved Article", titles)
        self.assertNotIn("Pending Article", titles)

    def test_journalist_can_create_article(self):
        self.client.force_authenticate(user=self.journalist)

        data = {
            "title": "Journalist Created Article",
            "summary": "Created through API",
            "content": "Full API article content",
            "publisher": self.publisher.id,
        }

        response = self.client.post("/api/articles/", data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Article.objects.filter(title="Journalist Created Article").count(), 1)

        article = Article.objects.get(title="Journalist Created Article")
        self.assertEqual(article.author, self.journalist)
        self.assertFalse(article.approved)

    def test_reader_cannot_create_article(self):
        self.client.force_authenticate(user=self.reader)

        data = {
            "title": "Reader Article",
            "summary": "Should fail",
            "content": "Readers cannot create articles",
            "publisher": self.publisher.id,
        }

        response = self.client.post("/api/articles/", data)

        self.assertEqual(response.status_code, 403)

    def test_editor_can_delete_article(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.delete(f"/api/articles/{self.approved_article.id}/")

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Article.objects.filter(id=self.approved_article.id).exists())

    def test_newsletter_can_be_created_by_authenticated_user(self):
        self.client.force_authenticate(user=self.journalist)

        data = {
            "title": "Weekly Roundup",
            "description": "Best stories of the week",
        }

        response = self.client.post("/api/newsletters/", data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Newsletter.objects.filter(title="Weekly Roundup").count(), 1)

    @patch("articles.utils.send_mail")
    @patch("articles.utils.requests.post")
    def test_article_approval_triggers_email_and_x_logic(self, mock_post, mock_send_mail):
        mock_post.return_value.status_code = 201
        mock_send_mail.return_value = 1

        self.unapproved_article.approved = True
        self.unapproved_article.save()

        self.assertTrue(mock_send_mail.called)
