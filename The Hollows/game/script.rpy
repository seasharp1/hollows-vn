define e = Character("Elliot", who_color="4287f5")
define s = Character("Stella", who_color="ef42f5")
define z = Character("Zach", who_color="42f584")
define bm = Character("Boisterous Man", who_color="e62222")
define lum = Character("Lumberjack", who_color="cc5500")
##define me = Character("[povname]") ## Use this for named main character

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform hop:
    linear 0.1 ypos 50
    linear 0.1 ypos 0

# This is for displaying multiple character's dialogue simultaneously ---
# Use (multipe=3) after dialogue on same line to use this
style multiple3_say_window:
    xsize 500
    background None

style block1_multiple3_say_window:
    xalign 0.0

style block2_multiple3_say_window:
    xalign 0.5

style block3_multiple3_say_window:
    xalign 1.0
#------------------------------------------------------------------------

# Stranger walking animation used in second scene -----------------------
image stranger walking:
    animation
    "default character test" # Replace this with a better picture
    xalign 0.0
    linear 2.0 xalign 1.0
#-------------------------------------------------------------------------

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
#End Example Animation ---------------------------------------------------

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

#Show the Animation Example -----------------------------------------------
#"Start example"
#show character change:
#pause
#hide character change
#"End example"
#End Animation Example ----------------------------------------------------

## Begin User Input Test --------------------------------------------------
#"Hmm, what is my name again..."
#python:
#    povname = renpy.input("Name thyself: ", length=32)
#    povname = povname.strip()
#
#    if not povname:
#        povname = "Unidentified User"
#"Hello [povname]"
## End User Input Test ----------------------------------------------------

# The game starts here. \'O'/
label start:

    scene bg car

    "We've been driving for hours, the three of us.
        Elliot, the big guy in the back fast asleep, and a good friend of mine."

    "Then there's Stella, who generously volunteered to navigate, even though no one asked."

    "And your pilot this afternoon is me, Zach, the most dashing, charming man you'll ever meet."

    "*{i}My thoughts are cut off as Stella pulls out a giant map that blocks my view.{/i}*"

    "My thoughts are cut off as Stella pulls out a giant map that blocks my view."

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

    "*{i}Stella opens the car door and proceeds to vomit, revealing a tipped over sign that says
        \"Welcome to Timberland\".{/i}"

    e "Looks like you knew what you were doing after all, Zach. I guess we're in Timberland... or
        what's left of it."

    z "Did I hit that sign?"

    #"*{i}Zach and Elliot get out of the car to inspect the hood{/i}*"
    #Show elliot and zach moving off screen to inspect hood

    e "Well, they aren't going to miss that thing."

    e "On the bright side, we gave the town an excuss to upgrade."

    #Show main cast coming back into car

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

    hide Elliot
    hide Zach
    hide Stella

