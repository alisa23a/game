label day21:

    $ days = 21

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music fadeout 1.0


    play music "audio/music/z_124.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Несколько дней я не вела дневник. Но зато, я писала в своей  тетрадке  ДЛЯ РАЗНЫХ МЫСЛЕЙ."


    scene cg thoughts_notebook_01 with dissolve

    "Вот  эта тетрадка, я украсила обложку рисунком совы. И еще деревья с дуплами, в которых  живут совята. Правда, красиво получилось?"

    pause (10000000000000000000000.0)

    "В нее я записала главные мысли, которые я думаю. А есть еще не главные, но тоже важные. Их потом запишу."

    "Эта тетрадка помогает мне, как говорит папа, «СОБРАТЬ МЫСЛИ В КУЧКУ». А это для репортера, особенно следователя, важнее всего."


    scene cg thoughts_notebook_03 with dissolve

    "Эти вопросы я обязательно задам СОВЕ."

    pause (10000000000000000000000.0)


    scene an_d10_01_bg with dissolve

    show an_10_01

    "Наконец-то состоялся наш первый поход с Ольгой Дмитриевной. О походе  хотела написать отдельно."

    "Но, случилось еще то, что мы нашли шифр к записям Семёна. И в его дневнике, этот поход описан как мне кажется, интереснее."

    "История с шифром была такая. Мы с Алисой заглянули в библиотеку, что бы отдать книги."

    "Но мы не стали рассказывать Жене о том, что увидели на кладбище и Ольге Дмитриевне не стали. Мы решили, что поднимется шум, а у нас нет доказательств."

    "К тому же нам влетело бы за то, что мы отсутствовали всю ночь и без спросу ходили на кладбище."


    scene bg library with dissolve

    "Мы отдали книги и когда уходили, Женя нас окликнула. "

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    je "Вы интересовались книгами, которые брал Семён. Он уже вернул книги, и если хотите, я дам их вам."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "Нет, не стоит, мы уже почитали те, что ты советовала. Так что..."

    ul "Стоп, не торопись, какие, ты говоришь, книги?"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Наверное, эти действительно вам будут неинтересны. Словарик специальных технических терминов на английском, и сказки Бажова."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "Сказки? Нам без надобности. Что мы дети, читать сказки?"

    ul "А покажи эти книги, пожалуйста. Я вот, сказки люблю, например. Да и словарик тоже покажи."

    al "А словарик тебе зачем?"

    ul "(Шепотом) \nГлупая, в книгах бывают закладки!"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Женя отдала нам книги и записала их на нас."


    scene bg auhouse2 with dissolve

    "Когда мы пришли к себе, стали аккуратно перелистывать книги. В них ничего не было. Но в одной из книг на последней страничке я увидела какие-то вдавленные буквы."


    stop music fadeout 1.0


    play music "audio/music/z_999.mp3"

    "Так бывает, когда пишут, подложив более мягкий листок под тот, на котором пишут, чтобы ручка лучше писала."

    "Я вспомнила, что папа рассказывал, как в одной из криминальных хроник описал случай раскрытия преступления по оттиску с документа написанного от руки."

    "Нужно вдавленные буквы заштриховать мягким карандашом, и буквы проявятся. Так можно прочитать любую записку, которую написали раньше. Листок бумаги, на котором писали, работает в этом случае, как копирка."

    "Я поделилась с Алисой своими мыслями. У Алисы был простой карандаш 2М. Мы сели и аккуратно заштриховали чистый листок бумаги последней страницы книги. И... ПРОЯВИЛИСЬ БУКВЫ! Это была не просто записка..."


    jump get_code

return

image strokethesheet:

    "images/an/an21day/an_d21_21.png" with Dissolve(0.5, alpha=True)
    pause 0.5
    "images/an/an21day/an_d21_22.png" with Dissolve(0.5, alpha=True)
    pause 0.5

    repeat

screen get_code():

    modal True

    add "images/an/an21day/an_d21_01.webp"

    add "strokethesheet" pos (0, 0)

    imagebutton:
        xpos 28 ypos 42
        xsize 200 ysize 199
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"

        action Hide("get_code"), Jump("day21_cont")


label get_code:

    $ show_quick_menu = False

    show screen get_code with fade


