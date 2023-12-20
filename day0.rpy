
#screen diary_page_01():

image prologue = Movie(play="video/prologue.webm", size=(1920, 1080))

    # scene ul_pi_island_02

    # pause (10000000000)

label start:

    stop music

    $ _skipping = False

    show prologue

    $ renpy.pause(299.5, hard=True)

    #pause (1000000000000)

    #$ _skipping = True



jump day8