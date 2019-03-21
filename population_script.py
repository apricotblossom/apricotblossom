import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    cats = {"The Invisible Guardian": {"yturl": "/static/ITAV/The Invisible Guardian.mp4",
                                       "cats": "LONG LIVE INTERACTIVE VIDEO GAME",
                                       "releasedate": "2019-01-23",
                                       "introduction": "\"The Invisible Guardian\" long live interactive video experience (Orange light authorized adaptation of new work), create a spy war legend belonging to each person! The road we have taken! I would like to pay tribute to the unknown heroes who have struggled on the secret front!  Synopsis:  Your name is Xiao Tu. You were two years ago, or a patriotic student in Shanghai who was eager to scream \"anti-Japanese salvation\" on the street, but was arrested and imprisoned for being young and bloody. After the release, the teacher arranged for you to study in Japan. Two years later, your image of the patriotic student was already forgotten by people. The teacher and the organization decided to let you enter the enemy. How do you play this \"spy\"? Faced with a tough choice is to take care of the overall situation or be soft-hearted?  Returning to the turbulent era of war, you will become an invisible guardian and experience the spy war life of step by step. Each of your choices will affect the direction of the ending, hundreds of branch plots waiting for you to unlock! The four completely different endings make you feel a lot!",
                                       "review": "\"The Invisible Guardian\" long live interactive video experience (Orange light authorized adaptation of new work), create a spy war legend belonging to each person! The road we have taken! I would like to pay tribute to the unknown heroes who have struggled on the secret front!  Synopsis:  Your name is Xiao Tu. You were two years ago, or a patriotic student in Shanghai who was eager to scream \"anti-Japanese salvation\" on the street, but was arrested and imprisoned for being young and bloody. After the release, the teacher arranged for you to study in Japan. Two years later, your image of the patriotic student was already forgotten by people. The teacher and the organization decided to let you enter the enemy. How do you play this \"spy\"? Faced with a tough choice is to take care of the overall situation or be soft-hearted?  Returning to the turbulent era of war, you will become an invisible guardian and experience the spy war life of step by step. Each of your choices will affect the direction of the ending, hundreds of branch plots waiting for you to unlock! The four completely different endings make you feel a lot!",
                                       "iosurl": "https://www.youtube.com/",
                                       "andurl": "https://www.youtube.com/",
                                       "pcurl": "https://store.steampowered.com/search/?snr=1_4_4__12&term=The+Invisible+Guardian",
                                       "pictureurl": "/static/img/The_Invisible_Guardian/",
                                       "views": 0,
                                       "likes": 0,
                                       },
            "Counter-Strike\uff1aGlobal Offensive":{"yturl": "/static/ITAV/Counter-Strike.mp4",
                                                    "cats": "Shooting",
                                                    "releasedate": "2012-08-21",
                                                    "introduction": "Global Offensive is definitely a Counter-Strike sequel -- it looks and feels familiar, with minor tweaks here and there to help                              balance old issues and surprise longtime players. This is a demanding, skill-based multiplayer game that's as                              satisfying now as it ever was, but it's for a specific kind of player. If you're not willing to learn to play                               different than you're used to, look elsewhere. Otherwise, this is a top-tier tactics game that will probably                               share the long-tailed legacy of its predecessors..",
                                                    "review": "Global Offensive is definitely a Counter-Strike sequel -- it looks and feels familiar, with minor tweaks here and there to help                              balance old issues and surprise longtime players. This is a demanding, skill-based multiplayer game that's as                              satisfying now as it ever was, but it's for a specific kind of player. If you're not willing to learn to play                               different than you're used to, look elsewhere. Otherwise, this is a top-tier tactics game that will probably                               share the long-tailed legacy of its predecessors..",
                                                    "iosurl": "https://www.youtube.com/",
                                                    "andurl": "https://www.youtube.com/",
                                                    "pcurl": "https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/",
                                                    "pictureurl": "/static/img/Counter-Strike/",
                                                    "views": 0,
                                                    "likes": 1,
                                                    },
            "Dota 2":{"yturl": "/static/ITAV/DOTA_2.mp4",
                                "cats": "RPG",
                                "releasedate": "2013-07-09",
                                "introduction": "Dota 2 deserves its intimidating reputation, and it probably won\u2019t suit you if you\u2019re looking to play casually. There\u2019s a huge time investment before you can even enjoy a game, let alone feel competent at it. But once you start to learn its secrets, there\u2019s a wild and exciting variety of play here that\u2019s unmatched, even by its peers. It\u2019s a challenge of knowledge as well as reflexes, and success is a rush. The fact that it\u2019s completely and totally free to play in the way we wish all free-to-play games could be isn\u2019t just one of the most generous propositions anywhere in gaming, it creates a level playing field where skill and cooperation is paramount. May the best team win.",
                                "review": "Dota 2 deserves its intimidating reputation, and it probably won\u2019t suit you if you\u2019re looking to play casually. There\u2019s a huge time investment before you can even enjoy a game, let alone feel competent at it. But once you start to learn its secrets, there\u2019s a wild and exciting variety of play here that\u2019s unmatched, even by its peers. It\u2019s a challenge of knowledge as well as reflexes, and success is a rush. The fact that it\u2019s completely and totally free to play in the way we wish all free-to-play games could be isn\u2019t just one of the most generous propositions anywhere in gaming, it creates a level playing field where skill and cooperation is paramount. May the best team win.",
                                "iosurl": "https://www.youtube.com/",
                                "andurl": "https://www.youtube.com/",
                                "pcurl": "https://store.steampowered.com/app/570/Dota_2/",
                                "pictureurl": "/static/img/Dota2/",
                                "views": 0,
                                "likes": 2,
                      },
            "MONSTER HUNTER\uff1aWORLD":{"yturl": "/static/ITAV/Monster Hunter- World .mp4",
                                                    "cats": "Adventure",
                                                    "releasedate": "2018-08-10",
                                                    "introduction": "Whether or not it's the best, this is certainly the most audacious Monster Hunter game. World takes a dramatic leap into a look, feel, and size that feels truly new, simultaneously staying true to the series\u2019 ideals by maintaining the addictive loop of combat, intimidating monsters and meaningful upgrades that fans love. The sheer depth and commitment required is still intense, but it clearly isn\u2019t Capcom\u2019s aim to court a casual crowd. This is as all-consuming and incredible a ride as ever..",
                                                    "review": "Whether or not it's the best, this is certainly the most audacious Monster Hunter game. World takes a dramatic leap into a look, feel, and size that feels truly new, simultaneously staying true to the series\u2019 ideals by maintaining the addictive loop of combat, intimidating monsters and meaningful upgrades that fans love. The sheer depth and commitment required is still intense, but it clearly isn\u2019t Capcom\u2019s aim to court a casual crowd. This is as all-consuming and incredible a ride as ever..",
                                                    "iosurl": "https://www.youtube.com/",
                                                    "andurl": "https://www.youtube.com/",
                                                    "pcurl": "https://store.steampowered.com/app/582010/MONSTER_HUNTER_WORLD/",
                                                    "pictureurl": "/static/img/MHW/",
                                                    "views": 0,
                                                    "likes": 3,
                                         },
            "Devil May Cry V":{"yturl": "/static/ITAV/Devil May Cry 5 - Official V Trailer.mp4",
                                "cats": "Action",
                                "releasedate": "2019-03-08",
                                "introduction": "The question of which Devil May Cry game is the best has gotten much easier with Devil May Cry 5. The combat is the strongest the series has seen to date, the story does a great job of balancing all three of its main characters and doling out rewarding bits of its mysterious story at an enticing pace, and the unlockable difficulties, sheer number of techniques to earn, and the upcoming free Bloody Palace DLC will provide a ton of incentive for replayability. It\u2019s good to have you back, Dante and Nero.",
                                "review": "Grand Theft Auto V is not only a preposterously enjoyable video game, but also an intelligent and sharp-tongued satire of contemporary America. It represents a refinement of everything that GTA IV brought to the table five years ago. It\u2019s technically more accomplished in every conceivable way, but it\u2019s also tremendously ambitious in its own right. No other world in video games comes close to this in size or scope, and there is sharp intelligence behind its sense of humour and gift for mayhem. It tells a compelling, unpredictable, and provocative story without ever letting it get in the way of your own self-directed adventures through San Andreas.",
                                "iosurl": "https://www.youtube.com/",
                                "andurl": "https://www.youtube.com/",
                                "pcurl": "https://store.steampowered.com/app/601150/Devil_May_Cry_5/",
                                "pictureurl": "/static/img/DMC5/",
                                "views": 0,
                                "likes": 4,
                               },
            "Pok\u00e9mon GO":{"yturl": "/static/ITAV/Discover Pok\u00e9mon in the Real World with Pok\u00e9mon GO!.mp4",
                                                    "cats": "Shooting",
                                                    "releasedate": "2016-07-07",
                                                    "introduction": "Pok\u00e9mon Go hit the world like a Solar Beam. Or a Hyper Beam. Some kind of powerfully explosive beam. Those who were familiar with the classic franchise and the cutting-edge technology knew it was going to be big. No one knew how big. Server-crushing, street-flooding, industry-redefining, culture-shaping big.",
                                                    "review": "Pok\u00e9mon Go hit the world like a Solar Beam. Or a Hyper Beam. Some kind of powerfully explosive beam. Those who were familiar with the classic franchise and the cutting-edge technology knew it was going to be big. No one knew how big. Server-crushing, street-flooding, industry-redefining, culture-shaping big.",
                                                    "iosurl": "https://itunes.apple.com/gb/app/pok%C3%A9mon-go/id1094591345?mt=8",
                                                    "andurl": "https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo&hl=en_GB",
                                                    "pcurl": "https://www.toutube.com",
                                                    "pictureurl": "/static/img/Poke\u0301mon GO/",
                                                    "views": 0,
                                                    "likes": 5,
                               },
            "Minecraft":{"yturl": "/static/ITAV/Official Minecraft Trailer.mp4",
                                "cats": "Sandbox",
                                "releasedate": "2017-05-24",
                                "introduction": "Like any review, my feelings on Minecraft are the result of my experience with it. Maybe you don&#Array;t thrive off random adventures like I do, or maybe you won&#Array;t feel the same sense of accomplishment I did when I completed my first house. If not, then you likely haven&#Array;t or won&#Array;t enjoy Minecraft in the same way. And that&#Array;s OK. Minecraft, more than any other game I know, isn&#Array;t about playing it a specific way; it&#Array;s an open-world, a blank page just daring you to jump in and do with it what you will. The question, then, isn&#Array;t what you need to do to succeed, what&#Array;s needed to win, but what are you willing to do to make your dreams come to life?.",
                                "review": "Grand Theft Auto V is not only a preposterously enjoyable video game, but also an intelligent and sharp-tongued satire of contemporary America. It represents a refinement of everything that GTA IV brought to the table five years ago. It\u2019s technically more accomplished in every conceivable way, but it\u2019s also tremendously ambitious in its own right. No other world in video games comes close to this in size or scope, and there is sharp intelligence behind its sense of humour and gift for mayhem. It tells a compelling, unpredictable, and provocative story without ever letting it get in the way of your own self-directed adventures through San Andreas.",
                                "iosurl": "https://itunes.apple.com/gb/app/minecraft/id479516143?mt=8",
                                "andurl": "https://play.google.com/store/apps/details?id=com.mojang.minecraftpe",
                                "pcurl": "https://store.steampowered.com/app/639170/Minecraft_Story_Mode__Season_Two/",
                                "pictureurl": "/static/img/Minecraft/",
                                "views": 0,
                                "likes": 6,
                         },
            "NBA 2K19":{"yturl": "/static/ITAV/NBA 2K19 - Official Gameplay Trailer.mp4",
                                                    "cats": "Sports",
                                                    "releasedate": "2018-09-11",
                                                    "introduction": "For many, basketball is more than just a game, and NBA 2K19 doesn\u2019t take that lightly. It throws every resource it has into the theatrics of the sport, creating charismatic presentation, a well-written story mode, and strong core gameplay. The series\u2019 persistent weaknesses are still apparent in areas like the transition game and ludicrous microtransactions, but there\u2019s so much variety to how its extensive MyLeague mode plays out that there\u2019s always a reason to look forward to the next game of basketball.",
                                                    "review": "For many, basketball is more than just a game, and NBA 2K19 doesn\u2019t take that lightly. It throws every resource it has into the theatrics of the sport, creating charismatic presentation, a well-written story mode, and strong core gameplay. The series\u2019 persistent weaknesses are still apparent in areas like the transition game and ludicrous microtransactions, but there\u2019s so much variety to how its extensive MyLeague mode plays out that there\u2019s always a reason to look forward to the next game of basketball.",
                                                    "iosurl": "https://itunes.apple.com/us/app/nba-2k19/id1412321065?mt=8",
                                                    "andurl": "https://play.google.com/store/apps/details?id=com.t2ksports.nba2k19and&hl=en",
                                                    "pcurl": "https://store.steampowered.com/app/841370/NBA_2K19/",
                                                    "pictureurl": "/static/img/2k19/",
                                                    "views": 0,
                                                    "likes": 7,
                        },
            "Brawl Stars":{"yturl": "/static/img/game_review/Brawl Stars- Pre-Register Now.mp4",
                                "cats": "Action",
                                "releasedate": "2015-04-14",
                                "introduction": "Time to BRAWL! Team up with your friends and get ready for epic multiplayer MAYHEM!                                Brawl Stars is the newest game from the makers of Clash of Clans and Clash Royale.                                Jump into your favorite game mode and play quick matches with your friends.                                Shoot 'em up, blow 'em up, punch 'em out and win the BRAWL.",
                                "review": "Brawl Stars is a freemium multiplayer mobile arena fighter/party brawler/shoot 'em up video game developed and published by Supercell.[6] On June 14, 2017, Supercell announced the game via a livestream video on YouTube. It received an iOS soft launch in the Canadian App Store the following day, June 15, 2017. The game was made available in Canada, Finland, Sweden, Denmark, Norway, Ireland, Singapore, Hong Kong, Macao and Malaysia App Stores on January 19, 2018. On June 26, 2018, Android received access to the game as a continuation of the soft launch. On November 14, 2018, Supercell announced its global launch on a YouTube stream.[7] The game was released globally on December 12th, 2018,[8] and made more than $63 million in its first month.",
                                "iosurl": "https://itunes.apple.com/app/brawl-stars/id1229016807?mt=8",
                                "andurl": "https://play.google.com/store/apps/details?id=com.supercell.brawlstars&hl=en",
                                "pcurl": "https://www.toutube.com",
                                "pictureurl": "/static/img/Brawl Stars/",
                                "views": 0,
                                "likes": 8,
                           },
            "Clash Royale":{"yturl": "/static/img/game_review/CLASH ROYALE- EPIC COMEBACK!.mp4",
                                                    "cats": "Shooting",
                                                    "releasedate": "2012-08-21",
                                                    "introduction": "Clash Royale is a real-time multiplayer game starring the Royales,                                 your favourite Clash characters and much,                                 much more. Collect and upgrade dozens of cards featuring the Clash of Clans troops,                                 spells and defenses you know and love, as well as the Royales: Princes, Knights, Baby Dragons and more.                                 Knock the enemy King and Princesses from their towers to defeat your opponents and win Trophies,                                 Crowns and glory in the Arena.",
                                                    "review": "Time to BRAWL! Team up with your friends and get ready for epic multiplayer MAYHEM!                                Brawl Stars is the newest game from the makers of Clash of Clans and Clash Royale.                                Jump into your favorite game mode and play quick matches with your friends.                                Shoot 'em up, blow 'em up, punch 'em out and win the BRAWL.",
                                                    "iosurl": "https://itunes.apple.com/app/id1053012308?mt=8",
                                                    "andurl": "https://play.google.com/store/apps/details?id=com.supercell.clashroyale",
                                                    "pcurl": "https://www.toutube.com",
                                                    "pictureurl": "/static/img/Clash Royale/",
                                                    "views": 0,
                                                    "likes": 9,
                            },
            "Boom Beach":{"yturl": "/static/img/game_review/This March on Boom Beach!.mp4",
                                "cats": "Adventure",
                                "releasedate": "2018-10-26",
                                "introduction": "Come with a plan or leave in defeat! Welcome to Boom Beach, an epic combat strategy game where your brains and your troop\u2019s brawn fight against the evil Blackguard.                                 Attack bases to free enslaved islanders or create a task force with friends and other players to take on the enemy together,                                 all while exploring and unlocking secrets of this beautiful archipelago.                                 Scout, plan, then BOOM THE BEACH!",
                                "review": "Come with a plan or leave in defeat! Welcome to Boom Beach, an epic combat strategy game where your brains and your troop\u2019s brawn fight against the evil Blackguard.                                 Attack bases to free enslaved islanders or create a task force with friends and other players to take on the enemy together,                                 all while exploring and unlocking secrets of this beautiful archipelago.                                 Scout, plan, then BOOM THE BEACH!",
                                "iosurl": "https://itunes.apple.com/app/reef/id672150402?mt=8",
                                "andurl": "https://play.google.com/store/apps/details?id=com.supercell.boombeach&referrer=mat_click_id%3D7eaae9c2d9f3078d3a14bb1f01d94049-20141216-1681",
                                "pcurl": "https://www.toutube.com",
                                "pictureurl": "/static/img/Boom Beach/",
                                "views": 0,
                                "likes": 10,
                          },
            "Clash of Clans":{"yturl": "/static/img/game_review/Clash of Clans- Hammer Jam!.mp4",
                                                    "cats": "Adventure",
                                                    "name": "Clash of Clans",
                                                    "releasedate": "2016-03-12",
                                                    "introduction": "Answer the call of the mustache! Join the international fray that is Clash of Clans.                                     Customize your village, build an army and crush your opponents.                                     Like using friendship to strike fear into your enemies? Join a Clan, or establish a Clashing legacy by creating your own.                                     The choice is yours in this millions-strong community of Barbarians.                                     Download for free and Clash on, Chief!",
                                                    "review": "Answer the call of the mustache! Join the international fray that is Clash of Clans.                                     Customize your village, build an army and crush your opponents.                                     Like using friendship to strike fear into your enemies? Join a Clan, or establish a Clashing legacy by creating your own.                                     The choice is yours in this millions-strong community of Barbarians.                                     Download for free and Clash on, Chief!",
                                                    "iosurl": "https://itunes.apple.com/app/clash-of-clans/id529479190?mt=8",
                                                    "andurl": "https://play.google.com/store/apps/details?id=com.supercell.clashofclans&referrer=mat_click_id%3Df6890da7bad79ed3290aa334b12d358d-20141216-1681",
                                                    "pcurl": "https://www.toutube.com",
                                                    "pictureurl": "/static/img/Clash of Clans/",
                                                    "views": 0,
                                                    "likes": 11,
                              },
            "Grand Theft Auto V":{"yturl": "/static/ITAV/Grand Theft Auto V Trailer.mp4",
                                    "cats": "Action",
                                    "releasedate": "2015-04-14",
                                    "introduction": "Grand Theft Auto V is not only a preposterously enjoyable video game, but also an intelligent and sharp-tongued satire of contemporary America. It represents a refinement of everything that GTA IV brought to the table five years ago. It\u2019s technically more accomplished in every conceivable way, but it\u2019s also tremendously ambitious in its own right. No other world in video games comes close to this in size or scope, and there is sharp intelligence behind its sense of humour and gift for mayhem. It tells a compelling, unpredictable, and provocative story without ever letting it get in the way of your own self-directed adventures through San Andreas.",
                                    "review": "Grand Theft Auto V is not only a preposterously enjoyable video game, but also an intelligent and sharp-tongued satire of contemporary America. It represents a refinement of everything that GTA IV brought to the table five years ago. It\u2019s technically more accomplished in every conceivable way, but it\u2019s also tremendously ambitious in its own right. No other world in video games comes close to this in size or scope, and there is sharp intelligence behind its sense of humour and gift for mayhem. It tells a compelling, unpredictable, and provocative story without ever letting it get in the way of your own self-directed adventures through San Andreas.",
                                    "iosurl": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/",
                                    "andurl": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/",
                                    "pcurl": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/",
                                    "pictureurl": "/static/img/Grand Theft Auto V Review/",
                                    "views": 0,
                                    "likes": 12,
                                  },
            "Red Dead: Redemption\u2161":{"yturl": "/static/ITAV/Red Dead Redemption 2.mp4",
                                                    "cats": "Adventure",
                                                    "releasedate": "2018-10-26",
                                                    "introduction": "Red Dead Redemption 2 stands shoulder-to-shoulder with Grand Theft Auto V as one of the greatest games of the modern age. It\u2019s a gorgeous depiction of an ugly period that\u2019s patient, polished, and a huge amount of fun to play, and it\u2019s combined with Rockstar\u2019s best storytelling to date. Even after finishing the lengthy story I can\u2019t wait to go back and play more. This is a game of rare quality; a meticulously polished open world ode to the outlaw era. Looking for one of this generation\u2019s very best single-player action experiences? Here\u2019s your huckleberry.",
                                                    "review": "Red Dead Redemption 2 stands shoulder-to-shoulder with Grand Theft Auto V as one of the greatest games of the modern age. It\u2019s a gorgeous depiction of an ugly period that\u2019s patient, polished, and a huge amount of fun to play, and it\u2019s combined with Rockstar\u2019s best storytelling to date. Even after finishing the lengthy story I can\u2019t wait to go back and play more. This is a game of rare quality; a meticulously polished open world ode to the outlaw era. Looking for one of this generation\u2019s very best single-player action experiences? Here\u2019s your huckleberry.",
                                                    "iosurl": "https://steamcommunity.com/sharedfiles/filedetails/?id=1552300181&searchtext=",
                                                    "andurl": "https://steamcommunity.com/sharedfiles/filedetails/?id=1552300181&searchtext=",
                                                    "pcurl": "https://steamcommunity.com/sharedfiles/filedetails/?id=1552300181&searchtext=",
                                                    "pictureurl": "/static/img/RDR2/",
                                                    "views": 0,
                                                    "likes": 13,
                                          },
            "Negligee: Love Stories":{"yturl": "/static/ITAV/Negligee - Trailer.mp4",
                                        "cats": "AVG",
                                        "releasedate": "2018-08-10",
                                        "introduction": "A series of four stories following the characters Karen, Charlotte, Sophie and Jasmin. Following their early lives and the decisions they had to make, whether to follow their heart or their head and how that impacts their lives.In the first story we follow Karen as the games protagonist. After living in an emotionally abusive marriage she turns to a new friend for comfort and gets more than she bargained for, but before long her secret affair helps her to realise that she should leave her husband and start over. How will this story play out and the eventual confrontation with her husband. You decide in this visual novel tale with multiple endings.",
                                        "review": "A series of four stories following the characters Karen, Charlotte, Sophie and Jasmin. Following their early lives and the decisions they had to make, whether to follow their heart or their head and how that impacts their lives.In the first story we follow Karen as the games protagonist. After living in an emotionally abusive marriage she turns to a new friend for comfort and gets more than she bargained for, but before long her secret affair helps her to realise that she should leave her husband and start over. How will this story play out and the eventual confrontation with her husband. You decide in this visual novel tale with multiple endings.",
                                        "iosurl": "https://store.steampowered.com/app/1002100/Negligee_Love_Stories/",
                                        "andurl": "https://store.steampowered.com/app/1002100/Negligee_Love_Stories/",
                                        "pcurl": "https://store.steampowered.com/app/1002100/Negligee_Love_Stories/",
                                        "pictureurl": "/static/img/Negligee-Love Stories/",
                                        "views": 0,
                                        "likes": 14,
                                      },
            "Call of Duty: Black Ops 4":{"yturl": "/static/ITAV/Official Call of Duty\u00ae- Black Ops 4.mp4",
                                                    "cats": "Shooting",
                                                    "releasedate": "2018-10-12",
                                                    "introduction": "Call of Duty is a first-person shooter video game franchise. Starting out in 2003, it first focused on games set in World War II, but over time, the series has seen games set in modern times, the midst of the Cold War, futuristic worlds, and outer space. Infinity Ward was the series' first developer, with Treyarch later becoming the second, creating a two-team development cycle. Sledgehammer Games later became the third developer in the cycle. Activision has served as the publisher for the series since its creation. Several spin-offs and handheld versions of titles have also been made by other developers. The most recent title, Call of Duty: Black Ops 4, was released on October 12, 2018.",
                                                    "review": "Call of Duty is a first-person shooter video game franchise. Starting out in 2003, it first focused on games set in World War II, but over time, the series has seen games set in modern times, the midst of the Cold War, futuristic worlds, and outer space. Infinity Ward was the series' first developer, with Treyarch later becoming the second, creating a two-team development cycle. Sledgehammer Games later became the third developer in the cycle. Activision has served as the publisher for the series since its creation. Several spin-offs and handheld versions of titles have also been made by other developers. The most recent title, Call of Duty: Black Ops 4, was released on October 12, 2018.",
                                                    "iosurl": "https://www.callofduty.com/uk/en/blackops4/pc",
                                                    "andurl": "https://www.callofduty.com/uk/en/blackops4/pc",
                                                    "pcurl": "https://www.callofduty.com/uk/en/blackops4/pc",
                                                    "pictureurl": "/static/img/Call of Duty-Black Ops 4/",
                                                    "views": 0,
                                                    "likes": 15,
                                         }
            }

    for cat, cat_data in cats.items(): 
        #c = add_cat(cat) 
        c = add_cat(cat, cat_data["yturl"],cat_data["cats"],cat_data["releasedate"],cat_data["introduction"],cat_data["review"],
                    cat_data["iosurl"],cat_data["andurl"],cat_data["pcurl"],cat_data["pictureurl"],cat_data["views"],cat_data["likes"])

    for c in Category.objects.all(): 
        for p in Page.objects.filter(category=c): 
            print("- {0} - {1}".format(str(c), str(p))) 


def add_cat(name,yturl,cats,releasedate,introduction,review,iosurl,andurl,pcurl,pictureurl,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.yturl = yturl
    c.cats = cats
    #c.name = name
    c.releasedate = releasedate
    c.introduction = introduction
    c.review = review
    c.iosurl = iosurl
    c.andurl = andurl
    c.pcurl = pcurl
    c.pictureurl = pictureurl
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