label day21_cont:


    image an_21_01: # Анимация шифр
        
        # "images/an/an21day/an_d21_01.webp" with Dissolve(0.5, alpha=True)
        # pause 0.5
        "images/an/an21day/an_d21_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an21day/an_d21_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        #repeat


    scene an_d21_01

    show an_21_01 with dissolve

    $ renpy.pause(9.5, hard=True)

    scene an_d21_20 with dissolve

    pause (10000000000000000000000.0)

    show an_d21_23

    pause (10000000000000000000000.0)

    $ show_quick_menu = True

    $ inv_item_23 = True

    scene cg semyons_diary with dissolve

    "Это была копия ШИФРА которым пользовался Семён при написании своего дневника! Алиса похвалила меня за сообразительность. Теперь у нас был ключ к записям!"

    "Нужно было только еще раз стащить дневник, который мы незаметно вернули назад в прошлый раз, и сфотографировать странички."

    "И мы сделали это, дождавшись, когда Семён отлучится в столовую."

    "Первые его записи касались нашего недавно прошедшего похода. Они настолько интересны, что я решила не писать о походе сама, а просто выложить в своём дневнике расшифровку записей Семёна."

    "Всегда мечтала увидеть событие, которое знаю, глазами другого человека."

    "Может быть, мы зря обижаемся на мальчишек за их нелогичные поступки. Они же не такие как мы! Кажется, скоро мы откроем  великую тайну. Мы наконец у знаем  О ЧЕМ ДУМАЮТ МАЛЬЧИШКИ."

    "Вот записи. Я не стала ничего из них выбрасывать. Пусть будут, как есть."


    jump day21_sem_diary01

return


style SemDiaryText_text:
    color "#000"
    #font "fonts/mateur-webfont.ttf"
    size 20

screen day21_sem_diary01():

    # on 'show' action PauseAudio('music', True) 
    # on 'hide' action PauseAudio('music', False)

    tag menu
    zorder 100
    modal True

    imagemap:

        ground "images/cg/cg_day21/cg sem_diary_01.webp"
        idle "images/cg/cg_day21/sem_diary_fw.png"
        hover "images/cg/cg_day21/sem_diary_fw.png"

        hotspot(1796, 457, 100, 167) action Hide ("day21_sem_diary01"), Show ("day21_sem_diary02")



screen day21_sem_diary02():

    tag menu
    zorder 100
    modal True

    imagemap:

        ground "images/cg/cg_day21/cg sem_diary_02.webp"
        idle "images/cg/cg_day21/cg sem_diary_02_idle.png"
        hover "images/cg/cg_day21/cg sem_diary_02_hover.png"

        hotspot(260, 450, 600, 414) action Hide ("day21_sem_diary02"), Show ("day21_sem_diary02_img01")
        hotspot(1101, 98, 587, 342) action Hide ("day21_sem_diary02"), Show ("day21_sem_diary02_img02")
        hotspot(1097, 521, 594, 342) action Hide ("day21_sem_diary02"), Show ("day21_sem_diary02_img03")

        hotspot(24, 457, 100, 167) action Hide ("day21_sem_diary02"), Show ("day21_sem_diary01")
        hotspot(1796, 457, 100, 167) action Hide ("day21_sem_diary02"), Show ("day21_sem_diary03")



screen day21_sem_diary02_img01():

    tag menu
    zorder 100
    modal True

    add "images/cg/cg_day21/cg peak_dv_01.webp"


    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("day21_sem_diary02_img01"), Show("day21_sem_diary02")


screen day21_sem_diary02_img02():

    tag menu
    zorder 100
    modal True

    add "images/cg/cg_day21/cg peak_dv_02.webp"


    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("day21_sem_diary02_img02"), Show("day21_sem_diary02")



screen day21_sem_diary02_img03():

    tag menu
    zorder 100
    modal True

    add "images/cg/cg_day21/cg peak_dv_03.webp"


    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("day21_sem_diary02_img03"), Show("day21_sem_diary02")



screen day21_sem_diary03():

    tag menu
    zorder 100
    modal True

    imagemap:

        ground "images/cg/cg_day21/cg sem_diary_03.webp"
        idle "images/cg/cg_day21/cg sem_diary_03_idle.png"
        hover "images/cg/cg_day21/cg sem_diary_03_hover.png"

        hotspot(202, 81, 667, 501) action Hide ("day21_sem_diary03"), Show ("day21_sem_diary03_img01")

        hotspot(24, 457, 100, 167) action Hide ("day21_sem_diary03"), Show ("day21_sem_diary02")
        hotspot(1796, 457, 100, 167) action Hide ("day21_sem_diary03")#, Jump ("day21_cont2")



