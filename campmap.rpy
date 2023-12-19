#экран карты лагеря
screen campmap:
    tag menu
    zorder 100
    modal True
    
    imagemap:
        ground "images/bg/campidle.png"
        idle "images/bg/campidle.png"
        hover "images/bg/camphover.png"
        
        if cm1:
            hotspot(147,251,149,66) action Hide ("campmap"), Jump ("mus")
        if cm2:
            hotspot(286,327,99,53) action Hide ("campmap"), Jump ("atsuroom")
        if cm3:
            hotspot(356,255,89,37) action Hide ("campmap"), Jump ("showers")
        if cm4:
            hotspot(215,477,101,59) action Hide ("campmap"), Jump ("zcloset")
        if cm5:
            hotspot(331,441,151,55) action Hide ("campmap"), Jump ("diroom")
        if cm6:
            hotspot(394,568,182,47) action Hide ("campmap"), Jump ("library")
        if cm7:
            hotspot(445,644,175,49) action Hide ("campmap"), Jump ("medic")
        if cm8:
            hotspot(453,752,212,45) action Hide ("campmap"), Jump ("viroom")
        if cm9:
            hotspot(520,859,259,93) action Hide ("campmap"), Jump ("odhouse")
        if cm10:
            hotspot(593,965,149,61) action Hide ("campmap"), Jump ("msecret")
        if cm11:
            hotspot(902,911,119,46) action Hide ("campmap"), Jump ("secret1")
        if cm12:
            hotspot(947,383,87,31) action Hide ("campmap"), Jump ("genda")
        if cm13:
            hotspot(950,516,112,49) action Hide ("campmap"), Jump ("square")
        if cm14:
            hotspot(952,668,238,90) action Hide ("campmap"), Jump ("lmhouse")
        if cm15:
            hotspot(1180,360,151,43) action Hide ("campmap"), Jump ("dining")
        if cm16:
            hotspot(453,214,95,57) action Hide ("campmap"), Jump ("watchcloset")
        if cm17:
            hotspot(499,291,83,34) action Hide ("campmap"), Jump ("stock")
        if cm18:
            hotspot(592,81,174,62) action Hide ("campmap"), Jump ("busstop")
        if cm19:
            hotspot(657,214,109,68) action Hide ("campmap"), Jump ("stand")
        if cm20:
            hotspot(767,182,108,65) action Hide ("campmap"), Jump ("secret4")
        if cm21:
            hotspot(917,58,106,42) action Hide ("campmap"), Jump ("bombu")
        if cm22:
            hotspot(615,310,125,37) action Hide ("campmap"), Jump ("stadium")
        if cm23:
            hotspot(661,388,137,46) action Hide ("campmap"), Jump ("stage")
        if cm24:
            hotspot(1057,99,198,68) action Hide ("campmap"), Jump ("handmade")
        if cm25:
            hotspot(1258,135,169,53) action Hide ("campmap"), Jump ("gteach")
        if cm26:
            hotspot(1070,268,127,36) action Hide ("campmap"), Jump ("fotoc")
        if cm27:
            hotspot(1295,284,215,58) action Hide ("campmap"), Jump ("kroof")
        if cm28:
            hotspot(1234,526,211,65) action Hide ("campmap"), Jump ("szhhouse")
        if cm29:
            hotspot(1210,753,107,40) action Hide ("campmap"), Jump ("secret2")
        if cm30:
            hotspot(1479,589,109,40) action Hide ("campmap"), Jump ("secret3")
        if cm31:
            hotspot(1243,627,165,101) action Hide ("campmap"), Jump ("shande")
        if cm32:
            hotspot(1521,280,132,53) action Hide ("campmap"), Jump ("stels")
        if cm33:
            hotspot(1555,345,195,107) action Hide ("campmap"), Jump ("attic")
        if cm34:
            hotspot(1483,495,216,69) action Hide ("campmap"), Jump ("auhouse")
        if cm35:
            hotspot(1702,97,198,180) action Hide ("campmap"), Jump ("pointers")
        if cm36:
            hotspot(775,78,106,57) action Hide ("campmap"), Jump ("tirhands")
        if cm37:
            hotspot(213,221,132,29) action Hide ("campmap"), Jump ("peep1")
        if cm38:
            hotspot(48,417,150,38) action Hide ("campmap"), Jump ("peep2")
        if cm39:
            hotspot(386,378,153,32) action Hide ("campmap"), Jump ("peep3")
        if cm40:
            hotspot(127,185,167,33) action Hide ("campmap"), Jump ("peep4")
        if cm41:
            hotspot(298,833,180,35) action Hide ("campmap"), Jump ("peep5")
        if cm42:
            hotspot(205,735,163,31) action Hide ("campmap"), Jump ("peep6")
        if cm43:
            hotspot(331,887,112,38) action Hide ("campmap"), Jump ("secret7")
        if cm44:
            hotspot(421,336,193,34) action Hide ("campmap"), Jump ("sroom")

# Локации лагеря
label mus:
    scene bg mus with dissolve
    "Музыкальный и хореографический кружок"
    call screen campmap
    return
    
label atsuroom:
    scene bg atsuroom with dissolve
    "Комната Атсуи"
    scene bg atsuroom2 with dissolve
    "Комната Атсуи2"
    call screen campmap
    return
    
label showers:
    scene bg showers with dissolve
    "Душевые"
    scene bg showers2 with dissolve
    "Душевые2"
    call screen campmap
    return
    
label zcloset:
    scene bg zcloset with dissolve
    "Каморка Жени"
    scene bg zcloset2 with dissolve
    "Каморка Жени2"
    call screen campmap
    return
    
label diroom:
    scene bg diroom with dissolve
    "Комната директрисы"
    call screen campmap
    return
    
