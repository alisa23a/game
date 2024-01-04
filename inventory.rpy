#####################################################
##В этом файле описывается инвентарь

style InvItemStyleTitle_text:
    color "#fff"
    font "fonts/mateur-webfont.ttf"
    size 50
    
style InvItemStyleText_text:
    color "#fff"
    #font "fonts/mateur-webfont.ttf"
    size 30

style InvItemPrevCaption_frame:
    background None

style InvItemPrevCaption_text:
    color "#fff"
    size 20

style InvItemPrevCaption_vbox:
    xalign (0.5) yalign (0.07)

style keysStyle_text:
    color "#fff"
    font "fonts/mateur-webfont.ttf"
    size 30


screen inventory_slots():

    ##Экран инвентаря со слотами. Для каждого предмета инвентаря зарезервирован собственный слот. При открытии этот экран проверяет значение булевой переменной для предмета, и если значение true, отображает предмет, иначе отображает пустой слот.

    tag menu
    zorder 100
    modal True
    
    add "images/inventory/inv_slots.webp"
    
    style_prefix "InvItemPrevCaption"
    
    # vbox:
        # style_prefix "btns"
            # textbutton "Жемчужина" action Hide ("inventory_slots"), Show("inv_item_pearl")
    
    ## Превьюшка Жемчужина

    if inv_item_01:
        button:
            xpos 92 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_perl.png"
            hover_background "images/inventory/item_prev/prev_with_slot_perl.png"
            style_prefix "InvItemPrevCaption"
            text "Жемчужина" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_pearl")

    ## Превьюшка Записная книжка

    if inv_item_02:
        button:
            xpos 342 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_notebook.png"
            hover_background "images/inventory/item_prev/prev_with_slot_notebook.png"
            style_prefix "InvItemPrevCaption"
            text "Записная книжка" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_notebook")

    ## Превьюшка Карта и компас

    if inv_item_03:
        button:
            xpos 592 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_mapcompass.png"
            hover_background "images/inventory/item_prev/prev_with_slot_mapcompass.png"
            style_prefix "InvItemPrevCaption"
            text "Карта и компас" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_mapcompass")

    ## Превьюшка Связка ключей

    if inv_item_04:
        button:
            xpos 842 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_keys.png"
            hover_background "images/inventory/item_prev/prev_with_slot_keys.png"
            style_prefix "InvItemPrevCaption"
            text "Связка ключей" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("keys_slots")

    ## Превьюшка Конфетки

    if inv_item_05:
        button:
            xpos 1092 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_sweets.png"
            hover_background "images/inventory/item_prev/prev_with_slot_sweets.png"
            style_prefix "InvItemPrevCaption"
            text "Конфетки" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_sweets")

    ## Превьюшка Котлетки

    if inv_item_06:
        button:
            xpos 1342 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_cutlets.png"
            hover_background "images/inventory/item_prev/prev_with_slot_cutlets.png"
            style_prefix "InvItemPrevCaption"
            text "Котлетки" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_cutlets")

    ## Превьюшка Сахарные грибы

    if inv_item_07:
        button:
            xpos 1592 ypos 52
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_shugar_mushrooms.png"
            hover_background "images/inventory/item_prev/prev_with_slot_shugar_mushrooms.png"
            style_prefix "InvItemPrevCaption"
            text "Сахарные грибы" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_shugar_mushrooms")

    ## Превьюшка Кокарда горного инженера
    
    if inv_item_08:
        button:
            xpos 92 ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_badge.png"
            hover_background "images/inventory/item_prev/prev_with_slot_badge.png"

            vbox:
                style_prefix "InvItemPrevCaption"
                text "Кокарда горного" xalign (0.5) yalign (0.07)
                text "Инженера" xalign (0.5) yalign (0.17)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_badge")

    ## Превьюшка Моток веревки

    if inv_item_09:
        button:
            xpos 342  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_rope.png"
            hover_background "images/inventory/item_prev/prev_with_slot_rope.png"
            style_prefix "InvItemPrevCaption"
            text "Моток веревки" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_rope")

    ## Превьюшка Кристалл

    if inv_item_10:
        button:
            xpos 592  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_crystal.png"
            hover_background "images/inventory/item_prev/prev_with_slot_crystal.png"
            style_prefix "InvItemPrevCaption"
            text "Кристалл" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_crystal")

    ## Превьюшка Перочинный ножик

    if inv_item_11:
        button:
            xpos 842  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_knife.png"
            hover_background "images/inventory/item_prev/prev_with_slot_knife.png"
            style_prefix "InvItemPrevCaption"
            text "Перочинный ножик" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_knife")

    ## Превьюшка Фотоаппарат

    if inv_item_12:
        button:
            xpos 1092  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_camera.png"
            hover_background "images/inventory/item_prev/prev_with_slot_camera.png"
            style_prefix "InvItemPrevCaption"
            text "Фотоаппарат" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_camera")

    ## Превьюшка Фонарик

    if inv_item_13:
        button:
            xpos 1342  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_flashlight.png"
            hover_background "images/inventory/item_prev/prev_with_slot_flashlight.png"
            style_prefix "InvItemPrevCaption"
            text "Фонарик" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_flashlight")

    ## Превьюшка Ягоды забвения

    if inv_item_14:
        button:
            xpos 1592  ypos 365
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_berries.png"
            hover_background "images/inventory/item_prev/prev_with_slot_berries.png"
            style_prefix "InvItemPrevCaption"
            text "Ягоды забвения" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_berries")

    ## Превьюшка Древние бусики

    if inv_item_15:
        button:
            xpos 92 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_beads.png"
            hover_background "images/inventory/item_prev/prev_with_slot_beads.png"
            style_prefix "InvItemPrevCaption"
            text "Древние бусики" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_beads")

    ## Превьюшка Слиток золота

    if inv_item_16:
        button:
            xpos 342 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_gold.png"
            hover_background "images/inventory/item_prev/prev_with_slot_gold.png"
            style_prefix "InvItemPrevCaption"
            text "Слиток золота" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_gold")

    ## Превьюшка Баночка для шуршавчиков
    
    if inv_item_17:
        button:
            xpos 592 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_jar.png"
            hover_background "images/inventory/item_prev/prev_with_slot_jar.png"

            vbox:
                style_prefix "InvItemPrevCaption"
                text "Баночка для" xalign (0.5) yalign (0.07)
                text "шуршавчиков" xalign (0.5) yalign (0.17)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_jar")

    ## Превьюшка Бинокль

    if inv_item_18:
        button:
            xpos 842 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_binoculars.png"
            hover_background "images/inventory/item_prev/prev_with_slot_binoculars.png"
            style_prefix "InvItemPrevCaption"
            text "Бинокль" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_binoculars")

    ## Превьюшка Бинтик

    if inv_item_19:
        button:
            xpos 1092 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_bandage.png"
            hover_background "images/inventory/item_prev/prev_with_slot_bandage.png"
            style_prefix "InvItemPrevCaption"
            text "Бинтик" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_bandage")

    ## Превьюшка Йод

    if inv_item_20:
        button:
            xpos 1342 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_iodine.png"
            hover_background "images/inventory/item_prev/prev_with_slot_iodine.png"
            style_prefix "InvItemPrevCaption"
            text "Йод" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("inv_item_iodine")

    ## Превьюшка Записки

    if inv_item_21:
        button:
            xpos 1592 ypos 679
            xsize 234 ysize 288
            idle_background "images/inventory/item_prev/prev_with_slot_notes.png"
            hover_background "images/inventory/item_prev/prev_with_slot_notes.png"
            style_prefix "InvItemPrevCaption"
            text "Записки" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("inventory_slots"), Show("notes_slots")

    ## Кнопка закрытия инвентаря

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("inventory_slots"), Show("info_stand")



