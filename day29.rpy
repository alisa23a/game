label day29:

    $ days = 29

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    #scene an_d16_06 with dissolve














    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day28

return 