#Экран карты и разметка костров
screen map:
    #tag menu
    #modal True запрещает взаимодействие с другими объектами под этим экраном
    modal True
    #порядок отображения экрана(слой)
    zorder 300


    fixed:
        xsize 1920 ysize 1080
        add "images/bg/wmap.webp" align (.5,.5)

    fixed:
        xsize 1920 ysize 1080

        imagebutton:
            xpos 1856 ypos 11
            idle "gui/closebut_idle.png"
            hover "gui/closebut_hover.png"
            action Hide ("map"), Show ("info_stand")

        if gm1:
            button:
                xpos 519 ypos 505
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("nbeach")

        if gm2:
            button:
                xpos 612 ypos 394
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("gog")
        
        if gm3:
            button:
                xpos 828 ypos 313
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("smg")
        
        if gm4:
            button:    
                xpos 973 ypos 180
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("disland")
        
        if gm5:
            button:    
                xpos 657 ypos 90
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("lakedeep")
        
        if gm6:
            button:    
                xpos 147 ypos 155
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("uhouse")
        
        if gm7:
            button:    
                xpos 1042 ypos 605
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("newtcreek")
        
        if gm8:
            button:
                xpos 908 ypos 562
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("thiefpath")
        
        if gm9:
            button:
                xpos 840 ypos 765
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("swamp")
        
        if gm10:
            button:
                xpos 1222 ypos 325
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("boat_station")
        
        if gm11:
            button:
                xpos 1450 ypos 245
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("fbeach")
        
        if gm12:
            button:
                xpos 1303 ypos 600
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("mcity")
        
        if gm13:
            button:
                xpos 1333 ypos 510
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("dpeak")
        
        if gm14:
            button:    
                xpos 773 ypos 250
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("ushallow")
        
        if gm15:
            button:    
                xpos 1430 ypos 180
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("shpi")
        
        if gm16:
            button:
                xpos 1580 ypos 328
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("cave")
        
        if gm17:
            button:
                xpos 1638 ypos 620
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                #focus_mask кнопка нажимается только по видимым пикселям
                focus_mask True
                action Hide ("map"), Show ("moсr")
        
        if gm18:
            button:
                xpos 990 ypos 545
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                #focus_mask кнопка нажимается только по видимым пикселям
                focus_mask True
                action Hide ("map"), Show ("opine")
        
        if gm19:
            button:    
                xpos 1096 ypos 857
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("laboratory")
        
        if gm20:
            button:
                xpos 1029 ypos 660
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("oldroad")
        
        if gm21:
            button:
                xpos 1711 ypos 513
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("tcc")
        
        if gm22:
            button:    
                xpos 1238 ypos 65
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("goldd")
        
        if gm23:
            button:    
                xpos 705 ypos 805
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("busstop")
        
        if gm24:
            button:
                xpos 250 ypos 200
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("oldcamp")
        
        if gm25:
            button:
                xpos 1052 ypos 82
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("bravepath")
        
        if gm26:
            button:    
                xpos 1530 ypos 97
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("wilderness")
        
        if gm27:
            button:    
                xpos 1497 ypos 571
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("roadtn")
        
        if gm28:
            button:    
                xpos 1107 ypos 170
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pibuh")
        
        if gm29:
            button:
                xpos 1334 ypos 920
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("oldmine")
        
        if gm30:
            button:    
                xpos 296 ypos 940
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("tuni")
        
        if gm31:
            button:    
                xpos 156 ypos 977
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("tuno")
        
        if gm32:
            button:    
                xpos 298 ypos 372
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("reeds")
        
        if gm33:
            button:    
                xpos 422 ypos 340
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("iford")
        
        if gm34:
            button:    
                xpos 1435 ypos 877
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("caroad")
        
        if gm35:
            button:    
                xpos 1688 ypos 968
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("carier")
        
        if gm36:
            button:    
                xpos 1557 ypos 896
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("zdm")
        
        if gm37:
            button:    
                xpos 165 ypos 552
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("ford")
        
        if gm38:
            button:    
                xpos 927 ypos 612
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("ford2")
        
        if gm39:
            button:    
                xpos 590 ypos 553
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("ford3")
        
        if gm40:
            button:    
                xpos 256 ypos 698
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pointers")
        
        if gm41:
            button:    
                xpos 992 ypos 790
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("plane")
        
        if gm42:
            button:    
                xpos 367 ypos 570
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("crsh")
        
        if gm43:
            button:    
                xpos 1643 ypos 165
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("rapids")
        
        if gm44:
            button:    
                xpos 1232 ypos 482
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("hetu")
        
        if gm45:
            button:    
                xpos 327 ypos 147
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("jusu")
        
        if gm46:
            button:    
                xpos 857 ypos 99
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pbc")
        
        if gm47:
            button:    
                xpos 447 ypos 250
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("dnest")
        
        if gm48:
            button:    
                xpos 629 ypos 199
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("shouse")
        
        if gm49:
            button:
                xpos 165 ypos 82
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("crystalspring")
        
        if gm50:
            button:
                xpos 1399 ypos 566
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("mine")
        
        if gm51:
            button:
                xpos 1491 ypos 671
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("oldclock")
        
        if gm52:
            button:
                xpos 1409 ypos 737
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("oldcem")
        
        if gm53:
            button:
                xpos 1269 ypos 144
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("shallow")

        if gm54:
            button:
                xpos 474 ypos 722
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("campmap")
        
        if gm55:
            button:
                xpos 1442 ypos 393
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("lyhouse")
        
        if gm56:
            button:
                xpos 546 ypos 960
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("deroad")
        
        if gm57:
            button:
                xpos 1700 ypos 304
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("wdgorge")
                
        if gm58:
            button:
                xpos 722 ypos 280
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("dwhir")
                
        if gm59:
            button:
                xpos 414 ypos 945
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pot")

        if gm60:
            button:
                xpos 1034 ypos 238
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pfis")
        
        if gm61:
            button:
                xpos 1741 ypos 583
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("ogm")
        
        if gm62:
            button:
                xpos 1252 ypos 241
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("tbo")
        
        if gm63:
            button:
                xpos 472 ypos 58
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("pdl")
                
        if gm64:
            button:
                xpos 1057 ypos 907
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("spa")
                
        if gm65:
            button:
                xpos 843 ypos 889
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("rail")

        if gm66:
            button:
                xpos 350 ypos 610
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("aulane")

        if gm67:
            button:
                xpos 120 ypos 590
                xsize 27 ysize 37
                idle_background "images/fire.png"
                hover_foreground "images/fireh.png"
                focus_mask True
                action Hide ("map"), Show ("misemhidenbeach")