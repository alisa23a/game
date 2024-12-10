label day47:

    $ style.say_window = style.window

    $ days = 47

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_46_00 = True
    $ im_gal_46_02 = True
    $ im_gal_46_03 = True
    $ im_gal_46_04 = True
    $ im_gal_46_05 = True
    $ im_gal_46_06 = True
    $ im_gal_46_07 = True
    $ im_gal_46_08 = True
    $ im_gal_46_10 = True
    $ im_gal_46_11 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


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


    scene bg smu_legs with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Лысая голова «вождя всея пионерии» бессильно свисала. Глаза закатились. Лицо приобрело синеватый оттенок."

    scene bg smu_medic_far with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Мику, как это случилось?"

    hide sp_al_057


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    mi "Я точно не знаю, он где-то долго прятался, потом оголодал, прокрался на кухню и добрался до той кастрюли с грибным супчиком. Он съел всё!"

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

    ul "Наверное, он в царстве грибов цветные сны смотрит. Вряд ли ему плохо. Скорее, хорошо."

    hide sp_ul_019


    scene cg mushroom_trip with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_542.mp3"


    " И я вспомнила, как это было у меня..."


    scene bg smu_medic_far with dissolve


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "(Шёпотом) \nТихо, нельзя глумиться над умирающим."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Так это, я серьёзно. У меня тоже такое было после Юлиного отвара."

    hide sp_ul_019


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Суета вокруг посиневшего Смутьянова, кажется, подходила к финалу."


    scene bg medic2 with dissolve

    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Несмотря на все старания Виолы, Смутьянов не приходил в сознание, и она бессильно развела руками."

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

    al "Ну, развоплощённые души ищут свободные тела. Никогда не читала про это? Во всех страшилках про привидения об этом есть."

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

    al "Не знаю. Заодно и проверим. Только вот я не уверена, ОН это будет, или ОНА. Сейчас быстро сбегай в домик, возьми банку с шуршавчиком и тащи сюда."

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


    scene bg smu_legs2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


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



    scene an_47_01 #with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1003.mp3"


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

    al "Не знаю, но души Смутьянова там уже нет. Она теперь в банке. Фу, какой противный цвет у него."


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

    al "Так что тебе повезло, что ты случайно запихнула его в стеклянную банку. Да еще и со стеклянной крышкой."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я нашла её в лаборатории. Там все банки такие."

    hide sp_ul_021


    scene bg medic2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_495.mp3"


    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Вошла Виола и озадаченно посмотрела на лежащее тело."

    hide sp_vio_001


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "В дверь просунулось сразу несколько голов пионеров и голова Семёна."

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

    show sp_vio_022:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    vio "С ума сошли. Это медицинский спирт, я принесла его для обтирания трупа. Странно, что спирт так подействовал на больного."

    hide sp_vio_022


    show sp_vio_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

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


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_197.mp3"


    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "После чудесного исцеления Смутьянова было вот что."

    "Все хотели расспросить спасённого, где он был во время восстания. А также, что он чувствовал, когда объелся грибного супа."


    scene bg camp_artifacts with dissolve


    show sp_shu_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Особенно усердствовали кибернетики. Их волновал научный аспект этой, как они сами говорили, «клинической смерти»."

    "Шурик выдвинул теорию, согласно которой вернувшийся с того света человек должен помнить, как происходил переход и «что там»."

    "Но ему намекнули, что это неэтично."


    scene bg camp_artifacts with dissolve

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Да и о чём Смутьянову было рассказывать? Как убежал, прятался, а потом отравился грибами? Невелик подвиг."


    scene cg smu_soul2 with dissolve

    "Только мы с Алисой знали, что настоящий Смутьянов сейчас под кроватью в баночке, сидит и не отсвечивает. То есть отсвечивает, тихим коричнево-зеленым светом."

    "Но мы завернули баночку в черную бумагу, которую выпросили в Славином фотокружке. И думаю, Смутьянов там, в темноте, просто дремал. Если, конечно, души умеют дремать."

    "Главное, чтобы этот бунтарь не выскочил и не воплотился в какое-нибудь другое, чужое тело."


    scene bg auhouse4 with dissolve

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Обновленный же Смутьянов молча слушал, не принимая участия в общих разговорах."

    "Охотно ел конфеты, даже спрятал несколько штук в карман. Наверное, он сильно оголодал после промываний, которые ему сделала Виола."

    "Внешне он совсем оправился, отказался от карантина, на котором настаивала наша доктор. Он вышел под наше поручительство. И за него по нашей просьбе похлопотала Ольга Дмитриевна."

    "Так он сидел, тихо слушая всё, о чём мы говорили. Потом он сказал, что ему НУЖНО. А мы с Алисой переглянулись и незаметно пошли за ним."


    scene bg toilet with dissolve

    "Когда Смутьянов вышел из нашего домика, он пошел на спортивную площадку, где стояли раздевалки и туалет."


    scene bg toilet2 with dissolve

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Подойдя к кабинкам туалета, разделенным на мужскую и женскую половины, он постоял некоторое время, оглянулся, словно хотел убедиться, что его никто не видит."

    "Затем направился к кабинке с буквой Ж и смело вошел в неё."


    scene bg toilet with dissolve

    show sp_al_046:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Вот так дела. Это точно не ОН. Это, скорее, ОНА."

    hide sp_al_046


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Помнишь, в архивах есть фотографии всех девушек, на которых были поставлены эксперименты? После них семеро выжили, но исчезли после взрыва."


    scene cg girls_archive with dissolve

    ul "Там еще на тех, кто не выдержали эксперимент, стояла печать «СДАНО В АРХИВ». А на этих печатей не было."

    pause (1000000000000000000000000.0)


    scene bg toilet with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Так, кажется, я начинаю понимать твою мысль. Если в тело Смутьянова воплотилась одна из душ девушек, то Смутьянов по идее должен среагировать на фото. Так мы узнаем, кто она."

    hide sp_al_005


    stop music fadeout 0.5

    queue music "audio/music/z_132.mp3"


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот именно! Я предлагаю прикрепить эти фото на доску в красном уголке, где висят фото ушедших на фронт воспитателей."

    ul "Так что, никто не заметит появления новых фотографий девушек в военной форме."

    hide sp_ul_012


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Но как заманить в красный уголок Смутьянова? Впрочем, кажется у меня есть идея. Наверняка эта душа будет интересоваться прошлым лагеря. Это же логично."

    al "Она сейчас молчит и осваивается. Но скоро начнет действовать."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Не будем забывать, что это такая же девушка-суперсолдат, как и Виола. В них же заложена программа..."

    hide sp_ul_013


    show sp_ul_050:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Убивать."

    hide sp_ul_050


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Из тела Смутьянова машина для убийства, как из дерьма пуля. Дрищ головастый. Куда ему."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А трансформация? Ведь у Эли все её части тела не железные. Я трогала. С виду вроде как шестеренки, но это точно не железо."

    ul "А в последнее время они стали как будто исчезать. Обрастать каким-то материалом, напоминающим кожу. Кажется, она постепенно меняется."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ты хочешь сказать, что в Эле тоже сидит чья-то душа и она трансформирует её под себя?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Не знаю. Пока я думаю, что это плод воображения кибернетиков."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Хм... Так-так, хорошо, будем внимательно наблюдать за всеми изменениями."

    al "Тихо, Смутьянов выходит. Прячемся."


    scene bg auhouse2 with dissolve

    "Вернувшись в домик, мы достали из архивных папок семь фото девушек и еще раз рассмотрели их."


    scene cg girls_archive3 with dissolve

    "Одна была совсем молодая, остальным было лет по восемнадцать, не меньше. Их звали Оля, Наташа, Вера, Антонина, Зоя, Галя и самую молодую Инга."


    pause (1000000000000000000000000.0)


    scene cg girls_archive2 with dissolve


    pause (1000000000000000000000000.0)


    ul "Инга — не русское имя."

    al "Она из Прибалтики. Только они там светлые, а эта, вроде, темненькая. Это или литовское или латышское имя. А может быть, эстонское."


    scene bg auhouse_crop1 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Будем окликать Смутьянова со спины этими именами. Возможно, он среагирует на одно из них."

    hide sp_ul_013


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "(Вздохнув) \nДа уж... Это было бы слишком просто. Но, как вариант. Я больше надеюсь на идею с фотографиями."


    scene cg girls_archive3 with dissolve

    "И мы не мешкая прикрепили фотографии в нашем красном уголке, на стенд БОЕВОЙ СЛАВЫ."


    scene bg library with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Мы застали Семёна в библиотеке. Усадив его напротив, мы выложили ему всё, что знали про лабораторию."

    "Семён долго молчал. Потом встал и начал ходить по библиотеке что-то обдумывая."

    sem "Вы ещё не всё знаете про Виолу. Но об этом потом. Еду ей всегда ношу я, в медпункт или в её домик. В столовой она не питается, потому что не доверяет тёте Любе."

    sem "Она вообще никому не доверяет. И заставляет меня попробовать, чтобы убедиться, что пища не отравлена. Я всё время снимаю пробу с её блюд. Это первое."

    sem "Что касается слияния с Пионером, то..."

    "Семён показал в пространство фигу."

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

    sem "Весь лагерь – это его маленькая планета, на которой он устраивает свои эксперименты-спектакли: восстания, войны. Погружает нас в пороки."

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

    sem "Да."

    hide sp_sem_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Так Пионер это не Пионер?"

    hide sp_ul_019


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Нет. Это личина. На самом деле, он Гендаков Владимир Геннадьевич, начальник проекта и с 1939 года руководитель лаборатории."

    sem "Он может менять внешность. Последнее время что-то у него не ладится. Потому и решил свернуть эксперимент."

    sem "Он заметно постарел за этот месяц. Последняя наша встреча была на отмели. Я поразился произошедшим с ним изменениям."

    sem "Страшно ощущать себя донором. Но пока Виола всё держит в своих руках, я не могу ни сбежать, ни как-то повлиять на ситуацию."

    sem "Если честно, я был в отчаянии. Хорошо, что я не один. Теперь я вижу, что у меня есть поддержка."

    sem "Но ещё месяц назад, приди вы ко мне с таким предложением, я с легкой совестью сдал бы вас Виоле. Очень многое произошло за это время."

    hide sp_sem_001


    show sp_sem_025:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Алиса, ты простишь меня? Ты же знаешь моё отношение к тебе."

    hide sp_sem_025


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Знаю. Не могу ответить тебе тем же, но простить смогу."

    hide sp_al_004


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Мне кажется, мы пришли к единому мнению относительно того, что нужно делать. Теперь все идем к Юле. Она сейчас на чердаке. Надо посвятить её в наш план."

    hide sp_ul_019


    scene bg attic2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


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


    scene bg opine2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_005.mp3"


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

    ul "Тогда вон там вижу один кустик."

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

    "Вскоре, помахав рукой сове, высунувшейся из дупла и громко крикнувшей, очевидно для острастки, мы побежали в лагерь, а сова удивлённо смотрела нам вслед."


    pause (100000000000000000000000000.0)


    scene bg dining with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


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


    scene bg medic_lib_ext with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Когда пришло время обеда, мы с замиранием сердца наблюдали, как Семён тащит разнос с едой в медпункт. Дверь за ним закрылась."


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Меня всю колотит. Только бы не сорвалось. Она точно заставит его пить. Семён вроде что-то принял перед этим?"

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

    "Прошло десять минут. На крыльцо вышел покачивающийся Семён."

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


    "Больше он ничего сказать не успел, так как его голова упала на грудь. Мы подхватили его и оттащили на лавочку неподалеку, где он и уснул."


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

    uv "Нет, но проспит долго."

    hide sp_iul_012


    scene bg watchmans_cabin_2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_201.mp3"


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


    scene cg vio_docs with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"



    "Когда мы открыли сейф, то увидели в нем папки и тетради. А также пачки отдельных листочков аккуратно перевязанных бечёвкой."


    scene cg vio_docs


    pause (10000000000000000000000.0)


    "Пролистав папки, мы поняли, что они содержат результаты экспериментов. А вот тетради были ни чем иным, как дневниками Виолы. Которые, как выяснилось, она аккуратно вела с 1942 года."

    "Тетрадки были очень толстыми. Помимо страниц в них были подшиты какие-то документы."

    "Но самым интересным для нас было то, что относилось непосредственно к нашему году. Именно это мы и решили прочитать, как только у нас окажется свободное время."


    scene bg medic_lib_ext with dissolve


    "А пока нужно было спешить. Оказывается, Виола успела сделать уколы почти всем отрядам. Из первого отряда не уколотыми были только мы с Алисой, Юля, Семён, Женя и Ольга Дмитриевна."

    "Также можно было рассчитывать на Элю. Остальные, двигались очень медленно, как будто в полусне."

    "Всё было продумано и судя по всему, процесс «тестирования» должен был начаться с часу на час."

    "Петрович предложил отнести Виолу на наш Чердак, потому что её точно будут искать в медпункте и библиотеке, а скорее всего, заглянут и в подвал."


    scene cg vio_final with dissolve

    "Мы тут же перетащили Виолу на чердак. Туда же позже мы переправили и Семёна."

    "Никто не знал, сколько ещё живых манекенов было у Гендакова. А то, что он будет не один, не вызывало сомнений."


    stop music


    play music "audio/music/z_207_1.mp3" noloop


    scene an_46_06 with dissolve

    "Во второй половине дня, тишину лагеря нарушил странный звук. Это скрипела поворачивающаяся статуя Генды."

    "Она развернулась, уставилась глазами-стеклышками на библиотеку и началась вибрация."


    stop music


    play music "audio/music/z_048.mp3"


    "Но в это раз она была вдвое сильнее обычной."


    stop music


    play music "audio/music/z_064.mp3" noloop


    #scene арт с манекенами и Гендой with dissolve
    
    scene bg gates with dissolve

    show sp_pi_010:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2


    "Тут же в лагерь через ворота механическим шагом вошли несколько манекенов, окружавших идущего в центре Пионера."


    stop music fadeout 0.5

    queue music "audio/music/z_151.mp3"


    "Он остановился и поднял руку. Все замолчали. Он медленно опустил руку и улыбнулся."


    stop music


    play music "audio/music/z_065.mp3" noloop
 

    image an_47_02: # Анимация трансформация Генды

        "images/an/an47day/an_d47_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/an/an47day/an_d47_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.1


    scene an_47_02 with dissolve


    "Затем раздался легкий хлопок и фигура стала похожей на серый расплывающийся человеческий силуэт"


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Видение длилось секунду, и вот перед нами стоял уже не пионер, хотя он был всё в той же белой рубашке с галстуком. Он был похож на изрядно постаревшего пионервожатого."

    "Но теперь у него было лицо ПАМЯТНИКА. Настоящий, живой Генда с бородкой и в очках."

    "Он стоял некоторое время, как бы наслаждаясь произведенным эффектом."


    scene bg medic_lib_ext3 with dissolve


    show sp_shu_001:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.8


    show sp_le_016:
        yalign -0.2 subpixel True
        xalign 0.60 subpixel True
        zoom 0.78


    show sp_tol_013:
        yalign -0.30 subpixel True
        xalign 0.74 subpixel True
        zoom 0.75


    show sp_mi_017:
        yalign -0.3 subpixel True
        xalign 0.29 subpixel True
        zoom 0.75


    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 0.8


    show sp_el_003:
        yalign -0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 0.8


    show sp_at_002:
        yalign -0.1 subpixel True
        xalign 0.88 subpixel True
        zoom 0.8


    show sp_elya_017:
        yalign -1.7 subpixel True
        xalign 0.02 subpixel True
        zoom 0.75


    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.12 subpixel True
        zoom 0.85


    show sp_iul_009:
        yalign -1.1 subpixel True
        xalign 0.67 subpixel True
        zoom 0.75


    show sp_ul_019:
        yalign -1.0 subpixel True
        xalign 0.39 subpixel True
        zoom 0.75



    "Все были не в силах сдвинуться с места."


