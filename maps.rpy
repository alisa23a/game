#Локации на карте мира

style LocationStyleTitle_text:
    color "#fff"
    font "fonts/mateur-webfont.ttf"
    size 50
    
style LocationStyleText_text:
    color "#fff"
    #font "fonts/mateur-webfont.ttf"
    size 30

#style InvItemPrevCaption_frame:
    #background None

style InvItemPrevCaption_text:
    color "#fff"
    size 20

style LocationStyleTitle_vbox:
    background ("#000")
    #xalign (0.5) yalign (0.07)


screen nbeach:

    # Пляж ближний

    #tag menu
    modal True
    zorder 300

    add "bg nbeach"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж ближний"
                
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("nbeach"), Show("nbeach2")

screen nbeach2:

    # Пляж ближний 2

    #tag menu
    modal True
    zorder 300

    add "bg nbeach2"
 
    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж ближний"
 
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("nbeach2"), Show("nbeach3")

screen nbeach3:

    # Пляж ближний 3

    #tag menu
    modal True
    zorder 300

    add "bg nbeach3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж ближний"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("nbeach3"), Show("nbeach4")

screen nbeach4:

    # Пляж ближний 4

    #tag menu
    modal True
    zorder 300

    add "bg nbeach4"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж ближний"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("nbeach4"), Show("map")

screen gog:

    # Поляна слётов

    #tag menu
    modal True
    zorder 300

    add "bg gog"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Поляна слётов"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("gog"), Show("map")


screen smg:

    # Малая поляна

    #tag menu
    modal True
    zorder 300

    add "bg smg"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Малая поляна"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("smg"), Show("map")


screen disland:

    # Остров Дальний

    #tag menu
    modal True
    zorder 300

    add "bg disland"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Остров Дальний"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("disland"), Show("disland2")


screen disland2:

    # Остров Дальний 2

    #tag menu
    modal True
    zorder 300

    add "bg disland2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Остров Дальний"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("disland2"), Show("map")


screen lakedeep:

    # Озеро Глубокое

    #tag menu
    modal True
    zorder 300

    add "bg lakedeep"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Озеро Глубокое"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("lakedeep"), Show("lakedeep2")


screen lakedeep2:

    # Озеро Глубокое 2

    #tag menu
    modal True
    zorder 300

    add "bg lakedeep2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Озеро Глубокое"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("lakedeep2"), Show("map")


screen uhouse:

    # Дом Юли

    #tag menu
    modal True
    zorder 300

    add "bg uhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дом Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse"), Show("uhouse2")


screen uhouse2:

    # Дом Юли 2

    #tag menu
    modal True
    zorder 300

    add "bg uhouse2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дом Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse2"), Show("uhouse3")


screen uhouse3:

    # Комната Юли

    #tag menu
    modal True
    zorder 300

    add "bg uhouse3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Комната Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse3"), Show("uhouse4")


screen uhouse4:

    # Камин Юли

    #tag menu
    modal True
    zorder 300

    add "bg uhouse4"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Камин Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse4"), Show("uhouse5")


screen uhouse5:

    # Кровать Юли

    #tag menu
    modal True
    zorder 300

    add "bg uhouse5"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кровать Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse5"), Show("uhouse6")


screen uhouse6:

    # Ванна Юли

    #tag menu
    modal True
    zorder 300

    add "bg uhouse6"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Ванна Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("uhouse6"), Show("map")


screen newtcreek:

    # Ручей тритонов

    #tag menu
    modal True
    zorder 300

    add "bg newtcreek"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Ручей тритонов"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("newtcreek"), Show("map")


screen newtcreek:

    # Ручей тритонов

    #tag menu
    modal True
    zorder 300

    add "bg newtcreek"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Ручей тритонов"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("newtcreek"), Show("map")


screen thiefpath:

    # Тропа украденной котлеты

    #tag menu
    modal True
    zorder 300

    add "bg thiefpath"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тропа украденной котлеты"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("thiefpath"), Show("map")


screen swamp:

    # Болота

    #tag menu
    modal True
    zorder 300

    add "bg swamp"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Болота"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("swamp"), Show("map")


screen boat_station:

    # Лодочная станция

    #tag menu
    modal True
    zorder 300

    add "bg boat_station"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Лодочная станция"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("boat_station"), Show("map")


