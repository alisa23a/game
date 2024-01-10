#экран карты лагеря
screen campmap:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/bg/campidle.webp"
        idle "images/bg/campidle.webp"
        hover "images/bg/camphover.webp"
        
        if cm1:
            hotspot(147,251,149,66) action Hide ("campmap"), Show ("mus")
        if cm2:
            hotspot(286,327,99,53) action Hide ("campmap"), Show ("atsuroom")
        if cm3:
            hotspot(356,255,89,37) action Hide ("campmap"), Show ("showers")
        if cm4:
            hotspot(215,477,101,59) action Hide ("campmap"), Show ("zcloset")
        if cm5:
            hotspot(331,441,151,55) action Hide ("campmap"), Show ("diroom")
        if cm6:
            hotspot(394,568,182,47) action Hide ("campmap"), Show ("library")
        if cm7:
            hotspot(445,644,175,49) action Hide ("campmap"), Show ("medic")
        if cm8:
            hotspot(453,752,212,45) action Hide ("campmap"), Show ("viroom")
        if cm9:
            hotspot(520,859,259,93) action Hide ("campmap"), Show ("odhouse")
        if cm10:
            hotspot(593,965,149,61) action Hide ("campmap"), Show ("msecret")
        if cm11:
            hotspot(902,911,119,46) action Hide ("campmap"), Show ("secret1")
        if cm12:
            hotspot(947,383,87,31) action Hide ("campmap"), Show ("genda")
        if cm13:
            hotspot(950,516,112,49) action Hide ("campmap"), Show ("square")
        if cm14:
            hotspot(952,668,238,90) action Hide ("campmap"), Show ("lmhouse")
        if cm15:
            hotspot(1180,360,151,43) action Hide ("campmap"), Show ("dining")
        if cm16:
            hotspot(453,214,95,57) action Hide ("campmap"), Show ("watchcloset")
        if cm17:
            hotspot(499,291,83,34) action Hide ("campmap"), Show ("stock")
        if cm18:
            hotspot(592,81,174,62) action Hide ("campmap"), Show ("busstop_cm")
        if cm19:
            hotspot(657,214,109,68) action Hide ("campmap"), Show ("info_stand")
        if cm20:
            hotspot(767,182,108,65) action Hide ("campmap"), Show ("secret4")
        if cm21:
            hotspot(917,58,106,42) action Hide ("campmap"), Show ("bombu")
        if cm22:
            hotspot(615,310,125,37) action Hide ("campmap"), Show ("stadium")
        if cm23:
            hotspot(661,388,137,46) action Hide ("campmap"), Show ("stage")
        if cm24:
            hotspot(1057,99,198,68) action Hide ("campmap"), Show ("handmade")
        if cm25:
            hotspot(1258,135,169,53) action Hide ("campmap"), Show ("gteach")
        if cm26:
            hotspot(1070,268,127,36) action Hide ("campmap"), Show ("fotoc")
        if cm27:
            hotspot(1295,284,215,58) action Hide ("campmap"), Show ("kroof")
        if cm28:
            hotspot(1234,526,211,65) action Hide ("campmap"), Show ("szhhouse")
        if cm29:
            hotspot(1210,753,107,40) action Hide ("campmap"), Show ("secret2")
        if cm30:
            hotspot(1479,589,109,40) action Hide ("campmap"), Show ("secret3")
        if cm31:
            hotspot(1243,627,165,101) action Hide ("campmap"), Show ("shande")
        if cm32:
            hotspot(1521,280,132,53) action Hide ("campmap"), Show ("stels")
        if cm33:
            hotspot(1555,345,195,107) action Hide ("campmap"), Show ("attic")
        if cm34:
            hotspot(1483,495,216,69) action Hide ("campmap"), Show ("auhouse")
        if cm35:
            hotspot(1702,97,198,180) action Hide ("campmap"), Show ("pointers")
        if cm36:
            hotspot(775,78,106,57) action Hide ("campmap"), Show ("tirhands")
        if cm37:
            hotspot(213,221,132,29) action Hide ("campmap"), Show ("peep1")
        if cm38:
            hotspot(48,417,150,38) action Hide ("campmap"), Show ("peep2")
        if cm39:
            hotspot(386,378,153,32) action Hide ("campmap"), Show ("peep3")
        if cm40:
            hotspot(127,185,167,33) action Hide ("campmap"), Show ("peep4")
        if cm41:
            hotspot(298,833,180,35) action Hide ("campmap"), Show ("peep5")
        if cm42:
            hotspot(205,735,163,31) action Hide ("campmap"), Show ("peep6")
        if cm43:
            hotspot(331,887,112,38) action Hide ("campmap"), Show ("secret7")
        if cm44:
            hotspot(421,336,193,34) action Hide ("campmap"), Show ("sroom")
        if cm45:
            hotspot(543,469,87,38) action Hide ("campmap"), Show ("dresser")
        if cm46:
            hotspot(914,125,115,51) action Hide ("campmap"), Show ("basketball")
        if cm47:
            hotspot(340,511,95,53) action Hide ("campmap"), Show ("caretakers_room")
        if cm48:
            hotspot(460,523,150,42) action Hide ("campmap"), Show ("fine_arts")
        if cm49:
            hotspot(1049,316,82,68) action Hide ("campmap"), Show ("dining_menu")
        if cm50:
            hotspot(1183,424,171,72) action Hide ("campmap"), Show ("sewing")
            

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("campmap"), Show ("info_stand")


