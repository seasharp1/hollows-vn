# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elliot")
define s = Character("Stella")
define z = Character("Zach")
define bm = Character("Boisterous Man")

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg car1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    s "*pulls out a rediculously large map that blocks part of Zach's view*"

    s "Is this the place?"

    z "HEY! I'm driving here. Put that away"

    "*Elliot wakes up from the car swerving. Zach stops the car*"

    s "Well, MAYBE if you knew where you were going, I wouldn't have to pull out a map."

    s "You know, this is just like that time we went on that road trip to see Aunt Katherine."

    s "You refused to listen to me, and remember where we ended up?"

    s "Up in some rando's trailer park home, eating five flavors of caramelized sushi that,
        mind you, he got from a local gas station!"

    s "I still can't get that eight-day old fish flavor outta my mouth."

    e "I'm not a rando, I'm his best friend! *Elliot points to Zach*"

    e "And that was some good sushi!"

    z "I'm with Stel on this one. You eat some of the weirdest crap I've ever seen."

    e "I can't help that I like food. . ."

    s "You call that food!? You can't be serious."

    z "*Chuckles* It's still better than that time he made us try jellied moose nose."

    s "Don't remind me."

    e "It was soo chewy. . ."

    s "I think I'm gonna hurl. *Her face turns visibly green*"

    z "Nice one, Elliot. Hey Stel, don't hurl in my car, okay?"

    s "I'm trying not to, I promise!"

    s "*Stella opens the car door and proceeds to vomit, revealing a tipped over sign that says \"Welcome to Timberland\""

    e "Looks like you knew what you were doing after all Zach. I guess we're in Timberland. . . or, what's left of it."

    z "Did I hit that sign?"

    "*Zach and Elliot get out of the car to inspect the car hood*"

    s "*Still throwing up*"

    z "It sure looks a bit run down, don't ya think?"

    e "Maybe we should turn around?"

    s "We're going in. I don't hide in a trunk for eight hours for nothing."

    s "Besides, where's your sense of adventure?"

    e "Not in the trunk, that's for sure."

    s "*Rolls her eyes* How's the hood look?"

    z "Not even a den't, that wood couldn't be any more rotten."

    s "That's good. I don't think that rustbucket you drive can take much more of a beating."

    z "Yeah, she's been through a lot. She's my first car."

    s "You two need to get a room. I can't stand how you talk about it like it's your girlfriend."

    s "*Annoyed* Or is it because you've never had a girlfriend that you've talked to like that? *Snickering*"

    z ". . ."

    e "A little harsh, don'tcha think Stella?"

    s "Whatever, let's just hurry to town. I'm starving."

    z "How can you think of food after you just threw up your stomach?"

    s "It's BECAUSE I just threw up that I'm hungry now."

    e "How about we get some. . ."

    s "Don't even finish that sentence. You're gonna make me lose my appetite, so just. . . don't."

label Tavern:
    show Elliot

    #image launch = Movie(play="watercolor_test.gif", pos=(10, 10), anchor=(0, 0))


    # These display lines of dialogue.

    e "And I'll have the Bear Brain Soup."

    show Stella at slightleft

    s "Who comes up with these recipes?"

    e "Where is your sense of adventure now?"

    e "But at least it looks like these zombie-like people can understand us."

    e "I wish they could communicate with us though."

    bm "Fantastic soup again Margaret!"

    e "It sounds like there is someone sane in this town afterall."

    show Zach at slightright

    z "I don't think anyone who likes the soup of the day here could be considered sane."

    z "Excuse me."

    hide Stella

    hide Elliot

    show Boisterous Man at slightleft

    bm "Well I'll be! Am I hallucinating or are you talkin' to me?"

    menu:
        "Well I'll be! Am I hallucinating or are you talkin' to me?"

        "You're hallucinating":
            "I'm not real. I'm a ghost. oooOOOooo"

        "I'm talkin' to you":
            "I'm talking to you, but you're facing the wrong way"

    bm "Rude comment here"

    bm "I haven't had a real conversation over three moths now."

    s "Three months?"

    bm "That was the last time someone passed through here. I mean, we are in the middle of nowhere after all."

    bm "Not much reason for people to come visit unless you have family here."

    "The Boisterous Man glances at the waitress"

    bm "But then again, who would want to visit their family here?"

    bm "Everyone acts like they tasted somethin' sour n' can't talk!"

    "Sounds like this guy has been here for a while, nows a good chance to ask some questions"

    menu:
        "Sounds like this guy has been here for a while, nows a good chance to ask some questions"

        "Why are you here?":
            jump whyareyouhere

        "What happened to the people":
            jump whathappened

        "Do you know anything about this amulet?":
            jump amulet

    label whyareyouhere:
        z "So why are you here?"
        jump ontrack

    label whathappened:
        z "What happened to everyone in this town?"
        jump ontrack

    label amulet:
        z "Do you know anything about this amulet?"
        jump ontrack

    label ontrack:
        "Here!"



    # This ends the game.

    return