#######################################################
## Экраны предметов

screen inv_item_pearl():

    ## Жемчужина

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_pearl_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Жемчужина"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это самая прекрасная жемчужина, \nкоторую Атсуи подняла со дна \nОмута Большого Сома. \nОчень она мне нравится. \nДумаю, что можно на нее выменять. \nХотя, наверное, оставлю себе."
                
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_pearl"), Show("inventory_slots")

screen inv_item_notebook():

    ## Записная книжка

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_notebook_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Записная книжка"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это моя записная книжка \n«ДЛЯ РАЗНЫХ МЫСЛЕЙ». \nВ ней мои размышления... \nЕсть даже запретные... \nОчень секретные. \nТе, что нельзя писать в дневник."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_notebook"), Show("inventory_slots")

screen inv_item_mapcompass():

    ## Карта и компас

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_mapcompass_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Карта и компас"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это моя карта, срисованная \nс настоящей военной карты. \nТоже очень секретная. \nА без нее и компаса, мне нельзя. \nИначе, какой же я следопыт-разведчик?"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_mapcompass"), Show("inventory_slots")

screen inv_item_keys():

    ## Связка ключей

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_keys_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Связка ключей"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Ключи от всяких хитрых чуланчиков. \nОчень важные ключи. \nС их помощью, надеюсь, \nмы проникнем во все тайны. \n(Пока не подошли ни к одной двери)."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_keys"), Show("inventory_slots")

