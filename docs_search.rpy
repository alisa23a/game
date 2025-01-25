define doc_search_item_01 = False # Резинка Мику, Под лестницей в музкружок
define doc_search_item_02 = False # Альбом Художника, Музкружок, рояль
define doc_search_item_03 = False # Документы лётчика, Музкружок, за картиной
define doc_search_item_04 = False # Неизвестная женская заколка, Каморка сторожа, кровать
define doc_search_item_05 = False # Импортная зажигалка, Каморка сторожа, под кроватью
define doc_search_item_06 = False # Часы, Кружок Усталые руки, внутри
define doc_search_item_07 = False # Белая панама, вход в Бомбоубежище, под кустом
define doc_search_item_08 = False # Дужка от очков, Кружок Умелые руки, под столом
define doc_search_item_09 = False # Голубая пуговица, Генда, у подножья
define doc_search_item_10 = False # Синий галстук скаута, Крыша где хорошо целоваться
define doc_search_item_11 = False # Нашивка на рубашку, чердак Алисы и Ульяны, за диваном в левом нижнем углу
define doc_search_item_12 = False # Заколка для волос «Желтое сердечко», Нычка 2, возле лавки в нижнем левом углу
define doc_search_item_13 = False # Пряжка от ремня. Нычка 7, в углу здания, у дальнего края лавки
define doc_search_item_14 = False # Конверт со стихами. Библиотека, на полке
define doc_search_item_15 = False # Черный парик, Раздевалка, шкафчик в верхнем рядку, в центре, возле угла


# define doc_search_item_01 = True # Резинка Мику, Под лестницей в музкружок
# define doc_search_item_02 = True # Блокнот Художника, Музкружок, рояль
# define doc_search_item_03 = True # Документы лётчика, Музкружок, за картиной
# define doc_search_item_04 = True # Неизвестная женская заколка, Каморка сторожа, кровать
# define doc_search_item_05 = True # Импортная зажигалка, Каморка сторожа, под кроватью
# define doc_search_item_06 = True # Часы Шурика, Кружок Усталые руки, внутри
# define doc_search_item_07 = True # Панамка ОД, вход в Бомбоубежище, под кустом
# define doc_search_item_08 = True # Дужка от очков Жени, Кружок Умелые руки, под столом
# define doc_search_item_09 = True # Синяя пуговица Атсуи, Генда, у подножья
# define doc_search_item_10 = True # Галстук Саманты, Крыша где хорошо целоваться
# define doc_search_item_11 = True # Нашивка Слави, чердак Алисы и Ульяны, за диваном в левом нижнем углу
# define doc_search_item_12 = True # Заколка Алисы, Нычка 2, возле лавки в нижнем левом углу
# define doc_search_item_13 = True # Пряжка от ремня. Нычка 7, в углу здания, у дальнего края лавки
# define doc_search_item_14 = True # Конверт со стихами-признанием. Библиотека, на полке
# define doc_search_item_15 = True # Чёрный шиньон, Раздевалка, шкафчик в верхнем рядку, в центре, возле угла







style DocsSearchStyleTitle_text:
    color "#fff"
    font "fonts/mateur-webfont.ttf"
    size 30
    
style DocsSearchStyleText_text:
    color "#fff"
    #font "fonts/mateur-webfont.ttf"
    size 30

#style InvItemPrevCaption_frame:
    #background None

style InvItemPrevCaption_text:
    color "#fff"
    size 20

style DocsSearchStyleTitle_vbox:
    background ("#000")
    #xalign (0.5) yalign (0.07)


