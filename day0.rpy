####################################
## Дневник, картиночная версия, отображается в начале игры
screen sc_p_prologue:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_prologue.webp"
        idle "gui/dnav1idle.png"
        hover "gui/dnav1hover.png"
        
        hotspot(1784,464,112,152) action Hide ("sc_p_prologue"), Show ("sc_p_00")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page"), Show ("info_stand")

screen sc_p_00:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_00.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_00"), Show ("sc_p_prologue")
        hotspot(1784,464,112,152) action Hide ("sc_p_00"), Show ("sc_p_01")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page2"), Show ("info_stand")

screen sc_p_01:
    tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/diary/p_01.webp"
        idle "gui/diary4i.png"
        hover "gui/diary4h.png"
        
        hotspot(1040,277,685,384) action Hide ("sc_p_01"), Show ("sc_p_01_pic")
        hotspot(24,464,112,152) action Hide ("sc_p_01"), Show ("sc_p_00")
        hotspot(1784,464,112,152) action Hide ("sc_p_01"), Show ("sc_p_02")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page4"), Show ("info_stand")


screen sc_p_01_pic:
    tag menu
    zorder 100
    modal True

    on "show" action Play("dreamMusicChannel", "audio/music/dream.mp3")
    on "hide" action Stop("dreamMusicChannel")

    add "p_dream"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sc_p_01_pic"), Show("sc_p_01")

        
screen sc_p_02:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_02.webp"
        idle "gui/diary5i.png"
        hover "gui/diary5h.png"
        
        hotspot(176,149,682,685) action Hide ("sc_p_02"), Show ("sc_p_02_pic")
        hotspot(24,464,112,152) action Hide ("sc_p_02"), Show ("sc_p_01")
        hotspot(1784,464,112,152) action Hide ("sc_p_02"), Show ("sc_p_03")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page5"), Show ("info_stand")    

screen sc_p_02_pic:
    tag menu
    zorder 100
    modal True

    #$ renpy.music.stop()
    add "p_house"
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sc_p_02_pic"), Show("sc_p_02")

screen sc_p_03:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_03.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_03"), Show ("sc_p_02")
        hotspot(1784,464,112,152) action Hide ("sc_p_03"), Show ("sc_p_04")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page6"), Show ("info_stand")

screen sc_p_04:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_04.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_04"), Show ("sc_p_03")
        hotspot(1784,464,112,152) action Hide ("sc_p_04"), Show ("sc_p_05")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page7"), Show ("info_stand")

screen sc_p_05:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_05.webp"
        idle "gui/diary8i.png"
        hover "gui/diary8h.png"
        
        hotspot(1061,465,612,332) action Hide ("sc_p_05"), Show ("sc_p_05_pic")
        hotspot(24,464,112,152) action Hide ("sc_p_05"), Show ("sc_p_04")
        hotspot(1784,464,112,152) action Hide ("sc_p_05"), Show ("sc_p_06")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page8"), Show ("info_stand")

screen sc_p_05_pic:
    tag menu
    zorder 110
    modal True

    add "images/prolog/boat.webp"
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sc_p_05_pic"), Show("sc_p_05")

screen sc_p_06:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_06.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_06"), Show ("sc_p_05")
        hotspot(1784,464,112,152) action Hide ("sc_p_06"), Show ("sc_p_07")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page9"), Show ("info_stand")

screen sc_p_07:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_07.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_07"), Show ("sc_p_06")
        hotspot(1784,464,112,152) action Hide ("sc_p_07"), Show ("sc_p_08")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page10"), Show ("info_stand")


screen sc_p_08:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_08.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
 
        hotspot(24,464,112,152) action Hide ("sc_p_08"), Show ("sc_p_07") 
        hotspot(1784,464,112,152) action Hide ("sc_p_08"), Show ("sc_p_09")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page11"), Show ("info_stand")

screen sc_p_09:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_09.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_09"), Show ("sc_p_08")
        hotspot(1784,464,112,152) action Hide ("sc_p_09"), Show ("sc_p_10")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page12"), Show ("info_stand")

screen sc_p_10:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_10.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_10"), Show ("sc_p_09")
        hotspot(1784,464,112,152) action Hide ("sc_p_10"), Show ("sc_p_11")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page13"), Show ("info_stand")

