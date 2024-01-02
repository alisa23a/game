screen sc_d_prologue:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_prologue.webp"
        idle "gui/dnav1idle.png"
        hover "gui/dnav1hover.png"
        
        hotspot(1784,464,112,152) action Hide ("sc_d_prologue"), Show ("sc_d_00")
        hotspot(1787,37,85,84) action Hide ("sc_d_prologue"), Show ("info_stand")

screen sc_d_00:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_00.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_00"), Show ("sc_d_prologue")
        hotspot(1784,464,112,152) action Hide ("sc_d_00"), Show ("sc_d_01")
        hotspot(1787,37,85,84) action Hide ("sc_d_00"), Show ("info_stand")

screen sc_d_01:
    tag menu
    zorder 100
    modal True

    imagemap:
        ground "images/diary/p_01.webp"
        idle "gui/diary4i.png"
        hover "gui/diary4h.png"
        
        hotspot(1040,277,685,384) action Hide ("sc_d_01"), Show ("sc_d_01_pic")
        hotspot(24,464,112,152) action Hide ("sc_d_01"), Show ("sc_d_00")
        hotspot(1784,464,112,152) action Hide ("sc_d_01"), Show ("sc_d_02")
        hotspot(1787,37,85,84) action Hide ("sc_d_01"), Show ("info_stand")


screen sc_d_01_pic:
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
        action Hide ("sc_d_01_pic"), Show("sc_d_01")

        
screen sc_d_02:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_02.webp"
        idle "gui/diary5i.png"
        hover "gui/diary5h.png"
        
        hotspot(176,149,682,685) action Hide ("sc_d_02"), Show ("sc_d_02_pic")
        hotspot(24,464,112,152) action Hide ("sc_d_02"), Show ("sc_d_01")
        hotspot(1784,464,112,152) action Hide ("sc_d_02"), Show ("sc_d_03")
        hotspot(1787,37,85,84) action Hide ("sc_d_02"), Show ("info_stand")    

screen sc_d_02_pic:
    tag menu
    zorder 100
    modal True

    add "p_house"
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sc_d_02_pic"), Show("sc_d_02")

screen sc_d_03:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_03.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_03"), Show ("sc_d_02")
        hotspot(1784,464,112,152) action Hide ("sc_d_03"), Show ("sc_d_04")
        hotspot(1787,37,85,84) action Hide ("sc_d_03"), Show ("info_stand")

screen sc_d_04:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_04.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_04"), Show ("sc_d_03")
        hotspot(1784,464,112,152) action Hide ("sc_d_04"), Show ("sc_d_05")
        hotspot(1787,37,85,84) action Hide ("sc_d_04"), Show ("info_stand")

screen sc_d_05:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_05.webp"
        idle "gui/diary8i.png"
        hover "gui/diary8h.png"
        
        hotspot(1061,465,612,332) action Hide ("sc_d_05"), Show ("sc_d_05_pic")
        hotspot(24,464,112,152) action Hide ("sc_d_05"), Show ("sc_d_04")
        hotspot(1784,464,112,152) action Hide ("sc_d_05"), Show ("sc_d_06")
        hotspot(1787,37,85,84) action Hide ("sc_d_05"), Show ("info_stand")

screen sc_d_05_pic:
    tag menu
    zorder 110
    modal True

    add "images/prolog/boat.webp"
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("sc_d_05_pic"), Show("sc_d_05")

screen sc_d_06:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_06.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_06"), Show ("sc_d_05")
        hotspot(1784,464,112,152) action Hide ("sc_d_06"), Show ("sc_d_07")
        hotspot(1787,37,85,84) action Hide ("sc_d_06"), Show ("info_stand")

screen sc_d_07:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_07.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_07"), Show ("sc_d_06")
        hotspot(1784,464,112,152) action Hide ("sc_d_07"), Show ("sc_d_08")
        hotspot(1787,37,85,84) action Hide ("sc_d_07"), Show ("info_stand")


screen sc_d_08:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_08.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
 
        hotspot(24,464,112,152) action Hide ("sc_d_08"), Show ("sc_d_07") 
        hotspot(1784,464,112,152) action Hide ("sc_d_08"), Show ("sc_d_09")
        hotspot(1787,37,85,84) action Hide ("sc_d_08"), Show ("info_stand")

