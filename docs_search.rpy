# define doc_search_item_01 = False # Резинка Мику, Под лестницей в музкружок
# define doc_search_item_02 = False # Блокнот Художника, Музкружок, рояль
# define doc_search_item_03 = False # Документы лётчика, Музкружок, за картиной
# define doc_search_item_04 = False # Неизвестная женская заколка, Каморка сторожа, кровать
# define doc_search_item_05 = False # Импортная зажигалка, Каморка сторожа, под кроватью
# define doc_search_item_06 = False # Часы Шурика, Кружок Усталые руки, внутри
# define doc_search_item_07 = False # Панамка ОД, вход в Бомбоубежище, под кустом
# define doc_search_item_08 = False # Дужка от очков Жени, Кружок Умелые руки, под столом
# define doc_search_item_09 = False # Синяя пуговица Атсуи, Генда, у подножья
# define doc_search_item_10 = False # Галстук Саманты, Крыша где хорошо целоваться
# define doc_search_item_11 = False # Нашивка Слави, чердак Алисы и Ульяны, за диваном в левом нижнем углу
# define doc_search_item_12 = False # Заколка Алисы, Нычка 2, возле лавки в нижнем левом углу
# define doc_search_item_13 = False # Пряжка от ремня. Нычка 7, в углу здания, у дальнего края лавки
# define doc_search_item_14 = False # Конверт со стихами-признанием. Библиотека, на полке
# define doc_search_item_15 = False # Чёрный шиньон, Раздевалка, шкафчик в верхнем рядку, в центре, возле угла


define doc_search_item_01 = True # Резинка Мику, Под лестницей в музкружок
define doc_search_item_02 = True # Блокнот Художника, Музкружок, рояль
define doc_search_item_03 = True # Документы лётчика, Музкружок, за картиной
define doc_search_item_04 = True # Неизвестная женская заколка, Каморка сторожа, кровать
define doc_search_item_05 = True # Импортная зажигалка, Каморка сторожа, под кроватью
define doc_search_item_06 = True # Часы Шурика, Кружок Усталые руки, внутри
define doc_search_item_07 = True # Панамка ОД, вход в Бомбоубежище, под кустом
define doc_search_item_08 = True # Дужка от очков Жени, Кружок Умелые руки, под столом
define doc_search_item_09 = True # Синяя пуговица Атсуи, Генда, у подножья
define doc_search_item_10 = True # Галстук Саманты, Крыша где хорошо целоваться
define doc_search_item_11 = True # Нашивка Слави, чердак Алисы и Ульяны, за диваном в левом нижнем углу
define doc_search_item_12 = True # Заколка Алисы, Нычка 2, возле лавки в нижнем левом углу
define doc_search_item_13 = True # Пряжка от ремня. Нычка 7, в углу здания, у дальнего края лавки
define doc_search_item_14 = True # Конверт со стихами-признанием. Библиотека, на полке
define doc_search_item_15 = True # Чёрный шиньон, Раздевалка, шкафчик в верхнем рядку, в центре, возле угла







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

        hotspot(453,214,95,57) action Hide ("docs_search"), Show ("watchcloset_ds")

        hotspot(775,78,106,57) action Hide ("docs_search"), Show ("tirhands_ds")

        hotspot(917,58,106,42) action Hide ("docs_search"), Show ("bombu_ds")

        hotspot(1057,99,198,68) action Hide ("docs_search"), Show ("handmade_ds")

        hotspot(947,383,87,31) action Hide ("docs_search"), Show ("genda_ds")

        hotspot(1295,284,215,58) action Hide ("docs_search"), Show ("kroof_ds")

        hotspot(1555,345,195,107) action Hide ("docs_search"), Show ("attic_ds")

        hotspot(1479,589,109,40) action Hide ("docs_search"), Show ("secret3_ds")

        hotspot(1210,753,107,40) action Hide ("docs_search"), Show ("secret2_ds")

        hotspot(902,911,119,46) action Hide ("docs_search"), Show ("secret1_ds")

        hotspot(331,887,112,38) action Hide ("docs_search"), Show ("secret7_ds")

        hotspot(394,568,182,47) action Hide ("docs_search"), Show ("library_ds")

        hotspot(543,469,87,38) action Hide ("docs_search"), Show ("dresser_ds")
            

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

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Нычка под лестницей в музкружок"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("mus_stairs_ds"), Show("docs_search")


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




screen library_ds:

    # Библиотека

    tag menu
    modal True
    zorder 300

    add "bg library"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Библиотека"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("library_ds"), Show("docs_search")


screen secret1_ds:

    # Нычка 1

    tag menu
    modal True
    zorder 300

    add "bg secret1"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Нычка 1"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret1_ds"), Show("docs_search")


screen genda_ds:

    # Генда

    tag menu
    modal True
    zorder 300

    add "bg genda"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Генда"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("genda_ds"), Show("docs_search")


