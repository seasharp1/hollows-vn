label chapter3:
    scene bg tavern
    show bg tavern
    with fade

    play music "audio/Old-distorted-music-1.mp3" fadein 1.0 volume 0.5

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

    jump chapter4

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

    jump chapter4

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

    jump chapter4
