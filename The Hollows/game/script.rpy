define e = Character("Elliot", who_color="4287f5")
define s = Character("Stella", who_color="ef42f5")
define z = Character("Zach", who_color="42f584")
define bm = Character("Boisterous Man", who_color="e62222")

$ ownRoom
$ groupRoom

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

#Example Animation
#image character change:
    #animation
    #"default character test"
    #xalign 0.0
    #pause 1
    #"angry character test"
    #linear 5.0 xalign 1.0
    #pause 1
    #repeat 2
#End Example Animation

# The game starts here.
label start:

    ## This is an example of showing multiple characters talking simultaneously
    ##style multiple2_say_window:
        ##xsize 500
        ##background None

    ##style block1_multiple2_say_window:
        ##xalign 0.0

    ##style block2_multiple2_say_window:
        ##xalign 0.5

    ##s "Test character 1" (multiple=2)
    ##e "Test character 2" (multiple=2)
    ## End example ------------------------------------------------------------

    #Show the Animation Example
    #"Start example"
    #show character change:
    #pause
    #hide character change
    #"End example"
    #End Animation Example

    scene bg car

    s "*Pulls out a ridiculously large map that blocks part of Zach's view*"

    show Stella at slightright
    with dissolve

    s "Is this the place?"

    show Zach at slightleft
    with dissolve

    z "HEY! I'm driving here. Put that away."

    "*Camera shake, Car swerves, Zach stops the car*"
    show bg car with hpunch

    s "Well, MAYBE if you knew where you were going, I wouldn't have to pull out a map."

    s "You know, this is just like that time we went on that road trip to see Aunt Kathrine.
        You refused to listen to me, and remember where we ended up?"

    s "Up in some rando's trailer park home, eating five flavors of caramelized sushi that, mind you,
        he got from a local gas station! I still can't get that eight-day old fish flavor outta my mouth."

    show Elliot at center
    with dissolve

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

    hide Elliot
    hide Zach
    hide Stella

label Timberland:
    #Shows some towns people who look disoriented

    show bg timberland
    with fade

    show Elliot at slightleft
    with dissolve
    e "...Anyone else think it's a little strange here? It's like everyone's just
    wandering around aimlessly... almost like they're mindless."

    show Stella at slightright
    with dissolve
    s "Sounds like Zach would fit right in."

    show Zach at center
    with dissolve
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

    hide Elliot

label Tavern:
    show bg tavern
    with fade

    show Elliot at slightright
    with dissolve


    # These display lines of dialogue.

    e "And I'll have the Bear Brain Soup."

    show Stella at slightleft
    with dissolve

    s "Who comes up with these recipes?"

    e "Where is your sense of adventure now?"

    e "But at least it looks like these zombie-like people can understand us."

    e "I wish they could communicate with us though."

    bm "Fantastic soup again Margaret!"

    e "It sounds like there is someone sane in this town afterall."
    #Line in the doc says "You guys hear that? Someone {i}actually{/i} sane in this town?"

    show Zach at center
    with dissolve

    z "I don't think anyone who likes the soup of the day here could be considered sane."
    #Goes over to a man whose cheeks are flushed

    z "Excuse me."

    hide Stella
    hide Elliot

    show Boisterous Man at left
    with dissolve

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
    show bg tavern

    z "So why are you here?"

    bm "Because that's my wife behind the counter."

    "The man gestures to the waitress from earlier"
    #Zoom if possible

    z "Her?"

    bm "Yeah, aint she a beaut?"

    show Stella at slightright
    with moveinright

    s "I guess it’s true that love has no bounds. Unless there’s something funky in that drink…"

    bm "I can assume you I'm drinking Root Beer"

    s "Right..."

    hide Stella
    with moveoutright

    bm "She wasn't always hollow, or that's what I call it at least."

    bm "One day I left for uh, work, and she went on a walk. When I came home she was like this."

    jump ontrack

label whathappened:
    show bg tavern

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
    show bg tavern

    z "Do you know anything about this amulet?"

    bm "Not a clue. I mean, there's not much to go on."

    bm "There are plenty of trees in the world. The 'H' probably stands for something."

    bm "But I am sure you could have figured all that out on your own. Why ask me?"

    z "We are actually here looking for my family."

    bm "Your family?"

    z "My biological family are locals here. I wanted to see them and ask why I was put up for adoption"

    show Stella at slightright
    with moveinright

    s "And {i}I've{/i} been telling you that you might not want to know the answer to that."

    s "Furthermore, what if your biological parents don't want to see you?"

    z "..."

    s "But go ahead...ignore me. It's not like I know anything."

    hide Stella
    with moveoutright

    jump ontrack