screen sc_p_11:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_11.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_11"), Show ("sc_p_10")
        hotspot(1784,464,112,152) action Hide ("sc_p_11"), Show ("sc_p_12")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page14"), Show ("info_stand")


screen sc_p_12:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_12.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_12"), Show ("sc_p_11")
        hotspot(1784,464,112,152) action Hide ("sc_p_12"), Show ("sc_p_13")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page15"), Show ("info_stand")

screen sc_p_13:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_13.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_13"), Show ("sc_p_12")
        hotspot(1784,464,112,152) action Hide ("sc_p_13"), Show ("sc_p_14")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page16"), Show ("info_stand")

screen sc_p_14:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_14.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_14"), Show ("sc_p_13")
        hotspot(1784,464,112,152) action Hide ("sc_p_14"), Show ("sc_p_14_1")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page17"), Show ("info_stand")

screen sc_p_14_1:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_14_1.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_14_1"), Show ("sc_p_14")
        hotspot(1784,464,112,152) action Hide ("sc_p_14_1"), Show ("sc_p_15")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page17"), Show ("info_stand")

screen sc_p_15:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_15.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_15"), Show ("sc_p_14")
        hotspot(1784,464,112,152) action Hide ("sc_p_15"), Show ("sc_p_15_1")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_15_1:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_15_1.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_15_1"), Show ("sc_p_15")
        hotspot(1784,464,112,152) action Hide ("sc_p_15_1"), Show ("sc_p_15_2")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_15_2:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_15_2.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_15_2"), Show ("sc_p_15_1")
        hotspot(1784,464,112,152) action Hide ("sc_p_15_2"), Show ("sc_p_16")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_16:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_16.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_16"), Show ("sc_p_15_2")
        hotspot(1784,464,112,152) action Hide ("sc_p_16"), Show ("sc_p_17")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_17:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_17.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_17"), Show ("sc_p_16")
        hotspot(1784,464,112,152) action Hide ("sc_p_17"), Show ("sc_p_18")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_18:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_18.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_18"), Show ("sc_p_17")
        hotspot(1784,464,112,152) action Hide ("sc_p_18"), Show ("sc_p_19")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_19:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_19.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_19"), Show ("sc_p_18")
        hotspot(1784,464,112,152) action Hide ("sc_p_19"), Show ("sc_p_20")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_20:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_20.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_20"), Show ("sc_p_19")
        hotspot(1784,464,112,152) action Hide ("sc_p_20"), Show ("sc_p_21")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_21:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_21.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_21"), Show ("sc_p_20")
        hotspot(1784,464,112,152) action Hide ("sc_p_21"), Show ("sc_p_22")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_22:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_22.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_22"), Show ("sc_p_21")
        hotspot(1784,464,112,152) action Hide ("sc_p_22"), Show ("sc_p_23")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_23:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_23.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_23"), Show ("sc_p_22")
        hotspot(1784,464,112,152) action Hide ("sc_p_23"), Show ("sc_p_24")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_24:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_24.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_24"), Show ("sc_p_23")
        hotspot(1784,464,112,152) action Hide ("sc_p_24"), Show ("sc_p_25")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_25:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_25.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_25"), Show ("sc_p_24")
        hotspot(1784,464,112,152) action Hide ("sc_p_25"), Show ("sc_p_26")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_26:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_26.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_26"), Show ("sc_p_25")
        hotspot(1784,464,112,152) action Hide ("sc_p_26"), Show ("sc_p_27")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_27:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_27.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_27"), Show ("sc_p_26")
        hotspot(1784,464,112,152) action Hide ("sc_p_27"), Show ("sc_p_28")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_28:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_28.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_28"), Show ("sc_p_27")
        hotspot(1784,464,112,152) action Hide ("sc_p_28"), Show ("sc_p_29")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_29:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_29.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_29"), Show ("sc_p_28")
        hotspot(1784,464,112,152) action Hide ("sc_p_29"), Show ("sc_p_30")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_30:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_30.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_30"), Show ("sc_p_29")
        hotspot(1784,464,112,152) action Hide ("sc_p_30"), Show ("sc_p_31")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_31:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_31.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_31"), Show ("sc_p_30")
        hotspot(1784,464,112,152) action Hide ("sc_p_31"), Show ("sc_p_32")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_32:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_32.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_32"), Show ("sc_p_31")
        hotspot(1784,464,112,152) action Hide ("sc_p_32"), Show ("sc_p_33")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_33:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_33.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_33"), Show ("sc_p_32")
        hotspot(1784,464,112,152) action Hide ("sc_p_33"), Show ("sc_p_34")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_34:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_34.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_34"), Show ("sc_p_33")
        hotspot(1784,464,112,152) action Hide ("sc_p_34"), Show ("sc_p_35")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_35:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_35.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_35"), Show ("sc_p_34")
        hotspot(1784,464,112,152) action Hide ("sc_p_35"), Show ("sc_p_36")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_36:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_36.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_36"), Show ("sc_p_35")
        hotspot(1784,464,112,152) action Hide ("sc_p_36"), Show ("sc_p_37")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_37:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_37.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_37"), Show ("sc_p_36")
        hotspot(1784,464,112,152) action Hide ("sc_p_37"), Show ("sc_p_38")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_38:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_38.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_38"), Show ("sc_p_37")
        hotspot(1784,464,112,152) action Hide ("sc_p_38"), Show ("sc_p_39")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_39:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_39.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_39"), Show ("sc_p_38")
        hotspot(1784,464,112,152) action Hide ("sc_p_39"), Show ("sc_p_40")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen sc_p_40:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_40.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_40"), Show ("sc_p_39")
        hotspot(1784,464,112,152) action Hide ("sc_p_40"), Show ("sc_p_41")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_41:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_41.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_41"), Show ("sc_p_40")
        hotspot(1784,464,112,152) action Hide ("sc_p_41"), Show ("sc_p_42")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_42:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_42.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_42"), Show ("sc_p_41")
        hotspot(1784,464,112,152) action Hide ("sc_p_42"), Show ("sc_p_43")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_43:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_43.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_43"), Show ("sc_p_42")
        hotspot(1784,464,112,152) action Hide ("sc_p_43"), Show ("sc_p_44")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_44:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_44.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_44"), Show ("sc_p_43")
        hotspot(1784,464,112,152) action Hide ("sc_p_44"), Show ("sc_p_45")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_45:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_45.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_45"), Show ("sc_p_44")
        hotspot(1784,464,112,152) action Hide ("sc_p_45"), Show ("sc_p_46")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_46:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_46.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_46"), Show ("sc_p_45")
        hotspot(1784,464,112,152) action Hide ("sc_p_46"), Show ("sc_p_47")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_47:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_47.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_47"), Show ("sc_p_46")
        hotspot(1784,464,112,152) action Hide ("sc_p_47"), Show ("sc_p_48")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_48:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_48.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_48"), Show ("sc_p_47")
        hotspot(1784,464,112,152) action Hide ("sc_p_48"), Show ("sc_p_49")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen sc_p_49:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_49.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_49"), Show ("sc_p_48")
        hotspot(1784,464,112,152) action Hide ("sc_p_49"), Show ("sc_p_50")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")