# Локации лагеря

screen mus:

    # Музыкальный и хореографический кружок

    tag menu
    modal True
    zorder 300

    add "bg mus"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Музыкальный и хореографический кружок"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("mus"), Show("campmap")


screen atsuroom:

    # Комната Атсуи

    tag menu
    modal True
    zorder 300

    add "bg atsuroom"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната Атсуи"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("atsuroom"), Show("atsuroom2")


screen atsuroom2:

    # Комната Атсуи 2

    tag menu
    modal True
    zorder 300

    add "bg atsuroom2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната Атсуи"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("atsuroom2"), Show("campmap")


screen showers:

    # Душевые

    tag menu
    modal True
    zorder 300

    add "bg showers"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Душевые"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("showers"), Show("showers2")


screen showers2:

    # Душевые 2

    tag menu
    modal True
    zorder 300

    add "bg showers2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Душевые"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("showers2"), Show("campmap")


screen zcloset:

    # Каморка Жени

    tag menu
    modal True
    zorder 300

    add "bg zcloset"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Каморка Жени"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("zcloset"), Show("zcloset2")


screen zcloset2:

    # Каморка Жени 2

    tag menu
    modal True
    zorder 300

    add "bg zcloset2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Каморка Жени"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("zcloset2"), Show("campmap")


screen diroom:

    # Комната директрисы

    tag menu
    modal True
    zorder 300

    add "bg diroom"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната директрисы"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("diroom"), Show("campmap")


screen library:

    # Библиотека

    tag menu
    modal True
    zorder 300

    add "bg library"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Библиотека"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("library"), Show("library2")


screen library2:

    # Библиотека 2

    tag menu
    modal True
    zorder 300

    add "bg library2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Библиотека"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("library2"), Show("campmap")


screen medic:

    # Медпункт

    tag menu
    modal True
    zorder 300

    add "bg medic"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Медпункт"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("medic"), Show("campmap")


screen viroom:

    # Комната Виолы

    tag menu
    modal True
    zorder 300

    add "bg viroom"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната Виолы"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("viroom"), Show("campmap")


screen odhouse:

    # Домик ОД и Семёна

    tag menu
    modal True
    zorder 300

    add "bg odhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик ОД и Семёна"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("odhouse"), Show("odhouse2")


screen odhouse2:

    # Комната ОД

    tag menu
    modal True
    zorder 300

    add "bg odhouse2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната ОД"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("odhouse2"), Show("odhouse3")


screen odhouse3:

    # Комната Семёна

    tag menu
    modal True
    zorder 300

    add "bg odhouse3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната Семёна"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("odhouse3"), Show("campmap")


