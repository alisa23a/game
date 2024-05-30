label day39:

    $ style.say_window = style.window

    $ days = 39

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_38_00 = True


    play music "audio/music/z_1003.mp3"

    show screen current_day_bad_1 with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day_bad_1

    $ show_quick_menu = True



    style Cant_Write_Style:
        color "#fff"
        size 30

    screen cant_write():

        style_prefix "Cant_Write_Style_text"
        text "Не могу пока писать ничего." xalign 0.5 yalign 0.5



    show screen cant_write with fade


    pause (10000000000000000000000.0)


    hide screen cant_write


    scene black with fade


    jump day40

return