#####################################################################
##Экраны информационного стенда

screen stand_camp_rules():

    ## Экран с правилами лагеря, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_camp_rules_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_camp_rules"), Show("info_stand")

screen stand_honor_board():

    ## Экран с доской почёта, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_honor_board_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_honor_board"), Show("info_stand")




define adv_1 = False
define adv_3 = False
define adv_5 = False
define adv_7 = False
define adv_10 = False
define adv_12 = False
define adv_15 = False


style stand_adds_text:
    color "#222222"
    font "fonts/B52.ttf"
    size 40

style stand_adds_header_text:
    color "#222222"
    font "fonts/B52.ttf"
    size 50


screen stand_advertisements():

    zorder 100
    modal True

    add "images/info_stand/stand_advertisments_gr.webp"


    frame:
        background "#ddf"
        align (0.5, 0.5)
        xysize (1000, 800)
        xpadding 80
        ypadding 80


        vbox:
            xalign 0.5
            vbox:
                xalign 0.5

                style_prefix "stand_adds_header"

                text "ВНИМАНИЕ!" xalign (0.5)

            if adv_1:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "Вожатым всех отрядов собраться в помещении музкуржка на летучку."

                    null height 20

                    text "Повестка – обсуждение планов торжественного открытия сезона отдыха в ОПЛ «Совенок»."

                    null height 20

                    text "Явка строго обязательна. Время сбора 14-00."

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_3:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "Меню столовой будет пересмотрено."

                    null height 20

                    text "Всем вожатым сдать уточнённые списки пионеров нуждающихся в дополнительном питании (особенно касается малышей)."

                    null height 20

                    text "Списки подавать завхозу М. Кейтель. Время подачи списков сегодня до 19-00."

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_5:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "Составляется график очередности походов отрядов."

                    null height 20

                    text "Для согласования всем вожатым необходимо подойти к физруку не позже 14-00."

                    null height 20

                    text "Также подать списки детей, которым не разрешены физические нагрузки по показаниям врача лагеря."

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_7:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "Сегодня с 10-00 объявляется СУББОТНИК."

                    null height 20

                    text "Генеральная уборка помещений и территорий лагеря в связи с приездом делегации и посещением нашего лагеря представителем организации скаутов США."

                    null height 20

                    text "Вся информация по мероприятию будет у старост групп и вожатых."

                    null height 20

                    text "Явка на субботник строго обязательна!"

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_10:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "В связи с плохой погодой пляжные  мероприятия сегодня отменяются!"

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_12:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "В связи с карантином танцевальные вечера временно отменяются, до особого распоряжения администрации!"

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."


            if adv_15:

                vbox:
                    xalign 0.5

                    null height 70

                    style_prefix "stand_adds"

                    text "Вожатым согласовать графики выездов своих отрядов в краевой центр."

                    null height 20

                    text "Музей, кинотеатр, экскурсии в совхоз."

                    null height 20

                    text "Заранее подать списки желающих."

                    null height 20

                    text "Директор ОПЛ «Совенок» МП Умнова."



    # frame:
        # xpadding 10
        # ypadding 10
        # pos (300, 300)
        # background None
        # xsize 300

        # if adv_0:

            # vbox:

                # style_prefix "stand_adds"
                # text "Эмблема горного" xalign (0.5) yalign (0.07):
                    # size 24



            # text "Тут будут объявления":
                # xalign 0.5




    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide("stand_advertisements"), Show("info_stand")








screen stand_mailbox():

    ## Экран с почтовым ящиком, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_mailbox_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_mailbox"), Show("info_stand")

screen stand_hikes():

    ## Экран с походами, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_hikes_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_hikes"), Show("info_stand")

screen stand_history():

    ## Экран с историей, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_history_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_history"), Show("info_stand")

screen stand_main_map():

    ## Экран с главной картой, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_main_map_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_main_map"), Show("info_stand")


define newspaper_0 = True
define newspaper_1 = False
define newspaper_2 = False
define newspaper_3 = False

screen stand_wall_newspaper():

    ## Экран со стенгазетой, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    if newspaper_0:

        add "images/info_stand/stand_wall_newspaper_0.webp"

    if newspaper_1:

        add "images/info_stand/stand_wall_newspaper_1.webp"

    if newspaper_2:

        add "images/info_stand/stand_wall_newspaper_2.webp"

    if newspaper_3:

        add "images/info_stand/stand_wall_newspaper_3.webp"

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide("stand_wall_newspaper"), Show("info_stand")


screen stand_camp_map():

    ## Экран с картой лагеря, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_camp_map_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_camp_map"), Show("info_stand")

# screen stand_gallery():

    # ## Экран с галереей, открывается при клике в главном меню соответствующей таблички на стенде
    # #tag menu
    # zorder 100
    # modal True

    # imagemap:
        # ground "images/info_stand/stand_gallery_gr.webp"
        # idle "gui/info_stand_nav_idle.png"
        # hover "gui/info_stand_nav_hover.png" 

        # hotspot(1845,0,75,77) action Hide("stand_gallery"), Show("info_stand")


###################################
## Сова, дающая подсказки