screen msecret:

    # Чердак меганычка

    tag menu
    modal True
    zorder 300

    add "bg msecret"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Чердак меганычка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("msecret"), Show("msecret2")


screen msecret2:

    # Чердак меганычка 2

    tag menu
    modal True
    zorder 300

    add "bg msecret2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Чердак меганычка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("msecret2"), Show("campmap")


screen secret1:

    # Нычка 1

    tag menu
    modal True
    zorder 300

    add "bg secret1"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 1"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret1"), Show("campmap")


screen genda:

    # Генда

    tag menu
    modal True
    zorder 300

    add "bg genda"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Генда"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("genda"), Show("campmap")


screen square:

    # Площадь

    tag menu
    modal True
    zorder 300

    add "bg square"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Площадь"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("square"), Show("campmap")


screen lmhouse:

    # Домик Лены и Мику

    tag menu
    modal True
    zorder 300

    add "bg lmhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик Лены и Мику"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("lmhouse"), Show("lmhouse2")


screen lmhouse2:

    # Домик Лены и Мику 2

    tag menu
    modal True
    zorder 300

    add "bg lmhouse2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик Лены и Мику"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("lmhouse2"), Show("campmap")


screen dining:

    # Столовая

    tag menu
    modal True
    zorder 300

    add "bg dining"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Столовая"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dining"), Show("campmap")


screen watchcloset:

    # Каморка сторожа

    tag menu
    modal True
    zorder 300

    add "bg watchcloset"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Каморка сторожа"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("watchcloset"), Show("campmap")


screen stock:

    # Склад

    tag menu
    modal True
    zorder 300

    add "bg stock"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Склад"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stock"), Show("stock2")


screen stock2:

    # Склад 2

    tag menu
    modal True
    zorder 300

    add "bg stock2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Склад"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stock2"), Show("campmap")


screen stock2:

    # Склад 2

    tag menu
    modal True
    zorder 300

    add "bg stock2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Склад"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stock2"), Show("campmap")


screen busstop_cm:

    # Центральный вход. Автобус 410

    tag menu
    modal True
    zorder 300

    add "bg busstop5"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Центральный вход. Автобус 410"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("busstop_cm"), Show("busstop_cm2")


screen busstop_cm2:

    # Центральный вход. Автобус 410 2

    tag menu
    modal True
    zorder 300

    add "bg busstop4"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Центральный вход. Автобус 410"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("busstop_cm2"), Show("busstop_cm3")


screen busstop_cm3:

    # Центральный вход. Автобус 410 3

    tag menu
    modal True
    zorder 300

    add "bg busstop"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Центральный вход. Автобус 410"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("busstop_cm3"), Show("busstop_cm4")


screen busstop_cm4:

    # Центральный вход. Автобус 410 4

    tag menu
    modal True
    zorder 300

    add "bg busstop3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Центральный вход. Автобус 410"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("busstop_cm"), Show("campmap")


screen secret4:

    # Нычка 4. Гитара

    tag menu
    modal True
    zorder 300

    add "bg secret4"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 4. Гитара"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret4"), Show("campmap")


screen bombu:

    # Вход в бомбоубежище

    tag menu
    modal True
    zorder 300

    add "bg bombu"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Вход в бомбоубежище"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("bombu"), Show("bombu2")


screen bombu2:

    # Вход в бомбоубежище 2

    tag menu
    modal True
    zorder 300

    add "bg bombu2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Вход в бомбоубежище"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("bombu2"), Show("campmap")


screen stadium:

    # Стадион

    tag menu
    modal True
    zorder 300

    add "bg stadium"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Стадион"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stadium"), Show("stadium2")


screen stadium2:

    # Стадион 2

    tag menu
    modal True
    zorder 300

    add "bg stadium2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Стадион"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stadium2"), Show("campmap")


screen stage:

    # Эстрада

    tag menu
    modal True
    zorder 300

    add "bg stage"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Эстрада"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stage"), Show("stage2")


screen stage2:

    # Эстрада 2

    tag menu
    modal True
    zorder 300

    add "bg stage2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Эстрада"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stage2"), Show("campmap")