#экран карты лагеря для поиска документов
screen docs_search:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/bg/docs_search_idle.webp"
        idle "images/bg/docs_search_idle.webp"
        hover "images/bg/docs_search_hover.webp"
        

        hotspot(400, 153, 225, 53) action Hide ("docs_search"), Show ("mus_stairs_ds")

        hotspot(147,251,149,66) action Hide ("docs_search"), Jump ("mus_ds")

        hotspot(453,214,95,57) action Hide ("docs_search"), Jump ("watchcloset_ds")

        hotspot(775,78,106,57) action Hide ("docs_search"), Jump ("tirhands_ds")

        hotspot(917,58,106,42) action Hide ("docs_search"), Jump ("bombu_ds")

        hotspot(1057,99,198,68) action Hide ("docs_search"), Jump ("handmade_ds")

        hotspot(947,383,87,31) action Hide ("docs_search"), Jump ("genda_ds")

        hotspot(1295,284,215,58) action Hide ("docs_search"), Jump ("kroof_ds")

        hotspot(1555,345,195,107) action Hide ("docs_search"), Jump ("attic_ds")

        hotspot(1479,589,109,40) action Hide ("docs_search"), Jump ("secret3_ds")

        hotspot(1210,753,107,40) action Hide ("docs_search"), Jump ("secret2_ds")

        hotspot(902,911,119,46) action Hide ("docs_search"), Jump ("secret1_ds")

        hotspot(331,887,112,38) action Hide ("docs_search"), Jump ("secret7_ds")

        hotspot(394,568,182,47) action Hide ("docs_search"), Jump ("library_ds")

        hotspot(543,469,87,38) action Hide ("docs_search"), Jump ("dresser_ds")
            

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("docs_search"), Jump ("day27_cont")


# Локации лагеря

screen mus_stairs_ds:

    # Нычка под лестницей в музкружок

    tag menu
    modal True
    zorder 300

    add "bg mus_stairs"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("mus_stairs_ds"), Show("docs_search")


    if doc_search_item_01 == False:

        imagebutton:
            xpos 727 ypos 751
            xsize 72 ysize 59
            idle "images/docs_search/p_01_miku_scrunche.png"
            hover "images/docs_search/p_01_miku_scrunche.png"
            action Hide ("mus_stairs_ds"), Jump("mus_stairs_ds_find_01")


screen mus_ds:

    # Музыкальный и хореографический кружок

    tag menu
    modal True
    zorder 300

    add "bg mus"


    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("mus_ds"), Show("docs_search")


    if doc_search_item_02 == False:

        imagebutton:
            xpos 560 ypos 477
            xsize 498 ysize 114
            idle "gui/bg_1x1_transparent.png"
            hover "gui/bg_1x1_transparent.png"
            action Hide ("mus_ds"), Jump("mus_ds_find_02")

    if doc_search_item_03 == False:

        imagebutton:
            xpos 1140 ypos 484
            xsize 74 ysize 146
            idle "gui/bg_1x1_transparent.png"
            hover "gui/bg_1x1_transparent.png"
            action Hide ("mus_ds"), Jump("mus_ds_find_03")




image watchcloset_ds_splash:

    # Анимация искры

    pos (1822, 689)

    "images/docs_search/p_splash_01.png"
    pause 0.1
    "images/docs_search/p_splash_01.png"
    pause 0.1
    "images/docs_search/p_splash_01.png"
    pause 0.1
    "images/docs_search/p_splash_01.png"
    pause 0.1
    "images/docs_search/p_splash_01.png"
    pause 0.1
    "gui/bg_1x1_transparent.png"
    pause 3.0
    repeat


screen watchcloset_ds:

    # Каморка сторожа

    tag menu
    modal True
    zorder 300

    add "bg stock"


    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("watchcloset_ds"), Show("docs_search")


    if doc_search_item_04 == False:

        imagebutton:
            xpos 1823 ypos 696
            xsize 70 ysize 70
            idle "images/docs_search/p_04_unknown_barrette.png"
            hover "images/docs_search/p_04_unknown_barrette.png"
            action Hide ("watchcloset_ds"), Jump("watchcloset_ds_find_04")


    if doc_search_item_05 == False:

        imagebutton:
            xpos 1466 ypos 896
            xsize 70 ysize 70
            idle "images/docs_search/p_05_imported_lighter.png"
            hover "images/docs_search/p_05_imported_lighter.png"
            action Hide ("watchcloset_ds"), Jump("watchcloset_ds_find_05")