screen day21_sem_diary03_img01():

    tag menu
    zorder 100
    modal True

    add "images/cg/cg_day21/cg peak_dv_04.webp"


    imagebutton:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        idle "gui/bg_1x1_transparent.png"
        hover "gui/bg_1x1_transparent.png"
        action Hide ("day21_sem_diary03_img01"), Show("day21_sem_diary03")




label day21_sem_diary01:

    stop music fadeout 1.0


    play music "audio/music/z_140.mp3"


    show screen day21_sem_diary01 with dissolve

    pause (10000000000000000000000.0)

    hide screen day21_sem_diary01


    jump day21_cont2


label day21_cont2:


    stop music fadeout 1.0


    play music "audio/music/z_491.mp3"

    scene bg nbeach with dissolve

    "Сегодня на пляж перед обедом пришли Маргарита Павловна и Атсуи. Впервые директриса появилась в купальнике!"


    scene cg d21_mp_ats_beach with dissolve

    "Мальчики лежали на песке, делая вид что загорают, но на самом деле живо обсуждали информацию о том, что Атсуи плавает как лягушка."

    "В Японии она была капитаном команды дайверов. Людей, которые плавают с аквалангами в море. Несколько смущал надувной круг, который они притащили с собой."

    "Мнения разделились. Одни говорили, что круг нужен Маргоше, и что она вовсе не умеет плавать."

    "Другие склонялись к тому, что «старушка еще даст копоти» и покажет себя на дистанции 50 метров, которую они плавали на время, сдавая нормы ГТО."

    "Как-то незаметно, сам собой, спор плавно перетек в обсуждение женских фигур. Тут мнения тоже разделились."

    "Электронику понравилась фигурка Атсуи, которой он явно симпатизировал. И к слову, живейшее участие обоих кибернетиков в данном споре наголову разбивало миф об их «странной дружбе», ходивший в отряде до этого."

    "Другая часть мужского населения отряда соглашалась с тем, что хотя у Атсуи очень хорошая, типично японская фигура, но длинные ноги Марго очень «сильный аргумент»."


    scene cg d21_al_beach with dissolve

    "А Алиса, которая загорала с закрытыми глазами, даже не посмотрела в сторону этой парочки. Но все слышала. Она сказала: «Мужчины, так предсказуемы»."

    "На ней был черный запасной купальник, который она не надевала раньше. Но из-за того, что она отдала мне свой, первый раз надела."

    "Мне пришлось ушить немного ее купальник, но из своего я явно выросла. Мы тут все слегка поправились на лагерных харчах."

    "Этот чёрный купальник подчеркивал фигуру Алисы, и она смотрелась в нем потрясно. Семён отметил обновку фразой: «Сегодня наша прима особенно хороша», на что Алиса только презрительно хмыкнула."

    pause (10000000000000000000000.0)


    scene cg d21_mp_ats_beach with dissolve

    "В пылу спора никто не заметил, как Маргарита Павловна и Атсуи прошли мимо достаточно близко, чтобы слышать о чем, собственно, спор. Может быть, именно поэтому они вдруг оглянулись и засмеялись?"

    pause (10000000000000000000000.0)

    scene cg d21_vio_beach with dissolve

    "А потом мы услышали еще более громкий смех. Оказывается, на пляж пришло все наше начальство и наши американки. Они незаметно разделись и загорали позади нас, за раздевалками. И все слышали."

    "Были Виола, Майя и даже Мегги сегодня пришла, она была самая загорелая. Вот, что значит бегать на пляж по утрам и делать гимнастику."

    "Странно, но все были в черных купальниках. Нам стало ясно, что приход директрисы на пляж спровоцировал цепную реакцию, «форма одежды строгая, черная»."

    pause (10000000000000000000000.0)


    scene bg nbeach with dissolve

    show sp_al_059:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса толкнула меня в плечо и сказала на ухо:"

    al "Жалкие подхалимы, все точно в таких же купальниках."

    hide sp_al_059

    show sp_ul_042:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Алисочка, в таком случае твой прогиб будет замечен. Жди поощрений. Ты же сегодня тоже в черном."

    hide sp_ul_042


    show sp_al_060:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Все грохнули от смеха. Алиса сконфузилась. Но потом нашлась."

    al "Это они узнали, что я буду в черном, и от зависти быстро перестроились.  Я пришла на пляж первая. Жалкий плагиат. "

    hide sp_al_060

    "Все снова загалдели. Теперь обсуждали фигуру Виолы и Майи."

    "Вскоре, к разговору присоединились и девочки отряда. Однако они быстро увели спор от фигур в русло оценки купальников."

    "Не то, что бы их не волновала тема фигур (конечно, каждой хотелось, чтобы на пляже на неё смотрели с восхищением), однако КУПАЛЬНИКИ... Согласитесь, ЭТО СВЯТОЕ."


    stop music fadeout 1.0


    play music "audio/music/z_076.mp3"


    scene bg dining with dissolve

    "Странно, уже целый день после соревнований прошёл, а кушать хочется, «как не в себя». И в обед особенно кушать хотелось. Как говорила тетя Люба, промялись, видать, спортсмены."

    "А у нас еще будут заплывы на 25 и 50 метров. И мы решили потренироваться до обеда."

    "Я первая пришла с пляжа. Думала уговорить Толика, который дежурил по кухне, положить мне большую котлету. Самую большую из тех, что есть."


    scene cg ul_tol_potato with dissolve

    "И даже за это помогла ему почистить всю картошку. Но он сказал, что котлеты теперь делает машина. И они калиброванные. Слово мне непонятное. Понятно только, что одинаковые."

    "Эта машина стояла в подвале, но тетя Люба не справлялась, и завхоз разрешила установить эту машину. Толик показал, как она работает. Загружается фарш, и пошло-поехало."

    "Она сама его сначала в колбасу вытягивает, потом на дольки режет и плющит. Так что котлетки выскакивают прямо как братья-близнецы. А следит за всем тетя Люба. Тут не «смухоморишь»."

    "И вот, пока мы разговаривали, я увидела как тетя Люба на наш стол тарелки раскладывает. И тут заходит Семён. А она ему с подноса тарелочку. А там! Не поверите! Вместо одной, ТРИ КОТЛЕТЫ! Вот Гад!"


    stop music fadeout 1.0


    play music "audio/music/z_1004.mp3"

    "Ну, у меня от такой несправедливости, прямо красные круги перед глазами. Я толкаю Толика: «Видишь?!» А он так грустно отвечает: «Да, она так всегда делает»."

    "И всё, тут я стерпеть не могла. Меня какая-то сила прямо вперед бросила, и я, подскочив к Семёну из-за спины, схватила две котлеты из тарелки и наутек."

    "И думала в домик бежать. Но тут он тоже выскочил на улицу. И я подумала, в домике он меня схватит. Поэтому я бросилась в лес."


    scene cg sem_ul_cutlet6 with dissolve

    "Я там недавно нашла тропинку, которая была мне неизвестна. И я, что было сил, побежала (я быстрее всех бегаю). Но и Семён не отставал."

    "Мы бежали сильно, а тропинка всё петляла, а лес вокруг становился всё темней и гуще. Тропинка вела в глубокую чащобу, и я испугалась. Я начала на бегу думать: «Может, ну их, эти котлеты, пусть забирает»."

    "Потом подумала, что НЕТ, черта с два, пусть эти котлеты никому не достанутся. Остановилась и зашвырнула их далеко в лес. И снова побежала. Я слышала за спиной тяжелое дыхание Семёна..."


    stop music fadeout 1.0


    play music "audio/music/z_1001.mp3"

    scene cg ul_cutlet_path2 with dissolve

    "И я подумала: «Бедненький, ему ни в жизнь меня не догнать». Но, ведь если он меня не догонит, то какой смысл было их воровать."


    scene cg ul_cutlet_path3 with dissolve

    "И я остановилась, чтобы посмотреть как сильно он отстал. Но он оказался ближе, чем я думала, налетел сзади и снес меня."


    stop music fadeout 1.0


    play music "audio/music/z_1005.mp3" noloop

    "Я ударилась коленкой. Там был склон, и мы покатились по тропинке вниз, в траву."

    stop music fadeout 1.0


    play music "audio/music/z_125.mp3"

    "И я оказалась прямо под ним. А у него глаза дикие и не человеческие какие-то. Как у Вано, когда он на меня смотрит. И я ещё сильнее испугалась."


    scene cg sem_ul_cutlet with dissolve

    "А он прямо впился мне в руки своими пальцами, чуть не сломал. Большой, потный и дышит... Ну, и я сказала первое, что мне пришло в голову: «НАСИЛОВАТЬ БУДЕШЬ?»"

    "А он вдруг перестал сильно сжимать и так странно на меня посмотрел. Сел сверху, я даже пошевелиться не могла. И вдруг сказал: «Дура ты. Это твой Пионер бы сделал. А я – нет»."

    "Потом наклонился. Я зажмурилась, думаю — ВСЁ! И схватилась за шорты. Думаю: «НЕ СДАВАЙСЯ ЛЕНИНА, борись!»"

    "А он просто губами в лоб меня поцеловал, так тихо-тихо, и отпустил. От него шел запах женских духов, но я их узнала. Я такие у Ольги Дмитриевны на столике видела. Называются «МОЖЕТ БЫТЬ»."

    "И сразу представила себе (ну это я фантазировала) их отношения."


    scene cg sem_od_kiss with dissolve

    "Ну, они же в одном домике живут. Тут еще эти сплетни в отряде про ОД... И меня почему-то прямо в жар кинуло. Наверное, я красна вся стала."

    stop music fadeout 1.0


    play music "audio/music/z_010.mp3"


    scene cg sem_ul_cutlet2 with dissolve

    sem "Что с тобой? Ты не заболела? Вся горишь... \n(трогает щеки и лоб)"

    ul "(Убирая руку) \nСмотри, порвал майку. И ссадина на колене."

    sem "Отдай мне, вечером зашью. А ссадина... До свадьбы заживет."

    ul "Ещё чего, я сама шить умею. И не нужна мне никакая свадьба."

    ul "(Усмехнувшись) \nЧто скажут, если увидят тебя рядом, а на мне разорванную майку?"

    sem "Ну, я бы ее сейчас забрал, а тебе отдал бы свою рубашку. Все решат, что мы с пляжа идем."

    ul "Хм... Как надолго отдал бы?"

    sem "Ну, не знаю... Если что, у меня еще есть."

    sem "(Дует на Ульянину коленку) \nБольно?"

    ul "Больно. Ладно, отвернись, а то я без купальника."

    ul "(Снимает майку) \nИ снимай свою рубаху. Я такая не покажусь Алисе. Она вечно делает из мухи слона."

    sem "(Сидя спиной протягивает ей рубаху) \nНа, держи. А зачем ты так сказала?"


    scene cg ul_cutlet_path4 with dissolve

    ul "(Надевая рубаху Семёна) \nПро НАСИЛОВАТЬ?"

    sem "Да."

    ul "Ну, не знаю. Я в фильме такое видела. Там немцы. Зою Космодемьянскую сначала пытали, а потом..."

    sem "Ну, скажешь тоже! Я что, гестаповец какой? Тоже мне, Зоя! И да, черт с ними, с котлетами."

    ul "А зачем тогда погнался?"

    sem "(Посмотрев странно) \nМожет, ты мне нравишься? Глупая."

    ul "(Опешив) \nЧего?!"

    sem "(Смеется) \nА что? Считаешь, я не способен, э-э-э... Дружить?"

    ul "НЕ СПОСОБЕН. Алиса говорит, что ты сексуальный маньяк и не пропускаешь ни одной юбки."

    sem "А ты не Алисиным умом живи, а своим. И вовсе это не так. Просто я, может, «ищу в колоде свою карту»."

    ul "И что, нашел?"

    "Семён поднялся."

    sem "Ладно, вставай. Вот, твоя сандалия, держи, потеряла. \n(стирает ладонью пыль с Ульяниной обуви и отдает)"

    sem "Ничего ты не понимаешь. Может и нашел. Джокера. \n(смеётся)"

    sem "А что с котлетами будем делать?"

    ul "Пусть достанутся Ежу и Черепахе."


    stop music fadeout 1.0


    play music "audio/music/track2.mp3"

    scene cg sem_ul_cutlet3 with dissolve

    "И мы вместе зашагали назад. А я спросила по дороге:"

    ul "А за что ты так Пионера не любишь? Он хороший. Он меня не тронул на острове."

    "И тут я поняла, что проговорилась. А Семён как-то вдруг пристально посмотрел на меня, с изменившимся лицом."

    sem "Не тронул? На острове? Так вот он где прячется..."

    ul "(Помолчав) \nТы про дружбу серьезно говорил?"


    scene cg sem_ul_cutlet4 with dissolve

    sem "Само собой."

    ul "(Выдержав паузу) \nХорошо. Я подумаю. Только учти, дружба, это навсегда. Готов к такому?"

    sem "(Улыбнувшись) \nДа, условие серьезное... Говорят, платонические отношения между мужчиной и женщиной невозможны. А ты как считаешь?"


    scene cg sem_ul_cutlet5 with dissolve

    "Ты скользкий... Уходишь от ответа. Так ДА или НЕТ?"

    sem "Да."


    scene cg sem_ul_cutlet6 with dissolve

    pause (10000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene bg library with dissolve

    "А позже в этот же день я занесла словарик английских терминов в библиотеку и заметила, что Женя выглядит озабочено."


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    je "Слушай, тут Семён заходил, он у всех спрашивает, не видел ли кто его связку ключей. Похоже, он их потерял. Тебе не попадались? Или, может, нашёл кто... Ты же все про всех знаешь."


    scene bg library2 with dissolve


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    ul "Нет. Если бы попадались, я бы отнесла Ольге Дмитриевне. А от чего ключи?"
 

    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Он не сказал."

    hide sp_je_001 

    "И я убежала. А сама подумала: было бы интересно найти эти ключи."


    scene bg square_day with dissolve

    "Нужно решить, где искать ключи."

    jump keys_choice


label keys_choice:

    menu:

        "Памятник Генде":
            jump keys_genda
        
        "Раздевалка":
            jump keys_dresser

        "Баскетбольная площадка":
            jump keys_basketball

        "Ближний пляж":
            jump keys_nbeach

        "Лазейка":
            jump keys_stels

        "Душевые":
            jump keys_showers

        "Центральный вход":
            jump keys_busstop

        "Столовая":
            jump keys_dining

        "Тропа украденной котлеты":
            jump keys_thiefpath



label keys_genda:

    scene bg genda with dissolve

    "Я поискала возле памятника Генде, но ничего не нашла."

    jump keys_choice


label keys_dresser:

    scene bg dresser with dissolve

    "Я поискала в раздевалке, но ничего не нашла."

    jump keys_choice


label keys_basketball:

    scene bg basketball with dissolve

    "Я поискала на баскетбольной площадке, но ничего не нашла."

    jump keys_choice


label keys_nbeach:

    scene bg nbeach3 with dissolve

    "Я поискала на Ближнем пляже, но ничего не нашла."

    jump keys_choice


label keys_stels:

    scene bg stels with dissolve

    "Я поискала там, где Лазейка, но ничего не нашла."

    jump keys_choice


label keys_showers:

    scene bg showers2 with dissolve

    "Я поискала в душевых, но ничего не нашла."

    jump keys_choice


label keys_busstop:

    scene bg busstop4 with dissolve

    "Я поискала возле Центрального входа, но ничего не нашла."

    jump keys_choice


label keys_dining:

    scene bg dining with dissolve

    "Я поискала в столовой, но ничего не нашла."

    jump keys_choice


screen keys_theifpath():

    tag menu
    zorder 100
    modal True

    imagebutton:
        xpos 1647 ypos 879
        xsize 273 ysize 201
        idle "images/cg/cg_day21/mushroom.png"
        hover "images/cg/cg_day21/mushroom.png"
        action Hide ("keys_theifpath"), Jump("day21_cont3")


label keys_thiefpath:

    scene bg thiefpath with dissolve

    "Что ж, поищу здесь."

    $ show_quick_menu = False

    show screen keys_theifpath

    pause (10000000000000000000000.0)

    hide screen keys_theifpath

    jump day21_cont3




label day21_cont3:

    scene bg thiefpath

    show semyon_keys

    pause (10000000000000000000000.0)

    hide semyon_keys

    show got_keys

    pause (10000000000000000000000.0)

    $ show_quick_menu = True

    hide got_keys

    $ inv_item_37 = True
    $ inv_item_38 = True
    $ inv_item_39 = True
    $ inv_item_40 = True


    "Так я и знала! Семён обронил ключи в том месте, где мы боролись за котлеты!"

    "Отлично. Теперь мы узнаем, от чего эти ключи."


    scene cg door_search with dissolve

    "После ужина мы с Алисой решили найти, к чему подходят ключи, которые потерял Семён. Мы не хотели их присвоить, просто хотели сначала узнать, что они открывают."


    jump find_the_door



screen no_01():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/no.png" xpos 69 ypos 611


screen no_02():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/no.png" xpos 484 ypos 543


screen no_03():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/no.png" xpos 546 ypos 530


screen no_04():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/no.png" xpos 1213 ypos 371


screen no_05():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/no.png" xpos 1695 ypos 629


screen yes_01():

    #tag menu
    zorder 100
    #modal True

    add "images/cg/cg_day21/yes.png" xpos 975 ypos 205


screen find_the_door():



    # on 'show' action PauseAudio('music', True) 
    # on 'hide' action PauseAudio('music', False)

    tag menu
    zorder 100
    modal True

    imagemap:

        ground "images/cg/cg_day21/cg door_search.webp"
        idle "images/cg/cg_day21/door_search_idle_hover.png"
        hover "images/cg/cg_day21/door_search_idle_hover.png"

        hotspot(91, 648, 45, 100) action Hide ("no_02"), Hide ("no_03"), Hide ("no_04"), Hide ("no_05"), Show ("no_01")
        hotspot(470, 578, 76, 110) action Hide ("no_01"), Hide ("no_03"), Hide ("no_04"), Hide ("no_05"), Show ("no_02")
        hotspot(553, 568, 45, 74) action Hide ("no_01"), Hide ("no_02"), Hide ("no_04"), Hide ("no_05"), Show ("no_03")
        hotspot(978, 235, 31, 82) action Hide ("find_the_door"), Hide ("no_01"), Hide ("no_02"), Hide ("no_03"), Hide ("no_04"), Hide ("no_05"), Jump ("day21_cont4")
        hotspot(1213, 407, 41, 93) action Hide ("no_01"), Hide ("no_02"), Hide ("no_03"), Hide ("no_05"), Show ("no_04")
        hotspot(1677, 659, 59, 102) action Hide ("no_01"), Hide ("no_02"), Hide ("no_03"), Hide ("no_04"), Show ("no_05")


label find_the_door:


    stop music fadeout 1.0


    play music "audio/music/z_124.mp3"

    $ show_quick_menu = False


    show screen find_the_door

    pause (1000000000000000000.0)


    hide screen find_the_door

    $ show_quick_menu = True

    jump day21_cont4 


label day21_cont4:

    scene cg door_search_yes

    pause (1000000000000000000.0)


    scene cg door_search

    show key_idented

    $ inv_item_37 = False
    $ inv_item_26 = True

    pause (1000000000000000000.0)

    hide key_idented

    $ show_quick_menu = True

    "И мы прикладывали их ко всем замкам в лагере, какие только можно было найти. Даже к замку в двери кабинета директрисы Маргариты Павловны. Только один ключ подошел. Об этом подробнее. Это важно."


    scene bg odhouse4 with dissolve

    "На втором этаже домика ОД тоже был чердак, как и над нашим с Алисой. Он тоже был закрыт на замок, как и все чердаки (мы проверяли все). А вот к этой двери ключ подошел."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"

    scene bg msecret with dissolve

    "И вот мы вошли. Мы думали что там будет пыль и паутина как у нас (мы же долго его отмывали и прибирали там, прежде чем сделать себе нычку)."

    "Но там было чисто. Был даже включатель для света, сбоку. И плотная шторка на окне. Мы включили свет и увидели, что там есть тумбочка и кровать. Кровать была аккуратно застелена свежим постельным бельем."

    "Было ощущение, что тут буквально вчера еще кто-то был. Подушки были как будто примяты и одеяло застелено наполовину."

    "Алиса понюхала одну подушку и сказала: «Вообще не пахнет»."

    scene cg pallmall with dissolve

    "В тумбочке лежала пачка каких-то сигарет, не наших, у нас таких не делают. Алиса прочитала на английском: «ПЕЛ МЕЛ»."


    scene bg msecret with dissolve

    "И консервы разные. Кажется шпроты, сгущенка и баночка леденцов. На тумбочке лежали две книги из нашего читального зала библиотеки. Мы даже заглянули под кровать."


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Обследуя пол под кроватью) \nЕсли есть сигареты, то значит есть и окурки. Надо посмотреть везде. Вот, смотри, есть!"

    hide sp_al_005


    scene cg hardcandies2 with dissolve
  
    "Еще одна открытая баночка из под леденцов и она была не пустая."

    ul "Кто-то любит сладкое. Ну-ка, ну-ка, что тут у нас... \n(вытряхивает леденцы)"


    scene cg hardcandies with dissolve

    ul "Ой красотища... Можно я возьму несколько штучек? Ну как вещественные доказательства."

    al "(Сглотнув) \nНет. Лучше не надо. Будет заметно."


    scene bg msecret with dissolve

    show sp_ul_016:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ладно... \n(разочарованно)"

    hide sp_ul_016

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А, вот, то, что надо. Окурки! Смотри тут примятый окурок со следом! Между прочим, Семён не курит, если ты заметила. Это явно не его."

    hide sp_ul_012


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Разглядывая окурок) \nИ губы не красит."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Сигареты иностранные. А кто у нас иностранцы?"

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Саманта, но она не курит еще, маленькая. Атсуи, Мику, и... Мэгги. Виола, Маргоша, Любаня, и наша завхоз."

    al "Маргоша и завхоз отпадают, Любаня курит те же вонючие папироски что и Петрович. Виола... Да, возможно. Но у нее есть своя комнатка. Остаются наши."

    hide sp_al_005


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Даже если Атсуи или Мику курят, о чем мы не знаем, то губы они точно не красят."

    hide sp_ul_019

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Нюхая окурок с следами губной помады) \nПахнет классно."

    hide sp_al_006


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну, это просто. Значит, Мэгги!"

    hide sp_ul_014


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Подожди, не спеши с выводами. Все вроде совпадает, но нет логики."

    al "Да, Мегги курит, но я ни разу не видела у нее на губах помады. Она, по моему, презирает все женское. Даже платьев не носила бы, если бы ее не уговорили одеться, как пионервожатую."

    al "У нас тут правила такие. Никто не должен выделяться."

    hide sp_al_005


    "Мы сели на кровать и задумались. Это была та еще задача. Ну посудите сами, есть нычка в которой живет кто-то, кого в лагере ни разу не видели."

    "И тут меня осенило. Значит, этот человек приходит сюда только ночью! Иначе его давно бы заметили."

    "Но даже ночью Петрович мог бы увидеть. Он же сторож. Значит, Петрович либо знает этого человека, либо тот слишком осторожен. Но что было точно, так это то, что Семён знал этого человека. Эту женщину..."


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Надо установить Слежку за Сёмой в ночное время. А точнее, выставить тут дежурство. Семён потерял ключи, но у того второго они есть."

    al "Давай подведем итог. Первое - Семён знает эту женщину."

    al "Второе - женщина курит. Она возможно иностранка, или имеет возможность доставать иностранные сигареты. (Семён принес?)"

    al "Третье – она сладкоежка."

    al "Четвертое - она очень аккуратна, потому что мы не обнаружили больше ничего. Ни следов волос на подушке, ни каких-либо принадлежностей женского гардероба. Даже баночка с окурками аккуратно стояла за ножкой кровати."

    al "Ладно, потом разберемся. Осталось еще два ключа. Ты уверена, что мы все замки в лагере посмотрели?"

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Есть замок под памятником, но тут такого ключа нет. Замок от подвала, но туда мы не можем попасть. Замок от медпункта, но там сейчас Виола, и проверить мы не сможем пока. И... И..."

    hide sp_ul_013


    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ты тоже подумала?"

    hide sp_al_006


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да!"

    hide sp_ul_012


    stop music fadeout 1.0


    play music "audio/music/z_131.mp3"


    scene bg bomp_shelter2 with dissolve

    "И ту мы вместе воскликнули: «БОМБОУБЕЖИЩЕ!»"

    "Дверь в бомбоубежище никогда не открывалась, и никто там никогда не был."


    scene bg tirhands2 with dissolve

    "Рядом с спортивной площадкой была маленькая раздевалка для мальчиков."

    "Мальчиков туда, правда, не пускали, потому что девочки оборудовали лавочку напротив, за кустами, чтобы не бежать в свою раздевалку, и мальчишки бы подглядывали. Оттуда эта лавочка была «как на ладони»."

    "Ключ от нее был только у физрука. Насчет нее шли всякие разговоры. Мы подозревали, что там кто-нибудь может прятаться. Но из-за темных стекол ничего не было видно. Потом привыкли и переодевались спокойно."

    "А рядом с ней была мощная дверь, а на ней надпись: «Бомбоубежище». И указатель, куда спускаться. И ещё надпись: «В случае опасности идти сюда»."


    scene bg bomp_shelter with dissolve

    "Опасности не было, но мы решили пойти туда, если ключ подойдет."

    "Мы быстро привели все в порядок, чтобы никто не догадался, что мы сидели на кровати, и спустились вниз."

    "Дальше было легкотня. Мы подошли к двери в бомбоубежище, улучшив момент, когда на спортивной площадке никого не было. Я стояла на стреме, а Алиса подбирала ключ."

    "Пока я смотрела за площадкой, я услышала радостный вопль Алисы. ЕСТЬ! Один ключ точно подошел. Но сейчас спускаться туда было небезопасно. Нас могли увидеть. Мы решили дождаться ночи."


 









    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day22

return 







