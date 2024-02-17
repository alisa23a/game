label day28:

    $ days = 28

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_022.mp3"


    scene an_d16_06 with dissolve

    "Предупреждения Петровича насчет Вано скоро оправдались. Вано Артабекович явно выделял меня из общей массы пионерок. Он всячески тайно подчеркивал свое расположение и задаривал меня подарками."

    "Подарки были безобидные. Лишняя порция пюре, котлетка(которые Любаша клала по его распоряжению в мою тарелку), фрукты за стол первого отряда, особо чистая посуда и стол, всегда аккуратно расставленные стулья."

    "Он прямо весь расцветал, когда я приходила в столовую. И все время пытался шутить и всяко заговаривать со мной, называя мня «персик»."

    "Весь отряд за глаза посмеивался надо мной, называя меня ПЕРСИКОМ. Я злилась, но терпела."

    "Но постепенно к его выходкам привыкли. Алиса говорила, что южные люди от природы очень эксцентричные (надо запомнить это слово)."

    scene bg camp_artifacts with dissolve

    show sp_od_001:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1 


    "Однако Ольга Дмитриевна так не считала. Она неоднократно указывала (и я это лично слышала) Маргарите Павловне на странное поведение заведующего общепитом."


    scene bg camp_artifacts with dissolve

    show sp_mp_003:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2
    

    "Но та, только отмахивалась:"

    mp "Где я вам в разгар сезона найду такого специалиста? Пусть доработает, а там посмотрим"

    "Но эти отговорки (как выяснилось) продолжались уже третий сезон, а Вано был «непотопляем»."

    "Возможно, Ольга Дмитриевна подозревала Маргариту Павловну в банальном взяточничестве, но доказать это было трудно."

    scene bg camp_artifacts with dissolve

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1


    "К тому же, она хорошо относилась к Жене, которая не разделяла убеждений матери, а была честной и принципиальной девочкой. Она пострадала бы автоматически, случись Маргарите покинуть лагерь."

    "Её практика в библиотеке шла в зачет к ее характеристике для поступления на филфак после школы. (О её планах поведал мне Сёмен)."


    scene bg camp_artifacts with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1

    "Как рассказывал Петрович, в свое время Вано оставил престижную и прибыльную работу в торговле и переместился в лагерь, поближе к детям, устроившись простым заведующим столовой."

    "Как будто это из за несчастного случая с его ребенком, которого он не мог забыть."
    

    scene an_d28_01 with dissolve

    "Вскоре из нашего с Алисой домика стали пропадать вывешенные на просушку на балкончик трусики и майки. И Юля тут была ни при чём."


    image an_28_01: # Анимация пропадающего с верёвки белья
        
        # "images/an/an28day/an_d28_01.webp" with Dissolve(0.5, alpha=True)
        # pause 0.7
        "images/an/an28day/an_d28_02.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an28day/an_d28_03.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an28day/an_d28_04.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an28day/an_d28_05.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an28day/an_d28_06.webp" with Dissolve(0.5, alpha=True)
        pause 1.0


    scene an_28_01 with dissolve

    pause (10000000000000000000000.0)


    "Сначала мы грешили на пионеров второго отряда. Но допрос с пристрастием, проведенный Алисой, запугавшей весь второй отряд, показал беспочвенность таких подозрений."

    "Оставался Вано. Ольге Дмитриевне было доложено."


    scene an_d28_06 with dissolve


    show sp_od_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 
    with dissolve

    od "Чертов фетишист пузатый. \n(ворчала она)"

    od "Это уже не первый случай. Слава Богу, дальше этого пока не шло. Но, кто знает."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"


    image an_28_02: # Анимация Ольга Дмитриевна пишет, ест печенье
        
        "images/an/an28day/an_d28_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an28day/an_d28_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat

    scene an_28_02 with dissolve

    pause (10000000000000000000000.0)


    scene an_d28_07 with dissolve

    "ОД строго проинструктировала меня на случай «непредвиденных обстоятельств» и дала мне милицейский свисток."

    od "Если что, будет приставать или заманивать куда, свисти, я услышу! Давно хочу убрать его из лагеря, но случая не было. Хитрый гад. Осторожный."

    "Я кивала. Вместе с Алисой и ОД мы твердо решили подловить и убрать Вано из лагеря. Но события развивались слишком стремительно."


    scene bg dining with dissolve


    "В один из дней, когда снова ночью была вибрация, а памятник Генде повернулся лицом к Библиотеке, весь отряд отправили на кухню, помогать готовить праздничный обед для малышей."

    "А поводом был ДЕНЬ РЕБЕНКА, который проводили каждый заезд. И должны были быть «Веселые старты» и эстафета."


    scene bg stock3 with dissolve

    "Меня Вано взял на легкую работу. Все чистили картошку, а я складывала подарки и завязывала ленточки. Это было на складе."

    "Я помогала Вано Атарбековичу, а он рассказывал мне про свою жизнь. Вроде как разоткровенничался. Потому что я напоминала ему его покойную дочь."

    "Он сказал, что она погибла. Была моего возраста, и что мы похожи. Он так расчувствовался, что стал плакать, я его успокаивала."

    "Он всё спрашивал, хочу ли я подарков, потому что ему теперь подарки дарить некому, а была бы дочь, он бы дарил ей, и что я ему стала как дочь."

    "И стал рассказывать, как он её любил и качал на коленях."


    stop music fadeout 1.0


    play music "audio/music/z_1005.mp3" noloop


    "Дальше произошло то, о чем я писать не буду. В общем, как и предполагала Ольга Дмитриевна, свисток пригодился. И как только я засвистела..."

    stop music fadeout 1.0


    play music "audio/music/z_371.mp3" noloop


    scene bg stock3 with dissolve


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    show sp_sem_007:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1


    "Дверь в кладовку склада,  слетела с петель и я увидела как Петрович с ломиком и Семен, ворвались внутрь"






     

    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day28

return 