screen fbeach:

    # Пляж дальний

    #tag menu
    modal True
    zorder 300

    add "bg fbeach"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж дальний"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("fbeach"), Show("map")


screen mcity:

    # Посёлок Рудный

    #tag menu
    modal True
    zorder 300

    add "bg mcity"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Посёлок Рудный"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("mcity"), Show("mcity2")


screen mcity2:

    # Посёлок Рудный 2

    #tag menu
    modal True
    zorder 300

    add "bg mcity2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Посёлок Рудный"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("mcity2"), Show("map")


screen dpeak:

    # Пик Двачевской

    #tag menu
    modal True
    zorder 300

    add "bg dpeak"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пик Двачевской"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dpeak"), Show("map")


screen ushallow:

    # Ульянина мель

    #tag menu
    modal True
    zorder 300

    add "bg ushallow"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Ульянина мель"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("ushallow"), Show("map")


screen shpi:

    # Шалаш пионера

    #tag menu
    modal True
    zorder 300

    add "bg shpi"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Шалаш пионера"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("shpi"), Show("map")


screen cave:

    # Пещера

    #tag menu
    modal True
    zorder 300

    add "bg cave"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пещера"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("cave"), Show("map")


screen moсr:

    # Горный ручей

    #tag menu
    modal True
    zorder 300

    add "bg moсr"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Горный ручей"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("moсr"), Show("map")


screen opine:

    # Сосна совы

    #tag menu
    modal True
    zorder 300

    add "bg opine"
    add "tips_owl_anim"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Сосна совы"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("opine"), Show("map")


screen laboratory:

    # Лаборатория

    #tag menu
    modal True
    zorder 300

    add "bg laboratory"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Лаборатория"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("laboratory"), Show("map")


screen oldroad:

    # Старая дорога

    #tag menu
    modal True
    zorder 300

    add "bg oldroad"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старая дорога"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldroad"), Show("map")


screen tcc:

    # Тропа безбашенных альпинистов

    #tag menu
    modal True
    zorder 300

    add "bg tcc"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тропа безбашенных альпинистов"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tcc"), Show("map")


screen goldd:

    # Землянка золотоискателя

    #tag menu
    modal True
    zorder 300

    add "bg goldd"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Землянка золотоискателя"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("goldd"), Show("map")


screen oldcamp:

    # Старый лагерь

    #tag menu
    modal True
    zorder 300

    add "bg oldcamp"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старый лагерь"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcamp"), Show("oldcamp2")


screen oldcamp2:

    # Старый лагерь 2

    #tag menu
    modal True
    zorder 300

    add "bg oldcamp2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старый лагерь"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcamp2"), Show("oldcamp3")


screen oldcamp3:

    # Старый лагерь 3

    #tag menu
    modal True
    zorder 300

    add "bg oldcamp3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старый лагерь"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcamp3"), Show("map")


screen bravepath:

    # Тропа отважных

    #tag menu
    modal True
    zorder 300

    add "bg bravepath"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тропа отважных"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("bravepath"), Show("bravepath2")


screen bravepath2:

    # Тропа отважных 2

    #tag menu
    modal True
    zorder 300

    add "bg bravepath2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тропа отважных"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("bravepath2"), Show("map")


screen wilderness:

    # Глухомань

    #tag menu
    modal True
    zorder 300

    add "bg wilderness"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Глухомань"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("wilderness"), Show("wilderness2")


screen wilderness2:

    # Глухомань 2

    #tag menu
    modal True
    zorder 300

    add "bg wilderness2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Глухомань"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("wilderness2"), Show("wilderness3")


screen wilderness3:

    # Глухомань 3

    #tag menu
    modal True
    zorder 300

    add "bg wilderness3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Глухомань"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("wilderness3"), Show("map")


screen roadtn:

    # Дорога в никуда

    #tag menu
    modal True
    zorder 300

    add "bg roadtn"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дорога в никуда"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("roadtn"), Show("map")


screen pibuh:

    # Пиратская бухта (гавань)

    #tag menu
    modal True
    zorder 300

    add "bg pibuh"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пиратская гавань"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pibuh"), Show("map")


