label day40:

    $ style.say_window = style.window

    $ days = 40

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True


    show screen current_day_bad_2 with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day_bad_2

    $ show_quick_menu = True



    screen cant_write2():

        style_prefix "Cant_Write_Style_text"
        text "Сегодня тоже не могу писать. Завтра напишу." xalign 0.5 yalign 0.5   


    show screen cant_write2  with fade


    pause (10000000000000000000000.0)


    hide screen cant_write2


    scene black with fade


    jump day41

return