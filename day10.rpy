label day10:

    $ style.say_window = style.window

    $ days = 10

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = True
    $ adv_12 = False
    $ adv_15 = False



    $ im_gal_09_00 = True
    $ im_gal_09_01 = True


    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg stadium2 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_023.mp3"


    "После завтрака мы пошли играть в мяч. Я кидала, а Алиса отбивала его бейсбольной битой, потом наоборот. В процессе мы обсудили наш план."

    show sp_al_062:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Я не собираюсь это так оставлять. Я знаю, кто это сделал. Это Долговязый из второго отряда и его дружки. Всё, им конец."

    hide sp_al_062


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А вдруг, ты ошиблась? Пострадают невинные."

    hide sp_ul_019


    scene bg dresser3 with dissolve

    "Мы зашли в раздевалку. Там никого не было, и можно было спокойно обсудить наш план."


    show sp_al_056:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Не говори ерунду. Эта компания по всему лагерю слоняется. Вечно смотрят, как бы напакостить."

    al "Тузику привязали к хвосту консервную банку и развлекались, наблюдая, как бедный ошалевший пес бегает по лагерю."

    al "Петровичу в табак насыпали какой-то дряни, он потом три дня болел."

    al "А сетку волейбольную кто, по твоему, украл и пытался ловить ею рыбу? Нашли сетку через два дня, её снесло течением, и она зацепилась за опору лодочной станции."

    al "В ней еще запутались малыши. Они могли утонуть, а наказали физрука. Я, конечно, не люблю Тараса Юрьевича, но пострадал он зазря."

    hide sp_al_056


    show sp_al_062:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Короче, им не жить! Всё, кончились их подлые выходки. За малышей, за Тузика и за Петровича страшно отомстим!"

    hide sp_al_062


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Отомстим, точно! Но как?"


    scene bg secret3 with dissolve

    "Мы переоделись и вышли на улицу."


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_176.mp3"


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "У меня есть план. Я вызову Долговязого на разборку."

    hide sp_al_005


    show sp_ul_026:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но это же драка! За такое точно по головке не погладят."

    hide sp_ul_026


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "И потом, он трус, один он не пойдет, позовёт с собой весь второй отряд. А они все тебя ненавидят. "

    hide sp_ul_013


    #scene an_spec_nb_02_12 with dissolve
    scene cg al_bat_tree with dissolve

    al "Тогда я на всякий случай возьму биту для бейсбола, которую мне подарила Саманта. На всякий крайний. Ну, если толпой нападут. А один на один на кулаках он мне проиграет."


    image spec_nb_02_an_01: # Анимация Алиса с битой
        

        #"images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        #pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat


    #scene spec_nb_02_an_01 with dissolve

    scene cg al_bat_tree

    pause (10000000000000000000000.0)


    scene bg secret3 with dissolve


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Не будет он драться один на один. Только если случайно столкнемся, и ему просто деваться некуда будет."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Давай так. Я постараюсь с ним разобраться один на один, но если он позовет толпу, то беги к нашим."

    al "Когда начнется, ты на васаре будешь стоять. В драку, если что, не лезь. Тебя затопчут, малявка."

    hide sp_al_004


    show sp_ul_045:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот еще! Я ловкая. Я не буду смотреть, как тебя бьют."

    hide sp_ul_045


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Верю. Но всё равно, на стрёме стой. Ну что, ОДИН ЗА ВСЕХ?!"

    hide sp_al_005


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И ВСЕ ЗА ОДНОГО!"

    hide sp_ul_014

    "И мы ударились кулаками."


    scene bg stadium2 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_131.mp3"


    "Но все случилось быстрее, чем мы думали. Со стороны спортплощадки нас окликнул Долговязый. Он был не один. С двумя мальчиками из второго отряда."


    show sp_gan_001:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    gan "Эй, голожопые, куда намылились?"



    scene bg secret3 with dissolve

    show sp_al_061:
        yalign 0.05 subpixel True
        xalign 0.50 subpixel True
        zoom 1.2
    with dissolve

    al "(Направляясь прямо к нему) \nНу что, придурок, продолжаешь распространять слухи про нас с Ульяной? Когда это мы бегали пьяные и голые по пляжу?"

    al "А чем вам Тузик помешал? Кстати, за Петровича тоже давно пора вам навалять."


    scene bg stadium2 with dissolve

    show sp_gan_001:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    gan "(Ухмыляясь) \nНу и чё ты нам сделаешь, рыжая?"


    scene cg al_gan_fight with dissolve

    "И тут она ему резко, неожиданно (даже я вздрогнула), врезала кулаком. Так ловко, снизу, под дых. А когда он согнулся, ударила коленкой в челюсть."


    scene cg al_gan_fight


    pause (10000000000000000000000.0)


    "Он охнул и свалился, держась за лицо. Ну и испуганная же у него была рожа! Кажется, она ему губу разбила, а может, даже зубу хана."

    "Те двое побежали сразу за подмогой. А я кинулась в домик Ольги Дмитриевны."


    scene bg odhouse4 with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Семён что-то читал на крыльце."

    hide sp_sem_001


    show sp_ul_026:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я заорала: «Наших бьют!»"

    hide sp_ul_026


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_1004.mp3"


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Семён даже не стал спрашивать, что и как. Перепрыгнул через поручень, прямо как Тарзан, и мы побежали к столовой."


    scene bg dining_menu_bu with dissolve


    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    show sp_el_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "По дороге, с вопросом «А что случилось?» к нам присоединились Толик, Шурик и Электроник, возвращавшиеся с ужина."


    scene bg camp_artifacts with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1
    with dissolve

    ul "Кое-кому надо объяснить, что девочек трогать нехорошо!"


    scene bg stadium2 with dissolve

    "Когда мы подбежали, весь второй отряд уже был там, а руководил Долговязый."

    show sp_gan_002:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    gan "Справа заходи! Ты, мелкий, кидайся ей под ноги! Отсекайте от домиков, она сейчас убежит!"


    scene cg al_bat_wall with dissolve

    "Но Алиса не собиралась бежать. Они окружили её, и она стала спиной к складу, держа в руках биту. А кто-то уже валялся на земле, держась за руку."


    scene cg al_bat_wall


    pause (10000000000000000000000.0)


    scene bg stadium2 with dissolve

    "Долговязый прятался за спинами и орал:"

    show sp_gan_003:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    gan "Тварь! Бейте ногами! Держите её за руки, я ей щас врежу!"

    hide sp_gan_003


    "Они нас не ждали. И мы налетели."


    image spec_nb_02_an_02: # Анимация драка со вторым отрядом


        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat


    scene spec_nb_02_an_02 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_088.mp3"


    pause (10000000000000000000000.0)

    
    scene cg squad_fight with dissolve

    pause (10000000000000000000000.0)


    scene bg stadium2 with dissolve

    show sp_tol_011:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    "Особенно отличился Толик. Кто бы мог подумать, что он так ловко умеет бить всех в лоб своей лысой башкой?!"

    hide sp_tol_011


    show sp_sem_017:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2
    with dissolve

    "На Семёна напали сразу трое."

    hide sp_sem_017

    "Долговязый визжал как резаный:"


    show sp_gan_003:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    gan "Здорового валите, его первого надо отключить! Вы, трое, вперед!"


    scene cg squad_fight2 with dissolve

    "Но я Семёну помогла, одного отвлекла на себя. Шурик с Электроником дрались ещё с тремя. Один потом убежал, но их всё равно было много."


    scene cg sl_mi_le_running with dissolve

    "И тут, я вижу, бегут наши."


    pause (10000000000000000000000.0)


    "Славя — просто звезда, сходу завалила какого-то пацана, ловко ударив его ногой в пах. Как он орал, держась за (тут не буду писать не хорошее слово)."

    "Остальные девчонки хватали тех за волосы. Одному Ленка расцарапала лицо, а потом Мику с Леной повалили Долговязого."

    "Он вырвался, но споткнулся и в позе «зю» пробежал метра три, уткнувшись прямо в колени Алисы."


    scene bg stadium2 with dissolve

    show sp_al_063:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.0

    al "Вот так встреча! \n(прикладывает его битой по спине)"


    scene cg squad_fight2 with dissolve

    "Женя упала и потеряла очки. Её пытались ударить ногой, лежачую и душил один галстуком, но подскочил Шурик, выручил её, скинул душителя и нашел ей очки."

    "Они с Шуриком потом вообще дрались как в фильме «Семеро отважных», стоя спина к спине."

    "(Шурик её потом провожал до домика, ведь надежда умирает последней)."


    scene bg stadium2 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_196.mp3"


    "В общем, когда эти, из второго отряда, поняли, что все пропало, они бросились наутек. Одного мы взяли в плен, потом отпустили."

    show sp_at_020:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.0
    with dissolve

    "Атсуи, прибежала тоже, но на «шапочный разбор». Очень расстроилась, что без неё всё закончилось."

    hide sp_at_020


    "А Саманта ужинала в своей комнатке и ничего не видела. Но это даже лучше. А вдруг бы она влезла в драку? Был бы международный конфликт."

    "Я представила Мегги в драке и что-то мне поплохело. Точно трупики штабелем бы лежали. Нет, хорошо что они не видели."


    scene bg camp_artifacts with dissolve

    "Ну вот. Что было потом. Прибежали еще пионеры с других отрядов, доложили Ольге Дмитриевне."


    show sp_od_025:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    "Она сразу отправила Алису к директрисе (замолчать такое шумное событие было невозможно)."


    scene bg mp_office2 with dissolve

    show sp_mp_001:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.3

    "Та наказала, естественно, зачинщика."


    scene bg camp_artifacts with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Физруку поручили отвести Алису в изолятор лагеря, временно, пока точно не выяснится, кто виноват."


    image spec_nb_02_an_03: # Анимация Алиса в изоляторе
        

        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat

    scene spec_nb_02_an_03 with dissolve

    pause (10000000000000000000000.0)


    scene an_spec_nb_02_01 with dissolve

    "Ну, мы ей сразу туда притащили еды и сигарет, а Женя — хорошую книжку. Кажется, Хроника царствования Карла двенадцатого, Мериме (там еще про Варфоломеевскую ночь)."


    scene bg camp_artifacts with dissolve

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "А на мне ни царапины."

    hide sp_ul_014


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Семён меня поблагодарил за помощь. Хотя он сам справился, если честно. Дерется он круто. Закончил с этими и сразу помогать нашим."

    hide sp_sem_001


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я только два раза стукнула одного, прыщавого. Пнула ногой, как в карате, как меня Мегги учила. Он сложился сразу."

    hide sp_ul_014


    image spec_nb_02_an_04: # Анимация Ульяна карате
        

        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an_spec_nb/an_spec_nb_02/an_spec_nb_02_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.1


        repeat


    scene spec_nb_02_an_04 with dissolve


    $ renpy.music.set_volume(0.00, delay=1.0, channel='music')

    play miscSounds "audio/music/z_035.mp3" noloop


    pause (10000000000000000000000.0)


    scene bg camp_artifacts with dissolve


    stop miscSounds fadeout 1.0


    $ renpy.music.set_volume(1.00, delay=1.0, channel='music')


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Больше не успела. Все очень быстро закончилось. Алиса меня похвалила, сказала: «Вот это удар! Вроде, я тебе такого не показывала»."

    hide sp_ul_014


    scene cg meeting_sad with dissolve

    "Плохо только, что будет собрание отряда, а может даже лагеря, и нас будут ПРОРАБАТЫВАТЬ. Как сказала Ольга Дмитриевна, чтобы другим было неповадно."

    "А я так думаю, правильно мы всё сделали!"


    scene bg mp_office2 with dissolve

    show sp_mp_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Вечером мы пошли всем отрядом к директрисе. Просить за Алису."


    scene bg mp_office with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Семён был от нас делегатом. Он говорил за всех."

    "А выбрали мы его потому, что знали, что Маргоша к нему неровно дышит. Почему так думали? Ну, лагерь хоть и большой, но маленький. Ничего не утаишь."

    "Например, когда Сёму пригласили на вечеринку администрации, кто-то из ребят видел, как он остался у Маргоши в кабинете, когда все разошлись."

    "Не сказку же он ей на ночь рассказывал? В общем, дело ясное."

    hide sp_sem_001


    show sp_od_023:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    "И вот, мы стоим в кабинете Маргариты Павловны. И Ольга Дмитриевна тоже там."


    scene bg mp_office2 with dissolve

    show sp_mp_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "А Маргарита Павловна так ходит туда-сюда, как тигр в в клетке, и выговаривает:"

    mp "Вы позорите лагерь! Наша репутация теперь не стоит выеденного яйца! Кто захочет отправлять детей на убой?!"

    mp "Мы — лагерь образцового содержания! Никогда до вас тут не было потасовок."

    mp "А что я скажу вашим родителям? Мы за вас отвечаем. А если бы кому-нибудь пробили голову или выбили глаз?!"

    "Ну и всё в таком духе."


    scene bg mp_office with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Семён дал ей выпустить пар и взял слово."

    "И это было круто!"

    "Он так логически все разложил, что по его словам выходило, что нас не то что наказывать, а благодарить надо за то, что мы предотвратили анархию, моральное разложение и развал в лагере."

    "Что мы надежда и опора администрации. И что драку начала не Алиса, а на неё подло напали. Могли и изнасиловать. Но, слава богу, мы подоспели вовремя."

    "И все мы, как один, отбивались от хулиганов и спасали члена своего отряда."

    "И самое главное – хулиганы из второго отряда опасны для дисциплины в лагере и что этот вирус неповиновения, идущий от них, может заразить и другие отряды."

    "И что только железною рукой... И так далее."


    hide sp_sem_001


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    "А мы дружно поддакивали и кивали. И Ольга Дмитриевна приняла нашу сторону."

    hide sp_od_022


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2
    with dissolve

    "Потом Семён рассказал факты о втором отряде, которых не знала Марго."


    scene bg mp_office2 with dissolve

    show sp_mp_009:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Она ахнула. От былой ее решимости нас наказать не осталось и следа. И мы попросили выпустить Алису из изолятора, как потерпевшую."


    scene bg mp_office with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Она сразу позвала Тараса Юрьевича, и мы торжественно пошли её вызволять."


    scene bg insulator with dissolve

    "А когда открыли изолятор, выяснилось, что Алиса сбежала через окно. Вот так..."

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2
    with dissolve

    "Тарас Юрьевич выругался: «Хулиганка» и пошел к себе в раздевалку. У него там малыши готовились к соревнованиям."

    hide sp_fi_015

    "Теперь надо было найти Алису и рассказать ей, что гроза миновала, и чтобы она возвращалась."


    scene an_d10_01_bg with dissolve

    "Вот так всё закончилось. И всё благодаря Семёну."


    image an_10_01: # Анимация с Ульяной, лежащей в комнате и пишущей дневник
        
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    show an_10_01

    "Как-то я забыла написать про наши кружки. Ну, то есть я написала, что они есть, но они настолько интересные, что нужно написать отдельно."


    scene bg mus with dissolve
    
    show sp_mi_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "У нас есть: Музыкальный кружок «Меломан», который ведет Мику. "


    scene bg balet_room_empty with dissolve

    show sp_al_037 at flip:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Хореографический кружок «Прима», который ведет Алиса"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Ещё есть библиотечный кружок «Юный полиглот», который ведет Женя."


    scene bg sewing with dissolve

    show sp_le_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.15

    "И кружок «Вышивальщица», который ведет Лена в помещении столовой. Там есть такая перегородочка, они берут столы и стулья в зале."


    scene bg fotoc with dissolve

    show sp_sl_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "А также кружок-фотостудия «Совенок», который ведет Славя."


    scene bg handmade with dissolve

    show sp_el_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_shu_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Ну и куда без кружка «Умелые руки» с Шуриком и Электроником во главе."


    scene bg stadium with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Также, на нашем стадионе, Тарас Юрьевич ведет секцию «Юный Спортсмен»."


    scene bg fine_arts with dissolve

    "И наконец, тоже мой любимый кружок, кружок ИЗО. Изобразительного искусства."


    show sp_sem_013:
        yalign 1.0 subpixel True
        xalign 0.5 subpixel True
        zoom 0.8
    with Dissolve(0.3)

    "Правда я не рисовала еще, а только позировала Семёну (об этом отдельно напишу). Но я наверстаю."


    scene an_d10_01_bg with dissolve

    show an_10_01


    "Есть расписание занятий кружков и каждый записался в те кружки, которые ему нравятся."

    "Я, конечно, записалась во все кружки. Но из-за того, что я часто занята всякими интересными делами (вы же знаете, какая я непоседа), я не всегда успеваю во все ходить."

    "Я решила, что чаще буду ходить в те, что пригодятся мне в жизни."


    scene bg handmade with dissolve

    "Вот, например, «Умелые руки». Я туда частенько заглядываю по разным делам. Но, скажем, сидеть и паять микросхемы там разные, или крутить всякие винтики мне не очень интересно."

    "К тому же, у меня аллергия на дым канифоли, который там всё время витает в воздухе."


    scene bg balet_room_empty with dissolve

    "Вот кружок хореографии, это класс! Тем более, что его ведет моя лучшая подруга. Про него расскажу, про первый."

    "Занимаемся мы в свободные часы в помещении музкружка, когда Мику не проводит там свои «Веселые голоса», аккомпанируя на рояле малышам. У них хор."


    scene bg stage with dissolve

    "Или когда нет репетиции нашего ансамбля (вот ещё любимое моё занятие – играть на барабанах, на ударной установке). Проводим их прямо на эстраде лагеря."


    scene an_d10_01_bg with dissolve

    show an_10_01

    "Часов получается немного, но зато мы стараемся «выложиться», как говорит Алиса. Начинаем с физических упражнений, согреваний и растяжки."

    "Утренние занятие с Мегги, пробежка и бокс с тенью, тоже как бы входят в физическую подготовку, но это все-таки не хореография."

    "И у Мегги не кружок. Это мы её с Семёном упросили показать нам приёмчики. Она же морской пехотинец, хотя и скрывает это. Но нам, под большим секретом, про неё рассказала Саманта."


    scene cg balet_room_training with dissolve

    "Сперва начинаем растягиваться. Это очень поможет нам в жизни, так сказала Алиса. На растяжку уходит почти всё занятие."

    "Мику нам аккомпанирует на рояле в такт растяжке. Рояль очень старый и там западает одна клавиша, поэтому Мику играет в другой тональности."

    "Потом мы разучиваем всякие движения. Надо сказать, что эти занятия нам очень помогли, когда Маргарита Павловна разрешила танцы в лагере."

    "В танцевальный кружок (хореографический) ходят пионеры из разных отрядов, в основном, девочки. Но мы обратились к ОД, сказали, что у нас мало мальчиков и нет партнеров изучать парные танцы. И она нам «выделила мальчиков»."

    "Это значит, что часть мальчиков освобождалась от дежурства по кухне и могла провести его, танцуя с нами. Они тогда охотно приходили. Добровольно записались все наши мальчишки, но в основном приходят Толик и Семён."

    "Семён, потому что не ровно дышит к Алисе, а Толик, потому что там у него есть партнерши, которые на обычных танцах в лагере с ним бы танцевать не стали."

    "Из девочек особенно ходит Лена, если не занята в своем кружке (думаю, она заодно «присматривает» за Семёном). Она всё время становится к нему в пару. Ещё ходят Саманта и Атсуи."

    "Женя хочет, но у неё много работы в библиотеке и она стесняется в трико. (Вот дуреха, у неё же лучшая фигура в отряде!) Она прибегает, когда все уходят и занимается с Алисой индивидуально."

    "А ещё Алиса нас ругает что, выражаясь её словами, мы «много жрем». Мы правда все поправились в лагере за эти дни. Но это идет только мне и Мику, потому что мы «доходяги»."

    "Остальные, как выразилась Алиса, «стадо шустрых, пока ещё, бегемотов» (занятие начинается с пробежки вокруг зала)."

    "Ну вот, я рассказала про кружок хореографии."


    scene cg marmalade with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "А, чуть не забыла! У Мику в помещении музкружка живет кот Мармелад."

    "Сокращенно – Марик. Мы все его любим и таскаем ему с кухни вкусненькое. Поэтому он толстый. Ему без нагрузки никак нельзя."

    "Каждый день он приходит в зал хореографии и, как ему кажется, упорно тренируется. Чтобы наконец сбросить лишний вес, заработанный поеданием изумительных котлеток Любови Никаноровны."


    # image an_10_02: # Анимация с Алисой, занимающейся йогой
        

        # "images/an/an10day/an_d10_2_02.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_03.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_01.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_02.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_03.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_01.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_04.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_05.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_06.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_07.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_06.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_05.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_04.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_03.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_08.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_09.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an10day/an_d10_2_10.png" with Dissolve(0.5, alpha=True)
        # pause 0.5

  
        # repeat


    # scene an_d10_2_bg with dissolve

    scene alisa_gymnastics with dissolve


    "Алиса очень гибкая. Она показывает нам все движения и организует растяжку перед каждыми танцами."

    "Все упражнения мы делаем под музыку. Мы очень стараемся сделать как она. Но получается не у всех. Наверное она от природы очень пластичная."

    "Некоторые упражнения не могу повторить даже я, хотя в нашей школе на физкультуре меня всегда ставили в пример другим и хвалили."

    "Но все мои достижения - просто ерунда по сравнению с Алисой. Может быть, к концу каникул проведенных в лагере и я смогу стать такой же гибкой. Посмотрим. Буду упорно заниматься."

    scene alisa_gymnastics with dissolve

    pause (10000000000000000000000.0)


    scene cg alise_training_wcat with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_078.mp3"


    "Марик, тоже любит крутиться возле Алисы, когда она показывает нам растяжку."

    "Алиса нам улыбается, а через улыбку шипит на него: «Брысь, животное!»."

    "Но он не уходит. Однажды, когда она делала упражнения лежа, он вообще забрался ей на спину и катался так, вверх и вниз."

    "Еще он любит сидеть на ноге. Алиса смеялась. Она сказала: «Когда я поднимаю ноги или качаю пресс, то использую его как живую гантелю»."


    scene an_d10_01_bg with dissolve

    "Ну всё, я побежала! Много разных дел сегодня. Допишу еще про кружки, попозже."


    scene an_d10_3_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3" 


    image an_10_03: # Анимация Петрович, Алиса, Ульяна и Лена на лавочке
        
        "images/an/an10day/an_d10_3_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_3_10.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat



    "Вечером всем неохота идти спать и мы собирались возле Петровича, который, как он сам говорил – «заступил на дежурство»."

    "На самом деле никуда он не заступал. Просто из своей каморки, в которой спал днем, перемещался на лавочку возле нашего домика."

    "Оттуда был хорошо виден внутренний двор лагеря и площадь со спортивной площадкой, а также просматривались входы в столовую и библиотеку."

    "Мы уже ждали. Он неторопливо садился на лавочку, отложив суковатую палку в сторону и, закинув ногу в старом разношенном и сто раз чиненом сапоге за ногу, доставал, как он его называл, «прибор»."

    "Прибор, это маленькое, похожее на коробочку приспособление для скручивания самокруток.."
    
    "Преисполненный чувства собственной значительности, Петрович знал, что все мы ждем его вечерних рассказов о «старых добрых временах»."


    scene cg tales_of_petrovich with dissolve

    "Скоро подтянулись и остальные члены отряда. Всем хотелось послушать."


    scene an_d10_3_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


    pe "Трофейная, \n( показывает на коробочку)"

    show an_10_03

    pe "С мертвого фрица снял. Даа… Вдарил его штыком, в самую середку, он и охнуть успел."

    pe "Здоровенный был, гад. Не дождалась Гретхен своего Фрица. Тут, значит, или он меня или я его. Война. \n(все недоверчиво затихли)"


    scene an_d10_3_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3"


    pe "Ну так вот, ребятишки, слушайте… Щас расскажу про прииск."

    "Петрович насыпал строго отмеренную часть махорки в коробочку, внутри которой была намотана папиросная бумага, провел языком по её краю, провернул валик и ловко вытащил из коробочки готовую сигарету."
    
    pe "Ну вот, значит, был тут золотой прииск."


    scene bg stage3

    show sp_smu_001:
        yalign -0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    smu "Враки всё это! Буржуазные сплетни! Про прииск вы нам сто раз рассказывали. Не было тут никакого прииска. И золота отродясь не было! Если бы было, бы мы бы его тут находили, под ногами бы валялось."

    smu "Вы нам лучше про «батискаф» расскажите, что на берегу валяется."


    scene cg tales_of_petrovich with dissolve

    allchar "Какой батискаф? Какой батискаф?"


    scene bg stage3

    show sp_smu_001:
        yalign -0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    smu "Ну бочка такая, с иллюминатором и ржавым люком, которая на Рачьей отмели. От неё еще цепь в омут тянется. Неужели не видели? \n(покосился опасливо на палку Петровича)"


    scene an_d10_3_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


    show sp_pe_006:
        yalign 0.0 subpixel True
        xalign 0.432 subpixel True
        #zoom 0.8

    pe "(Грозно) \nТы кто такой, малец, чтобы старших перебивать?!"


    scene bg stage3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_121.mp3"


    show sp_smu_005:
        yalign 0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    smu "Это противозаконно! Рукоприкладство! Это произвол администрации!"


    scene bg stage4 with dissolve

    show sp_smu_005:
        yalign 0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 0.5

    "Смутьянов вскакивает на сцену эстрады как на трибуну и вытаскивает пачку листовок, написанных от руки."
    
    smu "Вот, тут у меня воззвание к пионерам. Хватит терпеть, товарищи! В компот не докладывают фруктов! Котлеты маленькие, пюре разбавляют молоком!"

    smu "Заставляют обливаться ледяной водой! Мучают интеллектуалов зарядкой. А может, им не показана физическая нагрузка?! Может, мы мозг нации?! Доколе мы будем ходить строем?! Тут вам не плантации какие-нибудь!"

    smu "Мы не рабы! \n(разбрасывает вокруг себя листовки)"


    stop music fadeout 0.5

    queue music "audio/music/z_128.mp3"


    show cg leaflet:
        yalign 0.2 subpixel True
        xalign 0.5 subpixel True

    

    pause (10000000000000000000000.0)


    scene bg stage3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_126.mp3"


    "Тузик бросается на Смутьянова и тот убегает"
  

    scene cg tales_of_petrovich with dissolve
 
 
    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    pe "А ну-ка, дайте мне эту агитацию. На самокрутки пущу её. Гляди-ка. Это же из кабинета Любаши бумага. Наверное, в присутствии спёр..."

    "Присутствием Петрович называл административный корпус, где стояла печатная машинка, на которой Любаша помогала директрисе печатать приказы и распоряжения, которыми была увешана доска информации на площади."
    
    "Пионеры собрали листовки и вручили старику."


    scene an_d10_3_bg with dissolve

    "Даа… Вот такие крикуны и довели страну до цугундера. \n(прячет бумагу в карман телогрейки)" 
    
    pe "Ишь, шельма, как повернул. Котлеты ему маленькие. Хорошие у Любаши котлеты, очень я их уважаю. Правду говорю, гаврики?"
    
    "«Гаврики» дружно закивали."


    scene cg tales_of_petrovich with dissolve

    sl "Да вы не обращайте на него внимания, Архип Петрович. Его тут уже давно никто не слушает кроме второго отряда."

    sl "А что за батискаф на Рачьей отмели?"


    scene an_d10_3_bg with dissolve

    "Петрович улыбнулся и хитро прищурился, отчего всё его лицо стало похоже на печеное яблоко."

    pe "А вот эта история как раз про прииск. Я хотел рассказать. Да тут этот смутьян... \n(прокашлялся)"


    scene cg bathyscaphe
    
    pause (10000000000000000000000.0)
    
    pe "Это не батискаф. Это колокол водолазный. И вот зачем. Когда драга намыла много песку, а дно опустилось (омута-то раньше вовсе не было), то драга стала вынимать со дна самородки."


    scene an_d10_3_bg with dissolve

    ul "Эх, вот бы такой найти!"


    pe "Не перебивай, а то забуду, что хотел сказать. Они значит, тяжелее и оседают вниз. А песочек-то сверху."


    scene cg tales_of_petrovich with dissolve

    el "Мы бы с Шуриком придумали устройство производительнее."


    scene an_d10_3_bg with dissolve

    pe "(Не обращая внимания на реплики) \nНо черпала она медленно и тут, значит, инженер наш покойный и придумал эту штуку."

    pe "Чтобы в ней опускаться и собирать золото прямо со дна. Где среди гальки были вот такенные самородки."
    
    "Петрович показал свой прокуренный большой палец."

    al "Наверное страшно было опускаться?"

    pe "Эт точно! Опускались многие, да и сам я в нём был. Страшно было… Течение норовит перевернуть колокол, а ты стоишь по колено в воде, внутри него, значит, и корячишься."


    scene cg tales_of_petrovich with dissolve

    shu "И много вы там накорячились, деда?"

    pe "А почитай пудов на десять золотишка взяли. Да только лафа эта скоро закончилась. Вычерпали всё."

    el "А что с золотом?"

    pe "Известное дело, в сейф, под замок. Этот сейф и посейчас стоит в том доме, что на болотах."
    
    "Петрович махнул рукой в сторону реки."


    scene bg shouse


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3" 


    pe "Инженер там жил с женой и дочерью. Ждали, что приедет золотопромышленник, да увезет золотишко. Я в охране стоял. Потому как народ тут лихой был."


    scene cg tales_of_petrovich with dissolve

    "Все замолчали. Очевидно, у каждого были свои ассоциации с домом на болотах."


    scene an_d10_3_bg with dissolve

    le "Там страшно... Мы ходили с девчонками, но не вошли внутрь, убежали. Там какие-то звуки все время были и смех женский... Жуть..."


    scene cg tales_of_petrovich with dissolve

    mi "Да... Как вспомню, прямо мурашки."


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    sl "(Пытаясь снять напряжение) \nА что большевики?"

    # stop music fadeout 0.5

    # queue music "audio/music/z_131.mp3"

    scene an_d10_3_bg with dissolve

    pe "Хотели изъять. Только не успели. А когда эту чертову революцию учинили, кинулись комиссары – а в сейфе-то ничего и нет. Руководство сбежало, допрашивать некого. Так и уехали, не солоно хлебавши."

    al "Как нет? А где же оно?"

    pe "Однако, думаю, инженер его положил туда, где раньше оно в природе лежало. На дно, значит. Потому и не нашли. А он-то вернулся, искал. Да вот пропал. А может, нашел. Кто теперь знает?"

    ul "Да, деда, десять пудов это много. Не может быть, чтобы десять. Хоть пуд-то был?"


    scene cg tales_of_petrovich with dissolve

    pe "Был, внученька, был. Вот вы про сома не верили. А он был?"

    "Петрович хитро прищурился"

    ul "Да, это правда. Огромный такой. Сама его видела, как вечером купались. Хотя, может и показалось. С виду-то как бревно, только ныряет. Ну расскажи, деда, про колокол! А в нём сейчас опуститься можно на дно?"

    pe "Ясно дело, можно. Если механизм лебедки починить. Он хоть и ржавый, а я его исправно бы опустил. Да и поднял бы, если подсобил бы кто. Только кто возиться будет? Таких смелых еще поискать."


    scene an_d10_3_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_132.mp3"
  
  
    ul "Я готова!"

    pe "Ишь ты, мелочь. Готова она. Вот. А сам-то я не смогу. Боязно. Я и тогда боялся. Я закрытых помещений жуть как боюсь. Даже в бытовке двери открытыми держу."


    scene cg tales_of_petrovich with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    el "Так деда, там же в лебедке электричества нету. И наверное, обмотка давно тю-тю..."

    pe "А нет там никакого двигателя, сынок. Вручную всё. В наше время лебедки ручные были. И колодцы так рыли большие, и в шахтах работали. Ручками всё, ручками. Система колес разных, шестерни разновеликие, шкивы, рычаги всякие."

    pe "Слыхал про такое?"

    shu "Это вроде древних римских механизмов для подъема тяжестей? Колизей так строили."

    pe "Про Колизей не знаю. А у нас работало. Хотя, что я всё болтаю без толку! А ну-ка, ребятишки, пошли. Покажу вам агрегат. Только чур, не говорите, что я вас туда водил. А то начальство у нас строгое."


    scene bg winch


    stop music fadeout 0.5

    queue music "audio/music/z_140.mp3"


    "И мы пошли на пристань."

    "Там Петрович нам показал лебедку. А я думала сначала, что эта штука лодки вытаскивает на берег. А она для другого."


    show sp_ul_012:
        yalign -0.2 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0


    ul "А как же лебедка с пристани батискаф (ну, то есть колокол), поднимала? Ведь омут там, а она здесь."

    hide sp_ul_012

    show sp_pe_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    pe "Хех! А ты наблюдательная и смышленая. Вот бы мне внучку такую! "

    hide sp_pe_001

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe "Колокол вместе с понтоном буксировали к омуту течением. Ну, сначала привязывали его и помаленьку травили канат. Его течение аккурат в центр омута приносило. Там якорь бросали, ну и вперед."

    hide sp_pe_005

    show sp_ul_014:
        yalign -0.2 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0

    ul "А назад как?"

    hide sp_ul_014

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe "Потом назад таким же способом. Лебедку крутили, канат наматывался и против течения понтон шел назад, к пристани."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_102.mp3"


    show an_10_01

    "Вот такой рассказ Петровича. Завтра я напишу еще про кружки (все не вместилось). И про Странные дела в лагере. Но мне еще нужно все получше разузнать. Как говорит папа, «собрать аргументацию»."

    "Не знаю точно, что это значит (я еще не весь репортерский словарик знаю), но думаю, это УЛИКИ."

    "А уж улики-то я собирать умею!"




    #pause (10000000000000000000000.0)


    scene black with fade

    stop music fadeout 1.0

    jump day11

return







