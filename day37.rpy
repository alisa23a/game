label day37:

    $ days = 37

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_477.mp3"


    scene cg longboat_repaired with dissolve

    "Баркас был готов. Как сказал Семён, которого все негласно считали за капитана, «Нужно провести ходовые испытания»."

    "И вот, рано утром, ещё до подъёма, команда нашего «Смелого» (так мы назвали баркас) выгрузилась на острове, чтобы сделать пробное плавание."

    "Пришлось немного повозиться, чтобы столкнуть его в воду. Но всё же нам это удалось. И он, как говорят в таких случаях, «закачался на волнах». А мы крикнули «УРА!»."

    "У нас была мачта и парус, пошитый Леной в страшной тайне ото всех посторонних."


    scene cg longboat_first_ride with dissolve

    "Мы решили не рисковать и отвели баркас ближе к отмелям на веслах на тот самый берег, где мы с Алисой бегали голышом. Там была небольшая бухточка."

    "А главное, туда никто бы не попал, так как пришлось бы долго идти по берегу реки со стороны старого лагеря."

    "А мы на лодке быстро вернулись назад в «Совёнок» и даже успели на утреннюю перекличку."


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

    ul "Семь раз. Я конечно могу и больше."

    hide sp_ul_013


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Верю, верю."

    hide sp_od_024

    "И на этом от нас отстали."








    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day38

return