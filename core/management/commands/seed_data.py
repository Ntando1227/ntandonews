from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta

from accounts.models import CustomUser
from publishers.models import Publisher
from articles.models import Article


class Command(BaseCommand):
    help = "Seed Ntando News database with all articles"

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
            ("Thatcorporategent Speaks on South Africa Massive Concert Wave in 2026", "current_affairs", "Thatcorporategent says South Africa concert culture is beautiful but financially dangerous.", """South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory, with concerts, music festivals, and large scale live events continuing to dominate social conversations across the country.

From amapiano spectacles to international headline acts, music lovers say 2026 has already delivered an overwhelming number of events, forcing many fans to make difficult financial and emotional decisions.

Among those commenting on the trend is Thatcorporategent, who described the current entertainment landscape as beautiful but financially dangerous.

Every second weekend there is another event people suddenly need to attend, Thatcorporategent joked. South Africans are fighting for their lives financially.

Fans have especially highlighted the excitement surrounding events such as Samthing Soweto's Good Morning Live, Once Upon a Time, Scorpion Kings, and J Cole.

According to Thatcorporategent, the surge in concerts reflects something deeper than entertainment alone.

People want experiences now, he explained. After years of stress, uncertainty, and constantly being online, live music feels important again.

We may not recover financially, but at least the vibes will be immaculate."""),

            ("Ntando Mtimkulu Speaks on South Africa Massive Concert Wave in 2026", "current_affairs", "Ntando Mtimkulu says South Africans are chasing live experiences despite financial pressure.", """South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory.

Among those commenting on the trend is Ntando Mtimkulu, who described the current entertainment landscape as beautiful but financially dangerous.

Every second weekend there is another event people suddenly need to attend, Ntando joked. South Africans are fighting for their lives financially.

According to Ntando, the surge in concerts reflects something deeper than entertainment alone. People want experiences now.

Ntando also noted the growing cultural significance of South African live music spaces, particularly within amapiano culture.

It is not just about the music anymore, he said. It is community, energy, aesthetics, memories, everything."""),

            ("Concerned Citizens Continue Closely Watching Developments Around the Madlanga Commission", "politics", "South Africans continue following developments around the Madlanga Commission.", """Public discussion surrounding the Madlanga Commission continues to grow as South Africans follow ongoing developments, testimonies, and political reactions linked to the commission work.

Across social media platforms, radio discussions, and public forums, many citizens say they are paying close attention to the proceedings.

People are tired of hearing about corruption, dysfunction, and political conflict, one concerned citizen explained. But many still want to believe accountability is possible.

Observers say public interest comes from broader concerns about leadership, transparency, and the effectiveness of institutions in South Africa.

As the commission continues its work, many South Africans remain hopeful that the process will contribute toward accountability and renewed public confidence."""),

            ("Why Everyone Thinks They Can Start a Podcast", "current_affairs", "Podcast culture among young people continues growing rapidly.", """In what experts are now calling a global microphone epidemic, increasing numbers of young people are reportedly becoming convinced that they possess the exact combination of charisma, wisdom, and internet presence required to successfully host a podcast.

Across campuses, coffee shops, and friend groups, discussions about starting a podcast have reached unprecedented levels.

According to several students interviewed, almost every social circle now contains at least one person who has either started a podcast, planned a podcast, or spoken about starting a podcast for over two years without recording a single episode.

It usually starts after one deep conversation at 1am, one student explained. Suddenly someone says, Honestly, we should start a podcast.

People think having opinions is the same thing as having a podcast, one observer joked.

Until then, millions of imaginary podcasts remain trapped inside Notes app drafts, unfinished logos, and voice notes beginning with: Bro trust me, this could actually blow up."""),

            ("NBA Playoffs 2026 Continue Destroying Sleep Schedules Worldwide", "sports", "Basketball fans worldwide continue sacrificing sleep during the playoffs.", """As the 2026 NBA Playoffs intensify, basketball fans across the globe are reportedly suffering from exhaustion, emotional instability, and dangerously inconsistent sleeping patterns.

Students and working professionals alike have admitted to making increasingly irresponsible decisions in order to watch playoff games.

I told myself I would only watch the first quarter, one fan explained. Next thing I knew it was 4am and I was emotionally invested in a twelve point comeback.

Analysts say the playoffs have delivered drama, trash talk, heartbreak, superstar performances, and social media chaos.

Despite the emotional damage, fans continue returning night after night. This is peak basketball, one exhausted fan admitted."""),

            ("South Africa Unemployment Crisis Continues to Weigh Heavily on Young People", "finance", "Youth unemployment remains one of South Africa biggest concerns.", """South Africa unemployment crisis remains one of the country biggest social and economic challenges, with millions of citizens, particularly young people, continuing to struggle to find stable work opportunities.

The country official unemployment rate has increased, and youth unemployment remains especially concerning.

Speaking on the issue, Ntando Mtimkulu described unemployment as the defining challenge facing the current generation.

You cannot have millions of ambitious young people with no opportunities and expect society to remain stable, Ntando said.

Despite the grim outlook, Mtimkulu remains optimistic that entrepreneurship, digital innovation, and skills development could create new opportunities."""),

            ("The Rise of Ntando Mtimkulu: The Next Big Force in the Commercial World", "finance", "Ntando Mtimkulu is positioning himself as one of South Africa promising young commercial minds.", """In a world increasingly shaped by innovation, adaptability, and visionary leadership, one young South African name is beginning to stand out above the rest: Ntando Mtimkulu.

Known among peers for his ambition, sharp commercial instincts, and relentless drive for excellence, Ntando is rapidly positioning himself as one of the most promising young minds in business and enterprise development.

He built his academic foundation at Rhodes University and later pursued a Postgraduate Diploma in Enterprise Management.

Observers describe him as a commercial juggernaut in the making, someone capable of bridging business, technology, culture, and modern African enterprise.

While his journey is still unfolding, one thing is becoming clear: the name Ntando Mtimkulu is one the commercial world may soon find impossible to ignore."""),

            ("Ntando Mtimkulu Left Devastated as Arsenal Close In on League Glory", "sports", "Liverpool supporter Ntando Mtimkulu is reportedly struggling with Arsenal title charge.", """For many football supporters, the closing weeks of the season bring excitement, hope, and celebration. But for Ntando Mtimkulu, this season has reportedly delivered frustration, disbelief, and emotional damage.

The outspoken Liverpool supporter has allegedly struggled to come to terms with the possibility of Arsenal lifting the league title.

Every week he keeps saying they will bottle it, one friend reportedly said. And every week Arsenal somehow win again.

Sources suggest his patience with new Liverpool manager Arne Slot has already worn dangerously thin.

He misses Klopp football, another source joked. Every conversation somehow ends with him saying Klopp would never allow this.

If Arsenal actually win the league, friends say nobody should expect him to answer football messages for at least a month."""),

            ("Mystery Romance? Ntando Mtimkulu Reportedly in Long Distance Relationship With Freckles", "current_affairs", "Speculation continues around Ntando relationship with Freckles.", """Social circles close to Ntando Mtimkulu have recently been buzzing with speculation surrounding what many are calling his most mysterious chapter yet, a long distance relationship with a woman known only as Freckles.

While neither Ntando nor the mystery woman has publicly confirmed the relationship, insiders claim the connection has quietly become one of the most talked about topics among friends.

Described as deep, intense, and surprisingly wholesome, the relationship reportedly thrives despite the distance.

There is business Ntando, one friend joked, and then there is Freckles Ntando.

Whether the mystery surrounding Freckles will ever fully be revealed remains unknown."""),

            ("Freckles Counting Down the Days Until the Next A Court of Thorns and Roses Release", "current_affairs", "Freckles is reportedly preparing emotionally for the next ACOTAR release.", """Excitement is reportedly reaching dangerous levels within the reading community as fans of A Court of Thorns and Roses continue speculating about the next release connected to the fantasy universe created by Sarah J Maas.

Among the most emotionally invested fans is the mysterious Freckles, the long distance love interest frequently associated with Ntando Mtimkulu.

Friends claim Freckles has become completely unbearable whenever discussions about the series arise.

She genuinely talks about those books like they are historical events, one source joked.

Ntando has reportedly accepted that when the new book drops, communication may temporarily decrease because Freckles will disappear into Prythian."""),

            ("Ntando Mtimkulu Reportedly Loses Patience During Flat Earth Debate", "current_affairs", "Flat earth debate reportedly pushed Ntando Mtimkulu to the edge.", """What began as a casual late night conversation among friends quickly descended into chaos after the topic of flat earth theories was introduced.

Sources claim Ntando initially assumed the statement was a joke. Then he realized the person was serious.

Friends say he attempted to remain respectful at first, but the conversation became difficult after theories involving Antarctica, NASA, and hidden truths were introduced.

At one point Ntando just stared at the ceiling in silence, another source recalled. You could literally see him questioning humanity.

He has since vowed to avoid future flat earth debates unless professional astronomers are present."""),

            ("Ntando Mtimkulu Says Internet Debates Between Believers and Skeptics Have Gone Completely Off the Rails", "current_affairs", "Internet philosophical debates reportedly continue exhausting everyone involved.", """According to close friends of Ntando Mtimkulu, one of his favorite forms of online entertainment has become watching philosophical arguments spiral completely out of control on social media.

The Rhodes University graduate reportedly spent several hours observing a heated debate between religious users, skeptics, amateur philosophers, and random podcast fans.

One person was quoting philosophy. Another was posting science articles. Somebody else brought up ancient history for no reason. It was chaos.

Friends say Ntando later joked that modern internet debates often involve extreme confidence with absolutely no intention of listening.

He concluded that the internet may have given society too much access to microphones and not enough access to humility."""),

            ("Ntando Mtimkulu Says He Is Concerned But Calm Amid Growing Hantavirus Discussions", "politics", "Ntando reportedly takes a cautiously confident approach to Hantavirus discussions.", """As conversations surrounding Hantavirus continue circulating online and across global health discussions, Ntando Mtimkulu has reportedly adopted what friends describe as a cautiously confident approach.

Sources close to Mtimkulu say he has spent recent weeks keeping informed while encouraging those around him not to panic unnecessarily.

He is nervous, obviously, one friend said. But he also keeps telling people that fear without information helps nobody.

Known for his analytical mindset and calm demeanor under pressure, Ntando has approached the topic with concern and practicality.

He remains optimistic and focused on long term goals while continuing to monitor public discussion."""),

            ("Ntando Mtimkulu Allegedly Believes He Could Run a Fortune 500 Company Tomorrow", "finance", "Friends joke that Ntando confidence has reached dangerous levels.", """Friends of Ntando Mtimkulu have jokingly accused him of possessing dangerous levels of confidence after he reportedly claimed he could successfully run a Fortune 500 company if given the opportunity.

The statement was allegedly made during a casual late night discussion about business leadership.

He genuinely started explaining restructuring strategies like the board had already hired him, one source laughed.

Known for his passion for enterprise management and commercial strategy, Ntando reportedly spends hours studying business models and global corporate structures.

He talks big, one friend admitted, but the scary thing is that he has usually thought things through."""),

            ("The Spotify Sessions: Ntando Mtimkulu Music Taste Sparks Heated Debate", "current_affairs", "Friends are divided over Ntando unpredictable music rotation.", """A fierce debate has reportedly broken out among friends of Ntando Mtimkulu after several people questioned his increasingly unpredictable music rotation.

While Ntando is known for having a deep appreciation for music, insiders claim his playlists have recently become emotionally confusing.

One minute it is deep lyrical rap. The next minute it is heartbreak music, then jazz, then aggressive gym music.

Friends suspect the mysterious influence of Freckles may be partially responsible for the shift.

Despite the criticism, Ntando reportedly defends his playlists passionately, arguing that music should reflect every version of who you are."""),

            ("Ntando Mtimkulu Reportedly Preparing for Unmatched Greatness Era", "current_affairs", "Friends say Ntando has entered a new period of discipline and ambition.", """Close associates of Ntando Mtimkulu say he has recently entered what he privately refers to as his Unmatched Greatness Era.

While the phrase has confused many around him, friends claim it refers to a new period of discipline, ambition, and personal reinvention.

He talks like he is in a sports documentary now, one friend joked.

Sources say the phase includes stricter routines, clearer career goals, improved fitness habits, and a renewed focus on long term success.

Whether exaggerated or not, those closest to Ntando admit one thing: his confidence is extremely difficult to ignore."""),
        ]

        for index, (title, category, summary, content) in enumerate(articles):
            Article.objects.update_or_create(
                title=title,
                defaults={
                    "summary": summary,
                    "content": content,
                    "category": category,
                    "article_type": "internal",
                    "publisher": publisher,
                    "author": journalist,
                    "approved": True,
                    "published_at": timezone.now() - timedelta(days=index),
                },
            )

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(articles)} articles successfully."))