label library:
    scene bg library with dissolve
    "Библиотека"
    scene bg library2 with dissolve
    "Библиотека2"
    call screen campmap
    return
    
label medic:
    scene bg medic with dissolve
    "Медпункт"
    call screen campmap
    return
    
label viroom:
    scene bg viroom with dissolve
    "Комната Виолы"
    call screen campmap
    return
    
label odhouse:
    scene bg odhouse with dissolve
    "Домик ОД и Семёна"
    scene bg odhouse2 with dissolve
    "Комната ОД"
    scene bg odhouse3 with dissolve
    "Комната Семёна"
    call screen campmap
    return
    
label msecret:
    scene bg msecret with dissolve
    "Чердак меганычка"
    scene bg msecret2 with dissolve
    "Чердак меганычка2"
    call screen campmap
    return
    
label secret1:
    scene bg secret1 with dissolve
    "Нычка 1"
    call screen campmap
    return
    
label genda:
    scene bg genda with dissolve
    "Генда"
    call screen campmap
    return
    
label square:
    scene bg square with dissolve
    "Площадь"
    call screen campmap
    return
    
label lmhouse:
    scene bg lmhouse with dissolve
    "Домик Лены и Мику"
    scene bg lmhouse2 with dissolve
    "Домик Лены и Мику2"
    call screen campmap
    return
    
label dining:
    scene bg dining with dissolve
    "Столовая"
    call screen campmap
    return
    
label watchcloset:
    scene bg watchcloset with dissolve
    "Каморка сторожа"
    call screen campmap
    return
    
label stock:
    scene bg stock with dissolve
    "Склад"
    scene bg stock2 with dissolve
    "Склад2"
    call screen campmap
    return
    
label busstop:
    scene bg busstop with dissolve
    "Центральный вход. Автобус 410"
    scene bg busstop2 with dissolve
    "Центральный вход. Автобус 410 2"
    scene bg busstop3 with dissolve
    "Центральный вход. Автобус 410 3"
    scene bg busstop4 with dissolve
    "Центральный вход. Автобус 410 4"
    call screen campmap
    return
    
label stand:
    scene bg stand with dissolve
    "Cтенд. Рассписание"
    call screen campmap
    return
    
label secret4:
    scene bg secret4 with dissolve
    "Нычка 4. Гитара"
    call screen campmap
    return
    
label bombu:
    scene bg bombu with dissolve
    "Вход в бомбоубежище"
    scene bg bombu2 with dissolve
    "Вход в бомбоубежище2"
    call screen campmap
    return
    
label stadium:
    scene bg stadium with dissolve
    "Стадион"
    scene bg stadium2 with dissolve
    "Стадион2"
    call screen campmap
    return
    
label stage:
    scene bg stage with dissolve
    "Эстрада"
    scene bg stage2 with dissolve
    "Эстрада2"
    call screen campmap
    return
    
label handmade:
    scene bg handmade with dissolve
    'Кружок "Умелые руки"'
    call screen campmap
    return
    
label gteach:
    scene bg gteach with dissolve
    "Комната физрука и завхоза"
    call screen campmap
    return
    
label fotoc:
    scene bg fotoc with dissolve
    "Фотостудия"
    call screen campmap
    return
    
label kroof:
    scene bg kroof with dissolve
    "Крыша на которой удобно целоваться"
    call screen campmap
    return
    
label szhhouse:
    scene bg szhhouse with dissolve
    "Домик Слави и Жени"
    call screen campmap
    return
    
label secret2:
    scene bg secret2 with dissolve
    "Нычка 2"
    call screen campmap
    return
    
label secret3:
    scene bg secret3 with dissolve
    "Нычка 3"
    call screen campmap
    
label shande:
    scene bg shande with dissolve
    "2 этаж. Шурик и Электроник"
    call screen campmap
    return
    
label stels:
    scene bg stels with dissolve
    "Лазейка. Уйти незаметно."
    call screen campmap
    return
    
label attic:
    scene bg attic with dissolve
    "Чердак. Лучшая нычка для курения и игры в карты."
    call screen campmap
    return
    
label auhouse:
    scene bg auhouse with dissolve
    "Домик Алисы и Ульяны."
    scene bg auhouse2 with dissolve
    "Домик Алисы и Ульяны2."
    call screen campmap
    return
    
label pointers:
    scene bg pointers with dissolve
    "Тропинка. Указатели."
    call screen map
    return
    
label tirhands:
    scene bg tirhands with dissolve
    "Кружок Усталые ручки"
    scene bg tirhands2 with dissolve
    "Кружок Усталые ручки2"
    call screen campmap
    return
    
label peep1:
    scene bg peep1 with dissolve
    "Подглядывать 1"
    call screen campmap
    return
    
label peep2:
    scene bg peep2 with dissolve
    "Подглядывать 2"
    call screen campmap
    return
    
label peep3:
    scene bg peep3 with dissolve
    "Подглядывать 3"
    scene bg peep32 with dissolve
    "Подглядывать 3 2"
    call screen campmap
    return
    
label peep4:
    scene bg peep4 with dissolve
    "Подглядывать 4"
    call screen campmap
    return
    
label peep5:
    scene bg peep5 with dissolve
    "Подглядывать 5"
    call screen campmap
    return
    
label peep6:
    scene bg peep6 with dissolve
    "Подглядывать 6"
    call screen campmap
    return
    
label secret7:
    scene bg secret7 with dissolve
    "Нычка 7"
    scene bg secret72 with dissolve
    "Нычка 7 2"
    call screen campmap
    return
    
label sroom:
    scene bg sroom with dissolve
    "Комната саманты"
    call screen campmap
    return