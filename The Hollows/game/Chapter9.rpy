label chapter9:
    scene bg woodshed furance
    show bg woodshed furance

    play music "audio/SpookyNoise.mp3" fadein 3.0

    "*{i}The stench of iron gets stronger{/i}*"

    show Stella
    with easeinleft
    s "Sorry guys! I should've been more careful."

    show Zach at slightleft
    z "It's okay Stel, I landed on Elliot."

    s "Elliot! Are you okay?!"

    show Elliot at slightright
    e "Yeah, it takes a lot more than that to hurt me. *{i}winces in pain{/i}*"

    s "*{i}looks worried{/i}*If you say so..."
    s "Here let me give you a hand."

    e "*{i}Grabs Stella's hand{/i}* Thanks."

    "*{i}Zack, Elliot and Stella examine their surroundings{/i}*"


    z "It looks like an average woodshed to me."

    "*{i}The woodshed has 3 rows of logs on each side.{/i}*"

    e "*{i}limping{/i}* A furnace doesn't really belong in a woodshed if you ask me."

    z "You've got a point. *{i}moves towards furnace{i}*"

    s "*{i}covers her nose{/i}* The smell of iron is even stronger down here."

    e "I'm starting to feel sick."

    z "Me too."

    "..."

    show bg hand furnace
    z "*{i}slightly panicked{/i}* Uh, guys... what's in the fire?"

    e "I..I don't know but it looks like..."

    s "Like a..."

    e "A hand!" (multiple=2)
    s "A hand!" (multiple=2)

    z "What the-? All that time we were smelling blood?!"

    s "I don’t know. Scientifically we shouldn’t be smelling blood. If anything, we should be smelling something like cooked meat."
    s "And there’s no remnants of blood in the woodshed at all."
    s "I understand that blood can linger, but the stench... it's so strong."

    e "Mmmmm... cooked meat."

    z "Not a good time to be talking about food, Elliot."

    "..."

    s "I want to know what it actually is. Elliot, can you hand me the tongs over there to your left?"
    s "*{i}Annoyed{/i}* No, your other left. *{i}Elliot hands tongs to Stella{/i}*"
    s "*{i}Reaching the tongs into the fire{/i}* It looks like a hand, all right. *{i}clasps hand with tongs{/i}*"
    s "Though can't say anything for certain until we examine it."
    s "Okay, I think I got it. *{i}pulls out the hand shaped object{/i}*"

    e "*{i}confused{/i}* It looks like an ordinary piece of charred wood."

    s "Is there anything sharp laying around? We're going to have to cut it open to be sure of anything."
    s "I'm gonna try jabbing the tongs in between the middle and index finger and see if I can break it apart."

    "*{i}cracking noise{/i}*"

    s "I think I'm starting to get it!"

    "*{i}snap{/i}*"

    s "Got it!"

    "*{i}The broken wood hand reveals arteries and veins and a reminiscence of where bone was{/i}*"

    s "I-I don't get it... How is this even possible??"

    show bg woodshed furance with hpunch
    e "*{i}Stumbles into a stack of logs and knocks them over{/i}* Sorry guys, I last my balance."
    e "When I fell down those stairs earlier, I grazed my leg pretty badly."

    "*{i}Zach and Stella rush over to Elliot{/i}*"

    z "It's okay, I'm just glad you're in one piece."

    s "Uh guys, I think we have bigger things to worry about."
    s "Look behind you."
    s "*{i}voice shaking{/i}* There's a stack of those limb-shaped...things. The lumberjack must've been hiding them."

    "*{i}Zach's jaw drops{/i}*"

    z "What the...?! He has enough limbs for a quarter of the people living in Timberland!"
    z "We need to hide our evidence and get out of here."
    z "Elliot, are you okay to walk?"

    e "Ugh, fine I guess. I don't know how far I'll be able to go."

    z "That isn't my definition of fine."

    "*{i}footsteps{/i}*"

    s "It's the lumberjack!"
    s "We need to get out of here NOW!"

    z "I'll help Elliot up the stairs."

    show bg woodshed furance
    s "*{i}nods and starts heading up the stairs{/i}* I'll distract the lumberjack if I see him."

    z "Be careful."
    z "Please."

    hide Elliot
    hide Zach
    s "*{i}opens the door{/i}* I will."
    s "{i}No sign of him... I don't like this.{/i}"

    lum "*{i}From a distance, calmly{/i} Fancy meeting you here."

    s "{i}It's the lumberjack!{/i}"

    show lum at slightright

    lum "May I ask what you were doing in my woodshed?"

    s "I... uh, was investigating the smoke I smelled from your house."
    s "Turned out I was smelling blood."

    lum "So you know then. Listen, I can explain everything."

    s "You don't need to explain anything! I already know you're a monster."

    show Zach at slightleft
    show Elliot

    s "*{i}Notices Zach and Elliot{/i}* RUN!!"

    "*{i}Zach, Elliot, and Stella run into the woods behind the shed{/i}*"

    hide Zach
    hide Elliot
    hide Stella

    lum "*{i}Shouting{/i}* Please! I'm begging you! Don't split up in those woods!"
    lum "You'll become a... if..."

    stop music fadeout 1.0

    jump chapter10
