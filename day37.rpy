label day37:

    $ days = 37

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True










    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day38

return