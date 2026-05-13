from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta

from accounts.models import CustomUser
from publishers.models import Publisher
from articles.models import Article


class Command(BaseCommand):
    help = "Seed Ntando News database with full article bodies"

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
                "content": """
South Africa entertainment scene appears to be entering one of its busiest and most exciting periods in recent memory, with concerts, music festivals, and large scale live events continuing to dominate social conversations across the country.

From amapiano spectacles to international headline acts, music lovers say 2026 has already delivered an overwhelming number of events, forcing many fans to make difficult financial and emotional decisions.

Among those commenting on the trend is Thatcorporategent, who described the current entertainment landscape as beautiful but financially dangerous.

"Every second weekend there is another event people suddenly need to attend," Thatcorporategent joked. "South Africans are fighting for their lives financially."

Fans have especially highlighted the excitement surrounding events such as Samthing Soweto's Good Morning Live, the highly anticipated Once Upon a Time experience, performances from the legendary Scorpion Kings, and growing discussions surrounding international artists like J Cole potentially connecting with South African audiences once again.

According to Thatcorporategent, the surge in concerts reflects something deeper than entertainment alone.

"People want experiences now," he explained. "After years of stress, uncertainty, and constantly being online, live music feels important again."

Social media timelines have reportedly become flooded with concert outfit discussions, ticket complaints, accommodation planning, and emotionally charged debates about which events are actually worth attending.

Sources claim many young South Africans are currently operating under what economists may soon classify as concert season delusion, where individuals knowingly ignore their budgets in exchange for temporary happiness.

"People are buying tickets first and asking financial questions later," one observer laughed.

Thatcorporategent also noted the growing cultural significance of South African live music spaces, particularly within amapiano culture, where concerts have increasingly become social experiences tied to identity, fashion, and youth culture.

"It is not just about the music anymore," he said. "It is community, energy, aesthetics, memories, everything."

Still, not everybody is surviving the experience comfortably. Fans online continue expressing concern over rising ticket prices, travel costs, and the emotional damage caused by sold out events.

"There is nothing more painful than seeing Tickets Sold Out while waiting for payday," one fan admitted.

Despite the financial pressure, excitement surrounding the country music scene shows no signs of slowing down. With more events expected later in the year, many South Africans are already preparing themselves mentally, emotionally, and financially for another chaotic concert season.

As one concerned music fan summarized: "We may not recover financially, but at least the vibes will be immaculate."
""",
            },
            {
                "title": "Why Everyone Thinks They Can Start a Podcast",
                "category": "current_affairs",
                "summary": "Podcast culture among young people continues growing rapidly.",
                "content": """
In what experts are now calling a global microphone epidemic, increasing numbers of young people are reportedly becoming convinced that they possess the exact combination of charisma, wisdom, and internet presence required to successfully host a podcast.

Across campuses, coffee shops, and friend groups, discussions about starting a podcast have reached unprecedented levels, with many people allegedly believing that purchasing a microphone automatically transforms them into cultural commentators.

According to several students interviewed, almost every social circle now contains at least one person who has either started a podcast, planned a podcast, or spoken about starting a podcast for over two years without recording a single episode.

"It usually starts after one deep conversation at 1am," one student explained. "Suddenly someone says, Honestly, we should start a podcast."

Experts say podcast ideas often emerge immediately after discussions about relationships, motivation, business, gym culture, or the state of society.

Friends also report that podcast enthusiasm tends to peak shortly after someone watches clips from successful online creators and becomes convinced they, too, could discuss life while seated in LED lighting for an hour.

"People think having opinions is the same thing as having a podcast," one observer joked.

Sources claim the average podcast planning session includes choosing a name, discussing aesthetics, imagining sponsorships, debating camera angles, and absolutely no actual recording.

One student admitted that his group has redesigned their imaginary podcast studio at least fourteen times despite never filming an episode.

Internet culture analysts say the popularity of podcasts reflects a larger desire among young people to express themselves publicly, build communities, and feel heard in an increasingly online world.

"People want connection," one communications student explained. "Also attention. But mostly connection."

Still, listeners say many podcasts unfortunately suffer from what experts describe as excessive confidence with minimal structure.

"There are only so many times you can hear four people discussing mindset before losing consciousness," one listener admitted.

Despite the criticism, podcast culture continues growing rapidly, especially among students and young professionals hoping to build personal brands, discuss pop culture, or simply document conversations with friends.

Some podcasts have even become surprisingly successful, proving that while many ideas never leave the group chat, a few eventually develop real audiences.

Until then, however, millions of imaginary podcasts remain trapped inside Notes app drafts, unfinished logos, and voice notes beginning with: "Bro trust me, this could actually blow up."
""",
            },
            {
                "title": "Concerned Citizens Continue Closely Watching Developments Around the Madlanga Commission",
                "category": "politics",
                "summary": "South Africans continue following developments around the Madlanga Commission.",
                "content": """
Public discussion surrounding the Madlanga Commission continues to grow as South Africans follow ongoing developments, testimonies, and political reactions linked to the commission work.

Across social media platforms, radio discussions, and public forums, many citizens say they are paying close attention to the proceedings, viewing them as an important reflection of accountability, governance, and public trust within the country.

One self described concerned citizen said the situation has left many South Africans feeling both frustrated and cautiously hopeful.

"People are tired of hearing about corruption, dysfunction, and political conflict," the citizen explained. "But at the same time, many still want to believe accountability is possible."

Observers say much of the public interest surrounding the commission comes from broader concerns about leadership, transparency, and the effectiveness of institutions in South Africa. Citizens online have repeatedly expressed frustration about recurring scandals and controversies dominating national discourse.

"There is a growing feeling that ordinary people are carrying the weight of problems created by powerful individuals," another concerned observer commented.

Political analysts note that commissions of inquiry often become major moments of national attention because they reveal not only legal or administrative issues, but also deeper social frustrations surrounding inequality, unemployment, governance, and economic pressure.

For younger South Africans especially, discussions around the commission reportedly reflect a wider concern about the future of the country and confidence in public systems.

"People want stability," one university student explained. "They want to believe institutions still matter."

Despite the seriousness of the proceedings, South Africans online have continued responding in their usual fashion: through memes, debates, dramatic commentary, and highly emotional WhatsApp voice notes.

Sources claim many citizens now spend evenings alternating between watching commission updates and scrolling through social media reactions trying to understand the latest developments.

Still, experts say public engagement remains important.

"Whether people agree or disagree politically, civic awareness matters," one commentator said. "The fact that citizens are paying attention at all is significant."

As the commission continues its work, many South Africans remain hopeful that the process will ultimately contribute toward greater accountability, stronger governance, and renewed public confidence in democratic institutions.
""",
            },
            {
                "title": "NBA Playoffs 2026 Continue Destroying Sleep Schedules Worldwide",
                "category": "sports",
                "summary": "Basketball fans worldwide continue sacrificing sleep during the playoffs.",
                "content": """
As the 2026 NBA Playoffs intensify, basketball fans across the globe are reportedly suffering from exhaustion, emotional instability, and dangerously inconsistent sleeping patterns.

Students and working professionals alike have admitted to making increasingly irresponsible decisions in order to watch playoff games that begin at unreasonable hours of the night.

"I told myself I would only watch the first quarter," one fan explained. "Next thing I knew it was 4am and I was emotionally invested in a twelve point comeback."

Analysts say the 2026 playoffs have already delivered the perfect combination of drama, trash talk, heartbreak, superstar performances, and social media chaos required to completely consume basketball fans online.

According to sources, productivity levels have sharply declined whenever games enter clutch time.

"People are pretending to work while secretly refreshing box scores," one observer claimed.

Fans have also reported severe emotional whiplash caused by the unpredictable nature of playoff basketball, where teams can appear unstoppable one night before collapsing entirely two days later.

"Every series changes direction every forty eight hours," one fan complained. "Nobody knows what is happening anymore."

Social media has reportedly made the experience even more intense, with basketball debates reaching dangerous levels after every game. Experts confirm that a single bad shooting performance is now enough to cause immediate overreactions across the internet.

"One player misses three shots and suddenly people are saying he was never good," a sports commentator noted.

Meanwhile, supporters of eliminated teams are reportedly entering what psychologists describe as forced maturity season, where fans begin pretending they are only watching basketball for the love of the game.

Friends close to several basketball fans say playoff stress has become impossible to avoid, especially during close fourth quarters.

"You can physically hear people aging during overtime," one student joked.

The playoffs have also sparked renewed arguments surrounding legacy conversations, superstar rankings, coaching decisions, and whether modern basketball fans use the word generational too casually.

Despite the emotional damage, fans continue returning night after night, fully aware the playoffs may once again ruin their sleep schedules, mental stability, and academic productivity.

Still, supporters insist the suffering is worth it.

"This is peak basketball," one exhausted fan admitted while visibly struggling to stay awake in class.
""",
            },
            {
                "title": "South Africa Unemployment Crisis Continues to Weigh Heavily on Young People",
                "category": "finance",
                "summary": "Youth unemployment remains one of South Africa biggest concerns.",
                "content": """
South Africa unemployment crisis remains one of the country biggest social and economic challenges, with millions of citizens, particularly young people, continuing to struggle to find stable work opportunities.

According to the latest labour market figures released by Statistics South Africa, the country official unemployment rate has once again increased, reaching 32.7 percent in the first quarter of 2026.

Even more concerning, youth unemployment continues to rise at an alarming pace. Reports indicate that unemployment among young South Africans between the ages of 15 and 34 has climbed to nearly 46 percent, with the 15 to 24 age category remaining the hardest hit.

Speaking on the issue, emerging business commentator Ntando Mtimkulu described unemployment as the defining challenge facing the current generation.

"You cannot have millions of ambitious young people with no opportunities and expect society to remain stable," Ntando said during a recent discussion with peers.

According to Mtimkulu, the crisis extends beyond economics alone. He believes unemployment is increasingly affecting confidence, mental health, long term planning, and even how young people view their futures.

"A lot of young people are educated, talented, and willing to work," he explained. "The frustration comes from feeling stuck despite trying."

Analysts say several factors continue contributing to the crisis, including slow economic growth, limited industrial expansion, skills mismatches, and insufficient job creation across both public and private sectors. While some industries such as finance and construction have recently shown small signs of growth, major sectors including manufacturing and trade have continued shedding jobs.

Friends close to Ntando say the issue resonates deeply with him because many people within his own generation are directly affected.

"He always says unemployment is not just a statistic," one associate explained. "It is people postponing their lives."

Despite the grim outlook, Mtimkulu reportedly remains optimistic that entrepreneurship, digital innovation, and skills development could help create new opportunities for younger generations in the future.

"This generation is resilient," he said. "People are starting businesses, freelancing, learning online, building brands, trying anything they can. That determination matters."

Still, many experts warn that without significant structural economic improvements and more aggressive job creation strategies, unemployment may remain one of South Africa most pressing long term challenges for years to come.
""",
            },
            {
                "title": "The Rise of Ntando Mtimkulu: The Next Big Force in the Commercial World",
                "category": "finance",
                "summary": "Ntando Mtimkulu is positioning himself as one of South Africa promising young commercial minds.",
                "content": """
In a world increasingly shaped by innovation, adaptability, and visionary leadership, one young South African name is beginning to stand out above the rest: Ntando Mtimkulu.

Known among peers for his ambition, sharp commercial instincts, and relentless drive for excellence, Ntando Mtimkulu is rapidly positioning himself as one of the most promising young minds in business and enterprise development. From lecture halls to leadership conversations, his journey reflects the rise of a future powerhouse in the commercial landscape.

Born with an entrepreneurial mindset and a passion for strategic thinking, Mtimkulu first built his academic foundation at Rhodes University, where he completed his undergraduate studies. During his time at Rhodes, he developed a reputation for creativity, discipline, and the ability to think beyond conventional boundaries. Those who studied alongside him often described him as someone destined for influence far beyond the classroom.

Not content with stopping there, Ntando continued sharpening his commercial expertise by pursuing a Postgraduate Diploma in Enterprise Management at Rhodes University. The qualification further strengthened his understanding of business strategy, innovation, entrepreneurship, and modern organizational leadership, all critical tools for navigating today rapidly changing economic environment.

But what truly separates Ntando Mtimkulu from many of his peers is not only his academic background. It is his vision.

Observers describe him as a commercial juggernaut in the making, someone capable of bridging business, technology, culture, and modern African enterprise into one powerful ecosystem. Whether discussing digital innovation, entrepreneurship, branding, or business development, Mtimkulu consistently demonstrates the kind of forward thinking mindset associated with future industry leaders.

Friends and colleagues say he possesses an unusual combination of confidence, creativity, and strategic awareness. Rather than simply chasing success, Ntando appears focused on building influence, legacy, and systems that create meaningful impact.

As South Africa continues searching for a new generation of commercially minded leaders capable of competing on a global scale, many believe Ntando Mtimkulu represents exactly that future: ambitious, educated, innovative, and unapologetically visionary.

While his journey is still unfolding, one thing is becoming increasingly clear: the name Ntando Mtimkulu is one the commercial world may soon find impossible to ignore.
""",
            },
            {
                "title": "Ntando Mtimkulu Left Devastated as Arsenal Close In on League Glory",
                "category": "sports",
                "summary": "Liverpool supporter Ntando Mtimkulu is reportedly struggling with Arsenal title charge.",
                "content": """
For many football supporters around the world, the closing weeks of the season bring excitement, hope, and celebration. But for Ntando Mtimkulu, this season has reportedly delivered nothing but frustration, disbelief, and emotional damage.

The outspoken Liverpool supporter has allegedly struggled to come to terms with the possibility of Arsenal F.C. lifting the league title, a scenario he once confidently dismissed earlier in the campaign.

According to friends close to Mtimkulu, the mere thought of Arsenal fans celebrating a title has become deeply upsetting to him, with some jokingly claiming he now avoids football debates entirely whenever Arsenal form is mentioned.

"Every week he keeps saying they will bottle it," one friend reportedly said. "And every week Arsenal somehow win again."

Mtimkulu, a passionate supporter of Liverpool F.C., is said to have entered the season with high expectations following the managerial transition after the departure of club legend Jurgen Klopp. However, sources suggest that his patience with new Liverpool manager Arne Slot has already worn dangerously thin.

While many Liverpool fans have urged patience during the new era, Ntando reportedly remains unconvinced by Slot tactical decisions, substitutions, and inability to stop Arsenal momentum in the title race.

"He misses Klopp football," another source joked. "Every conversation somehow ends with him saying, Klopp would never allow this."

Observers say Ntando frustrations are amplified by the confidence currently flowing through Arsenal supporters online, something he reportedly finds almost impossible to tolerate. Social media activity from the lifelong Liverpool fan has allegedly shifted from optimism to weekly emotional survival.

Despite the football heartbreak, those who know Mtimkulu best say his passion for the sport is exactly what makes him such a committed supporter. Win or lose, he remains deeply invested in Liverpool success and continues to believe the club will eventually return to the summit of English football.

Still, with Arsenal edging closer to glory, friends say the coming weeks could be emotionally challenging for him.

"He is trying to stay strong," one insider laughed. "But if Arsenal actually win the league, nobody should expect him to answer football messages for at least a month."
""",
            },
            {
                "title": "Mystery Romance? Ntando Mtimkulu Reportedly in Long Distance Relationship With Freckles",
                "category": "current_affairs",
                "summary": "Speculation continues around Ntando relationship with Freckles.",
                "content": """
Social circles close to Ntando Mtimkulu have recently been buzzing with speculation surrounding what many are calling his most mysterious chapter yet, a long distance relationship with a woman known only by the nickname Freckles.

While neither Ntando nor the mystery woman has publicly confirmed the relationship, insiders claim the connection between the two has quietly become one of the most talked about topics among friends and followers alike.

Described by sources as deep, intense, and surprisingly wholesome, the relationship reportedly thrives despite the physical distance separating the pair. Friends close to Mtimkulu say the two spend countless hours talking, sharing music, exchanging memes, and planning future experiences together.

"People think long distance relationships are impossible," one source allegedly said. "But these two somehow make it work."

The woman, referred to almost exclusively as Freckles, has become somewhat of an urban legend within Ntando social circles. Very little is publicly known about her identity, fueling even more curiosity online. Some claim she is highly intellectual and creative, while others insist she has completely transformed Ntando softer side.

Those close to the situation say the relationship has had a noticeable effect on Mtimkulu energy and outlook. Known publicly for his ambitious and commercially driven mindset, friends say he becomes noticeably calmer and more relaxed whenever Freckles is mentioned.

"There is business Ntando," one friend joked, "and then there is Freckles Ntando."

Sources also claim the pair have developed rituals to maintain the relationship despite the distance, including scheduled movie nights, late night calls, shared playlists, and constant communication throughout the day.

Still, long distance relationships are never easy. Friends say balancing personal ambitions, demanding schedules, and emotional connection across different locations has not come without challenges. Yet despite this, those around the pair insist their connection appears stronger than ever.

Adding even more intrigue to the story is the fact that Ntando has reportedly gone to great lengths to keep the relationship private. While many public figures openly display their romantic lives online, Mtimkulu seems determined to protect this one from public scrutiny.

Whether the mystery surrounding Freckles will ever fully be revealed remains unknown. But one thing appears increasingly clear: behind the ambitious entrepreneur and rising commercial mind is a young man deeply invested in a relationship that many close to him believe is very real and very serious.
""",
            },
            {
                "title": "Freckles Counting Down the Days Until the Next A Court of Thorns and Roses Release",
                "category": "current_affairs",
                "summary": "Freckles is reportedly preparing emotionally for the next ACOTAR release.",
                "content": """
Excitement is reportedly reaching dangerous levels within the reading community as fans of A Court of Thorns and Roses continue speculating about the next release connected to the beloved fantasy universe created by Sarah J Maas.

Among the most emotionally invested fans, according to sources close to the situation, is the mysterious Freckles, the long distance love interest frequently associated with Ntando Mtimkulu.

Friends claim Freckles has become completely unbearable whenever discussions about the series arise, with conversations quickly turning into passionate breakdowns of characters, theories, emotional trauma, and romantic tension.

"She genuinely talks about those books like they are historical events," one source joked.

The A Court of Thorns and Roses series, often referred to by fans simply as ACOTAR, has built a massive global following thanks to its mix of fantasy, romance, political intrigue, and emotionally intense storytelling. Readers around the world have become deeply attached to characters like Feyre, Rhysand, Cassian, and Nesta, creating one of modern fantasy most dedicated fan communities.

According to insiders, Freckles is particularly excited about the rumored October release window connected to the franchise, having allegedly spent months rereading sections of the series in preparation.

"She has theories," one friend explained. "So many theories."

Sources claim Ntando himself remains slightly confused by the emotional intensity surrounding the books but has learned to accept that discussing ACOTAR requires full attention and emotional preparedness.

"He once asked a simple question about a character," a witness recalled. "He got a forty minute explanation."

Friends say Freckles especially loves the way the series blends romance with themes of healing, loyalty, personal growth, and resilience. Like many readers, she reportedly believes the emotional depth of the characters is what makes the books so addictive.

"There is always screaming, crying, war, romance, betrayal, magic, everything at once," one insider laughed.

The anticipation surrounding the next installment has reportedly become so intense that Freckles has already begun planning her reading schedule weeks in advance to avoid interruptions once the release arrives.

Sources close to Ntando say he has accepted that when the new book eventually drops, communication may temporarily decrease.

"He already knows he is going to lose her to Prythian for at least three business days," one friend joked.

Whether the next release lives up to expectations remains to be seen. But one thing appears certain: Freckles, along with millions of readers worldwide, is more than ready to return to the world of ACOTAR.
""",
            },
        ]

        for index, item in enumerate(articles):
            Article.objects.update_or_create(
                title=item["title"],
                defaults={
                    "summary": item["summary"],
                    "content": item["content"].strip(),
                    "category": item["category"],
                    "article_type": "internal",
                    "publisher": publisher,
                    "author": journalist,
                    "approved": True,
                    "published_at": timezone.now() - timedelta(days=index),
                },
            )

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(articles)} full articles successfully."))
