label day13:

    $ days = 13

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music


    play music "audio/music/z_199.mp3"

    scene bg camp_artifacts

    "Идея игры в карты принадлежала Алисе. Она же определила место."

    "У каждого домика лагеря был закрытый чердак. Чердак этот был полноценной комнатой  и использовался лишь в случаях, когда количество пионеров  было больше ожидаемого."

    "Но те времена давно прошли и чердаки были заботливо заколочены Петровичем по заданию завхоза, а на двери повешены  замки. Был такой чердак и над нашей комнатой."

    "Я прознала, где Петрович держит ключи от всех чердаков лагеря, благо входить к нему в каморку девочкам разрешалось в любое время."


    scene bg watchmans_cabin_2

    "Оставалось выяснить, какой из почти тридцати ключей был именно от чердака нашего домика. Однако долго искать не пришлось."

    "Будучи аккуратистом по натуре, Петрович снабдил каждый ключ ярлычком из приклеенного к веревочке медицинского пластыря с написанным на нём номером домика. Это было очень кстати."

    "Мы прокрались в каморку. Но ярлычка с нужным номером, т.е. ключа от нашего чердака, там не было. Мы решили, что ключ находиться на связке, которую Петрович носит с собой."


    scene an_d13_02_bg

    "Мы знали, что он частенько любит подремать на лавочке . Иногда ключи  почти  падали с его руки  и можно было их умыкнуть, пока он спит. Но спал он чутко. Эту ответственейшую операцию, было поручено провернуть мне. "

    scene black with fade

    stop music

    jump key_theft_1

return



image stealthekey:

    "images/an/an13day/an_d13_14.png" with Dissolve(0.5, alpha=True)
    pause 0.5
    "images/an/an13day/an_d13_16.png" with Dissolve(0.5, alpha=True)
    pause 0.5

    repeat

############################################
## Экраны на которых нужно кликать на ключ - модальные. На которых реакция Петровича - не модальные, клик в любом месте экрана сразу переводит на лейбл, а там стоит жёсткая пауза перед скрытием текущего экрана

screen key_theft_1():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0)   

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_2")


screen key_theft_2():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_09.png" pos (0, 0)


screen key_theft_3():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_4")


screen key_theft_4():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_10.png" pos (0, 0)

screen key_theft_5():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_6")


screen key_theft_6():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_11.png" pos (0, 0)


screen key_theft_7():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_8")


screen key_theft_8():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_12.png" pos (0, 0)


screen key_theft_9():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_12.png" pos (0, 0)

    add "images/an/an13day/an_d13_17.png" pos (0, 0)


label key_theft_1:
    
    play music "audio/music/z_200.mp3"

    show screen key_theft_1 with fade

    $ show_quick_menu = False

    pause (1000000000000000000000.0)

label key_theft_2:

    hide screen key_theft_1

    show screen key_theft_2

    jump key_theft_3

label key_theft_3:

    $ renpy.pause(3.0, hard=True)

    hide screen key_theft_2

    show screen key_theft_3

    pause (1000000000000000000000.0)

label key_theft_4:

    hide screen key_theft_3

    show screen key_theft_4

    jump key_theft_5

label key_theft_5:

    $ renpy.pause(3.0, hard=True)

    hide screen key_theft_4

    show screen key_theft_5

    pause (1000000000000000000000.0)

label key_theft_6:

    hide screen key_theft_5

    show screen key_theft_6

    jump key_theft_7

label key_theft_7:

    $ renpy.pause(2.0, hard=True)

    hide screen key_theft_6

    show screen key_theft_7

    pause (1000000000000000000000.0)

label key_theft_8:

    hide screen key_theft_7

    show screen key_theft_8

    $ renpy.pause(1.0, hard=True)

    hide screen key_theft_8

    show screen key_theft_9

    $ renpy.pause(2.0, hard=True)

    hide screen key_theft_9

    jump day13_2