label Timberland:
    show bg timberland
    with fade

    #Shows some towns people who look disoriented

    show Elliot at slightleft
    with dissolve
    e "...Anyone else think it's a little strange here? It's like everyone's just
    wandering around aimlessly... almost like they're mindless."

    show Stella at slightright
    with dissolve
    s "Sounds like Zach would fit right in."

    show Zach at center
    with dissolve
    z "Hey, rude!"

    z "*{i}Zach turns to someone walking nearby{/i}*"

    z "Excuse me, could you tell me..."

    show stranger walking:
    "*{i}The stranger walks past without stopping{/i}*"
    hide stranger walking

    e "That was... {i}weird{/i}."

    s "Yeah, let's ask someone else."

    show stranger walking:
    "*{i}There is still no response from the townsfolk{/i}*"
    hide stranger walking

    z "Well, that didn't get us anywhere."

    s "Yeah, what is up with everyone in this town? They all look like zombies."

    z "I guess we should look for some place to eat and stay the night."

    s "{i}Stay the night?!{/i}"

    z "Yes, stay the night."

    e "I saw a bar and grill about a block back the way we came."

    z "It has normal food, right?"

    e "Normal food? What do you mean?"

    s "I saw it too. It looks like it's the only restuarant in town, so we don't have a choice. *{i}sigh{/i}*"

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

    e "And I'll have the Bear Brain Soup."

    show Stella at slightleft
    with dissolve

    s "Who comes up with these recipes?"

    e "Where's your sense of adventure now?"

    e "But at least it looks like these zombie-like people can understand us."

    e "I wish they could communicate with us though."

    bm "Fantastic soup again Margaret!"

    e "You guys hear that? Someone is {i}actually{/i} sane in this town?"

    show Zach at center
    with dissolve

    z "I don't think anyone who likes the soup of the day here could be considered sane."

    z "*{i}Zach walks over to the man in question{/i}*"

    hide Stella
    hide Elliot

    z "Excuse me..."

    show Boisterous Man at left
    with dissolve

    bm "Well I'll be! Am I hallucinating or are you talkin' to me?"

    menu:
        bm "Well I'll be! Am I hallucinating or are you talkin' to me?"

        "You're hallucinating":
            z "I'm not real. I'm a ghost! {i}oooOOOooo{/i}"

            bm "Ha, I like to think I know a ghost when I see one, and you aint it."

        "I'm talkin' to you":
            z "I'm really talking to you..."

    bm "Well call me surprised, I haven't had a real conversation over three months now."

    s "Three months?"

    bm "That was the last time someone passed through here.
        I mean, we {i}are{/i} in the middle of nowhere after all."

    bm "Not much reason for people to come visit unless you have family here."

    "*{i}The Boisterous Man glances at the waitress{/i}"

    bm "But then again, who would want to visit their family here?"

    bm "Everyone acts like they tasted somethin' sour n' can't talk!"

    "*{i}It appears like this guy has been here for a while, might be a good chance to ask some questions{/i}"

    menu:
        "*{i}It appears like this guy has been here for a while, might be a good chance to ask some questions{/i}"

        "Why are you here?":
            jump whyareyouhere

        "What happened to the people":
            jump whathappened
        # I see no mention of an amulet before this point ------------------
        "Do you know anything about this amulet?":
            jump amulet

label whyareyouhere:

    z "So why are you here?"

    bm "Because that's my wife behind the counter."

    "*{i}The man gestures to the waitress from earlier{/i}"

    show bg tavern with dissolve:
        zoom 1.5

    hide Boisterous Man
    hide Zach

    show Waitress
    with dissolve

    z "Her?"

    bm "Yeah, aint she a beaut?"

    hide Waitress

    show bg tavern with dissolve:
        zoom 1.0

    show Stella at slightright
    with moveinright

    show Boisterous Man at left

    show Zach at center

    s "I guess it’s true that love has no bounds. Unless there’s something funky in that drink..."

    bm "I can assure you I'm drinking Root Beer"

    s "Right..."

    hide Stella
    with moveoutright

    bm "She wasn't always like this, hollow I mean, or that's what I call it at least."

    bm "One day I left for uh, work, and she went on a walk. When I came home she was like this."

    jump ontrack

label whathappened:

    z "What happened to everyone in this town?"

    bm "Couldn't tell ya..."

    bm "But I {i}do{/i} know that it started about 21 years ago. That was when the first person went hollow."

    bm "I think it was someone who was visiting their family. Started acting weird."

    bm "At first we thought they were just startled after seeing a bear or somethin."

    bm "But as the days and weeks went on, more and more people started acting the same way."

    z "Hollow?"

    bm "Yeah, thats what I like to call 'em. The people around these parts used to be pretty lively folk."

    bm "My man Earl over there in the red tux used to be the liveliest man around."

    bm "He used to play gigs in the tavern every Tuesday."

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

    z "We should probably introduce ourselves. I'm Zack, and this..."

    show Elliot at slightright
    with dissolve

    z "This is my friend Elliot and this..."

    show Stella at slightleft
    with dissolve

    z"is my sister Stella."

    e "We were also looking for a place to stay the night. Do you have any recommendations?"

    bm "Yeah, this bar also runs a motel that is right behind this building.
        My wife can ring up a room for you."

    bm "It's $70 a night for a room, two beds and...uh...well there WAS cable TV."

    bm "But people stopped visiting the town once people started going hollow.
        The Motel couldn't afford to keep the cable."

    z "Um..."

    bm "It's a travesty! I know that business is bad, but what about the rest
        of us who sneak in to watch the college ball games!?"

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
            $ ownRoom = True
            $ groupRoom = False
        "If you pay for it":
            z "You can have it if you pay for it."

            s "..."

            z "I brought enough money for Elliot and myself."

            z "I mean, the least you could have done is brought some money for
                yourself if you were going to hide in my trunk."

            s "..."

            s "Fine, I'll share the room."
            $ groupRoom = True
            $ ownRoom = False

    bm "How long are you going to be in town?"

    z "By the looks of it, not long. I mean, I can't exactly find my biological
        parents if I can't even talk to anyone in town."

    bm "You should at least take a look at the nearby hiking trails before you leave."

    # This line needs a name for the Mountain --------------------------------
    bm "It's probably the only redeeming part of the town. The trail takes you
        up the (insert name) Mountain to one of the most beautiful views."

    z "I mean we might as well take a look while we're here."

    e "I love hiking! Let's go!"

    s "Hmpf, I guess I'll tag along."

    bm "Perfect..."

    hide Elliot
    hide Stella
    hide Zach
    hide Boisterous Man

    if ownRoom:
        jump zeRoom
    else:
        jump gRoom

