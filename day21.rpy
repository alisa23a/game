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

    "Но, случилось еще то, что мы нашли шифр к записям Семена. И в его дневнике, этот поход описан как мне кажется, интереснее."

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

    je "Вы интересовались книгами, которые брал Семен. Он уже вернул книги, и если хотите, я дам их вам."


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

    "Это была копия ШИФРА которым пользовался Семен при написании своего дневника! Алиса похвалила меня за сообразительность. Теперь у нас был ключ к записям!"

    "Нужно было только еще раз стащить дневник, который мы незаметно вернули назад в прошлый раз, и сфотографировать странички."

    "И мы сделали это, дождавшись, когда Семен отлучится в столовую."

    "Первые его записи касались нашего недавно прошедшего похода. Они настолько интересны, что я решила не писать о походе сама, а просто выложить в своём дневнике расшифровку записей Семена."

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
        hotspot(1796, 457, 100, 167) action Hide ("day21_sem_diary03"), Jump ("day21_cont2")



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

    $ show_quick_menu = False

    show screen day21_sem_diary01 with dissolve

    pause (10000000000000000000000.0)


label day21_cont2:

    $ show_quick_menu = True

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

    "Этот чёрный купальник подчеркивал фигуру Алисы, и она смотрелась в нем потрясно. Семен отметил обновку фразой: «Сегодня наша прима особенно хороша», на что Алиса только презрительно хмыкнула."

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






    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day22

return 







