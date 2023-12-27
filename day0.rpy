screen prolog_diary_page:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary1.jpg"
        idle "gui/dnav1idle.png"
        hover "gui/dnav1hover.png"
        
        hotspot(1784,464,112,152) action Hide ("prolog_diary_page"), Show ("prolog_diary_page2")
        #hotspot(1787,37,85,84) action Hide ("prolog_diary_page"), Show ("info_stand")

screen prolog_diary_page2:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary2.jpg"
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
        ground "images/diary/diary3.jpg"
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
        ground "images/diary/diary4.jpg"
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
        ground "images/diary/diary5.jpg"
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
        ground "images/diary/diary6.jpg"
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
        ground "images/diary/diary7.jpg"
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
        ground "images/diary/diary8.jpg"
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

    add "images/prolog/boat.jpg"
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
        ground "images/diary/diary9.jpg"
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
        ground "images/diary/diary10.jpg"
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
        ground "images/diary/diary11.jpg"
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
        ground "images/diary/diary12.jpg"
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
        ground "images/diary/diary13.jpg"
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
        ground "images/diary/diary13choice.jpg"
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
        ground "images/diary/diary14.jpg"
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
        ground "images/diary/diary15.jpg"
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
        ground "images/diary/diary16.jpg"
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
        ground "images/diary/diary17.jpg"
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
        ground "images/diary/diary18.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day3_diary_page18"), Show ("day3_diary_page17")
        hotspot(1784,464,112,152) action Hide ("day3_diary_page18"), Jump ("day8")
        #hotspot(1787,37,85,84) action Hide ("day3_diary_page18"), Show ("info_stand")










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




































