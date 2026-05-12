from datetime import timedelta

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.utils import timezone

from accounts.models import CustomUser
from articles.models import Article
from newsletters.models import Newsletter
from publishers.models import Publisher


class Command(BaseCommand):
    help = "Seed Ntando News with users, publishers, newsletters, internal articles, and external-style articles."

    def handle(self, *args, **kwargs):
        journalist_group, _ = Group.objects.get_or_create(name="Journalist")
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        reader_group, _ = Group.objects.get_or_create(name="Reader")

        journalist, _ = CustomUser.objects.get_or_create(
            username="Ntando",
            defaults={
                "email": "ntando@news.com",
                "role": "journalist",
            },
        )
        journalist.set_password("Mtimkulu")
        journalist.role = "journalist"
        journalist.save()
        journalist.groups.add(journalist_group)

        editor, _ = CustomUser.objects.get_or_create(
            username="NtandoM",
            defaults={
                "email": "editor@news.com",
                "role": "editor",
            },
        )
        editor.set_password("Mtimkulu")
        editor.role = "editor"
        editor.save()
        editor.groups.add(editor_group)

        reader, _ = CustomUser.objects.get_or_create(
            username="Reader1",
            defaults={
                "email": "reader@news.com",
                "role": "reader",
            },
        )
        reader.set_password("reader123")
        reader.role = "reader"
        reader.save()
        reader.groups.add(reader_group)

        newsroom, _ = Publisher.objects.get_or_create(
            name="Ntando Newsroom",
            defaults={
                "description": "South African digital newsroom covering sports, politics, finance, current affairs, culture, and personality features.",
                "website": "https://ntandonews.onrender.com",
            },
        )

        economic_desk, _ = Publisher.objects.get_or_create(
            name="Ntando Economic Desk",
            defaults={
                "description": "Economic, labour market, business, and youth finance reporting.",
                "website": "https://ntandonews.onrender.com",
            },
        )

        sports_desk, _ = Publisher.objects.get_or_create(
            name="Ntando Sports Desk",
            defaults={
                "description": "Football, PSL, Liverpool, Arsenal, and South African sports coverage.",
                "website": "https://ntandonews.onrender.com",
            },
        )

        current_affairs_desk, _ = Publisher.objects.get_or_create(
            name="Ntando Current Affairs",
            defaults={
                "description": "Human-interest stories, internet culture, public issues, and current affairs.",
                "website": "https://ntandonews.onrender.com",
            },
        )

        lifestyle_desk, _ = Publisher.objects.get_or_create(
            name="Ntando Lifestyle Desk",
            defaults={
                "description": "Music, relationships, personality, and lifestyle coverage.",
                "website": "https://ntandonews.onrender.com",
            },
        )

        cape_times, _ = Publisher.objects.get_or_create(
            name="Cape Times",
            defaults={
                "description": "South African news publication used as an external source.",
                "website": "https://capetimes.co.za",
            },
        )

        the_south_african, _ = Publisher.objects.get_or_create(
            name="The South African",
            defaults={
                "description": "South African digital news publication used as an external source.",
                "website": "https://www.thesouthafrican.com",
            },
        )

        for publisher in [
            newsroom,
            economic_desk,
            sports_desk,
            current_affairs_desk,
            lifestyle_desk,
        ]:
            publisher.journalists.add(journalist)
            publisher.editors.add(editor)

        reader.subscribed_publishers.add(
            newsroom,
            economic_desk,
            sports_desk,
            current_affairs_desk,
            lifestyle_desk,
            cape_times,
            the_south_african,
        )
        reader.subscribed_journalists.add(journalist)

        now = timezone.now()

        internal_articles = [
            {
                "days_ago": 1,
                "publisher": current_affairs_desk,
                "title": "Ntando Mtimkulu Says Internet Debates Between Believers and Skeptics Have Gone Completely Off the Rails",
                "category": "current_affairs",
                "summary": "Ntando reportedly spent hours watching philosophical internet debates descend into chaos.",
                "content": """
According to close friends of Ntando Mtimkulu, one of his favorite forms of online entertainment has become watching philosophical arguments spiral completely out of control on social media.

The Rhodes University graduate reportedly spent several hours recently observing a heated debate between religious users, skeptics, amateur philosophers, and random podcast fans  a discussion that insiders say achieved absolutely nothing after nearly five hours.

One person was quoting philosophy, a witness explained. Another was posting science articles. Somebody else brought up ancient history for no reason. It was chaos.

Sources claim Ntando initially entered the discussion hoping for a thoughtful exchange of ideas. However, things reportedly deteriorated rapidly after multiple participants began using increasingly dramatic language to defend their worldviews.

At some point people stopped debating and just started typing paragraphs with words like objective reality and quantum mechanics, one friend laughed.

According to insiders, Ntando's breaking point came after a participant allegedly claimed they had personally defeated philosophy during a TikTok comment section argument.

He just closed his laptop for like ten minutes, a source recalled.

Friends say Ntando later joked that modern internet debates often involve extreme confidence with absolutely no intention of listening.

He said everybody enters those arguments trying to win instead of trying to understand, one witness explained.

Despite the absurdity, sources say Mtimkulu still enjoys observing the discussions because they reveal how passionate people become about meaning, existence, morality, and purpose.

He finds humanity fascinating, a friend said. Also slightly exhausting.

The entrepreneur reportedly concluded the evening by announcing that the internet may have given society too much access to microphones and not enough access to humility.
""",
            },
            {
                "days_ago": 2,
                "publisher": current_affairs_desk,
                "title": "Ntando Mtimkulu Reportedly Loses Patience During Flat Earth Debate",
                "category": "current_affairs",
                "summary": "Friends say Ntando struggled to remain calm during an unexpected flat earth debate.",
                "content": """
What began as a casual late-night conversation among friends quickly descended into chaos after the topic of flat earth theories was unexpectedly introduced  and according to witnesses, Ntando Mtimkulu was absolutely not prepared for it.

Sources claim the discussion started innocently before one participant allegedly suggested that the Earth might actually be flat. The statement reportedly caused immediate confusion in the room, with Ntando initially assuming it was a joke.

He laughed for like thirty seconds, one witness said. Then he realized the guy was serious.

Friends say Mtimkulu, known for his calm and analytical personality, attempted to remain respectful at first. However, the conversation reportedly became increasingly difficult after several conspiracy theories involving Antarctica, NASA, and hidden truths were introduced.

At one point Ntando just stared at the ceiling in silence, another source recalled. You could literally see him questioning humanity.

According to those present, the Rhodes University graduate tried explaining basic scientific concepts, gravity, global travel routes, and satellite technology  only to reportedly receive even more bizarre counterarguments in return.

He said, Brother, people have literally gone to space, one friend laughed. But somehow that still was not enough.

The discussion allegedly reached its breaking point after someone claimed airplanes only move sideways because the Earth is a flat plane.

That is when Ntando stood up and walked around the room, a witness explained. He needed fresh air.

Despite the frustration, friends insist the entire exchange eventually became comedy material for the rest of the evening, with Ntando repeatedly joking that humanity may never fully recover from internet conspiracy culture.

He kept saying, We have too much access to Wi-Fi now, one source joked.

While flat earth communities continue existing online, Ntando reportedly remains firmly committed to what he calls very radical ideas, including science, geography, and basic common sense.

Sources say he has since vowed to avoid future flat earth debates entirely unless professional astronomers are present.
""",
            },
            {
                "days_ago": 3,
                "publisher": economic_desk,
                "title": "South Africa Unemployment Crisis Continues to Weigh Heavily on Young People",
                "category": "politics",
                "summary": "Youth unemployment remains one of South Africa's biggest social and economic challenges.",
                "content": """
South Africa's unemployment crisis remains one of the country's biggest social and economic challenges, with millions of citizens  particularly young people  continuing to struggle to find stable work opportunities.

According to the latest labour market figures released by Statistics South Africa, the country's official unemployment rate has once again increased, reaching 32.7% in the first quarter of 2026.

Even more concerning, youth unemployment continues to rise at an alarming pace. Reports indicate that unemployment among young South Africans between the ages of 15 and 34 has climbed to nearly 46%, with the 15-24 age category remaining the hardest hit.

Speaking on the issue, emerging business commentator Ntando Mtimkulu described unemployment as the defining challenge facing the current generation.

You cannot have millions of ambitious young people with no opportunities and expect society to remain stable, Ntando said during a recent discussion with peers.

According to Mtimkulu, the crisis extends beyond economics alone. He believes unemployment is increasingly affecting confidence, mental health, long-term planning, and even how young people view their futures.

A lot of young people are educated, talented, and willing to work, he explained. The frustration comes from feeling stuck despite trying.

Analysts say several factors continue contributing to the crisis, including slow economic growth, limited industrial expansion, skills mismatches, and insufficient job creation across both public and private sectors.

Friends close to Ntando say the issue resonates deeply with him because many people within his own generation are directly affected.

He always says unemployment is not just a statistic, one associate explained. It is people postponing their lives.

Despite the grim outlook, Mtimkulu reportedly remains optimistic that entrepreneurship, digital innovation, and skills development could help create new opportunities for younger generations in the future.

This generation is resilient, he said. People are starting businesses, freelancing, learning online, building brands, trying anything they can. That determination matters.
""",
            },
            {
                "days_ago": 4,
                "publisher": economic_desk,
                "title": "Young People Are No Longer Waiting  Ntando Mtimkulu Speaks on the Rise of Youth Investing",
                "category": "finance",
                "summary": "Ntando Mtimkulu says young people are becoming increasingly focused on investing and long-term wealth creation.",
                "content": """
As economic pressures continue reshaping the ambitions of young people across South Africa, a noticeable shift is emerging: more young adults are beginning to invest, save, and think seriously about long-term wealth creation.

In an exclusive interview, emerging commercial analyst and enterprise management graduate Ntando Mtimkulu shared his thoughts on why today's youth are becoming increasingly focused on financial growth and future stability.

According to Mtimkulu, the stereotype that young people only care about trends, nightlife, and short-term gratification is rapidly becoming outdated.

Young people are realizing that survival alone is no longer enough, Ntando explained. People want ownership. They want security. They want freedom. And increasingly, they understand that investing is one of the pathways toward that.

Ntando believes social media and access to information have played a major role in the transformation.

Ten years ago, investment conversations felt exclusive, he said. Now a university student can learn about ETFs, compound interest, or building a business directly from their phone.

The Rhodes University graduate also pointed to economic uncertainty as a major driver behind the trend.

People are nervous about the future, Ntando explained. But instead of giving up, many are trying to prepare themselves financially earlier than ever before.

Interestingly, Mtimkulu says the modern definition of investing has also evolved. While traditional investing once focused almost exclusively on stocks and property, younger generations are now investing in skills, personal brands, digital businesses, and online platforms.

Somebody learning coding, building a YouTube channel, freelancing online, or starting a small clothing brand  that is also investment, he said. The mindset has shifted from simply earning money to building assets.

Despite the optimism, Ntando warned against what he described as performative wealth culture online, where unrealistic lifestyles and quick-money promises create dangerous expectations for young people.

A lot of people are being sold fantasies, he cautioned. Real wealth usually takes time, discipline, patience, and consistency. Most successful people are not becoming rich overnight.

Still, he remains optimistic about the future of financially conscious youth in South Africa.
""",
            },
            {
                "days_ago": 5,
                "publisher": economic_desk,
                "title": "The Rise of Ntando Mtimkulu: The Next Big Force in the Commercial World",
                "category": "finance",
                "summary": "Ntando Mtimkulu is rapidly positioning himself as one of South Africa's most promising young minds in business.",
                "content": """
In a world increasingly shaped by innovation, adaptability, and visionary leadership, one young South African name is beginning to stand out above the rest: Ntando Mtimkulu.

Known among peers for his ambition, sharp commercial instincts, and relentless drive for excellence, Ntando Mtimkulu is rapidly positioning himself as one of the most promising young minds in business and enterprise development.

Born with an entrepreneurial mindset and a passion for strategic thinking, Mtimkulu first built his academic foundation at Rhodes University, where he completed his undergraduate studies.

During his time at Rhodes, he developed a reputation for creativity, discipline, and the ability to think beyond conventional boundaries. Those who studied alongside him often described him as someone destined for influence far beyond the classroom.

Not content with stopping there, Ntando continued sharpening his commercial expertise by pursuing a Postgraduate Diploma in Enterprise Management at Rhodes University.

The qualification further strengthened his understanding of business strategy, innovation, entrepreneurship, and modern organizational leadership  all critical tools for navigating today's rapidly changing economic environment.

But what truly separates Ntando Mtimkulu from many of his peers is not only his academic background. It is his vision.

Observers describe him as a commercial juggernaut in the making  someone capable of bridging business, technology, culture, and modern African enterprise into one powerful ecosystem.

Whether discussing digital innovation, entrepreneurship, branding, or business development, Mtimkulu consistently demonstrates the kind of forward-thinking mindset associated with future industry leaders.

Friends and colleagues say he possesses an unusual combination of confidence, creativity, and strategic awareness. Rather than simply chasing success, Ntando appears focused on building influence, legacy, and systems that create meaningful impact.

As South Africa continues searching for a new generation of commercially minded leaders capable of competing on a global scale, many believe Ntando Mtimkulu represents exactly that future: ambitious, educated, innovative, and unapologetically visionary.

While his journey is still unfolding, one thing is becoming increasingly clear  the name Ntando Mtimkulu is one the commercial world may soon find impossible to ignore.
""",
            },
            {
                "days_ago": 6,
                "publisher": sports_desk,
                "title": "Ntando Mtimkulu Left Devastated as Arsenal Close In on League Glory",
                "category": "sports",
                "summary": "Liverpool supporter Ntando Mtimkulu is reportedly struggling with Arsenal's title charge.",
                "content": """
For many football supporters around the world, the closing weeks of the season bring excitement, hope, and celebration. But for Ntando Mtimkulu, this season has reportedly delivered nothing but frustration, disbelief, and emotional damage.

The outspoken Liverpool supporter has allegedly struggled to come to terms with the possibility of Arsenal F.C. lifting the league title  a scenario he once confidently dismissed earlier in the campaign.

According to friends close to Mtimkulu, the mere thought of Arsenal fans celebrating a title has become deeply upsetting to him, with some jokingly claiming he now avoids football debates entirely whenever Arsenal's form is mentioned.

Every week he keeps saying they will bottle it, one friend reportedly said. And every week Arsenal somehow win again.

Mtimkulu, a passionate supporter of Liverpool F.C., is said to have entered the season with high expectations following the managerial transition after the departure of club legend Jurgen Klopp.

However, sources suggest that his patience with new Liverpool manager Arne Slot has already worn dangerously thin.

While many Liverpool fans have urged patience during the new era, Ntando reportedly remains unconvinced by Slot's tactical decisions, substitutions, and inability to stop Arsenal's momentum in the title race.

He misses Klopp football, another source joked. Every conversation somehow ends with him saying, Klopp would never allow this.

Observers say Ntando's frustrations are amplified by the confidence currently flowing through Arsenal supporters online  something he reportedly finds almost impossible to tolerate.

Despite the football heartbreak, those who know Mtimkulu best say his passion for the sport is exactly what makes him such a committed supporter.

Still, with Arsenal edging closer to glory, friends say the coming weeks could be emotionally challenging for him.

He is trying to stay strong, one insider laughed. But if Arsenal actually win the league, nobody should expect him to answer football messages for at least a month.
""",
            },
            {
                "days_ago": 7,
                "publisher": current_affairs_desk,
                "title": "Mystery Romance? Ntando Mtimkulu Reportedly in Long-Distance Relationship With Freckles",
                "category": "current_affairs",
                "summary": "Speculation continues around Ntando's reported long-distance relationship with a mystery woman known as Freckles.",
                "content": """
Social circles close to Ntando Mtimkulu have recently been buzzing with speculation surrounding what many are calling his most mysterious chapter yet  a long-distance relationship with a woman known only by the nickname Freckles.

While neither Ntando nor the mystery woman has publicly confirmed the relationship, insiders claim the connection between the two has quietly become one of the most talked-about topics among friends and followers alike.

Described by sources as deep, intense, and surprisingly wholesome, the relationship reportedly thrives despite the physical distance separating the pair.

Friends close to Mtimkulu say the two spend countless hours talking, sharing music, exchanging memes, and planning future experiences together.

People think long-distance relationships are impossible, one source allegedly said. But these two somehow make it work.

The woman, referred to almost exclusively as Freckles, has become somewhat of an urban legend within Ntando's social circles.

Very little is publicly known about her identity, fueling even more curiosity online. Some claim she is highly intellectual and creative, while others insist she has completely transformed Ntando's softer side.

Those close to the situation say the relationship has had a noticeable effect on Mtimkulu's energy and outlook.

Known publicly for his ambitious and commercially driven mindset, friends say he becomes noticeably calmer and more relaxed whenever Freckles is mentioned.

There is business Ntando, one friend joked, and then there is Freckles Ntando.

Sources also claim the pair have developed rituals to maintain the relationship despite the distance  including scheduled movie nights, late-night calls, shared playlists, and constant communication throughout the day.

Still, long-distance relationships are never easy. Friends say balancing personal ambitions, demanding schedules, and emotional connection across different locations has not come without challenges.

Yet despite this, those around the pair insist their connection appears stronger than ever.

Whether the mystery surrounding Freckles will ever fully be revealed remains unknown. But one thing appears increasingly clear: behind the ambitious entrepreneur and rising commercial mind is a young man deeply invested in a relationship that many close to him believe is very real  and very serious.
""",
            },
            {
                "days_ago": 8,
                "publisher": current_affairs_desk,
                "title": "Ntando Mtimkulu Says He Is Concerned But Calm Amid Growing Hantavirus Discussions",
                "category": "politics",
                "summary": "Ntando reportedly adopts a cautiously confident approach amid growing online discussions around Hantavirus.",
                "content": """
As conversations surrounding Hantavirus continue circulating online and across global health discussions, Ntando Mtimkulu has reportedly adopted what friends describe as a cautiously confident approach to the situation.

Sources close to Mtimkulu say the rising commercial personality has spent recent weeks keeping informed about developments while also encouraging those around him not to panic unnecessarily.

He is nervous, obviously, one friend said. But he also keeps telling people that fear without information helps nobody.

Known for his analytical mindset and calm demeanor under pressure, Ntando has allegedly approached the topic with a balance of concern and practicality.

Friends say he has become unusually interested in public health discussions, preventative measures, and global preparedness conversations.

According to those close to him, Mtimkulu believes modern society often reacts emotionally before fully understanding situations  something he reportedly wants to avoid.

He is trying not to become one of those people doom-scrolling at 2am, another insider joked.

While there is no indication that Ntando himself has been directly affected, sources claim the discussions around Hantavirus have sparked broader reflections in him about health, productivity, and the unpredictability of life.

Despite the uncertainty surrounding public conversations online, Ntando reportedly remains optimistic and focused on his long-term goals.
""",
            },
            {
                "days_ago": 9,
                "publisher": newsroom,
                "title": "Ntando Mtimkulu Allegedly Believes He Could Run a Fortune 500 Company Tomorrow",
                "category": "finance",
                "summary": "Friends joke that Ntando's confidence has reached dangerous levels after a Fortune 500 leadership claim.",
                "content": """
Friends of Ntando Mtimkulu have jokingly accused him of possessing dangerous levels of confidence after he reportedly claimed he could successfully run a Fortune 500 company if given the opportunity.

The statement, allegedly made during a casual late-night discussion about business leadership, has since become legendary among his friend group.

He genuinely started explaining restructuring strategies like the board had already hired him, one source laughed.

Known for his passion for enterprise management and commercial strategy, Ntando reportedly spends hours studying business models, leadership systems, and global corporate structures.

Friends say conversations with him can quickly transform from casual small talk into full-scale TED Talks about branding, innovation, and organizational culture.

While some view the confidence as amusing, others insist there may actually be substance behind it.

He talks big, one friend admitted, but the scary thing is that he has usually thought things through.
""",
            },
            {
                "days_ago": 10,
                "publisher": lifestyle_desk,
                "title": "The Spotify Sessions: Ntando Mtimkulu Music Taste Sparks Heated Debate",
                "category": "current_affairs",
                "summary": "Friends are divided over Ntando's unpredictable music rotation and emotionally confusing playlists.",
                "content": """
A fierce debate has reportedly broken out among friends of Ntando Mtimkulu after several people questioned his increasingly unpredictable music rotation.

While Ntando is known for having a deep appreciation for music, insiders claim his playlists have recently become emotionally confusing.

One minute it is deep lyrical rap, said one source. The next minute it is heartbreak music, then jazz, then aggressive gym music.

Friends suspect the mysterious influence of Freckles may be partially responsible for the shift, though no confirmation has been made.

Despite the criticism, Ntando reportedly defends his playlists passionately, arguing that music should reflect every version of who you are.

Sources also claim he treats Spotify algorithms with almost scientific seriousness, frequently curating playlists for different moods, environments, and even weather conditions.
""",
            },
            {
                "days_ago": 11,
                "publisher": current_affairs_desk,
                "title": "Ntando Mtimkulu Reportedly Preparing for Unmatched Greatness Era",
                "category": "current_affairs",
                "summary": "Friends say Ntando has entered a new period of discipline, ambition, and personal reinvention.",
                "content": """
Close associates of Ntando Mtimkulu say he has recently entered what he privately refers to as his Unmatched Greatness Era.

While the phrase has confused many around him, friends claim it refers to a new period of discipline, ambition, and personal reinvention.

He talks like he is in a sports documentary now, one friend joked.

Sources say the new phase allegedly includes stricter routines, clearer career goals, improved fitness habits, and a renewed focus on long-term success.

Friends have also noticed an increase in motivational quotes, strategic planning discussions, and random speeches about legacy.

He genuinely believes he is building toward something massive, another source explained.

Whether exaggerated or not, those closest to Ntando admit one thing: his confidence is extremely difficult to ignore.
""",
            },
        ]

        seeded_articles = []

        for item in internal_articles:
            article, _ = Article.objects.update_or_create(
                title=item["title"],
                defaults={
                    "summary": item["summary"],
                    "content": item["content"].strip(),
                    "category": item["category"],
                    "article_type": Article.INTERNAL,
                    "publisher": item["publisher"],
                    "author": journalist,
                    "approved": True,
                    "source_name": "",
                    "external_url": None,
                    "external_image_url": "",
                    "published_at": now - timedelta(days=item["days_ago"], hours=item["days_ago"]),
                },
            )
            seeded_articles.append(article)

        external_articles = [
            {
                "days_ago": 1,
                "publisher": cape_times,
                "title": "LIVE | Cyril Ramaphosa Remains President After National Address",
                "category": "politics",
                "summary": "President Cyril Ramaphosa addressed the nation following political pressure and Constitutional Court developments.",
                "content": "This is an aggregated summary. Continue reading the full article on Cape Times using the original source link.",
                "source_name": "Cape Times",
                "external_url": "https://capetimes.co.za/news/politics/2026-05-11-live-cyril-ramaphosa-addresses-the-nation/",
            },
            {
                "days_ago": 2,
                "publisher": the_south_african,
                "title": "Kaizer Chiefs Bosses Face Decisions on Coaches",
                "category": "sports",
                "summary": "Kaizer Chiefs management are reportedly evaluating members of the technical team after securing continental qualification.",
                "content": "This is an aggregated sports summary. Continue reading the full article on The South African using the original source link.",
                "source_name": "The South African",
                "external_url": "https://www.thesouthafrican.com/sport/soccer/psl-south-africa/kaizer-chiefs-bosses-face-decisions-on-coaches/",
            },
        ]

        for item in external_articles:
            article, _ = Article.objects.update_or_create(
                external_url=item["external_url"],
                defaults={
                    "title": item["title"],
                    "summary": item["summary"],
                    "content": item["content"],
                    "category": item["category"],
                    "article_type": Article.AGGREGATED,
                    "publisher": item["publisher"],
                    "author": None,
                    "approved": True,
                    "source_name": item["source_name"],
                    "external_image_url": "",
                    "published_at": now - timedelta(days=item["days_ago"], hours=item["days_ago"]),
                },
            )
            seeded_articles.append(article)

        newsletter, _ = Newsletter.objects.get_or_create(
            title="Ntando Weekly Briefing",
            defaults={
                "description": "A curated weekly briefing featuring the latest stories from Ntando News.",
                "author": journalist,
            },
        )
        newsletter.articles.set(seeded_articles[:8])

        self.stdout.write(self.style.SUCCESS("Sample data created successfully."))
        self.stdout.write(f"Articles seeded: {len(seeded_articles)}")
        self.stdout.write("Journalist Login: Ntando / Mtimkulu")
        self.stdout.write("Editor Login: NtandoM / Mtimkulu")
        self.stdout.write("Reader Login: Reader1 / reader123")