screen handmade:

    # Кружок «Умелые руки»

    tag menu
    modal True
    zorder 300

    add "bg handmade"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кружок «Умелые руки»"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("handmade"), Show("campmap")


screen gteach:

    # Комната физрука и завхоза

    tag menu
    modal True
    zorder 300

    add "bg gteach"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната физрука и завхоза"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("gteach"), Show("campmap")


screen fotoc:

    # Фотостудия

    tag menu
    modal True
    zorder 300

    add "bg fotoc"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Фотостудия"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("fotoc"), Show("campmap")


screen kroof:

    # Крыша на которой удобно целоваться

    tag menu
    modal True
    zorder 300

    add "bg kroof"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Крыша на которой удобно целоваться"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("kroof"), Show("campmap")


screen szhhouse:

    # Домик Слави и Жени

    tag menu
    modal True
    zorder 300

    add "bg szhhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик Слави и Жени"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("szhhouse"), Show("campmap")


screen secret2:

    # Нычка 2

    tag menu
    modal True
    zorder 300

    add "bg secret2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 2"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret2"), Show("campmap")


screen secret3:

    # Нычка 2

    tag menu
    modal True
    zorder 300

    add "bg secret3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 3"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret3"), Show("campmap")


screen shande:

    # 2 этаж. Шурик и Электроник

    tag menu
    modal True
    zorder 300

    add "bg shande"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "2 этаж. Шурик и Электроник"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("shande"), Show("campmap")


screen stels:

    # Лазейка. Уйти незаметно

    tag menu
    modal True
    zorder 300

    add "bg stels"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Лазейка. Уйти незаметно."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("stels"), Show("campmap")


screen attic:

    # Чердак. Лучшая нычка для курения и игры в карты.

    tag menu
    modal True
    zorder 300

    add "bg attic"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Чердак. Лучшая нычка для курения и игры в карты."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("attic"), Show("campmap")


screen auhouse:

    # Домик Алисы и Ульяны

    tag menu
    modal True
    zorder 300

    add "bg auhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик Алисы и Ульяны"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("auhouse"), Show("auhouse2")


screen auhouse2:

    # Домик Алисы и Ульяны 2

    tag menu
    modal True
    zorder 300

    add "bg auhouse2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Домик Алисы и Ульяны"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("auhouse2"), Show("campmap")


screen tirhands:

    # Кружок Усталые ручки

    tag menu
    modal True
    zorder 300

    add "bg tirhands"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кружок Усталые ручки"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tirhands"), Show("tirhands2")


screen tirhands2:

    # Кружок Усталые ручки 2

    tag menu
    modal True
    zorder 300

    add "bg tirhands2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кружок Усталые ручки"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tirhands2"), Show("campmap")


screen peep1:

    # Подглядывать 1

    tag menu
    modal True
    zorder 300

    add "bg peep1"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 1"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep1"), Show("campmap")


screen peep2:

    # Подглядывать 2

    tag menu
    modal True
    zorder 300

    add "bg peep2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 2"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep2"), Show("campmap")


screen peep3:

    # Подглядывать 3

    tag menu
    modal True
    zorder 300

    add "bg peep3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 3"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep3"), Show("peep32")


screen peep32:

    # Подглядывать 3 2

    tag menu
    modal True
    zorder 300

    add "bg peep32"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 3 2"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep32"), Show("campmap")


screen peep4:

    # Подглядывать 4

    tag menu
    modal True
    zorder 300

    add "bg peep4"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 4"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep4"), Show("campmap")



screen peep5:

    # Подглядывать 5

    tag menu
    modal True
    zorder 300

    add "bg peep5"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 5"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep5"), Show("campmap")



screen peep6:

    # Подглядывать 6

    tag menu
    modal True
    zorder 300

    add "bg peep6"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Подглядывать 6"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("peep6"), Show("campmap")



screen secret7:

    # Нычка 7

    tag menu
    modal True
    zorder 300

    add "bg secret7"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 7"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret7"), Show("secret72")


screen secret72:

    # Нычка 7 2

    tag menu
    modal True
    zorder 300

    add "bg secret72"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Нычка 7 2"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("secret72"), Show("campmap")


