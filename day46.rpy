label day46:

    $ style.say_window = style.window

    $ days = 46

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_45_00 = True
    $ im_gal_45_01 = True
    $ im_gal_45_02 = True
    $ im_gal_45_03 = True
    $ im_gal_45_04 = True
    $ im_gal_45_05 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg forest1 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_478.mp3"


    "Рано утром я пыталась идти, но не смогла. К тому же наше кораблекрушение оставило свой след, я сильно ударилась коленкой о камень. Теперь она распухла и болела."

    "Семён сказал, что это не беда и что он дотащит меня до Юлиного убежища, а там её травки быстро поставят меня на ноги."

    "И я подумала, что он все-таки очень сильный. Ведь кроме меня, ему придется еще тащить два рюкзака, мой и Жени."

    "Я закрыла глаза и представила, как Семён несет меня на руках."


    scene cg sem_ul_carries with dissolve

    "Ну, как в фильмах про принцесс. Там принц всегда носит принцессу на руках. Это красиво."


    pause (100000000000000000000000000.0)


    "Но у них там нет рюкзаков. Поэтому я подумала, что на руках, конечно, эффектно, но непрактично. А на спине тоже неплохо."

    "И я представила, что ранена на поле боя. И Семён выносит меня из-под огня (как в фильмах про войну). А я такая - «Брось командир, не донесешь»..."

    "Раньше я никогда не каталась на спине у кого-то. Правда, когда-то папа сажал меня маленькую на плечо. Но это не в счет."

    "Только один раз мы играли в «колбасу», и я запрыгнула на спину кому-то из мальчишек. Но «колбаса» сразу развалилась и покататься не получилось."

    "А тут сам Семён будет нести меня на спине почти до лагеря. И я вскарабкалась ему на спину, а он подхватил меня снизу под коленки, и так получилось неплохо."


    scene cg sem_ul_carries2 with dissolve

    "И мы пошли через чащу..."


    pause (100000000000000000000000000.0)


    "А я как бы случайно держалась, закрывая ему глаза, и он там смешно рычал. И говорил: «Вот упадем, будешь ночевать в кювете. Р-р-р-р». Это была игра."

    "А я говорила ему, как Машенька медведю: «Семён, сядь на пенек, съешь пирожок!» Хотя не было у нас никакого пирожка. А я бы от него не отказалась."

    "Но были два бутерброда. Женя их заботливо завернула в целлофан, они почти не размокли."

    "Семён, казалось, не уставал. А ведь я увесистая. Я посоветовала ему чаще делать привалы. Но он только отшучивался."


    scene bg forest2 with dissolve

    "Мы шли с горы, а с горы всегда легче. Озеро было где-то внизу, и мы шли уже по тропе, которая должна была вывести нас к нему."

    "Наконец, я увидела пенек. И вот тут я уже заставила Семёна сесть. Это был первый привал."

    "И я ещё поспала у него на руках. Это было так здорово. Так я себя ощущала только с бабушкой, когда гостила у неё в деревне."


    scene cg ul_granny with dissolve

    "Она замечательные делала пельмешки. От них бы я сейчас точно не отказалась. В ее доме было тепло, уютно и хорошо пахло."


    pause (100000000000000000000000000.0)


    "От Семёна тоже шел приятный запах. Не такой, как от бабушки, когда я зарывалась носом в её руки."

    "Руки у неё были большие, теплые и шершавые. «Это от подойников» – говорила она. Бабушка работала на молочной ферме."


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


    scene cg sem_ul_carries3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_495.mp3"


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



    "Он слился в плотную массу, вот прямо без веток и деревьев, и покачивался. Не знаю, как это описать."

    "А может быть, это я качалась в такт шагов Смена. Но это было так удивительно!"

    "Никогда раньше я не ощущала такого странного чувства. Как будто я сама стала частью этого изумрудного вязкого марева и ощущала дыхание ароматного, хвойного ветра."

    "И что я тоже колыхалась, как деревья. Чувствовала свои листья, что по ним ползут букашки и что я тяну соки из земли..."

    "Это было потрясающее состояние, как очень красивая и интересная галлюцинация. И я подумала, вдруг я съела чего-нибудь такого..."

    "Внезапно Семён остановился, а лес продолжил покачиваться. И я услышала, как он сказал: «ВОЛШЕБНО»."

    "Мы стояли и смотрели на колышущийся лес. То есть он стоял, а я была на его руках."

    "И я прижалась к нему, потому что мне все-таки было немножко страшно. А вдруг лес проглотит нас навсегда?"


    scene bg forest3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_516.mp3"


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

    sem "В общем, надо быстрее добраться до домика Юли, а то нам каюк. Так у нас не только лес оживет но и земля.  Все оживет: листья, ягоды, грибы, желуди."

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


    stop music fadeout 0.5

    queue music "audio/music/track4.mp3"


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

    "Облака отражались в воде и были как будто над нами и под нами. И у меня возникла идея."


    scene an_d46_05 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тут мелко, давай войдем в воду, и будем стоять как бы на тучах."


    scene cg sem_ul_clouds with dissolve

    "Так и сделали. Облака были классные, как стадо барашков."


    pause (100000000000000000000000000.0)


    scene cg sky2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1015.mp3"


    "Семён рассказал мне про своё детство."

    "Оказывается, эти времена у всех чем-то похожи. Но только я, как он, не ходила в спортивную секцию, а вот  по крышам и заборам  тоже лазала и воровала яблоки в соседском саду."

    "И мы делились всякими секретами, где и как лучше что-то стащить. Вот орехи, например. Тут надо осторожно. Если сторож увидит, то хана."

    "И что надо связать рубашку рукавами и получиться мешок для орехов, а чтобы больше влезло, чистить их прямо под кустом и складывать в рубашку уже чищенные. Ну и всё такое."

    "И мы не заметил как проговорили, наверное, целый час, а может быть два."

    "И мне стало казаться что мы знаем друг друга уже сто лет. А ещё я случайно рассказа ему про то, что мы нашли на прииске."


    scene cg scull with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


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



    scene an_46_03 with dissolve


    pause (10000000000000000000000.0)


    "Сделала вид, что кусаю его. А он от меня отшатнулся и бросился бежать."


    scene an_d46_05 with dissolve

    show sp_ul_020:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я стояла, как дура, на берегу и ничего не понимала. И я закричала:"

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


    stop music fadeout 0.5

    queue music "audio/music/z_048.mp3"


    pause (10000000000000000000000.0)


    "И я вдруг поняла, что озеро не просто блестит, а дрожит. Вода покрылась рябью, потому что озеро что-то трясет, а из-под земли гул и тоже какая-то дрожь. Прямо как в лагере тогда."

    "Вот про это и сказал Семён «ВИБРАЦИЯ». И я вспомнила притчу Пионера про детей. И кажется, я стала понимать. Что когда гудит земля, то ЖЕЛАНИЯ ИСПОЛНЯЮТСЯ."

    "И еще я вспомнила слова Юли, что камушки усиливают желания, и когда начинается вибрация, материализуют их."

    "Я посмотрела еще раз на камушек и спрятала его. А Семён еще долго не приближался, пока я сама к нему не подошла и не села ему на колено."


    scene an_d46_05 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_002.mp3"


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


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    "Ну вот... Потом мы перекусили остатками Женькиного бутерброда (первый мы съели ещё там, в шалаше) и пошли дальше."


    scene cg sem_ul_cutlet3 with dissolve

    "Теперь притворяться уже было бессмысленно, и я шла сама. Хотя иногда канючила, что «хочу на ручки»."


    pause (100000000000000000000000000.0)


    "Но он только смеялся. Сказал, что в ДОКТОРА мы поиграем, когда я по настоящему устану или снова заболею. А в КАПРИЗНУЮ ДЕВОЧКУ играть не будем. Мол, я уже взрослая."

    "Тогда я ему заявила, что если я уже взрослая, то следующий поцелуй пусть будет не в лобик, как в прошлый раз, с котлетой."

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


    scene bg iul_hide2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_011.mp3"


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


    scene bg uhouse4 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


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


    scene bg old_well with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_005.mp3"


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

    ul "Конечно, узнаю. Хоть это и было ночью. Странно, а ты откуда о нем знаешь?"

    hide sp_ul_021


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Я рассказала. Именно через тайный ход, который ведет из Старой Лаборатории на остров, я попадаю в лагерь, когда Бурлейка разливается и сносит все мосты на бродах."

    hide sp_iul_012


    "Так я узнала про то, что Семён регулярно пользуется тайным ходом. "


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_910.mp3"


    "Вскоре мы были уже в лагере. Все в это время были в столовой. Мы заглянули туда. Нас радостно встретили. Все переживали за нас."


    scene bg attic2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


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
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

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


    scene bg mus with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_132.mp3"


    "Все собрались в музкружке и там был «военный совет»."

    "Ольга Дмитриевна подробно изложила нам ситуацию последнего дня и спросила:"


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Какие будут предложения по восстановлению дисциплины? Я на вас сильно рассчитываю."

    hide sp_od_022


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "В лагере назревала смута."

    "Пионеры строились в колонны и с новой песней (не иначе, автором был Смутьянов) и двигались на площадь."


    scene cg right_pioneers_march with dissolve


    stop music fadeout 0.5

    queue music "audio/music/right_pioneers_march.mp3"


    "Стройся в колонну шеренгами, в ряд, по четыре\nПравофланговым, равнять на железный наш строй!\nВ этом нелепом, кривом и неправильном мире\nМы лишь идем, рассчитавшись на первый-второй"

    "Пусть в нас не верят, но нам наплевать на оценки\nЗдесь свою веру в тебя, измеряет другой\nГалстук есть красный мандат, на поставить всех стенке\nНо сначала спроси себя - С кем я ? И кто я такой?"

    "Стройся в колонну шеренгами, в ряд, по четыре\nПравофланговым, равнять на железный наш строй!\nВ этом нелепом, кривом и неправильном мире\nМы лишь идем, рассчитавшись на первый-второй"

    "Мир наш прогнил, в нем уже компромисс невозможен\nЖизни в нем хватит едва на короткую повесть\nЗубы сцепив, говорим себе, «Делай, что должен!»\nВерим в закон. И закон наш, конечно же – совесть"

    "Стройся в колонну шеренгами, в ряд, по четыре\nПравофланговым, равнять на железный наш строй!\nВ этом нелепом, кривом и неправильном мире\nМы лишь идем, рассчитавшись на первый-второй"

    "Если свернул не туда, терпеливо поправим
    \nПримем ряды, несогласным ломая хребты\nПомни, что ты пионер и держись наших правил\nДать слабину может кто-то, но точно, не ты"

    "Стройся в колонну шеренгами, в ряд, по четыре\nПравофланговым, равнять на железный наш строй!\nВ этом нелепом, кривом и неправильном мире\nМы лишь идем, рассчитавшись на первый-второй"


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


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
        "images/an/an46day/an_d46_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_89.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_90.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_91.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_92.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_93.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_94.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_95.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat



    scene an_46_04 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_049.mp3"



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



    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    "Мы бросились к складу."


    show sp_od_027:
        yalign 0.0 subpixel True
        xalign 0.30 subpixel True
        zoom 1.1
    with dissolve

    "Ольга пыталась загородить нам путь, но мы с Алисой ловко поднырнули под её расставленные руки и добежав до склада, запрыгнули туда в последний момент перед вторым ВЗРЫВОМ."


    stop music fadeout 0.5


    play music "audio/music/z_047_2.mp3" noloop


    scene cg capter_explosion with dissolve

    "Взрыв был сильный!"


    pause (100000000000000000000000000000.0)


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


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


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


    stop music fadeout 0.5


    play music "audio/music/z_051.mp3" noloop


    "Мы, все трое, закричали: «УРА! Подмога!»"


    scene cg stock_mannequins3 with dissolve


    stop music


    play music "audio/music/z_202.mp3"



    show sp_vio_020:
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


    scene bg camp_artifacts with dissolve

    "Битва переместилась на площадь."

    "Мне удалось вытащить из помещения склада ящик с ацетоном и раздать бутылки всем желающим, объясняя на ходу, как сделать «коктейль Молотова»."

    "Пионеры притащили простыни, которые рвали на длинные полосы. Они обматывали их вокруг бутылок, опускали один конец внутрь бутылок и, поджигая другой конец, бросали в толпу манекенов."

    "Не обошлось без потерь и со стороны юных ленинцев. Двоих девочек врагу удалось пленить и утащить в помещение склада, где уже лежал связанный Петрович."

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

    al "Стоп! Всем стоп! Давайте выясним, чего они хотят."

    al "ПЕРЕГОВОРЫ!"


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1003.mp3"



    "Похоже, манекены хотели того же. Они прекрасно понимали, что рано или поздно их количество перестанет быть достаточным для сопротивления."

    "И хотя, обезображенные ударами пионеров, «тела» всё ещё корчились и пытались встать с земли, они были уже ни на что не годны."

    "Один из манекенов, с повязкой на лбу, раздававший приказания голосом диктора метрополитена и, очевидно, ГЛАВНЫЙ, поднял руку."

    "Битва на время прекратилась. Он выступил вперед."


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_mann_002:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3

    manneq "У нас ваши заложники. Также, мы можем взорвать лагерь, если поймем, что проиграли. Однако, у вас есть тот, кто нам нужен. Если вы отдадите его, мы уйдем."

    hide sp_mann_002


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Мы однозначно не отдадим никого из людей. Но все же интересно, кто это?"


    scene black with dissolve

    show sp_elya_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2



    manneq  "У вас есть андроид."

    manneq "Она нужна нам для... \n(он замялся)"

    manneq "Это вопрос выживания."


    scene bg camp_artifacts with dissolve


    show sp_mann_004:
        yalign 0.15 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    show sp_mann_002:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3

    manneq "Так как вы уничтожили последнего манекена-женщину. Только что. Вы не оставили нам выбора."

    hide sp_mann_004 with dissolve


    manneq "Отдайте нам андроида, и мы уйдем в Бункер к своим товарищам."

    hide sp_mann_002


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


    show sp_vio_028:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Виола, насмешливо наблюдая за переговорами:"

    vio "Это нам понятно, господин Главнокомандующий Картонными Войсками. Вы лучше скажите, зачем вы это начали и какова была ваша первоначальная цель?"

    hide sp_vio_028


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    show sp_mann_002:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3
    with dissolve

    manneq "Нас создал гений, а не ваша наука. Он вложил в уста сторожа заклинание. Но сейчас нашего создателя, к сожалению, нет с нами, иначе бы вам пришлось плохо."

    manneq "Мы схватили сторожа потому, что он отрекся от нашего создателя. Оскорбил его и пытался разрушить его творение, то есть НАС."

    manneq "Такое непростительно. Мы хотели спокойно уйти. Но он пытался уничтожить нас. И поплатился."

    manneq "Он жив только потому, что наш Создатель не дал нам указаний, что делать с этим ничтожеством."

    manneq "Мы обменяем ваших двух пионерок и собаку на свободный проход. Но сторожа мы забираем с собой. Позже он будет предан суду."

    manneq "Вы пытаетесь жечь нас этой жидкостью. Но посмотрите, почти у каждого из нас уже есть в руках динамитная шашка. Их было полно у вашего сторожа. Мы вскрыли один ящик."

    manneq "И поверьте, вам будет несдобровать, если я дам команду."

    manneq "Нас около тридцати, а вас кажется меньше двадцати, минус две девочки и сторож. Подумайте трезво: война и неизбежное поражение, или моё выгодное предложение?"


    hide sp_mann_002


    stop music fadeout 0.5

    queue music "audio/music/z_197.mp3"


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


    show sp_vio_027:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Между тем, ввиду события, явно переломившего «ход боевых действий», Ольга и Виола склонялись в сторону принятия предложения Главного. Это было заметно."


    scene bg camp_artifacts with dissolve


    show sp_elya_014:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Привели Элю. Рвущихся не допустить ОБМЕНА Электроника и Шурика держали за руки пионеры."

    hide sp_elya_014 with dissolve


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

    ul "Так что есть надежда, что в лагере не появятся всякие новые ожившие кастрюли, швабры, музыкальные инструменты и бог знает что ещё."

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


    scene cg mannequin_world with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


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

    al "Ну, что теперь?"

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


    image an_46_11: # Анимация поворот таблички


        "images/an/an46day/an_d46_65.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_66.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_67.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_68.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_69.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_70.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_71.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


    scene an_46_11 with dissolve


    pause (100000000000000000000000000000000000.0)


    "За ней оказался какой-то рычаг."


    al "Рубильник, что ли? Током не ударит?"

    "Алиса обмотала руки снятыми гольфами, и я сделала то же самое. Мы ухватились за рычаг."


    image an_46_12: # Анимация рубильник



        "images/an/an46day/an_d46_72.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_73.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_74.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_75.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_76.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_77.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_78.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_79.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_80.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_81.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_82.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_83.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_84.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_85.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_86.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_87.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_88.webp" with Dissolve(0.5, alpha=True)
        pause 0.5




    scene an_46_12 with dissolve

    "Раз, два, три! Рычаг со скрипом ушел вниз."


    pause (100000000000000000000000000000000000.0)


    image an_46_06: # Анимация памятник поворачивается

        "images/an/an46day/an_d46_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


    stop music fadeout 0.5


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


    scene cg fallen_manns with dissolve


    stop music


    play music "audio/music/z_151.mp3"


    "Мы посмотрели на площадь. Манекены вдруг стали бесцельно двигаться взад и вперед. Многие упали на колени и пытались ползти."


    pause (1000000000000000000000000000.0)


    "Дольше всех на ногах стоял Главный. Он цеплялся за Виолу, чтобы не упасть. Она коротким движением ударила его в грудь, но он успел схватить её за халат."


    scene cg vio_mann with dissolve

    "Крутанувшись вокруг своей оси, Виола оставила халат в руках Главного и нанесла ему потрясающий по красоте удар с разворота в его пластмассовую голову."


    pause (1000000000000000000000000000.0)


    stop music


    play music "audio/music/z_052.mp3" noloop


    "Голова вмялась, и образовавшаяся на месте виска огромная дыра выплюнула сгусток пыли."


    scene bg camp_artifacts with dissolve


    stop music


    play music "audio/music/z_023.mp3"


    show sp_vio_018:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3
    with dissolve

    vio "Отдыхай, трухлявый!"

    hide sp_vio_018


    "Главный рухнул на площадь и его голова откатилась в сторону. Тело шарило вокруг в поисках утерянной части. Но некоторые пионеры уже пинали эту голову друг другу."

    "Другие пионеры, не занятые этим своеобразным футболом, ходили по территории, отбирая у бессмысленно ползающих манекенов зажатые в пластмассовых руках динамитные шашки."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Виола, я не знаю, что произошло, но, кажется, напасть миновала. Их надо оттащить с площади, вдруг они снова оживут?"

    hide sp_od_022


    show sp_vio_018:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3
    with dissolve

    "Виолетта Церновна с подозрением посмотрела на нас с Алисой. Потом на памятник."

    vio "Так-так... Ваша работа?"

    "Казалось, она была огорчена таким исходом битвы."

    hide sp_vio_018


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Не понимаю, о чем Вы, Виолетта Церновна. Мы удивлены не меньше Вас. А что, всё уже кончилось? Мы ходили за шлангом. Семён сказал, они боятся воды."

    hide sp_al_004


    show sp_vio_018:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3
    with dissolve

    vio "Ну да, врать вам не привыкать. Хорошо. Идите, помогите убрать этот хлам."

    vio "И ещё, там в пожарном щите два огнетушителя. Пользоваться умеете? Хорошо. Залейте то, что ещё горит. Пожара нам только не хватало."


    hide sp_vio_018


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


    scene cg mushroom_soup with dissolve

    "Юля с помощью тети Любы быстро сварила «грибной супчик», добавив туда еще каких-то трав."

    "Я не удержалась и даже попробовала ложечку (пока никто не видит). Было очень вкусно, но меня сразу потянуло в сон. Насилу растолкали. Мощная штука, этот грибной бульончик."


    scene bg dining with dissolve

    "Что касается второго отряда. История с манекенами их ничему не научила. Ожидаемого «сплочения «масс» перед общей бедой не случилось."

    "Хотя, они конечно вместе с нами боролись с манекенами, но как только «беда миновала», тут же принялись за свое."

    "Очевидно, «яд Смутьяновской пропаганды» проник в них глубоко."


    scene cg dining_crowded with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_910.mp3"


    "Вскоре, оголодавшие после своих выборов, пионеры, нагрянули в столовую и набросились на еду."

    "Они и не подумали заниматься уборкой в лагере."

    "Прятать отобранные у манекенов динамитные шашки, растаскивать завалы склада, а также убирать площадь от остатков костра и запчастей от валяющихся манекенов, пришлось первому отряду."

    "Нам помогали только часть пионеров третьего отряда и Эля."


    stop music fadeout 0.5

    queue music "audio/music/z_177.mp3"


    "За обедом «революционеры» живо обсуждали последние новости, своё сборище и кто какие «министерские портфели» получил в новом пионерском правительстве."

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


    scene cg parade with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    "Интересно, когда они меня казнят, будущие поколения будут проходить мимо моего памятника как в спектакле про мальчиша Кибальчиша, отдавая салют?"


    pause (1000000000000000000000000.0)


    "Я представила себе, как геройски погибну, запытанная до смерти Смутьяновым и его кликой, и даже всплакнула."

    "Такого хорошего человека угробят! Сволочи. Что я им плохого сделала? Ну врезала одному с ноги разок. А ещё, не позволяла никому говорить плохо о нашем отряде."

    "Но пусть. Потомки Ленину не забудут."


    scene cg dining_crowded with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_177.mp3"


    "Кстати, этот мальчик из второго отряда, который был в меня влюблен, сбежал от них и тоже где-то прятался."

    "Они его ищут, чтобы провести над ним суд и объявить его РЕНЕГАТОМ, а потом показательно казнят (принесут в жертву Генде) как и всех, кого поймают из нашего отряда."


    scene cg dining_crowded2 with dissolve
    
    show sp_vio_028:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Между тем, стоявшая в стороне Виола, слушая эти «планы», только ухмылялась."


    scene cg dining_crowded with dissolve

    "А я подумала, все-таки он оказался неплохой мальчик, надо его найти и спасти."

    "Особенно с удовольствием они обсуждали за столом, как они будут наказывать Ольгу Дмитриевну и директрису."

    "Об этом даже писать не хочется. Никогда не думала, до какой низости могут упасть люди."


    scene cg dining_crowded2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_910.mp3"


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Я спросила у Юли, что будет, когда они проснутся, и как мы должны с ними поступить."

    "Она сказала: «НИКАК». Потому что они не будут даже помнить того, что натворили. Она положила им в суп какую-то лошадиную дозу грибов."

    hide sp_iul_009


    scene bg dining with dissolve

    "И точно, они засыпали и валились на пол тут же, в столовой."

    "Вскоре вся столовая храпела мощным храпом. Все двадцать человек."

    "Такой вот конец был у этой РЕВОЛЮЦИИ."


    scene cg squad_formation6 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/track2.mp3"


    "Потом нас собрала Ольга Дмитриевна, поблагодарила за помощь, поздравила с «победой»."


    pause (10000000000000000000000.0)


    "Еще она попросила не писать в дневниках об этом происшествии. Сказала, пусть это будет нашим секретом."

    "Все согласились, потому что понимали. Даже если кому рассказать... Все равно в такое никто не поверит."


    scene bg dining with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"


    "В лагере наступила непривычная тишина."

    "Мы пошли в столовую. Надо было помочь Любови Никаноровне с чисткой картошки. Кроме нашего отряда помогать ей было некому, потому что пионеры крепко спали."

    "За этим занятием мы обсудили последние события."

    "Вибрация возобновилась. Было очевидно, что МАШИНА самообучается и поэтому надо искать вход в «машинный зал». В этом нам поможет карта Петровича."


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но ведь мы были в Бункере. Нет там никакой машины!"

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Узкоколейка через болота ведет в здание новой лаборатории, а мы были в старой. Новую, согласно документам из Архива, построили сразу же после взрыва."

    al "Юля сказала, что здание не разрушено, но все двери там железные и они заварены."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Снова идти через болота? Я до сих пор в ужасе от той нашей попытки. В этот раз может и не повезти."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А мы и не пойдем. Мы поедем."

    hide sp_al_005


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Как это?"

    hide sp_ul_012


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Зачем-то же строили узкоколейку к лаборатории. Помнишь, когда мы прошли по строй железной дороге и увидели узкоколейку, то она тянулась в обе стороны?"

    al "Мы вышли на неё посередине. Но рельсы уходили не только в сторону болот, но и в сторону лагеря."

    al "Если посмотреть по карте, то железная дорога отмечена на ней синим. А рядом проходит более узкая и тоже синяя линия. Они в одном месте почти соединены."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ты полагаешь, что узкоколейка тянется до самого лагеря?"

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я уверена, что существует «конечная остановка»."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но мы же всё тут облазили. Кроме..."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Кроме кабинета Виолы."

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я была там, в её кабинете. Там ничего нет. Только топчан для массажа, стол и всякие инструкции на стенах. Ещё есть шкаф. Там все лекарства."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Тут что-то не то. Помнишь, как Виола оставалась ночевать в медпункте? Но когда я заглядывала в окно медпункта и в окно кабинета, её там не было. Она просто растворилась."

    al "Есть там какой-то ход."

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Сегодня же ночью, надо пробраться в её кабинет."

    hide sp_ul_013


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А где Долговязый? Его не было со всеми когда его отряд пришел на ужин и второй отряд тоже не весь, как минимум пары человек нет."

    hide sp_al_002


    "Мы вышли в зал столовой и пересчитали спящих. Точно! Не было Долговязого и еще нескольких пионеров."


    scene cg tuz_gan with dissolve

    "Мы сразу выскочили во двор и заметили группу, стоящую возле склада."


    pause (10000000000000000000000000000.0)


    "Долговязый и пара мальчиков с ним, привязали Тузика к забору и кидали в него камешки, наблюдая как бедное животное уворачивается."


    play miscSounds "audio/music/z_061.mp3"


    "Было ясно, что вибрация усиливает плохие стороны человеческой натуры. Вполне нормальные еще вчера ребята так бы себя не вели."

    "Алиса закричала на них. Но они и ухом не повели."

    "А я сильно разозлилась. Я подумала, что будь Тузик большим и сильным, он разорвал бы обидчиков."


    stop miscSounds


    play miscSounds "audio/music/z_062.mp3" noloop


    scene cg tuz_gan2 with dissolve

    "Дальше произошло странное. Тузик стал темнеть, шерсть на нём окрасилась в почти чёрный цвет, он оскалился и стал как будто крупнее. Да, он рос прямо на глазах!"


    pause (10000000000000000000000000000.0)


    "Тут я с испугом вспомнила, что кристаллы, которые я забрала со склада, всё еще при мне. Мысли о них вылетели у меня из головы."

    "Я сунула руку в карман шорт. Да, они были всё ещё в кармане. Надо было выбросить их. Но, было поздно."

    "Мальчишки, опешившие от вида громадного пса, легко порвавшего веревку, бросились врассыпную."

    "Долговязый бежал быстрее всех. Но Тузик, обогнав группу, помчался именно за ним. Тот бежал к лесу, в надежде добежать до дерева и взобраться на него."

    "И наверное успел бы, если бы не споткнулся."


    stop music


    stop miscSounds


    play music "audio/music/z_062.mp3" noloop


    play miscSounds "audio/music/z_063.mp3" noloop


    scene cg tuz_gan3 with dissolve

    "Упавшего Долговязого накрыла черная тень..."

    "Раздался душераздирающий крик."


    pause (10000000000000000000000000000.0)


    stop music


    stop miscSounds


    play music "audio/music/z_171.mp3"


    "Для Долговязого всё было кончено."

    "Пионеры стояли оцепенев. Никто не бросился помогать своему товарищу. Все были скованы ужасом."

    "Пес поднял окровавленную морду, посмотрел на лагерь и исчез в густых зарослях."


    scene bg dining with dissolve

    "Пионеры забежали в столовую в поисках Ольги Дмитриевны, очевидно, чтобы рассказать ей о страшном происшествии."

    "Они были очень испуганы, пытались растолкать спящих, чтобы поделится с ними увиденным. Но те спали крепко."


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Надо их задержать!"

    hide sp_al_007


    "Алиса быстро сориентировалась, сказав, что сама сбегает к ОД, и чтобы они ждали тут. Сделала вид, что уходит. А сама махнула мне рукой, показывая на кастрюлю с грибным супчиком."

    "Я успокоила пионеров, как могла, и сказала, что пока мы ждем ОД, надо хотя бы перекусить."

    "Они долго не могли успокоится, наперебой делясь впечатлениями, а я разливала им суп по тарелкам."

    "Волнения и голод сделали свое дело. Из-за войны с манекенами обед в лагере не случился. Вскоре и они тоже спали мертвецким сном."


    scene bg dining with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"



    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    "Появилась Алиса, она привела с собой ОД."


    hide sp_od_022

    "Алиса прижала палец к губам, делая мне знак. А потом шепнула:"

    al "Пусть они потом сами наткнутся на тело или то, что от него осталось. Все равно никто ничего после сна не вспомнит. Так мы спасем Тузика."

    al "Не факт, что его потом не станут искать вызванные в лагерь МП охотники, чтобы убить собаку-людоеда."


    scene bg dining with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_197.mp3"



    "ОД сказала, чтобы мы не будили уснувших в столовой. Мы усадили их на стулья. Так они и спали, положив головы на столы."

    "Время от времени, те кто просыпались, медленно, шатаясь, шли к выходу, откуда мы их по одному разводили по домикам."

    "Когда столовая опустела, мы тоже поужинали. Потом пошли к себе, и с нами увязалась Мику."

    "По всему лагерю летал пепел от сожженных воззваний, листовок и прокламаций «революционеров». По площади ветер носил разбросанные Смутьяновым обгоревшие листочки."

    "Кое где текст на них сохранился. Алиса подняла одну из них. В домике мы внимательно изучили воззвание."


    scene cg leaflet2 with dissolve


    pause (10000000000000000000000.0)


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Смутьянова работа. Вот гад! Смотри, что пишет. Значки ему наши не нравятся. Между прочим, на вождя твоего бочку катит."

    al "Напечатано-то на машинке Маргариты Павловны. Они точно взломали административный корпус."


    scene bg auhouse_crop1 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Им за это будет!"


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ничего им не будет. Проспятся от грибочков и на голубом глазу все будут отрицать. Они же даже не вспомнят ничего."

    al "На, сохрани для нашего архива."


    scene cg leaflet2 with dissolve

    $ inv_item_24 = True

    
    show got_leaflet with dissolve



    pause (10000000000000000000000.0)


    scene bg auhouse3 with dissolve


    show sp_mi_019:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Ну-ка, дай, посмотрю. Вот дела... Получается, мы стали участниками стихийного движения народных масс."


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Как сказал бы Смутьянов."


    scene bg auhouse_crop1 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Или Вопиющего Безобразия, как сказала бы Маргарита Павловна."


    scene bg auhouse3 with dissolve
    
    "Все засмеялись."

    show sp_mi_015:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Между тем, Мику беспрестанно теребила свои хвостики и закидывала их за спину. Она всегда делала так, когда волновалась и хотела что-то сказать."

    "Было видно, что она едва сдерживается, чтобы не выложить какую-то очередную «тайну»."


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Чего маешься? Ну, говори. Я же вижу, ты хочешь что-то рассказать. Например, куда вы с Женей исчезли, когда все началось."


    scene bg auhouse3 with dissolve

    show sp_mi_019:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Да. Я не стала говорить при всех, но вам расскажу. Нас не было тогда на площади с Женей в первые минуты, это правда. Но потом мы тоже помогали."


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Испугались?"


    scene bg auhouse3 with dissolve

    show sp_mi_019:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Нет. Вовсе нет. Это не наша вина. Виола спрятала нас, когда в лагере начались беспорядки и когда распяли чучело."

    mi "Они стали искать всех из первого отряда, и Виола испугалась за нас. Она заперла нас у себя. Но когда она ушла, мы вылезли через окно."


    scene bg auhouse_crop2 with dissolve

    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Но, насколько я знаю, пионеры заглядывали в медпункт! Как они вас не нашли?"


    scene bg massage with dissolve

    mi "Потому что она заперла нас в массажном кабинете. Виола просила не говорить никому. В общем, там есть топчан для массажа."


    pause (10000000000000000000000.0)


    scene bg massage2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    mi "Она нажала на одну ножку, и он встал на дыбы. Под ним открылся люк, такой квадратный, и лестница вниз. Мы все туда спустились."


    pause (10000000000000000000000.0)


    mi "А потом топчан с люком встали на место. Я ещё удивилась, зачем в медпункте такой люк? Но Виола сказала, что это спуск в бомбоубежище."


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "И что было потом? Вы пошли..."


    scene bg bomp_shelter3 with dissolve

    mi "Никуда мы не пошли. Виола усадила нас в небольшом помещении с лавками."


    pause (10000000000000000000000.0)


    mi "Сели на лавку, длинную такую. Она сказала, чтобы мы сидели тихо. А сама куда-то быстро исчезла."

    mi "Там был еще длинный коридор, он куда-то уходил далеко. Но мы туда не пошли. Он мрачный."


    scene bg auhouse3 with dissolve

    show sp_mi_019:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "А потом наверху началось что-то невообразимое, мы не выдержали и вылезли через люк, а потом через окно."


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да, «А ларчик просто открывался». Спасибо тебе, Мику, ты нам очень помогла."


    scene bg auhouse3 with dissolve

    show sp_mi_017:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Вы же не собираетесь туда?"


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Конечно, нет. Просто интересно знать про все тайны лагеря. Ты же знаешь, Ульяна пишет историю «Совенка»."


    scene bg auhouse3 with dissolve

    show sp_mi_020:
        yalign 0.07 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Ладно, тогда я пошла. Вы же никому не расскажете?" 


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Обещаем."


    scene bg medic2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "В тот же вечер мы, конечно же, пробрались в медпункт через оставленную открытой форточку. Я пролезла. Открыла окно и впустила Алису."

    "Мы сделали всё, как рассказывала Мику. И действительно, механизм сработал."


    scene bg bomp_shelter3 with dissolve

    "Мы спустились в люк и пошли по коридору мимо той самой лавочки."


    scene bg hangar with dissolve

    "В конце коридора был небольшой ангар, в котором на полу были рельсы. Догадка Алисы нашла свое подтверждение. На рельсах стояло что-то, накрытое брезентом. Мы с Алисой стащили этот чехол."


    pause (10000000000000000000000.0)


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Дрезина."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "О, я такое только в фильмах видела!"

    hide sp_ul_021


    "Рельсы уходили в широкий тоннель и пока Алиса изучала устройство дрезины я прошла по нему вперёд."

    "Он уходил куда-то очень далеко. Самое интересное, что он был освещен. Очевидно, при открытии люка, автоматически зажигался свет."

    "Я вернулась. Алиса уже сидела в сиденье и указала мне на сиденье напротив. Между сиденьям был большой рычаг."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Хватайся. Надо качать рычаг вперед и назад. Там внизу маховик. Как раскрутится, мы поедем."

    hide sp_al_056


    "Я села. Рычаг был выше моей головы."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Давай, я стоя. Мне не удобно сидя. Это для взрослого человека."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Улька, вот ты дурында. Подкрути стул, он на винте. Делается выше и ниже... Ну что, получилось?"

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, отлично. Вот сейчас удобно. Правда, я на цыпочках сижу, но уже лучше."

    hide sp_ul_021


    scene cg handcar with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_053.mp3"


    "Мы стали качать рычаг, по очереди отталкивая его от себя."


    pause (10000000000000000000000.0)


    "Дрезина заскрипела и медленно тронулась. Потом всё быстрее и быстрее. Наконец, она поехала так быстро, что лампочки в тоннеле стали мелькать, сливаясь в одну белую полосу."

    "Через некоторое время мы выскочили на поверхность. Перед тем как это произошло, перед нами разъехались створки каких-то больших дверей."

    "Я оглянулась, но за нами сзади был холм весь поросший кустами. В нём, очевидно, и находился выход. Створки снова съехались вместе, и их не стало видно за кустами."

    "Как будто и не было никакого входа в подземелье."

    "Начала всходить Луна, поэтому было хорошо видно две полосы рельс, отсвечивающих в сумерках."

    "Дрезина, постукивая на стыках, катилась в сторону леса, за которым простиралась ТОПЬ."

    "Я налегала на рычаг, стараясь не отставать от Алисы. Мы вошли в ритм и не думали ни о чём. Просто смотрели, как мимо плывёт трава."

    "Пахло лугом, болотом и... Чем-то неуловимо знакомым."


    al "Ты тоже это чувствуешь?"


    "И тут я поняла! Пахло костром, и Алиса указала на огонек вдали."


    al "Похоже, хозяин блиндажа вернулся. Но нам лучше не встречаться. Интересно, кто это? Но сейчас у нас другая задача. Мы должны пробраться в лабораторию."

    ul "И как мы это сделаем? Петрович говорил, что там все двери заварены чтобы не лазали пионеры."

    al "Ещё никто не заваривал крыши. Мы просто разберем потолок. Благо, у нас есть опыт лазанья по крышам. Помнишь Дом на Болотах?"

    ul "Мы стали медленнее ехать. Наверное, дрезина пошла в гору."

    al "Давай встанем. Эти стулья можно убрать. Видишь, они отводятся вбок? Стоя навалимся. Так удобнее. И всем телом. Главное, преодолеть этот пригорок, а там снова ровно."


    stop music fadeout 0.5

    queue music "audio/music/z_054.mp3"


    "Мы встали и качали рычаг стоя. Дрезина весело взвизгнула всеми колесами и снова начала разгоняться."


    ul "Так, а с пригорка? Тормозов-то у нас нет!"

    al "Может и есть, просто я не нашла. Но зачем нам тормоза? Пусть катиться сама, а мы отдохнем."

    al "Если что, приготовься прыгать на ходу. Судя по карте, узкоколейка проходит мимо лаборатории и идет дальше до шахты. По-любому, десантироваться нужно будет."

    al "Когда будем прыгать, прыгай под углом ноги впереди а голова сзади. Чтобы когда приземлишься тебя бросило вперед и ты выровнялась."

    al "Как коснешься земли, сразу беги. Так не убьешься. Главное, держи ноги напряженными."

    al "Но если все-таки кинет вперед, сворачивайся калачиком и катись как мячик. Иначе сломаешь что-нибудь."

    al "Мы сейчас идем на спуск. По моим ощущениям, мы набрали приличную скорость."

    ul "Агась, буду как мячик..."


    stop music fadeout 0.5

    queue music "audio/music/z_053.mp3"


    "Вдали появился лесок, а за ним виднелась коричневая крыша старой лаборатории."

    "Здание было двухэтажным. Никто из нас никогда не был в этих местах, и мы с Алисой с интересом рассматривали здание."

    "Разогнавшаяся было дрезина ехала всё медленней. Здание стояло на холме."

    "Какое-то время мы ещё работали рычагом, и дрезина неохотно проехала еще около полкилометра, подъехав совсем близко к зданию."

    "Мы облегченно вздохнули, прыгать на ходу не пришлось."

    "Дрезина какое-то время постояла, а затем тронулась в обратном направлении. Видимо, здесь был обратный уклон."

    "Алиса стала тянуть все рычаги, торчащие из пола, в надежде, что один из них окажется тормозом."

    "На одном из рычагов дрезина заметно дрогнула и как бы споткнулась. Алиса резко потянула этот рычаг вниз. Я тоже стала помогать ей, и мы вдвоем навалились всем своим весом на рычаг."


    stop music fadeout 0.5

    queue music "audio/music/z_056.mp3"


    "Раздался пронзительный визг тормозов, из под колес посыпались искры. Дрезина встала."


    scene bg laboratory2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "Мы вышли из неё, прошли пешком метров пятьдесят и остановились перед воротами."

    "Да, это были именно ворота, высотой почти с полтора этажа. Верхние окна были зарешечены. По сути, лаборатория представляла собой огромный ангар."

    "Я посмотрела вверх. До крыши было высоко, и никаких лестниц вокруг не было. Пустошь. Даже Дом на Болотах выглядел более приветливо и обитаемо."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса почесала в затылке. Похоже, её тоже одолевали сомнения. Никаких идей насчет того, как попасть внутрь, нам в голову не приходило."

    hide sp_al_056


    scene bg barrels with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Рядом с лабораторией стояли желтые бочки с нерусскими буквами. На них были нарисованы знаки. Очевидно, что содержимое бочек было опасно для здоровья, а то и жизни."

    "Рядом стояли ящики. Мы присели на один из них."


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё, приехали. Моя идея с крышей, наверное, была не лучшей."

    al "Что это за ящики? Странно, бочки ржавые, а ящики как будто только что привезены откуда-то."

    al "Смотри, даже краска не облупилась. А вот стружка. Они явно лежали где-то на складе. Причем, не так давно."

    "Алиса понюхала стружку."

    "Давай просмотрим, что внутри. Вот маркер «осторожно, стекло»."

    hide sp_al_057


    scene cg box with dissolve

    "Мы обследовали ящики. Один из них был длинный и очень вместительный."


    scene cg box2 with dissolve

    "Закрывались они как все военные ящики, на петельку с рычагом, притягивающую крышку плотно к корпусу."


    scene cg box3 with dissolve

    "Мы отомкнули все эти застежки у самого большого ящика. Внутри лежали длинные колбы и всякие стеклянные принадлежности. Очевидно, для каких-то химических лабораторных исследований."


    scene cg box2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса задумчиво вытащила одну огромную колбу и стала смотреть сквозь неё на свет."

    "Вдруг, лицо её вытянулось, она стала разглядывать что-то вдали, используя колбу как подзорную трубу."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что ты делаешь?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Смотрю. Видишь, там, в колбе, есть еще одна. Видно, ящики стояли под дождем и туда попала вода. Между колбами."

    "Они хорошо притёрты, но тем не менее, вода попала туда и получилась водяная линза. Фактически, увеличительное стекло."

    hide sp_al_055


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Дай мне тоже посмотреть!"


    scene cg lens with dissolve

    ul "Спасибо... Да, и правда видно, как в бинокль. А я свой не взяла. Думала, будем шарахаться по темным помещениям. Зачем он там."

    ul "Ой, что там? Что-то приближается."

    al "Дай, я посмотрю. Значит, мне не показалось. Вот и хозяин блиндажа. Идет как раз с той стороны, где мы видели костер, проезжая по узкоколейке."

    ul "Ну-ка, дай я посмотрю. О боже! Это же... Пионер! Нет не пионер... Но очень похож на пионера, тоже с челкой на глазах.  А с ним еще кто-то."

    ul "Похоже, это манекены. Значит, мы не всех видели. Кто-то ушел тогда от возмездия."


    scene cg box2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Быстро прячемся!"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Куда? Тут кругом одна трава..."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Выкидывай колбы вон туда, за бочки! И быстро в ящик!"

    hide sp_al_056


    "Мы выбросили всю стеклянную начинку ящика и спокойно уместились в нём вдвоем с Алисой, закрыв над собой крышку."


    scene cg box with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"



    pause (10000000000000000000000.0)


    al "Если заглянут внутрь, нам хана."


    scene cg box4 with dissolve

    "Мы пролежали около пяти минут, пока над нами не раздался такой знакомый мне голос."

    pi "Берите вот эти два ящика и несите в лабораторию."



    image an_46_07: # Анимация Алису и Ульяну несут в ящике

        "images/an/an46day/an_d46_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an46day/an_d46_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat


    scene an_46_07 with dissolve

    "Ящик закачался, и я ощутила движение. Нас несут в лабораторию! Идея Алисы, пусть и случайно, но выстрелила. У нас есть шанс сделать то, ради чего мы сюда приехали."


    pause (10000000000000000000000.0)


    "Шаги снаружи стали гулкими. Похоже, что нас внесли в большое помещение."


    scene cg box4 with dissolve

    "Вскоре покачивание прекратилось и мы ощутили толчок."

    "Неожиданно прямо рядом с ящиком раздался женской голос. Это был голос Виолы."


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    vio "Давно жду Вас. Уже два часа курю. Дрезину отослала, думала Вы приедете на ней, но ошиблась. Хотя, как мне показалось, я слышала стук колес о рельсы."


    "Алиса крепко, почти до боли, стиснула меня руками. Мы боялись шелохнуться."


    pi "Надо было кое-что забрать из старой лаборатории. Мне помогли истуканы. Но больше они не нужны."

    vio "Тише, они могут услышать. Что собираетесь с ними делать?"

    pi "Аннигилятор."

    vio "Здесь? Прямо тут?"

    pi "Да. Времени мало. Кажется, кое-кто из наших подопытных начинает кое о чем догадываться. Надо замести следы."

    pi "Убрать всё, что можно. Потом всех в ЗАЛ. Проведем пробную версию перевоплощения. Первый и третий варианты, я думаю. Всех, кто выживет, в стеклянную тару."

    vio "А что делать с теми душами в старой лаборатории? Оставим там?"

    pi "Тоже в стеклянную тару. Я заберу их с собой. Мы начнем всё с начала там, в будущем, где я буду в новом теле."

    vio "Семён?"

    pi "Да. Надеюсь, отклонений не было? Он выполнил все твои задания? Я ощутил пять контактов с пионерками через его тело. Но я уверен, что было больше."

    vio "Я не всегда давала ему таблетки. В случае с собой, например, или с Ольгой и Майей. Маргарита и Майя не в теме. Если вы помните, у нас была договоренность."

    pi "Понятно. Я помню, Марго. Шестой контакт. Я не возражаю против Вашей самостоятельности. Имеете право. Мы это оговаривали."

    pi "Ольгу я оставляю. Она ничего не знает и не в курсе эксперимента."

    pi "Мы использовали её втёмную. Бедная овечка. Надеюсь, она найдет своё счастье в этой советской действительности. Не так ли?"

    pi "Майю я заберу с собой, а Марго — аннигилировать."


    ul "(Шёпотом) \nПионер... Вот гад. А прикидывался хорошим. Эх я, простота. Кто такая Марго?"

    al "(Шёпотом) \nМаргарита Павловна."


    pi "Кстати, как там Мари? Она тоже уйдет с нами."

    vio "Она исчезла. Последний раз мой осведомитель видел её в Доме на Болотах. Девчонка свихнулась на магии."

    vio "И кажется, она запала на Вашего клона. Вы просили не вмешиваться, и я не вмешивалась."

    pi "Бедная девочка, она очень талантлива. Мне будет её не хватать там, в будущем. Тем более, она меня... \n(осекся)"

    pi "Так любит моего... э-э-э... клона. Но оставлять её нельзя, как Вы понимаете."

    vio "Вот именно. Любит Вашего клона, а не Вас."

    pi "Не вижу разницы."

    vio "Аннигилировать?"

    pi "Я этого не говорил."

    vio "Но подумали."

    pi "Оставляю это на Ваше усмотрение. Найдите её непременно."

    vio "Что с кошкой?"

    pi "Она не выходит за пределы ЗОНЫ, она кодирована. Так что пусть живет тут..."

    pi "Меня больше беспокоит эта милая рыжая девочка Ульяна. Очевидно, она и её подруга — сталкеры. Их бы я оставил в этом времени. Но боюсь, что они не будут молчать."

    vio "Возьмёте с собой?"

    pi "Да, консервация, в колбы, как и всех остальных."

    pi "Найду для неё лучшую жизнь. Я как-то проникся к ней почти что отцовской любовью. Всегда должно быть что-то светлое, даже в нашей, такой жесткой, жизни."

    vio "От девчонки одни проблемы. Но Вам виднее. Идут Ваши помощники."


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    pi "Пусть сядут на ящик напротив Аннигилятора. Надеюсь, Вы избавите меня от необходимости видеть это."

    vio "Разумеется. Но в прошлый раз получилось наслоение. Они могут просто попасть во временную петлю, а не аннигилироваться."

    pi "Пусть. Был же библейский дождь из лягушек. Теперь будет дождь из манекенов. Вот только время неизвестно. Но постарайтесь, чтобы получилось с первого раза."

    pi "Этот хлам тут не нужен. Они ведь фактически бессмертны. Не стоит засорять экологию будущего отходами нашего времени."

    vio "Когда планируете переход?"

    pi "Завтра мы делаем тесты. Слияние послезавтра. Подготовьте тело юноши."

    vio "Хорошо, Владимир Геннадьевич."


    "Послышались удаляющиеся шаги. Затем топот многих ног. На ящик кто-то сел."


    vio "Как хорошо, что мы все сегодня вместе собрались, господа. Скоро, как мы и обещали, наступит эра манекенов. Вы готовы?"

    manneqs "(Нестройным хором) \nД-а-а..."

    vio "Включаю наш КОЛЛАЙДЕР. Все смотрим вот на этот малиновый огонек у меня в руке."


    stop music fadeout 0.5

    queue music "audio/music/z_048.mp3"


    "Мы с Алисой почувствовали, как началась сильная вибрация. Ящик трясло."


    stop music fadeout 0.5

    queue music "audio/music/z_151.mp3"


    "Затем возник сильный свист и оглушительный шум. Я почувствовала себя как в тот раз, когда я ехала и уснула в 410-м автобусе."


    stop music


    play music "audio/music/z_047_2.mp3" noloop


    image an_46_08: # Анимация вспышка перед аннигиляцией

        "images/an/an46day/an_d46_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.1


        #repeat


    scene an_46_08 with dissolve


    pause (10000000000000000000000.0)


    image an_46_09: # Анимация аннигиляция

        "images/an/an46day/an_d46_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_51.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_51.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.1


        #repeat


    scene an_46_09 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


    "Был ЗВУК… Меня как будто втянуло в какую-то трубу и стало вращать. Было ощущение падения, и оно не заканчивалось. И это было страшно."

    "Но вдруг, я почувствовала, что не одна. Что кто-то сжимает мою руку. Это была Алиса. Похоже, что с ней происходило то же самое."

    "Мы летели куда-то в бездну, словно став частью этой вибрации. Тела как будто не было. Мне даже показалось, что я сама и Алиса, превратились в этот странный звук."


    stop music


    play music "audio/music/z_1008.mp3" noloop


    scene cg box4 with dissolve

    "Вдруг все кончилось. Кружение прекратилось. Стихли шаги уходящей Виолы."


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Ощупав пространство вокруг себя, я наткнулась на руку Алисы. Кажется, она была без сознания."


    scene cg ash_piles with dissolve

    "Я спиной приподняла крышку и огляделась. В щель между крышкой и ящиком были видны дымящиеся останки манекенов. Точнее, это были даже не останки, а кучки пепла."


    pause (10000000000000000000000.0)


    "Что спасло нас от Аннигилятора, оставалось загадкой. Я потрогала стенки ящика. Изнутри они были выложены каким-то серым металлом. Листы металла тянулись вдоль всего ящика. Свинец?"

    "Но зачем ящик со склянками оправлять в свинцовую рубашку? Если только это не колбы для тех самых душ, которыми нам предстояло стать."

    "Впрочем, сейчас это было уже неважно. Свинец спас нас от превращения в пепел. Это было главным."


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Я пошлёпала Алису по щекам. Она затрясла головой и стала хвататься за стенки ящика, как будто её болтало на лодке в бушующем море. Затем её стошнило."

    al "Извини, Улька... Я что-то совсем никакая. Тебя тоже укачало?"

    hide sp_al_057


    show sp_ul_020:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Не то слово."

    hide sp_ul_020


    "Мы встали на ноги, но не могли пройти и пары шагов. Нас шатало из стороны в сторону, и мы снова опустились на пол."

    "Лежа на нём, мы пытались унять дрожь в коленках и восстановить ощущение реальности."

    "Стены продолжали мерно покачиваться. То есть, покачивало нас, даже лежа. Но нам казалось, что весь этот ангар ходит ходуном."

    "Через полчаса мы смогли подняться и нормально ходить."


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


    "Сразу принялись искать выход. Огромные ворота были закрыты. Зато, в углу помещения был люк и лестница вела куда-то вниз."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Выбирать не приходиться. Пойдём вниз. Вдруг, это запасной выход?"

    hide sp_al_056


    scene cg collider_console with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_417.mp3"


    "Вибрация не стихала. Лестница вела глубоко под землю. Мы прошли четыре пролета, пока не очутились в небольшом зале с мигающими повсюду огоньками."

    "По периметру зала шел балкон с которого можно было наблюдать весь процесс. Также там был пульт."


    scene cg collider_console2 with dissolve

    "Я кинулась к нему. Но Алиса быстро охладила мой пыл."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ничего не трогай, это опасно! Мы не знаем как поведет себя МАШИНА."

    al "Возможно, есть кнопка остановки. Но она может оказаться и кнопкой самоликвидации. Я такие штуки в кино видела."

    hide sp_al_056


    scene cg collider_console3 with dissolve

    "Штуковина в центре гудела и подрагивала. Похоже, вибрация исходила именно от неё."

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё. Это и есть МАШИНА, которую мы так долго искали. Точнее, как её назвала Виола — Коллайдер."

    hide sp_al_056


    scene cg laboratory_hangar with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Мы быстро поднялись наверх."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что будем делать?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Выбираться. Во всяком случае, мы знаем, где эта штуковина находится. У Петровича есть динамит. Взорвем всё к черту, и все их планы насмарку. Без машины они никто."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Легко сказать. Сюда надо ещё будет снова попасть, а потом как-то выбраться отсюда. Я надеюсь, у тебя есть план?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "План всё тот же. Крыша."

    hide sp_al_056


    scene cg laboratory_hangar2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Я видела внутри зала лом, канат от вагонетки и лестницу, ведущую на балкон. Оттуда через маленькое окошко вниз и на дрезину."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Высоко. Хватит этого каната? И зачем нам лом?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Лом всегда пригодится. Там же решётки на окнах. Если что, попробуем отогнуть. Хватит ли верёвки? Не знаю. Идём."

    hide sp_al_056


    "Когда мы выбрались в ангар, выяснилось, что лестница вела не на балкон, а в шахту вентиляции."

    "Поднявшись, мы взяли канат и отвязали его. Он оказался недлинным, как раз в два наших роста."

    "Алиса открыла заслонку, отчего воздух из ангара с шумом начал всасываться в трубу."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Надо лезть."

    hide sp_al_056


    image an_46_10: # Анимация вентилятор

        "images/an/an46day/an_d46_53.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_54.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_55.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_56.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an46day/an_d46_57.webp" with Dissolve(0.5, alpha=True)
        pause 0.1



        repeat


    scene an_46_10 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_057.mp3"


    "Мы ползли по вентиляционной шахте и уперлись в вентилятор."


    pause (100000000000000000000000000000.0)


    "Никакого пульта у него не было. Но зато на стене мы заметили коробочку куда шли толстые, в металлической оплетке, провода."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Тут контакты. Надо оторвать или замкнуть провода и тогда мы пролезем. Иначе нас изрубит в капусту."

    hide sp_al_056


    "Она открыла коробочку и, достав платок, обмотала им кисть руки. Потом этой же рукой соединила два проводка."


    scene bg fan with dissolve


    stop music


    play music "audio/music/z_060.mp3" noloop


    "Раздался хлопок и сноп искр на секунду озарил всё вокруг. Вентилятор встал. Сразу наступила тишина."

    "Я боялась электричества. Меня уже било дома током, когда я сунула вилку в розетку в пятилетнем возрасте, отломав средние два зубца для удобства. Папа сказал потом: «Долго жить будешь»."

    "Поэтому я ужаснулась, с какой легкостью Алиса проделала этот фокус."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса смотала с руки дымящийся платок и выбросила его."

    al "Это чтобы руку не обожгло дугой разряда."

    "Как же Алиса много знает!"

    scene bg fan2 with dissolve


    stop music


    queue music "audio/music/z_059.mp3" noloop


    "Мы отогнули решетку ломиком, взятым в зале, пролезли между лопастей и вышли на крышу."


    scene bg lab_roof with dissolve


    stop music fadeout 0.5


    play music "audio/music/z_171.mp3"


    "Было высоко. Но как ни странно, на крыше оказалась пожарная лестница, и нам не пришлось ломать ноги."


    pause (100000000000000000000000000000.0)


    "Лестница раскладывалась вперед и вниз. С земли дотянуться до нее было невозможно. Это была большая удача."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Когда мы разложим лестницу, сможем потом попасть в зал с машиной через крышу без проблем."

    hide sp_al_055


    "Мы спустились на нижний пролет, привязали к нему веревку и спустились на землю."


    scene cg view2 with dissolve

    "Мы бежали по насыпи, надеясь, что наша дрезина всё ещё там. Но её не было. Похоже, Виола укатила на ней в лагерь."


    pause (10000000000000000000000.0)


    "Мы прошли по насыпи несколько километров. Хотелось пить и есть. Наконец вдали мы увидели маленькое яркое пятно."


    scene cg view with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Это флаг лагеря. За лесом уже лагерь. Все-таки мы дошли."


    scene cg view2 with dissolve



    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day47

return