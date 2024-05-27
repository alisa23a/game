label day28:

    $ style.say_window = style.window

    $ days = 28


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene an_d16_06 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"


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

    scene an_d28_07 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


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


    stop music fadeout 0.5

    queue music "audio/music/z_1005.mp3" noloop


    "Дальше произошло то, о чем я писать не буду. В общем, как и предполагала Ольга Дмитриевна, свисток пригодился. И как только я засвистела..."



    scene bg stock3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_371.mp3" noloop



    show sp_pe_007:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    show sp_sem_017:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve


    "Дверь в кладовку склада,  слетела с петель и я увидела как Петрович с ломиком и Семен, ворвались внутрь"


    stop music fadeout 0.5

    queue music "audio/music/z_173.mp3" noloop


    show sp_od_026:
        yalign -0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 1.0 
    with dissolve


    "А за ними Ольга Дмитриевна, вся белая, и кто-то из нашего отряда. И они все вместе скрутили Вано."


    pause (10000000000000000000000.0)


    scene bg stock3 with dissolve

    show sp_al_061:
        yalign 0.05 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1

    "Алиса даже успела ему врезать."

    pause (10000000000000000000000.0)


    scene bg stock3 with dissolve


    show sp_pe_007:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1

    "А Петрович кричал: «Я на войне контуженый, я за себя не отвечаю!» Но у него отобрали ломик."

    pause (10000000000000000000000.0)
 

    scene bg stock3 with dissolve    


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3" noloop



    "Вано сидел связанный, качался из стороны в сторону, плакал и повторял, что все мы его не так поняли."


    show sp_fi_014:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.25
    with dissolve

    "А когда на него прикрикнул Тарас Юрьевич (весь был белый, я думала он его убьет), замолчал."


    pause (10000000000000000000000.0)


    scene bg stock3 with dissolve


    show sp_ln_001:
        yalign -0.2 subpixel True
        xalign 0.05 subpixel True
        zoom 0.90


    show sp_mp_009:
        yalign 0.0 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1


    show sp_may_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1


    "Потом прибежали Маргарита Павловна, завхоз и Люба. А Вано очнулся, стал ныть: «Я больной человек, не зовите милицию. Если надо, возьмите деньги»."


    scene cg ul_all_asking with dissolve

    "И все взрослые спрашивали меня: «ОН ЭТО СДЕЛАЛ?» А я не понимала, о чем они, а они не говорили. Я рассказала, как было, сказала, что у меня только пара синяков, царапины на спине и порванная майка. И всё."

    "И всех, кроме меня, отправили по домикам. Магоша сказала: «Вам тут не цирк»."


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_444.mp3"


    "Праздник отложили на следующий день. А вечером, приехал тот же следователь и с ним еще четверо."


    stop music fadeout 0.5

    queue music "audio/music/z_1018.mp3"


    "Спросили меня про всё и записали. Долго говорили с Виолеттой Церновной и я услышала, как она сказала: «Я не думаю, но завтра будет ясно»."


    scene cg vano_cops with dissolve

    "Потом Вано в наручниках посадили в УАЗик. А он всё время повторял «Вай, вай, вай». Как объяснила Алиса, по грузински, это означает «ВСЕМУ КИРДЫК». И они уехали."


    scene cg vio_0 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_201.mp3"


    "А Виолетта Церновна провела со мной несколько часов. Брала всякие анализы и говорила много и ласково."

    "Она задавала мне странные вопросы. Например, интересовалась, как часто мы с Алисой меняем постельное белье. Принимаю ли я ее таблетки. И не замечала ли я каких ни будь странностей с собой по утрам."

    "Я ответила, что странностей не замечала, но мне снятся всякие сны. И рассказала... Она же врач."

    "Она улыбнулась и произнесла: «В твоем возрасте такие сны видеть еще рано, но раз ты их видишь, значит все идет по плану»."

    "А я спросила, ПО КАКОМУ ПЛАНУ? Но она не ответила. Потом наклонилась прямо к уху и сказала шёпотом: «Не стесняйся. Мне можешь рассказывать все, я умею хранить тайны»."

    "А в конце осмотра она произнесла, как будто говорила сама с собой: «Удивительно, какой потрясающий эффект. Впрочем, как и ожидалось». Я запомнила эту её фразу."


    scene an_28_02 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_067.mp3"

 
    "Вообще же, в течении дня, Ольга Дмитриевна с Алисой от меня не отходили, и я гостила в домике Ольги Дмитриевны. Она мне рассказывала что-то о себе, чтобы отвлечь меня от всего, что было."

    "Мы с Алисой натащили ей вкусняшек. Их для нас двоих было слишком много. Ведь каждый из отряда считал своим долгом принести «пострадавшей» что-нибудь вкусное. "

    "И мы устроили грандиозные посиделки с чаепитием. Ольга Дмитриевна оказалась сладкоежкой."


    pause (100000000000000000000000000000.0)


    scene bg odhouse6 with dissolve

    show sp_od_024:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    "Я спросила у Ольги Дмитриевны, можно ли забрать себе фотоаппарат, который дал мне Вано, или это вещественное доказательство."

    od "Там, куда его увезли, он ему точно не понадобиться. И потом, судя по всему, он подарил его тебе от чистого сердца."

    hide sp_od_024


    scene bg odhouse7 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Это была взятка."

    hide sp_ul_019


    scene bg odhouse6 with dissolve

    show sp_od_024:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    od "Считай, что это компенсация за перенесенные страдания."


    scene an_d10_01_bg with dissolve

    show an_10_01

    "И хоть я нисколечко не страдала (ну немного испугалась только), я согласилась. В общем, у нас появился свой фотоаппарат. А Славин мы вернули."

    "Просто так я бы его не взяла, но это нужно было для дела. Получилось, что он как бы не мой лично, а нашей следственной группы. А это, как сказал бы Петрович, «совсем другой коленкор»."


    scene cg meeting_staff with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_197.mp3"


    "А вечером было собрание персонала. Я забежала в столовую чтобы успеть всех сфотографировать новым фотоаппаратом для стенгазеты."

    "Физрук начал кричать, а Маргарита Павловна сказала: «Пусть снимает, мы редко собираемся в полном составе. Будет память». И я их щелкнула."

    "Ну вот. На собрании  тетю Любу директриса назначила заведующей столовой, вместо Вано. Теперь все называли её только Любовь Никаноровна."

    "Приехала новый повар, женщина, Клавдия Сергеевна, с громкой фамилией Громова."

    "Котлетки стали толще, пюре перестало быть жидким, перестали давать надоевший всем лапшевник (его заменили творожником). Стало вкусно. А в столовой появились новые скатерти."

    "В остальном всё было по-прежнему. Теперь, когда все хвалили новое меню, Любаша (ой, Любовь Никаноровна) говорила: «Скажите спасибо Лениной»."


    scene cg smu_hut with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    "И вроде теперь все вопли Смутьянова по поводу плохого питания можно было бы считать выдумкой. Но он сбежал. Наверное, после того случая с милицией."

    "Но, как сказал мой поклонник из второго отряда (ну тот, что подарил мне свою футболку красивую после соревнований), Смутьянов прячется на Рачьей отмели и живет в шалаше."

    "Девочки из второго отряда таскают ему еду из столовой. А он называет себя «жертвой борьбы с режимом»."





    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day29

return 