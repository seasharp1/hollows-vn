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

    scene bg cerulean

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label Timberland:
        show Elliot
        e "...Anyone else think it's a little strang here? It's like everyone's
        just wandering around aimlessly... almost like they're mindless."

        show Stella
        s "Sounds like Zach would fit right in."

        show Zach
        z "Hey! *snarky comback here*" #TODO

        z "Excuse me, could you tell me..."

        #Hollow looking stranger doesn't respond, Moves past as if he doesn't see
        #him

        e "That was... {i}weird{/i}. *visibly scared*"

        s "Yeah, let's ask someone else. *visibily uncomfortable*"

        #Shows multiple hollow town's folk
        z "Well, that didn't get us anywhere."

        s "Yeah, what is up with everyone in this town? They all look like
        zombies. *Grossed out*"

        z "I guess we should look for someplace to eat and stay the night."

        s "Yes, stay the night."

        e "I saw a bar and grill about a block back the way we came."

        z "It has normal food, right?"

        e "Normal food? What do you mean? *confused*"

        s "I saw it too. It looks like it's the only restuarant in town, so
        we don't have a choice. *sigh*"

        z "Okay, let's go."

        #Zach and Stella walk off

        e "My pallet isn't {i}that{/i} bad... right?"



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
