label day37:

    $ style.say_window = style.window

    $ days = 37


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene cg longboat_repaired with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_477.mp3"


    "Баркас был готов. Как сказал Семён, которого все негласно считали за капитана, «Нужно провести ходовые испытания»."

    "И вот, рано утром, ещё до подъёма, команда нашего «Смелого» (так мы назвали баркас) выгрузилась на острове, чтобы сделать пробное плавание."

    "Пришлось немного повозиться, чтобы столкнуть его в воду. Но всё же нам это удалось. И он, как говорят в таких случаях, «закачался на волнах». А мы крикнули «УРА!»."

    "У нас была мачта и парус, пошитый Леной в страшной тайне ото всех посторонних."


    scene cg longboat_first_ride with dissolve

    "Парус поставить не удалось, были какие-то нарушения в конструкции. И мы на веслах отвели баркас на тот самый берег, где мы с Алисой бегали голышом."

    "Там была небольшая бухточка. А главное, туда никто бы не попал, так как пришлось бы долго идти по берегу реки со стороны старого лагеря. Мы назвали это место «Якорная стоянка»."

    "Потом мы на лодке быстро вернулись назад в «Совёнок» и даже успели на утреннюю перекличку."


    scene bg camp_artifacts with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Только ОД подозрительно просмотрела на нас и спросила:"

    od "А что это вы все такие взмыленные? Ленина?"

    hide sp_od_022


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Мы, Ольга Дмитриевна, бегаем на реку с утра, закаляемся и тренируемся. Потом на турнике подтягиваемся. У нас программа. Ну и на спор подтягивались."

    hide sp_ul_013


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Ну, если на спор. Тогда ладно. А сколько раз ты подтянулась, Ленина?"

    hide sp_od_024


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Семь раз. Я, конечно, могу и больше."

    hide sp_ul_013


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Верю, верю."

    hide sp_od_024

    "И на этом от нас отстали."


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "После обеда МП вызвала ОД, Виолу, Майю, Любовь Никаноровну, физрука, всех вожатых и даже Петровича на СОВЕЩАНИЕ."

    "Мероприятие было секретное и закрытое. Они заперлись в кабинете у директрисы и долго совещались."

    "Как я позже узнала, речь шла об аномалии, которая не позволяла никому покинуть лагерь, а также, попасть в него извне."


    scene cg medic_journal with dissolve

    "А я воспользовалась ситуацией и заглянула в случайно незапертый медпункт. На столе лежал журнал, который Виола в спешке не успела спрятать в ящик стола."


    pause (10000000000000000000000.0)


    "Это был журнал за 1944 год. Очевидно, Женя принесла его Виоле из архива."


    scene bg pool_big_catfish_morning with dissolve

    "Из архивного журнала стало ясно, что на дне омута кроется какая-то страшная тайна, связанная с лабораторией. Я тут же побежала и рассказала о своей находке Алисе."


    scene cg collider with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_417.mp3"


    "Мы предположили, что руководство лаборатории, уходя после взрыва, бросило на дно реки свое секретное оборудование. А скорее, намеренно спрятало."

    "Возможно, даже сама МАШИНА, о которой говорил Пионер, находится где-нибудь там, под водонепроницаемым стеклом. И всё еще работает, как атомный реактор, который невозможно погасить полностью."


    pause (10000000000000000000000.0)


    "Нужно было проверить эту версию. Это можно было сделать только одним способом — спустившись на дно омута."


    scene bg bathyscaphe2 with dissolve

    "Придя к такому выводу мы сразу вспомнили про старый подводный колокол или как мы его назвали, БАТИСКАФ."


    scene bg bathyscaphe with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "Он был привязан к понтону и служил местом экскурсий. Иногда его неглубоко опускали для «экскурсий» под воду. Для этого на понтоне была установлена ручная лебёдка."

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Что, если мы отгоним понтон к Омуту и там закрепим? А потом спустимся в батискафе на дно и всё проверим?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я думаю, это очень рискованно. А вдруг, мы не удержим понтон, и его снесёт вниз на пороги?"

    ul "Или, что ещё хуже, его оторвет от цепи, когда мы будем спускаться на батискафе вниз?"

    ul "Или оторвется канат, за который держаться батискаф? Или заест лебедка, когда его надо будет вытаскивать наверх?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "В батискафе тоже есть лебедка. На случай, если сверху никто не крутит ручку. А ещё есть тросик, который опускается на дно с той же ручной лебедки."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но она же ржавая. Мы её, конечно, смазали, но кто её поверял?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я проверяла. И никто не мешает нам сделать это ещё раз перед операцией."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну что же, тогда, давай попробуем. Только понтон надо угнать ночью, а вернуться ещё затемно. Как будем возвращаться?"

    hide sp_ul_021


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Просто. Помнишь, как с той лодкой? Привяжем его на лебедку за канат и будем отпускать понемногу, когда пойдём вниз по течению."

    al "А возвращаясь против течения, будем наматывать. Только надо вдвоем изо всех сил крутить, иначе нам хана."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Это ещё не самое страшное. Самое страшное, если оборвётся канат. Поэтому надо ещё усилить якорем, когда будем на месте."

    ul "У понтона есть два якоря. Сегодня же всё обследуем, провернём и смажем. Я попробую вытащить один якорь, посмотрю, как он тянется."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я предлагаю взять с собой Тузика. Мы его сначала опустим. Как в космос запускали Белку и Стрелку."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "ТОЧНО! Только нам понадобятся фонарики. И не один."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Это уже мелочи."

    hide sp_al_055


    scene bg bathyscaphe6 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "И мы отправились проверять понтон. Лебёдка исправно вращалась, все канаты, трос и цепи были на месте."

    "Мы перетащили в батискаф всё снаряжение и ждали когда в лагере наступит тишина."


    scene bg square with dissolve

    "Наконец, когда лагерь угомонился и стало тихо, мы отвязали Тузика, не понимающего, зачем его зовут с собой в такое позднее время, но соблазнившегося котлеткой."

    "В ожидании второй подачки, он бодро семенил за нами на пристань."

    "Мы, как всегда, улизнули из лагеря через запасной вход, который между собой называли ЛАЗЕЙКОЙ."


    scene bg bathyscaphe5 with dissolve

    "От реки веяло прохладой."

    "Было тихо, только привязанные лодки постукивали бортами друг о друга, едва слышно плескалась вода, да заходящее солнце освещала тускло поблескивающий иллюминатором батискаф."

    "Мы, как всегда, взяли с собой бутерброды. Мало ли что, вдруг, что-то пойдет не так? А кушать-то хочется."

    "Мы старались не думать о том, что может случиться, поэтому разговаривали нарочито весело."

    "Какое-то время ушло на то, чтобы поднять якоря, которыми понтон держался за дно."

    "Понтон потихоньку начал отходить от берега, когда мы стали разматывать канат, связывающий его с другим понтонами. Канат слегка потрескивал."


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А как мы его столкнём с понтона?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Зачем? Там же колодец в понтоне, через него плавно опустим. Ты как не местная. Переволновалась что ли?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А, точно. Забыла."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "На стремнине нас подхватит, напряжение в канате усилится. Проверим, сможем ли мы подтянуться назад. Если нет, то остановим всю эту технику и ждем помощи."

    al "Если что, скажем что понтон отвязался, и мы не в курсе, как он это сделал. Всё равно, кроме физрука и Петровича никто не знает системы крепления понтона."

    al "Физрук на больничном, а Петрович, надеюсь, нас не сдаст."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Думаешь, он догадается?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Сто процентов. Он же не дурак. Поймет, что мы куда-то намылились. Вот почему надо вернуться не позже утра."

    hide sp_al_055


    scene cg pontoon with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_126.mp3"


    "Понтон в лучах уходящего солнца величественно двигался по водной глади."

    "Тузик, поняв, что его обманули, с тоской смотрел на удаляющийся берег. Он все ещё помахивал хвостом, но уже довольно вяло."

    "Он с надеждой оглядывался на нас, и было ясно, что скоро начнет лаять и скулить. Алиса вынула вторую котлету."

    al "А что тут у нас для собачки?"
   
    "Алиса показала котлету Тузику. Сомнения пса сразу исчезли. Его вкусно кормят, и вообще, разве это не весело, плавать на понтоне?"

    "Бедняга ещё не знал, что ему придется опускаться в бездну. Сначала одному, а потом с нами."


    scene cg pontoon2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "Вскоре канат натянулся. Это означало, что мы на середине реки и течение подхватило понтон."


    scene bg pool_big_catfish_morning with dissolve

    "Солнце спряталось за лесом, и все вокруг из тёпло-оранжевого стало холодно-голубым. Через полчаса показался омут."

    "Хорошо, что мы привязали к понтону лодку. Нужно было закрепить один конец каната на дереве на берегу и подтянуть понтон, уведя его от стремнины."

    "Тогда он окажется как раз в центре омута. Там тоже было течение, но из-за глубины омута оно было небольшим на поверхности."

    "Мы остановили лебедку, и у кормы понтона сразу образовался бурун воды. Это значило, что течение тут ещё довольно приличное."

    "Сев в лодку, мы направились к тому месту, где когда-то с Петровичем ловили Большого Сома."

    "Большой моток каната разматывался и я подумал: «А что, если нам не хватит длины? Вот будет номер»."

    "Однако каната хватило. Мы привязали его на берегу к большому дереву, растущему у самой кромки воды."

    "Взошла луна и осветила всё вокруг, поэтому фонарики нам не понадобились."


    scene cg pontoon2 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Полнолуние, однако."

    al "Теперь нам осталось подтянуть понтон ближе к берегу. Это будет непросто. Нам надо ослабить канат, держащий нас за пристань и натянуть тот, что держит нас за дерево."

    hide sp_al_055


    "Мы долго возились, но наконец нам удалась эта операция. Час потребовался на то, что бы подвести понтон к середине омута и бросить якорь."

    "Мы с Алисой сильно устали. А сытый Тузик спокойно лежал, положив голову на лапы, как будто и не участвовал в приключении века."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Надо передохнуть, а потом начнем спуск Тузика. Опустим до дна, потом поднимем и посмотрим, не проникла ли в батискаф вода."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А Тузик, не утонет, если вдруг проникнет?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Нет, не утонет. Люк, куда уходит воздух расположен ниже, а не в крыше батискафа. Поэтому под куполом всегда будет воздушный мешок."

    al "Чтобы Тузик всплыл под купол, мы наденем на него один из наших спасательных жилетов. И ещё посадим его на спасательный круг."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А может, просто опустим без Тузика?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Можно и без. Но тогда какой же это будет эксперимент, без живого акванавта? Белка и Стрелка были первыми в космосе, а Тузик будет первым исследователем глубин."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот это да! Мы будем единственными пионерами, кто проведет эксперимент с животным на глубоководное погружение!"

    hide sp_ul_021


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Только надо быть осторожными. Сначала мы открываем входной люк и только после того как его плотно «задраим», открываем люк в полу."

    al "Если вода начнет набираться, то надо подняв батискаф. Сначала закрепить его к понтону, причем жестко, а только потом открывать."

    al "Но, думаю, до этого не дойдет. Вода будет набираться медленно, и мы это увидим по пузырькам воздуха, поднимающимся со дна."

    al "Мы поднимем батискаф быстрее, чем он наберёт воды. И, кстати, ты забыла про грузики."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но Тузик не сможет сбросить грузики. У него же лапки..."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Тузик нет, а мы сбросим. Но потом, если понадобится быстро всплыть уже нам. Но это, так сказать, в случае аварии."

    hide sp_al_055


    scene cg bathyscaphe_tuz with dissolve


    "Мы проверили хорошо ли батискаф держится за понтон и запустили внутрь Тузика, надев на него спасательный жилет. Туда же мы положили и спасательный круг."

    "Пес не почуял подвоха и поэтому не сопротивлялся. Он думал, что мы сядем в батискаф вместе. Но вот люк захлопнулся."

    "Внутри задался скулеж, а потом лай обескураженного животного."


    stop music fadeout 0.5

    queue music "audio/music/z_207.mp3"


    "Лебедка закрутилась и батискаф пошел вниз."

    "Раньше мы играли возле батискафа и когда Тараса Юрьевича не было рядом, десятки раз опускали и поднимали его. Поэтому всё прошло на удивление быстро."


    scene cg pontoon3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Через какое-то время мы увидели, что канат, держащий батискаф, ослаб."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё, он на дне. Подождем немного. Посмотрим, есть ли пузырьки от воздуха."

    hide sp_al_056


    scene cg bathyscaphe_tuz with dissolve

    "Мы стали ждать, вглядываясь в воду, Алиса даже надела маску и погрузила в воду голову."

    "А я держала её за бедра, боялась, что она или свалиться в воду, или кто-нибудь страшный снизу схватит и утащит её."


    scene cg pontoon3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Что там?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Вижу свет от иллюминатора, от нашего фонарика внутри. Но он далеко. Все-таки тут огромная глубина."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А Тузика видишь?"

    hide sp_ul_019


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, машет тебе лапой."

    hide sp_al_037

    "Мы обе засмеялись, представив, как Тузик стоит у иллюминатора и отдает нам пионерский салют."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё, хватит. А то Тузик там с ума сойдет, в одиночестве. Воздух не поднимается, значит всё в порядке."

    al "Я только думаю, как пойдёт подъём батискафа. Мы проверяли внутреннюю лебедку, когда крутили её вхолостую, а тут же будет нагрузка. Хватит ли нам сил?"

    al "Одно дело вдвоём большой лебедкой поднимать Тузика, другое дело малой лебедкой нас обеих."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А я не пойму до сих пор, как эта штука работает, чтобы внутрь не проникла вода."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Через систему шестерёнок. Валик с канатом находится не внутри батискафа а снаружи, и соединен с ручкой системой шестерёнок."

    al "Там нет зазора для воды. Ну или почти нет. Вода капает конечно, потихоньку, особенно на глубине. Главное, чтобы прокладки в муфте выдержали."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Откуда ты столько знаешь?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я у Петровича про все агрегаты расспросила. Он мне очень подробно всё рассказал и показал. Старик любит, когда с ним советуются. Готов часами болтать."

    hide sp_al_056


    scene cg bathyscaphe_tuz with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1016.mp3"


    "Подъем Тузика прошёл без происшествий, и мы негромко закричали «УРА!» В иллюминаторе мы увидели радостно улыбающуюся собачью морду. Кажется, животное радовалось больше нас."


    scene cg pontoon2 with dissolve

    "Затем мы перевели трос, держащий батискаф, на внутреннюю лебедку. Батискаф немного осел, но уровень воды был гораздо ниже входного люка. Это внушало оптимизм."

    "У него была, как сказала Алиса, «почти нулевая плавучесть». Нулевая, это когда он стоит в воде ровно, как подводная лодка, ни в верх, ни вниз."

    "Сложно удержать эту нулевую плавучесть. Так говорил Петрович. На настоящих подводных лодках для этого есть целая система прокачки воздуха и заполнения цистерн."

    "Но у нас всё проще. Грузики и трос."

    "Я подумала, что наверное, если бы не захотела стать журналистом, то стала бы подводником. Как знаменитый Жак Ив Кусто. Есть такой исследователь морей и океанов."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну, как говорила моя бабушка, с Богом."

    hide sp_al_056

    "Мы скормили Тузику еще один бутерброд, чтобы он, занятый едой, не помышлял о выходе из батискафа и залезли туда сами. Люк закрылся."

    scene cg bathyscaphe with dissolve

    "Алиса закрутила колесо, которое прижимало люк к батискафу. Я начала потихоньку крутить ручку лебедки. Все оказалось достаточно просто. Пока так казалось, во всяком случае."

    "Постепенно свет луны в иллюминаторе исчез и стало темно. Мы включили свои фонарики."

    "Тузик доел бутерброд и прилег."


    scene bg bathyscaphe7 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Надо открыть нижний люк, пока мы еще не глубоко. Посмотрим, не просачивается ли вода, внутрь."

    hide sp_al_056


    "Вместе мы не без труда открыли нижний люк и увидели воду. Алиса направила в темноту воды свой фонарик."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Видно дно?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Нет, до дна еще метров двадцать. Фонарик не добивает."

    hide sp_al_056


    "Алиса снова одела маску и окунула голову в воду, продолжая светить. Потом подняла голову, и сняв маску, закрыла нижний люк и затянула винт."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё, опускаемся."

    hide sp_al_056


    stop music fadeout 0.5

    queue music "audio/music/z_207.mp3"


    "Я затарахтела лебедкой и батискаф пошел вниз."


    stop music fadeout 0.5

    queue music "audio/music/z_1012.mp3"


    "Мое сердце сильно забилось."


    stop music fadeout 0.5

    queue music "audio/music/z_1016.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "СТОП! Давай проверим подъем, пока не поздно. И вот ещё. Тузика надо оставить на понтоне."

    al "Конечно, с ним веселее. Но если что-то случиться, он хотя бы своим лаем привлечет внимание. Да и жалко псину будет, если начнем тонуть."

    al "Ему с такой глубины не выплыть. Кстати, хорошо что мы взяли спасательные жилеты."

    hide sp_al_056


    scene cg bathyscaphe with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_207.mp3"


    "Я крутанула ручку назад. Она пошла тяжело и Алисе пришлось мне помочь."


    scene cg pontoon2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1016.mp3"


    "Мы поднялись и открыли люк."

    "Тузик выскочил, постоянно оглядываясь, как бы говоря: «А вы что же? Так и будете сидеть в этой железной будке или побежим на волю, ближе к солнцу и харчам?»"

    hide sp_tuz_001


    stop music fadeout 0.5

    queue music "audio/music/z_126.mp3"


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Прощай, животина."

    "Алиса захлопнула люк и закрутила его штурвал до конца."


    scene cg bathyscaphe with dissolve  


    stop music fadeout 0.5

    queue music "audio/music/z_207.mp3"


    "Мы снова начали спуск. Я крутила ручку легко, но не торопясь. Как-то не хотелось с разгона удариться о дно."


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "Внизу течение было сильней, и канат заметно натянулся. Его потрескивание держало нас в напряжении, ощущался холодок и предательская слабость в ногах. Было по-настоящему страшно."


    scene bg bathyscaphe7 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса смотрела в иллюминатор и её губы шевелились. Она считала."


    scene cg bathyscaphe with dissolve

    "Наконец, мы почувствовали толчок. Это наш батискаф достиг дна омута."


    scene bg bathyscaphe7

    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я отрапортовала:"

    ul "Батискаф «Бобёр один» достиг заданной точки! \n(название я украла из своего любимого мультика)"

    ul "Доложил помощник капитана, Ульяна Ленина!"

    hide sp_ul_023


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса посмотрела на меня и нахмурилась."

    al "Всё это замечательно, но тут не двадцать, а больше тридцати метров. Я посчитала скорость спуска и помножила её на время."

    al "Мы ошиблись. Так что давление тут, будь здоров. В случае аварии, выныривать будем в экстремальных условиях."

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А какая скорость подъема у человека?"

    hide sp_ul_019


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну, полметра-метр в секунду. Это в лучшем случае."

    al "Запаса воздуха для нормального дыхания тут хватит максимум на 20-30 минут. Потом начнется отравление выдыхаемым углекислым газом."

    al "Если посчитать скорость подъема в жилетах, то получается, что мы будем находиться без воздуха секунд сорок. Или вроде того. Но, это, если идеально."

    al "Нужно будет, попав в воду, обязательно продуть уши, зажав нос пальцами. Иначе давление сразу сдавит барабанные перепонки. Кровь из ушей, и слуху хана."

    hide sp_al_057


    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Какой ужас."

    hide sp_ul_033


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ладно, не будем думать о плохом. Давай-ка осмотримся. Мы, вроде, стоим твердо. Дно тоже, вроде, ровное. Теперь нужно открыть очень осторожно нижний люк."

    hide sp_al_056


    "Мы взялись за ручку и начали крутить. Вскоре мы услышали какое-то шипение"

    "Затем люк открылся. Под нами, в круглом проеме, была вода. Она стала подниматься вверх, но не дойдя до края люка, остановилась."


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Так, вода давлением уплотнила воздух в батискафе."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, дышать стало тяжелее, как будто. А может, мне просто кажется."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Посмотри, не капает ли из-под дверного люка."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет, сухо."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Отлично."


    scene cg bathyscaphe with dissolve

    "Алиса надела маску, взяла фонарик и посветила в воду."


    ul "Ну, что там?"

    al "Ничего. Дно гладкое, есть ракушки и ещё водоросли, немного. Песочек."

    al "Подожди-ка... Что-то черное. Но не камень. Вот черт, у самого края железного обода. И глубоко, рукой не достать."

    al "Держи меня, а лучше привяжи вот этой веревкой... Спасибо. Так я смогу опуститься немного вниз. Держи крепко. Свети тоже, своим фонарем, у меня руки будут заняты."

    al "Так, есть... Захватила. Тащи меня!"

    ul "Тащу. Ну, что там?"


    scene bg bathyscaphe7 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса выбралась из люка. Сняла маску и протянула мне руку."

    "В её ладони лежало что-то темное. Я взяла и удивилась, насколько тяжелым был этот предмет."


    scene cg gold_bar with dissolve

    "По форме он напоминал брусок, только был весь облеплен каким-то илом. Мы склонились над предметом."

    "Алиса протёрла его своей мокрой майкой, и мы увидели тускло блеснувшие буквы: «П. ОВЧИННИКОВЪ 1884 год»"


    pause (10000000000000000000000.0)


    scene bg bathyscaphe7 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса озадаченно посмотрела на меня."

    al "Все это конечно очень интересно... Но никакой машины, ни в иллюминаторе, ни на дне, я не увидела. Похоже, ее тут нет. Ладно... Что ты думаешь по поводу этой штуки?"


    scene cg gold_bar with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


    "Мы долго разглядывали брусочек."

    "Из документов, которые нашлись в архивах, мы знали что фамилия, вытесненная на бруске, была фамилией местного золотопромышленника, который держал Прииск еще в царские времена."


    scene bg bathyscaphe7 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это золото."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Возможно, отметка в журнале Виолы, это указание не на остатки приборов лаборатории, а на золото Прииска?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я думаю, что лабораторию не уничтожили, а перенесли. Ещё думаю, что она продолжает работать."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно. Иначе откуда взялись все эти странности в лагере? И кто, по-твоему, может проводить опыты в лаборатории сегодня?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Не знаю. Но судя по утопленнице, остатки экспериментов уничтожаются. Так сказать, «концы в воду»."

    hide sp_al_056


    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Думаешь, это пионерка из прошлого заезда? Боже... это же ужас!"

    hide sp_ul_033


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я вот что думаю. У нас осталось мало времени. Воздух в батискафе постепенно становиться непригодным для дыхания. А у нас нет кислородного баллона."

    al "Так что, еще минут пятнадцать и наверх. Я посмотрю еще на дне, может быть, что-то найду."

    hide sp_al_056


    stop music fadeout 0.5

    queue music "audio/music/z_208.mp3" noloop


    "Алиса нырнула снова."


    scene cg bathyscaphe with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "На этот раз я только светила ей двумя фонариками."

    "Алиса сама погрузилась в воду, и я видела, как она плавает внутри колокола, разглядывая что-то на дне."

    "Наконец, она вынырнула. В руке у нее, был такой же брусок, как и в первый раз. Алиса выбралась из проема. Она дрожала."


    scene bg bathyscaphe7 with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "На, держи. Похоже, такой же. Там больше ничего нет, всё обыскала. Если и есть, то дальше, за границей батискафа. Тут сильное течение. И холод адский. А еще очень сильно давит на уши."

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Дай, я тебя разотру своей майкой. Черт, мы даже полотенце не захватили."

    hide sp_ul_019


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Порывшись в рюкзаке и стуча зубами) \nЗато, я захватила ЭТО."

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что это?"

    hide sp_ul_019


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Помнишь, Петрович давал Толику, когда мы ходили на Вторую охоту, на Сома?"

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Архиповка?"

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да. Я выпросила у Петровича, и он налил мне во флакончик. Сказал, только как наружное средство, растираться от простуды». Думаю, сейчас самое время."

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Давай, тебя первую."

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, снаружи и немного внутрь. Два глоточка приму, она очень крепкая. А потом тебя разотру, тоже вся синяя сидишь."

    hide sp_al_057


    "Я стала растирать Алису. В это время мы услышали странный звук. Какой-то «ДЗЫНЬ!» Как будто, что-то ударило про крышке батискафа."

    "Потом батискаф качнуло. Он как будто сдвинулся с места. Наступила тишина. Потом раздался скрип."


    stop music fadeout 0.5

    queue music "audio/music/z_205.mp3"


    "Батискаф полз по дну и края колокола скребли песок . Звук усиливался самой конструкцией аппарата и оттого был очень громким."


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё, хана… Это канат лопнул. Быстро покрути ручку лебедки!"

    hide sp_al_057


    stop music fadeout 0.5

    queue music "audio/music/z_204.mp3"


    show sp_ul_053:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Не чувствую сопротивления, просто вращается вхолостую."

    hide sp_ul_053


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А ну, дай я... Да, действительно. Значит, он оборвался. Это плохо."

    hide sp_al_057


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_ul_053:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нас тащит. Мы ползем по дну..."

    hide sp_ul_053


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, знаю. Не мешай, я думаю."

    al "Через верхний люк нам не выбраться, его прижимает давлением, а нижний открыт. Но пока дно гладкое, нас просто будет тащить, пока мы во что-то не упремся."

    al "Мы остановимся, и там не будет щели, чтобы выбраться. Потом река начнет постепенно забрасывать батискаф песком..."

    al "И через пару лет мы станем отмелью. Мумиями в склепе. И никто никогда нас не найдет."

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ты хотела сказать, мы станем не отмелью, а МЕЛЬЮ?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну да... Кстати, та мель, ну, на которую нас вынесло. Она же прямо за Омутом, между ним и водоворотом."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Значит, она... Ты считаешь, она образовалась искусственно?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Может быть, может быть... Если что-то тяжелое сначала тащило течением, а потом засыпало песком."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А это «что-то» сейчас на МЕЛИ. На которую наведывается Петрович с лопатой. Значит, это может быть..."

    hide sp_ul_019


    scene bg bathyscaphe7 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    al_ul "(В один голос) \nЗОЛОТО!"


    scene bg bathyscaphe7 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Правильно! Помнишь, Петрович рассказывал, что перед революцией, золото несколько лет подряд не вывозилось!"

    al "А потом, когда начались события революции, то целый караван из подвод ехал в сторону Прииска и их завернули красноармейцы? Значит, золота тут очень много, и его так и не вывезли!"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да. И Инженер знал об этом. Не даром, он приезжал сюда. И недаром, в желудке у Сома нашли его значок."

    ul "Он нырял за золотом, которое сам же когда-то утопил на дне омута, и потом его, этого инженера, схрумкал Сом!"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Странно. Не таскал же он этот значок столько лет с собой просто так. Ну разве что, как талисман, память. А может, боялся что его не узнают и хотел предъявить... Кому-то. Но кому?"

    hide sp_al_056


    scene bg bathyscaphe7 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    al_ul "(В один голос) \nПЕТРОВИЧУ!"


    scene bg bathyscaphe7 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да! Потому что он единственный из работавших на прииске, оставался в живых. А возможно, единственный был посвящен в тайну спрятанного клада!"

    ul "Точно, инженеру был нужен помощник. Ведь столько лет прошло. Одному ему столько золота было не достать и не вывезти."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Думаешь, Петрович утопил Инженера? А сам понемногу копает золотишко на мели?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно! Вот для чего ему там нужна была лопата!"

    ul "Но я не думаю, что он утопил инженера. Он мог, зная, что клада уже нет на дне Омута, просто сделать вид, что не узнал его, и сказать: «Я Вас не знаю», и всё."

    ul "А тот от безысходности пошел нырять в омут. А там Чудовище! Вспомни, откуда вытащили ржавый батискаф."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну, фактически из Омута, если верить Петровичу."

    hide sp_al_056


    scene cg bathyscaphe with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    "Так мы беседовали, пока течение тащило наш батискаф по дну. Потом батискаф стал приподниматься и вращаться. Сначала медленно, потом все быстрее."


    scene bg bathyscaphe7 with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "ВОДОВОРОТ! Держись!"

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Он не поднимет наш колокол, тот слишком тяжелый!"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Поднимает, как видишь, но ненамного. Пока он его держит силой вращения, нужно ему помочь. Это восходящая струя. Она уже как бы за Водоворотом."

    al "Если мы раскачаем колокол, то опрокинем его с помощью водоворота, и тогда, с выходящим воздухом и воспользовавшись ВОСХОДЯЩЕЙ СТРУЕЙ, вынырнем наружу!"

    al "Хватай рюкзак с находками, пристегни его крепко к себе, потому что тебе понадобятся свободные руки."

    hide sp_al_056


    scene cg bathyscaphe with dissolve

    "И мы, как и сказала Алиса, взобравшись на скамеечку, стали дружно, по её команде, раскачивать верхнюю часть колокола."

    "Он все больше раскачивался и в какой-то момент стал заваливаться набок."


    scene bg bathyscaphe7 with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Набирай воздух! Как только мы окажемся в воде, продуй уши, как я учила! Сейчас понесет!"

    hide sp_al_057


    scene cg bathyscaphe3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    "Дальше всё произошло почти мгновенно. Нас закрутило внутри переворачивающегося батискафа."


    scene cg bathyscaphe2 with dissolve

    "Алиса исчезла, выброшенная огромным пузырем воздуха. А меня, зацепившуюся лямками рюкзака за ручку лебедки, тащило дальше, вместе с перевернутым батискафом."


    scene bg bathyscaphe8 with dissolve

    "Я отчаянно пыталась освободиться, но перочинный ножик остался у Алисы, и перерезать лямки рюкзака было нечем."

    "Наконец, я перестала делать резкие движения вспомнив, что расход кислорода в организме напрямую зависит от напряжения мышц."

    "Я обреченно озиралась, пытаясь что-то разглядеть в темноте и придумать способ, чтобы не задохнуться. Но было очень темно, потому что иллюминатор оказался внизу."


    scene bg bathyscaphe9 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "Но вот, после очередного толчка, влекомый течением по дну батискаф, развернулся иллюминатором вверх, и стало немного светлее."

    "Я знала, что где-то подо мной находится лебедка, и нащупав её ногой, оттолкнулась вверх, к воздушному пузырю, оставшемуся между иллюминатором и потолком батискафа."

    "Мне это удалось. Лямки рюкзака от интенсивного ерзания немного ослабли, но всё ещё крепко держали меня. Глотнув немного воздуха из пузыря, я снова погрузилась вниз."

    "«Почему бы мне не снять рюкзак вместе со спасательным жилетом» — подумала я."

    "Я стала расстегивать жилет на груди, и вскоре он соскользнул вместе с рюкзаком, а я рванулась к спасительному голубому кругу воздуха над головой."

    "Мысль о том, что в рюкзаке  осталась находка, мелькнула и исчезла. Если меня не станет, то кому нужно это открытие?"

    "В пузыре было темно, холодно, и воздух был уже несвежим от дыхания, но всё же, это была ЖИЗНЬ."

    "В борьбе за выживание я не думала о холоде, но сейчас я почувствовала его очень остро. Он был почти невыносим."

    "Держась за край иллюминатора, я подняла руку вверх, в поисках более надежной опоры и нащупала скобу."

    "Подтянувшись, мне удалось приподняться настолько, чтобы выбраться из воды. Но это удалось сделать только наполовину. Ноги все еще были в ледяной воде."

    "Сколько я могу так продержаться? Через иллюминатор в батискаф попадал тусклый голубовато-зеленый свет с поверхности омута. Это означало, что наверху начинается утро."

    "Как там Алиса? Наверное сошла с ума от мысли, что я погибла. А может быть, её снова затянуло в водоворот и я теперь одна живая... Но надолго ли?"

    "Я стала смотреть в иллюминатор как, наверное, смотрят наружу, через узкое окошко камеры осужденные на смерть. Теперь я их понимала."

    "Чередой пробежали воспоминания обо всём, что случилось за последние дни. О родителях, о том как им «сообщат»."

    "Я заревела. И подумала: «Тут и так много воды, а я добавляю». А потом стала смеяться. Наверно, от истерики."

    "Смеялась, потому что было смешно представлять, как мои слезы заполнят воздушный пузырь, и я утону от собственных слез. И наверное, это будет очень соленая вода."

    "Тут я стала фантазировать. А что было делать?"

    "Я понимала, что не поднимусь на поверхность с двадцатиметровой глубины без жилета, который крепко держал мой рюкзак, который в свою очередь, держало что-то еще."

    "За что же он мог зацепиться? Я думала эту мысль. Я представляла, как мой трупик плывет вниз по реке или, что ещё хуже, вращается в водовороте вечно. У той утопленницы, была хотя бы могила..."

    "Но холод вернул меня к действительности. Поднимая из воды то одну, то другую ногу, я старалась растирать их свободной рукой. Хорошо, что я нашла выступ, на который оперлась."

    "Иначе, на коченеющих руках, с негнущимися от холода пальцами, я провисела бы недолго."


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Я вдруг поняла, что впадаю в какую то спячку. Возможно, от скопившегося выдыхаемого углекислого газа и еще от холода."

    "Наверное, так замерзают в снежной степи. Как в песне про ямщика."

    "Последнее, о чём я подумала, это что река протащила батискаф уже далеко, и если будут вестись поиски, то искать будут, наверное, возле понтона, а не там, где батискаф сейчас."

    "Впрочем, мне это должно было теперь быть без разницы."

    "Помню, я почти уснула, но что-то сильно стукнулось об иллюминатор снаружи. Я встрепенулась, ухватилась второй рукой за скобу и сильно прижалась к стеклу, чтобы разглядеть, что бы это могло быть."


    scene cg at_resque with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_542.mp3"


    "В тусклом свете, пробивающемся с поверхности, я увидела смотревшее на меня, сплюснутое о стекло, ЛИЦО АТСУИ."

    "Ну конечно же! Кто ещё у нас ныряет и плавает как лягушка!"


    scene bg bathyscaphe9 with dissolve

    show sp_at_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Вскоре Атсуи оказалась внутри. Мы обнялись, при этом обе погрузившись в воду. Но на этот раз меня крепко держали. Вынырнув, я спросила:"

    hide sp_at_003


    show sp_ul_053:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Алиса! Где Алиса? Она жива?"

    hide sp_ul_053


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Не беспокойся за Алису. Я выловила её ниже по течению. Она сейчас сохнет на мели. Беспокоится за тебя, рвалась снова нырять."

    ats "Но я её кое-как разубедила, сказав, что достать тебя, будет для меня парой пустяков."

    hide sp_at_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но ведь это огромная глубина! Как ты смогла?"

    hide sp_ul_019


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Потом расскажу. Ты вся синяя от холода. Давай выбираться."

    hide sp_at_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Хорошо, но как ты это себе представляешь? Я не смогу задержать дыхание так надолго."

    hide sp_ul_019


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Чепуха, сможешь. Я очень быстро тебя вытащу. Нам поможет течение. К тому же, тут уже не та глубина, что на дне омута. Вас порядком отнесло. Набирай побольше воздуха... Готова?"

    hide sp_at_001


    show sp_ul_053:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет! Там рюкзак! Он зацепился за что-то. В нём важные для нас с Алисой вещи. Но там темно, ты не увидишь."

    hide sp_ul_053


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Спокойно. Держись за скобу, пока я ныряю."

    hide sp_at_001


    "Атсуи с шумом ушла под воду и через минуту всплыла, держа в руках спасательный жилет и рюкзак."


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Надевай."

    hide sp_at_001


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Спасибо! Асечка, миленькая, ты суперменша какая-то! Ты даже не представляешь, как этот рюкзак важен для меня!"

    hide sp_ul_021


    "Атсуи помогла мне надеть жилет и рюкзак. Я прощупала сквозь ткань, бруски были на месте."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "За что он зацепился?"

    hide sp_ul_019


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Ты не поверишь, на нем лежала крышка нижнего люка. Ты одна никогда бы его не освободила."

    hide sp_at_001


    stop music fadeout 0.5

    queue music "audio/music/z_140.mp3"


    "И едва я успела набрать воздуха в легкие, как Атсуи стремительно потащила меня к нижнему люку."


    scene cg bathyscaphe3 with dissolve

    "Затем, проскользнув в него, мы начали стремительно всплывать. Она держала меня крепко за лямки рюкзака."

    "Атсуи шла как торпеда, а я трепыхалась сзади, как тряпочка."


    scene bg pbc with dissolve

    "Наконец мы вынырнули и поплыли дальше от водоворота."


    scene bg ushallow with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "На мели нас ждала взволнованная Алиса. Она подхватила меня, прижала к себе, и мы вместе упали на песок."

    hide sp_al_057

    "Атсуи рухнула рядом. Мы с Алисой дышали как рыбы выброшенные на берег. Она от волнения, а я от того, что не дышала."


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Атсуи, между тем, уже спокойно сидела и наблюдала за нами. Как будто только что ей не пришлось нырять на огромную глубину, задержав при этом дыхание на четыре минуты."

    "Ведь она не только донырнула до батискафа, но еще и обследовала его в поисках входа, а потом тащила меня наверх."

    "Я не заметила в ней признаков усталости. Как бы прочитав мои мысли, Атсуи вдруг улыбнулась и сказала:"

    ats "У вас есть книжка русского писателя-фантаста, «Человек амфибия». Не читала? Так вот, я и есть персонаж этой книги."


    scene bg ushallow2 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я тут же заметила, что тот персонаж был продуктом научных исследований."


    scene bg ushallow with dissolve

    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ats "Я тоже. Только не стоит об этом кому-то рассказывать в лагере. А то, задразнят лягушкой."

    hide sp_at_001


    "Мы приходили в себя и старались согреться, бегая по кругу и растирая друг друга. Атсуи рассказала нам о том, что в лагере заметили исчезновение понтона и батискафа."


    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Петрович, зайдя к вам в домик и никого там не застав, сразу всё понял и бросился к лодке. Но я опередила его."

    ats "Сейчас Петрович на понтоне. Он считает, что вы не могли выжить. Он знает, что канат оборвался. Но я подумала, что вас снесло течением, и отплыв ниже, стала искать."

    ats "На моё счастье, на дне рядом с батискафом лежал фонарик. Он давал слабенький отблеск, по которому я вас нашла."

    ats "Когда я почти добралась до батискафа, увидела, как снизу вверх, навстречу мне, двигается отчаянно дергающая руками и ногами Алиса. Я ухватила её и потащила вверх."

    ats "Так ей хватило дыхания. Давление было большое, она почти потеряла сознание. Ты бы тоже не выбралась сама, Улька. Так что, всё хорошо."

    ats "Вот только, Петрович там сидит на понтоне и оплакивает вас. А заодно, наверное, и меня."

    ats "Надо возвращаться. Я сплаваю к понтону и оттуда мы на лодке вернемся на мель, а вы сидите тут и ждите."


    scene bg pbc with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_182.mp3"


    "Атсуи разбежалась и нырнула. Было видно, как цепочка воздушных пузырьков, сносимых течением, вытянулась в сторону смутно виднеющегося вдали понтона."

    "Стало почти светло, и вот-вот должно было взойти солнце."


    scene bg ushallow2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Всё хорошо, их не будет еще какое-то время. А у нас есть возможность проверить нашу гипотезу про образование этой мели."


    scene bg ushallow with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, точно, надо только найти место, где Петрович спрятал лопату."

    hide sp_ul_019


    "Мы стали бродить по мели. Она была не такая уж и большая, хотя за годы река нанесла на неё много песка. Наконец, я услышала крик Алисы: «ЕСТЬ!»"

    "Алиса достала из зарослей камыша лопату и рюкзак."


    scene bg ushallow2 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Вот, смотри, он еще и рюкзак оставил, значит что-то хотел забрать."

    hide sp_al_055

    "Мы стали ходить вокруг и наткнулись на довольно большую яму. Было видно, что копали тут регулярно и не один раз."

    "Спустившись на дно ямы, мы стали сгребать осыпавшийся в неё песок, пока не услышали удар лопаты о что-то твердое. Мы опустились на колени и вдвоем, руками быстро очистили предмет."

    "Им оказался большой ящик с полуистлевшими от времени и сырости досками."

    "Оторвать их было несложно. То, что вывалилось из ящика, привело нас в восторг. Мы обнимались и исполняли дикий туземный танец."

    "Все наши догадки замечательно подтвердились. Это были такие же бруски, как и те, что нам удалось вытащить из воды."

    "Теперь было ясно, что мель образовалась искусственно. Течение тащило ящики, пока они не уперлись в возвышение на дне, возможно уже начинающуюся мель."

    "А потом их быстро заволокло песком. Сколько же там его, этого золота? Страшно даже представить."

    "Стоя на дне ямы, мы услышали голоса."


    stop music fadeout 0.5

    queue music "audio/music/z_477.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Быстро наверх! Подожди, я прикопаю ящик... Так, отлично. Надо положить лопату на место, пока Петрович с Атсуи не нашли нас."

    hide sp_al_056


    "Мы выбрались из ямы, побежали к камышам, спрятали лопату рядом с рюкзаком и как ни в чем ни бывало вышли на берег. Петрович страшно обрадовался."


    scene bg ushallow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    pe "Где вы были?! Мы вас искали, гаврики!"

    "Петрович заглядывал нам за спину, очевидно, пытаясь понять, нашли ли мы его «раскоп». Но Алиса быстро нашлась:"


    scene bg ushallow2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ходили по женским делам."


    scene bg ushallow2 with dissolve

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Петрович смутился."

    pe "Быстрее в лодку, пока в лагере не организовали большие поиски. А я постараюсь пока подтянуть понтон к берегу."

    hide sp_pe_003


    "Он сбегал в сторону, откуда мы пришли, но вернулся назад успокоенный. И мы сели в лодку."


    scene cg pontoon3 with dissolve

    "Мы быстро доплыли до понтона, высадили там Петровича."


    scene bg boat_station2 with dissolve

    "А через двадцать минут мы уже бодро шагали по причалу лодочной станции."

    show sp_od_025:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "На причале нас ждали ОД и весь отряд. По лицу Ольги Дмитриевны было ясно, что она вряд ли поверит в то, что мы просто купались в реке с утра пораньше."

    hide sp_od_025


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Косим под то, что понтон оборвался, и нас унесло течением, когда мы осматривали батискаф. Скажешь, что в прошлую экскурсию забыла там фонарик."

    al "Короче, версия такая (идея Петровича, кстати). Так что, врем дружно и складно."

    hide sp_al_056




    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day38

return