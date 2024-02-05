label day23:

    $ days = 23

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music fadeout 1.0


    play music "audio/music/z_012.mp3"


    scene cg tent_hike with dissolve

    show sp_vas_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Спали часов до десяти. Неугомонный Вася встал раньше всех, разжег костер, приготовил завтрак, сварил кофе и терпеливо ждал когда все проснутся."


    scene cg ul_vas_hike with dissolve

    "Я выбралась из спальника и в одной маечке и трусиках, накрывшись большим полотенцем, подсела к костру."

    "Полотенце соскользнуло с моих плеч, и я заметила, как Вася тут же покраснел и отвернулся. Он отвечал на мои вопросы, глядя куда-то в бок."

    "«Надо же», подумала я, «Какой скромный мальчик»."

    ul "Ты что, вообще не ложился?"

    vas "Нет, просто я, наверное, «жаворонок». Кофе готов, держи кружку. Мне одному неуютно тут. Расскажи мне про Женю, какая она."


    scene cg tent_hike with dissolve

    show sp_od_018:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2


    "Из палатки высунулась, привлеченная запахом кофе, Ольга Дмитриевна."

    od "Откуда у нас кофе? Какая прелесть! Драгович, ты просто умничка, что взял кофе! Из дому привез? У нас в лагере кофе достать трудно. Кофе в походе. Сказать кому, не поверят."

    "Так я узнала фамилию Васи. ОД подсела к костру. На ней был купальник, а на бедра она накинула спальник. Она так и сидела, напоминая наполовину вылупившегося из яйца птенца."

    "Я отдала свой кофе Ольге Дмитриевне. Взамен она угостила меня конфеткой."

    od "У меня еще есть."

    hide sp_od_018

    "Вскоре, весь наш походный лагерь пришел в движение. Все галдели у костра, обсуждая вечерние посиделки и купание у ручья. Но никто даже не заикнулся о драке, о которой знали уже все, кроме вожатой."
 

    scene bg lakedeep_path with dissolve

    "Наскоро позавтракав, все стали собираться. Как только солнце поднялось над деревьями, мы уже шагали по тропе в сторону озера, до которого оставался час ходьбы."


    stop music fadeout 1.0


    play music "audio/music/z_055.mp3"


    scene bg lakedeep7 with dissolve


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


    stop music fadeout 1.0


    play music "audio/music/prolog.mp3"

    scene cg flash_lake with dissolve

    "Потом  я стала смотреть на тот берег. Там что-то сверкало как зеркальце. Я сказала об этом Славе. Она тоже долго смотрела."

    show sp_ul_021:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve
 
    "Может быть, рыбаки?"

    hide sp_ul_021
 

    show sp_sl_020:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve
 
    "Ольга Дмитриевна сказала, что ту никто не живет. Странно. "

    hide sp_sl_020


    scene cg boat_lake_day with dissolve

    "Я сбегала к рюкзаку и достала папин бинокль. В бинокль была видна лодка. А в лодке какая-то фигура. Маленькая в сравнении с лодкой... Как ребенок."

    "Кто бы это мог быть? Но точно, не из нашего лагеря. Наверное, кто-то рыбачил. Вот бы выпросить у этого рыбака лодку и покататься по озеру!"


    stop music fadeout 1.0


    play music "audio/music/z_516.mp3"


    scene cg hike2 with dissolve

    "Через час, немного подкрепившись печеньем и холодным чаем из фляг, мы снова шли в гору."

    "Подъем был все круче. Все выбились из сил. Мы сделали короткий привал. Потом небольшой рывок по склону и мы оказались на хребте."


    scene bg bravepath2 with dissolve

    "По хребту шла тропа, идти было легко и весело. Душный, тяжелый воздух сменился ветерком, и все, наконец, вздохнули с облегчением. Так мы добрались до Землянки."

 
    scene bg goldd with dissolve

    "Землянка хорошо сохранилась. Но скорее, это все-таки была нора. Ольга Дмитриевна рассказала, какую-то выдуманную легенду о золотоискателе, который погиб в этих местах."

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

    od "(Улыбается) \nА, понятно, вы его больше слушайте, он вам еще не то расскажет. В общем, мираж это. Не было никакого золота. Потому что, еще при царе его уже всё выкопали."

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


    stop music fadeout 1.0


    play music "audio/music/z_527.mp3"


    scene bg lakedeep2 with dissolve

    "Дошли быстро. Спускаться с горы было гораздо легче, чем карабкаться на неё. Спустившись к озеру, прошли вдоль него дальше от места прежнего привала, нашли удобное для лагеря место. Поставили палатки."

    "Мальчишки ушли рыбачить. Точнее, только Толик захватил удочку, но рыбачить договорились по очереди. Ольга Дмитриевна еще в начале похода сказала, что в озере водится много рыбы."

    "Девочки разбрелись по берегу собирать ракушки. Кто-то купаться."


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

    ul "Слушай, Алиса, давай метнемся кабанчиком на тот берег? Тут, если по берегу, будет может, километр или два, не больше."

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


    stop music fadeout 1.0


    play music "audio/music/z_533.mp3"

    scene bg coast4 with dissolve

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


    stop music fadeout 1.0


    play music "audio/music/z_909.mp3"

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

    "Мы прошли еще немного и вышли, на, как нам показалось, полянку."


    scene bg glade_night with dissolve
 
    "В темноте почти ничего не было видно, луна ушла за тучи, и мы окончательно потеряли ориентиры. Только какая-то одинокая звезда еще слабо светила в небе."

    "Тогда мы решили остановиться тут и заночевать. Все лучше, чем в лесу. Только опустившись на землю, мы поняли, как смертельно устали. Сев спина к спине, мы тут же заснули."


    stop music fadeout 1.0


    play music "audio/music/z_533.mp3"


    scene cg al_awaking2 with dissolve


    "Когда я проснулась, мы уже лежали обнявшись. Алиса еще спала. Было прохладно, и мы, наверное, инстинктивно прижались друг к другу, чтобы не замерзнуть."

    "Я огляделась. Это действительно была маленькая уютная полянка в лесу. С огромными желтыми цветами и бабочками."

    "Я любовалась ими и жалела, что так мало знаю о природе. Таких бабочек и цветов я раньше никогда не видела."

    "Где-то далеко послышался странный звук. Но как я ни прислушивалась, не смогла понять, что это. Может быть, нас зовут ребята? Было ещё слишком рано, чтобы нас хватились в лагере."

    "Я растолкала Алису. Какое то время мы вместе смотрели на порхающих бабочек. Алиса была очарована ими как и я."

    image an_23_01: # Анимация с Ульяной Алисой, наблюдающими за бабочками
        
        "images/an/an23day/an_d23_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    scene an_23_01 with dissolve

    pause (10000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"
   

    scene cg al_awaking with dissolve

    "Но, как бы там ни было, надо было идти на звук. Алиса выглядела забавно. К ее волосам прилипли листья и веточки, куртка тоже была вымазана чем-то белым, наверное глиной."

    "Я сказала ей об этом. Она ответила, мол, на себя посмотри. И действительно, я немного порвала шорты и тоже была в глине."

    ul "Где же это мы нашли эту глину? Ничего же такого не было."

    al "Да уж нашли. Кстати, белая глина это признак осадочных пород, точнее известняка."

    "Алиса задумчиво разглядывала белые от глины пальцы."

    al "А осадочные породы сюда может вынести только река. Причем, подземная река. Река наверняка впадает в Бурлейку, так-как она течет по ущелью. Все остальные реки это её притоки. Что это значит?"

    ul "Это значит, что надо искать белую глину. Она выведет нас к притоку, а тот к Бурлейке. И вот мы спасены, потому что если идти вверх по течению Бурлейки, то мы точно придем в лагерь!"

    al "Соображаешь, Ленина!"

    ul "Но в лагерь нам еще рано... Нас будут искать у озера. Значит, надо идти вверх по течению ручья и тогда, он выведет нас на тропу по которой мы шли к озеру."

    al "Почему это?"

    ul "Да потому, что тропа подрезает склон, и все ручьи, идущие со склона, рано или поздно пересекают тропу. Что мы и видели, когда шли к озеру. Я насчитала тогда три ручья."

    al "Офигеть у тебя аналитические способности. Мне такое даже в голову бы не пришло. Хотя с луной мы облажались. И да, это была моя идея, каюсь."


    scene bg white_stream with dissolve

    "Мы пошли назад, чтобы найти место, где перемазались глиной. Выяснилось, что это ручей, который мы не заметили ночью. Очень маленький ручей и мутно-белый от глины. Мы пошли вверх по течению и скоро вышли на тропу."
 

    scene bg path with dissolve

    "Нашей радости не было предела. Но как выяснилось, это была «не та» тропа. Тропа сначала шла вдоль ручья, потом свернула налево."

    "И тут мы задумались. Идти по ручью или следовать дальше по тропе? Было заманчиво идти по тропе и посовещавшись, мы пошли по ней."

    "Тропа привела нас к подножью горы, дальше она терялась. Это был тупик. Мы прошли еще немного и вскоре уперлись в скалу которая была вся в террасах, похожих на дорожки, идущие вдоль склона."

    "Оставалось, или повернуть назад, или ещё пройти по террасе."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "С террасы скалы откроется вид на реку и мы сориентируемся. Тут довольно высоко."

    hide sp_al_056


    stop music fadeout 1.0


    play music "audio/music/z_1020.mp3"
   

    scene bg burleyka with dissolve

    "И действительно, скоро нам открылся вид на Бурлейку."

    "Это было очень красиво. Река в этом месте входила в ущелье, стены которого сужались, образуя каньон. Вода ускорялась и неслась по каньону, как по желобу, с большой скоростью."

    "Был даже слышен отдаленный рев этого потока. Это и был тот самый звук, что мы слышали в лесу. Так вот почему она Бурлейка! Мы двинулись назад, по террасе, и вдруг Алиса указала мне на склон:"


    stop music fadeout 1.0


    #play music "audio/music/z_130.mp3"
  

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Смотри, там что-то есть. Давай, посмотрим?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но это же на одну террасу ниже. Это нам не по пути."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ерунда, тут метров пять высоты, это несложно."

    hide sp_al_055
 

    scene bg cave2 with dissolve


    "Я согласилась, мы спустились и оказались напротив входа в грот. Грот уводил куда-то вглубь скалы. Со стен капали капли. А с потолка свисали длинные каменные сосульки."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Сталактиты. Давай отобьем кусочек, на память?"

    hide sp_al_055

    "Она постучала по сталактиту и не без труда отбила небольшой кусок. Он заискрился внутри фиолетовым блеском. Красота!"


    image an_23_02: # Анимация аметистовая жеода
        
        "images/an/an23day/an_d23_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    scene an_23_02 with dissolve

    pause (10000000000000000000000.0)


    scene bg cave2 with dissolve


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Это, наверное, жеода. Нам такую показывали в музее геологии, когда мы были на экскурсии. Если повезет, то это друза аметиста."

    hide sp_al_055


    "Мы хотели уходить, но я заметила что-то напоминающее бусинку. Я нагнулась и подняла её."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Это не природная. Это носил человек. Видишь, как она обработана? Если я не ошибаюсь, это сердоликовая бусина. Давай посмотрим, возможно, найдём ещё."

    hide sp_al_056


    scene cg beads with dissolve

    "Мы стали разгребать влажную от стекающей со стен воды глину у своих ног и нашли еще пять точно таких же бусин, но уже нанизанных на полуистлевшую нить."


    scene bg cave2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Смотри, высохшее, тонкое сухожилие.  Мумифицировалось. Вот какие они были, древние нитки!"

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тут была стоянка древнего человека! Пещера сохраняет всё. Микроклимат."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ну, не такого уж и древнего, слишком хорошо обработано. Но то, что эти люди жили в этой пещере – факт."


    scene bg white_stream with dissolve

    "Я положила находки в рюкзак. Больше мы ничего не нашли и отправились вниз по террасе, а потом вскоре нашли начало нашей тропы. Дошли по ней до ручья и снова пошли по нему."


    stop music fadeout 1.0


    play music "audio/music/z_140.mp3"
   

    scene bg coast3 with dissolve

    "Наш ручей привел нас на огромные песчаные плесы, тянущиеся вдоль Бурлейки."

    "Это было очень дикое место, потому что на девственном песке тянувшемуся на километры, не было видно ни одного следа."

    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ещё очень рано, мы успеем прийти в лагерь раньше группы. Другого такого случая побегать голышом у нас не будет."


    scene cg dunes_swimming with dissolve

    "Алиса принялась снимать с себя одежду. Вскоре её блестящие, белые ягодицы замелькали на фоне песка. Она с разгону бросилась в воду и замахала мне рукой:"

    al "Ну же, давай!"

    pause (10000000000000000000000.0)


    "Я тоже разделась и последовала её примеру. Вода была прохладной, но приятной. Мы ныряли и плавали, потом бегали голышом по берегу и играли в догонялки."

    "Потом вымазались в песке, зарывая друг друга по очереди, потом свалились в изнеможении, подставляя тела солнцу и загорая до самого полудня."


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"

    scene bg dunes with dissolve


    "Припекало. Идти никуда не хотелось."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Всё! Ополаскивайся и пошли. Если они послали Васю в лагерь сообщить о нас, (только он и ОД знают дорогу), то нас точно ищут все отряды, включая администрацию. Будет настоящее светопреставление."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но идти до лагеря сутки."

    hide sp_ul_019


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Усмехнувшись) \nВасе? Ты шутишь? Видела его костыли длиннющие? Он домчит до лагеря за пару часов."

    hide sp_al_037


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И никакие не костыли. Я видела его ноги..."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Заинтересованно)  \nНу-ну... Когда это ты видела его ноги?"

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Утром, он как раз искупался и готовил нам кофе. Красивые ноги, между прочим."

    hide sp_ul_021


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Улыбаясь) \nПонятно. Смотри, Жене, похоже, они тоже понравились."

    hide sp_al_037


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Скажешь тоже. Мне Вася в этом смысле не интересен. Я бы за Женьку только радовалась. Он про нее расспрашивал, кстати."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ух ты. Расскажешь?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Давай-ка думать лучше, как выбираться. Допустим, мы не встретим отряд и пойдем в лагерь."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Если придём рано, нас отругают и накажут."

    al "А если придем через день, то все очень переволнуются и будут рады, что мы просто живы. Сочиним слезную историю вроде той, что рассказала нам Ольга Дмитриевна."

    hide sp_al_055


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну да. Убегали от медведя, голодали, чуть не сорвались со скалы, чуть не утонули в реке, болоте, и всё такое."

    hide sp_ul_023

 
    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Оглядывает Ульяну) \nНу и вид у тебя, Улька! Видела бы ты себя перемазанную в песке. Так надо будет явиться в лагерь."

    hide sp_al_037


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что, голыми?"

    hide sp_ul_023
 
 
    # stop music fadeout 1.0


    # play music "audio/music/z_1014.mp3"


    scene bg coast3 with dissolve

    "Алиса стала хохотать, я тоже, и мы стали бороться и кататься по песку, окончательно перемазавшись."

    "В результате, я победила, сев на Алису сверху. Конечно, я думаю, что она поддалась мне, но это мелочи."

    al "Сдаюсь, сдаюсь!"


    stop music fadeout 1.0


    play music "audio/music/z_009.mp3"


    "Мы не стали мыться в реке, чтобы у нас был жалкий вид, согласно плану Алисы. Мы просто собрали вещи, оделись и пошли по левому берегу вверх по течению."


    scene cg footprints with dissolve

    "С этой стороны реки мы никогда еще не были, но знали что скоро начнутся камыши и болото. Поэтому мы взяли правее и вскоре снова вошли в лес. На этот раз реку было хорошо слышно и мы не боялись заблудиться."

    "Через полчаса мы вышли на опушку леса и миновав её, вошли в заросшую цветами долину, по которой пролегала маленькая чуть заметная тропка. Алиса наклонилась, показав мне на неё."


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene cg footprints2 with dissolve

    "На тропе явственно отпечатался след чьей-то босой, очень маленькой, ноги."

    pause (10000000000000000000000.0)


    scene cg footprints3 with dissolve

    al "Никого не напоминает?"

    al_ul "(В один голос) \nЮЛЯ!"

    pause (10000000000000000000000.0)
  
  
    scene cg map_fragment with dissolve


    "Вот я срисовала тут и карту и следы."

    pause (10000000000000000000000.0)


    scene cg fooptprints_comparison with dissolve


    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day24

return 