#    $ show_quick_menu = False


    pause (10000000000000000000000.0)


    scene bg medic_lib_ext with dissolve

    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Только Алиса не потеряла своего всегдашнего самообладания."

    al "(Шёпотом) \nГендаков... Владимир Геннадьевич. Вот, значит, кто скрывался под личиной таинственного Пионера."


    scene cg silent_scene with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Мы знали, что для начала «тестирования» ему понадобится Виола."

    "Что собой представляло «тестирование», мы не знали. Но предчувствие было нехорошим."


    scene bg medic_lib_ext2 with dissolve

    "Генда что-то сказал одному из манекенов, а сам вошел в медпункт."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Никого не обнаружив, он задумчиво вышел со стулом в руке, поставил его и сел."


    pause (10000000000000000000000.0)


    ge "(Обращаясь к манекенам) \nСоберите все отряды. Постройте."

    ge "(Обращаясь к строящимся пионерам) \nГде Ольга Дмитриевна? Где Виолетта Церновна?"

    "Было странно, что несмотря на то, что до этого никто из пионеров Гендакова в живую никогда не видел, все беспрекословно подчинялись его приказам."


    scene bg gates with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.488 subpixel True
        zoom 1.1

    "Одна Ольга Дмитриевна смело вышла вперед. Мы не успели её удержать."


    scene bg medic_lib_ext with dissolve

    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Черт, мы ей не рассказали! Теперь будет плохо."


    scene bg gates with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.488 subpixel True
        zoom 1.1

    od "Кто вы такой? Почему мы должны следовать вашим распоряжениям? Я позвоню в райотдел. Я вызову милицию."


    scene cg od_mann with dissolve


    "Манекены молча стали у неё за спиной, схватив за руки. Она было попыталась вырваться, но вскоре затихла."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Ко я такой? Я ваш Бог!"


    scene bg genda2 with dissolve

    ge "А вот и мой памятник."

    "Генда рассмеялся неприятным скрипучим смехом."

    ge "По-моему, неплох. Хотя, ему не хватаем моего изящества, конечно. Ну уж какой есть. Вы должны были привыкнуть к моему лицу."


    scene cg silent_scene with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


    "Пионеры стояли и молча смотрели в землю. Все понимали, что происходит что-то насильственное, ужасное. И это отнимало у всех силы."

    "Какая-то неизбежность происходящего лишала воли. Как будто кто-то шептал: «Так надо. Смирись»."


    scene cg manns2 with dissolve

    "Манекены, обшарив все домики, заглянули в каждое хозяйственное помещение (один даже сбегал на лодочную станцию) и вернулись на площадь."

    "Они сообщили что ни Виолы ни Семёна в лагере нет."


    scene bg medic_lib_ext with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Стерва! Сбежала. Она лгала мне. Увлеклась молодым парнем. Я должен был это предвидеть. Но всё же... Нет, это невероятно."

    ge "Хотя... В любом случае, им обоим не выйти за границы ЗОНЫ. Жаль, у меня мало времени. Я насладился бы местью."

    ge "В таком случае, тестирование отменяется. И это плохо в первую очередь для присутствующих. Ваша доктор предала не только меня, но и вас!"

    ge "А вы?"


    scene cg silent_scene with dissolve

    "Генда обвел взглядом стоявших перед ним пионеров."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Вы могли бы стать ростками нового невероятного изобретения, новой жизни."

    ge "Вы прошли жесткий отбор! Созрели для того, чтобы из вас сделали настоящих солдат! Супер-солдат. Моих солдат! Осталось только провести последние тесты!"

    ge "И я взял бы вас с собой в новый мир. Теперь всё летит к черту. Точнее, вы летите к черту."


    scene bg medic_lib_ext with dissolve

    show sp_mann_002:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2

    "Генда подозвал старшего манекена."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Лагерь сжечь. Пионеров аннигилировать."

    ge "Да! \n(наморщил лоб как бы вспоминая что-то)"

    ge "Где эти чертовы сталкерши? Я их не вижу.\n(оглядывает толпу)"

    "Алиса присела на корточки за спинами ребят и потянула меня вниз."

    ge "Где Двачевская и Ленина?"

    ge "(Усмехаясь) \nВпрочем, при самоуничтожении Коллайдера они тоже погибнут. Взрыв не удастся пережить никому. Как и в прошлый раз."


    scene cg od_mann with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    od "Я ничего не понимаю. Если нам всем суждено погибнуть..."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Не всем. Я лично уйду в портал. А вам счастливо оставаться."


    scene cg od_mann with dissolve

    od "Какой портал? Вы хотите сказать, что Вы уйдете вот в такую вороночку, что показывают в фильмах? Такую, похожую на торнадо? Вы сумасшедший! Отпустите детей. И катитесь к черту."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Вороночку. Хм... Да, пожалуй, похоже на то. Ладно. К чему пустые слова?"

    ge "Жаль, что мой клон исчез. Но я найду нового. Там..."

    "Генда неопределенно махнул рукой в пространство. Затем посмотрел на часы."

    ge "Черт, заболтался! Процесс уже начался..."


    scene bg medic_lib_ext with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Надо тянуть время. Возможно, что-то удастся придумать. Вся надежда на Пионера. Ты говорила, что в трудный момент он может помочь. Кристалл с тобой?"

    hide sp_al_001


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да."

    hide sp_ul_019


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Быстро представляй себе Пионера! Проси, заклинай, делай что угодно, но что бы он появился. Сегодня вибрация особенно сильная, это должно сработать. А я отвлеку Гендакова."

    hide sp_al_001


    scene bg genda2 with dissolve

    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса вышла из-за строя, так, чтобы её видел Генда."

    al "Скажите, а где Пионер? Вы же не Пионер? Я не верю, что Вы это он."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Ой, кого я вижу, вся рыжая гвардия в сборе. Кто это прячется у тебя за спиной, не Ульяна ли?"

    ge "Да, признаюсь, создали вы мне проблем."

    ge "Значит, наша отважная малышка влюбилась... В Пионера. Это так трогательно."

    ge "Нет, я не Пионер. Этот персонаж нашего «спектакля» позорно бежал от моей кары. Но, думаю, ненадолго."

    ge "Я неоднократно перевоплощался, поэтому знаю все ваши тайны. Я мог бы стать кем угодно. Хоть вашей вожатой. Коллайдер творит чудеса."


    scene bg genda2 with dissolve

    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это называется массовый гипноз?"


    scene bg medic_lib_ext with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1002.mp3"


    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "Именно. В точку. Но гораздо сильнее. А ты любознательная... Впрочем, эти знания вы унесете с собой в могилу. Хех."

    ge "Ах, да... Я и забыл, после аннигиляции могил не будет. Горстка пепла."

    ge "«Но идущий за мною сильнее меня; я не достоин понести обувь Его; Он будет крестить вас ОГНЕМ». Это про меня, между прочим."


    scene bg genda2 with dissolve

    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "(Неожиданно выступая вперед) \nОн сказал — «Духом святым и Огнем»."


    scene bg medic_lib_ext with dissolve

    show sp_ge_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    ge "(Удивленно) \nОднако... Евгения Умнова, Браво!"

    "Генда иронично похлопал в ладоши."

    ge "Святым духом говоришь? Ну да, ну да. В каком-то смысле именно так."

    ge "Жаль, я не смогу аннигилировать вместе с тобой и твою мать. Бедняжка, она будет безутешна. Такое вот мое наказание."

    "Генда захохотал."


    image an_47_03: # Анимация появление портала

        "images/an/an47day/an_d47_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_51.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_53.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_54.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_55.webp" with Dissolve(0.5, alpha=True)
        pause 0.2


    scene an_47_03 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_735.mp3"


    "Неожиданно напротив ворот возник сначала бледный, но все уплотняющийся вращающийся шар, постепенно превращавшийся в воронку голубого цвета."

    "Воронка ширилась и росла, пока не стала величиной с наш домик."

    "У всех растрепались волосы и галстуки. Ветер, кажется, шел внутрь этой ДЫРЫ."


    scene bg medic_lib_ext with dissolve

    show sp_ge_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Гендаков встал, отшвырнул ногой стул."

    ge "Да, такую прекрасную оперу превратить в фарс!"


    scene an_d47_55 with dissolve

    show sp_ge_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Он шагнул к воронке."


    scene cg manns3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"

 
    "В руках у манекенов появились какие-то странные приборы, напоминающие водяные детские пистолеты."


    image an_47_04: # Анимация аннигиляторы

        "images/an/an47day/an_d47_63.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_64.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_65.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_66.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_67.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_68.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_69.png" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_71.png" with Dissolve(0.5, alpha=True)
        pause 0.2

        repeat 

    scene black with dissolve

    show an_47_04


    pause (10000000000000000000000.0)





    scene bg genda2 with dissolve

    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Аннигиляторы! Где Пионер?"

    hide sp_al_066


    show sp_ul_016:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я старалась..."


    scene cg genda_plate_07 with dissolve

    "Я посмотрела на памятник Генде. Табличка под ним была открыта. Алиса перехватила мой взгляд."


    scene bg genda2 with dissolve

    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Как только он шагнет, врубаем СТОП КРАН!"

    hide sp_al_001


    "Мы бросились к памятнику. Зная брезгливость Генды, мы догадались, что манекены не начнут аннигиляцию раньше, чем он исчезнет (как произошло в тот раз в лаборатории)."


    scene an_d47_55 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_048.mp3"


    show sp_ge_001:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Генда обвел лагерь задумчивым взглядом, немного постоял, затем решительно шагнул в портал."


    image an_47_05: # Анимация Генда уходит в портал

        "images/an/an47day/an_d47_56.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_57.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_58.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_59.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_60.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_61.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_62.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_54.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.2
        "images/an/an47day/an_d47_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.2


    scene an_47_05 with dissolve


    pause (10000000000000000000000.0)


    "Портал тут же растворился. Через несколько секунд уже ничего не напоминало о его существовании. Ветер неожиданно прекратился."


    scene cg manns3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"


    "Манекены некоторое время еще смотрели на место, в котором исчез их бог, потом повернулись к пионерам, наводя на них свои «пистолетики»."


    scene an_46_12 with dissolve

    "Я упала на рубильник одновременно с Алисой. Рубильник поддался и ушел вниз, табличка захлопнулась. Однако вибрация не прекратилась."


    scene bg genda2 with dissolve

    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Еще действует! Думай, Ленина, думай! Ну хоть на что то годится же твой кристалл!"

    hide sp_al_007


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да! Сейчас."


    hide sp_ul_013


    show sp_ul_017:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я сосредоточилась, представляя себе бессильно падающих манекенов, у которых из рук выпадают аннигиляторы."

    "Но, кажется, я перестаралась. Они не просто падали, а лопались, как мыльные пузыри."

    "Пионеры бессильно садились на землю. Уколы всё ещё действовали. Однако, им хватило сил крикнуть вялое «Ура»."


    scene an_d47_39 with dissolve

    show sp_pi_007:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Появился Пионер. Он тяжело дышал."


    scene cg ul_pi_gates with dissolve

    "Я бросилась к нему."

    ul "Ну где же ты был!"

    pi "Я успел?! Думал, вас уже никого не застану в живых!"

    pi "Где Генда?"


    scene bg genda2 with dissolve

    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Исчез в портале."

    hide sp_al_007


    show sp_sem_022:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "На площади появился Семён. Он молча подошел и пнул ногой лежащий манекен."

    sem "Что у вас тут произошло?"

    hide sp_sem_022


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Финал спектакля под названием «Лагерь Совенок в объятьях Хаоса»."

    al "А Где Виола? Надеюсь, она еще не очнулась?"

    hide sp_al_004


    show sp_sem_022:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Нет, я был один на чердаке."

    hide sp_sem_022


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Сбежала! Вот хитрая бестия!"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Значит, она могла, но не стала помогать Генде!"

    hide sp_ul_013


    show sp_sem_022:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Я думаю, у нее была своя игра, и она изначально не собиралась ему помогать. Впрочем, это только мои предположения. Теперь это уже не имеет значения."

    hide sp_sem_022


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Подошла Ольга Дмитриевна."

    od "Кто объяснит, что это было? Оживший памятник, портал, манекены, аннигиляторы..."

    od "Бред какой-то. Или я уже схожу с ума... Мало нам вчерашней бойни, пожаров и потрясений."

    hide sp_od_022


    show sp_pe_005:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "К группе подошел запыхавшийся Петрович."

    hide sp_pe_005


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    od "Архип Петрович, а Вы где были, когда были так нужны! Где, наконец, Любовь Никаноровна?"

    hide sp_od_022


    show sp_pe_005:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "(Обращаясь к Пионеру) \nНу здоров же ты бегать, малец. За тобой не угнаться."

    pe "(Повернувшись к ОД)\nБыл там, где нужно."

    pe "Мы вот с ним (кивает на Пионера) кончали эту штуковину. Рванули там всё. Нет больше лаборатории. Самоуничтожения этого и взрыва не будет."

    pe "Мы снесли механизм самоуничтожения, но не смогли остановить машину. Она там под развалинами. Всё ещё работает."

    hide sp_pe_005


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    od "А где Любовь Никаноровна? Кто-нибудь её видел?"

    hide sp_od_022


    show sp_pe_005:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Запер ее в бытовке. Сказал ей не высовываться, пока все не кончится. Пойду, отопру."

    hide sp_pe_005


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "И что теперь, эта машина, ну Коллайдер, так и будет работать? Зачем были все эти жертвы?"

    hide sp_al_004


    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pi "Нет, не будет. Как давно исчез Портал? После закрытия Портала машина будет работать еще несколько минут. У вас есть возможность..."

    "Пионер запнулся."

    pi "Загадать последнее желание. Пока не прекратилась вибрация."

    pi "Вы все или кто-то из вас должны что-то пожелать. Или ничего не желать, постарайтесь не думать ни о чём, пока вибрация не остановится."

    hide sp_pi_001


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "В таком случае... Ольга Дмитриевна, говорите с пионерами. Отвлеките их, они не должны ничего желать. Пока они Вас слушают, их мысли будут сосредоточены на Вас. А нам тут надо быстро посоветоваться."

    hide sp_al_005


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    od "Поняла. Хоть я во всё это всё равно не верю, но я уже не раз убеждалась, что вы знаете больше меня."

    "ОД посмотрела на Семёна."

    od "И я надеюсь, вы знаете, что делаете."

    hide sp_od_022


    "Повернувшись, Ольга Дмитриевна пошла к стоящим на площади пионерам второго и третьего отряда."


    scene bg camp_artifacts with dissolve

    "Вдруг, передо мной в одно мгновение пронеслись все эти дни, что мы провели в лагере."

    "И я подумала. Всё, что произошло за последние три часа, можно было назвать сплошным кошмаром. Из-за работы Коллайдера все мысли находящихся в Зоне людей обретали физическое воплощение."

    "Мысли были разные. Безумные, странные, тусклые, обыденные. Иногда абсурдные. Но, какие бы они ни были, они тут же материализовались."

    "Как те манекены на складе, ожившие благодаря пьяному бреду Петровича и выступившие в проход, как деревянные солдаты Урфина Джуса."

    "Вспомнилось, как Тузик гонит Долговязого, и разрывает его."

    "Мысли и мечты кибернетиков, оживившие кибердевочку Элю."

    "Теперь она стояла воплощенная, как Галатея. Живая, обнимающая Электроника и быстро что-то говорящая ему своим синтетическим, лишенным эмоций, голосом."


    scene bg genda2 with dissolve


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса прикрикнула на Элю с напускной суровостью:"

    al "Молчи, железяка! Мы тут как бы пытаемся сосредоточится, а ты мешаешь."

    hide sp_al_007

    "Наступила тишина, нарушаемая только мягким гулом вибрирующей под ногами площади и голосом ОД, что-то говорящей пионерам."


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса повернулась к Пионеру."

    al "Какая у нас есть возможность? Напомни еще раз."

    hide sp_al_005


    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pi "Загадать последнее желание, пока вибрация не закончилась. Кристаллы с вами?"

    hide sp_pi_001


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, мой кристалл всегда со мной."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса о чём-то пошепталась с членами отряда, те кивнули, и Алиса выступила вперёд."

    hide sp_al_005


    stop music fadeout 0.5

    queue music "audio/music/track7.mp3"


    show sp_al_066:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ульяна, мы решили. Сейчас у нас осталось, если верить Пионеру, не больше двух-трёх, минут. Слава богу, что всё, наконец, закончится."

    al "Так вот. Мы все решили, что эти последние минуты мы НЕ БУДЕМ ДУМАТЬ НИ О ЧЁМ! Это трудно, очень трудно, не думать. Но мы попробуем."

    al "Мы оставляем последнее желание за тобой. Потому что знаем, ты самая чистая из нас, ты не можешь пожелать плохого."

    al "Ты ещё ребенок, и твои мечты и детские образы не принесут никому вреда, даже если ты вдруг и продумаешь о чём-то не том."

    al "Сосредоточься пожалуйста, у тебя есть минута, подумай о хорошем. Когда портал закроется, ничего нельзя будет уже исправить. Ну же! Быстрей!"


    scene bg medic_lib_ext2 with dissolve

    show sp_ul_017:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я сосредоточилась. Я старалась не думать о своих мечтах, я хотела что-нибудь для всех."

    "Я думала о нашей будущей взрослой жизни, которая пугала меня, о том, что я потеряю своих друзей, и они рано или поздно станут старше, а потом станут старичками и умрут."

    "И мне стало страшно. И я закрыла глаза и закричала:"

    "ПУСТЬ ВСЁ В ЛАГЕРЕ БУДЕТ, КАК В ПЕРВЫЙ ДЕНЬ, НО ВСЕ ПИОНЕРЫ НАШЕГО ОТРЯДА БУДУТ СОВЕРШЕННОЛЕТНИМИ И НЕ БУДУТ ЗАВИСЕТЬ ОТ ВЗРОСЛЫХ!"

    "И ПУСТЬ НАВСЕГДА ОСТАНУТСЯ ТАКИМИ ЖЕ ЮНЫМИ, А ЛЕТО ВЕЧНЫМ И МЫ БУДЕМ ДРУЖИТЬ! И ТАК БУДЕТ ВСЕГДА, ПОТОМУ ЧТО МЫ, НАКОНЕЦ, НАШЛИ СВОЙ ДОМ!"

    hide sp_ul_017

    "Через пару секунд вибрация исчезла. Все ждали взрыва, о котором говорил Генда-Гендаков."


    stop music fadeout 0.5

    queue music "audio/music/z_066.mp3"


    "Но вместо него вдруг раздался страшный звук, от которого все присели и схватились за голову. Казалось, наши барабанные перепонки вот-вот лопнут."

    stop music

    "Потом наступила какая-то звенящая тишина."


    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    "Я посмотрела на Пионера. Он что-то говорил, но я видела только двигающиеся губы."

    hide sp_pi_001


    "Через какое-то время свист в ушах стал стихать."

    "Между тем, произошло что-то странное... Сначала никто не мог понять, что. Но потом поняли, что всё окружающее нас странным образом изменилось."


    scene bg medic_lib_ext2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    "Каждый, стал как будто выше, лица приобрели осмысленное, взрослое выражение."


    scene bg medic_lib_ext2 with dissolve


    show sp_shu_006:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_el_008:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "Кибернетики возмужали."


    scene bg medic_lib_ext2 with dissolve

    show sp_iul_016:
        yalign 0.07 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1


    show sp_mi_026:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    "Юля стала вровень с Мику."


    scene bg medic_lib_ext2 with dissolve

    show sp_at_022:
        yalign 0.00 subpixel True
        xalign 0.9 subpixel True
        zoom 1.0


    "Глаза Атсуи больше не смотрели по-детски наивно, а вместо этого зажглись особым, восхитительным блеском."


    scene bg medic_lib_ext2 with dissolve

    show sp_sl_029:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.35


    "Бёдра Слави округлились, а грудь стала больше."


    scene bg medic_lib_ext2 with dissolve

    show sp_al_067:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "У Алисы исчезло ребяческое, вызывающее выражение лица, а в её и без того выразительных глазах появилась какая-то огромная глубина и мягкость."


    scene bg medic_lib_ext2 with dissolve

    show sp_je_020:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3


    "Женя расцвела и превратилась в стройную высокую девушку без признаков всегдашней робости и смущения."


    scene bg medic_lib_ext2 with dissolve

    show sp_le_023:
        yalign 0.08 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Ну а Лена стала просто красавицей!"


    scene bg medic_lib_ext2 with dissolve

    show sp_tol_016:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.4

    "Толик же, помолодел. Это не был больше пожилой лысый мужчина. Его лоб окаймляли милые кудряшки, а на лице застыло какое-то удивленное, детское выражение."


    scene bg medic_lib_ext2 with dissolve

    show sp_sem_027:
        yalign 0.07 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Только Семён ничуть не изменился."

    "Некоторое время все молчали. Затем лица вытянулись и рты открылись. Все разглядывали других, не зная что изменились сами."


    scene bg medic_lib_ext2 with dissolve

    show sp_al_068:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса резко повернулась ко мне:"

    al "ЧТО ТЫ СДЕЛАЛА!? О ЧЕМ ТЫ ПО…"

    "Она осеклась."

    al "Боже, Ульяна, твоя грудь!"


    scene bg medic_lib_ext2 with dissolve

    show sp_ul_054:
        yalign -0.02 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve


    "Я опустила глаза и вдруг поняла, что первый раз не вижу своего живота из-за двух внушительных холмиков, выпирающих из-под рубашки."

    "Я взялась за них, чтобы убедиться, что это не обман зрения. Они были НАСТОЯЩИМИ!"

    "В голове откуда-то из прошлого, зазвучал далекий голос Алисы: «Не спеши, маленькая, когда-нибудь и у тебя будут такие же»."


    scene bg medic_lib_ext2 with dissolve


    show sp_sem_027:
        yalign 0.07 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Я увидела глаза Семёна. В них больше не было братского, ироничного прищура, а только удивление, смешанное с восхищением, как если бы он вдруг увидел меня впервые."

    hide sp_sem_027


    scene cg ul_grownup with dissolve


    pause (100000000000000000000000000.0)


    "Я шагнула к нему, вложила свою ладошку в его большую руку и первый раз посмотрела на него не снизу вверх, а потом сказала голосом, который сама едва узнавала:"

    ul "Ну что, «братик», теперь у тебя есть возможность выполнить своё обещание. Помнишь? «Если бы ты не была мне как сестра»."


    scene cg ul_sem_hands with dissolve


    pause (100000000000000000000000000.0)


    "Я почувствовала, как его пальцы сжали мою ладонь."

    sem "Помню."


    scene cg_bikers with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_111.mp3"


    "На площадь перед памятником, рыча моторами, въехала колонна мотоциклистов, и, сделав круг, остановилась."

    "Знакомая длинноволосая фигура в кожаном комбинезоне приветственно подняла руку."


    scene bg genda2 with dissolve

    show sp_al_069:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Все повернулись к Алисе. Она буквально излучала свет."

    "Наверное, никакой коллайдер не смог бы преобразить человека так, как преображает его ощущение счастья. А это, несомненно, было ОНО."


    scene cg_bikers with dissolve

    "Мотоциклисты сделали круг, помахали нам на прощанье и, выехав за ворота, умчались по дороге в поселок."


    scene cg jean_square with dissolve

    "На площади остался только один мотоцикл. На нем сидел Жан. И улыбался во всю физиономию."


    pause (100000000000000000000000000.0)


    scene bg genda2 with dissolve

    show sp_ul_054:
        yalign -0.02 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Что же ты стоишь как столб? Вот глупая. Беги! Он же ждет!"


    scene cg jean_square with dissolve

    "Алиса рванулась к Жану, потом остановилась, кинулась ко мне. Мы обнялись в последний раз."

    "Подбежали девочки отряда. Это была сцена расставания. У всех были слезы, все обнимали и тихо на ушко поздравляли Алису. Это же как в сказке!"

    "Жан махнул нам рукой на прощанье, Алиса тоже. И они умчались. Так я потеряла подругу, как мне казалось. Ведь мы прежде строили планы, как будем вместе."

    "Но счастье, оно такое... Его на всех не хватает. Я знаю Алису, она обязательно появиться. Ведь мы — неразлейвода. В общем, я ревела."


    scene bg gates_buses with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_068.mp3"


    "Раздались гудки подъезжающих автобусов."


    stop music fadeout 0.5

    queue music "audio/music/z_069.mp3"


    "Из крайнего высыпали люди. Родители и пионеры двинулись навстречу друг другу."


    show sp_mp_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    "Возгласы радости перекрыл пронзительный голос Маргариты Павловны."

    mp "Что за анархия? Потом сантименты! Ольга Дмитриевна, организуйте группы!"

    mp "Все собираем вещи, ничего не забываем и дисциплинированно грузимся в автобусы! Надо пересчитать детей!"



    scene bg medic_lib_ext2 with dissolve

    show sp_je_020:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3

    "Женя, грустно глядя на всеобщую суету:"

    je "Ну да... Мама как всегда рулит. Как будто в последний день без этого было нельзя обойтись."

    hide sp_je_001


    scene bg medic_lib_ext2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_179.mp3"



    show sp_sl_030:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.35


    show tripod:
        yalign -1.0 subpixel True
        xalign 0.45 subpixel True
        zoom 0.8



    "Появилась Славя, неся треногу с фотоаппаратом."

    sl "Так, минуточку! Стоп! Надо сделать общее фото! Такого случая больше не будет! Первый Отряд! Все построились в две линии."

    sl "Алиса, приглашай Жана и становитесь во второй ряд. Да, Элю и Юлю тоже к нам!"

    sl "Саша! Саша Бременская! Ты чего там в сторонке? Становись, ты же наша теперь."

    sl "Ольга Дмитриевна, Любовь Никаноровна! Петрович! Давайте с нами!"


    scene bg genda2 with dissolve

    show sp_ul_054:
        yalign -0.02 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Пионера забыли!"

    hide sp_ul_054


    scene bg medic_lib_ext2 with dissolve

    show sp_sl_030:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.35


    show tripod:
        yalign -1.0 subpixel True
        xalign 0.45 subpixel True
        zoom 0.8

    sl "Да и Пионера тоже сюда."

    sl "Так... Стали?"

    hide sp_sl_030 with moveoutright

    "Славя запустила таймер на фотоаппарате, подбежала и стала ко всем."

    scene cg group_photo with dissolve


    sl "А теперь все дружно улыбнулись и сказали СЫЫЫЫЫЫР!"


    stop music


    play miscSounds "audio/music/z_071.mp3" noloop


    play music "audio/music/z_070.mp3"


    scene cg group_photo2


    with flash


    $ renpy.pause(1.0, hard=True)


    stop miscSounds


    scene cg group_photo3 with slowdissolve


    $ renpy.pause(3.0, hard=True)


    scene cg group_photo3


    pause (10000000000000000000000.0)


    scene black with fade


    stop music fadeout 1.0


    jump day48

return