label day5:

    $ style.say_window = style.window

    $ days = 5

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = True
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = False

    $ im_gal_08_00 = True
    $ im_gal_08_01 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day


    $ show_quick_menu = True


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"

    scene an_d10_01_bg with dissolve


    # ""

    # ""

    # ""

    # ""

    # ""

    # ""

    # ""

    # ""









    # ""

    # ""

    # ""

    # ""

    # ""

    # ""

    # ""





    scene black with fade

    pause (1000000000000000000000.0)

    stop music fadeout 1.0

    jump day8


return
    