screen oldmine:

    # Старая шахта

    #tag menu
    modal True
    zorder 300

    add "bg oldmine"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старая шахта"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldmine"), Show("oldmine2")


screen oldmine2:

    # Старая шахта 2

    #tag menu
    modal True
    zorder 300

    add "bg oldmine2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старая шахта"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldmine2"), Show("map")


screen tuni:

    # Тоннель вход

    #tag menu
    modal True
    zorder 300

    add "bg tuni"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тоннель вход"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tuni"), Show("map")


screen tuno:

    # Тоннель выход

    #tag menu
    modal True
    zorder 300

    add "bg tuno"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тоннель выход"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tuno"), Show("map")


screen reeds:

    # Камыши

    #tag menu
    modal True
    zorder 300

    add "bg reeds"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Камыши"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("reeds"), Show("map")


screen iford:

    # Непроходимый Брод

    #tag menu
    modal True
    zorder 300

    add "bg iford"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Непроходимый Брод"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("iford"), Show("map")


screen caroad:

    # Дорога на карьер

    #tag menu
    modal True
    zorder 300

    add "bg caroad"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дорога на карьер"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("caroad"), Show("map")


screen carier:

    # Карьер

    #tag menu
    modal True
    zorder 300

    add "bg carier"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Карьер"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("carier"), Show("map")


screen zdm:

    # Железнодорожный мост

    #tag menu
    modal True
    zorder 300

    add "bg zdm"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Железнодорожный мост"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("zdm"), Show("map")


screen ford:

    # Брод

    #tag menu
    modal True
    zorder 300

    add "bg ford"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Брод"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("ford"), Show("map")


screen ford2:

    # Брод 2

    #tag menu
    modal True
    zorder 300

    add "bg ford2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Брод 2"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("ford2"), Show("map")


screen ford3:

    # Брод 3

    #tag menu
    modal True
    zorder 300

    add "bg ford3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Брод 3"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("ford3"), Show("map")


screen plane:

    # Самолёт

    #tag menu
    modal True
    zorder 300

    add "bg plane"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Самолёт"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("plane"), Show("plane2")


screen plane2:

    # Самолёт 2

    #tag menu
    modal True
    zorder 300

    add "bg plane2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Самолёт"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("plane2"), Show("map")


screen crsh:

    # Рачья отмель

    #tag menu
    modal True
    zorder 300

    add "bg crsh"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Рачья отмель"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("crsh"), Show("map")


screen rapids:

    # Шалаш браконьеров

    #tag menu
    modal True
    zorder 300

    add "bg rapids"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Шалаш браконьеров"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("rapids"), Show("map")


screen hetu:

    # Охотничьи угодья ежа и черепахи

    #tag menu
    modal True
    zorder 300

    add "bg hetu"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Охотничьи угодья ежа и черепахи"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("hetu"), Show("map")


screen jusu:

    # Припасы Юли

    #tag menu
    modal True
    zorder 300

    add "bg jusu"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Припасы Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("jusu"), Show("jusu2")


screen jusu2:

    # Припасы Юли 2

    #tag menu
    modal True
    zorder 300

    add "bg jusu2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Припасы Юли"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("jusu2"), Show("map")


screen pbc:

    # Омут Большой Сом

    #tag menu
    modal True
    zorder 300

    add "bg pbc"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Омут Большой Сом"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pbc"), Show("map")


screen dnest:

    # Гнездо утки

    #tag menu
    modal True
    zorder 300

    add "bg dnest"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Гнездо утки"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dnest"), Show("map")


screen shouse:

    # Дом на болотах

    #tag menu
    modal True
    zorder 300

    add "bg shouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дом на болотах"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("shouse"), Show("map")


screen crystalspring:

    # Кристальный родник

    #tag menu
    modal True
    zorder 300

    add "bg crystalspring"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Кристальный родник"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("crystalspring"), Show("map")


screen mine:

    # Рудник

    #tag menu
    modal True
    zorder 300

    add "bg mine"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Рудник"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("mine"), Show("map")


screen oldclock:

    # Старая часовня

    #tag menu
    modal True
    zorder 300

    add "bg oldclock"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старая часовня"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldclock"), Show("map")


screen oldcem:

    # Старое кладбище

    #tag menu
    modal True
    zorder 300

    add "bg oldcem"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старое кладбище"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcem"), Show("oldcem2")


