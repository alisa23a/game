label day6:

    $ style.say_window = style.window

    $ days = 6

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = True
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = False

    $ im_gal_05_00 = True
    $ im_gal_05_01 = True
    $ im_gal_05_02 = True
    $ im_gal_05_03 = True
    $ im_gal_05_04 = True
    $ im_gal_05_05 = True
    $ im_gal_05_06 = True
    $ im_gal_05_07 = True
    $ im_gal_05_08 = True
    $ im_gal_05_09 = True
    $ im_gal_05_10 = True
    $ im_gal_05_11 = True
    $ im_gal_05_12 = True
    $ im_gal_05_13 = True
    $ im_gal_05_14 = True
    $ im_gal_05_15 = True
    $ im_gal_05_16 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day


    $ show_quick_menu = True


    stop music fadeout 0.5

    queue music "audio/music/z_017.mp3"

    scene bg auhouse_crop2 with dissolve
    
    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Утром мы с Алисой обсудили всё, что нам удалось узнать. История с кражей личных дел могла всплыть, и нужно было вернуть документы на место."

    "А это ещё один поход в кабинет Ольги Дмитриевны."


    scene bg square_day2 with dissolve

    show sp_sem_023:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Мы ломали голову, как это сделать незаметно для насторожившегося Семёна. Наверняка, он что-то заметил и был теперь начеку."


    scene bg auhouse_crop1 with dissolve
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "И тут я вспомнила про дымовуху. Мы делали такие, когда играли во дворе в войнушку. Они делались из старых смятых теннисных шариков или старой кинопленки и фольги и ужасно дымили."

    "Суть была в том, чтобы устроить в лагере переполох, а под шумок забраться в комнату Ольги и вернуть документы."


    scene bg auhouse_crop2 with dissolve
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Собираясь утром на линейку, Алиса  сказала:"

    al "С этой идеей мы ещё поработаем. Если что, шарики можно будет взять у физрука. Это я беру на себя."

    al "Как лучшей спортсменке в отряде, он дает мне ключи от бытовки и раздевалки, чтобы я принесла мячи и скакалки. Так что проблем не будет."


    stop music fadeout 0.5

    queue music "audio/music/z_900.mp3"


    scene cg squad_formation3 with dissolve

    "Эта линейка была особенная."

    "Обычно мы делаем перекличку, и Ольга Дмитриевна говорит что-то бодренькое. Затем поём гимн отряда и все бежим на зарядку. Потом утреннее закаливание и следом завтрак."

    "Но сегодня на площадке перед статуей Генды стоял стол, который взяли, по видимому, из столовой, и на нём стопкой лежали какие-то тетрадки. Рядом стояла Женя."

    scene cg squad_formation3 with dissolve

    pause (1000000000000000000000.0)


    scene bg square_day2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я толкнула Алису локтем:"

    ul "Что бы это могло значить?"


    scene bg square_day2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Она только пожала плечами."


    stop music fadeout 0.5

    queue music "audio/music/z_102.mp3"


    scene cg squad_formation3 with dissolve

    od "Внимание, пионеры!"

    "Вид у Ольги Дмитриевны был торжественный, а блузка, юбка и галстук были как-то подчеркнуто отглажены. Панамка задорно топорщилась."


    scene bg square_day2 with dissolve

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса прыснула в кулак:"

    al "Слушай, она её точно крахмалит."


    scene bg square_day2 with dissolve

    show sp_sl_025:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "Те, кто стояли рядом, захихикали, но Славя всех одернула. Она была старостой и должна была следить за дисциплиной."


    scene cg squad_formation3 with dissolve

    od "Как вы знаете, в нашем лагере при библиотеке работает литературный кружок «Юный журналист». Его ведёт Женя. Она подала мне идею ввести в отряде дневники."

    od "Это значит, что каждый будет записывать всё интересное, что в течении дня было в его жизни в лагере."

    od "Это даст юным репортерам, будущим журналистам, материал для стенной газеты, с которой из нашего отряда уже сотрудничает Ульяна."

    od "Кстати, она ведёт дневник с первого дня пребывания в Совёнке."


    scene bg square_day2 with dissolve

    show sp_ul_027:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Тут все посмотрели на меня и захлопали. А я покраснела. Я не знала, что Ольга Дмитриевна расскажет всем."

    "В первый день я похвасталась ей, что папа у меня журналист и я веду дневник потому, что хочу тоже быть писателем. И теперь я не знала, злиться мне на неё за это или нет."

    "Правда, слова не говорить никому я с неё не взяла, и она имела право. Но всё равно вышло неловко."


    scene cg squad_formation3 with dissolve

    od "Вы можете писать для себя всё, что хотите. Но отдельные ваши рассказы мы будем печатать в стенной газете. Какие, вы решите сами."

    od "Дневники ваши и вы сможете забрать их после каникул домой, как память о пребывании в лагере. Если кто-то делает это в первый раз, то может посоветоваться с Женей и Ульяной."

    od "Женя будет подсказывать вам ваши ошибки, чтобы вы вели дневник грамотно. А теперь мы вручим вам дневники."

    "Мы построились в очередь, и Женя раздала нам дневники."



    scene bg square_day2 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    ul "Интересно, дневники раздали во всех отрядах, или только в нашем?"


    scene bg square_day2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Думаю, только в нашем. Мы же образцово-показательный отряд. На нас теперь все эксперименты ставить будут."


    stop music fadeout 0.5

    queue music "audio/music/z_516.mp3"


    scene cg dining_crowded with dissolve

    "После того, как раздали дневники, все побежали в столовку, где прошло жаркое обсуждение новости."

    "По слухам, источником которых была Женя, так как она была вхожа в кабинет директрисы, к нам везут какую-то девочку из Америки. Точнее, из США."

    "Называли даже имя - Саманта Смит. Под большим секретом новость обошла весь лагерь."


    stop music fadeout 0.5

    queue music "audio/music/z_076.mp3"


    scene bg camp_artifacts with dissolve

    "То, что это правда, сомневаться не приходилось, потому что начался страшный переполох. Все отряды отправили на уборку территории."

    "Подметали, стригли газончики, белили деревья и даже бордюрчики вдоль главной дорожки в административный корпус."

    "Нам выдали новые галстуки и нашивки. До обеда мы должны были их (нашивки) пришить вместо старых."


    show sp_fi_017:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25


    show sp_may_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Физрук и завхоз носились с каким-то затравленным видом. Как сказала Алиса, «метались как попугаи в клетке»."


    scene cg pe_solo_bench with dissolve

    "Только наш сторож, Петрович, сохранял невозмутимое спокойствие. Раскуривая свою самокрутку, он посмеивался и отпускал неприличные реплики: «Иш, как забегали, прям как вша керосиновая»."


    scene cg pe_ul_bench with dissolve

    "А я не постеснялась и, закончив уборку газона, подсела к нему на лавочку."

    ul "Деда, а что такое, «вша керосиновая»?"

    "Петрович усмехнулся."

    pe "Это, деточка, когда в войну все завшивели, то лекарств у нас против этой напасти не было. Ну и, значит, народными средствами спасались — керосином. У кого он был, конечно."

    pe "Натирали им голову и везде. Насекомые, или как вы их нынче называете, начинали бегать как оглашенные. Вроде нашего начальства сегодня. Тут их ловили. И к ногтю."

    "Он засмеялся старческим скрипучим смехом."

    ul "А наше начальство тоже к ногтю?"

    "Петрович задумчиво затянулся самокруткой и покачал головой."

    pe "Могут. Потому что, видать, большая шишка едет. Ишь, как все всполошились! Я думаю, из самой Москвы инспекция."

    pe "Если проверят столовую, будет шухер. Любаша-то не ворует, а вот за начальника столовой не поручусь."

    "Петрович наклонился и перешел на шёпот."

    pe "Вано-то у нас точно на руку нечист. Да и другая у него слабость. Очень страдает до женского полу. Ты уж осторожней, деточка. Будет чем угощать, не принимай. Далеко ли до греха?"

    ul "Ой, деда, что вы такое говорите? Ну ладно, я запомню. И девочкам из отряда скажу."

    pe "Скажи, милая, скажи. Только меня не выдавай."


    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"


    scene bg camp_artifacts with dissolve

    "После уборки мы не пошли на пляж как всегда, а отряды развели по домикам, где вожатые провели с подопечными пионерами беседы."


    scene bg library2 with dissolve

    show sp_od_029:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Ольга Дмитриевна собрала нас в помещении библиотеки. Вид у неё был серьезный и озабоченный."

    "Она рассказала нам про скаутов, что они вроде наших пионеров только американские и носят синие галстуки."

    "Что девочка, которая приедет, Саманта, будет в нашем отряде. Мы заслужили такое право, как лучший отряд в лагере."

    "Ну и там всяко о том, что, мол, вы уж не подведите, вы должны быть внимательны, она плохо говорит по-русски."

    "Старайтесь показать всё лучшее, чем богата история нашей организации пионеров, что мы лицо страны, покажите ей лагерь. Ну и всё в таком духе."

    "Напомнила, что торжественная линейка будет вечером и нам нужно спеть гимн."

    "И ещё сказала, что директриса хотела устроить парад с торжественным прохождением отрядов, но Ольга Дмитриевна её отговорила."

    od "Кто, кроме меня, нормально говорит на английском?"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Руку подняла Женя."


    scene bg library with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "А ещё, неожиданно для нас, руку поднял Семён."


    scene bg library with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса толкнула меня в плечо:"

    al "Смотри, а наш-то знаток женского пола, туда же. Интересно, когда он успел выучить язык?"


    scene bg library with dissolve

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Хотя, ему же 28 лет по метрике"


    scene bg library2 with dissolve

    show sp_od_030:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Мы захихикали. Ольга Дмитриевна грозно посмотрела в нашу сторону."


    scene bg library2 with dissolve

    show sp_od_029:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Семён с Женей берут шефство над Самантой и в короткие сроки научат её говорить на русском, в пределах необходимого."

    od "Семён, останешься после собрания и я проверю твои знания. В Жене я не сомневаюсь."


    stop music fadeout 0.5

    queue music "audio/music/z_412.mp3"


    scene cg sam_diary1 with dissolve

    "В результате наше начальство прозевало приезд «высокой гостьи». Ждали у ворот. Ждали целую делегацию."

    "Но, как выяснилось, американцы никого не предупредили, а смылись из гостиницы (как потом рассказала сама Саманта) рано утром и, доехав на посольской машине до поселка, пересели в рейсовый автобус."

    "Ну, в общем, не доверяли они советской показухе, да и из скромности решили не шуметь."

    "У них там всё проще происходит. Это называется у них «встреча без галстуков»."

    "Пока все были заняты уборкой, они тихо вошли через лазейку (и откуда узнали?). В общем, Саманта ходила в сопровождении переводчицы по лагерю, пока мы бегали и перешивали эмблемки. Смех да и только."


    scene bg camp_artifacts with dissolve

    show sp_at_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Всё испортила Атсуи. Она бегло говорила по-английски и узнала Саманту по фото, которое до этого видела в журнале (почту ей привезли недавно уехавшие родственники)."


    scene cg sam_diary1 with dissolve

    "Она кинулась к Саманте, они стали быстро о чем-то говорить на своём и смеяться. Вокруг них стали собираться пионеры, бросившие метлы и лопаты."


    scene bg camp_artifacts with dissolve

    show sp_sl_028:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Мы раньше всех закончили уборку, и Славя побежала докладывать Ольге Дмитриевне о ЧП."


    stop music fadeout 0.5

    queue music "audio/music/z_075.mp3"


    scene bg camp_artifacts with dissolve

    show sp_mp_009:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Надо было видеть нашу директрису и всю администрацию, испуганно бежавшую от административного корпуса, надевая на ходу дежурные улыбки. Это было весело."


    scene bg camp_artifacts with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25


    show sp_may_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Завхоз споткнулась и разбила бы себе нос, если бы её не подхватил физрук."


    scene bg mus with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "В общем, был объявлен общий сбор, а Саманту под белые руки повели в актовый зал (музкружок)."


    scene bg busstop4 with dissolve

    "За воротами были слышны гудки. Это подъехали, наконец, наши «органы безопасности», проспавшие бегство Саманты. Бедные, вот им наверное влетело от начальства!"

    "Но как бы то ни было, дело было уже сделано. Весь план Маргариты Павловны и Ольги Дмитриевны пошел насмарку."


    stop music fadeout 0.5

    queue music "audio/music/z_018.mp3"


    scene bg mus with dissolve

    "Все отряды построили и отправили в музкружок. Поместились не все, а только первый, второй и третий отряды."

    "С остальными Саманту решено было знакомить позже, в библиотеке. Так сказать, «в процессе»."


    scene bg mus with dissolve

    show sp_sam_013:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Саманта оказалась девочкой невысокого роста с открытым и каким-то слегка удивленным лицом."


    scene bg mus with dissolve

    show sp_sam_013:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_meg_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Она каждый раз поворачивалась к переводчику и что-то переспрашивала. Очевидно, её живо интересовало всё, что происходило вокруг."


    scene bg mus with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Семён протиснулся к ней и быстро заговорил на английском. Как позже выяснилось, он объяснил ей, что она теперь будет в нашем отряде и мы устроим ей экскурсию по лагерю."


    scene bg mus with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Она все время кивала и говорила «Ес». На её лице играла добродушная улыбка."


    scene bg mus with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Другие пытались оттеснить Семёна и заговорить с девочкой, но Семён прочно удерживал её внимание и, наконец, взяв за руку, повёл в библиотеку."


    scene bg library2 with dissolve

    show sp_je_002:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Женя стала объяснять напиравшей толпе, что официальная часть знакомства произойдет позже и Саманта расскажет о себе и своей миссии, а пока ей нужно показать её комнату над библиотекой."


    stop music fadeout 0.5

    queue music "audio/music/z_179.mp3"


    scene bg library3 with dissolve

    "Когда страсти поутихли, весь наш отряд собрался в читальном зале. Мы были очень горды тем, что Саманту определили в наш отряд. Она нам сразу понравилась."


    scene bg library2 with dissolve

    show sp_od_029:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Когда все расселись, Ольга Дмитриевна попросила Саманту рассказать о себе."


    scene bg library with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Из её рассказа мы узнали, что она приехала по приглашению нашего правительства, когда написала письмо нашему «президенту» (так она называла Генерального секретаря ЦК КПСС)."


    scene cg sam_diary4 with dissolve

    "Что сначала её повезли в Москву. Москва произвела на неё большое впечатление. Потом было много встреч и экскурсий."


    scene bg library with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Потом она попросила познакомить её с «русскими скаутами». Ей не смогли отказать."

    "Почему высшим руководством был выбран именно наш лагерь, было непонятно. Саманта сказала, что наш лагерь ей очень понравился. У них нет таких специальных лагерей."

    "Скауты в США обычно представляют отдельные колледжи, а собираются только в походы на природу, во временные лагеря, где инструктора учат их «выживанию»."


    scene bg library2 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Я так и не поняла, от чего и зачем они выживают. Я хотела, чтобы Семён перевёл мой вопрос, но Ольга Дмитриевна остановила меня, сказав, что вопрос не этичный."

    "Тогда я спросила про цвет галстука. Ведь у нас каждый пионер знает, почему наши галстуки красные."


    scene bg library with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Саманта выслушала вопрос и растерялась. Она пожала плечами, улыбнулась и сказала просто «Я не знаю, но обязательно спрошу у нашего руководства»."

    "Ещё она добавила, что этот вопрос никогда не возникал и что «так было всегда»."


    stop music fadeout 0.5

    queue music "audio/music/z_418.mp3"


    scene bg library2 with dissolve

    show sp_mp_013:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.2

    "Потом встала наша директриса Маргарита Павловна, которая до этого момента сидела тихо, как мышь. Она подняла руку и все замолчали."

    "Она сказала, что поскольку Саманте трудно говорить через переводчика, то она расскажет нам о скаутском движении в США. И стала рассказывать удивительные вещи."


    scene bg library with dissolve

    show sp_sam_013:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Саманта, которой Женя быстро переводила рассказ Маргариты Павловны, сидела с большими круглыми глазами. Было видно, что многое из того, что рассказывала наша директриса, она слышит впервые."

    "И вот что та рассказала."


    scene cg scout_diary with dissolve

    "Скауты возникли как Братства Православных Следопытов. Скаутское Движение бережно хранит свои атрибуты и символы, соблюдает свои особые скаутские традиции."

    "Главным символом скаутов является трехлепестковая лилия. Носить скаутскую форму почетно любому скауту. Скаут никогда не позволит, чтобы его форма была мятой, грязной, порванной."


    scene cg symbols_diary with dissolve

    "Нашивки и значки скаутов не такие, как у нас. У нас звезда, пламя и вождь, а у них лилия, круг с узелками и звездочки."

    "Скаут сам пришивает нашивки на свою форму, делает это аккуратно и красиво. Скаут должен следить за правильностью расположения нашивок на своей форме."


    scene cg uniform_diary with dissolve

    "Скаутская форма у разных организаций может быть разного покроя и разных цветов. Форменные рубашки у скаутов США чаще всего синего цвета, но не обязательно."

    "Порядок расположения нашивок на форме у всех скаутских организаций мира примерно одинаковый. Если уметь правильно читать форму, то можно многое узнать о хозяине формы."

    "Левый рукав и левое плечо рассказывают о принадлежности скаута к стране, организации, отряду. На левом погоне (плече) формы обычно располагается государственный флаг той страны, где живет скаут. "

    "На левом рукаве, под самое плечо, располагается нашивка организации, в которой состоит скаут. Над левым карманом находится круглая нашивка РСО."

    "Правая сторона формы рассказывает о личных достижениях скаута. На правой стороне рубашки располагаются нашивки испытаний, которые заслужил скаут."

    "На правом кармане формы, а также над ним, располагаются нашивки скаутских специальностей, которые он освоил, и лагерей, в которых он побывал."


    scene cg scout_diary with dissolve

    "Каждый скаут обязательно носит шейный платок (галстук). Именно этот элемент отличает одну скаутскую группу от другой: галстуки различных скаутских патрулей и групп отличаются по цвету."

    "Они могут иметь цвета герба твоего края, города, местности. Галстук Братства Православных Следопытов может быть трех цветов. Желтый — галстук новичка. Это первое приобщение к БПС."

    "Синий — галстук скаута III степени. Такой у Саманты. При посвящении скаута во II степень на одном из концов галстука завязывается узелок."

    "При посвящении скаута в I степень узелки завязываются на обоих концах галстука."

    "Оранжевый галстук — галстук ровера, это уже третье звание скаута."

    "Ровер — «бывалый» скаут, (у нас это комсомолец и пионервожатый) у которого хороший стаж работы с детьми и большой опыт по различным специальностям. Обычно про роверов говорят, что это тот, кто умеет всё и хорошо."

    "Зеленый — цвет наставника (высшее звание среди скаутов). Добиться этой ступени — значит, уметь находить выход из любой ситуации, быть лидером среди товарищей и являть собой эталон настоящего скаута."

    "Скаутский шейный платок завязывается особым образом и не так, как пионерский. Иногда есть специальная застежка для галстука."


    scene bg library2 with dissolve

    show sp_mp_013:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.2

    "Директриса закончила, и все удивленно зааплодировали. Саманта громче всех. Директриса даже покраснела. Видно было, что она готовилась к приезду гостьи и выучила всё наизусть."


    stop music fadeout 0.5

    queue music "audio/music/z_196.mp3"


    scene bg camp_artifacts with dissolve

    "Потом нам разрешили показать Саманте лагерь и окрестности."

    "А Ольга Дмитриевна ушла на совещание с Маргаритой Павловной и персоналом лагеря. Перед уходом она строго нам сказала:"

    show sp_od_022:
        yalign 0.03 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Не ходите кучей, как овцы, не привлекайте внимания. Достаточно трёх человек."


    scene bg camp_artifacts with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Но мы её не очень послушались. Всем хотелось побыть рядом с Самантой."


    scene cg ul_sam_flag_diary with dissolve

    "Все фотографировались. И я тоже сфотографировалась с Самантой."


    scene bg camp_artifacts with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Хотя, второй и третий отряды хотели чтобы она была только с ними. Прямо из кожи вон лезли."


    scene bg camp_artifacts with dissolve

    show sp_sb_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Говорили, что у них Бременская знает английский. Мы её, конечно, пустили к Саманте, остальным сказали, «не сегодня»."


    scene bg camp_artifacts with dissolve

    show sp_sam_012:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Она же ещё будет почти месяц в лагере. Ничего, успеют."


    stop music fadeout 0.5

    queue music "audio/music/z_516.mp3"


    scene cg squad_formation2 with dissolve

    "Ну вот. Оказывается, Ольга Дмитриевна приготовила дневник и для Саманты. И ей его торжественно вручила под наши аплодисменты. Вот какая у нас предусмотрительная вожатая. Ни в одном лагере такой нет."

    "Интересно, что напишет Саманта про наш лагерь. Вот бы посмотреть хоть одним глазком. Может, и про меня что-нибудь."

    scene cg squad_formation2 with dissolve

    pause (1000000000000000000000.0)





    scene black with fade

    pause (1000000000000000000000.0)

    stop music fadeout 1.0

    jump day7


return
    