label ontrack:
    show bg tavern

    z "We should probably introduce ourselves. I'm Zack, and this..."

    show Elliot at slightright
    with dissolve

    z "This is my friend Eliiot and this..."

    show Stella at slightleft
    with dissolve

    z"is my sister Stella."

    e "We were also looking for a place to stay the night. Do you have any recommendations?"

    bm "Yeah, this bar also runs a motel that is right behind this building. My wife can ring up a room for you."

    bm "It's $70 a night for a room, two beds and...uh...well there WAS cable TV."

    bm "But people stopped visiting the town once people started going hollow. The Motel couldn't afford to keep the cable."

    z "Um..."

    bm "It's a travesty! I know that business is bad, but what about the rest of us who sneak in to watch the college ball games!?"

    bm "I can't take it anymore, this is unfair, an outrage, total anarchy!"

    e "Why don't you upgrade your TV service yourself?"

    bm "Do you know how much that would cost me? In this rundown hovel?"

    bm "There is {i}no{/i} business to be had here! Business has been stalled for over 20 years!"

    e "..."

    e "I'm sorry I asked."

    z "We'll be taking one room."

    s "I don't think so. You think I'm staying in the same room as you two {i}clowns{/i}?"

    menu:

        "You can have your own room":
            z "{i}Fine{/i}, you can have your own room."

            s "Yay! Thank you Zach!"
            ownRoom = True
        "If you pay for it":
            z "You can have it if you pay for it."

            s "..."

            z "I brought enough money for Elliot and myself."

            z "I mean, the least you could have done is brought some money for yourself if you were going to hide in my trunk."

            s "..."

            s "Fine"
             groupRoom = True

    bm "How long are you going to be in town?"

    z "By the looks of it, not long. I mean, I can't exactly find my biological parents if I can't even talk to anyone in town."

    bm "You should at least take a look at the nearby hiking trails before you leave."

    bm "It's probably the only redeeming part of the town. The trail takes you up the (insert name) Mountain to one of the most beautiful views."

    z "I mean we might as well take a look while we're here."

    e "I love hiking! Let's go!"

    s "hmpf, I guess I'll tag along."

    bm "Perfect..."

    hide Elliot
    hide Stella
    hide Zach
    hide Boisterous Man

label MotelNight1:
    show bg night motel
    with fade

    if ownRoom:
        jump zeRoom
    elif groupRoom:
        jump gRoom


label zeRoom:
    show bg night motel
    with fade
    #Zach unlockes Room 308
    #The room reeks of old mildew and strawberry flavored bubblegum

    show Elliot at slightright
    with dissolve

    e "So, Zach you never actually explained much of this trip's purpose to me."
    show Zach at slightleft
    with dissolve

    z "Huh? I told you about it shortly after we left my house. How did you already forget?"

    e "Haha, about that... I uh kinda... well um... slept most of the trip here"

    z "What are you talking about? I saw you with your eyes open!"

    e "I mean, they probably were. Every since I ate those fried oysters last Monday, my sleep cycle has been kinda weird."
    e "The other day I found my pillow in the fridge next to the mustard-stained cheese. I've never been one to sleep walkx, but I think I am now."

    z "...{i}Riiiight{\i}. Um.. well, since we're on the topic: Do you think you're going to get any sleep tonight?"
    z "You should be somewhat well-rested if we're going hiking tomorrow. I don't need you collapsing on us."

    e "I'd say a midnight snack should do the trick. Got anything?"

    z "I don't. I was in such a rush today that I didn't even think about that. I even forgot to pack my toothbrush!"
    z "But feel free to check the vending machines."

    e "Works for me!"

    z "Before you go... *sigh* He's already gone. That kid sure has a one-track mind."
    jump vending1