screen sroom:

    # Комната саманты

    tag menu
    modal True
    zorder 300

    add "bg sroom"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната саманты"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sroom"), Show("campmap")


screen dresser:

    # Раздевалка

    tag menu
    modal True
    zorder 300

    add "bg dresser"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Раздевалка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dresser"), Show("dresser2")


screen dresser2:

    # Раздевалка 2

    tag menu
    modal True
    zorder 300

    add "bg dresser2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Раздевалка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dresser2"), Show("campmap")


screen basketball:

    # Баскетбольная площадка

    tag menu
    modal True
    zorder 300

    add "bg basketball"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Баскетбольная площадка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("basketball"), Show("campmap")


screen caretakers_room:

    # Комната завхоза

    tag menu
    modal True
    zorder 300

    add "bg caretakers_room"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната завхоза"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("caretakers_room"), Show("caretakers_room2")


screen caretakers_room2:

    # Комната завхоза 2

    tag menu
    modal True
    zorder 300

    add "bg caretakers_room2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната завхоза"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("caretakers_room2"), Show("campmap")


screen fine_arts:

    # Кружок ИЗО

    tag menu
    modal True
    zorder 300

    add "bg fine_arts"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кружок ИЗО"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("fine_arts"), Show("campmap")


screen dining_menu:

    # Меню столовой

    tag menu
    modal True
    zorder 300

    add "bg dining_menu"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Меню столовой"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dining_menu"), Show("campmap")


screen sewing:

    # Кружок кройки и шитья

    tag menu
    modal True
    zorder 300

    add "bg sewing"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кружок кройки и шитья"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sewing"), Show("campmap")



label mus:
    scene bg mus with dissolve
    "Музыкальный и хореографический кружок"
    call screen campmap
    return
    
label atsuroom:
    scene bg atsuroom with dissolve
    "Комната Атсуи"
    scene bg atsuroom2 with dissolve
    "Комната Атсуи2"
    call screen campmap
    return
    
label showers:
    scene bg showers with dissolve
    "Душевые"
    scene bg showers2 with dissolve
    "Душевые2"
    call screen campmap
    return
    
label zcloset:
    scene bg zcloset with dissolve
    "Каморка Жени"
    scene bg zcloset2 with dissolve
    "Каморка Жени2"
    call screen campmap
    return
    
label diroom:
    scene bg diroom with dissolve
    "Комната директрисы"
    call screen campmap
    return
    
label library:
    scene bg library with dissolve
    "Библиотека"
    scene bg library2 with dissolve
    "Библиотека2"
    call screen campmap
    return
    
label medic:
    scene bg medic with dissolve
    "Медпункт"
    call screen campmap
    return
    
label viroom:
    scene bg viroom with dissolve
    "Комната Виолы"
    call screen campmap
    return
    
label odhouse:
    scene bg odhouse with dissolve
    "Домик ОД и Семёна"
    scene bg odhouse2 with dissolve
    "Комната ОД"
    scene bg odhouse3 with dissolve
    "Комната Семёна"
    call screen campmap
    return
    
label msecret:
    scene bg msecret with dissolve
    "Чердак меганычка"
    scene bg msecret2 with dissolve
    "Чердак меганычка2"
    call screen campmap
    return
    
label secret1:
    scene bg secret1 with dissolve
    "Нычка 1"
    call screen campmap
    return
    
label genda:
    scene bg genda with dissolve
    "Генда"
    call screen campmap
    return
    
label square:
    scene bg square with dissolve
    "Площадь"
    call screen campmap
    return
    
label lmhouse:
    scene bg lmhouse with dissolve
    "Домик Лены и Мику"
    scene bg lmhouse2 with dissolve
    "Домик Лены и Мику2"
    call screen campmap
    return
    
label dining:
    scene bg dining with dissolve
    "Столовая"
    call screen campmap
    return
    
label watchcloset:
    scene bg watchcloset with dissolve
    "Каморка сторожа"
    call screen campmap
    return
    
