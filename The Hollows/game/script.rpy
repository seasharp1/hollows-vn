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

    scene bg car

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    s "*Pulls out a ridiculously large map that blocks part of Zach's view*"

    show Stella at slightright

    s "Is this the place?"

    show Zach at slightleft

    z "HEY! I'm driving here. Put that away."

    "*Camera shake, Car swerves, Zach stops the car*"
    #Can use hpunch transition here, shakes the scene for 1/4 second

    s "Well, MAYBE if you knew where you were going, I wouldn't have to pull out a map."

    s "You know, this is just like that time we went on that road trip to see Aunt Kathrine.
        You refused to listen to me, and remember where we ended up?"

    s "Up in some rando's trailer park home, eating five flavors of caramelized sushi that, mind you,
        he got from a local gas station! I still can't get that eight-day old fish flavor outta my mouth."

    show Elliot at center

    e "I'm not a rando, I'm his best friend! *Elliot points to Zach*"

    e "And that was some good sushi!"

    z "I'm with Stel on this one. You eat some of the weirdest crap I've ever seen."

    e "I can't help that I like food..."

    s "You call that food?! You can't be serious."

    z "*Chuckles*"

    z "It's still better than that time he made us try jellied moose nose."

    s "Don't remind me."

    e "It was soo chewy..."

    s "I think I'm gonna hurl."

    z "Nice one, Elliot. Hey Stel, don't hurl in my car, okay?"

    s "I'm trying not to, I promise!"

    "*Stella opens the car door and proceeds to vomit, revealing a tipped over sign that says
        \"Welcome to Timberland\"."

    e "Looks like you knew what you were doing after all, Zach. I guess we're in Timberland... or
        what's left of it."

    z "Did I hit that sign?"

    "*Zach and Elliot get out of the car to inspect the hood*"

    z "It sure looks a bit run down, don't ya think?"

    e "Maybe we should turn around."

    s "We're going in. I didn't hide in a trunk for eight hours for nothing. Besides, where's
        your sense of adventure?"

    e "Not in the trunk, that's for sure."

    "*Stella rolls her eyes*"

    s "How's the hood look?"

    z "Not even a dent, that wood couldn't be anymore rotten."

    s "That's good. I don't think that rustbucket you drive can take much more of a beating."

    z "Yeah, she's been through a lot. She's my first car."

    s "You two need to get a room. I can't stand how you talk about that thing like it's your
        girlfriend. Or is it because you've never had a girlfriend that you've talked to like that?"

    s "*Snickering*"

    z "..."

    e "A little harsh, don'tcha think, Stella?"

    s "Whatever, let's just hurry to town. I'm starving."

    z "How can you think of food after you just threw up your stomach?"

    s "It's BECAUSE I threw up that I'm hungry now!"

    e "How about we get some-"

    s "Don't even finish that sentence. You're going to make me lose my appetite, so just don't."

    label Timberland:
    #Shows some towns people who look disoriented

    show Elliot
    e "...Anyone else think it's a little strange here? It's like everyone's just
    wandering around aimlessly... almost like they're mindless."

    show Stella
    s "Sounds like Zach would fit right in."

    show Zach
    z "Hey! *maybe make choice of snarky comeback here)*"

    z "Excuse me, could you tell me..."
    #Hollow looking stranger doesn't respond, moves past him as if he doesn't see him

    e "That was... {i}weird{/i}. *visibly scared*"

    s "Yeah, let's ask someone else. *visibly uncomfortable*"

    #Shows multiple hollow town's folk

    z "Well, that didn't get us anywhere."

    s "Yeah, what is up with everyone in this town? They all look like zombies. *grossed out*"

    z "I guess we should look for someplace to eat and stay the night."

    s "Stay the night?!"

    z "Yes, stay the night."

    e "I saw a bar and grill about a block back the way we came."

    z "It has normal food, right?"

    e "Normal food? What do you mean? *Confused*"

    s "I saw it too. It looks like it's the only restuarant in town, so we don't have a choice. (sigh)"

    z "Okay, let's go."

    #Zach and Stella walk off
    hide Zach
    hide Stella

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
    #Line in the doc says "You guys hear that? Someone {i}actually{/i} sane in this town?"

    show Zach at slightright

    z "I don't think anyone who likes the soup of the day here could be considered sane."
    #Goes over to a man whose cheeks are flushed

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

    bm "I haven't had a real conversation over three months now."

    s "Three months?"

    bm "That was the last time someone passed through here. I mean, we {i}are{/i} in the middle of nowhere after all."

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

        bm "Because that's my wife behind the counter."

        "The man gestures to the waitress from earlier"
        #Zoom if possible

        z "Her?"

        bm "Yeah, aint she a beaut?"

        show Stella at slightright

        #doc says Stella - "I guess it’s true that love has no bounds. Unless there’s something funky in that drink…"
        # bm says "I can assume you I'm drinking Root Beer"

        s "Right..."


        hide Stella

        bm "She wasn't always hollow, or that's what I call it at least."

        bm "One day I left for uh, work, and she went on a walk. When I came home she was like this."

        jump ontrack

    label whathappened:
        z "What happened to everyone in this town?"

        bm "Couldn't tell ya."

        bm "But I {i}do{/i} know that it started about 21 years ago. That was when the first person went hollow."

        bm "I think it was someone who was visiting their family. Started acting weird."

        bm "At first we thought they were just startled after seeing a bear or something."

        bm "But as the days and weeks went on, more and more people started acting the same way."

        z "Hollow?"

        bm "Yeah, thats what we call 'em. The people around these parts used to be lively and clamorous."

        bm "My man Earl over there in the red tux used to be the liveliest man around."

        bm "He used to play gigs in the Tavern every Tuesday."

        z "I see..."

        bm "I sure miss the noise. I used to hate it, but now? Heh, I'd do anything to get it back."


        jump ontrack

    label amulet:
        z "Do you know anything about this amulet?"

        bm "Not a clue. I mean, there's not much to go on."

        bm "There are plenty of trees in the world. The 'H' probably stands for something."

        bm "But I am sure you could have figured all that out on your own. Why ask me?"

        z "We are actually here looking for my family."

        bm "Your family?"

        z "My biological family are locals here. I wanted to see them and ask why I was put up for adoption"

        show Stella at rightish

        s "And I've been telling you that you might not want to know the answer to that!"

        s "Furthermore, what if your biological parents don't want to see you?"

        z "..."

        s "But go ahead...ignore me. It's not like I know anything."

        hide stella

        jump ontrack

    label ontrack:

        z "We should brobably Introduce ourselves. I'm Zack, and this..."

        show Elliot at slightright

        z "This is my friend Eliiot and this..."

        show Stella at slightleft

        z"is my sister Stella."

        e "We were also looking for a place to stay the night. Do you have any recommendations."

        bm "Yeah, this bar also runs a motel that is right behind this building. My wife can ring up a room for you."

        bm "It's $70 a night for a room, two beds and...uh...well there WAS cable TV."

        bm "But people stopped visiting the town once people started going hollow. The Motel couldn't afford to keep the cable."

        z "Um..."

        bm "It's a travesty! I know that business is bad, but what about the rest of us who sneak in to watch the college ball games!?"

        bm "I can't take it anymore, this is unfair, an outrage, total anarchy!"

        e "Why don't you upgrade your TV service yourself?"

        bm "Do you know how much that would cost me? In this rundown hovel?"

        bm "There is no business to be had here! Business has been stalled for over 20 years!"

        e "..."

        e "I'm sorry I asked."

        z "We'll be taking one room."

        s "I don't think so. You think I'm staying in the same room as you tow clowns?"

        menu:

            "You can have your own room":
                z "Fine, you can have your own room."

                s "Yay! Thank you Zach!"


            "If you pay for it":

                z "You can have it if you pay for it."

                s "..."

                z "I brought enough money for Elliot and myself."

                z "I mean, the least you could have done is brought some money for yourself if you were going to hide in my trunk."

                s "..."

                s "Fine"

        bm "How long are you going to be in town?"

        z "By the looks of it, not long. I mean, I can't exactly find my biological parents if I can't even talk to anyone in town."

        bm "You should at least take a look at the nearby hiking trails before you leave."

        bm "It's probably the only redeeming part of the town. The trail takes you up the Mountain to one of the most beautiful views."

        z "I mean we might as well take a look while we're here."

        e "I love hiking! Let's go!"

        s "hmpf, I guess I'll tag along."

        bm "Perfect..."



    # This ends the game.

    return