screen tirhands_ds:

    # Кружок Усталые ручки

    tag menu
    modal True
    zorder 300

    add "bg tirhands"


    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("tirhands_ds"), Show("docs_search")


    imagebutton:
        xpos 960 ypos 220
        xsize 70 ysize 70
        idle "images/docs_search/p_06_tirhands_door_knob.png"
        hover "images/docs_search/p_06_tirhands_door_knob.png"
        action Hide ("tirhands_ds"), Jump("tirhands_ds_find_door")


screen tirhands2_ds:

    # Кружок Усталые ручки 2

    tag menu
    modal True
    zorder 300

    add "bg tirhands2"


    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("tirhands2_ds"), Show("docs_search")


    if doc_search_item_06 == False:

        imagebutton:
            xpos 944 ypos 1010
            xsize 70 ysize 70
            idle "images/docs_search/p_06_shu_watch.png"
            hover "images/docs_search/p_06_shu_watch.png"
            action Hide ("tirhands2_ds"), Jump("tirhands_ds_find_06")


screen bombu_ds:

    # Вход в бомбоубежище

    tag menu
    modal True
    zorder 300

    add "bg bomp_shelter2"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("bombu_ds"), Show("docs_search")

    if doc_search_item_07 == False:

        imagebutton:
            xpos 1181 ypos 620
            xsize 70 ysize 70
            idle "images/docs_search/p_07_white_panama.png"
            hover "images/docs_search/p_07_white_panama.png"
            action Hide ("bombu_ds"), Jump("bombu_ds_find_07")




screen handmade_ds:

    # Кружок «Умелые руки»

    tag menu
    modal True
    zorder 300

    add "bg handmade"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("handmade_ds"), Show("docs_search")

    if doc_search_item_08 == False:

        imagebutton:
            xpos 946 ypos 648
            xsize 70 ysize 70
            idle "images/docs_search/p_08_glasses_frame.png"
            hover "images/docs_search/p_08_glasses_frame.png"
            action Hide ("handmade_ds"), Jump("handmade_ds_find_08")


screen genda_ds:

    # Генда

    tag menu
    modal True
    zorder 300

    add "bg genda2"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("genda_ds"), Show("docs_search")

    if doc_search_item_09 == False:

        imagebutton:
            xpos 1073 ypos 701
            xsize 70 ysize 70
            idle "images/docs_search/p_09_blue_button.png"
            hover "images/docs_search/p_09_blue_button.png"
            action Hide ("genda_ds"), Jump("genda_ds_find_09")


screen kroof_ds:

    # Крыша на которой удобно целоваться

    tag menu
    modal True
    zorder 300

    add "bg kroof"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("kroof_ds"), Show("docs_search")

    if doc_search_item_10 == False:

        imagebutton:
            xpos 1429 ypos 784
            xsize 165 ysize 100
            idle "images/docs_search/p_10_blue_neckerchief.png"
            hover "images/docs_search/p_10_blue_neckerchief.png"
            action Hide ("kroof_ds"), Jump("kroof_ds_find_10")


screen attic_ds:

    # Чердак. Лучшая нычка для курения и игры в карты.

    tag menu
    modal True
    zorder 300

    add "bg attic"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("attic_ds"), Show("docs_search")

    if doc_search_item_11 == False:

        imagebutton:
            xpos 832 ypos 557
            xsize 70 ysize 70
            idle "images/docs_search/p_11_shoulder_badge.png"
            hover "images/docs_search/p_11_shoulder_badge.png"
            action Hide ("attic_ds"), Jump("attic_ds_find_11")


screen secret2_ds:

    # Нычка 2

    tag menu
    modal True
    zorder 300

    add "bg secret2"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret2_ds"), Show("docs_search")

    if doc_search_item_12 == False:

        imagebutton:
            xpos 1291 ypos 230
            xsize 70 ysize 70
            idle "images/docs_search/p_12_barrette_yellow_heart.png"
            hover "images/docs_search/p_12_barrette_yellow_heart.png"
            action Hide ("secret2_ds"), Jump("secret2_ds_find_12")


