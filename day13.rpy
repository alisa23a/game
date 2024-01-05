label day13:

    $ days = 13

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music


    play music "audio/music/z_199.mp3"

    scene bg camp_artifacts

    "Идея игры в карты принадлежала Алисе. Она же определила место."

    "У каждого домика лагеря был закрытый чердак. Чердак этот был полноценной комнатой  и использовался лишь в случаях, когда количество пионеров  было больше ожидаемого."

    "Но те времена давно прошли и чердаки были заботливо заколочены Петровичем по заданию завхоза, а на двери повешены  замки. Был такой чердак и над нашей комнатой."

    "Я прознала, где Петрович держит ключи от всех чердаков лагеря, благо входить к нему в каморку девочкам разрешалось в любое время."


    scene bg watchmans_cabin_2

    "Оставалось выяснить, какой из почти тридцати ключей был именно от чердака нашего домика. Однако долго искать не пришлось."

    "Будучи аккуратистом по натуре, Петрович снабдил каждый ключ ярлычком из приклеенного к веревочке медицинского пластыря с написанным на нём номером домика. Это было очень кстати."

    "Мы прокрались в каморку. Но ярлычка с нужным номером, т.е. ключа от нашего чердака, там не было. Мы решили, что ключ находиться на связке, которую Петрович носит с собой."


    scene an_d13_02_bg

    "Мы знали, что он частенько любит подремать на лавочке . Иногда ключи  почти  падали с его руки  и можно было их умыкнуть, пока он спит. Но спал он чутко. Эту ответственейшую операцию, было поручено провернуть мне. "

    scene black with fade

    stop music

    jump key_theft_1

return



image stealthekey:

    "images/an/an13day/an_d13_14.png" with Dissolve(0.5, alpha=True)
    pause 0.5
    "images/an/an13day/an_d13_16.png" with Dissolve(0.5, alpha=True)
    pause 0.5

    repeat

############################################
## Экраны на которых нужно кликать на ключ - модальные. На которых реакция Петровича - не модальные, клик в любом месте экрана сразу переводит на лейбл, а там стоит жёсткая пауза перед скрытием текущего экрана

screen key_theft_1():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0)   

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_2")


screen key_theft_2():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_09.png" pos (0, 0)


screen key_theft_3():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_4")


screen key_theft_4():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_10.png" pos (0, 0)

screen key_theft_5():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_6")


screen key_theft_6():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_11.png" pos (0, 0)


screen key_theft_7():

    modal True

    add "images/an/an13day/an_d13_02_bg.webp"

    add "stealthekey" pos (0, 0) 

    imagebutton:
        xpos 993 ypos 716
        xsize 110 ysize 110
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Jump("key_theft_8")


screen key_theft_8():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_12.png" pos (0, 0)


screen key_theft_9():

    add "images/an/an13day/an_d13_02_bg.webp"

    add "images/an/an13day/an_d13_12.png" pos (0, 0)

    add "images/an/an13day/an_d13_17.png" pos (0, 0)


label key_theft_1:
    
    play music "audio/music/z_200.mp3"

    show screen key_theft_1 with fade

    $ show_quick_menu = False

    pause (1000000000000000000000.0)

label key_theft_2:

    hide screen key_theft_1

    show screen key_theft_2

    jump key_theft_3

label key_theft_3:

    $ renpy.pause(3.0, hard=True)

    hide screen key_theft_2

    show screen key_theft_3

    pause (1000000000000000000000.0)

label key_theft_4:

    hide screen key_theft_3

    show screen key_theft_4

    jump key_theft_5

label key_theft_5:

    $ renpy.pause(3.0, hard=True)

    hide screen key_theft_4

    show screen key_theft_5

    pause (1000000000000000000000.0)

label key_theft_6:

    hide screen key_theft_5

    show screen key_theft_6

    jump key_theft_7

label key_theft_7:

    $ renpy.pause(2.0, hard=True)

    hide screen key_theft_6

    show screen key_theft_7

    pause (1000000000000000000000.0)

label key_theft_8:

    hide screen key_theft_7

    show screen key_theft_8

    $ renpy.pause(1.0, hard=True)

    hide screen key_theft_8

    show screen key_theft_9

    $ renpy.pause(2.0, hard=True)

    hide screen key_theft_9

    jump day13_2


