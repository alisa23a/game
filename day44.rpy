label day44:

    $ style.say_window = style.window

    $ days = 44

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_43_00 = True
    $ im_gal_43_01 = True
    $ im_gal_43_02 = True


    show screen current_day_bad_1 with fade


    play music "audio/music/z_1003.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day_bad_1

    $ show_quick_menu = True


    scene an_d43_42 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "Утром, когда дождь ещё шел, но уже не так сильно, физрук отправился в пещеру."


    show sp_fi_017:
        yalign 0.15 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3
    with dissolve

    "Он вернулся и привёл с собой ночевавших в пещере малышей вместе с вожатыми. За исключением пятерых человек."

    "Когда физрук пришёл в пещеру, вожатые уже знали, что три мальчика из седьмого отряда и двое детей из шестого, брат и сестра, пропали."

    hide sp_fi_017


    scene cg meeting_sad with dissolve


    "Тогда Ольга Дмитриевна разделила первый второй и третий отряды на поисковые группы, и они начали поиски."


    scene bg bridge with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_je_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Семён и Женя отправились искать малышей в сторону моста по старой дороге."


    scene bg ford3 with dissolve

    show sp_sl_021:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    show sp_mi_013:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Славя и Мику пошли в сторону Брода."


    scene bg camp3 with dissolve

    show sp_le_015:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.25

    show sp_at_021:
        yalign 0.1 subpixel True
        xalign 0.9 subpixel True
        zoom 1.1

    "Лена и Атсуи искали в окрестностях лагеря."


    scene bg pool_big_catfish_morning with dissolve

    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Юля ушла в сторону Омута и дома на Болотах."


    scene bg hetu with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_149.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    "А мы с Алисой решили прошерстить окрестности пещеры (ну не могли же они далеко уйти!), Поселок Горняков, и заодно пошли посмотреть не спрятались ли они в угодьях Ежа и Черепахи."


    scene bg burleyka3 with dissolve

    show sp_fi_015:
        yalign 0.15 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3


    "Физрук сел в лодку и сказал, что спустится до самых порогов, потому что думает, что дети ушли к реке."


    scene bg boat_station2 with dissolve

    show sp_pe_011:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Когда мы сказали Петровичу о том, что физрук уплыл, он очень ругался. Сказал, что сейчас река поднялась, и Тараса Юрьевича унесет в ущелье быстрым течением, где бросит на камни."

    "Петрович тут же стал отвязывать лодку, чтобы плыть за ним и вернуть."


    scene cg river_monster with dissolve

    "Мы предупредили Петровича о том, что там водится ТВАРЬ, но он только махнул на нас рукой. Но мы настаивали, и он положил в лодку, на всякий случай, пару шашек динамита, багор и топор."


    scene bg newtcreek with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Остальные аукали, бродя у Ручья тритонов"


    scene bg crsh with dissolve

    "И Рачьей отмели."

    "Дальше, боясь что еще кто-то потеряется, Ольга Дмитриевна отозвала их в лагерь."


    scene bg hetu with dissolve

    "Мы обошли всё, даже еще раз прошли по пещере, но так и не нашли никого, а сами чуть не потерялись."


    stop music fadeout 0.5

    queue music "audio/music/z_047.mp3" noloop


    "Но потом услышали звук взрыва (два раза) и поняли, что Петрович что-то взорвал на реке. И мы пошли на этот шум. "


    scene bg boat_bow with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    show sp_pe_012:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "В районе заброшенного пляжа мы увидели Петровича."

    "Сидя в лодке, он подтягивал к себе багром плавающие в кровище куски какой-то рыбы или зверя."

    "Он тяжело дышал и, забирая нас в лодку, сказал:"

    "«Это просто... (дальше такое слово, что его лучше не писать) такая... (тут тоже пропущу), и я бросил шашку, а эту (тут снова пропуск)»"

    "«Она на меня кинулась, и тогда я её... (тут тоже пропуск). И тут динамит как... (тут прям совсем нехорошее слово)! И вот, смотрите что осталось от зверюги»."

    "Вот такой рассказ Петровича. А мы порадовались, что наконец наша Бурлейка перестала быть зоной особой опасности для пионеров. Ну, не считая Омута и Водоворота."

    "Но Петрович так и не нашел физрука. У нас с Алисой были две версии."


    scene cg fi_drowned with dissolve

    "Первая – Тарас Юрьевич утонул в реке."


    pause (10000000000000000000000.0)


    scene cg river_monster2 with dissolve

    "Вторая - его сожрала ТВАРЬ."


    pause (10000000000000000000000.0)


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_058.mp3"


    "Все поисковые группы, кроме Жени и Семёна, вернулись."


    show sp_le_015:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.25
    with dissolve

    "Больше всех переживала Лена. Она говорила: «Я должна была пойти с ними». Кажется, она ревнует Семёна к Жене."

    hide sp_le_015


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "А Алиса усмехнулась и шепнула мне:"

    al "Поздно пить боржоми, когда почки отвалились."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Это было грубо и зло, и я спросила:"

    ul "Всё ещё не можешь забыть Сёму?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса хмыкнула и ответила:"

    al "Нет, я люблю Жана. Это просто по дурости сказала. Я, наверно, испорченная. Что во мне нашёл Жан, до сих пор не пойму? Ну извини, маленькая."

    "Она обняла меня и чуть прижала к себе. А я подумала, что ничего она не испорченная. Просто сказала от обиды на жизнь. Ну, так бывает. Жизнь её не баловала."

    "И из друзей у неё была только я. Ну, остальные тоже. Но скорее как приятели. А мы «не разлей вода»."

    hide sp_al_055

    "Когда мы уже отчаялись дождаться Женю и Семёна, отправившихся на поиски малышей, они наконец появились. И с ними все пятеро пропавших малышей. Голодные, грязные, но с веселыми горящими глазами."

    "Оказывается, Женя и Семён нашли их на Карьере."


    scene bg carier with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_196.mp3"


    "Как они зашли так далеко, осталось загадкой. Что бы их ни спрашивали, они отвечали одинаково: «заблудились»."

    "По версии Алисы, они испугались грозы и побежали на север. Потом заблудились. Вышли на старую железную дорогу, оттуда по ней на мост, а потом спустились в карьер."

    "На вопрос «ЧТО ВЫ ДЕЛАЛИ В КАРЬЕРЕ?», они смущались и не хотели отвечать. Наверное, боялись что их накажут."

    "Свет на ситуацию пролил Семён, рассказав о том, что они застали детей играющими в ПИРАТОВ."

    "На карьере было много старых пиломатериалов. Часть из них представляли собой огромные доски."


    scene cg carier_pirates with dissolve


    "Когда карьер залила вода, образовался естественный бассейн,  довольно мелкий, чтобы утонуть, но достаточный глубокий, чтобы плавать на досках."

    "За игрой они забыли о голоде, равно как и о том, что их ищут и ждут. Женя и Семён пришли как раз вовремя."

    "Столовая гудела от голосов детей, которые делились с другими пионерами пережитым опытом. Кажется, после этих рассказов весь лагерь готов был идти на карьер играть в пиратов."


    pause (10000000000000000000000.0)


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_102.mp3"


    "Но в лагере после бури, наконец, восстановилась связь, и Маргарита Павловна вызвала автобусы (этот день был последним днём пребывания для младших групп)."

    "Вызвала, чтобы отправить, наконец, первую партию пионеров домой. Назначены были сборы. Все собирали рюкзаки и искали потерянные вещи."


    scene cg buss_dif with dissolve

    "Вскоре прибыли четыре автобуса."

    "В них приехала часть родителей, встревоженных отсутствием известий из лагеря и невозможностью прорваться сквозь непогоду."

    "Основная часть пионеров ничего не помнила о восстании (уколы Виолы сделали свое дело), а малыши ушедшие на карьер, говорили сбивчиво, бессвязно и в основном об играх."

    "Так МП удалось спустить всё «на тормозах». Мы же были «немы как рыбы» и на вопросы родителей «как вы тут отдыхали» отвечали только: «ЛУЧШЕ НЕ БЫВАЕТ»."


    scene bg camp_artifacts with dissolve

    "Скоро 4-й, 5-й, 6-й, 7-й, и 8-й отряды уехали. В лагере остались только наш и два отряда старших групп. Лагерь сразу как будто опустел."

    "МП разрешила купаться и кататься на лодках в оставшиеся полторы недели. На вопрос Ольги, как выстраивать отдых групп, ответила устало:"


    show sp_mp_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    mp "Делайте что хотите, Ольга Дмитриевна, Вы достаточно опытный педагог. Я предоставляю Вам право решать все административные вопросы самостоятельно, побудьте пока за меня."

    mp "Майя, Виола с Архипом Петровичем и пионеры первого отряда Вам помогут. Дайте мне немного отдохнуть. Ещё немного и я сойду с ума от всей этой вакханалии."

    mp "Надо решить вопрос с исчезновением Тараса Юрьевича и все как-то объяснить «органам». Звоните, если что."

    hide sp_mp_003


    scene bg handmade with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"


    "Шурика с Электроником что-то давно не было видно. И я предложила Алисе заглянуть в кружок «Умелые руки», а заодно забрать у кибернетиков фонарики. Так и сделали."


    image an_44_01: # Анимация Эля двигает глазами


        "images/an/an44day/an_d44_01.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_03.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_01.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_03.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_04.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_01.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_05.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_06.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_07.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_06.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_05.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_08.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_09.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an44day/an_d44_06.png" with Dissolve(0.5, alpha=True)
        pause 1.0


        repeat

    show an_44_01:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    "В кружке мы увидели следующую сцену."

    "На столе сидела кукла. Она о чем-то живо беседовала с Электроником, а Шурик сидел на полу, держась за сердце."

    "Мы тоже опешили."

    "ОНА ОЖИЛА!"

    "Однако мы с Алисой, в отличие от остальных, быстро пришли в себя, потому что догадывались, в чём дело."

    "Я шепнула Алисе:"


    scene bg handmade with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Надо сказать этим двоим, чтобы мечтали поосторожнее, а то они нам тут насоздают монстров похуже ТВАРИ из реки."

    ul "Во всяком случае, пока эта МАШИНА всё ещё работает."


    scene bg genda_looks_right with dissolve

    "Кстати, на тот момент вибрация прекратилась. Я быстро выскочила из кружка, чтобы посмотреть на памятник."

    "Генда больше не смотрел на библиотеку, а, как всегда, был развернут лицом к нашему домику. Так и есть!"


    scene bg handmade with dissolve

    # show sp_elya_001:
        # yalign 0.05 subpixel True
        # xalign 0.45 subpixel True
        # zoom 1.2


    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2


    "Между тем то, что происходило в кружке, напоминало кадры фантастического фильма."

    "Во-первых, это была уже не неуклюжая кукла, а био-робот (как выразился Электроник)."

    "Все её проводки и шарниры как бы были на месте, но они почему-то стали мягкими на вид и на ощупь похожими на живые."

    "А ещё она улыбалась, смеялась и шутила. Это было странно, ведь роботы обычно, насколько мне объяснял папа, могут только то, что заложено в них ПРОГРАММОЙ. А она была совсем как человек!"

    "И я подумала, как удивятся наши начальники, когда увидят такое! Это событие даже на время заслонило историю с поисками малышей, настолько оно было удивительным."


    scene cg meeting_elya with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_301.mp3"


    "Потом была кутерьма. Набежали пионеры, все столпились, разглядывали девочку-робота и общались с ней. Она оказалась довольно эрудированной. В смысле, умной для робота."


    pause (10000000000000000000000.0)


    scene bg handmade with dissolve


    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2


    show sp_shu_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "А Электроник с Шуриком прямо сияли оба. И не отходили от неё ни на шаг."

    "Конечно, все хотели дать ей имя."


    scene bg handmade with dissolve


    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_el_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Но Электроник указывая на девочку-робота сказал, что они с Шуриком уже дали ей имя в честь автора идеи. Эля Троник."


    scene bg handmade with dissolve

    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Все согласились, что имя ей идет. И с тем, что авторы имеют право на то, чтобы назвать свое детище как им заблагорассудится."

    "Но я хотела назвать ее Лолой. Впрочем, Эля тоже красивое имя."


    scene bg handmade with dissolve


    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_shu_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Кажется, Шурик влюбился в Элю. Он очень влюбчивый. Сначала Женя, потом Атсуи, а теперь Эля..."

    "Но я не знаю, она же робот! Как говорил мой папа, «Воистину, чудны дела твои, Господи!»"


    scene bg handmade with dissolve

    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Я всё трогала её, у неё такая «кожа» нежная, прямо не знаю, из чего сделана. И ещё блеск такой в глазах, прямо человеческий."

    "И вообще, она красивая. Ну, по меркам машины. Я думаю, я бы с ней подружилась."


    scene bg handmade with dissolve

    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    pause (10000000000000000000000.0)

    stop music fadeout 0.5

    queue music "audio/music/dolls.mp3"



    "Из ниток и веселых лоскутков
    \nНадежд и снов одежды будет шиться 
    \nНо оживут они, когда любовь
    \nНаполнит светом кукольные лица"

    "Но любовь приходит
    \nС лиц снимает маски
    \nОткрывает сцену
    \nНачинает сказку"

    "Жизнь человечков маленьких проста 
    \nИ в сундуках они лежат до срока
    \nНо вдруг наполнит музыка уста
    \nСловами благородства и порока" 

    "Но любовь приходит
    \nС лиц снимает маски
    \nШтопает прорехи 
    \nОбновляет краски"

    "Седой творец волшебной нитью шьёт
    \nСудьбы моей простое одеяло
    \nНо жаль в нем много темных лоскутков 
    \nА белых так на удивленье мало"

    "Пусть ангелы поют не в унисон
    \nИ нот добра, добра, кому-то мало
    \nУ счастья слишком простенький фасон
    \nИ ткань местами сшита как попало"

    "Но любовь приходит
    \nС лиц снимает маски
    \nСерый холст грунтует
    \nИ рисует сказку"




    scene bg handmade with dissolve

    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    pause (10000000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_301.mp3"


    "Я даже спросила её, может ли она чувствовать, и так слегка её ущипнула."

    hide sp_elya_001

    show sp_elya_014:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    "А она сказала «ОЙ!»"

    hide sp_elya_014


    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3
    with dissolve

    "Ну а Славя как всегда сразу заявила, что её надо принять в пионеры, в наш отряд, как Юлю."


    scene cg meeting_elya with dissolve

    "И все стали обсуждать, как это оформить по правилам пионерской организации. Потому что правил для роботов не было ещё. И мы их должны были придумать."

    "Чтобы потом всех роботов, принимали в пионеры по нашему «уставу». Хотя я думаю, что таких, как Эля больше не будет. Её же создала МАШИНА и воображение кибернетиков."

    "Человечество, как говорил сам Электроник, ещё не достигло таких высот развития искусственного интеллекта."


    scene bg handmade with dissolve

    show sp_elya_017:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Потом завхоз выдала ей пионерскую форму. Та сидела на ней немножко мешковато, но девочки быстро подшили ей рубашку и юбку по размеру."

    "После этого Эля выглядела, в общем, очень даже замечательно."


    scene cg ul_sam with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_009.mp3"


    "Я уже писала, что мы очень подружились с Самантой. Все мы знали, что скоро Саманта от нас уедет. Было грустно."


    pause (10000000000000000000000.0)


    "А я подумала, интересно, вела ли Саманта дневник? Точно помню, что в первые дни она таскала его с собой и постоянно что-то в него писала."

    "До того момента, как у нас отобрали все дневники."


    scene cg sam_diary_p1 with dissolve

    "Мне кажется, ее дневник всё ещё хранился у ОД. Наверное, она забыла про него. Тогда (если я до него доберусь) я многое узнаю про неё."


    pause (10000000000000000000000.0)


    scene cg maggie_gun with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_417.mp3"


    "Ну и всякие тайны про Мэгги. Все-таки Мэгги загадочная личность. И вообще. Никогда до этого не видела настоящего «зеленого берета», да еще и женщину. Мне повезло."

    "(Вот тут я ее нарисовала такой агентшей 007)"


    pause (10000000000000000000000.0)


    scene cg sam_parade with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_901.mp3"


    "На прощанье решили сделать торжество. Объявление о нем вывесили заранее. В честь Саманты устроили торжественную линейку и парад."


    pause (10000000000000000000000.0)


    "Потом был маленький концерт. В основном читали стихи, посвященные Саманте и русско-американской дружбе. Потом были танцы."


    scene cg concert_ad2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_454.mp3"


    pause (10000000000000000000000.0)


    "В этот раз мы сами играли на сцене. Ольга Дмитриевна в отсутствие директрисы дала нам поблажку."

    "Например, в тот вечер у нас были юбочки запрещенной длинны. Совсем немного. Ну, мы их подшили перед самым концертом."

    "Ольга Дмитриевна только ахнула, но уже ничего сделать было нельзя, и она махнула на это рукой."

    "Даже у меня такая была. Хоть я и барабанщица, и моей юбочки было не видно, её закрывал бас барабан, но я так поставила его, чтобы он стоял немного сбоку."

    "Например, было видно, как я отбиваю ногой в такт музыке. Ну, и ещё на поклон выходила."


    scene cg dancing with dissolve

    "Потом мы поставили записи музыки с кассеты Саманты, через усилитель и сами потанцевали. Саманта в это вечер была «нарасхват» Все хотели с ней потанцевать."


    scene cg sem_meg_dancing with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_460.mp3"


    "Даже Мэгги приглашали, хотя она была на голову выше своих кавалеров. Кроме Семёна, конечно. Он тоже с ней танцевал."

    "Меня мальчишки много приглашали. А Семён ни разу. Наверное, потому, что его не отпускали поклонницы."


    scene cg sem_ul_dancing2 with dissolve

    "Но я протиснулась к нему, всех растолкала и увела его с собой в середину толпы, как в прошлый раз. И там мы станцевали медленный танец."


    pause (10000000000000000000000.0)


    "И вот там он... Ладно, не буду об этом, потом напишу. Ну, чтобы вы не думали ничего такого... Милые глупости."

    "Ну там, комплименты были с его стороны. Но я знала, что выгляжу здорово. Мне об этом все девочки сказали."


    scene cg ul_loose_hair with dissolve

    "Я выпросила у Мику одни чулочки с рисунком, и выглядела старше в них. Папа был прав, ножки у меня как он выразился, были «с перспективой»."


    pause (10000000000000000000000.0)


    "Даже Семён всё время смотрел на них, а я ему говорила: «В глаза мне смотри, в глаза» (это я у Алисы научилась)."

    "А он вдруг покраснел (интересно, о чем он думал?). Вот никто не верит, а он правда покраснел. Первый раз за весь лагерь. Ну и пусть не верят. А я точно знаю."

    "И я спросила его прямо (я же очень прямолинейная), что было бы, если бы он не знал, что я это. Не Ульяна, а там, скажем, встретил бы меня где-нибудь в другое время, в другом месте."

    "Как бы он смотрел на меня, как на «сестру» или... по-другому?"

    "И он сказал: «Если бы ты не была мне как сестра...»"

    "И тут музыка закончилась. И он не закончил фразу, а только еще больше покраснел. Я так ничего и не узнала. Черт! Так было обидно! Но я мысленно за него договорила. Я же догадливая."


    scene bg square with dissolve

    "И я еще хотела с ним потанцевать, но тут танцы кончились."

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    "Было поздно, и Ольга Дмитриевна не дала нам посидеть на лавочке возле спортплощадки. Сказала, что Саманте завтра надо рано собираться. Что надо дать ей отдохнуть, и загнала нас спать."



 




    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day45

return