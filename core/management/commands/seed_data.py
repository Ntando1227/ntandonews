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
                "summary": "Thatcorporategent says South Africa concert culture is beautiful but financially dangerous.",
                "content": """South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory, with concerts, music festivals, and large scale live events continuing to dominate social conversations across the country.

From amapiano spectacles to international headline acts, music lovers say 2026 has already delivered an overwhelming number of events, forcing many fans to make difficult financial and emotional decisions.

Among those commenting on the trend is Thatcorporategent, who described the current entertainment landscape as beautiful but financially dangerous.

Every second weekend there is another event people suddenly need to attend, Thatcorporategent joked. South Africans are fighting for their lives financially.

Fans have especially highlighted the excitement surrounding events such as Samthing Soweto's Good Morning Live, the highly anticipated Once Upon a Time experience, performances from the legendary Scorpion Kings, and growing discussions surrounding international artists like J Cole potentially connecting with South African audiences once again.

According to Thatcorporategent, the surge in concerts reflects something deeper than entertainment alone.

People want experiences now, he explained. After years of stress, uncertainty, and constantly being online, live music feels important again.

Social media timelines have reportedly become flooded with concert outfit discussions, ticket complaints, accommodation planning, and emotionally charged debates about which events are actually worth attending.

Sources claim many young South Africans are currently operating under what economists may soon classify as concert season delusion, where individuals knowingly ignore their budgets in exchange for temporary happiness.

People are buying tickets first and asking financial questions later, one observer laughed.

Thatcorporategent also noted the growing cultural significance of South African live music spaces, particularly within amapiano culture, where concerts have increasingly become social experiences tied to identity, fashion, and youth culture.

It is not just about the music anymore, he said. It is community, energy, aesthetics, memories, everything.

Still, not everybody is surviving the experience comfortably. Fans online continue expressing concern over rising ticket prices, travel costs, and the emotional damage caused by sold out events.

There is nothing more painful than seeing Tickets Sold Out while waiting for payday, one fan admitted.

Despite the financial pressure, excitement surrounding the country music scene shows no signs of slowing down. With more events expected later in the year, many South Africans are already preparing themselves mentally, emotionally, and financially for another chaotic concert season.

As one concerned music fan summarized: We may not recover financially, but at least the vibes will be immaculate.""",
            },
            {
                "title": "Ntando Mtimkulu Speaks on South Africa Massive Concert Wave in 2026",
                "category": "current_affairs",
                "summary": "Ntando Mtimkulu says South Africans are chasing live experiences despite financial pressure.",
                "content": """South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory, with concerts, music festivals, and large scale live events continuing to dominate social conversations across the country.

From amapiano spectacles to international headline acts, music lovers say 2026 has already delivered an overwhelming number of events, forcing many fans to make difficult financial and emotional decisions.

Among those commenting on the trend is Ntando Mtimkulu, who described the current entertainment landscape as beautiful but financially dangerous.

Every second weekend there is another event people suddenly need to attend, Ntando joked. South Africans are fighting for their lives financially.

Fans have especially highlighted the excitement surrounding events such as Samthing Soweto's Good Morning Live, the highly anticipated Once Upon a Time experience, performances from the legendary Scorpion Kings, and growing discussions surrounding international artists like J Cole potentially connecting with South African audiences once again.

According to Ntando, the surge in concerts reflects something deeper than entertainment alone.

People want experiences now, he explained. After years of stress, uncertainty, and constantly being online, live music feels important again.

Social media timelines have reportedly become flooded with concert outfit discussions, ticket complaints, accommodation planning, and emotionally charged debates about which events are actually worth attending.

Sources claim many young South Africans are currently operating under what economists may soon classify as concert season delusion, where individuals knowingly ignore their budgets in exchange for temporary happiness.

People are buying tickets first and asking financial questions later, one observer laughed.

Ntando also noted the growing cultural significance of South African live music spaces, particularly within amapiano culture, where concerts have increasingly become social experiences tied to identity, fashion, and youth culture.

It is not just about the music anymore, he said. It is community, energy, aesthetics, memories, everything.

Still, not everybody is surviving the experience comfortably. Fans online continue expressing concern over rising ticket prices, travel costs, and the emotional damage caused by sold out events.

There is nothing more painful than seeing Tickets Sold Out while waiting for payday, one fan admitted.

Despite the financial pressure, excitement surrounding the country music scene shows no signs of slowing down. With more events expected later in the year, many South Africans are already preparing themselves mentally, emotionally, and financially for another chaotic concert season.

As one concerned music fan summarized: We may not recover financially, but at least the vibes will be immaculate.""",
            },
            {
                "title": "Concerned Citizens Continue Closely Watching Developments Around the Madlanga Commission",
                "category": "politics",
                "summary": "South Africans continue following developments around the Madlanga Commission.",
                "content": """Public discussion surrounding the Madlanga Commission continues to grow as South Africans follow ongoing developments, testimonies, and political reactions linked to the commission work.

Across social media platforms, radio discussions, and public forums, many citizens say they are paying close attention to the proceedings, viewing them as an important reflection of accountability, governance, and public trust within the country.

One self described concerned citizen said the situation has left many South Africans feeling both frustrated and cautiously hopeful.

People are tired of hearing about corruption, dysfunction, and political conflict, the citizen explained. But at the same time, many still want to believe accountability is possible.

Observers say much of the public interest surrounding the commission comes from broader concerns about leadership, transparency, and the effectiveness of institutions in South Africa. Citizens online have repeatedly expressed frustration about recurring scandals and controversies dominating national discourse.

There is a growing feeling that ordinary people are carrying the weight of problems created by powerful individuals, another concerned observer commented.

Political analysts note that commissions of inquiry often become major moments of national attention because they reveal not only legal or administrative issues, but also deeper social frustrations surrounding inequality, unemployment, governance, and economic pressure.

For younger South Africans especially, discussions around the commission reportedly reflect a wider concern about the future of the country and confidence in public systems.

People want stability, one university student explained. They want to believe institutions still matter.

Despite the seriousness of the proceedings, South Africans online have continued responding in their usual fashion: through memes, debates, dramatic commentary, and highly emotional WhatsApp voice notes.

Sources claim many citizens now spend evenings alternating between watching commission updates and scrolling through social media reactions trying to understand the latest developments.

Still, experts say public engagement remains important.

Whether people agree or disagree politically, civic awareness matters, one commentator said. The fact that citizens are paying attention at all is significant.

As the commission continues its work, many South Africans remain hopeful that the process will ultimately contribute toward greater accountability, stronger governance, and renewed public confidence in democratic institutions.""",
            },
            {
                "title": "Why Everyone Thinks They Can Start a Podcast",
                "category": "current_affairs",
                "summary": "Podcast culture among young people continues growing rapidly.",
                "content": """In what experts are now calling a global microphone epidemic, increasing numbers of young people are reportedly becoming convinced that they possess the exact combination of charisma, wisdom, and internet presence required to successfully host a podcast.

Across campuses, coffee shops, and friend groups, discussions about starting a podcast have reached unprecedented levels, with many people allegedly believing that purchasing a microphone automatically transforms them into cultural commentators.

According to several students interviewed, almost every social circle now contains at least one person who has either started a podcast, planned a podcast, or spoken about starting a podcast for over two years without recording a single episode.

It usually starts after one deep conversation at 1am, one student explained. Suddenly someone says, Honestly, we should start a podcast.

Experts say podcast ideas often emerge immediately after discussions about relationships, motivation, business, gym culture, or the state of society.

Friends also report that podcast enthusiasm tends to peak shortly after someone watches clips from successful online creators and becomes convinced they, too, could discuss life while seated in LED lighting for an hour.

People think having opinions is the same thing as having a podcast, one observer joked.

Sources claim the average podcast planning session includes choosing a name, discussing aesthetics, imagining sponsorships, debating camera angles, and absolutely no actual recording.

One student admitted that his group has redesigned their imaginary podcast studio at least fourteen times despite never filming an episode.

Internet culture analysts say the popularity of podcasts reflects a larger desire among young people to express themselves publicly, build communities, and feel heard in an increasingly online world.

People want connection, one communications student explained. Also attention. But mostly connection.

Still, listeners say many podcasts unfortunately suffer from what experts describe as excessive confidence with minimal structure.

There are only so many times you can hear four people discussing mindset before losing consciousness, one listener admitted.

Despite the criticism, podcast culture continues growing rapidly, especially among students and young professionals hoping to build personal brands, discuss pop culture, or simply document conversations with friends.

Some podcasts have even become surprisingly successful, proving that while many ideas never leave the group chat, a few eventually develop real audiences.

Until then, however, millions of imaginary podcasts remain trapped inside Notes app drafts, unfinished logos, and voice notes beginning with: Bro trust me, this could actually blow up.""",
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

        self.stdout.write(self.style.SUCCESS("Ntando News database seeded successfully."))