screen inv_item_sweets():

    ## Конфетки

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_sweets_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Конфетки"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Настоящие, шоколадные с начинкой. \nОчень вкусные, мои любимые. \nБез них вообще никак..."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_sweets"), Show("inventory_slots")

screen inv_item_cutlets():

    ## Котлетки

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_cutlets_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Котлетки"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Котлетки столовские. \nЛучшее произведение кулинарного \nгения Любовь Никаноровны. \nПросто объедение."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_cutlets"), Show("inventory_slots")

screen inv_item_shugar_mushrooms():

    ## Сахарные грибы

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_shugar_mushrooms_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Сахарные грибы"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Волшебные грибы, выращенные Юлей, \nпри помощи сахара и каких то \nзаклинаний.. \nНу как бы, они конечно съедобные. \nНо последствия после них пока еще \nне изучены. \nПоэтому они для «крайнего случая»."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_shugar_mushrooms"), Show("inventory_slots")

screen inv_item_badge():

    ## Кокарда горного инженера

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_badge_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Кокарда горного \nинженера"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это очень загадочна вещь. \nНайдена в желудке у Большого Сома. \nЕсть предположение, \nчто это кокарда от фуражки \nгорного инженера, работавшего на прииске \nеще при царе-батюшке. \nВ общем, сомик его схрумкал. \nНо это не точно."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_badge"), Show("inventory_slots")


screen inv_item_rope():

    ## Моток веревки

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_rope_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Моток веревки"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Вот без него вообще никуда. \nОчень нужная веревочка."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_rope"), Show("inventory_slots")

screen inv_item_crystal():

    ## Кристалл

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_crystal_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Кристалл"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Волшебный кристалл. \nАктивизируется каждый раз \nкогда памятник Генды поворачивается \nлицом к библиотеке. \nВ это время лучше ни о чем не думать. \nИначе исполнится."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_crystal"), Show("inventory_slots")

screen inv_item_knife():

    ## Перочинный ножик

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_knife_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Перочинный ножик"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Ну... ножик как ножик. Полезная вещь. \nВообще-то, когда папа давал его мне, \nсказал, что он «боцманский». \nНо у нас пока нет ни корабля, \nни команды, ни боцмана. \nТак что, я им просто играю в «ножички»."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_knife"), Show("inventory_slots")