screen sc_d_09:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_09.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_09"), Show ("sc_d_08")
        hotspot(1784,464,112,152) action Hide ("sc_d_09"), Show ("sc_d_10")
        hotspot(1787,37,85,84) action Hide ("sc_d_09"), Show ("info_stand")

screen sc_d_10:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_10.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_10"), Show ("sc_d_09")
        hotspot(1784,464,112,152) action Hide ("sc_d_10"), Show ("sc_d_11")
        hotspot(1787,37,85,84) action Hide ("sc_d_10"), Show ("info_stand")

screen sc_d_11:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_11.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_11"), Show ("sc_d_10")
        hotspot(1784,464,112,152) action Hide ("sc_d_11"), Show ("sc_d_12")
        hotspot(1787,37,85,84) action Hide ("sc_d_11"), Show ("info_stand")


screen sc_d_12:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_12.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_12"), Show ("sc_d_11")
        hotspot(1784,464,112,152) action Hide ("sc_d_12"), Show ("sc_d_13")
        hotspot(1787,37,85,84) action Hide ("sc_d_12"), Show ("info_stand")

screen sc_d_13:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_13.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_13"), Show ("sc_d_12")
        hotspot(1784,464,112,152) action Hide ("sc_d_13"), Show ("sc_d_14")
        hotspot(1787,37,85,84) action Hide ("sc_d_13"), Show ("info_stand")

screen sc_d_14:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_14.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_14"), Show ("sc_d_13")
        hotspot(1784,464,112,152) action Hide ("sc_d_14"), Show ("sc_d_15")
        hotspot(1787,37,85,84) action Hide ("sc_d_14"), Show ("info_stand")

screen sc_d_15:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_15.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_15"), Show ("sc_d_14")
        hotspot(1784,464,112,152) action Hide ("sc_d_15"), Show ("sc_d_16")
        hotspot(1787,37,85,84) action Hide ("sc_d_15"), Show ("info_stand")

screen sc_d_16:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_16.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_16"), Show ("sc_d_15")
        hotspot(1784,464,112,152) action Hide ("sc_d_16"), Show ("sc_d_17")
        hotspot(1787,37,85,84) action Hide ("sc_d_16"), Show ("info_stand")

screen sc_d_17:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_17.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_17"), Show ("sc_d_16")
        hotspot(1784,464,112,152) action Hide ("sc_d_17"), Show ("sc_d_18")
        hotspot(1787,37,85,84) action Hide ("sc_d_17"), Show ("info_stand")

screen sc_d_18:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_18.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_18"), Show ("sc_d_17")
        hotspot(1784,464,112,152) action Hide ("sc_d_18"), Show ("sc_d_19")
        hotspot(1787,37,85,84) action Hide ("sc_d_18"), Show ("info_stand")

screen sc_d_19:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_19.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_19"), Show ("sc_d_18")
        hotspot(1784,464,112,152) action Hide ("sc_d_19"), Show ("sc_d_20")
        hotspot(1787,37,85,84) action Hide ("sc_d_19"), Show ("info_stand")

screen sc_d_20:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_20.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_20"), Show ("sc_d_19")
        hotspot(1784,464,112,152) action Hide ("sc_d_20"), Show ("sc_d_21")
        hotspot(1787,37,85,84) action Hide ("sc_d_20"), Show ("info_stand")

screen sc_d_21:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_21.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_21"), Show ("sc_d_20")
        hotspot(1784,464,112,152) action Hide ("sc_d_21"), Show ("sc_d_22")
        hotspot(1787,37,85,84) action Hide ("sc_d_21"), Show ("info_stand")

screen sc_d_22:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_22.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_22"), Show ("sc_d_21")
        hotspot(1784,464,112,152) action Hide ("sc_d_22"), Show ("sc_d_23")
        hotspot(1787,37,85,84) action Hide ("sc_d_22"), Show ("info_stand")

screen sc_d_23:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_23.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_23"), Show ("sc_d_22")
        hotspot(1784,464,112,152) action Hide ("sc_d_23"), Show ("sc_d_24")
        hotspot(1787,37,85,84) action Hide ("sc_d_23"), Show ("info_stand")

screen sc_d_24:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_24.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_24"), Show ("sc_d_23")
        hotspot(1784,464,112,152) action Hide ("sc_d_24"), Show ("sc_d_25")
        hotspot(1787,37,85,84) action Hide ("sc_d_24"), Show ("info_stand")

