label chapter5:

    image shadowman run:
        animation
        "default character test" # Replace this with a better picture
        xalign 0.0
        linear 1.0 xalign 1.0
        #zorder 0.5
    show Stella at slightleft
    s "Who's idea was this again?"

    show Elliot
    e "I think it was the guy in the tavern's recommendation."

    s "Yeah, but who agreed to this?"

    show Zach at slightright
    z "We all did."

    s "Well {i}that{/i}... was a mistake. I... need... water."
    #Drop transition

    e "Here Stella, I brought enough for everyone."

    s "..."

    s "This tastes like its been in the car for months."

    e "Do you want it or not."

    s "Yes! Sorry! I want it!"

    z "Elliot? Where are we on the hiking trail?"

    e "Huh? How should I know?"

    z "You were the one in charge of grabbing a map at the trailhead!"

    e "Whose idea was that?"

    #TO DO: ADD CHOICE HERE

    e "Well, the damage has been done. Now we should probably focus on getting back."

    z "Do you know the way back?"

    e "I think I remember most of the path that we took. But we {i}have{/i} been
        hiking for a couple miles now."

    e "I don't know if I remember everything."

    s "Well, let's get moving. I don't want to spend another minute without cell service."

    z "Uhg. I feel so bad that all of your followers haven't seen your face in two hours."

    #Time pass transition(clock sound and swirl) or naration?

    s "Face it. We're lost."

    e "No we are not! The trail head should be half a mile ahead."

    s "But you said that five miles ago!"

    show shadowman at offscreenleft with moveinleft
    hide shadowman

    s "*{i}Visibly scared{/i}* Did anyone just see that?!"

    e "See what?"

    s "I don't know! It was moving to fast for me to make out."

    e "I didn't see anything."

    s "Seriously? How useless can you be?"

    #In the script, it says to make a choice here, but it is not fleshed out.

    e "..."

    z "Hey, that was {i}not{/i} okay Stella. Apologize."

    s "I... I'm sorry"

    show shadowman at offscreenright with moveinright
    hide shadowman

    e "Okay, I saw it that time."

    z "I did too, but where did it go?"

    show shadowman behind Elliot, Stella, Zach

    s "Guys, I think whatever it is... it's right behind us."

    z "What do we do??"

    e "I don't think we can outrun it."

    s "I don't need to be faster than it, I just need to be faster than you two, right?"

    e "That won't matter if it's a wolf, they hunt in packs. So there many be more close by."

    z "So what do we do? Play dead?"

    e "We don't have enought information! We'll just have to see what it is..."

    z "What if that spooks it?"

    e "Well, I hope you don't have any regrets in life."

    s "Wait! I don't want to die! Not without being honest about..."

    lum "Who's dying now?"

    hide shadowman
    show lumberjack behind Elliot, Stella, Zach

    s "Eek!"

    lum "I haven't seen many people this far into the woods in a while."

    lum "What brings you out here?"

    z "We were just hiking and got lost. What are you doing out here?"

    lum "Me? I live out here. Have been for about... eh I forget."

    s "You live out here?"

    lum "Is it not normal for a lumberjack to live out in the woods?"

    s "Maybe, like a hundered years ago."

    e "Excuse me, but are we close to town?"

    lum "The closets town is about 10 miles from here."

    e "Oh no. I'm sorry guys."

    s "No wonder my legs feel like pudding."

    z "I feel like I should introduce myself. I'm Zach"

    e "I'm Elliot."

    s "Stella."

    lum "I'm... Who am I again? It's been so long since I've talked to anyone that
        I haven't really needed a name."

    z "When's like last time you talked to somebody?"

    lum "Hmm... Probably about 20 years ago."

    s "20 YEARS?!" (multiple=3)
    e "20 YEARS?!" (multiple=3)
    z "20 YEARS?!" (multiple=3)

    s "I haven't even been {i}alive{/i} 20 years!"

    e "I can't imagine being alone for that long."

    z "Sorry to impose, but could you perhaps lead us in the right direction towards Timberland?"

    lum "I would, lad."

    z "(Lad?)"

    lum "But it seems you are all tired and hungry. You probably won't be able
        to make it back tonight."

    lum "Or at least in one piece."

    s "In once piece? *scared*"

    lum "Why don't you all come over to my place and rest. I wouldn't mind..."

    lum "Mind uh..."

    lum "..."

    lum "GUIDE! That's the word I'm looking for!"

    s "I wish I was that happy remembering diction."

    lum "Diction? What's that?"

    z "... Anyways, you were saying?"

    lum "Oh right, I don't mind being your guide back to Timberland tomorrow."

    lum "But you should rest today. Espically the young lady here."

    s "What are you talking about? I'm fine... *collapses*"
    #idk how to make this really happen in the game

    z "Stella!" (multiple=2)
    e "Stella!" (multiple=2)

    lum "Don't worry, she'll come to. Just a bit fatigued. If I had to guess, she's
        probably never exerted herself this much. That, and she locked her knees."

    z "What does that have to do with anything?"

    lum "Locking your knees restricts the blood flow in your legs, causing people to faint."

    z "For a man who doesn't know the word 'diction' means, you sure know a lot."

    e "Let's stop standing here and help her! I'll carry her. Can you lead us to your... house... cabin, wherever you live?"

    lum "Sure! Follow me."

    jump chapter6
