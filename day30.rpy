label day30:

    $ days = 30

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_002.mp3"


    scene cg pi_fishing_fog with dissolve

    "Я проснулась. В шалаше никого. И снова приятный запах рыбки от костра. И я выползаю на четвереньках из шалаша и ползу к костру. А глаза ещё слипаются."

    "Костер едва горит, но угли жаркие и булькает в котелке уха. Силуэт пионера с удочкой виден сквозь туман."


    pause (1000000000000000000.0)


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    "Пионер подходит, кладет удочки и садится рядом."

    pi "Все утро был туман. В туман здесь рыба плохо клюёт. Поймал пару штук, но на уху хватило. Хотя, он уже почти рассеялся. Зато они большие."

    "Порывшись в рюкзаке, Пионер достал миски."

    pi "На, накладывай, кушай. Сегодня тоже форель, ты же её любишь?"


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да, спасибо."

    ul "(Уписывает за обе щеки) \nВкусно! Я проголодалась. Не смотри."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ну почему же? Ты прекрасна со сна. Такой ребенок. Прелесть."

    pi "Что снилось?"


    scene bg hut3 with dissolve

    show sp_ul_032:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Получается, я проспала весь вчерашний вечер и ночь. Ужас. Меня же в лагере хвататься."

    hide sp_ul_032


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Хотя... Алиса что-нибудь придумает."

    ul "А мне сова снилась. Я ей вопросы задавала. Только ни черта не вышло. У меня все ответы исчезли."

    hide sp_ul_021


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Слушай, у меня к тебе дело..."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Я думал, ты соскучилась."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Пряча глаза) \nИ это тоже... Но сначала — дело."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Любую твою просьбу я выполню."


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Ковыряя палочкой в углях) \nЮля... Э-э-э, она говорит, что ты не пускаешь её в лагерь."

    ul "И что ты не хочешь, чтобы она была в нашем отряде. Но Ольга Дмитриевна не против. И Алиса, и все остальные. Юля тебя слушается и как будто боится. Без тебя она не придет к нам. Ты можешь её отпустить?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "(Посмотрев на небо и улыбнувшись) \nЯ разрешу. Всё равно, скоро дожди. Они все обнулят."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Что-что? Что обнулят?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Это я не тебе. Ладно, завтра она придет. Но хвост и уши я не смогу убрать. Даже ОН не сможет. Придется вам жить с ней так."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ничего не поняла. Кто такой ОН?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "(Наклонившись к ней, шепчет) \nГЕНДА..."


    # stop music fadeout 1.0


    # play music "audio/music/z_130.mp3"


    scene bg hut3 with dissolve

    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Какой Генда? Тот, который памятник? \n(смеется)"

    hide sp_ul_023


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я вижу, ты слишком долго жил в одиночестве. \n(сочувственно)"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Возможно... Но теперь есть ты. Все изменилось."


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ладно, я пошутила. Я тоже люблю фантазировать. А хвост и ушки, это так мило! И без них она была бы уже не Юлей. Мы привыкли и полюбили этот хвостик и ушки."

    ul "Тогда я пошла? Я тут очень долго, меня хвататься. Уже линейка прошла. Скоро построение для праздника. Будут искать. Спасибо за форель."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "На здоровье. Обычно добавляют — «расти большая». Но я так не скажу. Но, к сожалению, ты все равно вырастешь. И гораздо быстрее, чем думаешь."


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ты мня пугаешь. Говоришь загадками. Только я к тебе привыкну, начинаешь чудить. Я хотела бы вырасти быстрее. Но чудес не бывает."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Бывают. Тут все бывает."


    stop music fadeout 1.0


    play music "audio/music/z_125.mp3"


    pi "(Понизив голос) \nА Генда, это бывший начальник лагеря 410 Бурлейка. На самом деле его фамилия Гендаков."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А я думала, что начальником лагеря был профессор Новицкий..."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ты слишком много знаешь для маленькой девочки."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Мы нашли документы в упавшем самолете. Там письмо лаборанта из лаборатории Новицкому. И мы знаем, кто такая Виола."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ах вот как... Значит вы знаете."

    pi "Ну что же. Тогда добавлю только то, что Гендаков устранил профессора Новицкого. Все считают что Новицкий и Гендаков погибли при взрыве. Но это не так."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А как же... Как он сделал это? Виола помогла ему?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Нет, она была против. Вообще-то, это долгая история. Когда-нибудь расскажу."

    pi "Это страшный человек. Он поднялся по карьерной лестнице от начальника охраны до начальника лагеря, за полгода до появления тут... Немцев."

    pi "Потом прибрал все к рукам. Мне даже кажется, что немецкий десант это его рук дело. Никто во всем мире не мог знать о секретной лаборатории."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Даже ИВС?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ты и это знаешь? Да, Сталин лично курировал этот проект."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А почему Гендакова никто никогда не видел?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Его видели все. Он стоит посереди площади в лагере. Кстати, портретное сходство памятника и человека поразительно. Это он сам поставил себе памятник. У него комплекс Наполеона."

    pi "Между прочим, он имеет информаторов среди вас."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А кто они? Директриса тоже с ним?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Нет. Никто не с ним. Просто все от него зависят, у них нет выбора."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Даже у Виолы?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Она его правая рука. Но она сама по себе. Она слишком много о нем знает. И он зависит от ее знаний. Она тоже это знает. Ведет какую то свою игру..."

    pi "Я еще не разобрался, какую. В любом случае, пока что они заодно."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А ты тогда кто? Ты тоже информатор? Ты зависишь от него? Почему он не избавился от тебя?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "(Помрачнев) \nДа, я завишу. Я жив только потому, что мой отец когда-то был его другом."

    pi "А еще он привык считать меня маленьким мальчиком, которого он когда-то сажал себе на колени."

    pi "Самонадеянность. Уверенность в своем превосходстве. Он очень умный, и кажется, все просчитал."

    pi "Но он не знает, что за эти годы я изучил систему периметра и МАШИНУ. Я знаю то, чего не знает даже он."

    pi "Единственное, чего у меня нет, это ключа, останавливающего работу коллайдера. Поэтому я выжидаю."

    pi "Он носит его с собой. Всегда. Но вместе мы сможем получить этот ключ или найти способ, как-то еще остановить ее. Пока не знаю как. Не придумал."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да, я уже поняла, что есть машина которая меняет время и всякое другое еще.  А вот, расскажи еще, про шахты и прииск. И про чердак. И про бомбоубежище. И про вуду. У меня так много вопросов..."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Все. На сегодня хватит. Мне нужно будет исчезнуть на время. Кажется, ОН что-то подозревает. Он посылал за мной, но я спрятался. И тебе не стоит больше сюда приходить. Я боюсь за тебя."

    pi "Ладно, я отвезу тебя. Черт, лодка отвязалась, пока болтали!"


    stop music fadeout 1.0


    play music "audio/music/z_181.mp3"


    scene cg boat_water with dissolve

    "Пионер зашёл в воду по плечи, чтобы притянуть качающуюся на волнах лодку."


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Какой ты мокрый... \n(дотрагивается до обтягивающей тело мокрой рубашки)"

    ul "Не поцелуешь на прощанье? В щечку... Как тогда."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "А можно?"


    scene bg hut3 with dissolve

    show sp_ul_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Закрывая глаза и подставляя щеку) \nМожно."


    scene ul_pi_kiss with dissolve

    "Пионер целует ее в губы."


    pause (10000000000000000000000000.0)


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Отталкивая его) \nЧерт... Хитрец какой. Я не ожидала. Предупреждать надо."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ты против?"


    scene bg hut3 with dissolve

    show sp_ul_043:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Краснея) \nНу... Э-э-э, нет. Но в любом случае надо было спросить."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "(Улыбнувшись) \nНе обижайся, но о таком не спрашивают. У тебя мягкие губы... И пахнут клубникой."


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Дурак."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ладно, садись на корму. Я отвезу."


    scene bg hut3 with dissolve

    show sp_ul_044:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(С сердитыми видом отталкивает его руку) \nНе надо, я сама умею грести. Меня Петрович научил. И потом, ты простынешь, на тебе нитки сухой нет."


    scene cg bot_water_ul with dissolve

    ul "(Усаживается в лодке и спускает вёсла в воду) \nВот только еще, последний вопрос. Что это за люк в полу бомбоубежища, и куда он ведет?"

    ul "Я видела тебя там. Не специально... Просто мы с Алисой обследовали бомбоубежище."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "(Бледнея) \nБоже... Так вы были там? Никому не говори. Если ОН узнает, что вы ходите туда, то будет плохо. Забудьте."

    pi "А люк... Он ведет на подземную станцию. Там под землей есть старая узкоколейка. Но вам туда нельзя."



    scene cg bot_water_ul with dissolve

    ul "А куда ведет узкоколейка?"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Не спрашивай. Я и так слишком много сказал."

    "Лицо Пионера стало серьезным, скулы пришли в движение."


    scene cg bot_water_ul with dissolve

    ul "Все, не буду больше сегодня задавать вопросов. Туман совсем рассеялся, можно плыть. Спасибо. Оттолкни меня, пожалуйста."

    "Пионер отталкивает лодку."

    ul "Вот, отлично."


    stop music fadeout 1.0


    play music "audio/music/z_460.mp3"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ты уверенна, что сама доплывешь?"


    "Лодка удаляется. Ульяна что-то кричит в ответ, слышно только конец фразы:  «...а твои пахнут мятой!»"

    "Лодка исчезает за поворотом реки. Пионер долго стоит и смотрит в сторону исчезнувшей лодки."

    pi "(Бормочет) \nУдивительная... Удивительная..."





    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day31

return 