screen sc_d_25:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_25.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_25"), Show ("sc_d_24")
        hotspot(1784,464,112,152) action Hide ("sc_d_25"), Show ("sc_d_26")
        hotspot(1787,37,85,84) action Hide ("sc_d_25"), Show ("info_stand")

screen sc_d_26:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_26.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_26"), Show ("sc_d_25")
        hotspot(1784,464,112,152) action Hide ("sc_d_26"), Show ("sc_d_27")
        hotspot(1787,37,85,84) action Hide ("sc_d_26"), Show ("info_stand")

screen sc_d_27:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_27.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_27"), Show ("sc_d_26")
        hotspot(1784,464,112,152) action Hide ("sc_d_27"), Show ("sc_d_28")
        hotspot(1787,37,85,84) action Hide ("sc_d_27"), Show ("info_stand")

screen sc_d_28:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_28.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_28"), Show ("sc_d_27")
        hotspot(1784,464,112,152) action Hide ("sc_d_28"), Show ("sc_d_29")
        hotspot(1787,37,85,84) action Hide ("sc_d_28"), Show ("info_stand")

screen sc_d_29:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_29.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_29"), Show ("sc_d_28")
        hotspot(1784,464,112,152) action Hide ("sc_d_29"), Show ("sc_d_30")
        hotspot(1787,37,85,84) action Hide ("sc_d_29"), Show ("info_stand")

screen sc_d_30:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_30.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_30"), Show ("sc_d_29")
        hotspot(1784,464,112,152) action Hide ("sc_d_30"), Show ("sc_d_31")
        hotspot(1787,37,85,84) action Hide ("sc_d_30"), Show ("info_stand")

screen sc_d_31:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_31.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_31"), Show ("sc_d_30")
        hotspot(1784,464,112,152) action Hide ("sc_d_31"), Show ("sc_d_32")
        hotspot(1787,37,85,84) action Hide ("sc_d_31"), Show ("info_stand")

screen sc_d_32:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_32.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_32"), Show ("sc_d_31")
        hotspot(1784,464,112,152) action Hide ("sc_d_32"), Show ("sc_d_33")
        hotspot(1787,37,85,84) action Hide ("sc_d_32"), Show ("info_stand")

screen sc_d_33:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_33.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_33"), Show ("sc_d_32")
        hotspot(1784,464,112,152) action Hide ("sc_d_33"), Show ("sc_d_34")
        hotspot(1787,37,85,84) action Hide ("sc_d_33"), Show ("info_stand")

screen sc_d_34:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_34.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_34"), Show ("sc_d_33")
        hotspot(1784,464,112,152) action Hide ("sc_d_34"), Show ("sc_d_35")
        hotspot(1787,37,85,84) action Hide ("sc_d_34"), Show ("info_stand")

screen sc_d_35:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_35.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_35"), Show ("sc_d_34")
        hotspot(1784,464,112,152) action Hide ("sc_d_35"), Show ("sc_d_36")
        hotspot(1787,37,85,84) action Hide ("sc_d_35"), Show ("info_stand")

screen sc_d_36:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_36.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_36"), Show ("sc_d_35")
        hotspot(1784,464,112,152) action Hide ("sc_d_36"), Show ("sc_d_37")
        hotspot(1787,37,85,84) action Hide ("sc_d_36"), Show ("info_stand")


screen sc_d_37:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_37.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_37"), Show ("sc_d_36")
        hotspot(1784,464,112,152) action Hide ("sc_d_37"), Show ("sc_d_38")
        hotspot(1787,37,85,84) action Hide ("sc_d_37"), Show ("info_stand")

screen sc_d_38:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_38.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_38"), Show ("sc_d_37")
        hotspot(1784,464,112,152) action Hide ("sc_d_38"), Show ("sc_d_39")
        hotspot(1787,37,85,84) action Hide ("sc_d_38"), Show ("info_stand")

screen sc_d_39:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_39.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_39"), Show ("sc_d_38")
        hotspot(1784,464,112,152) action Hide ("sc_d_39"), Show ("sc_d_40")
        hotspot(1787,37,85,84) action Hide ("sc_d_39"), Show ("info_stand")

