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

    "Она плакала, но все-таки нашла в себе силы выразить благодарность Мегги и Саманте за участие в жизни лагеря и за их вклад и участи в игре Зарница."

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


    scene cg sam_bus with dissolve

    "Но ее мягко но настойчиво вели в машину... Машина была красивая. Большой красный автобус, не то что наш скромненький ПАЗик. Икарус называется." 

    "В машине ещё сидели какие-то люди в костюмах. Как сказала Алиса, «гебешники». Что это такое, я переспрашивать не стала."

    "Все дружно замахали руками, когда машина тронулась, и махали, пока она не скрылась за поворотом."


    scene bg road with dissolve

    "Наш отряд стал меньше на одного друга."

    "Все были в смешанных чувствах."


    stop music


    play music "audio/music/z_023.mp3"


    scene bg attic2 with dissolve

    "И мы решили собраться на чердаке, поговорить о событиях последних трех дней. Слишком много всего случилось."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    "Но когда мы собрались, то на чердаке вдруг появилась Ольга Дмитриевна. Как она узнала про чердак?"

    hide sp_od_022


    show sp_tol_007:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Все посмотрели на Толика. Но у него было такое лицо, что всем стало ясно – ЭТО НЕ ОН."

    hide sp_tol_007


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Я вижу, вся честная компания уже собралась. Ну и лица у вас! Не бойтесь, ничего вам не будет."

    od "Я давно знаю про ваше убежище. Теперь ясно, кто утащил у Тараса Юрьевича его диван. Давайте договоримся, ведь мы одна команда. Или вы мне доверяете или нет."

    od "Напоминаю, что я прикрыла вас, когда шло расследование по поводу всех ваших ЧП, хотя прекрасно знала о них. Никто не вылетел из лагеря."

    od "Ну так что, будем, наконец, дружить или как?"

    hide sp_od_024


    "Все облегченно вздохнули. Ольга Дмитриевна раскинула руки, как бы приглашая всех обниматься. Что мы с радостью и сделали."

    "Это была прекрасная сцена. У всех ещё стояли слезы по поводу отъезда Саманты, а тут такое! И мы снова ревели. Вспоминали нашу ВОЙНУ и всё-всё…"


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
        xalign 1.0 subpixel True
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
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Я обязана была провести с тобой воспитательный процесс. Ты должна меня понять и простить."

    od "Вспомни, какая колючая и ершистая ты приехала в лагерь. Мне тоже было не легко с вами."

    od "Ты доставляла больше всех хлопот. Но я тебя отстояла в тот раз перед Маргаритой Павловной. Ты же знаешь."

    hide sp_od_024


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "Ольга Дмитриевна, это же Алиса. Не берите в голову."

    hide sp_je_001


    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
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
        xalign 1.0 subpixel True
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
        xalign 0.0 subpixel True
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
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    elya "(Металлическим голосом) \nАфродизиа́ки, древнегреческое название произошедшее от имени богини любви Афродиты."

    elya "Вещества, стимулирующие или усиливающие половое влечение или половую активность у людей."

    hide sp_elya_006


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Да, точно. Так что всё это пройдет, как только вы уедете из лагеря."

    hide sp_od_022


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "Вот, значит, оно что!"

    hide sp_je_001


    show sp_sl_019:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    sl "Нет, не верю. Слишком просто."

    hide sp_sl_019


    show sp_le_016:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
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
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Как выкидывали? Что это еще такое? Вы, возможно, инфицированы!"

    od "(Уходя) \nСегодня же расскажу Виолетте Церновне, что часть пионеров не принимала таблетки."

    hide sp_od_025


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    je "Вы же сказали, что мы одна команда. Лгали, Ольга Дмитриевна? А мы поверили. Вы же этого не сделаете?"

    hide sp_je_001


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    od "Ладно. Но чтобы больше никаких тайн от меня!"

    hide sp_od_022 with moveoutright







    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day46

return