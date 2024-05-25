label day30:

    $ style.say_window = style.window

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

    ul "Получается, я проспала весь вчерашний вечер и ночь. Ужас. Меня же в лагере хватятся."

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

    ul "Да, я уже поняла, что есть машина которая меняет время и всякое другое.  А вот, расскажи ещё про шахты и прииск. И про чердак. И про бомбоубежище. И про вуду. У меня так много вопросов..."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Про шахту? Надеюсь, вы туда не лазали?"


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Нет."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Это хорошо. Потому что там есть бункер, в котором возможно находятся те, кто исчез при взрыве. И скорее всего, поэтому он заминирован."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Петрович тоже нас пугал минами. Но все же погибли!"


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Понимаешь, почему я так думаю, в разговоре с Виолой Гендаков упоминал о каких-то развоплощенных душах, которые он собирается использовать в своем жутком проекте."

    pi "Возможно исчезли только тела."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Души? А Ленин говорил, что душ нет, потому что мир материален. А души, они же нематериальны."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Вообще-то материальны. Только это другой вид материи. Ну, не знаю, что-то вроде плазмоидов."


    scene bg hut3 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Плазмоиды? Я такого слова не знаю."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Ну, это как шаровые молнии, только слабее, как светлячки. Не знаю, как тебе объяснить. Возможно, они невидимы для глаза. Или имеют слабое свечение."

    pi "В общем, не забивай себе голову."


    scene bg hut3 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ну от чего же. Интересно же."


    scene bg pi_ul_dialog with dissolve

    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    pi "Тебя, наверное, уже хватились. Потом про всё поговорим."

    pi "На сегодня хватит. Мне нужно будет исчезнуть на время. Кажется, ОН что-то подозревает. Он посылал за мной, но я спрятался. И тебе не стоит больше сюда приходить. Я боюсь за тебя."

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

    pi "Ты уверена, что сама доплывёшь?"


    "Лодка удаляется. Ульяна что-то кричит в ответ, слышно только конец фразы:  «...а твои пахнут мятой!»"

    "Лодка исчезает за поворотом реки. Пионер долго стоит и смотрит в сторону исчезнувшей лодки."

    pi "(Бормочет) \nУдивительная... Удивительная..."


    stop music fadeout 1.0


    play music "audio/music/z_011.mp3"


    scene cg iul_coming with dissolve

    "Я добралась до лагеря без приключений, а еще через час пришла Юля. Она постучала в окно, и мы впустили ее. Видно было, что она боится, что ее увидят другие пионеры."

    "Но мы успокоили ее, сказав, что в этом секторе нет других пионеров кроме нашего отряда, и тут же позвали ребят. Вскоре отряд собрался на чердаке. Все разглядывали Юлю."


    stop music fadeout 1.0


    play music "audio/music/z_002.mp3"


    scene cg iul_all_attic with dissolve

    "Каждый норовил ее погладить и дотронуться до ушек. Мы заранее предупредили, чтобы никто не задавал нескромных вопросов, типа «Вылизываешься ли ты». Или «А ешь ли ты мышей»."

    "Но Электроник все-таки, что-то ляпнул про хвост. На него все зашикали."

    "Встал вопрос о том, где будет жить Юля. Все девочки хотели её к себе. Но мы с Алисой возмутились. Мы сказали, что первые нашли Юлю и отдавать её не собираемся. Тут все согласились."

    "Но Юля ни в какую не хотела покидать свой домик в лесу."

    "Тогда мы сказали ей: «Как хочешь, но знай, что тут есть твоё место, всегда можешь остаться»."


    scene an_d30_01 with dissolve

    "В конце концов она согласилась. Мы вытребовали у завхоза гамак для неё, потому что спать на кровати она отказалась. Хотя в лесу в ее домике у неё была кровать. Это я точно помню."

    "А мальчики принесли шкафчик и тумбочку. Но Юля, узнав, что у нас есть чердак, забралась туда и повесила гамак. Он быстро убирается, если мы захотим провести там вечеринку."

    "Зато стало удобно выпроваживать засидевшихся. «Юля хочет отдыхать». В общем, у неё была лучшая нычка в лагере. При том, что начальство о ней не знало."

    "Если Юля не хотела нас беспокоить, она ночью ловко выбиралась через окно в чердаке по стоящему рядом густому кипарису и исчезала в лесу. Наверное, проверяла свои Припасы."

    "Её любимым местом, кроме чердака, был наш холодильник."


    image an_30_02: # Анимация Юля холодильник
        
        "images/an/an30day/an_d30_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat



    stop music fadeout 1.0


    play music "audio/music/z_027.mp3" # Мурчание и лакание


    scene an_30_02 with dissolve


    pause (10000000000000000000000.0)


    scene an_d30_15 with dissolve

    "Когда она пила молоко, хвост действительно стоял торчком. Думаю, от удовольствия. Но Электронику, который глупо шутил, мы об этом не сказали."


    stop music fadeout 1.0


    play music "audio/music/z_181.mp3"


    scene cg ul_iul_hammock with dissolve

    "И вот как-то раз, устроившись вдвоем с Юлей в гамаке на чердаке, мы беседовали обо всяких разностях."

    "Кто-то, может, скажет, что в гамаке мало места для лежания вдвоем. Но только не для нас. Нас двоих можно было считать за одного человека."

    "Она была такая же маленькая как и я, даже меньше. Есть такое слово – миниатюрная."

    "И нога у неё была на два размера меньше моей. Прямо лапка, а не нога, очень аккуратная, прямо игрушечная. И ручки такие же."

    "А вот когти на них – будь здоров! Никакими уговорами нам не удалось убедить Юлю срезать их."


    scene cg iul_hands with dissolve

    "Но зато мы с Алисой стали ухаживали за ними и привели их, как сказала Алиса, «в божеский вид»."

    "Алиса сделал ей настоящий маникюр, отмыла, подточила и покрасила ноготки. И не поверите, они перестали выглядеть устрашающе."

    "Получилось красиво. Даже Семён, когда увидел, не выдержал, сбегал за красками и бумагой и нарисовал ее руки. (А вот мои руки он не рисует)."

    pause (10000000000000000000000.0)


    scene bg attic2 with dissolve

    "Семён подарил рисунок, и мы повесили его на чердаке, закрыв нехорошее слово, которое осталось от прошлых заездов."

    "Алиса одобрила. Сказала: «Пусть будет альтернативой изображению грубой физической силы». Это она про портрет мускулистого дядьки, которого мы называем между собой «громила»."

    "Мы давно его хотим убрать, хотя мальчишкам он нравится. Но уже решено, что на чердаке теперь появятся и другие картины. Будет картинная галерея."

    "Так что, мы это чудовище уберем со временем. Пусть «громила» висит у кибернетиков."


    scene cg iul_new_dress with dissolve

    "Ну вот про Юлю. Юля оказалась красивой девочкой. Это стало особенно заметно, когда мы искупали её в нашей душевой."

    "Её волосы оказались густыми и шелковистыми. И мы ещё уговорили её немного их постричь. Совсем немного. Расчесали. Получилась впечатляющая копна."

    "После шампуня, когда они высохли, они стали настолько густыми и поднялись, что ушей стало вообще не видно. И она ходила два дня без панамки в новом платье, которое сшила ей Лена."

    "Но это я немножко забегаю вперед."


    pause (10000000000000000000000.0)


    scene cg iul_uniform2 with dissolve

    "Конечно, когда мы примем ее в пионеры, форма будет сидеть на ней еще красивее. Но пока надо еще подготовить Ольгу Дмитриевну."

    "А я вот представила ее в пионерской форме. Прям здорово."


    pause (10000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene bg camp_artifacts with dissolve

    show sp_shu_003:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2


    "Не удивительно, что Шурик стал ходить за ней по пятам."

    "Он сказал, что изучает её, чтобы воплотить в образе кибердевочки, которую они с Электроником вымучивали уже третью неделю и все никак не могли сделать."

    "Но мы-то понимали, что она ему просто понравилась."


    scene bg library2 with dissolve

    show sp_je_018:
        yalign 0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 1.3

    "Это превращение произошло с ним после того, как Женя резко отвергла его ухаживания."

    "Я бы даже сказала — безжалостно. Хоть и в вежливой форме. Да уж, что-что, а отшивать Женька умеет."


    scene bg camp_artifacts with dissolve

    show sp_shu_003:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Дня два Шурик ходил как потерянный, и на него было жалко смотреть. Но потом вдруг переключился на Юлю. Но Юля, хоть и разрешала ему сопровождать себя, однако никак не выражала своего особого расположения."

    "По моему, ей было все равно."


    stop music fadeout 1.0


    play music "audio/music/z_012.mp3"


    scene cg ul_iul_hammock with dissolve

    "Я спросила, нравится ли ей кто-нибудь из мальчиков первого или второго отрядов, а она только пожала плечами."

    uv "Я НЕ ЗНАЮ. До сих пор я дружила только с Семёном."


    ul "А Семён тебе нравится?"


    uv "Он хороший. Я ему доверяю."

    "И я подумала  что она наверное, не понимает моего вопроса. Ведь она всю жизнь живет одна и не знает, что бывают отношения. Но все-таки я снова спросила."


    ul "Я знаю, что ты читаешь книги, которые стащила в библиотеке. Там есть книжки про любовь. Что ты думаешь про любовь?"


    uv "Я знаю про любовь. Это когда тому, с кем дружишь, разрешаешь гладить и чесать за ушком. Но при этом не царапаешь его. Хотя очень хочется."


    ul "А тебе хотелось поцарапать Семёна?"


    "Юля какое-то время смотрела молча, потом улыбнулась."

    uv "Я знаю не только про любовь, но и про ревность. Я читала. И мне кажется, ты ревнуешь."


    stop music fadeout 1.0


    play music "audio/music/z_171.mp3"


    "И я поняла что проговорилась. Я недооценила Юлю, она оказалась очень умной."

    "Я подумала, что время остановилось, наверное, только для ее тела, но не для ума. Она наверняка перечитала за эти годы всю лагерную библиотеку."

    "Она знает, что такое ОТНОШЕНИЯ, а я для неё маленькая девочка."

    "То, что она умнее, чем кажется, наверняка знает и Семён. Конечно, Семёну она наверняка нравится. Иначе как объяснить, что он так быстро нашел общий язык с «дикаркой»."

    "Но когда они успели познакомиться?"

    "Я дотронулась до щеки, у меня горело лицо."

    "Я подумала, что надо спросить прямо. Она не будет мне врать. Она не такая."

    ul "Скажи... Когда вы познакомились Семёном?"


    uv "Обычно я никому не рассказываю про друзей. Но я вижу, для тебя это очень важно. Нас познакомил Пионер. Он сказал, что Семёну можно доверять. А я верю Пионеру."

    uv "Кстати, он называет тебя своим лучшим другом. И мы говорили о тебе. И я поняла про вас. У вас как в книгах..."

    uv "Так что, тебе не о чем беспокоиться. Семён никогда не чесал меня за ушком."


    stop music fadeout 1.0


    play music "audio/music/z_478.mp3"


    uv "А ты можешь. \n(смеётся)"

    "И она обняла меня. Ее прикосновения были очень приятными, а запах странный, но тоже приятный. И я обняла ее."


    $ renpy.music.set_volume(0.70, delay=1.0, channel='music')

    play miscSounds "audio/music/z_024.mp3"

    $ renpy.music.set_volume(2.00, delay=1.0, channel='miscSounds')


    "Так мы сидели какое-то время, и я слышала, как бьется ее маленькое сердце и... Возможно мне показалось, но я услышала также тихое мурчанье..."


    ul "А ты не поцарапаешь меня?"


    uv "Как видишь, нет."


    ul "Спасибо. Я не знала, что кошки умеют читать мысли."


    uv "Мы много чего умеем. Только не забудь... Я не совсем кошка."


    ul "(Облегченно вздохнув) \nДа, извини..."


    stop music fadeout 1.0

    stop miscSounds fadeout 1.0


    play music "audio/music/z_700.mp3"


    scene bg ruins with dissolve


    ul "Скажи, Юль, а что ты знаешь про старый лагерь?"


    uv "Там все разрушено взрывом. Но есть подземная часть, она целая. Все двери в подвалы замурованы еще во время войны. А та дверь, в которую вы с Алисой ходили, единственная открывается, если знать как."


    scene cg ul_iul_hammock with dissolve


    ul "А что ты знаешь о взрыве?"


    uv "Ничего. Кроме того, что он превратил меня в то, что я есть."


    ul "Значит ты была там во время взрыва? И сколько тебе было лет тогда?"


    uv "Мне было восемь лет. И иногда мне кажется, что я так и не выросла."


    ul "Подожди. Если взрыв произошел в 1942 году, а сейчас 1969, значит, тебе..."


    uv "Тридцать пять лет."


    ul "По моему, судя по тому, как ты выглядишь, тебе сейчас не больше 14 – 15 лет. Это значит, взрыв затормозил старение. Ой извини, взросление. На целых почти тридцать лет."

    ul "Ты говоришь, что знала Виолетту Церновну еще до взрыва?"


    uv "А разве я это говорила?"


    ul "Ну, мне показалось, что да."


    uv "Виолетте Церновне не понравится, если я буду рассказывать о ней. И я не буду."


    stop music fadeout 1.0


    play music "audio/music/z_151.mp3"


    scene cg vio_med with dissolve


    ul "Хорошо... Скажи, а она помнит тебя до взрыва? Вы были знакомы?"


    scene cg iul_number with dissolve

    uv "Не просто знакомы. Вот, видишь?"

    "Юля приспустила повязку на ноге"

    uv "Это она сделала. Точнее, ей приказали."

    "И я увидела номер. Прямо как у узников концлагерей, про которых я с папой смотрела фильм. Теперь понятно, почему Юля носит эту повязку. Она не поцарапалась, как все думали."

    "Я похолодела. Онемела. По коже пробежали мурашки. И кажется, Юля заметила мое состояние. Она быстро надела повязку обратно и улыбнулась."


    scene cg ul_iul_hammock with dissolve


    uv "Тогда было страшно... Теперь уже нет."

    "И я открыла рот, чтобы спросить, но увидев глаза Юли, поняла, что ПРО ЭТО она точно говорить не будет..."

    "Поэтому я сменила тему разговора. Мне всегда хотелось узнать историю Дома на Болотах. И я стала приставать к Юле, чтобы она рассказала по него все, что знает."


    stop music fadeout 1.0


    play music "audio/music/z_202.mp3"


    scene bg shouse with dissolve

    ul "А что ты знаешь про Дом на Болотах?"

    uv "Знаю, что там кто-то живет. Ночью, во всяком случае. Это существо появляется там и ходит по верхним этажам."

    uv "Но оно не человек. Хотя выглядит, как девушка с длинными черными волосами... Она в ночной рубашке, или что-то вроде того."

    uv "Меня оно не тронуло. Я редко там бываю. Там не ловится рыба, и вообще ничего не живет, даже лягушки. Живет утка, но она живет не возле самого дома, а возле Непроходимого Брода."


    scene bg dnest with dissolve

    ul "А почему брод назвали Непроходимым? Он правда непроходимый?"

    uv "Потому что там утонула немецкая машина и два немца. Такой броневик. Его засосал песок. Он и сейчас там. И скелеты внутри."

    uv "А человек там пройти может. Хоть там и глубоко. Нам с тобой по шейку. Но Семён там проходит легко. Течение небольшое."


    scene cg ul_iul_hammock with dissolve


    ul "А зачем там ходил Семён?"


    uv "Ему не понравится, если буду рассказывать. Поэтому не буду."


    ul "А тебе можно доверять тайны. Если я скажу, что мне не понравится, если ты кому-то что-то расскажешь, ты не расскажешь?"


    stop music fadeout 1.0


    play music "audio/music/z_017.mp3"


    uv "Я и так не расскажу. Просто скажи, что это ТАЙНА."


    ul "Хорошо, последний вопрос. Есть ли у вас с Семёном тайны?"


    scene an_d30_01 with dissolve

    uv "(Подмигивает) \nО, вот это как раз тайна! Хочешь яблоко из заброшенного сада у Озера? Держи!"


    image an_30_01: # Анимация Юля бросает яблоко
        
        "images/an/an30day/an_d30_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.25
        "images/an/an30day/an_d30_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.25


    scene an_30_01 with dissolve


    pause (10000000000000000000000.0)


    "И она кинула в меня яблоком так быстро, что я едва поймала."

    uv "А ты знаешь, из тебя вышла бы неплохая кошка."


    stop music fadeout 1.0


    play music "audio/music/z_022.mp3"


    scene bg stock4 with dissolve
    
    show sp_od_024:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    "После ужина мы с Алисой зашли в бытовку Вано, куда нас позвала Ольга Дмитриевна. Посмотреть, нет ли в ящике с украденными Вано вещами наших."

    "Она сказала: «Ищите» и показала нам на три ящика, стоящих в углу."


    scene cg stock_closes with dissolve

    "Мы довольно быстро нашли свои вещи, но моего красного купальника там не было. Я озадачено перебирала вещи, а потом решила открыть другие ящики."


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    "Алиса стала хохотать и сползла на пол."

    hide sp_al_003


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Садясь рядом) \nТы чего?"

    hide sp_ul_021


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Пытаясь сдержать  спазмы смеха) \nЯ тут подумала, ты не нашла купальник, потому что... Ой не могу..."

    hide sp_al_003


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Прекрати. Да говори же!"

    hide sp_ul_021


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ой, мамочки, сейчас умру от смеха... Потому что ОН БЫЛ НА НЕМ! Прямо вижу, как он сидит ночами, голый, волосатый, и перешивает себе твои вещи."

    hide sp_al_003


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Пытаясь не засмеяться) \nАлиса, прекрати. Нельзя смеяться. Он, конечно, больной человек. Но ему точно сейчас несладко."

    hide sp_ul_021


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Да ладно. Он получил то, что заслужил. Давай еще вот в этом ящике посмотрим."


    scene cg import_closes with dissolve

    al "Тут какие-то вещи женские, новые. Смотри, все еще не распечатано. Тут чулки и трикотажные юбочки. Ой, какие красивые... Импортные. Подожди, дай я примерю."
 

    scene cg stock_closes with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Не надо, вдруг кто-то увидит!"

    hide sp_ul_019


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Нет никого. Если это не изъяли при обыске, то это ничьё. Во всяком случае, вещей администрации тут нет. Смотри одни продукты и среди них женские новые вещи."

    al "Точно, он хотел загнать эти импортные шмотки директрисе и завхозу. Фарцовщик."

    al "Надо узнать у ОД, заказывали ли они ему что-то из вещей. Он часто ездил в райцентр, вполне могли. Если не заказывали, мы отдадим нашим девочкам. Тут очень много..."

    hide sp_al_005


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Слушай если так, то давай устроим конкурс красоты. Я всегда хотела как Мику, в чулочках. Но мне не покупали. Гольфы только. Говорили, маленькая еще."


    scene cg import_closes with dissolve

    al "(Деловито перебирая вещи) \nТак, это размер на Славю. О, а это точно на меня. Вот, тебе эти чулки подойдут, детские. Наверное, брал для чьих-то чад. Ну уж точно не для пионерок."

    al "Тут юбочки. Вот эта синяя, просто отпад. Это же югославские вещи, чешские, вот и этикетка. Жаль, обуви нет. Но зато есть косметика."


    scene cg stock_closes with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "У тебя в чемодане есть туфли лодочки. И босоножки."


    hide sp_ul_021


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Да, теперь у меня полный комплект. В общем, относим все к нам и я зову девочек. На день рождения Женьки устроим показ."

    hide sp_al_005


    "А Ольге Дмитриевне мы решили не говорить про находку. Просто спросили, привозил ли Вано в лагерь что-то для администрации, и получили отрицательный ответ. Вот, рассказываю, что было дальше."


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"


    scene bg oldcamp4 with dissolve

    "День рождения Жени мы решили отмечать всем отрядом, втайне от руководства и Ольги Дмитриевны. Сразу после отбоя, в 22-30 в хорошо сохранившемся административном корпусе старого лагеря."

    "Здание было дореволюционное, с большим подвалом, оборудованном в советское время то ли под клуб, то ли под агиттеатр."


    scene bg oldcamp_basement with dissolve

    "Во всяком случае, маленькая сцена там была. Мальчики натащили туда столов и лавок, а мы устроили уборку. А Семён расписал задник сцены под горный пейзаж."


    scene bg oldcam_stage with dissolve
 
    "Получилось довольно уютно."

    "Мы решили устроить вечеринку там. Для этого туда заранее, целых три дня носили всё необходимое для праздника."

    "Припасы, свечи, желтую ширму для конкурса и, как потом выяснилось, кое-что еще, чтобы сделать праздник более зажигательным."

    "И вот, долгожданный вечер настал. Старый лагерь был далековато от нового, поэтому шуметь было можно, сколько душе угодно."

    "Танцевали под радиоприемник, Семён показывал карточные фокусы, Алиса сделала танцевальный номер, а я читала свои стихи."

    "Мику играла на гитаре этюд, Электроник подражал голосам и показывал пародии на всех, включая физрука, а Шурик стоял вниз головой на руках на спор, на время."

    "Потом кушали вкусняшки, пели под гитару все известные песни. Нарезали заранее заказанный Любаше большой торт под чай, приготовленный тут же, на костре."

    "Из напитков кроме чая были ещё компот и лимонад. Лимонад не хотели брать сначала, тяжело тащить. Но я сказала, что я сама потащу. В результате, тащил Толик, целых четыре бутылки."

    "А компота взяли из столовой целую трёхлитровую банку. Славя, когда попробовала его, сразу выплюнула, сказала, что он прокис. Я заметила, что Алиса сразу встрепенулась и посмотрела на Семёна."

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "А ну-ка, плесните мне компотика. Сейчас скажу, прокис или не прокис."

    hide sp_al_005


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Залпом опустошив кружку компота) \nДа, действительно, прокис. Детям и чувствительным натурам — не пить."

    hide sp_al_004


    show sp_shu_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 
    with dissolve

    "Следующим среагировал Шурик. Быстренько налил себе компота и картинно выдохнув тоже выпил залпом."

    shu "И вправду, прокис. Никому не рекомендую."

    hide sp_shu_002


    "В следующие пять минут весь компот был выпит. Я тоже хотела попробовать, на общей волне, но Славя положила мне руку на плечо и покачала головой."


    stop music fadeout 1.0


    play music "audio/music/z_155.mp3"



    "Гвоздем программы были конкурсы. Игру в бутылочку отвергли. Все зашикали на предложившего её Шурика."

    "Зато конкурс чулочек прошел на УРА. Девочки вышли в обновах и трикотаже, который выгодно обтягивал стройные фигуры. В чулочках все смотрелись старше своего возраста и выглядели как настоящие леди."


    scene cg contest_ul2 with dissolve

    "Я тоже приняла участие. На мне были чулки и розовое платье."


    pause (100000000000000000000000000.0)


    scene bg oldcam_stage with dissolve

    "Никто не знал, что в конкурсе примет участие Женя. Все привыкли к её тихому, незаметному существованию в библиотеке. Когда Женя узнала от нас с Алисой, что будет конкурс, она решила участвовать. "
 
    "Женя старалась ничем не выделяться среди девочек отряда. Носила ту же форменную рубашку и юбочку."

    "Правда, её галстук был особенно хорошо отглажен. Но это и не мудрено, ведь в библиотеку постоянно заглядывало лагерное начальство."

    "В общем, одевалась скромно, хотя все знали, что она дочь обеспеченных родителей. Вот и сейчас, из принесенных нами со склада вещей, она выбрала неброское, черное, трикотажное платье."


    scene cg contest_je with dissolve

    "Но когда она вышла на «сцену», мы все ахнули."


    pause (100000000000000000000000000.0)


    sl "Ну, Умнова, ты просто королева!"

    al "Вот это выход из-за печки! Женька, ты прима!"

    "И вот, я вижу, как Женя сделала полукруг, остановилась, подняв руки. На мой взгляд, Женя была не просто хороша. Её фигурка была безупречна, а ноги сделали бы честь любому балетному коллективу."

    "Вот только рост у Жени был не балетный. Но благодаря пропорциональности её фигуры, это было вовсе незаметно."

    "Я наблюдала за Шуриком, он сидел, обхватив колени руками, раскачивался на стуле как завороженный и буквально пожирал Женю глазами."

    "Семён смотрел с неожиданно проснувшимся интересом. А Толик держался за сердце. И только Электроник улыбался своей вечной, странной улыбкой."

    "Потом грянули аплодисменты. А Семён, как председатель мужского жюри, выкрикнул:"


    scene bg oldcam_stage with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    sem "ЭТО ГРАН ПРИ!"


    scene cg contest_je with dissolve

    "Все, в том числе и еще не успевшие переодеться девочки, кинулись обнимать и целовать Женю. Все были очень рады за неё."


    # scene bg oldcam_stage with dissolve


    # show sp_le_001:
        # yalign 0.1 subpixel True
        # xalign 1.0 subpixel True
        # zoom 1.2 


    # le "(Трогая рукой платье Жени) \nНадо же, кто бы мог подумать! А тени... И помада. Какие классные! Вот, Женька, скрывала от нас такую красоту!"

    # le "Непременно дашь мне свои цацки и косметику на танцы! Заметано?"


    # scene cg contest_je with dissolve

    # je "Конечно."


    scene bg oldcam_stage with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    sem "(Взобравшись на стул) \nТИХО! Мы тут с ребятами посовещались. И вот что... Женя именинница, но победила она не поэтому. Надеюсь, со мной все согласны?"

    "Все одобрительно зашумели."

    sem "Так вот, она получает ГРАН ПРИ. Главный приз!"

    sem "Но остальные девочки тоже старались и нам нужно разыграть еще три места: особый приз за няшность, приз зрительских симпатий и утешительный приз."

    sem "Начну с утешительного приза! Он достанется..."


    scene cg contest_ul with dissolve

    "Все одновременно повскакивали с мест и закричали «УЛЬЯНЕ! УЛЬЯНЕ!»"

    sem "Да! Нашей дебютантке, Ульяне Лениной!"

    al "(Обнимая меня) \nНе реви, дуреха! Это же твоя премьера!"

    ul "Я от радости."


    pause (100000000000000000000000000.0)


    scene bg oldcam_stage with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    sem "(Сделав паузу) \nТретье место..."

    hide sp_sem_001

    "В старом офисе, озаряемом колеблющемся светом свечей, наступила напряженная тишина. Шурик неожиданно стал отбивать на стуле барабанную дробь и тут же, получив подзатыльник от Алисы, затих."


    scene cg contest_ats with dissolve

    sem "Приз зрительских симпатий у нас получает Атсуи!"


    pause (100000000000000000000000000.0)


    scene cg contest_girls with dissolve
 
    "Третье место разделили Мику Хатсуне и Елена Тихонова!"


    pause (100000000000000000000000000.0)


    scene cg contest_sl with dissolve

    "Второе место досталось Славе. С перевесом всего в один голос. Хотя, все были уверены, что только ей достанется первое место. Она же красавица."


    pause (100000000000000000000000000.0)


    scene cg contest_iul with dissolve

    "Юле ожидаемо достался приз за няшность."


    pause (100000000000000000000000000.0)


    scene cg contest_al with dissolve

    "И теперь всем стало ясно, что первое место достанется Алисе."

    "Но она закрыла лицо руками. Как потом она сама призналась, она была уверена, что выиграет Славя. И так сидела. Все ее тормошили и поздравляли. Но у неё было серьезное лицо, какое-то нерадостное."


    pause (100000000000000000000000000.0)


    al "Сёма, признайся, это твоя работа? Решил так подъехать? Это нечестно. Недостойно по отношению к другим конкурсанткам."


    scene bg oldcam_stage with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    sem "Алиса, это решение большинства. Если не веришь, тут все записки с голосами. Проверь сама."

    "Семён протянул Алисе кружку со свёрнутыми в трубочку записками."

    sem "Вот, смотри, я голосовал за Мику. Единственный из всех — не за тебя."


    scene cg contest_al with dissolve

    "Алиса повеселела."


    scene bg oldcam_stage with dissolve

    "И мы решили, что в этом чуланчике в старом лагере обязательно еще будем отмечать наш будущий отъезд и прощание с лагерем."

    "Потом все угощались, болтали, разбились на пары и разбрелись ненадолго по зданию. И тут я уже не могла за всеми уследить."

    "Помню только, что Семён поднялся с Женей на чердак. Они там о чем то болтали, а дверь была закрыта, и я так и не смогла подслушать."


    scene an_d30_25 with dissolve
 
    "Но когда они вышли, он ее обнял прямо на лестнице. И они целовались. Прямо по-взрослому."


    image an_30_03: # Анимация Семён Женя целуются в Старом лагере
        
        "images/an/an30day/an_d30_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an30day/an_d30_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat


    scene an_30_03 with dissolve

    pause (10000000000000000000000.0)


    scene bg oldcamp_hide with dissolve

    "А когда они ушли,  я проникла  туда."

    "Очень уютная нычка оказалась, надо сказать. А под лавочкой что-то блеснуло. Я нагнулась, а там лежал рюкзак, и в нем звякнуло, когда я ткнула его ногой."

    "Наверное, там как раз и было то, от чего «прокис» компот."

    "Но тут меня позвали и я кубарем скатилась вниз, иначе бы меня спалили. Надо будет как-нибудь туда еще наведаться."


    show location_open_old_camp_hide with dissolve

    pause (10000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_181.mp3"


    scene bg night_beach with dissolve

    "Потом все пошли на реку Бурлейку, купаться. На берегу ночью было очень красиво."

    "Как назло, купальников из лагеря не захватили (кто ж знал!). Но решено было не отменять веселья и купаться «как есть»."
 
    "Для этого мальчиков прогнали в другой конец пляжа. Но они, конечно же, подглядывали. И кажется, девочки вполне себе догадывались об этом."


    scene cg campfire_beach with dissolve

    "Потом жгли костер у самой кромки воды и он отражался в реке. Было ощущение, что в воде горит второй костер."


    scene cg all_campfire_iul with dissolve

    "Курили запретные сигареты, которые Семён купил тайком от Виолы, когда ездил вместе с ней в райцентр за медикаментами."

    "Праздник, определенно, удался. Кто протащил спиртное, я так и не выяснила. Славя была злая. Мы, наверное, с ней одни были трезвые, потому что пили лимонад."

    "Она еще спросила: «Улька, ты в курсе про водку?» Я ей сказала, что нет (и это правда). Так и не дознались."

    "Я потом у Алисы спросила, но она отмахнулась. Сказала: «Ну зачем тебе знать? Наверное, кто-то из мальчишек»."

    "Было еще много всего... Такого...  Но об этом я напишу в ТЕТРАДКЕ ДЛЯ ОСОБЫХ МЫСЛЕЙ."
 






    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day31

return 




