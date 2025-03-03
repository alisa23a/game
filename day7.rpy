label day7:

    $ style.say_window = style.window

    $ days = 7

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = True
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = False

    $ im_gal_08_00 = True
    $ im_gal_08_01 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day


    $ show_quick_menu = True


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"

    scene bg square_day2 with dissolve
    
    "С утра вся администрация бегала вокруг Саманты. Про нас, казалось, просто забыли. Славя пошла к ОД за инструкциями. Но та отмахнулась."


    show sp_od_029:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Видишь, что происходит? Я буду занята весь день в связи с приездом Саманты и очень надеюсь на вас с Семеном. Инструкции вожатым всех отрядов уже розданы."

    od "Вы же можете пока пойти на природу и посидеть где-нибудь на пляже до вечера. Возьмите мячи, надувные матрацы, и скажите Тарасу Юрьевичу, чтобы он обеспечил вам ограждение для плавания."

    od "Но если ребята не захотят на реку, то можете сходить на Цветочную Поляну, проведешь экскурсию. Я тебе ее показывала."

    od "Оттуда хороший вид на лагерь и реку. Можете даже разжечь костер. Только будьте осторожны."

    od "Я дала задание Любови Никаноровны, чтобы дала вам сухой паек. Пообедаете на природе. Прособираете цветы и отнесёте в наш красный уголок, сделаем выставку цветов."

    od "Далеко не уходить. Вечером доложишь."


    scene bg camp_artifacts with dissolve

    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Славя тут же прибежала к нам и сказала, что у нас «выходной» от лагерного расписания и кружков сегодня не будет. Что мы можем пойти и устроить себе костер. Чем мы и воспользовались."


    scene bg camp_artifacts with dissolve

    "Немного поспорили, стоит ли собирать цветы, но потом решили, что Ольга Дмитриевна не обидится на нас, если даже мы не устроим выставку."

    "Скорее всего, она придумала про цветы, чтобы нас чем-то занять, и к вечеру забудет об этом."


    scene cg campfire_aka_day with dissolve

    "В общем, мы пошли на нашу поляну, где мы с Алисой до этого жарили котлетки, и это было самое классное место. У Алисы была гитара."

    "Пели, делали сухарики на костре и жарили колбасу, которую Взяли у Любови Никаноровны в буфете."

    "Семен (как сказала Алиса) попросил прощения за тот случай. Она сделал вид, что простила. Поэтому он был веселый и много шутил."

    "Потом Семен стал рассказывать истории про то, как работал волонтером, помогал служителям в зоопарке. Как ухаживал за животными."

    "Он очень похоже копировал обезьян. Оказывается,  они умные, хитрые и вечно что-то воруют. Было смешно. Потом рассказывал про медвежат."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_le_018:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Не успел Семен закончить свою историю, как подошли Лена и Женя, которым Славя не успела сообщить, что мы на полянке, и они нашли нас сами."

    je "А что это вы тут от нас прячетесь? Картошку печете?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Картошка, это мысль. Надо будет в дежурство по кухне напроситься и стащить авоську картошки, чтобы на весь отряд хватило. Напечь и наестся."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_le_021:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "Тебе бы всё тащить, воришка. Знаешь, за такое по головке не погладят. Может, там вся картошка посчитана."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ага. Скажи ещё, пронумерована."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2



    show sp_el_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Подошли Шурик и Электроник с тяжёлым рюкзаком."

    shu "Всем привет!"

    el "А мы вам картошки принесли!"

    "Электроник достал сетку картошки из рюкзака и высыпал ее рядом с костром."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Вот это я понимаю. Люди пришли не с пустыми руками. Не то, что некоторые."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_020:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "Зато у Семена истории."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    je "Да, духовная пища не менее важна."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Надеюсь, картошка не краденная?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Да ладно вам. Скажете тоже. Мы были дежурными по кухне. Любовь Никаноровна нам разрешила. И ещё дала огурцов и помидоров."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_021:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Женя захлопала в ладоши."

    je "Круто! Да у нас целый пикник!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Можно сварить и потом сделать пюрешку."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Не, печеная круче. Вам что, пюрешка в столовой не надоела?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Кто за печеную картошку, поднимите руки!"


    scene cg campfire_aka_day with dissolve

    "Руки подняли все кроме меня."

    ul "Я что, зря свой котелок тащила? Нет, я себе почищу, а вы как хотите. Я пюрешку люблю."

    mi "Котелок твой маловат, на всех, но... Пусть будет больше картошки разной и всякой! Я попробую и ту и другую. Улька, на меня тоже чисть."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "А что вы ещё захватили?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_el_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "У нас много всего в рюкзаке. И специи. И кружки. Вообще мы приготовили всё в завтрашний поход, но Ольга Дмитриевна отложила на послезавтра. Не пропадать же добру."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Поход? А почему мы не знаем о нем? Что это за дела вообще?! Откуда информация?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Не начинай, Двачевская. О походе знала только я и Ольга Дмитриевна. А кибернетики просто подслушали."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Ничего мы не подслушивали. Просто близко стояли."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_le_018:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    le "Ладно, пока мальчики суетятся по поводу  харчей, Семен нам ещё историю одну расскажет. А то мы пришли на шапочный разбор и все пропустили. Да, Семен?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Это можно. Ну, скажем, вы в курсе, что в лагере ходит история про Омут Большого Сома?"


    scene bg shouse with dissolve

    sem "Что там девушка утопилась, которая жила в Доме на Болотах?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "А-фи-геть! А что за дом такой?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Все придвинулись поближе."

    sem "В общем, там две версии."


    scene cg catfish3 with dissolve

    sem "Первая, что девушку утащил большой Сом."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "А вторая, что она утопилась из-за любви."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_le_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    le "Чепуха какая-то. Сом не может утащить человека. И потом, если она утопилась из-за любви, то к кому? История явно не полная. Подробности есть?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Ну так я только начал."


    scene cg catfish3 with dissolve

    sem "Сомы достигают огромных размеров. И насколько я знаю, они способны утащить утку или плывущую собаку. Что было уже не раз. Есть истории об этом. Но человека... вряд ли."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Вторая версия кажется мне более правдоподобной."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    je "А не связана ли эта история с первой? Про золотоискателя. Может, он девушку искал, а не золото?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Конечно, девушку. Мне эта версия больше нравится. Романтично."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_020:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    mi "А ты бы на его месте что выбрал?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_021:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Женя лукаво посмотрела на Шурика."

    je "Я думаю, смотря кто из нас был бы на месте девушки."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_026:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Предлагаю поставить спектакль на местном материале. Прямо вижу название. Вот так: «Любовь и золото»."

    sl "История про бедную девушку, которая не перенесла того факта, что её суженый выбрал не её, а золото. И кинулась в омут."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_el_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Вы все несете полный бред. Слишком мало фактов. Я бы на такой хлипкой базе не строил предположений. Это антинаучно."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    je "А что, я бы сыграла утопленницу."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Чур, я СОМ!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_016:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    mi "А золотоискатель, конечно же, Семен."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Где-то это уже было."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    ul "Вий! Гоголя!"


    scene cg campfire_aka_day with dissolve

    "Все засмеялись."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_020:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    mi "Я ещё поверила бы, если бы её утащил не Сом, а медведь. Тут такая глушь. Медведи наверняка водятся."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "Если верить Петровичу, то да. И он говорит, что в голодные годы они подходят прямо к лагерю. Говорит, съели Альму, дворняжку. Остался Тузик. Раньше в лагере две собаки было."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_at_004:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ats "А вдруг этот год тоже голодный?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_el_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Ещё один бред! Какие голодные годы? Они нагуливают жир и спят! А не шатаются по лагерям. Я в энциклопедии читал!"

    el "Петрович известный фантазер. Хотел произвести на вас впечатление. А вы и купились."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "А может и шляются. Я слышал рычание вчера, когда ходил в лес. И не только я. Другие тоже говорят. И Ольга Дмитриевна нас предупреждала не заходить далеко в лес!"


    scene bg al_ul_campfire_empty2 with dissolve

    "Где-то треснула ветка. Все замолчали."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    mi "Что-то мне как-то уже нехорошо... Может, пойдем отсюда?"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_le_022:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "И правда. Я прям слышу, как кто-то крадется."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    je "И мне показалось. Вот, слышите хруст?"


    scene bg al_ul_campfire_empty2 with dissolve

    "Раздалось рычание."


    scene cg fake_bears with dissolve


    "Мику вскочила и, подвернув ногу, упала. Все бросились врассыпную. На полянку выбежали пионеры с криком: «Разыграли! Разыграли!». Один пионер был в махровом халате не по росту, натянутом на голову."

    "Все постепенно вернулись к костру."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_061:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Уроды малолетние! Так можно до инфаркта довести!"

    "Алиса методично раздала оболтусам несколько легких пинков и подзатыльников."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sem_022:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sem "А халат-то физрука. А это кража. Да, ребята, если он хватиться и узнает, то за такие дела вас из лагеря не просто выгонят, это уже уголовка."


    #scene cg fake_bears2 with dissolve



    scene bg al_ul_campfire_empty2 with dissolve




    show sp_2sq_pi_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0

    show sp_2sq_pi_003:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 1.0

    show sp_2sq_pi_001:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.0


    piro "Да я чё? Я ничё. Я верну. Мы же просто дурачились."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Смотрите, Мику! Она подвернула из-за вас ногу!"

    je "Мику, тебе больно? Идти сможешь? Черт, молчи, я вижу. Распухла как. Надо срочно в медпункт!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_al_012:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Идиоты. Из-за вас человек травмировался!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_mi_022:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Мику попыталась встать."

    mi "Я попробую идти. Ой нет, не могу..."



    scene bg al_ul_campfire_empty2 with dissolve


    show sp_2sq_pi_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0

    show sp_2sq_pi_003:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 1.0

    show sp_2sq_pi_001:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.0

    piros "Да мы... Мы только пошутили."


    scene bg al_ul_campfire_empty2 with dissolve

    "Пионеры второго отряда бросились наутёк."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Так, мальчики. Шурик, Электроник, взяли Мику под руки и быстро в медпункт. Вдруг у неё перелом или разрыв связок. Быстрее!"


    scene cg sem_mi_carrying with dissolve

    sem "Тихо. Тропа узкая, так не пройти, вдвоем неудобно. Я один её донесу, давайте мне её на руки. Вот так. Она легкая. "

    mi "Спасибо, Сёмочка! Ты такой классный."


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    je "Я с вами!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    sl "Я тоже!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_el_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Электроник залил костёр водой из стеклянной бутылки из-под лимонада."
  
    el "Идут все!"


    scene bg al_ul_campfire_empty2 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Эх... Накрылась моя пюрешка."

    "Ребята быстро ушли, а я завозилась, собирая картошку в сетку, и когда собрала, то увидела, что уже вокруг никого нет."

    "Река была рядом, и я подумала, что неплохо бы искупаться. Картошку я спрятала в кустах. Все равно мы сюда еще придем."


    scene bg crsh2 with dissolve

    "Я пошла в сторону реки и вскоре вышла на отмель. Я разделась и стала искать место, где песок и хорошо войти в воду."

    "И вдруг увидела что-то в воде рядом с берегом. Это была сеточка, похожая на авоську, растянутая на колышках. Часть ее уходила в воду. А в ней копошились раки."


    scene cg ul_crawfishes with dissolve

    "Видно кто-то поставил эту штуковину на раков. Кто бы это мог быть? Наш сторож Петрович, не иначе. Он так себе на выпивку зарабатывает."

    "Наловит раков и в поселок, на рынок. Но для экономии покупает портвейн."

    scene cg ul_crawfishes with dissolve

    pause (1000000000000000000.0)


    scene cg tales_of_petrovich with dissolve

    "И потом как выпьет, начинает философию наводить, а мы слушаем и смеёмся."

    "Говорит: «А что водка? Тех денег хватило бы на одну бутылку. А я вместо одной на эти деньги три «креплёнки» покупаю»."

    "Из поселка он всегда возвращается с кошелкой, в которой что-то позвякивает. Он бутылки в старые газеты заворачивает, чтобы директриса не видела. Но все равно, иногда звук его выдает."

    "Что уволят, Петрович не боится."

    "Говорит: «Я ценный кадр. Начальство меня уважает. Оттого поблажку дает. Сами судите, кто за вами, гавриками, тут за такие деньги присматривать станет? А работа у меня вредная для здоровья. Оттого я стресс снимаю»."


    scene cg ul_crawfishes with dissolve

    "Он ещё хвалился нам, что тут на всю округу самые рачьи места. Точно, его рук дело!"

    "Я увидела ещё две такие же сеточки. Видно, Петрович работает с размахом."

    "Потом я подумала, что если я возьму немного раков нам с Алисой, то Петрович от этого беднее не станет. Приманка там ещё есть. Другие наползут. И я взяла самых отборных."

    "Только их нести было трудно. Пришлось снять майку и сделать такую себе из неё авоську. Хорошо что у меня под ней купальник. Раки оказались кусачие. Хватали меня за пальцы сквозь майку. Но я быстро бежала."


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Когда я пришла, Алиса меня немножко поругала, но потом похвалила за смекалку. Хорошо, что я взяла много раков. Хоть и тяжеленные, и нести их было трудно. Зато теперь хватит на всю нашу компанию."

    scene bg auhouse_crop1 with dissolve
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Что с Мику?"


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Отвели в медпункт. Её Виола смотрит."

    scene bg auhouse_crop1 with dissolve
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А отряд где?"


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не знаю. Прибежал Толик, и все пошли с ним. Но вроде ничего срочного. Давай решим, что с раками делать будем."


    scene bg dining with dissolve

    show sp_ln_002:
        yalign 0.12 subpixel True
        xalign 0.45 subpixel True
        zoom 1.3


    "Сначала мы хотели оттащить их на кухню, но тетя Люба была сильно занята и сказала:"

    ln "К Петровичу отнесите, он вам сварит. Все равно сидит на лавочке весь день. А у меня тут светопреставление. Надо успеть до ужина сделать заготовки. Людей прибавилось."


    scene bg bench with dissolve

    "И мы с Алисой сели на лавочку  и задумались."
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Слушай... Может, отнесем их Петровичу просто? Ничего говорить не будем. Скажем просто, что помогаем ему ловить раков."


    scene bg bench with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ага, такие воришки-тимуровцы. Слямзили раков у деда и сами же принесли, а он им еще за это благодарность."


    scene bg bench with dissolve
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да ладно тебе. Ну не подумала я. Нести уже поздно."


    scene bg camp_artifacts with dissolve

    "И мы свесив головы побрели назад в домик. Но по дороге встретили Лену и Кибернетиков."


    scene bg camp_artifacts with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Вы куда? В Красный уголок не идёте? "


    scene bg camp_artifacts with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Вот ещё. У нас выходной от мероприятий. ОД сама разрешила. Если что, вы нас с Ульяной не видели, а мы как будто не знали про Красный Уголок. Лады?"

 
    scene bg camp_artifacts with dissolve

    show sp_el_009:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    el " Это что, раки? Вот класс. Сами наловили?"


    scene bg camp_artifacts with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну не совсем... Стащили у Петровича из раколовки. Вот теперь думаем покаяться."


    scene bg camp_artifacts with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Вот дурынды! Поздняк метаться. Давайте их съедим. Тем самым разделим коллективную ответственность. Правда, Лена?"


    scene bg camp_artifacts with dissolve

    show sp_le_018:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    le "Не знаю. По-моему, это достоевщина. Ладно, если вам стыдно, можете не есть. Лично я хочу раков."

 
    scene bg camp_artifacts with dissolve

    show sp_el_009:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Точно. Съедим и покаемся. Вместе. Повинную голову меч не сечет."


    scene bg camp_artifacts with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Но сначала сварим на костре и слопаем."


    scene bg camp_artifacts with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ладно. Только у нас не в чем варить."


    scene bg camp_artifacts with dissolve

    show sp_le_018:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "Я знаю, у кого есть большой походный котелок!"

    "И Лена вызвалась сбегать за походным котелком."


    scene bg camp_artifacts with dissolve
    
    show sp_ul_015:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Я засмеялась."


    scene bg camp_artifacts with dissolve

    show sp_le_021:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Лена спросила, чего я смеюсь."


    scene cg le_running with dissolve

    "Сбегать. Ну да. Я представила Ленку бегущую. У неё довольно большая грудь и бедра. Поэтому бегает она как утка. И «всё» ходит ходуном. Но мальчикам нравиться. Они же смотрят не на технику бега, а на «достоинства»."

    "Я ей, конечно, этого говорить не стала."

    scene cg le_running with dissolve

    pause (1000000000000000000.0)


    scene bg crsh2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Соврала, что представила лицо Петровича, который утром проверит свои раколовки. И скажет, закурив самокрутку: «Что-то вы, субчики, нынче не жалуете мои харчи. Видно заелись, клещатые!» Ну или что-то в этом роде."


    scene bg al_ul_campfire_empty2 with dissolve

    "Лена убежала и скоро притащила котелок! Договорились, что вечером снова пойдем на ту полянку и сварим раков."


    scene bg camp_artifacts with dissolve

    show sp_le_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    le "А они не умрут до вечера? Хотя, они же земноводные, наверное, могут дышать воздухом."


    scene bg camp_artifacts with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    shu "Нет, это лягушки земноводные, а они членистоногие."


    scene bg camp_artifacts with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Пока вы спорите, они точно помрут. Надо взять на кухне большую кастрюлю и налить им туда воды."


    scene bg camp_artifacts with dissolve

    "Так мы и сделали. А до вечера еще много чего случилось."


    scene cg pigeon_mail with dissolve

    "Например, у нас  появилась Голубиная Почта."

    "Ещё дома, мы во дворе с другими детьми играли в голубиную почту. Выбирали одного мальчика или девочку и назначали «почтовым голубем». Иногда двоих."

    "Им доверяли записки, которые мы писали друг другу. А он (голубь) должен был не читая их передавать."

    "За это ему те, кто получали записки, давали всякие вкусности. Конфеты, печенье, пряники. Это означало, что ему доверяют. И это было почётно. Я часто была «голубем»."

    "Иногда вот так, получаешь записку и не знаешь, от кого. В этом был интерес, догадаться, от кого. Обычно писали что-то приятное. Стихи, признания, хвалили или признавались в чувствах."

    "Или писали обиду. Ну, когда вслух не могли сказать, а тут такой случай. В ответ обычно писали: «Докажи»."

    "А ещё назначали свидание. Приходишь такая на свидание, думаешь, там один человек (на кого думаешь), а там совсем другой. Вот смеху-то."

    "Это, как говорил папа, помогает «выразить себя». Вот, например, мальчик хочет выразить себя, признаться в чувствах, но стесняется. Или боится получить отказ, или что его засмеют."

    "Ну и пишет: «Если я тебе не безразличен, приходи туда-то и туда-то. Если тебе всё равно — порви это письмо и напиши НЕТ»."

    "Всё должно быть в тайне. Поэтому никому никто не рассказывал, от кого записка, даже если и догадывался. Всё по-честному."

    "Мне, например, в записках признались двое мальчиков. Но встретиться испугались."

    "Ну, не знаю... Я же бы их не съела, чего бояться. Дурачки. Так я до сих пор и не знаю, кто это были. Уже всех в голове перебрала."

    "На уроках ходишь и смотришь, у кого какой почерк. Или тетрадки, сданные на проверку, на перемене изучаешь. Так можно догадаться."

    "Наверное, я с детства любила всякие тайны разгадывать. Но если записка не подписана, то можно конечно и пообсуждать с девчонками, догадки всякие строить. Весело же."

    "Думаю, и мальчишки тоже так делали. Но я ничего такого не писала мальчишкам, чтобы они меня не обсуждали."

    "Ну, там, напишешь:"


    scene cg pigeon_message with dissolve

    pause (1000000000000000000.0)


    scene cg pigeon_mail with dissolve

    "У нас так всегда проверяли на дружбу. Это папа мне подсказал. «Если мальчик не боится насмешек и таскает твой портфель, то значит, это очень серьезно»."

    "Папа рассказал, что тоже таскал портфель за одной девочкой из параллельного класса и дружит с той девочкой до сих пор, хотя, она потом и выбрала другого мальчика и даже вышла замуж за него. Ну, вот так бывает в жизни."

    "Но я отвлеклась. И вот я эту идею кинула в нашем лагере, и весь лагерь теперь, уже третий день, пишет записки. Все играют в Почтового Голубя."

    "И «голуби» так и летают по лагерю из отряда в отряд. Даже малыши играют в Почту."

    "Мне до этого дня никто пока не писал. Больше всех писали Алисе, Славе и Лене. Но даже Жене одно письмо принесли. Мику получила три письма (у меня тут учет строгий), Атсуи аж четыре!"

    "Саманте вообще принесли огромную кучу писем, но все на русском, и Мегги ей каждый день читает их. А она всем отвечает."

    "Даже кибернетикам пишут записки. Только Толику ни одной."

    "Поэтому я написала ему и подписалась «НЕЗНАКОМКА». Потому что это неправильно, что ему никто не пишет. Пусть ему тоже будет письмо. (Что написала, вам знать не обязательно)."


    scene cg dining_crowded with dissolve

    "И мы пошли в столовую."


    scene cg dining_crowded2 with dissolve
    
    show sp_ul_016:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я ковыряла запеканку (не люблю я её), а сама грустно думала, почему мне не пишут? Что со мной не так?"


    scene cg dining_crowded2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "А Алиса сказала, что все боятся, потому что у меня такой характер. Думают, засмею."


    scene cg dining_crowded2 with dissolve

    show sp_2sq_pi_002:
        yalign 0.08 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И вот когда мне стало совсем грустно, вдруг прибегает «почтовый голубь». Я кричу: «Алиса, это тебе!» А он ко мне и сует мне при всех в руку записку. И говорит: «Это вам»."

    "Я угостила «голубя» печеньем, и он убежал."


    scene cg dining_crowded with dissolve

    pause (1000000000000000000.0)


    scene cg dining_crowded2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "А Семён сразу заинтересовался и «Ну-ка, ну-ка, покажи, от кого? Надеюсь, не от физрука?» (это у него шутка такая юмора)."

    "Все стали смеяться. Алиса ему сразу тычка ногой (она это может). Вот гад. Но я с ним позже разберусь."


    scene bg auhouse2 with dissolve

    "И мы пошли в домик. Записка была сложена в конвертик, и сверху была приписка: «Лети письмо к другу, прямо в руки». Я не сразу открыла. Хотя, очень хотелось."


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Открывай."

    scene bg auhouse_crop1 with dissolve
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ну, не знаю... Открыть что ли? Может, потом?"


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не кривляйся, открывай. Я же знаю, ты хочешь!"


    scene bg auhouse2 with dissolve

    "Ну и вот, мы открыли (у меня нет тайн от Алисы). А там... аккуратный такой почерк, приятно пахнет леденцами и сердечко внизу пририсовано. Вот эта записка."


    scene cg_pi_note_diary with dissolve

    pause (1000000000000000000000.0)

    "Оказалось, от Пионера. Назначил мне свидание. Написал, что заберет меня с ближнего пляжа. На лодке кататься. Значит, он не забыл нашу встречу."

    "На душе стало тепло. Я даже простила его, что он тогда ушёл не попрощавшись. Вообще не могу долго злиться. Хотя тогда, помню, сильно злилась."

    "Приклею записку к дневнику. Для истории. Я же пишу историю нашего лагеря."


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "А Алиса отнеслась к записке серьезно. Говорит, одну тебя не пущу. Но я же упрямая. И она все-таки разрешила."


    #Анимация варят раков

    image crawfish_bowling:
        
        "images/an/an7day/an_d07_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an7day/an_d07_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat


    scene crawfish_bowling with dissolve

    pause (1000000000000000000.0)


    "Ну вот, а вечером мы варили раков. Только к костру никто не пришел кроме Ленки и Слави."

    "Как потом выяснилось, всех остальных собрали в Красном уголке, и никого не выпускали, пока мероприятие не кончилось."

    "Была встреча Саманты с младшими отрядами. А наш отряд припахали следить за порядком и все организовать."

    "ОД отправила Славю собрать остальных (меня, Лену и Алису) но та, оценив ситуацию, решила сделать вид что не нашла нас. А я думаю, просто ей хотелось посидеть с нами у костра."

    "Опыта раковарения у нас ни у кого не было. А они вариться не хотели, все норовили вылезти. Славя с Ленкой смешно визжали. Но Алиса палочкой скидывала раков назад в котелок."

    "Мне их даже стало немного жалко. Жили себе не тужили и бац, попали в котелок. Но Алиса меня успокоила."


    scene bg al_ul_campfire_empty with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Если бы не мы, то завтра их Петрович бы сварил или продал и выпивку купил. А так, можно сказать, что ты человека от пьянства спасла и от увольнения."


    scene cg campfire_crawfishes with dissolve

    "Скоро раки покраснели."


    scene bg al_ul_campfire_empty with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sl "Я слышала, что если красные, значит, можно кушать."


    scene bg al_ul_campfire_empty with dissolve

    show sp_le_017:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    le "Если я начну есть и он зашевелиться в руках, я точно умру от страха."


    scene bg al_ul_campfire_empty with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Они уже сто раз как мертвые. Представь, если бы тебя почти час держали в кипятке."


    scene cg campfire_crawfishes with dissolve

    "Но мы их на всякий случай ещё минут пять поварили."


    scene bg auhouse2 with dissolve

    "Потом мы оттащили их в лагерь. Наши все жалели, что с нами не были. Но зато мы устроили у нас в домике пир."


    scene bg auhouse2 with dissolve

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_mi_015:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Семен привел Мику. Виола наложила ей повязку и сказала, что до свадьбы заживет."


    scene cg boided_crayfishes with dissolve

    "Потом ели раков. Мне было вкусно. Все тоже ели и хвалили."

    "А Ленка съела аж пять штук. Мику одного, я трех, Славя двух, мальчишки, те уплетали, как будто были, как бы сказала моя бабушка, с голодного края."


    scene bg auhouse2 with dissolve

    show sp_at_004:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Атсуи не стала есть. Сказала, что водоплавающих никогда не ест. И даже водоползающих."


    scene bg auhouse2 with dissolve

    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sl "Жень, а ты что не ешь? Знаешь, как вкусно."


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Я их боюсь. Даже мертвых. Но если кто то мне почистит..."


    scene bg auhouse2 with dissolve

    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    shu "Я почищу. Тебе сколько?"


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Ну, если только одного, на пробу."

    "Мне кажется, Женя решила присоединиться, просто чтобы не разбивать компанию. Все ели руками, а она даже почищенного Шуриком рака брала салфеточкой."


    scene bg auhouse2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Жень, в первобытном обществе ты умерла бы с голоду. Пока бы ты думала, чем есть раков, всё бы слопали другие троглодиты."


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    je "Слава богу, мы не в первобытном обществе."

    "Женя откусила крохотный кусочек."


    scene bg auhouse2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса съела только пару штук, остальные есть не стала, а аккуратно  завернула в газету «Пионерская правда» и сказала, что завтра сбегает в поселок за пивом и мы их «прикончим со смыслом»."


    scene bg auhouse2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А мне все равно пиво нельзя. Можно я своих сейчас съем?"


    scene bg auhouse2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Нет. Тогда компании не будет. Мне с пивом одного рака хватит, остальные все твои завтра."


    scene bg auhouse2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Вот это - другое дело."

    "Вот это я понимаю, настоящая дружба!"


    scene bg auhouse2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "А потом Алиса достала сигареты."


    scene bg auhouse2 with dissolve

    show sp_sl_025:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Славя на неё зашикала и сказала, что это нарушение правил лагеря."


    scene bg auhouse2 with dissolve

    "Но все кончилось тем, что все закурили."

    show sp_le_018:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Даже Лена."


    scene cg sigarettes with dissolve

    "Сигареты были Космос."


    scene bg auhouse2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я тоже хотела попробовать и протянулась за сигареткой, но мне дали шлепка."


    scene bg auhouse2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса сказала, чтобы я «и думать не смела», что она займется моим воспитанием и что мне ко вредным привычкам приобщаться рано."


    scene bg auhouse2 with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_le_017:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И Славя с Леной кивали с умным видом. Ой, как будто они сами сильно взрослые и не нарушают. Ну, смешно прям..."



    scene black with fade

    pause (1000000000000000000000.0)

    stop music fadeout 1.0

    jump day8


return
    