screen watchcloset_ds:

    # Каморка сторожа

    tag menu
    modal True
    zorder 300

    add "bg watchcloset"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Каморка сторожа"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("watchcloset_ds"), Show("docs_search")


screen bombu_ds:

    # Вход в бомбоубежище

    tag menu
    modal True
    zorder 300

    add "bg bombu"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Вход в бомбоубежище"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("bombu_ds"), Show("docs_search")


screen handmade_ds:

    # Кружок «Умелые руки»

    tag menu
    modal True
    zorder 300

    add "bg handmade"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Кружок «Умелые руки»"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("handmade_ds"), Show("docs_search")


screen kroof_ds:

    # Крыша на которой удобно целоваться

    tag menu
    modal True
    zorder 300

    add "bg kroof"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Крыша на которой удобно целоваться"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("kroof_ds"), Show("docs_search")


screen secret2_ds:

    # Нычка 2

    tag menu
    modal True
    zorder 300

    add "bg secret2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Нычка 2"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret2_ds"), Show("docs_search")


screen secret3_ds:

    # Нычка 2

    tag menu
    modal True
    zorder 300

    add "bg secret3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Нычка 3"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret3_ds"), Show("docs_search")


screen attic_ds:

    # Чердак. Лучшая нычка для курения и игры в карты.

    tag menu
    modal True
    zorder 300

    add "bg attic"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Наш чердак."

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("attic_ds"), Show("docs_search")


screen tirhands_ds:

    # Кружок Усталые ручки

    tag menu
    modal True
    zorder 300

    add "bg tirhands"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Кружок Усталые ручки"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("tirhands_ds"), Show("docs_search")


screen tirhands2_ds:

    # Кружок Усталые ручки 2

    tag menu
    modal True
    zorder 300

    add "bg tirhands2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Кружок Усталые ручки"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("tirhands2_ds"), Show("docs_search")


screen secret7_ds:

    # Нычка 7

    tag menu
    modal True
    zorder 300

    add "bg secret7"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Нычка 7"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("secret7_ds"), Show("docs_search")


screen dresser_ds:

    # Раздевалка

    tag menu
    modal True
    zorder 300

    add "bg dresser"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "DocsSearchStyleTitle"
        vbox:
            style_prefix "DocsSearchStyleTitle"
            vbox:
                style_prefix "DocsSearchStyleTitle"
                text "Раздевалка"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("dresser_ds"), Show("docs_search")


label docs_search:

    show screen docs_search

    pause (10000000000000000000.0)


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
 
# label atsuroom:
    # scene bg atsuroom with dissolve
    # "Комната Атсуи"
    # scene bg atsuroom2 with dissolve
    # "Комната Атсуи2"
    # call screen docs_search
    # return
    
# label showers:
    # scene bg showers with dissolve
    # "Душевые"
    # scene bg showers2 with dissolve
    # "Душевые2"
    # call screen docs_search
    # return
    
# label zcloset:
    # scene bg zcloset with dissolve
    # "Каморка Жени"
    # scene bg zcloset2 with dissolve
    # "Каморка Жени2"
    # call screen docs_search
    # return
    
# label diroom:
    # scene bg diroom with dissolve
    # "Комната директрисы"
    # call screen docs_search
    # return
    
# label library:
    # scene bg library with dissolve
    # "Библиотека"
    # scene bg library2 with dissolve
    # "Библиотека2"
    # call screen docs_search
    # return
    
# label medic:
    # scene bg medic with dissolve
    # "Медпункт"
    # call screen docs_search
    # return
    
# label viroom:
    # scene bg viroom with dissolve
    # "Комната Виолы"
    # call screen docs_search
    # return
    
# label odhouse:
    # scene bg odhouse with dissolve
    # "Домик ОД и Семёна"
    # scene bg odhouse2 with dissolve
    # "Комната ОД"
    # scene bg odhouse3 with dissolve
    # "Комната Семёна"
    # call screen docs_search
    # return
    
# label msecret:
    # scene bg msecret with dissolve
    # "Чердак меганычка"
    # scene bg msecret2 with dissolve
    # "Чердак меганычка2"
    # call screen docs_search
    # return
    
# label secret1:
    # scene bg secret1 with dissolve
    # "Нычка 1"
    # call screen docs_search
    # return
    
# label genda:
    # scene bg genda with dissolve
    # "Генда"
    # call screen docs_search
    # return
    
# label square:
    # scene bg square with dissolve
    # "Площадь"
    # call screen docs_search
    # return
    
# label lmhouse:
    # scene bg lmhouse with dissolve
    # "Домик Лены и Мику"
    # scene bg lmhouse2 with dissolve
    # "Домик Лены и Мику2"
    # call screen docs_search
    # return
    