label stock:
    scene bg stock with dissolve
    "Склад"
    scene bg stock2 with dissolve
    "Склад2"
    call screen campmap
    return
    
label busstop:
    scene bg busstop5 with dissolve
    "Центральный вход. Автобус 410"
    scene bg busstop4 with dissolve
    "Центральный вход. Автобус 410 2"
    scene bg busstop with dissolve
    "Центральный вход. Автобус 410 3"
    scene bg busstop3 with dissolve
    "Центральный вход. Автобус 410 4"
    call screen campmap
    return
    
label stand:
    scene bg stand with dissolve
    "Cтенд. Рассписание"
    call screen campmap
    return
    
label secret4:
    scene bg secret4 with dissolve
    "Нычка 4. Гитара"
    call screen campmap
    return
    
label bombu:
    scene bg bombu with dissolve
    "Вход в бомбоубежище"
    scene bg bombu2 with dissolve
    "Вход в бомбоубежище2"
    call screen campmap
    return
    
label stadium:
    scene bg stadium with dissolve
    "Стадион"
    scene bg stadium2 with dissolve
    "Стадион2"
    call screen campmap
    return
    
label stage:
    scene bg stage with dissolve
    "Эстрада"
    scene bg stage2 with dissolve
    "Эстрада2"
    call screen campmap
    return
    
label handmade:
    scene bg handmade with dissolve
    'Кружок "Умелые руки"'
    call screen campmap
    return
    
label gteach:
    scene bg gteach with dissolve
    "Комната физрука и завхоза"
    call screen campmap
    return
    
label fotoc:
    scene bg fotoc with dissolve
    "Фотостудия"
    call screen campmap
    return
    
label kroof:
    scene bg kroof with dissolve
    "Крыша на которой удобно целоваться"
    call screen campmap
    return
    
label szhhouse:
    scene bg szhhouse with dissolve
    "Домик Слави и Жени"
    call screen campmap
    return
    
label secret2:
    scene bg secret2 with dissolve
    "Нычка 2"
    call screen campmap
    return
    
label secret3:
    scene bg secret3 with dissolve
    "Нычка 3"
    call screen campmap
    
label shande:
    scene bg shande with dissolve
    "2 этаж. Шурик и Электроник"
    call screen campmap
    return
    
label stels:
    scene bg stels with dissolve
    "Лазейка. Уйти незаметно."
    call screen campmap
    return
    
label attic:
    scene bg attic with dissolve
    "Чердак. Лучшая нычка для курения и игры в карты."
    call screen campmap
    return
    
label auhouse:
    scene bg auhouse with dissolve
    "Домик Алисы и Ульяны."
    scene bg auhouse2 with dissolve
    "Домик Алисы и Ульяны2."
    call screen campmap
    return
    
label pointers:
    scene bg pointers with dissolve
    "Тропинка. Указатели."
    call screen map
    return
    
label tirhands:
    scene bg tirhands with dissolve
    "Кружок Усталые ручки"
    scene bg tirhands2 with dissolve
    "Кружок Усталые ручки2"
    call screen campmap
    return
    
label peep1:
    scene bg peep1 with dissolve
    "Подглядывать 1"
    call screen campmap
    return
    
label peep2:
    scene bg peep2 with dissolve
    "Подглядывать 2"
    call screen campmap
    return
    
label peep3:
    scene bg peep3 with dissolve
    "Подглядывать 3"
    scene bg peep32 with dissolve
    "Подглядывать 3 2"
    call screen campmap
    return
    
label peep4:
    scene bg peep4 with dissolve
    "Подглядывать 4"
    call screen campmap
    return
    
label peep5:
    scene bg peep5 with dissolve
    "Подглядывать 5"
    call screen campmap
    return
    
label peep6:
    scene bg peep6 with dissolve
    "Подглядывать 6"
    call screen campmap
    return
    
label secret7:
    scene bg secret7 with dissolve
    "Нычка 7"
    scene bg secret72 with dissolve
    "Нычка 7 2"
    call screen campmap
    return
    
label sroom:
    scene bg sroom with dissolve
    "Комната саманты"
    call screen campmap
    return