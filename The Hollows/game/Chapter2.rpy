label chapter2:
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

    jump chapter3