# label dining:
    # scene bg dining with dissolve
    # "Столовая"
    # call screen docs_search
    # return
    
# label watchcloset:
    # scene bg watchcloset with dissolve
    # "Каморка сторожа"
    # call screen docs_search
    # return
    
# label stock:
    # scene bg stock with dissolve
    # "Склад"
    # scene bg stock2 with dissolve
    # "Склад2"
    # call screen docs_search
    # return
    
# label busstop:
    # scene bg busstop5 with dissolve
    # "Центральный вход. Автобус 410"
    # scene bg busstop4 with dissolve
    # "Центральный вход. Автобус 410 2"
    # scene bg busstop with dissolve
    # "Центральный вход. Автобус 410 3"
    # scene bg busstop3 with dissolve
    # "Центральный вход. Автобус 410 4"
    # call screen docs_search
    # return
    
# label stand:
    # scene bg stand with dissolve
    # "Cтенд. Рассписание"
    # call screen docs_search
    # return
    
# label secret4:
    # scene bg secret4 with dissolve
    # "Нычка 4. Гитара"
    # call screen docs_search
    # return
    
# label bombu:
    # scene bg bombu with dissolve
    # "Вход в бомбоубежище"
    # scene bg bombu2 with dissolve
    # "Вход в бомбоубежище2"
    # call screen docs_search
    # return
    
# label stadium:
    # scene bg stadium with dissolve
    # "Стадион"
    # scene bg stadium2 with dissolve
    # "Стадион2"
    # call screen docs_search
    # return
    
# label stage:
    # scene bg stage with dissolve
    # "Эстрада"
    # scene bg stage2 with dissolve
    # "Эстрада2"
    # call screen docs_search
    # return
    
# label handmade:
    # scene bg handmade with dissolve
    # 'Кружок "Умелые руки"'
    # call screen docs_search
    # return
    
# label gteach:
    # scene bg gteach with dissolve
    # "Комната физрука и завхоза"
    # call screen docs_search
    # return
    
# label fotoc:
    # scene bg fotoc with dissolve
    # "Фотостудия"
    # call screen docs_search
    # return
    
# label kroof:
    # scene bg kroof with dissolve
    # "Крыша на которой удобно целоваться"
    # call screen docs_search
    # return
    
# label szhhouse:
    # scene bg szhhouse with dissolve
    # "Домик Слави и Жени"
    # call screen docs_search
    # return
    
# label secret2:
    # scene bg secret2 with dissolve
    # "Нычка 2"
    # call screen docs_search
    # return
    
# label secret3:
    # scene bg secret3 with dissolve
    # "Нычка 3"
    # call screen docs_search
    
# label shande:
    # scene bg shande with dissolve
    # "2 этаж. Шурик и Электроник"
    # call screen docs_search
    # return
    
# label stels:
    # scene bg stels with dissolve
    # "Лазейка. Уйти незаметно."
    # call screen docs_search
    # return
    
# label attic:
    # scene bg attic with dissolve
    # "Чердак. Лучшая нычка для курения и игры в карты."
    # call screen docs_search
    # return
    
# label auhouse:
    # scene bg auhouse with dissolve
    # "Домик Алисы и Ульяны."
    # scene bg auhouse2 with dissolve
    # "Домик Алисы и Ульяны2."
    # call screen docs_search
    # return
    
# label pointers:
    # scene bg pointers with dissolve
    # "Тропинка. Указатели."
    # call screen map
    # return
    
# label tirhands:
    # scene bg tirhands with dissolve
    # "Кружок Усталые ручки"
    # scene bg tirhands2 with dissolve
    # "Кружок Усталые ручки2"
    # call screen docs_search
    # return
    
# label peep1:
    # scene bg peep1 with dissolve
    # "Подглядывать 1"
    # call screen docs_search
    # return
    
# label peep2:
    # scene bg peep2 with dissolve
    # "Подглядывать 2"
    # call screen docs_search
    # return
    
# label peep3:
    # scene bg peep3 with dissolve
    # "Подглядывать 3"
    # scene bg peep32 with dissolve
    # "Подглядывать 3 2"
    # call screen docs_search
    # return
    
# label peep4:
    # scene bg peep4 with dissolve
    # "Подглядывать 4"
    # call screen docs_search
    # return
    
# label peep5:
    # scene bg peep5 with dissolve
    # "Подглядывать 5"
    # call screen docs_search
    # return
    
# label peep6:
    # scene bg peep6 with dissolve
    # "Подглядывать 6"
    # call screen docs_search
    # return
    
# label secret7:
    # scene bg secret7 with dissolve
    # "Нычка 7"
    # scene bg secret72 with dissolve
    # "Нычка 7 2"
    # call screen docs_search
    # return
    
# label sroom:
    # scene bg sroom with dissolve
    # "Комната саманты"
    # call screen docs_search
    # return