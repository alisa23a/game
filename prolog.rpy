screen prolog_diary:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary1.jpg"
        idle "gui/dnav1idle.png"
        hover "gui/dnav1hover.png"
        
        hotspot(1784,464,112,152) action Hide ("prolog_diary"), Jump ("prolog_diary2")
        hotspot(1787,37,85,84) action Hide ("prolog_diary"), Show ("info_stand")

screen prolog_diary2:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary2.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary2"), Jump ("prolog_diary")
        hotspot(1784,464,112,152) action Hide ("prolog_diary2"), Jump ("prolog_diary3")
        hotspot(1787,37,85,84) action Hide ("prolog_diary2"), Show ("info_stand")

screen prolog_diary3:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary3.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary3"), Jump ("prolog_diary2")
        hotspot(1784,464,112,152) action Hide ("prolog_diary3"), Jump ("prolog_diary4")
        hotspot(1787,37,85,84) action Hide ("prolog_diary3"), Show ("info_stand")

screen prolog_diary4:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary4.jpg"
        idle "gui/diary4i.png"
        hover "gui/diary4h.png"
        
        hotspot(1040,277,685,384) action Hide ("prolog_diary4"), Jump ("prolog_diary4pic")
        hotspot(24,464,112,152) action Hide ("prolog_diary4"), Jump ("prolog_diary3")
        hotspot(1784,464,112,152) action Hide ("prolog_diary4"), Jump ("prolog_diary5")
        hotspot(1787,37,85,84) action Hide ("prolog_diary4"), Show ("info_stand")

screen prolog_diary5:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary5.jpg"
        idle "gui/diary5i.png"
        hover "gui/diary5h.png"
        
        hotspot(176,149,682,685) action Hide ("prolog_diary5"), Jump ("prolog_diary5pic")
        hotspot(24,464,112,152) action Hide ("prolog_diary5"), Jump ("prolog_diary4")
        hotspot(1784,464,112,152) action Hide ("prolog_diary5"), Jump ("prolog_diary6")
        hotspot(1787,37,85,84) action Hide ("prolog_diary5"), Show ("info_stand")    

screen prolog_diary6:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary6.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary6"), Jump ("prolog_diary5")
        hotspot(1784,464,112,152) action Hide ("prolog_diary6"), Jump ("prolog_diary7")
        hotspot(1787,37,85,84) action Hide ("prolog_diary6"), Show ("info_stand")

screen prolog_diary7:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary7.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary7"), Jump ("prolog_diary6")
        hotspot(1784,464,112,152) action Hide ("prolog_diary7"), Jump ("prolog_diary8")
        hotspot(1787,37,85,84) action Hide ("prolog_diary7"), Show ("info_stand")

screen prolog_diary8:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary8.jpg"
        idle "gui/diary8i.png"
        hover "gui/diary8h.png"
        
        hotspot(1061,465,612,332) action Hide ("prolog_diary8"), Jump ("prolog_diary8pic")
        hotspot(24,464,112,152) action Hide ("prolog_diary8"), Jump ("prolog_diary7")
        hotspot(1784,464,112,152) action Hide ("prolog_diary8"), Jump ("prolog_diary9")
        hotspot(1787,37,85,84) action Hide ("prolog_diary8"), Show ("info_stand")

screen prolog_diary8picsc:
    tag menu
    zorder 110
    modal True
    
    imagemap:
        ground "images/prolog/boat.jpg"
        idle "gui/dnav0idle.png"
        hover "gui/dnav0hover.png"
        
        hotspot(1787,37,85,84) action Hide ("prolog_diary8picsc"), Jump ("prolog_diary8")

screen prolog_diary9:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary9.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary9"), Jump ("prolog_diary8")
        hotspot(1784,464,112,152) action Hide ("prolog_diary9"), Jump ("prolog_diary10")
        hotspot(1787,37,85,84) action Hide ("prolog_diary9"), Show ("info_stand")

screen prolog_diary10:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary10.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("prolog_diary10"), Jump ("prolog_diary9")
        hotspot(1784,464,112,152) action Hide ("prolog_diary10"), Jump ("day2_diary11")
        hotspot(1787,37,85,84) action Hide ("prolog_diary10"), Show ("info_stand")

label prolog:

    scene bg room

    menu:
        "Видео пролога":
            jump prolog1
        "Пролог":
            jump prolog_diary

return

label prolog1:
    #e "prolog1"
    $ renpy.movie_cutscene("videos/prolog.ogv") #команда для запуска видео на весь экран
return

label prolog_diary:
    show screen prolog_diary
    jump start
    return

label prolog_diary2:
    show screen prolog_diary2
    jump start
    return

label prolog_diary3:
    show screen prolog_diary3
    jump start
    return

label prolog_diary4:
    if musicstop:
        play music track1

    show screen prolog_diary4
    jump start
    return

label prolog_diary4pic:
    show p_dream
    play music dreams
    ""
    hide p_dream
    stop music
    $ musicstop = True
    jump prolog_diary4
    return

label prolog_diary5:
    show screen prolog_diary5
    jump start
    return

label prolog_diary5pic:
    show p_house
    ""
    hide p_house
    jump prolog_diary5
    return

label prolog_diary6:
    show screen prolog_diary6
    jump start
    return

label prolog_diary7:
    show screen prolog_diary7
    jump start
    return

label prolog_diary8:
    show screen prolog_diary8
    jump start
    return

label prolog_diary8pic:
    call screen prolog_diary8picsc
    jump prolog_diary8
    return

label prolog_diary9:
    show screen prolog_diary9
    jump start
    return

label prolog_diary10:
    show screen prolog_diary10
    jump start
    return
return
