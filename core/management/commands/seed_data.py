from django.core.management.base import BaseCommand

from accounts.models import CustomUser
from articles.models import Article
from newsletters.models import Newsletter
from publishers.models import Publisher


class Command(BaseCommand):
    help = "Create sample data for Ntando's News."

    def handle(self, *args, **options):

        journalist, _ = CustomUser.objects.get_or_create(
            username="Ntando",
            defaults={
                "email": "journalist@ntandosnews.local",
                "role": "journalist",
            },
        )
        journalist.set_password("Mtimkulu")
        journalist.role = "journalist"
        journalist.save()

        editor, _ = CustomUser.objects.get_or_create(
            username="NtandoM",
            defaults={
                "email": "editor@ntandosnews.local",
                "role": "editor",
            },
        )
        editor.set_password("Mtimkulu")
        editor.role = "editor"
        editor.save()

        reader, _ = CustomUser.objects.get_or_create(
            username="Reader1",
            defaults={
                "email": "reader@ntandosnews.local",
                "role": "reader",
            },
        )
        reader.set_password("reader123")
        reader.role = "reader"
        reader.save()

        publisher, _ = Publisher.objects.get_or_create(
            name="Ntando Daily",
            defaults={
                "description": "A bold South African digital publication covering sports, politics, finance, and public life.",
                "website": "https://example.com",
            },
        )

        publisher.journalists.add(journalist)
        publisher.editors.add(editor)

        reader.subscribed_publishers.add(publisher)
        reader.subscribed_journalists.add(journalist)

        articles = [
            {
                "title": "Bafana Bafana Build Momentum Ahead of Continental Test",
                "category": "sports",
                "summary": "South African football fans are hopeful as the national team shows stronger discipline and attacking confidence.",
                "content": "Bafana Bafana are entering an important period with renewed belief from supporters. The squad has shown better structure, improved pressing, and a stronger attacking identity. For many fans, the current momentum reflects a team beginning to understand its rhythm and potential.",
            },
            {
                "title": "Local Rugby Academies Invest in Township Talent",
                "category": "sports",
                "summary": "Development programmes are creating new pathways for young rugby players from underrepresented communities.",
                "content": "Across South Africa, rugby academies are increasing their focus on township and rural talent. Coaches say the next generation of players needs access to facilities, mentorship, nutrition, and competitive fixtures. These investments could reshape the future of South African rugby.",
            },
            {
                "title": "Parliament Faces Pressure Over Service Delivery Promises",
                "category": "politics",
                "summary": "Communities are demanding clearer timelines, stronger accountability, and visible improvements from elected leaders.",
                "content": "Service delivery remains one of South Africa's most urgent political issues. Citizens are calling for transparent planning, honest reporting, and measurable progress. Analysts argue that public trust depends on whether leaders can convert campaign promises into practical results.",
            },
            {
                "title": "Youth Voices Push for Greater Political Accountability",
                "category": "politics",
                "summary": "Young South Africans are increasingly using digital platforms to question leadership and demand policy clarity.",
                "content": "South African youth are becoming more vocal in political conversations. Through social media, community forums, and civic organisations, young people are challenging leaders to explain decisions, publish results, and engage meaningfully with voters beyond election seasons.",
            },
            {
                "title": "Rand Stability Gives Businesses Room to Plan",
                "category": "finance",
                "summary": "Small businesses are watching currency movements closely as they manage imports, pricing, and cash flow.",
                "content": "Currency stability is important for South African businesses that rely on imported goods or international suppliers. While uncertainty remains, periods of rand stability allow entrepreneurs to plan stock purchases, manage prices, and protect profit margins.",
            },
            {
                "title": "Township Entrepreneurs Turn Side Hustles into Formal Businesses",
                "category": "finance",
                "summary": "More informal traders are registering businesses, using digital payments, and exploring new funding opportunities.",
                "content": "Township entrepreneurship continues to evolve as small business owners adopt digital tools and formal structures. From food services to clothing, delivery, cleaning, and online retail, entrepreneurs are building businesses that respond directly to local demand.",
            },
        ]

        created_articles = []

        for item in articles:
            article, _ = Article.objects.update_or_create(
                title=item["title"],
                defaults={
                    "category": item["category"],
                    "summary": item["summary"],
                    "content": item["content"],
                    "author": journalist,
                    "publisher": publisher,
                    "approved": True,
                },
            )
            created_articles.append(article)

        newsletter, _ = Newsletter.objects.get_or_create(
            title="Ntando Weekly Briefing",
            defaults={
                "description": "A curated weekly briefing covering South African sports, politics, and finance.",
                "author": journalist,
            },
        )

        newsletter.articles.set(created_articles)

        self.stdout.write(self.style.SUCCESS("Sample data created successfully."))
        self.stdout.write("Journalist Login: Ntando / Mtimkulu")
        self.stdout.write("Editor Login: NtandoM / Mtimkulu")
        self.stdout.write("Reader Login: Reader1 / reader123")