label day13_2:

    $ inv_item_28 = True

    $ show_quick_menu = True

    stop music

    play music "audio/music/z_089.mp3"

    scene bg attic_inside with dissolve

    "Наконец мы попали в заветное помещение. Там царили паутина, пыль и летучая мышь. Мышь решили не трогать, она стала символом Чердака и его талисманом. От остального безжалостно избавились."

    "Засучив рукава, мы с Алисой трудились все свободное от лагерного расписания время, и наконец, «номер нашей гостиницы», как его назвала Алиса, был готов."

    "Вскоре весь отряд собрался наверху."



    image an_13_01: #Анимация Ульяна карты

        "images/an/an13day/an_d13_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat 


    stop music

    play music "audio/music/z_201.mp3"

    scene an_d13_01_bg with dissolve

    show an_13_01

    pause (10000000000000000000000.0)


    scene bg attic_inside with dissolve

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sl "А это законно, девочки?"

    hide sp_sl_001

    show sp_le_006:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "Ясенева!"

    hide sp_le_006

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Какая разница? Кто узнает, если ты не скажешь?"

    hide sp_al_005

    show sp_je_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Офигеть! Это мечта. Я сделаю тут филиал библиотеки, перетащу в него запретку из спецхрана."

    hide sp_je_013

    show sp_mi_012:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    mi "И уроки на гитаре будем  устраивать, а главное – квартирники!"

    hide sp_mi_012

    show sp_at_004:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ats "Ой девочки, а на чем мы будем сидеть? Тут только один стул! И стол..."

    hide sp_at_004

    show sp_sam_010:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "Я понимать что, как это по русски... (подыскивает слова) эээ, революшен... нелегаль?"

    hide sp_sam_010

    show sp_sem_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Легаль, легаль. Только об этом никому говорить не стоит. Это, Сэмми, по-вашему – андеграунд."

    hide sp_sem_001

    show sp_sam_004:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "(Подпрыгивая и хлопая в ладоши) \nО, я понимать! Рашен андеграунд! Мне нравится!"

    hide sp_sam_004

    show sp_at_004:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ats "Так как насчет стульев?"

    hide sp_at_004

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ul "Фигня вопрос! Сейчас физрук в карантине, у Петровича есть дубликат ключей от бытовки и раздевалки."

    ul "Стащим физруковский диван и скажем, что так и было. С других чердаков по стулу скоммуниздим и «вуаля», как говорит Женя. Вот и мебель."

    hide sp_ul_014

    show sp_le_006:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "(Ухмыляясь и глядя на Алису) \nДа-а... Кто-то скоренько наладит тут личную жизнь."

    hide sp_le_006

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "На себя посмотри. Ты первая в очереди будешь на ключ."

    hide sp_al_005

    show sp_al_003:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да, Семен? \n(хитро подмигивает)"

    hide sp_al_003

    show sp_sem_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Не ссорьтесь, девочки. Диван нужен всем. И не в том смысле, а чтобы сидеть. Ну и вообще, комфорт минимальный все-таки нужен. Диван облагородит помещение. Что с картами?"

    hide sp_sem_001

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это я беру на себя."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "И чтобы на вечеринках было вкусненькое! Заготовку вкусняшек, думаю, надо поручить Саманте. Ей никогда не откажут."

    ul "И в поселок за конфетами пусть переводчицу... эту, Мегги пусть пошлет. Что она тут порожняком у нас проживается? Польза какая-никакая будет. Мой папа сказал бы «С худой овцы хоть шерсти клок»."

    hide sp_ul_012

    show sp_sam_004:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "(Смеясь) \nОвца, овца! Я сказать Мегги!"

    hide sp_sam_004

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Ну ты и хитрющая, Ленина! Откуда в тебе это?"

    hide sp_je_001

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Она у нас главный следопыт и следователь по особо важным делам!"

    hide sp_ul_012
 
    hide sp_al_005

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "А меня в игру берете?"

    hide sp_tol_001

    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Ты чё, братан?! Даже не сомневайся. Мы же команда!"

    hide sp_shu_001

    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Да!"

    hide sp_el_001

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "А я бы кибернетикам ключа не давала, мало ли. Превратят нашу нычку в филиал кружка «Умелые руки». Знаю я их. Натаскают всяких железок и поминай, как звали, уют и порядок... Нет уж."

    sl "Кстати, насчет порядка. Кто по щелям будет выметать?"

    hide sp_sl_001
 
    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "У кого ключ, тот и убирает за собой!"

    hide sp_el_001

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Логично. Я проверю!"

    hide sp_sl_001

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Объявляю операцию «Диван». Тащить будем ночью. Тут сила нужна. Мальчики! Вы готовы?"
 
    hide sp_al_005

    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    guys "(Хором) \nВсегда готовы!"

    hide sp_el_001

    hide sp_shu_001

    hide sp_tol_001






    pause (10000000000000000000000.0)


    scene black with fade

    stop music

    #jump day14

return