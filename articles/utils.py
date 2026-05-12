import requests

from django.conf import settings
from django.core.mail import send_mail


def get_article_subscriber_emails(article):
    subscriber_emails = set()

    if article.publisher:
        publisher_subscribers = article.publisher.subscribers.all()

        for subscriber in publisher_subscribers:
            if subscriber.email:
                subscriber_emails.add(subscriber.email)

    journalist_subscribers = article.author.journalist_subscribers.all()

    for subscriber in journalist_subscribers:
        if subscriber.email:
            subscriber_emails.add(subscriber.email)

    return list(subscriber_emails)


def email_article_to_subscribers(article):
    recipient_list = get_article_subscriber_emails(article)

    if not recipient_list:
        return 0

    subject = f"New article approved: {article.title}"

    message = f"""
Hello,

A new article has been published on Ntando's News.

Title: {article.title}
Author: {article.author.username}

Summary:
{article.summary}

Read it on Ntando's News.

Regards,
Ntando's News Team
"""

    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        fail_silently=True,
    )


def post_article_to_x(article):
    if not settings.X_BEARER_TOKEN:
        return False

    headers = {
        "Authorization": f"Bearer {settings.X_BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "text": f"New on Ntando's News: {article.title}"
    }

    try:
        response = requests.post(
            settings.X_API_URL,
            headers=headers,
            json=payload,
            timeout=10,
        )

        return response.status_code in [200, 201]
    except requests.RequestException:
        return False
