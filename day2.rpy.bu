screen day2_diary11:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary11.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
 
        hotspot(24,464,112,152) action Hide ("day2_diary11"), Show ("prolog_diary10") 
        hotspot(1784,464,112,152) action Hide ("day2_diary11"), Show ("day2_diary12")
        hotspot(1787,37,85,84) action Hide ("day2_diary11"), Show ("info_stand")

screen day2_diary12:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary12.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary12"), Show ("day2_diary11")
        hotspot(1784,464,112,152) action Hide ("day2_diary12"), Show ("day2_diary13")
        hotspot(1787,37,85,84) action Hide ("day2_diary12"), Show ("info_stand")

screen day2_diary13:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary13.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary13"), Show ("day2_diary12")
        hotspot(1784,464,112,152) action Hide ("day2_diary13"), Show ("day2_diary13choice")
        hotspot(1787,37,85,84) action Hide ("day2_diary13"), Show ("info_stand")

screen day2_diary13choice:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary13choice.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary13choice"), Show ("day2_diary13")
        hotspot(1784,464,112,152) action Hide ("day2_diary13choice"), Show ("day2_diary14")
        hotspot(1787,37,85,84) action Hide ("day2_diary13choice"), Show ("info_stand")

screen day2_diary14:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/diary/diary14.jpg"
        idle "gui/dnav3idle.png"
        hover "gui/dnav3hover.png"
        
        hotspot(24,464,112,152) action Hide ("day2_diary14"), Show ("day2_diary13choice")
        hotspot(1784,464,112,152) action Hide ("day2_diary14"), Show ("day3_diary15")
        hotspot(1787,37,85,84) action Hide ("day2_diary14"), Show ("info_stand")

label day2:
    "День 2"
    jump day2_diary11
return

label day2_diary11:
    show screen day2_diary11
    jump start
    return

label day2_diary12:
    show screen day2_diary12
    jump start
    return

label day2_diary13:
    show screen day2_diary13
    jump start
    return

label day2_diary13choice:
    show screen day2_diary13choice
    jump start
    return

label day2_diary14:
    show screen day2_diary14
    jump start
    return