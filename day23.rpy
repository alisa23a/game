label day23:

    $ style.say_window = style.window

    $ days = 23

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_22_00 = True
    $ im_gal_22_01 = True


    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene cg tent_hike with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_012.mp3"


    show sp_vas_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Спали часов до десяти. Неугомонный Вася встал раньше всех, разжег костер, приготовил завтрак, сварил кофе и терпеливо ждал, когда все проснутся."


    scene cg ul_vas_hike with dissolve

    "Я выбралась из спальника и в одной маечке и трусиках, накрывшись большим полотенцем, подсела к костру."

    "Полотенце соскользнуло с моих плеч, и я заметила, как Вася тут же покраснел и отвернулся. Он отвечал на мои вопросы, глядя куда-то вбок."


    pause (1000000000000000000.0)


    "«Надо же», подумала я, «Какой скромный мальчик»."

    ul "Ты что, вообще не ложился?"

    vas "Нет, просто я, наверное, «жаворонок». Кофе готов, держи кружку. Мне одному неуютно тут. Расскажи мне про Женю, какая она?"


    scene cg tent_hike with dissolve

    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2


    "Из палатки высунулась, привлеченная запахом кофе, Ольга Дмитриевна."


    pause (1000000000000000000.0)


    od "Откуда у нас кофе? Какая прелесть! Драгович, ты просто умничка, что взял кофе! Из дому привез? У нас в лагере кофе достать трудно. Кофе в походе. Сказать кому, не поверят."

    "Так я узнала фамилию Васи. ОД подсела к костру. На ней был купальник, а на бедра она накинула спальник. Она так и сидела, напоминая наполовину вылупившегося из яйца птенца."

    "Я отдала свой кофе Ольге Дмитриевне. Взамен она угостила меня конфеткой."

    od "У меня еще есть."


    scene cg tent_hike with dissolve


    "На запах кофе потянулись остальные. " 


    show sp_meg_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_sam_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "Первыми выбрались из своей палатки Мэгги и Саманта."


    sam "Coffee?"

    meg "Да. На русском звучит почти так же — кофе."


    scene cg tent_hike with dissolve

    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    od "Саманте тоже конфетку. За то, что скауты просыпаются раньше моих ленивых пионеров."


    scene cg tent_hike with dissolve

    show sp_sam_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sam "Конфетка. Это я понимать. Скауты — Один за всех и все за одного!"


    scene cg tent_hike with dissolve

    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    od "О, ты уже и это знаешь по-русски? Ты делаешь успехи. Твоя работа, Мэгги?"


    scene cg tent_hike with dissolve

    show sp_sam_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sam "Нет. Это Семён."


    scene cg tent_hike with dissolve

    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    od "Ну, не важно. Главное, что ты правильно понимаешь то, что лежит в основе пионерского движения. Взаимовыручка! Хвалю."


    scene cg tent_hike with dissolve

    show sp_ul_055:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Держи мой кофе."

    "Я протянула свою кружку Саманте."

    ul "Это уже вторая. Мне много будет."


    scene cg tent_hike with dissolve

    "Мику, Славя и Лена выглянули из своих палаток."


    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    od "Все проснулись? Устроим с утра вместо закаливания марш-бросок на пляж. Все за мной!"


    scene cg tent_hike with dissolve

    "Все дружно закричали ура, но при этом бежать на пляж явно не торопились. За ОД последовали только Саманта с Мэгги и Вася."


    scene cg tent_hike with dissolve

    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 

    "Алиса выбралась из палатки, ухмыляясь."

    al "Как всегда, за комиссаром в атаку никто не побежал. Так он стал героем. Посмертно. Налей-ка мне кофе Улечка. Я вижу, Вася набодяжил целый котелок, на весь лагерь. Золотой мужчинка."


    scene cg tent_hike with dissolve


    "Я тоже на пляж не побежала, решила задержаться. Очень интересно было узнать, чем закончились вечерние посиделки у костра и почему Шурик вчера так злился на Электроника."

    "Вскоре, весь наш походный лагерь пришел в движение. Все галдели у костра, обсуждая вечерние посиделки и купание у ручья. Но никто даже не заикнулся о драке, о которой знали уже все, кроме вожатой."
 

    scene bg lakedeep_path with dissolve

    "Наскоро позавтракав, все стали собираться. Как только солнце поднялось над деревьями, мы уже шагали по тропе в сторону озера, до которого оставался час ходьбы."


    scene bg lakedeep7 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    "Озеро встретило нас ослепительным блеском отраженного в нем солнца. Оно было великолепно. Далеко, насколько видел глаз, простиралась водная гладь, с каймой темно-зеленого с синеватой дымкой, леса."

    "Лагерь решили не разбивать. Нас ждал еще подъем на гору и посещение Землянки Золотоискателя."


    scene bg coast_lake with dissolve

    show sp_od_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    od "Здесь нет поселений. Можете бегать по берегу и купаться. Мальчики отдельно, подальше. А девочки тут."

    hide sp_od_017

    show sp_ul_023:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve
 
    "А можно, мы вместе?"

    hide sp_ul_023

    show sp_od_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "Вместе? Ну, как хотите. Я буду вон там, возле скалы. Позагораю. Далеко не уходите. Здесь много ракушек на берегу. Через час сбор и снова на тропу."

    od "До конца дня, нам надо вернуться от землянки Золотоискателя на этот берег. Тут заночуем, а утром уйдем в лагерь. Чтобы я никого не искала. Слышите? Василий, проследи!"

    hide sp_od_017


    "Мы убежали искать ракушки. Я нашла аж шесть штук. Они были как шапочки звездочетов. Но внутри пустые."

    "Вася сказал, что ракушки выбрасывает на берег, когда их обитатели покидают их. Вот бы увидеть эту живность. Я взяла их на память."


    scene cg flash_lake with dissolve


    stop music fadeout 0.5

    queue music "audio/music/prolog.mp3"


    "Потом  я стала смотреть на тот берег. Там что-то сверкало как зеркальце. Я сказала об этом Славе. Она тоже долго смотрела."

    show sp_ul_021:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve
 
    ul "Может быть, рыбаки?"

    hide sp_ul_021
 

    show sp_sl_020:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve
 
    sl "Ольга Дмитриевна сказала, что ту никто не живет. Странно. "

    hide sp_sl_020


    scene cg boat_lake_day with dissolve

    "Я сбегала к рюкзаку и достала папин бинокль. В бинокль была видна лодка. А в лодке какая-то фигура. Маленькая в сравнении с лодкой... Как ребенок."

    "Кто бы это мог быть? Но точно не из нашего лагеря. Наверное, кто-то рыбачил. Вот бы выпросить у этого рыбака лодку и покататься по озеру!"


    scene cg hike2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_516.mp3"


    "Через час, немного подкрепившись печеньем и холодным чаем из фляг, мы снова шли в гору."

    "Подъем был все круче. Все выбились из сил. Мы сделали короткий привал. Потом небольшой рывок по склону и мы оказались на хребте."


    scene bg bravepath2 with dissolve

    "По хребту шла тропа, идти было легко и весело. Душный, тяжелый воздух сменился ветерком, и все, наконец, вздохнули с облегчением. Так мы добрались до Землянки."

 
    scene bg goldd with dissolve

    "Землянка хорошо сохранилась. Но скорее, это все-таки была нора. Ольга Дмитриевна рассказала какую-то выдуманную легенду о золотоискателе, который погиб в этих местах."

    "Это была страшилка, чтобы мы не разбегались далеко. Потому что рассказ заканчивался словами: «И когда он зашел в чащобу, на него напал медведь и съел»."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    sem "А золото?"

    hide sp_sem_016


    show sp_je_017 at flip:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 
    with dissolve

    je "Как можно говорить о золоте,  когда Ольга Дмитриевна рассказывает про гибель человека?"

    hide sp_je_017


    show sp_od_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "Золото всегда приводит к трагедии. И оно никому не принесло счастья. Понял, Персунов? Вот вам пример. Всему виной алчность. Кто-то может считать это совпадением, а я думаю, что это судьба."

    hide sp_od_017


    show sp_al_055:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    al "А мы слышали, что это золото искали большевики."

    hide sp_al_055


    show sp_od_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "От кого слышали?"

    hide sp_od_017


    show sp_al_055:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    al "От Архипа Петровича."

    hide sp_al_055
   
    show sp_od_019:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "(Улыбается) \nА, понятно, вы его больше слушайте, он вам еще не то расскажет. В общем, мираж это. Не было никакого золота. Потому, что еще при царе его уже всё выкопали."

    od "Прииски, о которых рассказывает вам Петрович, давно закрыты, в виду истощения жилы. И даже если бы что-то было, то поверьте мне, местные жители давно бы это нашли. А что, у кого-то есть желание поискать?"

    hide sp_od_019

    show sp_shu_004:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    shu "(Ковыряя землю у входа в землянку) \nДа, я знаю, оно закопано под землянкой или у входа. Вот чуйка у меня."

    hide sp_shu_004


    show sp_od_019:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "(Со смехом) \nВот, третий поход сюда вожу, и всегда одно и то же! Все копают тут землю. Вы неисправимые романтики. Вы знаете об этом?"

    hide sp_od_019


    show sp_tol_009:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Я там только что всё обследовал, Ольга Дмитриевна. Золота нет. Точно."

    hide sp_tol_009


    "Все засмеялись."


    show sp_od_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    od "Нам нужно вернуться к озеру. Здесь быстро темнеет. Давайте, пошевеливайтесь!"

    hide sp_od_017


    scene bg lakedeep2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_527.mp3"


    "Дошли быстро. Спускаться с горы было гораздо легче, чем карабкаться на неё. Спустившись к озеру, прошли вдоль него дальше от места прежнего привала, нашли удобное для лагеря место. Поставили палатки."

    "Мальчишки ушли рыбачить. Точнее, только Толик захватил удочку, но рыбачить договорились по очереди. Ольга Дмитриевна еще в начале похода сказала, что в озере водится много рыбы."

    "Девочки разбрелись по берегу собирать ракушки. Кто-то — купаться."


    scene cg tent_hike with dissolve

    "К вечеру все стали собираться у костра. Приготовили ужин, открыв солидный запас взятых с собой консервов."


    show sp_vas_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "У Васи, как выяснилось, был день рождения, ему исполнялось восемнадцать. Он, из скромности, об этом умолчал, но Ольга Дмитриевна, как оказалось, помнила и объявила об этом торжественно."

    "Все обнимали красного от смущения вожатого. Решили не экономить еду и отметить событие. Ужин получился сытным."

    hide sp_vas_002


    scene cg camp_lake with dissolve

    "Когда все залезли в палатки, мы с Алисой стали обсуждать странный свет на том берегу."

    pause (10000000000000000000000.0)


    scene cg boat_lake with dissolve

    pause (10000000000000000000000.0)



    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "ОНО все еще там!"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Серьезная рыбалка."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А может и не рыбалка. Может быть, это ныряльщицы за жемчугом. Мне Атсуи рассказывала, в Японии есть такие."

    hide sp_ul_021


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Скажешь тоже. То океан, а тут озеро. Ольга Дмитриевна сказала, тут необитаемые места."

    hide sp_al_037


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Она не все знает. А я знаю, что есть морской жемчуг, а есть речной. А вот озерный... Не знаю."

    ul "Слушай, Алиса, давай метнемся кабанчиком на тот берег? Тут, если по берегу, будет, может, километр или два, не больше."

    ul "Если там лодка, то сплаваем сюда напрямую. Смотри,  какая луна. Я спать совсем не хочу. А ты?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Идея хорошая. Я взяла запасные батарейки. Только надо дождаться, пока Вася уйдет от костра. Он нас спалит."

    hide sp_al_055


    scene cg moon_lake with dissolve

    "Когда мы выглянули из палатки через час, у костра уже никого не было. Наш походный лагерь мирно спал."

    "Только у кибернетиков светился огонек. Они о чем то шептались, и я даже расслышала слова «надо сходить» и дальше неразборчиво. Похоже, не нам одним пришла в голову идея насчет лодки."

    "Тем более, надо было спешить."


    scene bg coast4 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_533.mp3"


    "Незаметно выскользнув из лагеря, мы отправились вдоль берега. Песок был твердый, спрессованный и идти было легко."

    "Фонарик выхватывал только небольшой кусочек берега перед нами, и мы старались не спешить, чтобы не оступиться."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Надо бы найти тропу. Наверняка есть тропа вокруг озера. К тому же, если это был рыбак, то скорее всего, скоро мы увидим свет костра."

    al "А если мы всё время будем идти по берегу, то зайдем в какие-нибудь плавни, камыши и увязнем там."

    hide sp_al_056

    "Это было разумно и я согласилась."


    scene bg moon_forest with dissolve

    "Мы ушли от берега и пошли по лесу, не выпуская из поля зрения луну, которая указывала нам направление на озеро."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Если луна всегда будет справа, значит мы идем верно. Знать бы только, когда повернуть."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Будем считать шаги. Если мы идем пять километров в час, то значит через двадцать минут мы дойдем до места, где озеро заканчивается. И тогда надо будет повернуть направо и идти прямо на луну."

    hide sp_ul_021


    scene bg forest with dissolve

    "Она согласилась, и мы так и сделали. Луна смещалась правее. Но Алиса сказала, что это нормально, так как луна тоже движется."

    "Лес становился все гуще. Темнело. Через час стало ясно, что мы заблудились."


    scene bg outback with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну и чащоба. Просто глухомань. В какой стороне теперь озеро?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Мы сделали глупость, луна ненадежный ориентир. Давай пойдем назад. Хотя теперь, обратную дорогу мы точно не найдем. Найти ночью следы невозможно."

    hide sp_al_056



    $ renpy.music.set_volume(0.00, delay=1.0, channel='music')

    play miscSounds "audio/music/z_1000.mp3" noloop

    "Мы обреченно сели на землю и стали прислушиваться. Где-то ухал филин."

    stop miscSounds fadeout 1.0


    $ renpy.music.set_volume(1.00, delay=1.0, channel='music')


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Может, будем ориентироваться на свет костра? Ведь в лагере всё еще горит костер."

    hide sp_al_056


    stop music fadeout 0.5

    queue music "audio/music/z_909.mp3"


    "Мы стали всматриваться в темноту. Вскоре от напряжения у меня разболелась голова."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Может, покричать?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Мы идем уже час. Представляешь, как далеко мы ушли? Кто нас услышит? Нет, это бесполезно. Надо ждать рассвета."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Рассвета? Но до рассвета еще уйма времени. Я за то, чтобы идти."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Уля, это глупая идея, поверь."

    hide sp_al_056

    "Мы прошли еще немного и вышли на, как нам показалось, полянку."


    scene bg glade_night with dissolve
 
    "В темноте почти ничего не было видно, луна ушла за тучи, и мы окончательно потеряли ориентиры. Только какая-то одинокая звезда еще слабо светила в небе."

    "Тогда мы решили остановиться тут и заночевать. Все лучше, чем в лесу. Только опустившись на землю, мы поняли, как смертельно устали. Сев спина к спине, мы тут же заснули."





    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day24

return 