screen sc_d_40:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_40.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_40"), Show ("sc_d_39")
        hotspot(1784,464,112,152) action Hide ("sc_d_40"), Show ("sc_d_41")
        hotspot(1787,37,85,84) action Hide ("sc_d_40"), Show ("info_stand")


screen sc_d_41:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_41.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_41"), Show ("sc_d_40")
        hotspot(1784,464,112,152) action Hide ("sc_d_41"), Show ("sc_d_42")
        hotspot(1787,37,85,84) action Hide ("sc_d_41"), Show ("info_stand")


screen sc_d_42:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_42.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_42"), Show ("sc_d_41")
        hotspot(1784,464,112,152) action Hide ("sc_d_42"), Show ("sc_d_43")
        hotspot(1787,37,85,84) action Hide ("sc_d_42"), Show ("info_stand")


screen sc_d_43:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_43.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_43"), Show ("sc_d_42")
        hotspot(1784,464,112,152) action Hide ("sc_d_43"), Show ("sc_d_44")
        hotspot(1787,37,85,84) action Hide ("sc_d_43"), Show ("info_stand")


screen sc_d_44:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_44.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_44"), Show ("sc_d_43")
        hotspot(1784,464,112,152) action Hide ("sc_d_44"), Show ("sc_d_45")
        hotspot(1787,37,85,84) action Hide ("sc_d_44"), Show ("info_stand")


screen sc_d_45:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_45.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_45"), Show ("sc_d_44")
        hotspot(1784,464,112,152) action Hide ("sc_d_45"), Show ("sc_d_46")
        hotspot(1787,37,85,84) action Hide ("sc_d_45"), Show ("info_stand")


screen sc_d_46:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_46.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_46"), Show ("sc_d_45")
        hotspot(1784,464,112,152) action Hide ("sc_d_46"), Show ("sc_d_47")
        hotspot(1787,37,85,84) action Hide ("sc_d_46"), Show ("info_stand")


screen sc_d_47:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_47.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_47"), Show ("sc_d_46")
        hotspot(1784,464,112,152) action Hide ("sc_d_47"), Show ("sc_d_48")
        hotspot(1787,37,85,84) action Hide ("sc_d_47"), Show ("info_stand")


screen sc_d_48:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_48.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_48"), Show ("sc_d_47")
        hotspot(1784,464,112,152) action Hide ("sc_d_48"), Show ("sc_d_49")
        hotspot(1787,37,85,84) action Hide ("sc_d_48"), Show ("info_stand")


screen sc_d_49:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/p_49.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("sc_d_49"), Show ("sc_d_48")
        hotspot(1784,464,112,152) action Hide ("sc_d_49"), Show ("info_stand")
        hotspot(1787,37,85,84) action Hide ("sc_d_49"), Show ("info_stand")

# label prolog:

    # scene bg room

    # menu:
        # "Видео пролога":
            # jump prolog1
        # "Пролог":
            # jump prolog_diary

# return

# label prolog1:
    # #e "prolog1"
    # $ renpy.movie_cutscene("videos/prolog.ogv") #команда для запуска видео на весь экран
# return

# label prolog_diary:
    # show screen prolog_diary
    # #jump start
    # #return

# label prolog_diary2:
    # show screen prolog_diary2
    # #jump start
    # return

# label prolog_diary3:
    # show screen prolog_diary3
    # jump start
    # return

# label prolog_diary4:
    # if musicstop:
        # play music track1

    # show screen prolog_diary4
    # jump start
    # return

# label prolog_diary4pic:
    # show p_dream
    # play music dreams
    # ""
    # hide p_dream
    # stop music
    # $ musicstop = True
    # #jump prolog_diary4
    # show screen prolog_diary4
    # return

# label prolog_diary5:
    # show screen prolog_diary5
    # jump start
    # return

# label prolog_diary5pic:
    # show p_house
    # ""
    # hide p_house
    # jump prolog_diary5
    # return

# label prolog_diary6:
    # show screen prolog_diary6
    # jump start
    # return

# label prolog_diary7:
    # show screen prolog_diary7
    # jump start
    # return

# label prolog_diary8:
    # show screen prolog_diary8
    # jump start
    # return

# label prolog_diary8pic:
    # call screen prolog_diary8picsc
    # jump prolog_diary8
    # return

# label prolog_diary9:
    # show screen prolog_diary9
    # jump start
    # return

# label prolog_diary10:
    # show screen prolog_diary10
    # jump start
    # return
# return
