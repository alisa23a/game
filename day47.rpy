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

    scene bg smu_medic_far with dissolve

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


    scene bg smu_medic_far with dissolve


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

    ul "Так это, я серьёзно. У меня тоже такое было после Юлиного отвара."

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


    scene bg smu_medic_far with dissolve


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


    scene bg medic_lib_ext with dissolve

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


    scene bg smu_medic_far with dissolve

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


    scene bg smu_medic_far with dissolve

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

    al "Не знаю, но души Смутьянова там уже нет. Она теперь в банке"

    al "о душу Смутьянова вытеснили, её там уже нет. Она теперь в банке. Фу, какой противный цвет у него."


    "Шарик заметался в банке. Он бился о её стенки, а потом затих. Алиса протянула банку мне."

    scene bg smu_medic_far with dissolve

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


    scene bg smu_medic_far with dissolve

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


    scene bg smu_medic_far with dissolve

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

    al "Увидим."

    hide sp_al_055


    stop music


    play music "audio/music/z_023.mp3"


    scene bg library with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Мы застали Семена в библиотеке. Усадив его напротив, мы выложили ему всё, что знали про лабораторию."

    "Семен долго молчал. Потом встал и начал ходить по библиотеке что-то обдумывая."

    sem "Вы ещё не всё знаете про Виолу. Но об этом потом. Еду ей ношу я, потому что тете Любе она не доверяет."

    sem "Она вообще никому не доверяет. И заставляет меня попробовать, чтобы убедиться, что пища не отравлена. Я всё время снимаю пробу с её блюд. Это первое."

    sem "Идея хороша. Возможно лучшая из всех предложенных вами вариантов."

    sem "Что касается слияния с Пионером, то..."

    "Семен показал в пространство фигу."

    hide sp_sem_001


    show sp_sem_023:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Вот ему, а не слияние. Хочет быть вечно молодым, сволочь. Вы знаете, сколько ему лет на самом деле? Он едва ли не старше Петровича."

    hide sp_sem_023


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Всё это затеяно им с одной целью – жить вечно. И ещё у него синдром Бога."

    sem "Весь лагерь – это его маленькая планета, на которой он устраивает свои эксперименты-спектакли. Восстания, войны, погружает нас в пороки."

    hide sp_sem_001


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Значит, это он устроил два восстания?"

    hide sp_al_001


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Да. Тут все чьи-то то прототипы. Смутьянов например, это наш незабвенный вождь мирового пролетариата в карманном исполнении Гендакова."

    hide sp_sem_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Так он не Пионер?"

    hide sp_ul_019


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Нет. Это личина. На самом деле, он Гендаков Владимир Геннадьевич, начальник проекта и с 1939 года руководитель лаборатории."

    sem "Он может менять внешность. Последнее время что-то у него не ладится. Потому и решил свернуть эксперимент."

    sem "Он заметно постарел за этот месяц. Последняя наша встреча была на отмели. Я поразился произошедшим с ним изменениям."

    sem "Страшно ощущать себя донором. Но пока Виола всё держит в своих руках, я не могу ни сбежать ни как-то повлиять на ситуацию."

    sem "Если честно, я был в отчаянии. Хорошо, что я не один. Теперь я вижу, что у меня есть поддержка."

    sem "Но ещё месяц назад, приди вы ко мне с таким предложением, я с легкой совестью сдал бы вас Виоле. Очень многое произошло за это время."

    hide sp_sem_001


    show sp_sem_025:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Вы простите меня?"

    sem "Алиса, ты... Ты меня еще..."

    hide sp_sem_025


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Хочешь, чтобы я сказала, что люблю тебя? Нет. Я уже говорила, что сделал свой выбор. Но простить смогу."

    hide sp_al_004


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Мне кажется, мы пришли к единому мнению относительно того, что нужно делать. Теперь все идем к Юле. Она сейчас на чердаке. Надо посвятить её в наш план."

    hide sp_ul_019


    stop music


    play music "audio/music/z_176.mp3"


    scene bg attic2 with dissolve

    show sp_iul_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Юля обрадовалась нашему приходу. Но когда мы рассказали ей всё, стала очень серьёзной."

    hide sp_iul_008


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Я намекнула ей, что её Ягоды Забвения могли бы нам помочь одолеть Виолу."

    uv "У меня ягод нет. Они растут в единственном месте, у Сосны Совы. Их ещё надо нарвать. Без меня вы точно не найдете их. Я беру Ульяну и мы сейчас же отправляемся."


    scene cg meeting_vio with dissolve

    "Когда мы с Юлей пробирались мимо площади, на ней Ольга Дмитриевна построила пионеров. Рядом стояла Виола."

    "Они говорили по очереди что-то о карантине и о том, что нужно всех временно изолировать и сделать необходимую профилактику. Речь шла об очередной порции уколов."


    scene bg stels with dissolve

    "Мы незаметно прокрались и выскочили за забор лагеря через нашу лазейку."


    stop music


    play music "audio/music/z_005.mp3"


    scene bg opine2 with dissolve

    "Юля шла быстро. Через пол часа мы были на вершине «кургана». На нём росла одинокая сосна. Она была огромной. Высоко над землей зияло дупло, откуда на нас смотрели два совиных глаза."


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Ну вот и Сосна Совы. Я поищу ягоды, а ты посиди тут."

    hide sp_iul_012


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А какие они?"

    hide sp_ul_019


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Обычные. Похожи на вороний глаз. Только не черные, а синеватые."

    hide sp_iul_012


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тогда вон там, вижу один кустик"

    hide sp_ul_021


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Молодец. У тебя отличное зрение. Надо набрать их минимум 10 штук. Чтобы наверняка подействовало. На кусте обычно не больше трех. Ищем вместе."

    hide sp_iul_012


    scene cg berries with dissolve

    "Мы набрали необходимое количество за десять минут. Ягод оказалось много, наверное в этом году на них был урожай."


    pause (100000000000000000000000000.0)


    stop music


    play music "audio/music/z_4102.mp3" noloop


    scene cg owl with dissolve

    "Вскоре, помахав рукой сове, высунувшейся из дупла, громко крикнувшей, очевидно для острастки, и удивленно смотревшей нам в след. Затем мы побежали в лагерь."


    pause (100000000000000000000000000.0)


    stop music


    play music "audio/music/z_131.mp3"


    scene bg dining with dissolve

    "Приближалось обеденное время. Юля сделала отвар и процедив, вылила его в стакан."


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Этот отвар не имеет ни вкуса ни запаха. Идеален для подмешивания в компот."

    hide sp_iul_012


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Она не любит компот. Лучше в чай с лимоном."

    hide sp_sem_001


    scene cg glass_tea with dissolve

    "Так мы и сделали."


    scene cg glass_tea

    pause (10000000000000000000000.0)


    stop music


    play music "audio/music/z_130.mp3"


    scene bg medic_lib_ext with dissolve

    "Когда пришло время обеда, мы с замиранием сердца наблюдали, как Семён тащит разнос с едой в медпункт. Дверь за ним закрылась."


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Меня всю колотит. Только бы не сорвалось. Она точно заставит его пить. Семен вроде что-то принял перед этим?"

    hide sp_al_001


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Я дала ему съесть много масла. Поэтому, если даже она заставит его отпить, на него подействует не сразу."

    hide sp_iul_012


    show sp_sem_024:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Прошло десять минут. На крыльцо вышел покачивающийся Семен."

    hide sp_sem_024


    scene bg medic_lib_ext2 with dissolve

    show sp_sem_024:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Спит, как суслик. \n(встряхивает головой)"

    sem "Ну и сильная же штука."

    hide sp_sem_024


    "Больше он ничего сказать не успел, так как его голова упала на грудь, Мы подхватили его, оттащили его на лавочку неподалеку, где он и уснул."


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Юля, он не умрет?"

    hide sp_al_001


    show sp_iul_012:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Нет, но проспит сутки."

    hide sp_iul_012


    stop music


    play music "audio/music/z_201.mp3"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Мы понимали, что крепко связать Виолу, чтобы она потом не развязалась, мы не сможем. Для этого нам понадобится Петрович."

    "Пришлось рассказать ему о планах Виолы и Гендакова. Старик покачал головой."

    pe "Знаю его, змея. От него можно было ожидать. Поди ж ты, живой оказался! А я думал, он того. После взрыва-то. Да-а... Ну и кашу вы заварили, ребятушки."


    scene cg vio_final with dissolve

    "Петрович помог нам с Виолой, связав ее каким-то особым морским узлом."


    scene cg vio_final


    pause (10000000000000000000000.0)


    scene bg watchmans_cabin with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    ul "Не вырвется?"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Петрович крякнул возмущенно:"

    pe "Пока ещё никому не удавалось. Если она, конечно, не сам сатана в юбке."


    scene bg medic with dissolve

    "Мы вернулись в медпункт."

    "Алиса порылась в ящике стола и обнаружила ключ."


    scene cg safe_key with dissolve


    pause (10000000000000000000000.0)


    "Ключ был сейфовый, мудреный, с завитушками и загогулинами. Было ясно, что сейф находится где-то в медпункте, а возможно и в кабинете Виолы."

    "Мы прочесали всё вдоль и поперек. И наконец, я услышала радостный крик Алисы."


    scene cg vision_test with dissolve

    "Дверцей сейфа оказалась таблица проверки зрения."


    scene cg vision_test

    pause (10000000000000000000000.0)



    scene cg vision_test2 with dissolve


    pause (10000000000000000000000.0)


    "Ключ входил аккурат в букву О."


    scene cg vision_test3 with dissolve


    pause (10000000000000000000000.0)


    stop music


    play music "audio/music/z_1013.mp3"


    scene cg vio_docs with dissolve


    "Когда мы открыли сейф, то увидели в нем папки и тетради. А также пачки отдельных листочков аккуратно перевязанных бечёвкой."


    scene cg vio_docs


    pause (10000000000000000000000.0)


    "Пролистав папки, мы поняли, что они содержат результаты экспериментов. А вот тетради были ни чем иным, как дневниками Виолы. Которые, как выяснилось, она аккуратно вела с 1942 года."

    "Тетрадки были очень толстыми. Помимо страниц в них были подшиты какие-то документы."

    "Но самым интересным для нас было то, что относилось непосредственно к нашему году. Именно это мы и решили прочитать, как только у нас окажется свободное время."


    scene bg medic_lib_ext with dissolve


    "А пока нужно было спешить. Оказывается, Виола успела сделать уколы почти всем отрядам. Из первого отряда не уколотыми были только мы с Алисой, Юля, Семен, Женя и Ольга Дмитриевна."

    "Также можно было рассчитывать на Элю. Остальные, двигались очень медленно, как будто в полусне."

    "Всё было продумано и судя по всему, процесс «тестирования» должен был начаться с часу на час."

    "Петрович предложил отнести Виолу на наш Чердак, потому что её точно будут искать в медпункте и библиотеке, а скорее всего, заглянут и в подвал."


    scene cg vio_final with dissolve

    "Мы тут же перетащили Виолу на чердак. Туда же позже мы переправили и Семёна. Он отпил чаю по приказу Виолы чтобы не вызывать подозрений, поэтому теперь всё время засыпал."

    "Никто не знал, сколько ещё живых манекенов было у Гендакова. А то, что он будет не один, не вызывало сомнений."












    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day48

return