# Own room
label zeRoom:
    show bg night motel
    with fade

    "*{i}Zach unlockes Room 308. The room reeks of mildew and strawberry flavored bubblegum{/i}*"

    show Elliot at slightright
    with dissolve

    e "So Zach, you never actually explained much of this trip's purpose to me."
    show Zach at slightleft
    with dissolve

    z "Huh? I told you about it shortly after we left my house. How did you already forget?"

    e "Haha, about that... I uh kinda... well um... slept most of the trip here"

    z "What are you talking about? I saw you with your eyes open!"

    e "I mean, they probably were. Every since I ate those fried oysters last
        Monday, my sleep cycle has been kinda weird."

    e "The other day I found my pillow in the fridge next to the mustard-stained
        cheese. I've never been one to sleep walkx, but I think I am now."

    z "...{i}Riiiight{\i}. Um.. well, since we're on the topic, do you think
        you're going to get any sleep tonight?"

    z "You should be somewhat well-rested if we're going hiking tomorrow. I
        don't need you collapsing on us."

    e "I'd say a midnight snack should do the trick. Got anything?"

    z "I don't. I was in such a rush today that I didn't even think about that.
        I even forgot to pack my toothbrush!"

    z "But feel free to check the vending machines."

    e "Works for me!"

    z "Before you go... *{i}sigh{/i}* He's already gone. That kid sure has a one-track mind."

    jump vending1

label vending1:
    show bg vending machine
    with fade

    "*{i}Elliot works his way to a section of 3 vending machines. All of them are
        empty except for the one on the far end that has 1 Oogle Boogle Nutty Candy Bar left in it.{/i}*"

    "*{i}Stella’s at the vending machine impatiently waiting for the candy bar to fall{/i}*"

    show Stella at slightleft
    with dissolve

    s "Come on! I don't have all day! *{i}She kicks the vending machine{/i}*"

    s "UGH, it won't budge *{i}She lets out a frustrated scream{/i}*"

    show Elliot at slightright
    with dissolve

    e "Hey Stella! What are you doing out here? I figured you would've locked
        yourself to the confinement of your room by now."

    s "What does it look like?! I'm {i}trying{/i} to get something to eat!"

    e "Still hungry? You didn't really touch your smoked cow tongue."

    s "Yeah, I should've just given it to you. And now this dang machine won't give me my candy bar!"

    s "I paid for the dang thing! Can you help me?"

    e "Sure, give me a sec. *{i}He starts shaking the vending machine and slams
        it down. The candy bar falls out{/i}*"
    #could use camera shake here again

    show Zach
    with dissolve

    z "*{i}Coming out of his room{/i}* What was that?!"

    e "What was what?"

    z "The noise!"

    s "That was Elliot's rage against the vending machine."

    e "Rage? You were the one kicking it earlier."

    s "Whatever. *{i}He picks up the candy bar and starts walking away{/i}*
        Thanks Elliot."

    e "I think that's the first time time I've ever heard her say thank you.
        Should I say \'you're welcome\'?"

    z "I think she already knows."

    z "Besides, you've already caused enough noise tonight. We should probably get back to the room."

    e "But I'm still hungry!"

    z "Then you should've grabbed that candy bar before Stella did.
        *{i}He smirks as he walks towards the room{/i}*"

    z "Come on you big lug."

    e "Ok..."

    e "I guess I'm just happy that Stella has something to eat."

    jump MotelNight1Pt2