screen oldcem2:

    # Старое кладбище 2

    #tag menu
    modal True
    zorder 300

    add "bg oldcem2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старое кладбище"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcem2"), Show("oldcem3")


screen oldcem3:

    # Старое кладбище 3

    #tag menu
    modal True
    zorder 300

    add "bg oldcem3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старое кладбище"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("oldcem3"), Show("map")


screen shallow:

    # Отмели

    #tag menu
    modal True
    zorder 300

    add "bg shallow"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Отмели"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("shallow"), Show("map")


screen lyhouse:

    # Дом Рыси

    #tag menu
    modal True
    zorder 300

    add "bg lyhouse"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дом Рыси"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("lyhouse"), Show("map")


screen deroad:

    # Дорога на посёлок

    #tag menu
    modal True
    zorder 300

    add "bg deroad2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дорога на посёлок"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("deroad"), Show("deroad2")


screen deroad2:

    # Дорога на посёлок 2

    #tag menu
    modal True
    zorder 300

    add "bg deroad3"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дорога на посёлок"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("deroad2"), Show("deroad3")


screen deroad3:

    # Дорога на посёлок 3

    #tag menu
    modal True
    zorder 300

    add "bg deroad"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Дорога на посёлок"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("deroad3"), Show("map")


screen wdgorge:

    # Очень глубокое ущелье

    #tag menu
    modal True
    zorder 300

    add "bg wdgorge"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Очень глубокое ущелье"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("wdgorge"), Show("map")


screen dwhir:

    # Смертельный водоворот

    #tag menu
    modal True
    zorder 300

    add "bg dwhir"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Смертельный водоворот"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("dwhir"), Show("map")


screen pot:

    # Тропа на тоннель

    #tag menu
    modal True
    zorder 300

    add "bg pot"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Тропа на тоннель"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pot"), Show("map")


screen pfis:

    # Пляж Дальний остров

    #tag menu
    modal True
    zorder 300

    add "bg pfis"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж Дальний остров"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pfis"), Show("map")


screen ogm:

    # Старый золотой прииск

    #tag menu
    modal True
    zorder 300

    add "bg ogm"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Старый золотой прииск"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("ogm"), Show("map")


screen tbo:

    # Взять лодку

    #tag menu
    modal True
    zorder 300

    add "bg tbo"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Взять лодку"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("tbo"), Show("map")


screen pdl:

    # Пляж Озеро Глубокое

    #tag menu
    modal True
    zorder 300

    add "bg pdl"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж Озеро Глубокое"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pdl"), Show("map")


screen spa:

    # Узкоколейка

    #tag menu
    modal True
    zorder 300

    add "bg spa"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Узкоколейка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("spa"), Show("spa2")

screen spa2:

    # Узкоколейка 2

    #tag menu
    modal True
    zorder 300

    add "bg spa2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Узкоколейка"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("spa2"), Show("map")


screen rail:

    # Железная дорога

    #tag menu
    modal True
    zorder 300

    add "bg rail"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Железная дорога"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("rail"), Show("map")


screen pointers:

    # Указатели

    #tag menu
    modal True
    zorder 300

    add "bg pointers"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Указатели"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("pointers"), Show("map")


screen busstop:

    # Остановка автобуса 410

    #tag menu
    modal True
    zorder 300

    add "bg busstop2"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Остановка автобуса 410"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("busstop"), Show("map")



screen aulane:

    # Поляна Алисы и Ульяны

    #tag menu
    modal True
    zorder 300

    add "bg aulane"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Поляна Алисы и Ульяны"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("aulane"), Show("map")



screen misemhidenbeach:

    # Пляж Мику и Семёна

    #tag menu
    modal True
    zorder 300

    add "bg mi_sem_hiden_beach"

    frame:
        xpadding 30
        ypadding 10
        pos (50, 50)

        style_prefix "LocationStyleTitle"
        vbox:
            style_prefix "LocationStyleTitle"
            vbox:
                style_prefix "LocationStyleTitle"
                text "Пляж Мику и Семёна"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("misemhidenbeach"), Show("map")





