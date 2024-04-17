label day45:

    $ days = 45

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music


    play music "audio/music/z_412.mp3"


    image an_45_01: # Анимация Ульяна плачет прощание с Самантой

        "images/an/an45day/an_d45_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an45day/an_d45_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat

    show an_45_01

    pause (10000000000000000000000.0)


    scene an_d45_04 with dissolve

    "Никогда я столько не ревела... Мы прощались с Самантой."


    scene bg camp_artifacts with dissolve

    show sp_od_023:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    "Ольга Дмитриевна хотела сказать речь, но заплакала."

    "Она плакала, но все-таки нашла в себе силы выразить благодарность Мегги и Саманте за участие в жизни лагеря и за их вклад и участи в игре «Зарница»."

    "(Про «Зарницу» я потом напишу, там много писать.)"

    hide sp_od_023


    show sp_sam_001:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    "Да.. Саманту любил весь лагерь. Даже малыши, перед тем как  уехали недавно, тоже тогда плакали и каждый считал необходимым подбежать к ней, обнять и сказать что-то хорошее."


    scene cg sem_sam_hugging2 with dissolve

    "Дольше всего Саманта прощалась с Семёном. Он держал ее за подбородок а она смотрела на него во все глаза. И все отошли в сторону, чтобы не мешать им."


    scene bg camp_artifacts with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса посмотрела на меня:"

    al "Когда они успели так близко сойтись?"


    scene cg sem_sam_hugging2 with dissolve

    "Этот же немой вопрос застыл в глазах и у других девочек. Однако Семён, прощаясь, поцеловал Саманту в лоб, как меня тогда, на Тропе украденной котлеты. Она ревела."


    scene bg sam_minibus with dissolve

    show sp_sam_001:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    "Но ее мягко но настойчиво вели в машину... Машина была красивая. Бело-голубой микроавтобус, не то что наш скромненький ПАЗик." 

    hide sp_sam_001 with dissolve


    "В машине ещё сидели какие-то люди в костюмах. Как сказала Алиса, «гебешники». Что это такое, я переспрашивать не стала."


    scene bg road with dissolve

    "Все дружно замахали руками, когда машина тронулась, и махали, пока она не скрылась за поворотом."

    "Наш отряд стал меньше на одного друга."

    "Все были в смешанных чувствах."


    stop music


    play music "audio/music/z_023.mp3"


    scene bg attic2 with dissolve

    "И мы решили собраться на чердаке, поговорить о событиях последних трех дней. Слишком много всего случилось."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Но когда мы собрались, то на чердаке вдруг появилась Ольга Дмитриевна. Как она узнала про чердак?"

    hide sp_od_022


    show sp_tol_007:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    "Все посмотрели на Толика. Но у него было такое лицо, что всем стало ясно – ЭТО НЕ ОН."

    hide sp_tol_007


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Я вижу, вся честная компания уже собралась. Ну и лица у вас! Не бойтесь, ничего вам не будет."

    od "Я давно знаю про ваше убежище. Теперь ясно, кто утащил у Тараса Юрьевича его диван. Давайте договоримся, ведь мы одна команда. Или вы мне доверяете или нет."

    od "Напоминаю, что я прикрыла вас, когда шло расследование по поводу всех ваших ЧП, хотя прекрасно знала о них. Никто не вылетел из лагеря."

    od "Ну так что, будем, наконец, дружить или как?"

    hide sp_od_024


    "Все облегченно вздохнули. Ольга Дмитриевна раскинула руки, как бы приглашая всех обниматься. Что мы с радостью и сделали."

    "Это была прекрасная сцена. У всех ещё стояли слезы по поводу отъезда Саманты, а тут такое! И мы снова ревели. Вспоминали наши приключения..."


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса, тем не менее, как всегда, нашла время для шутки."

    al "Семья воссоединилась, товарищи! Бурные аплодисменты!"

    hide sp_al_005


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Надеюсь, Алиса, ты сказала это без обычного сарказма?"

    hide sp_od_024


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Покраснев) \nДа нет, конечно! Я правда рада. Просто... Вы же мне тогда сказали про досье. Ну я как бы думала, что Вы не на нашей стороне. Ну какое-то время."

    hide sp_al_004


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Я обязана была провести с тобой воспитательный процесс. Ты должна меня понять и простить."

    od "Вспомни, какая колючая и ершистая ты приехала в лагерь. Мне тоже было не легко с вами."

    od "Ты доставляла больше всех хлопот. Но я тебя отстояла в тот раз перед Маргаритой Павловной. Ты же знаешь."

    hide sp_od_024


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    je "Ольга Дмитриевна, это же Алиса. Не берите в голову."

    hide sp_je_001


    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Да, Ольга Дмитриевна. Она так не думает. Просто она у нас немножко вредина."

    hide sp_sl_001


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну спасибо, Ясенева! Я, значит, теперь вредина. Ты же моя подруга. Ну была, точно."

    hide sp_al_004


    show sp_mi_015:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    mi "Девочки, не будем ворошить прошлое. Тем более что эта история с палаткой давно уже всеми разобрана по косточкам."

    mi "Все знают, что Семён просто перепутал палатки. Поэтому и уснул в Алисиной. А ты, Славя, вечно всё драматизируешь."

    hide sp_mi_015


    stop music


    play music "audio/music/z_197.mp3"


    show sp_sl_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Что значит, «всеми разобрана по косточкам?» Давайте отсюда, пожалуйста, поподробнее. Я рассказала только тебе. Ах ты, водоросль японская, вот значит как ты хранишь тайны!"

    hide sp_sl_006


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    mi "Все знают, что у меня «язык помело». Я не удержалась. Не надо было мне рассказывать. И к тому же, они и без меня узнали. Ты же ревела на весь лагерь."

    hide sp_mi_019


    show sp_sl_019:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Я ушла в лес и там была."

    hide sp_sl_019


    show sp_sem_022:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Так, прекратите! Вы, наверное, забыли, что с нами Ольга Дмитриевна, и она слушает. Могли бы перенести свои дружеские терки на другое время."

    hide sp_sem_022


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Нет-нет, пусть продолжают. Ситуация становиться все интересней и интересней."

    od "Значит, Сёма, ты спал в палатке Алисы, когда тебя искала Славя. А говорил, что придёшь ко мне пить чай. И я тоже, между прочим, тебя ждала."

    hide sp_od_022


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Ай-яй-яй, Семён! Ну, посмотри всем нам в глаза. Нехорошо вышло. Настоящие мужчины, так не поступают."

    hide sp_od_024


    stop music


    play music "audio/music/z_131.mp3"


    show sp_le_016:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.25
    with dissolve

    le "Он ещё мне обещал."

    hide sp_le_016


    allchar "(Резко повернувшись к Лене, хором)\n ЧТО ОБЕЩАЛ?"


    show sp_le_016:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.25
    with dissolve

    "Лена выдержала паузу. Потом посмотрела на Семёна."

    le "Ничего такого, о чем вы подумали. Просто он обещал поправить палатку. Я её натянула криво."

    le "Я даже фонарик повесила на ветку когда темно стало. Чтобы он смог перетянуть палатку и ему было видно. Но не дождалась, так и уснула в кривой палатке."

    hide sp_le_016


    show sp_at_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    ats "Она врет. Палатку ставила я, и палатка была натянута правильно. Она его выгораживает."

    ats "А фонарик она действительно повесила и включила. Красный маячок. И надела платье."

    ats "Из нас никто не тащил в поход платья. Мы бы тоже могли надеть. Значит, она его брала специально."

    hide sp_at_004


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Ехидно) \nАх, милый друг заблудился в чужих палатках! Какая трагедия."

    hide sp_al_003


    show sp_je_003:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "Хватит. Мало вам той драки? Пусть он сам расскажет, почему он не выполнял обещаний, и вообще, почему вел себя аморально."

    hide sp_je_003


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А тебе, Женечка, он часом ничего не обещал?"

    hide sp_al_003


    show sp_je_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "(Тоже ехидно) \nЖалеешь, что вернулась в свою палатку только под утро?"

    hide sp_je_002


    stop music


    play music "audio/music/z_177.mp3"


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Всё, с меня хватит! Я ухожу. Кстати, вы тут ссоритесь, а «подсудимый» улизнул. Не выдержал испытания ОЧНОЙ СТАВКОЙ."

    od "Запомните, в вашем возрасте это нормально, делать из мухи слона на почве отношений с противоположным полом. Всё забудется, попомните моё слово. Будут у вас ещё разочарования."

    od "А он, в общем, парень неплохой. Даже где-то совестливый. Потому и сбежал. Ему неловко. Значит, не всё ещё потеряно."

    od "Он сам должен сделать свой выбор. Не давите на него. Думаю, он в каком-то смысле под действием лекарств."

    hide sp_od_022


    allchar "Каких лекарств?"


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Я стеснялась вам сказать, но те таблетки, что давала вам Виолетта Церновна, имеют побочный эффект."

    od "Они действуют на человека, как бы это мягче выразиться, несколько возбуждающе. Это афродизиак. Думаю, все испытали на себе этот эффект."

    od "Кстати, я сама их принимаю. Это необходимо, потому что у нас эпидемия."

    hide sp_od_022


    stop music


    play music "audio/music/z_1016.mp3"


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А что такое афродизиак?"

    hide sp_ul_012



    show sp_elya_006:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    elya "(Металлическим голосом) \nАфродизиа́ки, древнегреческое название произошедшее от имени богини любви Афродиты."

    elya "Вещества, стимулирующие или усиливающие половое влечение или половую активность у людей."

    hide sp_elya_006


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Да, точно. Так что всё это пройдет, как только вы уедете из лагеря."

    hide sp_od_022


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    je "Вот, значит, оно что!"

    hide sp_je_001


    show sp_sl_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Нет, не верю. Слишком просто."

    hide sp_sl_019


    show sp_le_016:
        yalign 0.08 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    le "Это были не таблетки. Он был искренен."

    hide sp_le_016


    show sp_mi_019:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    mi "А мне как-то всё равно. Я не испытывала влечения полов."

    hide sp_mi_019


    show sp_iul_010:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "Я испытывала, но совсем немножечко. Снимала это состояние грибным супчиком. Хотя один раз... Но впрочем, это неважно."


    scene bg attic2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    show sp_el_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    guys "А почему только к нему влечение? Мы что, не противоположный пол?"


    scene bg attic2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "А мы с Ульяной эти таблетки выкидывали. Поэтому держали дистанцию и не попали в неловкую ситуацию. В отличие от остальных."

    hide sp_al_005


    show sp_od_025:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Как выкидывали? Что это еще такое? Вы, возможно, инфицированы!"

    od "(Уходя) \nСегодня же расскажу Виолетте Церновне, что часть пионеров не принимала таблетки."

    hide sp_od_025


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    je "Вы же сказали, что мы одна команда. Лгали, Ольга Дмитриевна? А мы поверили. Вы же этого не сделаете?"

    hide sp_je_001


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    od "Ладно. Но чтобы больше никаких тайн от меня!"

    hide sp_od_022 with moveoutright


    stop music


    play music "audio/music/z_176.mp3"


    scene bg genda2 with dissolve

    "С отъездом  Саманты вибрация возобновилась.  Памятник опять развернулся лицом к библиотеке."


    scene bg genda5 with dissolve

    "Никакие попытки нажать на табличку не удавались. Она будто прикипела намертво."


    scene cg ul_little_bot_day with dissolve

    "Очередной кораблик, пущенный по реке, вернулся с обратной стороны. Это означало, что ЗОНА закрылась, и из лагеря уже точно никто не выйдет."


    pause (10000000000000000000000.0)


    stop music


    play music "audio/music/z_023.mp3"


    scene bg road4 with dissolve

    "Мы тайно ходили по дороге, ведущей в поселок, но и она привела нас обратно. Из ЗОНЫ был только один выход – попытаться плыть по реке в сторону порогов."


    scene bg burleyka2 with dissolve

    "Возможно, на границе зоны действие МАШИНЫ было слабее. Как сказала Алиса, «поднырнем под купол». Если вода экранирует, то это было вполне возможно."

    "Оставалось только точно узнать место, где река поворачивает вспять и начинает течь по кругу. Это означало, что после прохождения границы пейзаж, мимо которого мы плывем, начнет повторяться."

    "Стал вопрос, делиться ли нашими знаниями о ЗОНЕ с отрядом. Мы твердо решили вытащить из «мышеловки» весь отряд, а если повезет, и остальных пионеров. Так что, надо было спешить."


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Понимаешь, в нашем отряде есть как идейные, так и паникеры. Начнется разброд и шатание, бесконечные споры, к тому же, от нас потребуют доказательств."

    al "И что мы можем предъявить? Отправить всех в поселок? Никто не пойдет. Покрутят пальцем у виска.  Другое дело, путешествие на баркасе. Тут все согласятся."


    scene bg auhouse_crop1 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Точно! Когда баркас сделает круг по реке и вернется в лагерь, никого ни в чем не надо будет убеждать! Тут мы им и расскажем все, что знаем."

    hide sp_ul_012


    scene cg longboat_sail with dissolve

    "Так и решили. Мы подговорили всех отправится на баркасе в небольшое путешествие. Объехать все острова до порогов и вернуться под парусом обратно."

    "Все хотели еще один поход, и наше предложение было встречено с энтузиазмом."

    "Стал вопрос Брать ли Ольгу Дмитриевну. Но он отпал как только мы поняли что ОД осталась в лагере за главную и не может отлучится ни на минуту."

    "Кроме того, после истории с заблудившимися малышами, вряд ли она разрешила бы нам самостоятельный поход."

    "Да еще по воде, мимо Омута, Водоворота и страшных порогов, на которых погиб по ее мнению Тарас Юрьевич."


    stop music


    play music "audio/music/z_011.mp3"


    scene cg longboat_ride with dissolve

    "Итак, вскоре вся команда в составе Мику, Лены, Жени, Алисы, Слави, Атсуи, Семёна, Толика, меня и кибернетиков собралась вместе и выдвинулась в сторону «Тайной пристани»."


    pause (10000000000000000000000.0)


    "Мы захватили съестные припасы и нужные в походе вещи на случай «мало ли чего». Жизнь в лагере и события последних дней многому нас научили."

    "До Пристани мы добрались без приключений. Погрузились на баркас и отчалили. Течение подхватило нас."

    "Парус понадобился, чтобы вырулить на середину Бурлейки, потом мы его свернули. Алиса хорошо держала курс."


    scene cg nbeach_couple with dissolve

    "Наш путь пролегал мимо Ближнего Острова, с которого нам махали какие-то два пионера. Очевидно, они встали пораньше, чтобы искупаться."

    "Мы тоже помахали им, и баркас стал огибать остров."

    "Издали мы увидели отчаянно бегущую к лодочной станции длинную, нескладную фигуру."


    scene bg deck1 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Долговязый! Следил, гад!"


    stop music


    play music "audio/music/z_126.mp3"


    scene bg nbeach with dissolve

    "Мы почти прошли мимо острова, когда с берега раздался заливистый лай. Это Тузик выбежал на песчаную косу, чтобы поприветствовать нас."

    "Судя по тому, как он подпрыгивал и сновал по берегу взад и вперед, он хотел на баркас."


    stop music


    play music "audio/music/track5.mp3"


    "Мы решили причалить и прокатить Тузика Дальнего пляжа, а там выпустить на берег. Совсем забирать его было нельзя. В противном случае Петрович мог нас поругать."

    "Он любил пса и тот часто был его единственным собеседником. Такая привязанность к собаке была не удивительна."

    "Петрович, при всей своей любви к детям был, всё же, очень одинок. Думаю, именно близость к шумному детскому сообществу и держала его в лагере."

    "Поэтому в лагере его одиночество чувствовалось им не так остро. Никто не знал, почему к нему не приезжают внуки. Наверное, стеснялись старика."

    "Петрович был слишком уж экзотичен и конечно же, редкий маргинал."

    "Мы подошли к берегу и помогли бросившемуся в воду Тузику забраться на борт."


    stop music


    play music "audio/music/z_131.mp3"


    scene bg boat_station6 with dissolve

    "Обогнув остров, мы увидели лодочную станцию. Наш дальнейший путь лежал мимо неё. Алиса взяла левее, чтобы нас оттуда не заметили."

    "Однако, мы заметили на станции суету и услышали шум, раздававшийся оттуда. Проплыв ещё, мы увидели как в лодки в спешке грузятся пионеры второго отряда."

    "Расстояние уже позволяло определить отдельные лица. Руководил всем этим мероприятием Долговязый."

    "Мы вдруг поняли, что именно мы стали причиной этой суеты."


    scene bg deck with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "ЭТО ПОГОНЯ."


    scene cg chase with dissolve

    "Семён попросил мой бинокль и посмотрел на отчаливающие лодки."


    scene bg deck with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "Да, точно погоня. Две лодки снарядили, негодяи. Самые большие."


    scene cg chase with dissolve

    "Все по очереди стали смотреть в бинокль. Лодки уже двигались в нашу сторону."


    scene bg deck with dissolve

    show sp_tol_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "Отчаянно гребут, Пора отрываться. Одно течение нас не спасет, они слишком быстро приближаются. ПОСТАВИТЬ ПАРУСА!"


    # stop music


    # play music "audio/music/z_1004.mp3"


    scene cg longboat_sail with dissolve

    "Как юнга, я тут же полезла на мачту. Парус поднимался легко, и надо было просто следить за тем, чтобы колечки на нём не перепутались со снастями и нигде не застряли."

    "Наконец, парус поднялся и через несколько секунд расправился и взял ветер. Наша скорость заметно возросла."


    scene cg chase with dissolve

    "С лодок что-то закричали. Было видно, как Долговязый на передней лодке машет рукой, отмеряя такт гребков."


    scene bg deck with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "А организаторские способности у него не отнять. Смотрите, как вышколил свою команду! Ни одного лишнего движения."

    sem "Интересно, они готовились к регате? Её же вроде отменили, из-за исчезновения физрука."


    scene cg chase with dissolve

    "Скорости сравнялись. Теперь преследователи и преследуемые шли не удаляясь и не приближаясь друг к другу."


    scene bg deck with dissolve

    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "Интересно, как долго они смогут держать такой темп?"

    "На лице Семёна играла улыбка садиста."

    hide sp_sem_016


    show sp_je_019:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    je "А мы можем увеличит скорость?"

    hide sp_je_019


    show sp_tol_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Да, если увеличим парусность."

    hide sp_tol_009


    show sp_mi_013:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    mi "А что для этого нужно?"

    hide sp_mi_013


    show sp_sem_016:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sem "Снять ваши майки и встать на корме, растянув их и подставив ветру. Шесть квадратных метров дополнительной парусности, это немало."

    hide sp_sem_016


    show sp_el_004:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    el "Восемь! Ты забыл про парней!"

    hide sp_el_004


    show sp_le_015:
        yalign 0.08 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    le "Но мы не надели лифчиков!"

    hide sp_le_015


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Первая снимая майку) \nДа пофиг! Пусть смотрят."

    hide sp_al_055


    stop music


    #play music "audio/music/z_075.mp3"
    play music "audio/music/z_099.mp3"


    scene cg longboat_sail with dissolve

    "Её примеру последовали остальные. Все, кроме Жени. На ней было платье."

    "Весь первый отряд встал на корме, растянув в руках майки. Ну и я, конечно, тоже. Мне было приятно, что мой маленький вклад поможет нам спастись от этих гадов."


    scene bg deck with dissolve

    "Лодки, которые подошли совсем близко, стали удаляться. Крики радости «сексуальных маньяков» второго отряда сменился воплем разочарования."


    # stop music


    # play music "audio/music/z_099.mp3"


    scene cg longboat_sail with dissolve

    "Славя засмеялась:"

    sl "Последнее шоу для пионеров второго отряда!"

    "Все наши подхватили её смех."

    "Я повернулась к преследователям и показала им свои ягодицы."

    ul "А это вы видели, извращенцы?! \n(пошлёпала себя по шортам)"


    scene bg deck with dissolve

    "Толпа на лодках злобно взревела. Тузик ответил им заливистым лаем."


    stop music


    play music "audio/music/z_131.mp3"


    scene cg chase with dissolve

    "Мы обогнули дальний остров и нас подхватило быстрое течение. Но баркас был тяжелее лодок и расстояние между нами снова стало сокращаться."


    ats "Вот черт!"

    "Все приуныли."


    stop music


    play music "audio/music/track4.mp3"


    scene cg longboat_sail with dissolve


    "Вдруг мы услышали спокойный, но громкий голос."

    je "ЛАДНО, РАЗ СИТУАЦИЯ КРИТИЧЕСКАЯ..."

    "Мы оглянулись. На Жене не было майки и шортиков, как на всех нас, на ней было длинное синее платье. Точнее, его уже НЕ БЫЛО."

    al "А это поступок!"

    "Онемевшие, все смотрели на стройную идеальную фигурку с изумительной формы грудью, стоявшую в одних только голубых трусиках."

    "Её платье, поднятое над головой, полоскал ветер."

    "Мальчики бросились к Жене и забрав её платье, растянули его, став к ней спиной и закрыв её ото всех."

    tol "А вот это ещё больший поступок! Даешь традиции рыцарства!"


    stop music


    play music "audio/music/z_196.mp3"


    scene bg deck1 with dissolve

    "Все заулыбались. Лодки преследователей снова отстали и, похоже, теперь уже безнадежно."











    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day46

return