label day13_2:

    $ inv_item_28 = True

    $ show_quick_menu = True

    stop music

    play music "audio/music/z_089.mp3"

    scene bg attic_inside with dissolve

    "Наконец мы попали в заветное помещение. Там царили паутина, пыль и летучая мышь. Мышь решили не трогать, она стала символом Чердака и его талисманом. От остального безжалостно избавились."

    "Засучив рукава, мы с Алисой трудились все свободное от лагерного расписания время, и наконец, «номер нашей гостиницы», как его назвала Алиса, был готов."

    "Вскоре весь отряд собрался наверху."



    image an_13_01: #Анимация Ульяна карты

        "images/an/an13day/an_d13_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an13day/an_d13_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat 


    stop music

    play music "audio/music/z_201.mp3"

    scene an_d13_01_bg with dissolve

    show an_13_01

    pause (10000000000000000000000.0)


    scene bg attic_inside with dissolve

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sl "А это законно, девочки?"

    hide sp_sl_001

    show sp_le_006:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "Ясенева!"

    hide sp_le_006

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Какая разница? Кто узнает, если ты не скажешь?"

    hide sp_al_005

    show sp_je_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Офигеть! Это мечта. Я сделаю тут филиал библиотеки, перетащу в него запретку из спецхрана."

    hide sp_je_013

    show sp_mi_012:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    mi "И уроки на гитаре будем  устраивать, а главное – квартирники!"

    hide sp_mi_012

    show sp_at_004:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ats "Ой девочки, а на чем мы будем сидеть? Тут только один стул! И стол..."

    hide sp_at_004

    show sp_sam_010:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "Я понимать что, как это по русски... (подыскивает слова) эээ, революшен... нелегаль?"

    hide sp_sam_010

    show sp_sem_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Легаль, легаль. Только об этом никому говорить не стоит. Это, Сэмми, по-вашему – андеграунд."

    hide sp_sem_001

    show sp_sam_004:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "(Подпрыгивая и хлопая в ладоши) \nО, я понимать! Рашен андеграунд! Мне нравится!"

    hide sp_sam_004

    show sp_at_004:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ats "Так как насчет стульев?"

    hide sp_at_004

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ul "Фигня вопрос! Сейчас физрук в карантине, у Петровича есть дубликат ключей от бытовки и раздевалки."

    ul "Стащим физруковский диван и скажем, что так и было. С других чердаков по стулу скоммуниздим и «вуаля», как говорит Женя. Вот и мебель."

    hide sp_ul_014

    show sp_le_006:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "(Ухмыляясь и глядя на Алису) \nДа-а... Кто-то скоренько наладит тут личную жизнь."

    hide sp_le_006

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "На себя посмотри. Ты первая в очереди будешь на ключ."

    hide sp_al_005

    show sp_al_003:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да, Семен? \n(хитро подмигивает)"

    hide sp_al_003

    show sp_sem_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Не ссорьтесь, девочки. Диван нужен всем. И не в том смысле, а чтобы сидеть. Ну и вообще, комфорт минимальный все-таки нужен. Диван облагородит помещение. Что с картами?"

    hide sp_sem_001

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это я беру на себя."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "И чтобы на вечеринках было вкусненькое! Заготовку вкусняшек, думаю, надо поручить Саманте. Ей никогда не откажут."

    ul "И в поселок за конфетами пусть переводчицу... эту, Мегги пусть пошлет. Что она тут порожняком у нас проживается? Польза какая-никакая будет. Мой папа сказал бы «С худой овцы хоть шерсти клок»."

    hide sp_ul_012

    show sp_sam_004:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sam "(Смеясь) \nОвца, овца! Я сказать Мегги!"

    hide sp_sam_004

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Ну ты и хитрющая, Ленина! Откуда в тебе это?"

    hide sp_je_001

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Она у нас главный следопыт и следователь по особо важным делам!"

    hide sp_ul_012
 
    hide sp_al_005

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "А меня в игру берете?"

    hide sp_tol_001

    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Ты чё, братан?! Даже не сомневайся. Мы же команда!"

    hide sp_shu_001

    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Да!"

    hide sp_el_001

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "А я бы кибернетикам ключа не давала, мало ли. Превратят нашу нычку в филиал кружка «Умелые руки». Знаю я их. Натаскают всяких железок и поминай, как звали, уют и порядок... Нет уж."

    sl "Кстати, насчет порядка. Кто по щелям будет выметать?"

    hide sp_sl_001
 
    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "У кого ключ, тот и убирает за собой!"

    hide sp_el_001

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Логично. Я проверю!"

    hide sp_sl_001

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Объявляю операцию «Диван». Тащить будем ночью. Тут сила нужна. Мальчики! Вы готовы?"
 
    hide sp_al_005

    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    guys "(Хором) \nВсегда готовы!"

    hide sp_el_001

    hide sp_shu_001

    hide sp_tol_001



    stop music

    play music "audio/music/z_102.mp3"   

    scene an_d10_01_bg with dissolve

    show an_10_01

    "После рассказов Петровича о подводном колоколе, мы с Алисой постоянно надоедали ему с просьбой поднять эту штуку, которую мы назвали между собой Батискаф."

    "И во наконец он согласился. Похоже, ему и самому хотелось. Просто вместе веселее."

    "К тому же, директриса дала добро (мы через ОД подкинули ей эту идею). Она сказала, если удастся поднять, как она выразилась, «эту ржавую бочку», Колокол станет объектом экскурсий для пионеров."

    "А через иллюминатор, можно будет разглядывать дно реки и всякую ихтиологическую живность. Что хорошо для общего развития пионеров. В общем, идея ей понравилась."

    "После обеда при помощи  первого отряда и Петровича, решено было начать подъем."


    stop music

    play music "audio/music/z_124.mp3" 

    scene bg bathyscaphe

    "К обеду все было готово. Петрович с Электроником и Шуриком , отбили ржавчину, смазали весь механизм, прикрепили трос."

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ну вот, лебедочка-то как новенькая. \n(довольно вытирая руки ветошью)"

    pe "Жаль, краска сошла. Помню, как привезли ее. Зеленая краска была. Вот еще надпись сохранилась. От тут... Читай внученька."

    hide sp_pe_005

    scene bg bathyscaphe4

    pause (10000000000000000000000.0)
    
    "Я прочитала вслух выдавленные на корпусе лебедки буквы: «Екатерининский завод»"

    scene bg bathyscaphe

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Механизмы значит, делали, Екатерининцы. Знаю их продукцию. А это у них, как сейчас говорят, заказной. Да... умели делать. А сейчас, пять лет и выкидывай железяку."

    pe "Ну что, крутанем? \n(в глазах старика заблестели так знакомые Ульяне по охоте на Сома искорки.)"

    hide sp_pe_005


    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2



    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "(Электроник с Шуриком в один голос) \nКрутанём!"

    hide sp_shu_001

    hide sp_el_001

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Еще как, крутанем!"

    hide sp_ul_012

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да, надо попробовать."
 
    hide sp_al_005

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "Как бы чего не вышло..."

    hide sp_tol_001

    show sp_sl_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Если нужна наша помощь, то мы, девочки нашего первого, краснознаменного, отряда... \n(она запнулась, подыскивая пафосное слово)"

    hide sp_sl_001

    show sp_le_004:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "(Исподлобья взглянув на Славю) \nТы не на митинге, Ясенева, лучше просто пусть скажет, что делать."

    hide sp_le_004

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Вот, сынки, становитесь так, чтобы у всех руки на рычаге были. Я как дам команду, вы начинайте. По часовой крутите. По часовой. Девчата пусть пока отдохнут. Мужское это дело."

    hide sp_pe_005
 
    "Шестеренки пришли в движение "

    "Точно по крику Петровича все налегли на рычаг лебедки. Трос, выбираясь, натянулся и послышался скрежет."

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Навались разом! Тут главное, колокол стронуть с места. Сильно его тиной занесло. А там пойдет, не остановишь!"

    hide sp_pe_005


    stop music

    play music "audio/music/z_206.mp3" 

    "Несмотря на протесты Петровича, все девочки кинулись помогать. Я споткнулась впопыхах и наверное упала бы с пристани, но зацепившись за коромысло, к которому был привязан противовес, повисла над водой."

    "Колесо с противовесом, медленно вращалось, поднимая меня все выше и выше."

    stop music

    play music "audio/music/z_205.mp3" 

    show sp_ul_037:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "А-а-а! Я высоты боюсь!"

    hide sp_ul_037

    "Я подтянулась и закрепилась ногами. Забравшись на самое коромысло крана-лебедки. Противовес шел вниз и я своим весом как бы помогала тянуть трос."

    stop music

    play music "audio/music/z_206.mp3" 

    "Все закричали: «Уходи оттуда! Отпускаем!» Но Петрович не дал отпустить рычаг."

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Всем держать! Если сейчас отпустить, то вес потянет всех назад. Беда будет. Тяните черти!"

    hide sp_pe_005


    stop music

    play music "audio/music/z_207.mp3" 

    scene bg bathyscaphe3

    "Наконец, противовес достиг высшей точки и остановился. С высоты коромысла я увидела весь лагерь и то, как колокол показался из воды и, медленно переворачиваясь, выпрямлялся."


    scene bg bathyscaphe

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Как станет торчком и наберет воздух, сразу станет легче и поплывет. Чертова железяка."

    pe "Тут уж вы не зевайте, ребятишки. Ты, белобрысый, сразу, как крикну, клин ставь вот в это отверстие. Стопори, значит, шестерни, а то не удержим. Там тонны две весу будет."

    hide sp_pe_005

    "Колокол вдруг вынырнул из воды и издал какой-то плюхающий звук."

    " Чпок!"

    stop music

    play music "audio/music/z_209.mp3" 

    "А я от неожиданности отпустила руки и полетела в воду."


    stop music

    play music "audio/music/z_208.mp3"


    "Хрясь!"

    stop music

    play music "audio/music/z_210.mp3" 

    scene an_d13_03_bg with dissolve

    "Вынырнув, я крикнула:"

    show sp_ul_036:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Живая, не волнуйтесь!"  

    hide sp_ul_036

    "И я гребками поплыла к огромному, как мне  показалось, куполу, колыхающемуся над водой. То, что я видела, было похоже на панцирь огромной железной черепахи. В моей груди все пело от восторга."

    "Я ухватилась за скобу рядом с иллюминатором, подтянулась и заглянула внутрь. Стекло было мутным от времени и прилипших снаружи водорослей."

    "В скобу люка был вставлен старый выцветший красный флажок. Такие используют моряки, чтобы передавать сообщения с корабля на корабль. Наверное, здесь он был нужен чтобы служить маяком для лодок."

    "Я взяла флажок и помахала им над головой. Но меня не видели."

    show sp_ul_036:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Тут есть лестница. Я щас."  

    hide sp_ul_036

    "Я вскарабкалась еще и скоро оказалась на вершине покачивающейся громадины. Течение тихо относило колокол к острову, берег удалялся. Это продолжалось до тех пор, пока трос не натянулся."

    "От неожиданности и сильного толчка я чуть не упала в воду. Однако удержалась, балансируя на одной ноге."


    image an_13_03: # Анимация Ульяна машет флажком
        

        # "images/an/an13day/an_d13_18.png" with Dissolve(0.5, alpha=True)
        # pause 0.2
        # "images/an/an13day/an_d13_19.png" with Dissolve(0.5, alpha=True)
        # pause 0.2
        "images/an/an13day/an_d13_20.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an13day/an_d13_21.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an13day/an_d13_22.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an13day/an_d13_23.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an13day/an_d13_24.png" with Dissolve(0.5, alpha=True)
        pause 0.2

  
        repeat



    scene an_d13_03_bg with dissolve

    show an_13_03

    "На берегу все закричали «Ура!»"

    "Ветер трепал мой флажок, как настоящее знамя. И я подумала: «Мое знамя видят». Я выпрямилась. Я снова впереди всех!"

    ul "Тяните!"

    "Я видела, как маленькие фигурки на пристани засуетились, трос напрягся и колокол медленно двинулся против течения. И я подумала: «Я как капитан крейсера Аврора. Жаль, что нет из чего пальнуть.»"

    "Для полноты счастья не хватало фейерверка."

    stop music

    play music "audio/music/z_102.mp3"   

    scene bg bathyscaphe2

    "Вот такая история. Так мы притащили батискаф. Он теперь  красуется рядом с пристанью. Физрук обещал сделать из него музей."

    "А мне страсть как хочется залезть внутрь. Это же штуковина, как «Наутилус» капитана Немо!"

    "Жаль, пока туда не пускают. Физрук не смог открыть ржавый замок. Но мы с Алисой уже выпросили у Петровича ножовку по металлу. И ночью... Ну вы поняли. Хе-хе."


    scene bg attic_inside


    # image je_el_sam composite = Composite(
        # (1920, 1080),
        # (1150, 0), "images/sp/el/sp_el_001.png",
        # (0, 0), "images/sp/sam/sp_sam_001.png",
        # (360, -120), "images/sp/cards/sp_cards_je_01.png")


    image je_el_sam composite = Composite(
        (13440, 1080),
        (1150, 0), "images/sp/el/sp_el_001.png",
        (0, 0), "images/sp/sam/sp_sam_001.png",
        (360, -120), "images/sp/cards/sp_cards_je_01.png",

        # (3070, 0), "images/sp/tol/sp_tol_001.png",
        # (1920, 0), "images/sp/at/sp_at_001.png",
        # (2280, -120), "images/sp/cards/sp_cards_al_01.png")

        (4990, 0), "images/sp/tol/sp_tol_001.png",
        (3840, 0), "images/sp/at/sp_at_001.png",
        (4200, -120), "images/sp/cards/sp_cards_al_01.png",


        (7580, 0), "images/sp/sl/sp_sl_001.png",
        (8780, 50), "images/sp/smu/sp_smu_001.png",
        (8040, -120), "images/sp/cards/sp_cards_sem_01.png",

        (12720, 0), "images/sp/shu/sp_shu_001.png",
        (11470, 0), "images/sp/mi/sp_mi_012.png",
        (11880, -120), "images/sp/cards/sp_cards_ul_02.png")



    transform loop_cars:
        xpos -13440
        linear 1.0 xpos -11520
        linear 0.5 xpos -11520  
        linear 2.0 xpos -7680
        linear 0.5 xpos -7680
        linear 2.0 xpos -3840
        linear 0.5 xpos -3840
        linear 2.0 xpos 0
        linear 0.5 xpos 0
        linear 1.0 xpos 1920
        #linear 1.0 xpos 3840


        
        # linear 1.0 xpos -5760
        # linear 1.0 xpos -5760
        # linear 1.0 xpos 0
        # linear 1.0 xpos 0
        # linear 1.0 xpos 5760
        # linear 1.0 xpos 5760
        # linear 1.0 xpos 9600
        #linear 1.0 xpos 1920
        #linear 1.0 xpos 3840


        repeat

    show je_el_sam composite at loop_cars

    # show je_el_sam composite with moveinleft
    # pause (1.0)
    # hide je_el_sam composite with moveoutright


    # image al_tol_at composite = Composite(
        # (1920, 1080),
        # (1150, 0), "images/sp/tol/sp_tol_001.png",
        # (0, 0), "images/sp/at/sp_at_001.png",
        # (360, -120), "images/sp/cards/sp_cards_al_01.png")

    # show al_tol_at composite with moveinleft
    # pause (1.0)
    # hide al_tol_at composite with moveoutright


    # image sem_sl_smu composite = Composite(
        # (1920, 1080),
        # (-100, 0), "images/sp/sl/sp_sl_001.png",
        # (1100, 50), "images/sp/smu/sp_smu_001.png",
        # (360, -120), "images/sp/cards/sp_cards_sem_01.png")

    # show sem_sl_smu composite with moveinleft
    # pause (1.0)
    # hide sem_sl_smu composite with moveoutright


    # image ul_shu_mi composite = Composite(
        # (1920, 1080),
        # (1200, 0), "images/sp/shu/sp_shu_001.png",
        # (-50, 0), "images/sp/mi/sp_mi_012.png",
        # (360, -120), "images/sp/cards/sp_cards_ul_02.png")

    # show ul_shu_mi composite with moveinleft
    # pause (1.0)
    # hide ul_shu_mi composite with moveoutright













    # show sp_el_001 with moveinleft:
        # yalign 0.0 subpixel True
        # xalign 1.0 subpixel True
        # zoom 1.2

    # show sp_sam_004 with moveinleft:
        # yalign 0.0 subpixel True
        # xalign 0.0 subpixel True
        # zoom 1.2

    
    # show sp_cards_je_01 with moveinleft:
        # yalign 0.98 subpixel True
        # xalign 0.5 subpixel True
        # zoom 1.0

    # #pause (0.5)
    # pause (10000000000000000000000000.0)

    # hide sp_el_001 with moveoutright
    # hide sp_sam_004 with moveoutright
    # hide sp_cards_je_01 with moveoutright









    # show sp_al_037 with moveinleft:
        # yalign 0.1 subpixel True
        # xalign 0.47 subpixel True
        # zoom 1.3

    # pause (0.5)

    # hide sp_al_037 with moveoutright



















    pause (10000000000000000000000.0)


    scene black with fade

    stop music

    #jump day14

return