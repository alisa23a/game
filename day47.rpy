label day47:

    $ days = 47

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music


    play music "audio/music/z_176.mp3"


    scene bg camp_artifacts with dissolve

    "Когда мы пришли в лагерь, то заметили, что на площади никого нет. Остатки манекенов куда-то убрали."



    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Где же все? Не случилось ли опять чего?"

    hide sp_al_056


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "На крыльцо медпункта выскочила Мику."

    mi "Где вас носит? Смутьянов умирает!"

    hide sp_mi_019


    scene bg medic2 with dissolve

    "Мы бросились в медпункт. Там было людно. Кажется, что весь лагерь собрался вокруг кушетки с лежащим телом."


    stop music


    play music "audio/music/z_131.mp3"


    scene bg smu_legs with dissolve

    "Лысая голова «вождя всея пионерии» бессильно свисала. Глаза закатились. Лицо приобрело синеватый оттенок."


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Мику как это случилось?"

    hide sp_al_057


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    mi "Я точно не знаю, он где-то долго прятался, потом оголодал, прокрался на кухню, и добрался до той кастрюли с грибным супчиком.Он съел всё!"

    hide sp_mi_019


    show sp_ul_053:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "С ума сойти... Она огромная. Там же было еще половина кастрюли! Все съел один?!"

    hide sp_ul_053


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Черт, вот мы идиоты. Надо было сразу вылить этот проклятый суп в помойку."

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Чего уж теперь, смотри, кажись, он того. Не дышит совсем. Представляю, как его сейчас плющит. Не по-детски."

    ul "Наверное, он в царстве грибов цветные сны смотрит. Вряд ли ему плохо. Скорее хорошо."

    hide sp_ul_019


    stop music


    play music "audio/music/z_542.mp3"


    scene cg mushroom_trip with dissolve

    " И я вспомнила, как это было у меня..."


    scene bg smu_legs with dissolve


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "(Шёпотом) \nТихо, нельзя глумится над умирающим."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Так это, я серьезно. У меня тоже такое было после Юлиного отвара."

    hide sp_ul_019


    stop music


    play music "audio/music/z_130.mp3"


    "Суета вокруг посиневшего Смутьянова, кажется, подходила к финалу."


    scene bg medic2 with dissolve

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Не смотря на все старания Виолы, Смутьянов не приходил в сознание, и она бессильно развела руками."

    vio "Это страшное отравление. Через 10 минут будет агония. Он не может дышать нормально, потому что дыхательные пути заложены."

    vio "Я попыталась хирургически освободить доступ воздуха в легкие, но это мало помогло. Яд проник в кровь. Он будет распухать дальше."

    vio "Лучшее, что я могу, это сделать ему эвтаназию. Но это запрещено законом."


    scene bg smu_legs with dissolve


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "(Шёпотом) \nУ меня идея."

    al "Кажется, то, что находится у тебя в баночке, может быть развоплощённой душой. Во всяком случае, это следует из того, что рассказал тебе Пионер про бункер."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну, допустим. А чем это может помочь Смутьянову?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну, развоплощённые души ищут свободные тела. Никогда не читала про это? Во всех страшщилках про привидения об этом есть."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я тоже думаю, что это душа. И как она..."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не знаю. Заодно и проверим. Только вот, я не уверенна, ОН это будет, или ОНА. Сейчас быстро сбегай в домик, возьми его и тащи сюда."

    al "Я попрошу Виолу оставить нас одних со Смутьяновым и всех удалить. Скажу, мы были друзьями, и я хочу попрощаться. А ты быстро сюда. Сейчас мы его реанимируем."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Как это? Виола сказала, что безнадежно."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "В нашем случае нет. Потом сама увидишь."

    hide sp_al_056


    scene cg swisher2 with dissolve

    "Я побежала в наш с Алисой домик и вытащила из под кровати баночку со светящимся шариком, летающим внутри. Он как будто обрадовался мне и зашуршал."


    pause (10000000000000000000000.0)


    "«Потерпи» – сказала я и бросилась в медпункт."


    scene bg medic2 with dissolve

    "Виола уже выводила пионеров с грустными лицами на улицу."

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    vio "Иди, там твоя подружка. Говорит, что вы хотите попрощаться с Володей. Не знаю, когда вы успели подружиться. Но это неважно."

    vio "Иди. Учти, сейчас начнутся судороги. Ты уверена, что хочешь это видеть?"

    hide sp_vio_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, мне всё равно. Он был хоть и взбалмошный, но, в общем, неплохой мальчик. Просто идейный."


    stop music


    play music "audio/music/z_131.mp3"


    scene bg smu_legs2 with dissolve

    "Я вошла в медпункт. Смутьянов уже был совсем бледный, кровь отлила от его кожи. Стал как будто полупрозрачный, восковой. Аж позеленел."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Быстрее. Я покараулю, чтобы никто не вошёл. Поставь баночку рядом с его изголовьем, открой и ничему не удивляйся."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Прямо скажем, не лучшее тело для воплощения. К тому же, больное."

    hide sp_ul_019


    "Я открыла баночку. Шуршавчик какое-то время не вылетал. Он как будто не верил в то, что его выпускают на свободу."


    scene an_d47_02 with dissolve

    "Потом приподнялся над баночкой. Сделал круг над кроватью Смутьянова. Остановился над головой потом заметался и вдруг стремительно влетел в его открытый хрипящий рот."


    image an_47_01: # Анимация воплощение шуршавчика

        #"images/an/an47day/an_d47_01.webp" with Dissolve(0.5, alpha=True)
        #pause 0.5
        "images/an/an47day/an_d47_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an47day/an_d47_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an47day/an_d47_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an47day/an_d47_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an47day/an_d47_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.2



        #repeat


    stop music


    play music "audio/music/z_1003.mp3"


    scene an_47_01 #with dissolve


    pause (10000000000000000000000.0)


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну вот, осталось ждать."

    hide sp_al_055


    scene cg smu_soul with dissolve

    "Неожиданно изо рта Смутьянова появился другой шарик. Он был коричнево-зеленый, а не оранжевый, как наш. Он повис, как будто не знал что ему делать."


    pause (10000000000000000000000.0)


    "Алиса молниеносным движением подставила под этот шарик банку, приподняла её и захлопнула сверху крышкой. Шарик остался заперт в банке."


    scene cg smu_soul2 with dissolve

    al "Это Смутьянов. Там ему самое место. Нелепый был человек."


    pause (10000000000000000000000.0)


    ul "Ты такое когда-нибудь видела? Они что, поменялись? У меня дрожат руки. Что теперь будет?"

    al "Не знаю. Ты же говорила, Пионер утверждал, что души меняют тела. Ну как бы они их регенерируют. Так что шанс  у нас есть."

    al "о душу Смутьянова вытеснили, её там уже нет. Она теперь в банке. Фу, какой противный цвет у него."


    "Шарик заметался в банке. Он бился о её стенки, а потом затих. Алиса протянула банку мне."

    scene bg smu_legs with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Спрячь быстрее. Сейчас появится Виола."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Это фантастика. Слушай. А в фильмах про всяких привидений духи проходят сквозь стены и всё такое. Баночка не должна быть для них препятствием."

    hide sp_ul_021


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не должна, но она препятствие. Возможно, все дело в кварце, из которого состоит стекло. В другой таре шуршавчика не удержать."

    al "Так что, тебе повезло, что ты случайно запихнула его в стеклянную банку. Да еще и со стеклянной крышкой."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я нашла её в лаборатории. Там все банки такие."

    hide sp_ul_021


    #"Я вдруг вспомнила, что в моем кошмарном сне Виола тоже держала меня в стеклянной банке."


    stop music


    play music "audio/music/z_495.mp3"


    scene bg medic2 with dissolve

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Вошла Виола, она посмотрела на лежащее тело озадаченно."

    hide sp_vio_001


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "В дверь просунулось сразу несколько голов пионеров и голова Семена."

    sem "Нужна помощь? Надо же отнести тело, как я понимаю. Я сейчас позову кибернетиков."

    hide sp_sem_001


    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    vio "Стоп. Не надо пока никого звать и уносить. Смутьянов ещё жив. Хотя это и невероятно. И кажется, он даже нормально дышит. Это какой-то нонсенс. Что вы с ним делали?"


    scene bg smu_legs with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ничего, только дали попить водички."

    hide sp_al_055


    scene bg medic2 with dissolve

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    vio "Какой водички?"

    hide sp_vio_001


    scene bg smu_legs with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "А вон, в том стакане."

    hide sp_al_055


    scene cg glass with dissolve

    pause (10000000000000000000000.0)


    scene bg medic2 with dissolve

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    vio "С ума сошли. Это медицинский спирт, я принесла его для обтирания трупа. Странно, что спирт так подействовал на больного."

    vio "Хорошо, пустите меня к нему и идите. Если он выживет, то считайте, что вы сделали научное открытие по побочному действию спирта на организм."


    scene bg camp_artifacts with dissolve

    "Мы вышли."


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Теперь он поправится?"

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Увидим"

    hide sp_al_055







    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day48

return