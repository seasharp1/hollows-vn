define e = Character("Elliot", who_color="4287f5")
define s = Character("Stella", who_color="ef42f5")
define z = Character("Zach", who_color="42f584")
define bm = Character("Boisterous Man", who_color="e62222")
define lum = Character("Lumberjack", who_color="cc5500")
define mv = Character("Mysterious Voice", who_color="5e0fb8")
##define me = Character("[povname]") ## Use this for named main character

image Elliot = "Elliot.png"
image Stella = "Stella.png"
image Zach = "Zach.png"
image Boisterous Man = "Boisterious_Man.png"
image Lumberjack = "Lumberjack.png"

transform slightleft:
    xalign 0.1
    yalign 1.0

transform slightright:
    xalign 0.9
    yalign 1.0

transform hop:
    linear 0.1 ypos 50
    linear 0.1 ypos 0

# This is for displaying multiple character's dialogue simultaneously ---
# For 2 characters...
# Use (multiple=2) after dialogue on same line to use this
style multiple2_say_window:
    xsize 500
    background None

style block1_multiple2_say_window:
    xalign 0.0

style block2_multiple2_say_window:
    xalign 0.5

# For 3 characters...
# Use (multiple=3) after dialogue on same line to use this
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

#Shadowman animation------------------------------------------------------
image shadow run:
    animation
    "shadow"
    xalign 0.0
    linear 1.0 xalign 1.0
#-------------------------------------------------------------------------

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

    call chapter1

    #Chapter Directory --------------------------
    # Chapter 1: The Car Scene
    # Chapter 2: Welcome to Timberland
    # Chapter 3: The Tavern
    # Chapter 4: The Hotel
    # Chapter 5: The Hiking Trail
    # Chapter 6: Lumberjack Cabin
    # Chapter 7: Well
    #--------------------------------------------

    # This ends the game
    return
