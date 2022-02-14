label chapter10:
    show bg woods
    show Stella at left

    play music "audio/TheHorrorGoat.wav" fadein 1.0

    s "He's chasing after us!"

    show Zach at center

    z "Keep running!"

    show Elliot at right

    e "I don't know how much longer I can go. My leg is giving out..."

    z "*{i}Panicking{/i}* Not good! What do we do?!"

    z "Should we split up?"

    menu:

        "We should split up.":
            jump splitup

        "We should stick together":
            jump sticktogether

label splitup: # Made more sense to me if these were swapped so I did that.
    z "How much longer do you think you can run, Elliot?"

    e "Not much further... I think it's best if you and Stella go on ahead."

    s "We're not leaving you!"

    e "Do you wanna get caught by the Lumberjack? If you and Zach continue running
        and I hide in some brush, he'll continue chasing you and pass me."

    e "Then I'll be able to get out of the woods and get help."

    pause 1.0

    s "..."

    s "Ok... but be careful."

    hide Elliot

    jump forestclearing

label sticktogether: # Made more sense to me if these were swapped so I did that.
    z "Should we split up?"

    s "What? That's a terrible idea. We're not doing that. Haven't you ever
        watched a horror movie?! That's the worst thing you can do!"

    e "I'm thinking we might have to."

    s "But..."

    e "I can't run anymore Stel, and the Lumberjack's behind us. I don't want
        to slow you guys down. There's not much more I can do."

    e "Zach, please, take Stella and get outta here!"

    e "I'll figure something out."

    z "Ok. Be careful Elliot."

    hide Elliot

    s "Elliot..."

    jump forestclearing

label forestclearing:
    show bg forest clearing
    with fade

    s "*{i}Out of breath{/i}* I... I... need a minute."

    z "*{i}Panting{/i}* Me... too."

    z "Let's take a break... in this clearing... for a little bit until
        we catch our... breath."

    s "There's a couple of stumps a little bit further ahead... Let's rest there."

    "*{i}Zach and Stella move towards the stumps for some rest{/i}*"

    z "I wonder how Elliot's doing?"

    s "I hope he's okay..."

    z "Elliot's a strong guy. He'll be fine."

    hide Stella
    hide Zach

    jump woods

label woods:
    show bg woods
    with fade

    show Elliot at center

    e "Oh, why did we split up. This was a terrible idea..."

    e "What's wrong with me. I hope Zach and Stel will be alright."

    hide Elliot

    mv "AhmnA... ROasDlkS...Hih-in"

    show Elliot at center

    e "What was that?!"

    hide Elliot

    mv "BraKL... Na... SepUNItE... nEmE... SEquEnA"

    show Elliot at center

    e "It sounds like it's getting closer."

    "*{i}Elliot tries to move, but he seems to be unable to{/i}*"

    e "What is this?! There's something wrapped around my ankle! I can't move!"

    mv "ZAnU... Ik... ToMn... BOsNYu... AAHjiOOnli... RoSiQua...nK"

    e "Let go of me!"

    mv "RAAAASINNNOOOO... NAAAKINNIII... GFOO"

    e "*{i}It's wrapping around my body!{/}* Somebody HELP!"

    e "*{i}I let you down Stel and Zach. Sorry...{/i}*"

    hide Elliot
    jump hazelstree

label hazelstree:
    show bg forest clearing
    with fade

    show Stella at slightright

    s "You're probably right. I bet you Elliot's already made it out of the forest."

    show Zach at slightleft

    z "Yeah, I'm sure too. We should get moving before you know who finds us again."

    s "Wait, there's something over there. I wanna take a closer look."

    "*{i}Stella moves closer to the area she was talking about{/i}*"

    s "This place kinda looks like it's sacred. Have yo unoticed how the stumps
        are arranged?"

    z "I did actually. They surround that oddly shaped tree in the center."

    show bg hazels tree
    with fade

    z "*{i}Zach moves towards the tree as if he's being pulled without realizing it{/i}*"

    z "I wasn't sure if we should ignore it and move forward or check it out, but
        now I feel like we need to take a closer look."

    hide Zach
    hide Stella

    mv "ShhhHAnli..."

    show Stella at slightright
    show Zach at slightleft

    s "What was that?!"

    z "The tree in the center."

    s "What? How do you know?"

    z "*{i}Walking closer to the tree{/i}* I... I don't know. I just do."

    s "Wait, these stumps look odd. Are those... veins?!"

    s "ZACH STOP MOVING! I think I figured out why the stumps are here."

    show Lumberjack at right

    lum "You should listen to her young man."

    z "*{i}Zach drops to his knees{/i}* That wood statue over there... It looks
        just like me..."

    s "Zach? What's wrong?"

    z "I don't understand... What's the purpose of this statue?"

    s "Zach? What's wrong? Answer me."

    z "Am I... turning Hollow?"

    s "Zach!"

    z "Huh? What?"

    s "Are you... ok?"

    z "I... I... don't know."

    z "This statue... it looks like the severed tree lims we saw in the woodshed.
        And it's of me."

    s "What does this mean?"

    z "I don't know"

    lum "I might have some answers for you."

    hide Stella
    hide Zach
    hide Lumberjack

    window hide # This hides the dialogue window
    show bg end
    with fade

    pause

    # This ends the game and returns to the main menu
    $ renpy.full_restart()
