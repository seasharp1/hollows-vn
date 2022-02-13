label chapter1:
    scene bg car
    play music "audio/upbeatThemeLoop.wav" fadein 1.0

    "We've been driving for hours, the three of us.
        Elliot, the big guy in the back fast asleep, and a good friend of mine."

    "Then there's Stella, who generously volunteered to navigate, even though no one asked."

    "And your pilot this afternoon is me, Zach, the most dashing, charming man you'll ever meet."

    "*{i}My thoughts are cut off as Stella pulls out a giant map that blocks my view.{/i}*"

    show Stella at slightright
    with dissolve

    s "Is this the place?"
    show Stella

    show Zach at slightleft
    with dissolve

    z "HEY! I'm driving here. Put that away."

    show bg car with hpunch
    "*{i}Car swerves, Zach stops the car{/i}*"

    s "Well, {i}MAYBE{/i} if you knew where you were going, I wouldn't have to pull out a map."

    s "You know, this is just like that time we went on that road trip to see Aunt Kathrine.
        You refused to listen to me, and remember where we ended up?"

    s "Up in some rando's trailer park home, eating five flavors of caramelized sushi that, mind you,
        he got from a local gas station! I still can't get that eight-day old fish flavor outta my mouth."

    show Elliot at center
    with dissolve

    e "I'm not a rando, I'm his best friend!"

    e "And that was some good sushi!"

    z "I'm with Stel on this one. You eat some of the weirdest crap I've ever seen."

    e "I can't help that I like food..."

    s "You call that food?! You can't be serious."

    z "*{i}Chuckles{/i}*"

    z "It's still better than that time he made us try jellied moose nose."

    s "Don't remind me."

    e "It was soo chewy..."

    s "I think I'm gonna hurl."

    z "Nice one, Elliot. Hey Stel, don't hurl in my car, okay?"

    s "I'm trying not to, I promise!"

    #animation with stella disapearing from view to vomit
    hide Stella
    with moveoutright
    play sound "<from 0 to 1>audio/Footsteps.wav" fadeout 1.0

    pause 0.5

    "*{i}Stella opens the car door and proceeds to vomit, revealing a tipped over sign that says
        \"Welcome to Timberland\".{/i}"

    e "Looks like you knew what you were doing after all, Zach. I guess we're in Timberland... or
        what's left of it."

    z "Did I hit that sign?"

    #"*{i}Zach and Elliot get out of the car to inspect the hood{/i}*"
    #Show elliot and zach moving off screen to inspect hood
    hide Zach
    hide Elliot
    with easeoutright
    play sound "<from 0 to 1>audio/Footsteps.wav" fadeout 1.0

    pause 0.5

    e "Well, they aren't going to miss that thing."

    e "On the bright side, we gave the town an excuss to upgrade."

    #Show main cast coming back into car
    show Stella at slightright
    show Zack at slightleft
    show Elliot at center
    with easeinright

    play sound "<from 0 to 1>audio/Footsteps.wav" fadeout 1.0
    pause 0.5

    z "The town sure looks a bit run down, don't ya think?"

    e "Maybe we should turn around."

    s "We're going. I didn't hide in a trunk for eight hours for nothing. Besides, where's
        your sense of adventure?"

    e "Not in the trunk, that's for sure."

    #"*{i}Stella rolls her eyes{/i}*"
    #Show stella annoyed

    s "How's the hood look?"

    z "Not even a dent, that wood couldn't be any more rotten."

    s "That's good. I don't think this rustbucket you drive can take much more of a beating."

    z "Yeah, she's been through a lot. She's my first car."

    s "You two need to get a room. I can't stand how you talk about that thing like it's your
        girlfriend. Or is it because you've never had a girlfriend that you talk like that?"

    #s "*{i}Snickering{/i}*"
    #show stella snickering (smug face activate)
    #could do this before previous diologue line

    z "..."

    e "A little harsh, don'tcha think, Stella?"

    s "Whatever, let's just hurry to town. I'm starving."

    z "How can you think of food after you just threw up your stomach?"

    s "It's {i}BECAUSE{/i} I threw up that I'm hungry now!"

    e "How about we get some-"

    s "Don't even finish that sentence. You're going to make me lose my appetite, so just don't."

    stop music fadeout 1.0 #stops current music
    pause 0.5

    hide Elliot
    hide Zach
    hide Stella

    jump chapter2