label vending1:
    "*Elliot works his way to a section of 3 vending machines. All of them are empty except for the
    one on the far end that has 1 Oogle Boogle Nutty Candy Bar left in it. Stella’s at the vending
    machine impatiently waiting for the candy bar to fall)*"

    show Stella at slightleft
    with dissolve

    s "*mutterting to herself* Come on! I don't have all day! *kicks the vending machine*"
    s "UGH, it won't budge *screams out of frustration*"

    show Elliot at slightright
    with dissolve

    e "Hey Stella! What are you doing out here? I figured you would've locked yourself to the confinement of your room by now."

    s "What does it look like?! I'm {i}trying{/i} to get something to eat!"

    e "Still hungry? You didn't really touch your smoked cow tongue."

    s "Yeah, I should've just given it to you. And now this dang machine won't give me my candy bar!"
    s "I paid for the dang thing! Can you help me?"


    e "Sure, give me a sec. *picks up the vending machine and slams it down, candy bar falls down*"
    #could use camera shake here again

    show Zach
    with dissolve

    z "*comes out of his room* What was that?!"

    e "What was what?"

    z "The noise!"

    s "That was Elliot's rage agaisnt the vending machine."

    e "Rage? You were the one kicking it earlier."

    s "Whatever. *picks up the candy bar and starts walking away and pauses, under her breath* Thanks Elliot. *continues walking*"

    e "I think that's the first time time I've ever heard her say thank you. Should I should 'you're welcome'?"

    z "I think she already knows."
    z "Besides, you've already caused enough noise tonight. We should probably get back to the room."

    e "But I'm still hungry!"

    z "Then you should've grabbed that candy bar before Stella did. *smirks* *walks towards the room*"
    z "Come on you big lug."

    e "Ok..."
    e "I guess I'm just happy that Stella has something to eat."

    jump MotelNight1Pt2

label MotelNight1Pt2:
    show Elliot at slightleft

    e "Well, I guess I'm going hungry tonight."

    show Zach at slightright

    z "*jokingly* I mean, there's that chewed gum stuck underneath that coffee table, but I wouldn't...."

    z "*sigh* Elliot, where's the gum?"

    z "That kid sure is something else. *Turns off the light and goes to bed*"
    #FADE OUT

    jump MotelMorn1

label gRoom:
    #Zach unlockes Room 308
    #The room reeks of old mildew and strawberry flavored bubblegum

    show Stella at slightleft

    s "So Zach, why do you even want to find your biological family? I mean, is our family not good enough for you?"

    show Zach at slightright

    z "Hey! I never said that!"

    s "Then why?"

    z "Because I want to know more about myself. It's like there's a part of me missing and I have no way of finding it."

    s "Okay genius, if there is 'no way of finding it' then why are we in this creepy town?"

    show Elliot

    e "Yeah, I was wondering that too."

    z "I told you everything in the car!"

    e "You know I was sleeping most of the ride, right?"

    z "*sigh*"

    e "I really should get a bite to eat before I head to bed for the night. *sees the gum under the table and starts reaching for it*"

    s "Gross! I should really get you a dog cone. Come on, we're going to the vending machines. I saw some outside."

    jump vending2

label vending2:
    show Elliot at slightright
    show Stella at slightleft

    "Elliot and Stella work their way to an area with 3 vending machines. All of them are empty except for one with
    1 Oogle Boogle Nutty Candy Bar in it."

    e "Looks like there's one left..."

    "Elliot and Stella split the bar"

    jump MotelMorn2

label MotelMorn1:
    "*Stella bangs on the door*"

    s "Rise and shine sleepyheads!!"

    show Zach at slightright

    z "Just give us 5 minutes Stel. We're almost ready."

    s "Oh you're awake? I wasn't expecting that."

    z "Suprised?"

    s "Well yeah! You're never up this early. You must be {i}really{/i} excited for this hiking trip."

    show Elliot at slightleft
    show Stella

    e "*opens the door* Believe me, he is. He's been up since 5:37 a.m."

    s "Yeesh, that explains why Zach looks like a..."
    s "You know what? Nevermind."

    s "Zach you ready yet?"

    z "Almost, I need to talk to Elliot quick though."

    z "Last night, you were outta this room so quick that I didn't get to tell you why I wanted to go on this trip
    in the first place."

    s "Actually. I'd like to know that too."

    e "Oh yeah... Sorry about that. When my minds on food, I kinda forget about my surroundings."

    style multiple2_say_window:
        xsize 500
        background None

    style block1_multiple2_say_window:
        xalign 0.0

    style block2_multiple2_say_window:
        xalign 0.5

    s "We know!" (multiple=2)
    z "We know!" (multiple=2)

    s "TALKING TALKING TALKING"



    # This ends the game
    return