label nbeach:
    scene bg nbeach with dissolve
    "Пляж ближний"
    scene bg nbeach2 with dissolve
    "Пляж ближний2"
    scene bg nbeach3 with dissolve
    "Пляж ближний3"
    scene bg nbeach4 with dissolve
    "Пляж ближний4"
    call screen map
    return
    
label gog:
    scene bg gog with dissolve
    "Поляна слётов"
    call screen map
    return
    
label smg:
    scene bg smg with dissolve
    "Малая поляна"
    call screen map
    return
    
label disland:
    scene bg disland with dissolve
    "Остров Дальний"
    scene bg disland2 with dissolve
    "Остров Дальний2"
    call screen map
    return 
    
label lakedeep:
    scene bg lakedeep with dissolve
    "Озеро Глубокое"
    scene bg lakedeep2 with dissolve
    "Озеро Глубокое2"
    call screen map
    return  
    
label uhouse:
    scene bg uhouse with dissolve
    "Дом Юли"
    scene bg uhouse2 with dissolve
    "Дом Юли2"
    scene bg uhouse3 with dissolve
    "Комната Юли"
    scene bg uhouse4 with dissolve
    "Камин Юли2"
    scene bg uhouse5 with dissolve
    "Кровать Юли"
    scene bg uhouse6 with dissolve
    "Ванна Юли"
    call screen map
    return
    
label newtcreek:
    scene bg newtcreek with dissolve
    "Ручей тритонов"
    call screen map
    return
    
label thiefpath:
    scene bg thiefpath with dissolve
    "Тропа украденной котлеты"
    call screen map
    return
    
label swamp:
    scene bg swamp with dissolve
    "Болота"
    call screen map
    return
    
label boat_station:
    scene bg boat_station with dissolve
    "Лодочная станция"
    call screen map
    return

label fbeach:
    scene bg fbeach with dissolve
    "Пляж дальний"
    call screen map
    return
    
label mcity:
    scene bg mcity with dissolve
    "Посёлок Рудный"
    scene bg mcity2 with dissolve
    "Посёлок Рудный2"
    call screen map
    return
    
label dpeak:
    scene bg dpeak with dissolve
    "Пик Двачевской"
    call screen map
    return
    
label ushallow:
    scene bg ushallow with dissolve
    "Ульянина мель"
    call screen map
    return
    
label shpi:
    scene bg shpi with dissolve
    "Шалаш пионера"
    call screen map
    return
    
label cave:
    scene bg cave with dissolve
    "Пещера"
    call screen map
    return
    
label moсr:
    scene bg moсr with dissolve
    "Горный ручей"
    call screen map
    return
    
label opine:
    scene bg opine with dissolve
    #show sova_anim
    show tips_owl_anim
    "Сосна совы"
    call screen map
    return
    
label laboratory:
    show bg laboratory with dissolve
    "Лаборатория"
    call screen map
    return
    
label oldroad:
    show bg oldroad with dissolve
    "Старая дорога"
    call screen map
    return
    
label tcc:
    show bg tcc with dissolve
    "Тропа безбашенных альпинистов"
    call screen map
    return
    
label goldd:
    show bg goldd with dissolve
    "Землянка золотоискателя"
    call screen map
    return
    
label oldcamp:
    show bg oldcamp with dissolve
    "Старый лагерь"
    show bg oldcamp2 with dissolve
    "Старый лагерь2"
    show bg oldcamp3 with dissolve
    "Старый лагерь3"
    call screen map
    return
    
label bravepath:
    show bg bravepath with dissolve
    "Тропа отважных"
    show bg bravepath2 with dissolve
    "Тропа отважных2"
    call screen map
    return
    
label wilderness:
    show bg wilderness with dissolve
    "Глухомань"
    show bg wilderness2 with dissolve
    "Глухомань2"
    show bg wilderness3 with dissolve
    "Глухомань3"
    call screen map
    return
    
label roadtn:
    show bg roadtn with dissolve
    "Дорога в никуда"
    call screen map
    return
    
label pibuh:
    scene bg pibuh with dissolve
    "Пиратская бухта"
    call screen map
    return
    
label oldmine:
    show bg oldmine with dissolve
    "Старая шахта"
    show bg oldmine2 with dissolve
    "Старая шахта2"
    call screen map
    return
    
label tuni:
    scene bg tuni with dissolve
    "Тоннель вход"
    call screen map
    return
    