screen secret7_ds:

    # Нычка 7

    tag menu
    modal True
    zorder 300

    add "bg secret7"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret7_ds"), Show("docs_search")

    if doc_search_item_13 == False:

        imagebutton:
            xpos 1075 ypos 575
            xsize 70 ysize 70
            idle "images/docs_search/p_13_belt_buckle.png"
            hover "images/docs_search/p_13_belt_buckle.png"
            action Hide ("secret7_ds"), Jump("secret7_ds_find_13")


screen library_ds:

    # Библиотека

    tag menu
    modal True
    zorder 300

    add "bg library3"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("library_ds"), Show("docs_search")

    if doc_search_item_14 == False:

        imagebutton:
            xpos 374 ypos 488
            xsize 70 ysize 70
            idle "images/docs_search/p_14_poem.png"
            hover "images/docs_search/p_14_poem.png"
            action Hide ("library_ds"), Jump("library_ds_find_14")


screen dresser_ds:

    # Раздевалка

    tag menu
    modal True
    zorder 300

    add "bg dresser3"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("dresser_ds"), Show("docs_search")

    if doc_search_item_15 == False:

        imagebutton:
            xpos 1009 ypos 18
            xsize 92 ysize 188
            idle "images/docs_search/p_15_locker.png"
            hover "images/docs_search/p_15_locker.png"
            action Hide ("dresser_ds"), Jump("dresser_ds_find_15")


screen secret1_ds:

    # Нычка 1

    tag menu
    modal True
    zorder 300

    add "bg secret1"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret1_ds"), Show("docs_search")


screen secret3_ds:

    # Нычка 3

    tag menu
    modal True
    zorder 300

    add "bg secret3"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret3_ds"), Show("docs_search")
      


label docs_search:

    $ show_quick_menu = False

    show screen docs_search

    pause (10000000000000000000.0)


label mus_stairs_ds_find_01:

    $ inv_item_07 = True

    $ doc_search_item_01 = True

    scene bg mus_stairs

    show got_doc_search_item_01

    pause (10000000000000000000.0)

    hide got_doc_search_item_01

    scene black

    show screen mus_stairs_ds

    pause (10000000000000000000000000000000000.0)

    return


label mus_ds:

    show screen mus_ds

    pause (10000000000000000000.0)

    #return

 
label mus_ds_find_02:

    $ inv_item_07 = True

    $ doc_search_item_02 = True

    scene bg mus

    show got_doc_search_item_02

    pause (10000000000000000000.0)

    hide got_doc_search_item_02

    scene black

    show screen mus_ds

    pause (10000000000000000000000000000000000.0)

    return


label mus_ds_find_03:

    $ inv_item_07 = True

    $ doc_search_item_03 = True

    scene bg mus

    show got_doc_search_item_03

    pause (10000000000000000000.0)

    hide got_doc_search_item_03

    show screen mus_ds

    pause (100000000000000000000000000000000.0)

    return


label watchcloset_ds:

    show screen watchcloset_ds

    pause (10000000000000000000.0)

 
label watchcloset_ds_find_04:

    $ inv_item_07 = True

    $ doc_search_item_04 = True

    scene bg stock

    show got_doc_search_item_04

    pause (10000000000000000000.0)

    hide got_doc_search_item_04

    show screen watchcloset_ds

    pause (100000000000000000000000000000000.0)

    return


label watchcloset_ds_find_05:

    $ inv_item_07 = True

    $ doc_search_item_05 = True

    scene bg stock

    show got_doc_search_item_05

    pause (10000000000000000000.0)

    hide got_doc_search_item_05

    show screen watchcloset_ds

    pause (100000000000000000000000000000000.0)

    return


label tirhands_ds:


    show screen tirhands_ds

    pause (10000000000000000000.0)


label tirhands_ds_find_door:


    show screen tirhands2_ds

    pause (10000000000000000000.0)


label tirhands_ds_find_06:

    $ inv_item_07 = True

    $ doc_search_item_06 = True

    scene bg tirhands2

    show got_doc_search_item_06

    pause (10000000000000000000.0)

    hide got_doc_search_item_06

    show screen tirhands2_ds

    pause (100000000000000000000000000000000.0)