image tips_owl_blink_anim:

    ##Анимация моргания совы

    pos (1462, 375)

    "images/tips_owl/tips_owl_blink_01.png"
    choice:
        pause 1.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    "images/tips_owl/tips_owl_blink_02.png"
    pause 0.2

    repeat

screen stand_tips_list():

    ## Экран со списком вопросов сове, открывается при клике на "Выбери вопрос" на экране stand_tips_owl
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips_list_gr.webp"
        idle "images/tips_owl/tips_list_idle.png" 
        hover "images/tips_owl/tips_list_hover.png" 

        hotspot(1845, 0, 75, 77) action Hide("stand_tips_list"), Hide("stand_tips_owl"), Show("info_stand")
        hotspot(134, 80, 437, 32) action Show("tips_owl_tip_01")
        hotspot(134, 112, 561, 32) action Show("tips_owl_tip_02")
        hotspot(134, 144, 550, 32) action Show("tips_owl_tip_03")
        hotspot(134, 176, 670, 32) action Show("tips_owl_tip_04")
        hotspot(134, 208, 674, 32) action Show("tips_owl_tip_05")
        hotspot(134, 240, 335, 32) action Show("tips_owl_tip_06")
        hotspot(134, 272, 236, 32) action Show("tips_owl_tip_07")
        hotspot(134, 304, 342, 32) action Show("tips_owl_tip_08")
        hotspot(134, 336, 310, 32) action Show("tips_owl_tip_09")
        hotspot(134, 368, 442, 32) action Show("tips_owl_tip_10")
        hotspot(134, 400, 377, 32) action Show("tips_owl_tip_11")
        hotspot(134, 432, 447, 32) action Show("tips_owl_tip_12")
        hotspot(134, 464, 395, 32) action Show("tips_owl_tip_13")
        hotspot(134, 496, 291, 32) action Show("tips_owl_tip_14")
        hotspot(134, 528, 753, 32) action Show("tips_owl_tip_15")
        hotspot(134, 560, 362, 32) action Show("tips_owl_tip_16")
        hotspot(134, 592, 275, 32) action Show("tips_owl_tip_17")
        hotspot(134, 624, 275, 32) action Show("tips_owl_tip_18")
        hotspot(134, 656, 299, 32) action Show("tips_owl_tip_19")
        hotspot(134, 688, 524, 32) action Show("tips_owl_tip_20")
        hotspot(134, 720, 462, 32) action Show("tips_owl_tip_21")
        hotspot(134, 752, 500, 32) action Show("tips_owl_tip_22")
        hotspot(134, 784, 250, 32) action Show("tips_owl_tip_23")
        hotspot(134, 816, 329, 32) action Show("tips_owl_tip_24")
        hotspot(134, 848, 244, 32) action Show("tips_owl_tip_25")
        hotspot(134, 880, 581, 32) action Show("tips_owl_tip_26")
        hotspot(134, 912, 475, 32) action Show("tips_owl_tip_27")
        hotspot(134, 944, 524, 32) action Show("tips_owl_tip_28")
        hotspot(134, 976, 510, 32) action Show("tips_owl_tip_29")

    add "tips_owl_blink_anim"


image tips_owl_anim:

    #Анимация совы

    pos (726, 93)

    "images/tips_owl/tips_owl_01.png"
    pause 0.2
    "images/tips_owl/tips_owl_02.png"
    pause 0.2
    "images/tips_owl/tips_owl_03.png"
    pause 0.2
    "images/tips_owl/tips_owl_04.png"
    pause 0.2
    "images/tips_owl/tips_owl_05.png"
    pause 0.2
    repeat

screen stand_tips_owl():

    ## Экран с совой, дающей подсказки, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips_owl_gr.webp"
        idle "images/tips_owl/tips_owl_idle.png"
        hover "images/tips_owl/tips_owl_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_tips_owl"), Show("info_stand")
        hotspot(1083, 167, 217, 238) action Show("stand_tips_list")

    add "tips_owl_anim"

################################
##Экраны ответов, даваемых совой

screen tips_owl_tip_01():

    ## Экран с подсказкой 01
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_01.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_01"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_02():

    ## Экран с подсказкой 02
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_02.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_02"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_03():

    ## Экран с подсказкой 03
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_03.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_03"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_04():

    ## Экран с подсказкой 04
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_04.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_04"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_05():

    ## Экран с подсказкой 05
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_05.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_05"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_06():

    ## Экран с подсказкой 06
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_06.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_06"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_07():

    ## Экран с подсказкой 07
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_07.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_07"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_08():

    ## Экран с подсказкой 08
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_08.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_08"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_09():

    ## Экран с подсказкой 09
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_09.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_09"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_10():

    ## Экран с подсказкой 10
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_10.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_10"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_11():

    ## Экран с подсказкой 11
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_11.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_11"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_12():

    ## Экран с подсказкой 12
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_12.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_12"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_13():

    ## Экран с подсказкой 13
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_13.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_13"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_14():

    ## Экран с подсказкой 14
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_14.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_14"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_15():

    ## Экран с подсказкой 15
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_15.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_15"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_16():

    ## Экран с подсказкой 16
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_16.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_16"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_17():

    ## Экран с подсказкой 17
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_17.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_17"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_18():

    ## Экран с подсказкой 18
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_18.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_18"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_19():

    ## Экран с подсказкой 19
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_19.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_19"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_20():

    ## Экран с подсказкой 20
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_20.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_20"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_21():

    ## Экран с подсказкой 21
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_21.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_21"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_22():

    ## Экран с подсказкой 22
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_22.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_22"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_23():

    ## Экран с подсказкой 23
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_23.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_23"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_24():

    ## Экран с подсказкой 24
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_24.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_24"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_25():

    ## Экран с подсказкой 25
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_25.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_25"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_26():

    ## Экран с подсказкой 26
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_26.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_26"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_27():

    ## Экран с подсказкой 27
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_27.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_27"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_28():

    ## Экран с подсказкой 28
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_28.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_28"), Show("stand_tips_list")


    add "tips_owl_anim"