label MotelNight1Pt2:
    show bg night motel
    with fade

    show Elliot at slightleft

    e "Well, I guess I'm going hungry tonight."

    show Zach at slightright

    z "*{i}Jokingly{/i}* I mean, there's that chewed gum stuck underneath
        that coffee table, but I wouldn't...."

    z "*{i}Sigh{/i}* Elliot, where's the gum?"

    z "That kid sure is something else. *{i}He turns off the light and goes to bed{/i}*"
    #FADE OUT

    jump MotelMorn1

# Group room
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

    #jump MotelMorn2

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

    z "Anyways, I decided to go on this trip because I wanted to know more about myself. I've always felt like an odd-ball."
    z "A misfit, you know I've never really fit in anywhere. And maybe there's a reason behind it. I know I have a loving sister, even if she doesn't show it."
    z "And a great best friend. It's just that my past is a mystery that I want to solve."


    e "I gotcha."

    s "*notices Zach's pendant flicker in the light* I know you never talk about it, but you'd like to know what that pendant means, right?"

    z "Well yeah... I've had it for as long as I can remember. It means a lot for me. I feel weird without it."
    z "It's a part of me."

    s "I can tell."

    z "I suppose we should get going. I can explain more on the way."
    jump HikingTrail







































































































label HikingTrail:
    show Stella with dissolve
    s "Who's idea was this again?"

    e "I think it was the guy in the tavern's recommendation."

    s "Yeah, but who agreed to this?"

    z "We all did."

    s "Well {i}that{/i}... was a mistake. I... need... water."
    #Drop transition

    e "Here Stella, I brought enough for everyone."

    s "..."

    s "This tastes like its been in the car for months."

    e "Do you want it or not."

    s "Yes! Sorry! I want it!"
    show Stella

    z "Elliot? Where are we on the hiking trail?"

    e "Huh? How should I know?"

    z "You were the one in charge of grabbing a map at the trailhead!"

    e "Whose idea was that?"

    #TO DO: ADD CHOICE HERE

    e "Well, the damage has been done. Now we should probably focus on getting back."

    z "Do you know the way back?"

    e "I think I remember most of the path that we took. But we {i}have{/i} been hiking for a couple miles now."

    e "I don't know if I remember everything."

    s "Well, let's get moving. I don't want to spend another minute without cell service."

    z "uhg. I feel so bad that all of your followers haven't seen your face in two hours."

    #Time pass transition(clock sound and swirl) or naration?

    s "Face it. We're lost."

    e "No we are not! The trail head should be half a mile ahead."

    s "But you said that five miles ago!"

    show shadowman at offscreen with moveinleft
    hide shadowman

    s "*scared* Did anyone just see that?!"

    e "See what?"

    s "I don't know! It was moving to fast for me to make out."

    e "I didn't see anything."

    s "Seriously? How useless can you be?"

    #In the script, it says to make a choice here, but it is not fleshed out.

    e "... *visibly sad*"

    z "Hey, that was {i}not{/i} okay Stella. Apologize."

    s "I... I'm sorry"

    show shadowman at offscreen with moveinright
    hide shadowman

    e "Okay, I saw it that time."
    "*everyone scared*"

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

    lum "But it seems you are all tired and hungry. You probably won't be able to make it back tonight."
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

    style multiple2_say_window:
        xsize 500
        background None

    style block1_multiple2_say_window:
        xalign 0.0

    style block2_multiple2_say_window:
        xalign 0.5

    z "Stella!" (multiple=2)
    e "Stella!" (multiple=2)

    lum "Don't worry, she'll come to. Just a bit fatigued. If I had to guess, she's
    probably never exerted herself this much. That, and she locked her knees."

    z "What does that have to do with anything?"

    lum "Locking your knees restricts the blood flow in your legs, causing people to faint."

    z "For a man who doesn't know the word 'diction' means, you sure know a lot."

    e "Let's stop standing here and help her! I'll carry her. Can you lead us to your... house... cabin, wherever you live?"

    lum "Sure! Follow me."












    # This ends the game
    return
