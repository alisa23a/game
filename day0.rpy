screen prolog_diary_page:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary1.webp"
        idle "gui/dnav1idle.png"
        hover "gui/dnav1hover.png"
        
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page"), Show ("prolog_diary_page2")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page"), Show ("info_stand")

screen prolog_diary_page2:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary2.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page2"), Show ("prolog_diary_page")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page2"), Show ("prolog_diary_page3")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page2"), Show ("info_stand")

screen prolog_diary_page3:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary3.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page3"), Show ("prolog_diary_page2")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page3"), Show ("prolog_diary_page4")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page3"), Show ("info_stand")

screen prolog_diary_page4:
    tag menu
    zorder 100
    modal True

    #$ renpy.music.set_pause(False, channel="music")

    imagemap:
        ground "images/diary/diary4.webp"
        idle "gui/diary4i.png"
        hover "gui/diary4h.png"
        
        hotspot(1040,277,685,384) action Hide ("prolog_diary_page4"), Show ("prolog_d4pic_page")
        hotspot(24,464,112,152) action Hide ("prolog_diary_page4"), Show ("prolog_diary_page3")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page4"), Show ("prolog_diary_page5")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page4"), Show ("info_stand")


screen prolog_d4pic_page:
    tag menu
    zorder 100
    modal True

    #$ renpy.music.set_pause(True, channel="music")
    on "show" action Play("dreamMusicChannel", "audio/music/dream.mp3")
    on "hide" action Stop("dreamMusicChannel")

    add "p_dream"

    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("prolog_d4pic_page"), Show("prolog_diary_page4")

        
screen prolog_diary_page5:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary5.webp"
        idle "gui/diary5i.png"
        hover "gui/diary5h.png"
        
        hotspot(176,149,682,685) action Hide ("prolog_diary_page5"), Show ("prolog_d5pic_page")
        hotspot(24,464,112,152) action Hide ("prolog_diary_page5"), Show ("prolog_diary_page4")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page5"), Show ("prolog_diary_page6")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page5"), Show ("info_stand")    

screen prolog_d5pic_page:
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
        action Hide ("prolog_diary_page5pic_page"), Show("prolog_diary_page5")

screen prolog_diary_page6:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary6.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page6"), Show ("prolog_diary_page5")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page6"), Show ("prolog_diary_page7")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page6"), Show ("info_stand")

screen prolog_diary_page7:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary7.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page7"), Show ("prolog_diary_page6")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page7"), Show ("prolog_diary_page8")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page7"), Show ("info_stand")

screen prolog_diary_page8:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary8.webp"
        idle "gui/diary8i.png"
        hover "gui/diary8h.png"
        
        hotspot(1061,465,612,332) action Hide ("prolog_diary_page8"), Show ("prolog_d8pic_page")
        hotspot(24,464,112,152) action Hide ("prolog_diary_page8"), Show ("prolog_diary_page7")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page8"), Show ("prolog_diary_page9")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page8"), Show ("info_stand")

screen prolog_d8pic_page:
    tag menu
    zorder 110
    modal True

    add "images/prolog/boat.webp"
    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("prolog_d8pic"), Show("prolog_diary_page8")

screen prolog_diary_page9:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary9.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page9"), Show ("prolog_diary_page8")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page9"), Show ("prolog_diary_page10")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page9"), Show ("info_stand")

screen prolog_diary_page10:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary10.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary_page10"), Show ("prolog_diary_page9")
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page10"), Show ("day2_diary_page11")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page10"), Show ("info_stand")


screen day2_diary_page11:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary11.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
 
        hotspot(24,464,112,152) action Hide ("day2_diary_page11"), Show ("prolog_diary10") 
        hotspot(1784,464,112,152) action Hide ("day2_diary_page11"), Show ("day2_diary_page12")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page11"), Show ("info_stand")

screen day2_diary_page12:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary12.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary_page12"), Show ("day2_diary_page11")
        hotspot(1784,464,112,152) action Hide ("day2_diary_page12"), Show ("day2_diary_page13")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page12"), Show ("info_stand")

screen day2_diary_page13:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary13.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary_page13"), Show ("day2_diary_page12")
        hotspot(1784,464,112,152) action Hide ("day2_diary_page13"), Show ("day2_diary_page13choice")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page13"), Show ("info_stand")

