label day48:

    $ style.say_window = style.window

    $ days = 48

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_47_00 = True
    $ im_gal_47_01 = True
    $ im_gal_47_02 = True
    $ im_gal_47_03 = True
    $ im_gal_47_04 = True
    $ im_gal_47_05 = True
    $ im_gal_47_06 = True
    $ im_gal_47_07 = True
    $ im_gal_47_08 = True
    $ im_gal_47_09 = True


    show screen current_day with fade


    #play music "audio/music/z_181.mp3"
    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_067.mp3"


    "Ещё два дня я была в лагере. Я вспомнила, как все грузились в автобусы. В какой-то страной спешке."


    scene cg le_bus with dissolve

    "И Лену, которая с огромными глазами металась по автобусу и всех спрашивала: «ГДЕ Семён?»"


    pause (10000000000000000000000.0)


    scene bg camp_artifacts with dissolve

    "После отъезда второго и третьего отрядов, а также Мику, Лены, Киберентиков и Слави, в лагере наступила непривычная тишина."


    scene bg square2 with dissolve


    pause (10000000000000000000000.0)


    scene bg stadium2 with dissolve


    pause (10000000000000000000000.0)


    scene bg stage6 with dissolve


    pause (10000000000000000000000.0)


    scene bg boat_station2 with dissolve


    pause (10000000000000000000000.0)


    scene bg camp_artifacts with dissolve

    "Никто не гонял в футбол, не купался а пляже. Сиротливо смотрелись вывески кружков."


    scene cg patyvan with dissolve

    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Приехали приглашенные Маргаритой Павловной рабочие, чтобы отремонтировать наполовину снесенную взрывом сторожку Петровича. А также два милиционера с собакой, один из которых был следователем."

    "Они долго выспрашивали про обстоятельства исчезновения Тараса Юрьевича, провели розыскные действия, которые ограничились поисками «тела» вдоль периметра лагеря. Но собака след не взяла."


    scene cg cop with dissolve

    "А перед тем как уехать, этот, что со следователем, здоровенный такой, как сказал бы мой папа, «с протокольной мордой», подошел ко мне (а я на лавочке сидела), и хитро улыбаясь так, говорит:"


    "«Тебе, девочка, точно нечего мне рассказать? Учти, мы же все равно все узнаем»."

    "Я спросила: «Это что, допрос?» И наверное, у меня было такое лицо, что он как-то замялся, перестал улыбаться и сказал ОД: «Ну и пионеры у вас». И ушёл злой."


    scene bg camp_artifacts with dissolve

    "Так они и уехали ни с чем."

    "Тузик тоже в лагерь не вернулся."


    scene cg smu with dissolve

    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Последними приехали родители Смутьянова. Он держался отстранённо, как бы не узнавая их, и все время молчал. Обеспокоенные, они посадили его в свою машину «Москвич» и уехали."


    scene bg camp_artifacts with dissolve

    show sp_smu_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "А через два часа я снова увидела Смутьянова, прошмыгнувшего мимо меня в сторону склада."

    "Судя по всему, от родителей он убежал. Они снова приехали, расспрашивали всех и расстроенные уехали."

    "Они же не знали, что Смутьянов в баночке. Никто кроме меня не видел, как он прятался. А я никому не сказала."


    scene bg camp_artifacts with dissolve


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2


    show sp_sb_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Кроме  меня, из наших в лагере была Женя, Юля и Саша Бременская, которая сказала, что домой не поедет."


    scene bg camp_artifacts with dissolve


    show sp_elya_017:
        yalign -0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0


    show sp_sb_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Элю и Сашу на следующий день Юля увела в свое убежище."

    hide sp_elya_017 with dissolve


    "Но родители Саши все-таки приехали, и пришлось ее «выдать»."


    scene cg od_sad with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_480.mp3"


    "Ольга Дмитриевна выглядела какой-то расстроенной. Срок её стажировки закончился, но МП  уговорила её остаться на пару дней."


    scene bg camp_artifacts with dissolve

    "Семёна после того памятного дня никто не видел. Он как в воду канул. И родители за ним не приехали."


    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Перед тем, как исчезнуть, он подошел и сунул мне в руки конверт. Попросил не открывать его до вечера."


    scene cg sem_letter with dissolve

    "Но я, конечно, не выдержала и открыла."


    pause (10000000000000000000000.0)


    scene cg sem_letter2 with dissolve

 
    pause (10000000000000000000000.0) 


    "Там было странное письмо. Из него следовало, что Семён не может остаться, но обязательно меня найдёт."

    "Что-то про время и про автобус который «больше не работает как портал». Всё это было очень загадочно и непонятно..."


    scene cg ul_sad with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1012.mp3"


    "У меня сжалось сердце. Я подумала, что наверное, никогда больше его не увижу. А нам так о многом надо было поговорить."



    "Мне надо было задать ему главный вопрос. Я даже в голове сочинила целую речь. Но... Вот, все зря. И на следующий день он тоже не появился. И я ревела у нас в домике."


    stop music fadeout 0.5

    queue music  "audio/music/z_055.mp3"


    "И вспоминала..."


    play miscSounds "audio/music/z_111.mp3"


    "Вспоминала, как мы обнимались и ревели под рев двигателя."

    stop miscSounds

    "Сильнее чем когда мы провожали Саманту."

    "А Алиса сказала: «Не надо. Долгие проводы, лишние слезы. Иди в домик»."


    scene cg ul_window with dissolve

    "И я убежала, но потом все равно у окна смотрела. И они укатили, и она ещё махала мне долго, пока мотоцикл совсем не скрылся."

    "Это, как сказал бы папа, была «большая трагедия»."

    "Мы конечно все обменялись адресами и будем писать друг другу. А ещё договорились на следующий год приехать сюда уже вожатыми. Мы же будем комсомольцы."

    "Но все равно, очень грустно."

    pause (100000000000000000000000000.0)


    scene cg ul_bed with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"



    "Было одиноко без Алисы, и я так ревела, что уснула."


    pause (10000000000000000000000.0)


    scene black with fade


    stop music fadeout 1.0


    jump day49

return 