screen sc_p_50:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_50.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_50"), Show ("sc_p_49")
        hotspot(1784,464,112,152) action Hide ("sc_p_50"), Show ("sc_p_51")
        #hotspot(1787,37,85,84) action Hide ("sc_d_50"), Show ("info_stand")


screen sc_p_51:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_51.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_51"), Show ("sc_p_50")
        hotspot(1784,464,112,152) action Hide ("sc_p_51"), Show ("sc_p_52")
        #hotspot(1787,37,85,84) action Hide ("sc_d_51"), Show ("info_stand")


screen sc_p_52:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_52.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_p_52"), Show ("sc_p_51")
        hotspot(1784,464,112,152) action Hide ("sc_p_52"), Jump ("day8")
        #hotspot(1787,37,85,84) action Hide ("sc_d_52"), Show ("info_stand")






#Jump ("day8")

image prologue = Movie(play="video/prologue.webm", size=(1920, 1080))

image first_morning = Movie(play="video/first_morning.webm", size=(1920, 1080))

    # scene ul_pi_island_02

    # pause (10000000000)

label start:

    stop music

    $ show_quick_menu = False

    show prologue

    pause (299.5)
    
    hide prologue

    jump first_m
    

label first_m:  

    show first_morning
    
    #$ renpy.movie_cutscene("video/first_morning.webm")

    pause (406.0)

    hide first_morning

    jump diary_pages_all


label diary_pages_all:

    show screen sc_p_prologue with fade
    
    pause (10000000000)




