screen day2_diary_page13choice:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary13choice.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary_page13choice"), Show ("day2_diary_page13")
        hotspot(1784,464,112,152) action Hide ("day2_diary_page13choice"), Show ("day2_diary_page14")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page13choice"), Show ("info_stand")

screen day2_diary_page14:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary14.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary_page14"), Show ("day2_diary_page13choice")
        hotspot(1784,464,112,152) action Hide ("day2_diary_page14"), Show ("day3_diary_page15")
        #hotspot(1787,37,85,84) action Hide ("day2_diary_page14"), Show ("info_stand")


screen day3_diary_page15:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary15.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(1784,464,112,152) action Hide ("day3_diary_page15"), Show ("day2_diary_page14")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page15"), Show ("day3_diary_page16")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page15"), Show ("info_stand")

screen day3_diary_page16:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary16.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page16"), Show ("day3_diary_page15")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page16"), Show ("day3_diary_page17")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page16"), Show ("info_stand")

screen day3_diary_page17:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary17.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page17"), Show ("day3_diary_page16")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page17"), Show ("day3_diary_page18")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page17"), Show ("info_stand")

screen day3_diary_page18:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary18.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page18"), Show ("day3_diary_page17")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page18"), Show ("day3_diary_page19")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page19:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary19.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page19"), Show ("day3_diary_page18")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page19"), Show ("day3_diary_page20")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page20:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary20.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page20"), Show ("day3_diary_page19")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page20"), Show ("day3_diary_page21")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page21:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary21.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page21"), Show ("day3_diary_page20")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page21"), Show ("day3_diary_page22")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page22:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary22.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page22"), Show ("day3_diary_page21")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page22"), Show ("day3_diary_page23")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page23:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary23.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page23"), Show ("day3_diary_page22")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page23"), Show ("day3_diary_page24")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page24:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary24.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page24"), Show ("day3_diary_page23")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page24"), Show ("day3_diary_page25")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page25:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary25.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page25"), Show ("day3_diary_page24")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page25"), Show ("day3_diary_page26")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page26:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary26.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page26"), Show ("day3_diary_page25")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page26"), Show ("day3_diary_page27")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page27:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary27.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page27"), Show ("day3_diary_page26")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page27"), Show ("day3_diary_page28")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page28:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary28.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page28"), Show ("day3_diary_page27")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page28"), Show ("day3_diary_page29")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page29:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary29.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page29"), Show ("day3_diary_page28")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page29"), Show ("day3_diary_page30")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page30:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary30.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page30"), Show ("day3_diary_page29")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page30"), Show ("day3_diary_page31")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page31:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary31.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page31"), Show ("day3_diary_page30")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page31"), Show ("day3_diary_page32")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page32:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary32.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page32"), Show ("day3_diary_page31")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page32"), Show ("day3_diary_page33")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page33:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary33.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page33"), Show ("day3_diary_page32")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page33"), Show ("day3_diary_page34")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page34:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary34.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page34"), Show ("day3_diary_page33")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page34"), Show ("day3_diary_page35")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page35:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary35.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page35"), Show ("day3_diary_page34")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page35"), Show ("day3_diary_page36")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page36:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary36.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page36"), Show ("day3_diary_page35")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page36"), Show ("day3_diary_page37")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page37:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary37.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page37"), Show ("day3_diary_page36")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page37"), Show ("day3_diary_page38")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page38:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary38.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page38"), Show ("day3_diary_page37")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page38"), Show ("day3_diary_page39")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page39:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary39.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page39"), Show ("day3_diary_page38")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page39"), Show ("day3_diary_page40")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen day3_diary_page40:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary40.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page40"), Show ("day3_diary_page39")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page40"), Show ("day3_diary_page41")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page41:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary41.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page41"), Show ("day3_diary_page40")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page41"), Show ("day3_diary_page42")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page42:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary42.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page42"), Show ("day3_diary_page41")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page42"), Show ("day3_diary_page43")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")

screen day3_diary_page43:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary43.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page43"), Show ("day3_diary_page42")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page43"), Show ("day3_diary_page44")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")


screen day3_diary_page44:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary44.webp"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page44"), Show ("day3_diary_page43")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page44"), Jump ("day8")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")








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

    show screen prolog_diary_page with fade
    
    pause (10000000000)




