label tuno:
    scene bg tuno with dissolve
    "Тоннель выход"
    call screen map
    return
    
label reeds:
    show bg reeds with dissolve
    "Камыши"
    call screen map
    return

label iford:
    scene bg iford with dissolve
    "Непроходимый Брод"
    call screen map
    return

label caroad:
    scene bg caroad with dissolve
    "Дорога на карьер"
    call screen map
    return

label carier:
    scene bg carier with dissolve
    "Карьер"
    call screen map
    return

label zdm:
    scene bg zdm with dissolve
    "Железнодорожный мост"
    call screen map
    return     
    
label ford:
    scene bg ford with dissolve
    "Брод"
    call screen map
    return
    
label ford2:
    scene bg ford2 with dissolve
    "Брод2"
    call screen map
    return
    
label ford3:
    scene bg ford3 with dissolve
    "Брод3"
    call screen map
    return
    
label plane:
    scene bg plane with dissolve
    "Самолёт"
    scene bg plane2 with dissolve
    "Самолёт2"
    call screen map
    return 
    
label crsh:
    scene bg crsh with dissolve
    "Рачья отмель"
    call screen map
    return

label rapids:
    scene bg rapids with dissolve
    "Шалаш браконьеров"
    call screen map
    return

label hetu:
    scene bg hetu with dissolve
    "Охотничьи угодья ежа и черепахи"
    call screen map
    return

label jusu:
    scene bg jusu with dissolve
    "Припасы Юли"
    scene bg jusu2 with dissolve
    "Припасы Юли 2"
    call screen map
    return

label pbc:
    scene bg pbc with dissolve
    "Омут Большой Сом"
    call screen map
    return

label dnest:
    scene bg dnest with dissolve
    "Гнездо утки"
    call screen map
    return      
    
label shouse:
    scene bg shouse with dissolve
    "Дом на болотах"
    call screen map
    return

label crystalspring:
    scene bg crystalspring with dissolve
    "Кристальный родник"
    call screen map
    return    
    
label mine:
    scene bg mine with dissolve
    "Рудник"
    call screen map
    return
    
label oldclock:
    scene bg oldclock with dissolve
    "Старая часовня"
    call screen map
    return
    
label oldcem:
    scene bg oldcem with dissolve
    "Старое кладбище"
    scene bg oldcem2 with dissolve
    "Старое кладбище2"
    scene bg oldcem3 with dissolve
    "Старое кладбище3"
    call screen map
    return
    
label shallow:
    scene bg shallow with dissolve
    "Отмели"
    call screen map
    return
    
label camp:
    show screen campmap
    "Лагерь"
    call screen map
    return
    
label lyhouse:
    scene bg lyhouse with dissolve
    "Дом Рыси"
    call screen map
    return
    
label deroad:
    scene bg deroad2 with dissolve
    "Дорога на посёлок"
    scene bg deroad3 with dissolve
    "Дорога на посёлок2"
    scene bg deroad with dissolve
    "Дорога на посёлок3"
    call screen map
    return
    
label wdgorge:
    scene bg wdgorge with dissolve
    "Очень глубокое ущелье"
    call screen map
    return
    
label dwhir:
    scene bg dwhir with dissolve
    "Смертельный водоворот"
    call screen map
    return
    
label pot:
    scene bg pot with dissolve
    "Тропа на тоннель"
    call screen map
    return
    
label pfis:
    scene bg pfis with dissolve
    "Пляж Дальний остров"
    call screen map
    return
    
label ogm:
    scene bg ogm with dissolve
    "Старый золотой прииск"
    call screen map
    return
    
label tbo:
    scene bg tbo with dissolve
    "Взять лодку"
    call screen map
    return
    
label pdl:
    scene bg pdl with dissolve
    "Пляж Озеро Глубокое"
    call screen map
    return
    
label spa:
    scene bg spa with dissolve
    "Узкоколейка"
    scene bg spa2 with dissolve
    "Узкоколейка2"
    call screen map
    return
    
label rail:
    scene bg rail with dissolve
    "Железная дорога"
    call screen map
    return

label aulane:
    scene bg rail with dissolve
    "Поляна Алисы и Ульяны"
    call screen map
    return






