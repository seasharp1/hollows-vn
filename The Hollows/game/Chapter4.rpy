label chapter4:

    show bg tavern

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

    stop music fadeout 1.0 #stops current music
    pause 1.0

    if ownRoom:
        jump zeRoom
    else:
        jump gRoom

# Own room
label zeRoom:
    scene bg night motel
    show bg night motel
    with fade

    play music "audio/JazzPiano.wav" fadein 1.0

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
    stop music fadeout 1.0 #stops current music
    pause 1.0

    jump vending1

label vending1:
    scene bg vending machine
    show bg vending machine
    with fade

    play music "audio/Playful-music.mp3" fadein 1.0

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

    stop music fadeout 1.0 #stops current music
    pause 1.0

    jump MotelNight1Pt2

label MotelNight1Pt2:
    scene bg night motel
    show bg night motel
    with fade

    play music "audio/JazzPiano.wav" fadein 1.0

    show Elliot at slightleft

    e "Well, I guess I'm going hungry tonight."

    show Zach at slightright

    z "*{i}Jokingly{/i}* I mean, there's that chewed gum stuck underneath
        that coffee table, but I wouldn't...."

    z "*{i}Sigh{/i}* Elliot, where's the gum?"

    z "That kid sure is something else. *{i}He turns off the light and goes to bed{/i}*"
    #FADE OUT

    stop music fadeout 1.0 #stops current music
    pause 1.0

    jump MotelMorn1

# Group room
label gRoom:
    scene bg night motel
    show bg night motel

    play music "audio/JazzPiano.wav" fadein 1.0

    "*{i}Zach unlockes Room 308. The room reeks of mildew and strawberry flavored bubblegum{/i}*"

    show Stella at slightleft

    s "So Zach, why do you even want to find your biological family? I mean,
        is our family not good enough for you?"

    show Zach at slightright

    z "Hey! I never said that!"

    s "Then why?"

    z "Because I want to know more about myself. It's like there's a part of
        me missing and I have no way of finding it."

    s "Okay genius, if there is \'no way of finding it\' then why are we in this creepy town?"

    show Elliot

    e "Yeah, I was wondering that too."

    z "I told you everything in the car!"

    e "You know I was sleeping most of the ride, right?"

    z "*{i}Sigh{/i}*"

    e "I really should get a bite to eat before I head to bed for the night.
        *{i}He sees the gum under the table and starts reaching for it{/i}*"

    s "Gross! I should really get you a dog cone. Come on, we're going to the
        vending machines. I saw some outside."

    stop music fadeout 1.0 #stops current music
    pause 1.0

    jump vending2

label vending2:
    show bg vending machine
    scene bg vending machine
    with fade

    play music "audio/Playful-music.mp3" fadein 1.0

    show Elliot at slightright
    show Stella at slightleft

    "Elliot and Stella work their way to an area with 3 vending machines.
        All of them are empty except for one with 1 Oogle Boogle Nutty Candy Bar in it."

    e "Looks like there's one left..."

    "Elliot and Stella split the bar"

    stop music fadeout 1.0 #stops current music
    pause 1.0

    #jump MotelMorn2

label MotelMorn1:
    scene bg morning motel
    show bg morning motel

    play music "audio/upbeatThemeLoop.wav" fadein 1.0 volume 0.75

    "*{i}Stella bangs on the door{/i}*"

    s "Rise and shine sleepyheads!"

    show Zach at slightright

    z "Just give us 5 minutes Stel. We're almost ready."

    s "Oh you're awake? I wasn't expecting that."

    z "Suprised?"

    s "Well yeah! You're never up this early. You must be {i}really{/i} excited for this hiking trip."

    show Elliot at slightleft
    show Stella

    e "*{i}Opening the door{/i}* Believe me, he is. He's been up since 5 a.m."

    s "Yeesh, that explains why Zach looks like a..."

    s "You know what? Nevermind."

    s "Zach you ready yet?"

    z "Almost, I need to talk to Elliot quick though."

    z "Last night, you were outta this room so quick that I didn't get to tell
        you why I wanted to go on this trip in the first place."

    s "Actually. I'd like to know that too."

    e "Oh yeah... Sorry about that. When my minds on food, I kinda forget about my surroundings."

    s "We know!" (multiple=2)
    z "We know!" (multiple=2)

    z "Anyways, I decided to go on this trip because I wanted to know more about
        myself. I've always felt like an odd-ball."

    z "A misfit, you know I've never really fit in anywhere. And maybe there's
        a reason behind it. I know I have a loving sister, even if she doesn't show it."

    z "And a great best friend. It's just that my past is a mystery that I want to solve."


    e "I gotcha."

    s "*{i}Noticing Zach's pendant flicker in the light{/i}* I know you never talk about
        it, but you'd like to know what that pendant means, right?"

    z "Well yeah... I've had it for as long as I can remember. It means a lot
        for me. I feel weird without it."

    z "It's a part of me."

    s "I can tell."

    z "I suppose we should get going. I can explain more on the way."

    stop music fadeout 1.0 #stops current music
    pause 1.0

    jump chapter5