screen inv_item_camera():

    ## Фотоаппарат

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_camera_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Фотоаппарат"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это вещь! Настоящий фотоаппарат. \nМы с Алисой выманили его у Слави \n(она наш штатный фотограф в лагере). \nНадеемся, с его помощью, войти в историю."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_camera"), Show("inventory_slots")

screen inv_item_flashlight():

    ## Фонарик

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_flashlight_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Фонарик"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Хороший фонарик. \nНи разу не ломался... \nТолько батарейки быстро кончаются."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_flashlight"), Show("inventory_slots")

screen inv_item_berries():

    ## Ягоды забвения

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_berries_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Ягоды забвения"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это особенные ягоды. \nРастут только в одном месте \n(где - не скажу). \nЗакинулся ягодкой и все забыл. \nНу в смысле плохое. \nНе даром они «ягоды забвения». \n(Пока не пробовала)."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_berries"), Show("inventory_slots")

screen inv_item_beads():

    ## Древние бусики

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_beads_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Древние бусики"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Эти бусики очень древние... \nНа них какой-то рисунок... \nНо расшифровать я не смогла. \nМожет быть, они даже волшебные. \nНайдены мой и Алисой «в одном месте». \nГде-где... Где были, там уже нет."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_beads"), Show("inventory_slots")

screen inv_item_gold():

    ## Слиток золота

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_gold_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Слиток золота"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Ну слиток как слиток, \nчто на него смотреть. \nДавай обратно. \nПусть полежит у меня."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_gold"), Show("inventory_slots")

screen inv_item_jar():

    ## Баночка для шуршавчиков

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_jar_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Баночка для \nшурчавчиков"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Сюда я собираю всех, кого поймала."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_jar"), Show("inventory_slots")

screen inv_item_binoculars():

    ## Бинокль

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_binoculars_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Бинокль"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Эта штука очень помогает \nмне все подмечать. \nА вы думали почему \nя все про всех знаю!"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_binoculars"), Show("inventory_slots")

screen inv_item_bandage():

    ## Бинтик

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_bandage_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Бинтик"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это бинтик. Понадобился только раз, \nкогда я убегала от страшной кошки \nв развалинах. Сильно оцарапалась. \nНо кто знает, что еще может случиться. \nПусть себе лежит."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_bandage"), Show("inventory_slots")

screen inv_item_iodine():

    ## Йод

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_iodine_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Йод"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это йод. Я его не люблю. Пачкучий и жжет. \nНо мама настояла что бы он был. \nГоворят, если его капнуть на сахар \nи съесть, то можно поднять температуру. \nНадо попробовать."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_iodine"), Show("inventory_slots")


screen notes_slots():

    ##Экран зписок со слотами. При клике на превьюшку записки открывается экран с полноразмерной картинкой записки и описанием.

    tag menu
    zorder 100
    modal True
    
    add "images/inventory/notes_slots.webp"
    
    style_prefix "InvItemPrevCaption"
    
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("notes_slots"), Show("inventory_slots")
    
    ## Превьюшка Первая записка

    if inv_item_22:
        button:
            xpos 353 ypos 271
            xsize 387 ysize 476
            idle_background "images/inventory/item_prev/prev_single_note.png"
            hover_background "images/inventory/item_prev/prev_single_note.png"
            style_prefix "InvItemPrevCaption"
            text "Первая записка" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("notes_slots"), Show("inv_item_note_one")

    ## Превьюшка Вторая записка

    if inv_item_23:
        button:
            xpos 766 ypos 271
            xsize 387 ysize 476
            idle_background "images/inventory/item_prev/prev_single_note.png"
            hover_background "images/inventory/item_prev/prev_single_note.png"
            style_prefix "InvItemPrevCaption"
            text "Вторая записка" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("notes_slots"), Show("inv_item_note_two")

    ## Превьюшка Третья записка

    if inv_item_24:
        button:
            xpos 1179 ypos 271
            xsize 387 ysize 476
            idle_background "images/inventory/item_prev/prev_single_note.png"
            hover_background "images/inventory/item_prev/prev_single_note.png"
            style_prefix "InvItemPrevCaption"
            text "Третья записка" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("notes_slots"), Show("inv_item_note_three")