label bombu_ds:

    show screen bombu_ds

    pause (10000000000000000000.0)



label bombu_ds_find_07:

    $ inv_item_07 = True

    $ doc_search_item_07 = True

    scene bg bomp_shelter2

    show got_doc_search_item_07

    pause (10000000000000000000.0)

    hide got_doc_search_item_07

    show screen bombu_ds

    pause (100000000000000000000000000000000.0)



label handmade_ds:

    show screen handmade_ds

    pause (10000000000000000000.0)



label handmade_ds_find_08:

    $ inv_item_07 = True

    $ doc_search_item_08 = True

    scene bg handmade

    show got_doc_search_item_08

    pause (10000000000000000000.0)

    hide got_doc_search_item_08

    show screen handmade_ds

    pause (100000000000000000000000000000000.0)



label genda_ds:

    show screen genda_ds

    pause (10000000000000000000.0)



label genda_ds_find_09:

    $ inv_item_07 = True

    $ doc_search_item_09 = True

    scene bg genda2

    show got_doc_search_item_09

    pause (10000000000000000000.0)

    hide got_doc_search_item_09

    show screen genda_ds

    pause (100000000000000000000000000000000.0)



label kroof_ds:

    show screen kroof_ds

    pause (10000000000000000000.0)



label kroof_ds_find_10:

    $ inv_item_07 = True

    $ doc_search_item_10 = True

    scene bg kroof

    show got_doc_search_item_10

    pause (10000000000000000000.0)

    hide got_doc_search_item_10

    show screen kroof_ds

    pause (100000000000000000000000000000000.0)



label attic_ds:

    show screen attic_ds

    pause (10000000000000000000.0)



label attic_ds_find_11:

    $ inv_item_07 = True

    $ doc_search_item_11 = True

    scene bg attic

    show got_doc_search_item_11

    pause (10000000000000000000.0)

    hide got_doc_search_item_11

    show screen attic_ds

    pause (100000000000000000000000000000000.0)



label secret2_ds:

    show screen secret2_ds

    pause (10000000000000000000.0)



label secret2_ds_find_12:

    $ inv_item_07 = True

    $ doc_search_item_12 = True

    scene bg secret2

    show got_doc_search_item_12


    pause (100000000000000000000000000000000.0)


    hide got_doc_search_item_12


    menu:

        "Начать расследование по предмету?"

        "Да":
            jump start_investignation_12

        "Нет":
            jump secret2_ds


    #show screen start_investignation_12


    pause (100000000000000000000000000000000.0)


    show screen secret2_ds

    pause (100000000000000000000000000000000.0)



label secret7_ds:

    show screen secret7_ds

    pause (10000000000000000000.0)



label secret7_ds_find_13:

    $ inv_item_07 = True

    $ doc_search_item_13 = True

    scene bg secret7

    show got_doc_search_item_13

    pause (10000000000000000000.0)

    hide got_doc_search_item_13

    show screen secret7_ds

    pause (100000000000000000000000000000000.0)



label library_ds:

    show screen library_ds

    pause (10000000000000000000.0)



label library_ds_find_14:

    $ inv_item_07 = True

    $ doc_search_item_14 = True

    scene bg library3

    show got_doc_search_item_14

    pause (10000000000000000000.0)

    hide got_doc_search_item_14

    show screen library_ds

    pause (100000000000000000000000000000000.0)



label dresser_ds:

    show screen dresser_ds

    pause (10000000000000000000.0)



label dresser_ds_find_15:

    $ inv_item_07 = True

    $ doc_search_item_15 = True

    scene bg dresser3

    show got_doc_search_item_15

    pause (10000000000000000000.0)

    hide got_doc_search_item_15

    show screen dresser_ds

    pause (100000000000000000000000000000000.0)




label secret1_ds:

    show screen secret1_ds

    pause (10000000000000000000.0)




label secret3_ds:

    show screen secret3_ds

    pause (10000000000000000000.0)


################################################################

