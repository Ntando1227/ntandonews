from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta

from accounts.models import CustomUser
from publishers.models import Publisher
from articles.models import Article


class Command(BaseCommand):

    help = "Seed Ntando News database"


    def handle(self, *args, **kwargs):

        self.stdout.write("Seeding Ntando News database...")


        journalist, _ = CustomUser.objects.update_or_create(
            username="Ntando",
            defaults={
                "email": "ntando@example.com",
                "role": "journalist",
                "is_staff": True,
                "is_superuser": True,
                "password": make_password("Mtimkulu"),
            },
        )

        editor, _ = CustomUser.objects.update_or_create(
            username="NtandoM",
            defaults={
                "email": "editor@example.com",
                "role": "editor",
                "is_staff": True,
                "password": make_password("Mtimkulu"),
            },
        )

        reader, _ = CustomUser.objects.update_or_create(
            username="Reader1",
            defaults={
                "email": "reader@example.com",
                "role": "reader",
                "password": make_password("reader123"),
            },
        )


        publisher, _ = Publisher.objects.get_or_create(
            name="Ntando News",
            defaults={
                "description": "South African digital news and culture platform",
                "website": "https://ntandonews.onrender.com",
            },
        )


        articles = [

            {
                "title": "Thatcorporategent Speaks on South Africa Massive Concert Wave in 2026",
                "category": "current_affairs",
                "summary": "South African concert culture continues exploding in 2026.",
                "content": "South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory. Concerts, music festivals, and large scale live events continue dominating social conversations across the country. Fans say 2026 has already delivered an overwhelming number of concerts and experiences. Many young South Africans are reportedly ignoring their budgets in exchange for unforgettable experiences and immaculate vibes.",
            },

            {
                "title": "Ntando Mtimkulu Speaks on South Africa Massive Concert Wave in 2026",
                "category": "current_affairs",
                "summary": "Ntando Mtimkulu says South Africa concert culture reflects a deeper need for experiences and connection.",
                "content": "South Africa entertainment landscape continues expanding rapidly as concerts and festivals dominate social media timelines. Ntando Mtimkulu says people now value experiences, energy, and memories more than ever before. Fans online continue debating ticket prices, sold out events, and whether surviving concert season financially is still possible.",
            },

            {
                "title": "Concerned Citizens Continue Closely Watching Developments Around the Madlanga Commission",
                "category": "politics",
                "summary": "Public interest surrounding the Madlanga Commission continues growing.",
                "content": "South Africans continue closely following developments surrounding the Madlanga Commission. Citizens say accountability, governance, and public trust remain major concerns. Discussions online continue ranging from serious political analysis to emotionally charged WhatsApp voice notes and social media debates.",
            },

            {
                "title": "Why Everyone Thinks They Can Start a Podcast",
                "category": "current_affairs",
                "summary": "Podcast culture among young people continues growing rapidly.",
                "content": "Experts are now calling it a global microphone epidemic as increasing numbers of young people become convinced they possess the exact combination of charisma and internet presence required to host a successful podcast. Many groups reportedly spend more time designing logos and discussing aesthetics than actually recording episodes.",
            },

            {
                "title": "NBA Playoffs 2026 Continue Destroying Sleep Schedules Worldwide",
                "category": "sports",
                "summary": "Basketball fans worldwide continue sacrificing sleep during the playoffs.",
                "content": "As the 2026 NBA Playoffs intensify, basketball fans across the globe are reportedly suffering from exhaustion, emotional instability, and dangerously inconsistent sleeping patterns. Students and working professionals alike admit to making irresponsible decisions in order to watch playoff games late into the night.",
            },

            {
                "title": "South Africa Unemployment Crisis Continues to Weigh Heavily on Young People",
                "category": "finance",
                "summary": "Youth unemployment remains one of South Africa biggest concerns.",
                "content": "South Africa unemployment crisis remains one of the country biggest social and economic challenges, with millions of young people continuing to struggle to find stable opportunities. Analysts say the issue continues affecting confidence, long term planning, and economic growth.",
            },

            {
                "title": "The Rise of Ntando Mtimkulu: The Next Big Force in the Commercial World",
                "category": "finance",
                "summary": "Observers say Ntando Mtimkulu continues positioning himself as a future commercial leader.",
                "content": "Known among peers for ambition, sharp commercial instincts, and relentless drive for excellence, Ntando Mtimkulu is rapidly positioning himself as one of the most promising young minds in enterprise development and modern business strategy.",
            },

            {
                "title": "Ntando Mtimkulu Left Devastated as Arsenal Close In on League Glory",
                "category": "sports",
                "summary": "Liverpool supporter Ntando Mtimkulu reportedly struggling emotionally as Arsenal edge closer to league success.",
                "content": "Friends say Ntando Mtimkulu has found recent football developments emotionally exhausting as Arsenal continue pushing toward league glory. Sources claim he misses Klopp football and now approaches football debates with visible stress and caution.",
            },

            {
                "title": "Mystery Romance? Ntando Mtimkulu Reportedly in Long Distance Relationship With Freckles",
                "category": "current_affairs",
                "summary": "Sources claim Ntando Mtimkulu relationship with Freckles continues drawing attention online.",
                "content": "Friends say the relationship between Ntando Mtimkulu and the mysterious Freckles has quietly become one of the most talked about stories within their social circles. Sources claim the pair continue bonding through playlists, movie nights, memes, and late night calls.",
            },

            {
                "title": "Freckles Counting Down the Days Until the Next A Court of Thorns and Roses Release",
                "category": "current_affairs",
                "summary": "Freckles reportedly preparing emotionally for the next ACOTAR release.",
                "content": "Excitement surrounding the A Court of Thorns and Roses universe continues growing among fantasy readers. Sources claim Freckles has already begun mentally preparing for the next release while Ntando Mtimkulu continues trying to survive increasingly detailed ACOTAR discussions.",
            },

            {
                "title": "Ntando Mtimkulu Reportedly Loses Patience During Flat Earth Debate",
                "category": "current_affairs",
                "summary": "Flat earth debate reportedly pushed Ntando Mtimkulu to the edge.",
                "content": "Sources say Ntando Mtimkulu struggled to remain calm after unexpectedly entering a late night flat earth debate involving conspiracy theories, Antarctica discussions, and increasingly confusing arguments about gravity and airplanes.",
            },

            {
                "title": "Ntando Mtimkulu Says Internet Debates Between Believers and Skeptics Have Gone Completely Off the Rails",
                "category": "current_affairs",
                "summary": "Internet philosophical debates reportedly continue exhausting everyone involved.",
                "content": "Ntando Mtimkulu reportedly spent several hours observing a chaotic online debate involving religion, skepticism, philosophy, podcasts, science, and people using words like objective reality far too confidently.",
            },

        ]


        for index, item in enumerate(articles):

            Article.objects.update_or_create(
                title=item["title"],
                defaults={
                    "summary": item["summary"],
                    "content": item["content"],
                    "category": item["category"],
                    "article_type": "internal",
                    "publisher": publisher,
                    "author": journalist,
                    "approved": True,
                    "published_at": timezone.now() - timedelta(days=index),
                },
            )


        self.stdout.write(
            self.style.SUCCESS("Ntando News database seeded successfully.")
        )