screen tips_owl_tip_29():

    ## Экран с подсказкой 29
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/tips_owl/tips/tip_29.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png"

        #hotspot(1845,0,75,77) action Return()
        hotspot(1845,0,75,77) action Hide("tips_owl_tip_29"), Show("stand_tips_list")


    add "tips_owl_anim"


##Конец экранов ответов, даваемых совой
################################

## Конец совы, дающей подсказки
################################


screen stand_diary():

    ## Экран с дневником, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_diary_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_diary"), Show("info_stand")

screen stand_inventory():

    ## Экран с инвентарём, открывается при клике в главном меню соответствующей таблички на стенде
    #tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/info_stand/stand_inventory_gr.webp"
        idle "gui/info_stand_nav_idle.png"
        hover "gui/info_stand_nav_hover.png" 

        hotspot(1845,0,75,77) action Hide("stand_inventory"), Show("info_stand")


image stand_campfire_anim:

    ##Анимация костра на стенде

    pos (627,555)

    "images/info_stand/stand_campfire/cf01.png"
    pause 0.2
    "images/info_stand/stand_campfire/cf02.png"
    pause 0.2
    "images/info_stand/stand_campfire/cf03.png"
    pause 0.2
    "images/info_stand/stand_campfire/cf01.png"
    pause 0.2
    "images/info_stand/stand_campfire/cf04.png"
    pause 0.2
    "images/info_stand/stand_campfire/cf05.png"
    pause 0.2
    repeat


screen stand_campfire():

    ## Экран с костром
    add "stand_campfire_anim"



image progressbar = Transform(DynamicImage('images/info_stand/progressbar/[days].png'), xpos = 446, ypos = 34, xsize=1027, ysize=68) ## Динамически меняющаяся картинка с прогрессбаром.
 
## РАСКОММЕНТИРОВАТЬ imgage progressbar, КОГДА БУДУТ КАРТИНКИ ПО КОЛИЧЕСТВУ ДНЕЙ. И НИЖЕ, В screen info_stand() ТОЖЕ


screen info_stand():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    # on 'show' action PauseAudio('music', True) 
    # on 'hide' action PauseAudio('music', False)

    on 'show' action (PauseAudio('music', True), SetField(config, "rollback_enabled", False))
    on 'hide' action (PauseAudio('music', False), SetField(config, "rollback_enabled", True))

    #tag menu
    zorder 100
    modal True

    imagemap:

        ground "images/info_stand/info_stand_gr2.webp"
        idle "images/info_stand/info_stand_normal2.png"
        hover "images/info_stand/info_stand_hover2.png"

        hotspot(589,285,373,42) action Show ("stand_camp_rules")
        hotspot(537,182,458,64) action Show ("stand_honor_board")
        hotspot(604,330,118,108) action Show ("stand_advertisements"), Hide("stand_advertisements"), Show ("stand_advertisements")
        hotspot(847,340,102,106) action Show ("stand_mailbox")
        hotspot(564,486,344,66) action Show ("stand_hikes")
        hotspot(569,747,327,40) action Show ("stand_history")
        hotspot(1017,181,415,182) action Show ("map")
        hotspot(1018,364,419,123) action Show ("stand_wall_newspaper")
        hotspot(983,512,255,261) action Show ("campmap")
        hotspot(1243,501,182,136) action Show ("stand_gallery_1")
        hotspot(1252,684,175,101) action Show ("stand_tips_owl")
        #hotspot(434,869,282,187) action Show ("sc_d_prologue")
        #hotspot(1258,851,226,212) action Show ("stand_inventory")
        #hotspot(1258,851,226,212) action Show ("inventory_slots")
        hotspot(848,851,226,212) action Hide ("info_stand"), Show ("inventory_slots")

    add "stand_campfire_anim"

    add "progressbar" #РАСКОММЕНТИРОВАТЬ, КОГДА БУДУТ КАРТИНКИ ДНЕЙ
    

    imagebutton:
        xpos 1856 ypos 11
        idle "gui/closebut_idle.png"
        hover "gui/closebut_hover.png"
        action Hide ("info_stand")#, Return()
        