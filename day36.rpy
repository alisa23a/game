label day36:

    $ days = 36

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_076.mp3"


    scene bg camp_artifacts with dissolve


    "По случаю поимки Большого Сома, в лагере было решено устроить праздник. Это была инициатива дирекстрисы."


    scene cg stage_catfish with dissolve

    "Дети сделали из картона чучело Большого Сома и водрузили его на площадке перед Сценой."

    "Потом был конкурс стихов малышей на тему подвига победы над Чудищем и конкурс «Рисунок на асфальте», где героев и сома изображали цветными мелками. Победителям вручали призы."


    scene cg festive_dinner with dissolve

    "Был праздничный обед, на котором подали рыбные блюда. История с Сомом стала частью истории лагеря."


    stop music fadeout 1.0


    play music "audio/music/z_197.mp3"


    scene bg oldcem6 with dissolve

    "Нам не давала покоя история с магией и куклой. И мы с Алисой решили после обеда еще раз сходить на кладбище."

    "Кроме оплавленных свечей и пентаграммы, мы нашли и то, чего сначала не заметили. В золе костра мы обнаружили остатки рыжих волос, которые были аккуратно связаны в косичку."

    "Именно то, что они были в косичке, и сохранило их от полного сгорания."


    scene cg pentagram with dissolve

    "Алиса долго рассматривала пентаграмму, а потом наклонилась и соскребла белую краску, которой она была нарисована. Внимательно разглядывая её, она вдруг сказала:"


    scene bg oldcem6 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это свинцовые белила. Такие используют художники. Много у нас в лагере художников?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет. Лена хотела вести кружок ИЗО, но она не сделала объявления по группам, и к ней ходил только Семен. В основном же, она рисует сама."

    ul "Часто ходит на «пленэр», как она это называет, на реку. Или рисует лес и горы. Два раза Семен ей позировал."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Так, теперь давай сопоставим все имеющиеся у нас факты."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"


    scene cg woodoo_doll with dissolve

    "Кукла сшита профессионально, а шьет у нас только Лена."


    scene cg lena_painter with dissolve

    "Краски художественные и хранятся они только у Лены."


    scene cg oldcem_figure with dissolve

    "Издалека плохо было видно, но всё же это была молодая девушка, а не женщина. Скорее всего, подросток."


    pause (10000000000000000000000.0)


    scene cg grass_magic with dissolve

    "Лена брала у Жени книги по травам, колдовству и магии."


    scene cg woodoo_doll with dissolve

    "Кукла с рыжими волосами, это мы с тобой. Только у нас во всем лагере (ну кроме Васи) рыжие волосы."

    "Тебя она не ревнует к Семену, остаюсь только я."


    scene bg oldcem6 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Значит, порчу наводили на меня. И наводила её Ленка. Мотивация была только у неё. Именно она и приходила ночью на кладбище!"

    al "Вот только где она взяла мои волосы?"

    al "Я вроде стриглась в первый день. Боже, я вспомнила! Меня же стригла Ленка!"


    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно, это она! Больше некому!"

    hide sp_ul_013


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Вот и попалась наша Леночка. Дружба дружбой, но желать человеку зла, болезней или смерти, это уже чересчур."

    hide sp_al_001


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Мы не ябеды. Надо дать человеку шанс исправится."

    hide sp_ul_013


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Это понятно Но.. Представь, она тут волхвует на моё здоровье, вон сколько булавок воткнула в куклу, а мы ей шанс?"

    hide sp_al_001


    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Даже если она раскается, то я ее вряд ли прощу. Как мы потом вообще будем жить вместе после того, что произошло? Об этом ты подумала?"

    hide sp_al_002


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но ОД не скажем."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Естественно."

    hide sp_al_004


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"


    scene bg auhouse2 with dissolve

    "Вечером к нам зашла Мику."





    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day37

return