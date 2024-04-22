label day46:

    $ days = 46

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music


    play music "audio/music/z_478.mp3"


    scene bg forest1 with dissolve

    "Рано утром я пыталась идти, но не смогла. К тому же наше кораблекрушение оставило свой след, я сильно ударилась коленкой о камень. Теперь она распухла и болела."

    "Семён сказал, что это не беда, и что он дотащит меня до Юлиного убежища, а там её травки быстро поставят меня на ноги."

    "И я подумала, что он все-таки очень сильный. Ведь кроме меня, ему придется еще тащить два рюкзака, мой и Жени."

    "Я закрыла глаза и представила, как Семён несет меня на руках."


    scene cg sem_ul_carries with dissolve

    "Ну, как в фильмах про принцесс. Там принц всегда носит принцессу на руках. Это красиво."


    pause (100000000000000000000000000.0)


    "Но у них там нет рюкзаков. Поэтому я подумала, что на руках конечно эффектно, но непрактично. Но на спине, тоже неплохо."

    "И я представила, что я ранена на поле боя. И Семён выносит меня из под огня (Как в фильмах про войну). А я такая - «Брось командир, не донесешь»..."

    "Раньше я никогда не каталась на спине у кого-то. Правда, когда-то папа сажал меня маленькую на плечо. Но это не в счет."

    "Только один раз мы играли в «колбасу», и я запрыгнула на спину кому-то из мальчишек. Но «колбаса» сразу развалилась и покататься не получилось."

    "А тут сам Семён будет нести меня на спине почти до лагеря. И я вскарабкалась ему на спину, а он подхватил меня снизу под коленки, и так получилось неплохо."


    scene cg sem_ul_carries2 with dissolve

    "И мы пошли через чащу..."


    pause (100000000000000000000000000.0)


    "А я как бы случайно держалась, закрывая ему глаза, и он там смешно рычал. И говорил: «Вот упадем», будешь ночевать в кювете. Р-р-р-р». Это была игра."

    "А я говорила ему, как Машенька медведю: «Семён, сядь на пенек, съешь пирожок!» Хотя не было у нас никакого пирожка. А я бы от него не отказалась."

    "Но были два бутерброда. Женя их заботливо завернула в целлофан, они почти не размокли."

    "Семён, казалось, не уставал. А ведь я увесистая. Я посоветовала ему чаще делать привалы. Но он только отшучивался."


    scene bg forest2 with dissolve

    "Мы шли с горы, а с горы всегда легче. Озеро было где-то внизу, и мы шли уже по тропе, которая должна была вывести нас к нему."

    "Наконец, я увидела пенек. И вот тут я уже заставила Семёна сесть. Это был первый привал."

    "И я ещё поспала у него на руках. Это было так здорово. Так я себя ощущала только с бабушкой, когда гостила у неё в деревне."


    scene cg ul_granny with dissolve

    "Она замечательные делала пельмешки. От них бы я сейчас точно, не отказалась. В ее доме было тепло, уютно и хорошо пахло."


    pause (100000000000000000000000000.0)


    "От Семёна тоже шел приятный запах. Не такой, как от бабушки, когда я зарывалась носом в её руки."

    "Рук у неё были большие теплые и шершавые. «Это от подойников» – говорила она. Бабушка работала на молочной ферме."


    scene bg forest2 with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И я уткнулась лицом в его руки, чтобы проверить шершавые они как у бабушки или нет. И запах у них был другой. От него что-то сжималось внутри."

    "И я подумала, хорошо что он не знает, о чем я думаю. А он засмеялся и сказал: «Ты как слепой щенок, тычешься мордочкой». И погладил меня по голове, как папа."

    "А потом он меня снова взвалил на спину."

    hide sp_sem_016


    "Но мне так понравилось играть в слабую больную девочку, что я решила схитрить и сказала, что устаю держаться, чтобы Семён делал привалы почаще. Он буркнул: «ЛАДНО»."

    "Я бы, наверное, даже смогла сама идти. Но когда тебя несут, это другое."

    "Я закрыла глаза и представила, что еду на большом слоне, как шах-падишах, и он так меня плавно несет на спине."

    "А вокруг джунгли и обезьяны, и крики всяких птиц-попугаев, и индусы в тюрбанах... И я, наверное, заснула."


    stop music


    play music "audio/music/z_495.mp3"


    scene cg sem_ul_carries3 with dissolve

    "Но иногда я открывала глаза, чтобы посмотреть вокруг и понять, куда же мы идем. Тропинка петляла и вела нас через полянки и лес."


    pause (100000000000000000000000000.0)


    "И то ли у меня была температура и всё расплывалось в глазах, то ли еще чего, но лес вдруг качнулся и слился с воздухом так, что им можно стало дышать."



    image an_46_01: # Анимация качающийся лес

        "images/an/an46day/an_d46_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat

    scene an_46_01 with dissolve


    pause (10000000000000000000000.0)



    "Он слился в плотную зеленую массу, вот прямо без веток и деревьев, и покачивался. Не знаю, как это описать."

    "А может быть, это я качалась в такт шагов Смена. Но это было так удивительно!"

    "Никогда раньше я не ощущала такого странного чувства. Как будто я сама стала частью этого изумрудного вязкого марева и ощущала дыхание ароматного, хвойного ветра."

    "И что я тоже колыхалась, как деревья, чувствовала свои листья, и что по ним ползут букашки, и что я тяну соки из земли..."

    "Это было потрясающее состояние, как очень красивая и интересная галлюцинация. И я подумала, вдруг я съела чего-нибудь такого..."

    "Внезапно Семён остановился, а лес продолжил покачиваться. И я услышала, как он сказал: «ВОЛШЕБНО»."

    "Мы стояли и смотрели на колышущийся лес. То есть он стоял, а я была на его руках."

    "И я прижалась к нему, потому что мне все-таки было немножко страшно. А вдруг, лес проглотит нас навсегда?"


    stop music


    play music "audio/music/z_516.mp3"


    scene bg forest3 with dissolve

    "Но вот, спустя время, всё стало четким, качание прекратилось, а лес стал обычным лесом."

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что это было?"

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Не знаю. Ты тоже это ощутила?"

    hide sp_sem_016


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что я — часть леса? Да. И ты тоже — часть."

    hide sp_ul_019


    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Мне страшновато стало."

    hide sp_sem_026


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И мне..."

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Эта зона, с ней что-то сейчас происходит. Не лагерь, а какая-то шкатулка чудес."

    hide sp_sem_016


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Шкатулка чудес! Как здорово, я обязательно напишу про лес в дневнике, и название уже есть. Классно!"

    hide sp_ul_021


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "А может быть, это бред. Ты бредишь, потому что болеешь, а я заразился от тебя."

    sem "В общем, надо быстрее добраться до домика Юли, а то нам каюк. Так у нас не только лес оживет но и земля.  Все оживет, листья, ягоды, грибы, желуди."

    hide sp_sem_016


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Желуди? А мы их схрумкаем. Будем как свинки."

    hide sp_ul_023


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Типа того. Перейдем на подножный корм."

    hide sp_sem_016


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я бы сейчас любой желудь съела, так жрать охота!"

    hide sp_ul_019


    "Тут мы рассмеялись оба и Семён пошел быстрее. А я снова уснула."


    scene an_d46_05 with dissolve

    "Проснулась я от слова «ОЗЕРО». Оказывается, мы шли, если верить Семёну, еще целый час и вышли к озеру."

    "Но я его отчитала за то, что он ни разу не сделал привал и, наверное, устал."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "А что тут такого? Мне же не тяжело совсем. Ты малявка и ничего не весишь. Рюкзак и то тяжелее!"

    hide sp_sem_016

    "Тут я хотела возмутиться на слово «МАЛЯВКА», но когда увидела Озеро, то прям замерла. Оно светилось и сверкало. "


    stop music


    play music "audio/music/track4.mp3"


    "Солнце только взошло, и всё переливалось, как в сказке. Я спрыгнула на землю и стояла, открыв рот."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Вижу, красота страшная сила, поднимает даже хворых."

    hide sp_sem_016


    "Но я ничего ему не ответила, а уже бежала к озеру, чтобы дотронутся до сверкающей воды. Она была холодная и мокрая... И мне снова стало зябко."

    "А тут подбежал Семён и отчитал меня за то, что я себя не берегу, что я ещё слабенькая и мне нельзя так бегать."

    "А я, как принцесса, изобразила обморок и упала ему на руки."

    "А он закричал: «ПРИТВОРЩИЦА!» и стал щекотать (как Алиса вечно делает). А я не могу терпеть щекотку и орала, как потерпевшая, и мы смеялись..."


    scene cg sky with dissolve

    "Передохнуть мы решили на берегу. Расположились на песке и смотрели на небо."

    "Тучи отражались в воде и были как будто над нами и под нами. И у меня возникла идея."


    scene an_d46_05 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тут мелко, давай войдем в воду, и будем стоять как бы на тучах."


    scene cg sem_ul_clouds with dissolve

    "Так и сделали. Тучки были классные, как стадо барашков."


    pause (100000000000000000000000000.0)


    stop music


    play music "audio/music/z_1015.mp3"


    scene cg sky2 with dissolve

    "Семён рассказал мне про своё детство."

    "Оказывается, эти времена у всех чем-то похожи. Но только я, как он, не ходила в спортивную секцию, а вот  по крышам и заборам  тоже лазала и воровала яблоки в соседском саду."

    "И мы делились всякими секретами, как лучше и где что стащить. Вот орехи, например. Тут надо осторожно. Если сторож увидит, то хана."

    "И что надо связать рубашку рукавами и получиться мешок для орехов, а чтобы больше влезло, чистить их прямо под кустом и складывать в рубашку уже чищенные. Ну и всё такое."

    "И мы не заметил как проговорили, наверное, целый час, а может быть два."

    "И мне стало казаться что мы знаем друг друга уже сто лет. А ещё я случайно рассказа ему про то, что мы нашли на прииске."


    stop music


    play music "audio/music/z_130.mp3"


    scene cg scull with dissolve

    "Ну это я, конечно, немножко проговорилась. Но он не удивился ничуть и сказал, что знает про немцев и про их задание. А вот откуда он знал это, интересно?"


    scene an_d46_05 with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "А он мне рассказал свои тайны детства. Оказывается, он тоже собирал стеклышки."

    hide sp_sem_016


    scene cg crystal1 with dissolve

    "И я вспомнила, что у меня один кристалл с собой. Достала и показала ему."


    scene an_d46_05 with dissolve

    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "А он изменился в лице и спросил:"

    sem "Откуда у тебя это?"

    hide sp_sem_026


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Но я не стала говорить. Я и так у же проговорилась про прииск и злилась на себя за это."

    ul "Так, просто, нашла."

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Но он, кажется, не поверил."

    sem "Сделай ещё так."

    hide sp_sem_016


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Как?"

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Посмотри на меня сквозь этот кристалл."

    hide sp_sem_016


    scene cg ul_crystal2 with dissolve

    "Я сначала решила что он меня разыгрывает, но потом согласилась. Я взяла свой кристалл и посмотрела сквозь него на Семёна."


    pause (100000000000000000000000000.0)


    scene cg crystal2 with dissolve

    sem "Твой камень был голубой а теперь он красный! Твои глаза изменили цвет. Они больше не голубые!"


    pause (100000000000000000000000000.0)


    ul "А какие?"


    scene cg ul_crystal3 with dissolve

    sem "Малиновые, как у вампира, и светятся изнутри."


    pause (100000000000000000000000000.0)


    "Я подумала, что он шутит, сделала страшное лицо и зарычала: «Ррр!»"


    image an_46_03: # Анимация Ульяна кристалл

        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_10.webp" with Dissolve(0.5, alpha=True)
        pause 1.0



        #repeat

    scene an_46_03 with dissolve


    pause (10000000000000000000000.0)


    "Сделала вид, что кусаю его. А он от меня отшатнулся и бросился бежать."


    scene an_d46_05 with dissolve

    show sp_ul_020:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я стояла как дура на берегу и ничего не понимала. И я закричала:"

    ul "Сёма, ну хватит уже! Возвращайся! Мы же играем в вампира!"

    hide sp_ul_020


    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "А он долго стоял у кромки леса, потом медленно подошёл."

    sem "Спрячь эту штуку и никогда не доставай. Во всяком случае, пока есть ВИБРАЦИЯ."

    hide sp_sem_026


    stop music


    play music "audio/music/z_048.mp3"


    image an_46_02: # Анимация озеро

        "images/an/an46day/an_d46_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat


    scene an_46_02 with dissolve


    pause (10000000000000000000000.0)


    "И я вдруг поняла, что озеро не просто блестит, а дрожит. Вода покрылась рябью, потому что озеро что-то трясет, а из-под земли гул и тоже какая-то дрожь. Прямо как в лагере тогда."

    "Вот про это и сказал Семён «ВИБРАЦИЯ». И я вспомнила притчу Пионера про детей. И кажется, я стала понимать. Что когда гудит земля, то ЖЕЛАНИЯ ИСПОЛНЯЮТСЯ."

    "И еще я вспомнила слова Юли, что камушки усиливают желания, и когда начинается вибрация, материализуют их."

    "Я посмотрела еще раз на камушек и спрятала его. А Семён еще долго не приближался, пока я сама к нему не подошла и не села ему на колено."


    stop music


    play music "audio/music/z_002.mp3"


    scene an_d46_05 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Всё, я уже не вампир, в эту игру мы больше не играем. Просто давай вот так посидим немного."

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "И я посмотрела ему в глаза. В них был еще испуг. А потом он сказал:"

    sem "Они снова голубые."

    hide sp_sem_016


    stop music


    play music "audio/music/z_055.mp3"


    "Ну вот... Потом мы перекусили остатками Женькиного бутерброда (первый мы съели ещё там, в шалаше) и пошли дальше."


    scene cg sem_ul_cutlet3 with dissolve

    "Теперь притворяться уже было бессмысленно, и я шла сама. Хотя иногда канючила, что «хочу на ручки»."


    pause (100000000000000000000000000.0)


    "Но он только смеялся. Сказал, что в ДОКТОРА мы поиграем, когда я по настоящему устану или снова заболею. А в КАПРИЗНУЮ ДЕВОЧКУ играть не будем. Мол, я уже взрослая."

    "Тогда я ему заявила, что если я уже взрослая, то следующий поцелуй пусть будет не в лобик, как в прошлый раз с котлетой."

    "Он остановился и посмотрел на меня очень серьезно (прямо как папа, когда я что-нибудь не то сделаю)."


    scene cg sem_ul_cutlet6 with dissolve

    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "НЕТ. В эту игру мы с тобой играть не будем."


    scene cg sem_ul_cutlet3 with dissolve

    "А потом мы пошли дальше. А я всё шла и думала."

    "Почему НЕТ-то? Почему всем можно, а мне нельзя? Я же подросла в лагере, уже месяц прошел!"

    "Вон, и Алиса сказала, что я вымахала за лето. И Семён сказал «уже взрослая». В общем, они все врут, чтобы меня не расстраивать, и совсем сами запутались в своем вранье."

    "И ещё чуть что, говорят про гормоны. Что за гормоны такие, я их совсем не чувствую. В общем, я злилась."


    stop music


    play music "audio/music/z_011.mp3"


    scene bg iul_hide2 with dissolve

    "Тем временем мы вышли на другую тропу."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Всё, я знаю эту тропу, она ведет на полянку, потом в лесок, где Юлины припасы, а оттуда к её домику. Давай, пойдем быстрее, если хочешь кушать."

    hide sp_sem_016


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, я подкрепилась бы. Бутерброд, конечно, был вкусный, но очень маленький."

    hide sp_ul_019


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Вот Юлька удивиться! Она, наверно, думала что мы уже уплыли, попрощалась, а тут мы."

    hide sp_sem_016


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, мы так с ней ещё поплакали на дорожку. Она классная! Я всё думала, почему мы не можем её забрать, как котеночка в корзинку и увезти с собой?"

    hide sp_ul_021


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Представляю размер корзинки."

    hide sp_sem_016


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ты меня нес легко, а её тем более. Вон какие у тебя плечи! Она же весит меньше меня. Вот кто — МАЛЯВКА."

    hide sp_ul_021


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Ну, не знаю. Мне она тоже нравилась всегда. Характер у неё покладистый, и вообще, она умная и милая."

    hide sp_sem_016


    scene bg bug_lane with dissolve

    "Тут  тропа закончилась, и мы вышли на поляну."

    "Полянка вся сияла от солнца и было много всяких жуков. Они проносились над головой и садились на цветы, не обращая на нас никакого внимания."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Красотища..."

    hide sp_sem_016


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да... Как здорово, что ты это чувствуешь. Вот с кибернетиками о природе говорить бесполезно. Сразу у них скучные лица."

    hide sp_ul_021


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Это естественно, у них голова занята другим. Давно уже замечено, что люди делятся на ФИЗИКОВ и ЛИРИКОВ."

    hide sp_sem_016


    "И вдруг кто-то меня толкнул так, что я присела. И Семён тоже присел. И мы удивленно смотрели друг на друга."


    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Ты чего толкаешься?"

    hide sp_sem_026


    show sp_ul_044:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я? С ума сошел! Сам толкнул, а теперь издеваешься. Зачем ты меня толкнул?"

    hide sp_ul_044


    "В это время из кустов раздался знакомый тихий голосок:"

    uv "Не спорьте. Лучше сидите тихо, это я толкнула."


    scene cg yulya_bushes with dissolve

    "И из кустов выглянула такая милая рожица с ушками."


    uv "Вы мне всех мышей распугаете. Я же охочусь. А почему вы здесь? Вы же уплыли."

    "Но мы давай её обнимать и целовать. Шумели очень."

    "В общем, всех мышей мы в тот день точно распугали."


    stop music


    play music "audio/music/z_023.mp3"


    scene bg uhouse4 with dissolve

    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Юля выслушала рассказ про наши приключения. Пока мы отдыхали, она заварила мне травки и дала отвар из грибов."


    scene bg yulya_bed with dissolve

    "Как всегда, после ее отвара, мне захотелось спать. И засыпая, я видела, как Юля о чем-то беседовала с Семёном."

    "Когда я проснулась, был уже вечер. Никого не было в домике. Меня, оказывается, заботливо укрыли одеялом."


    scene bg uhouse3 with dissolve

    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Вскоре вернулись Юля и Семён. Пора было собираться."


    scene cg iul_boat with dissolve

    "И мы пошли на берег к Омуту."


    pause (100000000000000000000000000.0)


    "В месте, где ручей Тихий впадает в Омут, где мы рыбачили Сома, была спрятана Юлина лодка. Оттуда мы добрались на ней до острова Ближний."


    stop music


    play music "audio/music/z_005.mp3"


    scene bg old_well with dissolve

    "Место, где мы причалили, было мне чем-то неуловимо незнакомо."


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Это поляна рядом со старым колодцем. Узнаешь?"

    hide sp_sem_016


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Конечно узнаю. Хоть это и было ночью. Странно, а ты откуда о нем знаешь?"

    hide sp_ul_021


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Я рассказала. Именно через тайный ход, который ведет из Старой Лаборатории на остров, я попадаю в лагерь, когда Бурлейка разливается и сносит все мосты на бродах."

    hide sp_iul_012


    "Так я узнала про то, что Семён регулярно пользуется тайным ходом. "


    stop music


    play music "audio/music/z_910.mp3"


    scene bg camp_artifacts with dissolve

    "Вскоре мы были уже в лагере. Все в это время были в столовой. Мы заглянули туда. Нас радостно встретили. Все переживали за нас."


    stop music


    play music "audio/music/z_171.mp3"


    scene bg attic2 with dissolve

    "После столовой мы снова собрались на чердаке нашего домика, который давно стал нашей «штаб квартирой», чтобы обсудить, что нам делать после нашего неудачного похода на баркасе."

    "Между тем, до нас стали доходить невеселые новости о лагере."

    show sp_sl_019:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3
    with dissolve

    sl "Пока вас не было, тут много чего произошло."

    hide sp_sl_019


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Кто-то утонул?"

    hide sp_ul_019


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    je "Нет, слава богу. Но опять исчез Смутьянов и с ним два мальчика из второго отряда. Мы знаем, что они выбрались на берег. Наверное, готовят новую смуту."

    hide sp_je_001


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    mi "Всем в лагере теперь заправлял Долговязый. Петрович второй день в запое."

    hide sp_mi_019


    show sp_at_002:
        yalign 0.1 subpixel True
        xalign 0.9 subpixel True
        zoom 1.2

    ats "Повариха исчезла. Любовь Никаноровна, зав столовой, вчера лежала с температурой. Хорошо, что третий отряд еще относительно слушался и помогал больной тете Любе с готовкой на кухне."

    hide sp_at_002


    show sp_le_016:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.25

    le "Директриса и завхоз, которая уехала с ней, не приехали, а ОД с ног сбилась, наводя порядок."

    le "Похоже, ее никто уже не слушает. Опять началось что-то вроде того массового психоза, который когда-то привел к восстанию."

    hide sp_le_016


    show sp_sem_026:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "А Виолета Церновна?"

    hide sp_sem_026


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "Дверь в медпункт закрыта. Я смотрела в замочную скважину. Никаких признаков движения. Хотя вчера я видела, как она туда входила."

    hide sp_je_001


    "И мы пошли к ОД, чтобы выяснить, чем мы можем ей помочь."


    stop music


    play music "audio/music/z_132.mp3"


    scene bg mus with dissolve

    "Все собрались в музкружке и там был «военный совет»."

    "Ольга Дмитриевна подробно изложила нам ситуацию последнего дня и спросила:"


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Какие будут предложения по восстановлению дисциплины? Я на вас сильно рассчитываю."

    hide sp_od_022


    stop music


    play music "audio/music/z_131.mp3"


    scene bg camp_artifacts with dissolve

    "В лагере назревала смута."

    "На площадь, где возник стихийный митинг, стекались пионеры второго и третьего отрядов. Тащили старые ящики из кладовки столовой, стулья, ломали скамейки и сваливали все в кучу."

    "Откуда-то принесли большое чучело и водрузили его на столб изображающий распятие. Чучело было одето в рубашку и юбку Маргариты Павловны."


    show sp_od_023:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Смотрите, ее вещи! Значит они взломали дверь в кабинет директора!"

    od "Вы должны помочь мне навести порядок, одна я не справлюсь."

    hide sp_od_023

    "Мы обещали помочь. Она раздала задания. Все разошлись по «боевым постам»."



    image an_46_04: # Анимация костёр с чучелом МП

        "images/an/an46day/an_d46_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat



    stop music


    play music "audio/music/z_049.mp3"


    scene an_46_04 with dissolve


    pause (10000000000000000000000.0)


    "Наша с Алисой задача была уговорить пионеров потушить костер который они развели, сжигая чучело директрисы. Это нужно было сделать, пока не загорелись рядом стоящие постройки."

    "Устроил «инквизицию» конечно же, Долговязый. Но за его спиной мы увидели знакомую плешь Смутьянова."


    show sp_smu_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Он деловито размахивал руками и что-то говорил собравшимся у костра пионерам."

    hide sp_smu_005


    scene bg camp_artifacts with dissolve

    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Явился, не запылился! Вот гад! Он все подготовил. Решил, что вторая попытка пройдет на ура. Затаился и ударил в нужный момент."

    hide sp_al_002


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Он неисправим. Ведь обещал вести себя достойно. Ему поверили. Маргарита Павловна не стала вызывать родителей. Подлец он."

    hide sp_ul_013


    scene an_46_04 with dissolve

    "Мы направились к костру."



    image an_46_05: # Анимация костёр землетрясение

        "images/an/an46day/an_d46_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat


    play miscSounds "audio/music/z_048.mp3"


    scene an_46_05 with dissolve


    "Вдруг начался гул. Земля пришла в движение."


    pause (10000000000000000000000.0)


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Опять включилась это проклятая машина! Жди беды."

    hide sp_al_001


    stop miscSounds


    play miscSounds "audio/music/z_047_1.mp3" noloop


    #scene an_46_05 with dissolve


    "Раздался взрыв. Мимо пробежала Славя."


    stop miscSounds


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Что случилось?"

    hide sp_al_007


    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Это у Петровича!"

    hide sp_sl_028


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А сам Петрович где? Он сейчас очень нужен."

    hide sp_ul_013


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Тебе же сказали, бухает второй день."

    hide sp_al_007


    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Петрович начал чудить, открыл склад, разговаривал с манекенами Вано. Потом пошел зачем-то к себе в каптёрку и достал топор. Хотел рубить манекенов. Двоих зарубил. Мы с Семёном его еле уняли."

    sl "А потом произошло что-то странное. Эти штуки ожили."

    hide sp_sl_028


    show sp_ul_050:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Какие штуки?"

    hide sp_ul_050


    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Ну, манекены! Их видели я, Семён и Ольга Дмитриевна. Мы прибежали на шум. Манекены подожгли каптерку Петровича!"

    hide sp_sl_028


    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Боже мой, там же ДИНАМИТ!"

    hide sp_al_066


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но ведь желания не исполнятся без тех кристаллов, что мы видели у Юли и нашли в ручье?!"

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "А где ты спрятала свои?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Неуверенно) \nНа складе. Там еще есть такая классная нычка за ящиками, как раз в помещении с..."

    hide sp_ul_013


    show sp_ul_050:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот же блин! С МАНЕКЕНАМИ!"

    hide sp_ul_050


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Скорее! Эти кристаллы надо оттуда забрать, если уже не поздно."

    hide sp_al_007



    stop music


    play music "audio/music/z_333.mp3"


    "Мы бросились к складу."


    show sp_od_027:
        yalign 0.0 subpixel True
        xalign 0.30 subpixel True
        zoom 1.1
    with dissolve

    "Ольга пыталась загородить нам путь, но мы с Алисой ловко поднырнули под её расставленные руки и добежав до склада, запрыгнули туда в последний момент перед вторым ВЗРЫВОМ."


    stop music


    play music "audio/music/z_047_2.mp3" noloop


    scene cg closet_ruins with dissolve

    "Взрыв был сильный!"


    stop music


    play music "audio/music/z_131.mp3"


    "Часть каморки Петровича разметало по всей спортивной площадке. Осталась одна стена и часть крыши."

    "Судя по всему, детонировал только один ящик с шашками. Остальные могли рвануть в любую минуту."


    scene cg stock_mannequins1 with dissolve

    "Мы вовремя забежали в помещение склада, иначе осколками стены нас точно бы ранило, если не убило."


    pause (100000000000000000000000000000.0)


    scene cg stock_mannequins2 with dissolve

    "Вдруг у нас за спиной появился Семён с топором."


    pause (100000000000000000000000000000.0)


    "Увидев нас, он заорал:"

    sem "Брысь отсюда! С ума сошли! Вы же в самое логово! Немедленно! Они же вас!"


    stop music


    play music "audio/music/z_125.mp3"


    "Закончить он не успел, дверь в помещение склада Вано открылась. Через проём на нас смотрели белеющие в темноте истуканы. Их глаза зловеще светились."

    "Целый взвод манекенов, вооруженных ракетками для бадминтона, с решительным видом двинулся в нашу сторону."

    "Они шли каким-то механическим шагом. От дерганых движений их фигуры выглядели ещё более зловещими."

    "Пожар подсвечивал их «лица», с темным впадинами глазниц, из которых колючими желто-красными угольками смотрели «глаза»."

    "Звуки вращающихся шарниров, которые скрипели при каждом их движении, дополняли эту ужасную картину."


    scene cg stock_mannequins3 with dissolve

    show sp_sem_023:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "Ну прямо зомби-апокалипсис какой-то. Хорошо, что Петрович зарубил двоих. Один, кажется, погиб при взрыве."

    sem "Но их все-таки многовато на нас троих. Берите, что под руку попадётся, но желательно потяжелее. Сейчас будет потеха."

    hide sp_sem_023


    show sp_sem_018:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Семён отбросил короткий топор и поднял лежащий на полу ломик, который оставил на складе Петрович ещё со времен памятного случая с Вано. Он улыбался."

    hide sp_sem_018

    "Я перевела взгляд на манекенов и поняла, почему. Ракетки для бадминтона. Они, эти твари, не понимали, что это плохое оружие."

    "Но после того, как Семён взял в руки лом, они стали переглядываться, а потом пошли к пожарному щиту."


    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Там топоры, лопаты и багор! Скорее! Надо опередить их и быть у щита раньше, чем они разберут «арсенал»!"

    hide sp_al_066


    "Я посмотрела вокруг и увидела ящик, набитый бутылками с ацетоном. Он остался от маляров, которые приводили лагерь в порядок перед нашим заездом."


    show sp_al_049:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса перехватила мой взгляд."

    al "Ты гений, Улька! Пластмасса! Они же пластмассовые!"


    scene cg stock_mannequins4 with dissolve

    "Неожиданно в склад заглянула Виола."


    pause (100000000000000000000000000000.0)


    stop music


    play music "audio/music/z_051.mp3" noloop


    "Мы, все трое, закричали: «УРА! Подмога!»"


    stop music


    play music "audio/music/z_202.mp3"


    scene cg stock_mannequins3 with dissolve


    show sp_vio_007:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Виола быстро оценила ситуацию и крикнула:"

    vio "Держитесь! Сейчас наши подойдут! Но не подходите к ним близко!"


    scene cg mannequins_fight with dissolve

    "Схватка началась стремительно."

    "Истуканы бросились в атаку, но были встречены дружным «огнем» нашей группы."

    "В манекенов полетели картошка и яблоки, в изобилии наваленные на бетонном полу склада, и даже мешки с сахаром."

    "Однако их это не остановило. Почти не закрываясь от разлетающихся при ударе об их тела «снарядов», они упрямо шли к пожарному щиту."

    "Но они просчитались. Вскоре там оказались Виола с Ольгой Дмитриевной."

    "Они разгадали замысел «картонной армии» (как назвал ее Семён) и вскоре багор и топор быстро замелькали в их руках."

    "Тут прибежали предупреждённые Мику пионеры во главе с Толиком и приняли активное участие в побоище."


    stop music


    play music "audio/music/z_076.mp3"


    scene bg camp_artifacts with dissolve

    "Битва переместилась на площадь."

    "Мне удалось вытащить из помещения склада ящик с ацетоном и раздать бутылки всем желающим, объясняя на ходу, как сделать «коктейль Молотова»."

    "Пионеры притащили простыни, которые рвали на длинные полосы. Они обматывали их вокруг бутылок, опускали один конец внутрь бутылок и, поджигая другой конец, бросали в толпу манекенов."

    "Не обошлось без потерь и со стороны юных ленинцев. Двоих девочек врагу удалось пленить и утащить в помещение склада, где уже лежал связный Петрович."

    "От брошенных бутылок горели уже несколько манекенов. Однако враг быстро учился."

    "Брошенные поспешно, особенно девочками, бутылки с ацетоном, либо не долетали до манекенов, либо, ударившись о пустотелые тела истуканов, отлетали обратно."

    "Один из манекенов стал подбирать горящие бутылки и передавать другим. Вскоре «арт дуэль» велась уже с обеих сторон."

    "Появились первые раненые."


    show sp_sem_017:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve


    "Семён ломом успел уложить трех манекенов, и они упали рядом с догорающими остатками еще двух, подожженных пионерами."

    "Он был исцарапан ударами теннисных ракеток, которые манекены сначала выбрали себе в качестве оружия. Это придавало ему по настоящему геройский вид."

    hide sp_sem_017

    "Из помещения склада появлялись все новые и новые манекены. Вооружены они были уже не теннисными ракетками, а лопатами и садовым инвентарем. Это в корне меняло ситуацию."


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Неожиданно, Алисе пришла в голову спасительная мысль."

    al "- Стоп! Всем стоп! Давайте выясним, чего они хотят."

    al "ПЕРЕГОВОРЫ!"


    stop music


    play music "audio/music/z_1003.mp3"


    scene bg camp_artifacts with dissolve
    #scene cg negotiation with dissolve

    "Похоже, манекены хотели того же. Они прекрасно понимали, что рано или поздно их количество перестанет быть достаточным для сопротивления."

    "И хотя, обезображенные ударами пионеров, «тела» всё ещё корчились и пытались встать с земли, они были уже ни на что не годны."

    "Один из манекенов, с белой повязкой на лбу, раздававший приказания голосом диктора метрополитена и, очевидно, ГЛАВНЫЙ, поднял руку."

    "Битва на время прекратилась. Он выступил вперед."


    stop music


    play music "audio/music/z_131.mp3"


    scene bg camp_artifacts with dissolve
    #scene cg negotiation_bg with dissolve


    manneq "У нас ваши заложники. Также, мы можем взорвать лагерь, если поймем, что проиграли. Однако, у вас есть тот, кто нам нужен. Если вы отдадите его, мы уйдем."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Мы однозначно не отдадим никого из людей. Но все же интересно, кто это?"


    scene cg elyatronic2 with dissolve

    manneq  "У вас есть андроид."

    manneq "Она нужна нам для... \n(он замялся)"

    manneq "Это вопрос выживания. Так как вы уничтожили последнего манекена-женщину. Только что. Вы не оставили нам выбора."


    scene bg camp_artifacts with dissolve
    #scene cg negotiation_bg with dissolve

    manneq "Отдайте нам андроида, и мы уйдем в Бункер к своим товарищам."


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Для этого надо спросить разрешения у её создателей. Если говорить вашим языком, у неё есть родители."

    hide sp_al_004


    show sp_el_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Электроник выступил вперёд."

    el "Нет, её вы не получите. Она не манекен, как вы. Тупые безголовые твари из пластмассы и папье-маше. Она существо, воплотившее в себе лучшее, что создала наука."

    el "Но у неё есть свободная воля. Если она сама не захочет уйти с вами, а такое право у неё есть, мы будем защищать её, как любого из нас."

    el "К тому же, она пионерка..."

    hide sp_el_007


    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Электроник замялся."

    el "Ну, в смысле, кандидат. Она подала заявление на вступление."

    hide sp_el_002


    show sp_vio_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Виола, насмешливо наблюдая за переговорами:"

    vio "Это нам понятно, господин Главнокомандующий Картонными Войсками. Вы лучше скажите, зачем вы это начали и какова была ваша первоначальная цель?"

    hide sp_vio_003


    stop music


    play music "audio/music/z_130.mp3"


    manneq "Нас создал гений, а не ваша наука. Он вложил в уста сторожа заклинание. Но сейчас нашего создателя, к сожалению, нет с нами, иначе бы вам пришлось плохо."

    manneq "Мы схватили сторожа потому, что он отрекся от нашего создателя. Оскорбил его и пытался разрушить его творение, то есть НАС."

    manneq "Такое непростительно. Мы хотели спокойно уйти. Но он пытался уничтожить нас. И поплатился."

    manneq "Он жив только потому, что наш Создатель не дал нам указаний, что делать с этим ничтожеством."

    manneq "Мы обменяем ваших двух пионерок и собаку на свободный проход. Но сторожа мы забираем с собой. Позже он будет предан суду."

    manneq "Вы пытаетесь жечь нас этой жидкостью. Но посмотрите, почти у каждого из нас уже есть в руках динамитная шашка. Их было полно у вашего сторожа. Мы вскрыли один ящик."

    manneq "И поверьте, вам будет несдобровать, если я дам команду."

    manneq "Нас около тридцати, а вас кажется меньше двадцати, минус две девочки и сторож. Подумайте трезво: война и неизбежное поражение, или моё выгодное предложение?"


    stop music


    play music "audio/music/z_197.mp3"


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Ко мне подошла Алиса и сказала так, чтобы не слышали манекены."

    al "В помещении склада есть оружие, которое осталось после Зарницы, но они о нём не знают. Они пользуются тем, что нашли в каморке Петровича."

    al "Возможно, они даже пытали его, но он не сказал."

    al "Нам нужно туда пробраться. Я видела там пулемет Максим. И ящик гранат."

    al "Но вот что странно. Виола могла бы их уделать. Она суперсолдат, и она знает про склад с оружием. Но она ничего не предпринимает."

    al "Это точно намеренно. Возможно, она была даже в курсе восстания. А возможно, даже его инициатором. Но зачем?"

    al "В любом случае, все это нужно прекращать. Мы должны пробраться на склад с другого хода."

    hide sp_al_004


    scene bg camp_artifacts with dissolve
    #scene cg negotiation_bg with dissolve

    show sp_vio_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Между тем, ввиду события, явно переломившего «ход боевых действий», Ольга и Виола склонялись в сторону принятия предложения Главного. Это было заметно."


    scene bg camp_artifacts with dissolve
    #scene cg negotiation_bg with dissolve

    show sp_elya_006:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Привели Элю. Рвущихся не допустить ОБМЕНА Электроника и Шурика держали за руки пионеры."

    hide sp_elya_006


    "Из помещения склада манекены вывели двух девочек со связанными за спиной руками. Переговаривающиеся стороны стали оговаривать «детали» и выторговывать «гарантии»."


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вообще-то, нам не пробраться на склад. Все выходы охраняют манекены. Главный соврал. Их не тридцать. Я насчитала у Вано в свое время пятьдесят два манекена."

    ul "Он торговал не только тряпками но и манекенами тоже. Вот почему их так много."

    ul "Главный слукавил. Как только они получать Элю, они захватят лагерь."

    ul "Они просто боятся, что мы уничтожим андроида. То есть поступим так, как поступили бы они в данной ситуации."

    ul "У меня есть другой план. Помнишь табличку на памятнике Генды?"

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, помню. И что с того? Мы все равно не смогли открыть ее в прошлый раз!"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Памятник как-то связан с вибрацией, и ожившие манекены появились именно тогда, когда началась вибрация."

    ul "Я успела забрать спрятанные на складе камушки, пока вы там «сдерживали натиск первой волны»."

    ul "Так что, есть надежда, что в лагере не появятся всякие новые ожившие кастрюли, швабры, музыкальные инструменты, и бог знает, что ещё."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Тогда бежим к памятнику. Скорее! Ольга уже жмет руку Главному!"

    al "Если они уведут Элю, то с её помощью они размножатся очень быстро. Она умная и это будет поколение супер андроидных манекенов, которые сметут всё."

    al "А если начнут воспроизводить сами себя бесконтрольно, то выйдут за пределы ЗОНЫ. Можешь представить себе, что тогда будет? Это будет ПРОСТО ЧУМА!"

    hide sp_al_004


    stop music


    play music "audio/music/z_131.mp3"


    scene cg mannequin_world with dissolve

    "Я сразу представила себе новое поколение манекенов-пионеров, выросших в Совёнке. Мне стало не по себе..."


    pause (100000000000000000000000000000.0)


    scene bg genda2 with dissolve

    "Мы бросились к памятнику."


    scene cg genda_plate_05 with dissolve

    "Табличка стояла в положении, в котором я её оставила. Она была ровной, заподлицо с постаментом, и не было видно даже маленькой щелочки по её краю."


    scene bg genda5 with dissolve


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну что теперь?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А то, что у меня кристалл. И у нас есть вибрация."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, она сегодня особенно сильная."

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нам нужно очень пожелать, чтобы табличка открылась."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Хорошо, что нужно делать?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Представлять себе, что она поддается, и жать на верхний край. На «раз, два, три» давим на верхний край."

    hide sp_ul_013


    scene cg genda_plate_06 with dissolve

    "Мы навалились на табличку всем весом. Она нехотя пошла внутрь постамента."

    "Нижний край оттопырился настолько, что под него стало можно просунуть пальцы, и Алиса ухватилась за него."

    "Алиса тянула вверх, а я толкала верхний край вперёд."

    "Наконец, раздался щелчок, и табличка неожиданно легко повернулась в горизонтальное положение, а затем уехала куда-то вглубь постамента."


    scene cg lever with dissolve

    "За ней оказался какой-то рычаг."


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Рубильник, что ли? Током не ударит?"

    hide sp_al_004


    "Алиса обмотала руки снятыми гольфами, и я сделала то же самое. Мы ухватились за рычаг."

    "Раз, два, три! Рычаг со скрипом ушел вниз."


    image an_46_06: # Анимация костёр землетрясение

        "images/an/an46day/an_d46_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


    stop music


    play music "audio/music/z_207_1.mp3" noloop


    scene an_46_06 with dissolve

    "Неожиданно памятник стал разворачиваться в сторону нашего домика. Теперь Генда смотрел уже не на Библиотеку, а прямо на наш чердак."


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Фух..."

    "Алиса вытерла лоб."

    hide sp_al_004


    "Вибрация неожиданно прекратилась."


    stop music


    play music "audio/music/z_151.mp3"


    scene cg fallen_mannequins with dissolve

    "Мы посмотрели на площадь. Манекены вдруг стали бесцельно двигаться взад и вперед. Многие упали на колени и пытались ползти."

    "Дольше всех на ногах стоял Главный. Он цеплялся за Виолу, чтобы не упасть. Она коротким движением ударила его в грудь, но он успел схватить её за халат."

    "Крутанувшись вокруг своей оси, Виола оставила халат в руках Главного и нанесла ему потрясающий по красоте удар с разворота в его картонную голову."


    stop music


    play music "audio/music/z_052.mp3" noloop


    "Голова вмялась, и образовавшаяся на месте виска огромная дыра выплюнула сгусток пыли."


    stop music


    play music "audio/music/z_023.mp3"


    show sp_vio_018:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    vio "Отдыхай, трухлявый!"

    hide sp_vio_018


    "Главный рухнул на плац и его голова откатилась в сторону. Тело шарило вокруг в поисках утерянной части. Но некоторые пионеры уже пинали эту голову друг другу."

    "Другие пионеры, не занятые этим своеобразным футболом, ходили по территории, отбирая у бессмысленно ползающих манекенов зажатые в картонных руках динамитные шашки."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Виола, я не знаю, что произошло, но, кажется, напасть миновала. Их надо оттащить с площади, вдруг они снова оживут?"

    hide sp_od_022


    show sp_vio_004:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Виолетта Церновна с подозрением посмотрела на нас с Алисой. Потом на памятник."

    vio "Так-так... Ваша работа?"

    "Казалось, она была огорчена таким исходом битвы."

    hide sp_vio_004


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Не понимаю, о чем Вы, Виолетта Церновна. Мы удивлены не меньше Вас. А что, всё уже кончилось? Мы ходили за шлангом. Семён сказал, они бояться воды."

    hide sp_al_004


    show sp_vio_004:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    vio "Ну да, врать вам не привыкать. Хорошо. Идите, помогите убрать этот хлам."

    vio "И ещё, там в пожарном щите два огнетушителя. Пользоваться умеете? Хорошо. Залейте то, что ещё горит. Пожара нам только не хватало."


    hide sp_vio_004


    scene cg dying_bonfire with dissolve

    "Костер на площади догорал. Огнетушители оказались вполне себе рабочими."


    pause (100000000000000000000000000000.0)


    scene bg dining with dissolve

    "Мы зашли на кухню, чтобы мобилизовать на большую уборку прятавшихся там пионеров, не принимавших участие в «битве»."


    show sp_ln_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Любовь Никаноровна сказала, что мальчики ушли готовиться к какому-то мероприятию, которое организовал Смутьянов."

    "Что-то вроде «партийного собрания», где они должны будут принять законы новой «пионерской республики» и избрать центральный комитет, пожизненного вождя и всё такое."

    hide sp_ln_002

    "Мы не стали их дожидаться."


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Появилась запыхавшаяся Юля, посланная еще в начале суматохи за мешочком волшебных грибов, которыми мы хотели воспользоваться, чтобы «умиротворить» восставших."

    "Идею тогда подал Семён."


    # stop music


    # play music "audio/music/z_023.mp3"


    scene cg mushroom_soup with dissolve

    "Юля с помощью тети Любы быстро сварила «грибной супчик», добавив туда еще каких-то трав."

    "Я не удержалась и даже попробовала ложечку (пока никто не видит). Было очень вкусно, но меня сразу потянуло в сон. Насилу растолкали. Мощная штука, этот грибной бульончик."


    scene bg dining with dissolve

    "Что касается второго отряда. История с манекенами их ничему не научила. Ожидаемого «сплочения «масс» перед общей бедой не случилось."

    "Хотя, они конечно вместе с нами боролись с манекенами, но как только «беда миновала», тут же принялись за свое."

    "Очевидно, «яд Смутьяновской пропаганды» проник в них глубоко."


    stop music


    play music "audio/music/z_910.mp3"


    scene cg dining_crowded with dissolve

    "Вскоре, оголодавшие после своих выборов пионеры, нагрянули в столовую и набросились на еду."

    "Они и не подумали заниматься уборкой в лагере."

    "Прятать отобранные у манекенов динамитные шашки, растаскивать завалы склада, а также убирать площадь от остатков костра и запчастей от валяющихся манекенов, пришлось первому отряду."

    "Нам помогали только часть пионеров третьего отряда и Эля."


    # stop music


    # play music "audio/music/z_120.mp3"


    "За обедом «революционеры» живо обсуждали последние новости, своё сборище, и кто какие «министерские портфели» получил в новом пионерском правительстве."

    "Смутьянова выбрали пожизненным диктатором, а Долговязого министром пропаганды."

    "Что-то я не замечала за ним способностей к красноречию, а министр информации, как мне кажется, должен был уметь красиво и связно излагать свои мысли."

    "Всё, что я помню из общения с Долговязым, это его вечные «заткнись, мелкая» и «сама такая»."

    "Ещё там у них был министр правды. Это вообще упасть-не-встать."

    "Значит, у него было своё министерство. Министерство правды. Не знаю такого министерства в нашей стране. Знаю только газету «Правда», которую выписывает мой папа."

    "Она конечно скучная, но зато правдивая, как он сам говорил."

    "Чем будет заниматься министерство правды в пионерском лагере, это конечно большой вопрос. Наверное, всем запретят врать."

    "Но это абсолютно невозможно. Даже я иногда вру. Как говорила мама, «ложь во благо». Это когда врешь, чтобы кого-то не наказали вместо тебя."

    "Ещё, кажется, у них был избран какой-то «комитет по расследованию зверств бывшего руководства»."

    "Это вообще непонятно. О каких таких зверствах шла речь?"

    "Наверное, о том, что их всех заставляли мыть руки перед едой и ноги перед сном, и о закаливании по утрам, которое так ненавидел Смутьянов?"

    "В общем, комитет назвали Чрезвычайным Комитетом, ЧК. И он должен был искать и карать."

    "Также под репрессии должны был попасть все инакомыслящие, то есть несогласные. Я вот, например."


    stop music


    play music "audio/music/z_333.mp3"


    scene cg parade with dissolve

    "Интересно, когда они меня казнят, будущие поколения будут проходить мимо моего памятника как в спектакле про мальчиша Кибальчиша, отдавая салют?"


    pause (1000000000000000000000000.0)


    "Я представила себе, как геройски погибну, запытанная до смерти Смутьяновым и его кликой, и даже всплакнула."

    "Такого хорошего человека угробят! Сволочи. Что я им плохого сделала? Ну врезала одному с ноги разок. А ещё, не позволяла никому говорить плохо о нашем отряде."

    "Но пусть. Потомки Ленину не забудут."


    stop music


    play music "audio/music/z_910.mp3"


    scene cg dining_crowded with dissolve

    "Кстати, этот мальчик из второго отряда, который был в меня влюблен, сбежал от них и тоже где-то прятался."

    "Они его ищут, чтобы провести над ним суд и объявить его РЕНЕГАТОМ, а потом показательно казнят (принесут в жертву Генде) как и всех, кого поймают из нашего отряда."

    
    show sp_vio_003:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Между тем, Виола, слушавшая стоя в стороне эти «планы», только ухмылялась."

    hide sp_vio_003


    "А я подумала, все-таки он оказался неплохой мальчик, надо его найти и спасти."

    "Особенно с удовольствием они обсуждали за столом, как они будут наказывать Ольгу Дмитриевну и директрису."

    "Об этом даже писать не хочется. Никогда не думала, до какой низости могут упасть люди."


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Я спросила у Юли, что будет, когда они проснутся, и как мы должны с ними поступить."

    "Она сказала: «НИКАК». Потому что они не будут даже помнить того, что натворили. Она положила им в суп какую-то лошадиную дозу грибов."

    hide sp_iul_009


    scene cg dining_lying_pioneers with dissolve

    "И точно, они засыпали и валились на пол тут же, в столовой."

    "Вскоре вся столовая храпела мощным храпом. Все двадцать человек."


    show sp_smu_007:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Потом неожиданно в столовую зашел Смутьянов, который припоздал."

    "Он с изумлением смотрел на своих товарищей, потом пытался их разбудить, но мы повалили его на пол и залили в него супчик."

    hide sp_smu_007

    "Вскоре и он спал как убитый."

    "Такой вот конец был у этой РЕВОЛЮЦИИ."


    stop music


    play music "audio/music/track2.mp3"


    scene cg meeting_total with dissolve

    "Потом нас собрала Ольга Дмитриевна, поблагодарила за помощь, поздравила с «победой»."


    pause (10000000000000000000000.0)


    "Еще она попросила не писать в дневниках об этом происшествии. Сказала, пусть это будет нашим секретом."

    "Все согласились, потому что понимали. Даже если кому рассказать... Все равно в такое никто не поверит."










    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day47

return