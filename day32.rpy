label day32:

    $ days = 32

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"


    scene cg od_sl_earful with dissolve



    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day33

return 