screen inv_item_note_one():

    ## Первая записка

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_note_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Первая записка"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Это записка от... \nНе скажу от кого. \nЧто в ней? \nМного будешь знать, скоро состаришься."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_note_one"), Show("notes_slots")

screen inv_item_note_two():

    ## Вторая записка

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_note_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Вторая записка"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "(Читай, что написала про первую)."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_note_two"), Show("notes_slots")

screen inv_item_note_three():

    ## Третья записка

    tag menu
    zorder 100
    modal True

    add "images/inventory/item_full/inv_item_full_bg.png"
    add "images/inventory/item_full/inv_item_note_full.png" pos (1112, 255)
        
    frame:
        xpadding 10
        ypadding 10
        pos (300, 300)
        background None


        vbox:
            vbox:
                style_prefix "InvItemStyleTitle"
                text "Третья записка"

            style_prefix "InvItemStyleText"   
            vbox:
                null height 50
                style_prefix "InvItemStyleText"
                text "Очень личная. Ну ты понял. Завидуй молча."

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("inv_item_note_three"), Show("notes_slots")



screen keys_slots():

    ##Экран ключей со слотами. При клике на превьюшку ключа открывается экран с полноразмерной картинкой ключа и описанием.

    tag menu
    zorder 100
    modal True
    
    add "images/inventory/keys_slots.webp"
    
    style_prefix "InvItemPrevCaption"

    frame:
        xpadding 10
        ypadding 10
        pos (350, 60)
        background None


        vbox:
            vbox:
                style_prefix "keysStyle"
                text "Я нашла эту связку ключей в лагере. На ней было три ключа. \nЯ буду цеплять сюда все ключи, которые найду."

    
    
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("keys_slots"), Show("inventory_slots")
    
    ## Превьюшка Ключ от Коптёрки физрука

    if inv_item_25:
        button:
            xpos 356 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Коптёрка физрука" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")

    ## Превьюшка Ключ от Лодочной станции

    if inv_item_26:
        button:
            xpos 662 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Лодочная станция" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")

    ## Превьюшка Ключ от Продуктового склада

    if inv_item_27:
        button:
            xpos 968 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Продуктовый склад" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Ключ от Чердака Алисы и Ульяны

    if inv_item_28:
        button:
            xpos 1274 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Наш чердак" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Ключ от Супернычки (чердак домика ОД)

    if inv_item_29:
        button:
            xpos 356 ypos 613
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Супернычка" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Ключ от Бомбоубежища

    if inv_item_30:
        button:
            xpos 662 ypos 613
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Бомбоубежище" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Ключ от Спецхрана библиотеки

    if inv_item_31:
        button:
            xpos 968 ypos 613
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Спецхран библиотеки" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Ключ от Лаборатории

    if inv_item_32:
        button:
            xpos 1274 ypos 613
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Лаборатория" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Неизвестный ключ 1

    if inv_item_33:
        button:
            xpos 356 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Неизвестно от чего" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Неизвестный ключ 2

    if inv_item_34:
        button:
            xpos 662 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Неизвестно от чего" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")


    ## Превьюшка Неизвестный ключ 3

    if inv_item_35:
        button:
            xpos 968 ypos 230
            xsize 287 ysize 353
            idle_background "images/inventory/item_prev/prev_single_key.png"
            hover_background "images/inventory/item_prev/prev_single_key.png"
            style_prefix "InvItemPrevCaption"
            text "Неизвестно от чего" xalign (0.5) yalign (0.07)
            #focus_mask True
            action Hide ("keys_slots"), Show("inventory_slots")