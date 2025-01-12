label day14:

    $ style.say_window = style.window

    $ days = 14

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = True
    $ adv_15 = False

    $ im_gal_13_00 = True
    $ im_gal_13_01 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day

    $ show_quick_menu = True


    scene cg meeting_far with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"


    "За суетой с нашими с Алисой похождениями все как то забыли о том, что мы должны были устроить праздник в честь приезда Саманты. Но ОД напомнила нам об этом тем же вечером. Мы побежали готовиться."

    "Собственно, событий должно было быть аж три. Первое в честь приезда Саманты, второе в честь празднования Годовщины Лагеря и третье, заключительный прощальный концерт перед отъездом (до которого было еще время)."

    scene cg meeting with dissolve

    "Но приезд Саманты, как сказал бы Петрович, мы «профукали». Даже построения толком не получилось. Ее внезапное появление застало всех врасплох."

    "Поэтому решено было провести творческий вечер и все, что приготовлено, просто почитать со сцены."

    scene bg stage3 with dissolve

    "А у нас ничего приготовлено не было. Если малыши седьмого и восьмого отрядов хотя бы выучили стишки, то у нас, как сказал бы мой папа, «И бык не валялся»."

    show sp_mi_020:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve 

    "Выручила Мику. Она была заведующей музыкального кружка. И вот что она предложила. Она напишет песню, а мы ее разучим и споем хором. Так и сделали."

    hide sp_mi_020


    scene bg stage2 with dissolve

    "Песня получилась неплохая. Называлась «Наш Совенок». Но хор не сложился. Потому, что пели - «кто в лес, а кто по дрова». И как она не билась, ничего не выходило."


    scene bg stage4 with dissolve

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_at_001:
        yalign 0.1 subpixel True
        xalign 0.65 subpixel True
        zoom 1.2

    show sp_je_001:
        yalign 0.07 subpixel True
        xalign 0.35 subpixel True
        zoom 1.2

    show sp_sem_001:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "У Толика вообще не было слуха, Атсуи забывала слова, Женя стеснялась, а Семён не пел, а издавал какие-то непотребные звуки."


    scene bg stage4 with dissolve

    show sp_od_022:
        yalign 0.00 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_sl_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Как сказала про него ОД, «Ржет как конь стоялый». А Славя засмеялась. Надо спросить у Слави, что такое «конь стоялый», все-таки она у нас селянка."


    scene bg stage4 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Тогда, Алиса предложила сделать ВИА. Ну то есть вокально-инструментальный ансамбль. И спеть эту песню с эстрады."


    scene cg al_sl_guitar with dissolve

    "И конечно, начались репетиции. Алиса со Славей полностью ушли в «процесс». Подбирали репертуар. Но надо было решить вопрос с организацией. На чем играть, где, когда."


    scene bg mus with dissolve

    "Ну вот, ВИА. Инструменты в музкружке были. И всем эта идея понравилась, особенно мальчикам, это освобождало их от необходимости петь, потому что ВИА был женским."


    scene cg ul_drums with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_306.mp3"


    "Стали распределять, кто на чем будет играть. Я, конечно, сразу села за барабаны."


    scene cg miku_piano with dissolve

    "Мику, как самая грамотная музыкантша, взяла на себя клавишные и вокал."


    scene cg al_sl_guitar with dissolve

    "Славя с Алисой гитары и вокал."


    scene cg al_mi_guitar with dissolve

    "Мику у нас вообще была «многостаночица». В перерывах между игрой на клавишных, она успевала ещё на ритм-гитаре помочь, там где Алиса выходила в соло импровизацию."


    scene cg mi_sem_stage with dissolve

    "А фон держал Семён. Он, оказывается, мог играть на бас-гитаре, его Мику научила." 


    scene cg mi_sem_training with dissolve

    "(И где это они и когда репетировали, почему я не знаю?!)"


    scene cg ul_drums with dissolve

    "Договорились, что Алиса будет меня подменять на ударных. Я тоже хотела все время вокал, но меня засмеяли. Сказали, что барабанщиков вокалистов не бывает."

    "А я им: «А Ринго Стар?» А они мне: «Так то же Стар... А ты еще не доросла»."

    "Ну и мы поссорились немного. Но я на репетициях все равно им подпеваю, пока они не слышат. Без микрофона, потому что микрофон они у меня отобрали."

    "(Но позже я всё-таки уговорила их на две песни)."


    scene cg miku_piano with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_410.mp3"


    "Для нас Мику написала три  песни. Первая, моя любимая, «Почему не спит сова». Вот, прямо про Совенок."


    scene bg stage2 with dissolve

    show sp_fi_006:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2
    with dissolve

    "Даже Тарасу Юрьевичу понравилось, хотя ему «медведь на ухо наступил»."

    hide sp_fi_006

    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "И ОД тоже похвалила Мику. Сказала, что если будет краевой конкурс пионерских песен, то мы поедем на него с этой песней."

    hide sp_od_024

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Вот там где соло, это я пою. Тоненьким таким голосом."

    hide sp_ul_014

    window hide


    pause (100000000000000000.0)


    "Вторая — «Знаменосец» и третья — лирическая, «Принеси мне цветок полевой». Ну, она тоже любимая. Но только не про меня. Никто мне записок и цветов не шлет. Ну разве что Пионер. Но он не в счет. А вот знамя, это самое то."


    #scene cg standard_bearer with dissolve

    image an_14_04: # Анимация Знаменосец
        

        "images/an/an14day/an_d14_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_51.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat


    scene an_14_04 with dissolve

    stop music fadeout 0.5

    #queue music "audio/music/znamenosets_v3.0_cut.mp3" #noloop

    queue music "audio/music/znamenosets_v5.0.mp3"


    #pause (10000000000000000000.0)


    "Бьется знамя на ветру — как живое \nЕсли мы умрем в бою — вместе, двое"
    "Люди скажут — не беда, пал за дело. \nБыл он видно до конца — пионером."

    "И тут, у меня всегда ком в горле... Прямо допеть не могу этот куплет. Так жалко знамя, павшее в бою, ну и себя немножко. Вот, я же прямо вижу себя со знаменем. Ну и лошадку жалко. Да всех жалко."

    "И тут проигрыш такой, на соло гитаре Алиса в конце припева, ка-а-ак выдаст! Ииииуууууууу..."

    "И я на барабанах, бам, бам, и трель такую..."

    "А Мику прям сочно аккорды на ионике. А Семён на басухе тын-тун, тын-тун. Аж в ушах толчки и горшки на подоконнике подпрыгивают."

    "Ну, в общем, круто вышло. Песня прямо вышла офигенная! Даже Маргоше понравилась. Хотя, она у нас и придира."

    pause (10000000000000000.0)


    scene cg wildflower with dissolve


    stop music fadeout 0.5

    queue music "audio/music/wildflower.mp3"


    "Вот, хотела слова «Цветка полевого» еще написать. Помню там такое..."

    "Принеси мне цветок полевой \nЯ его положу между строк"

    "Не судьба нам, наверно, с тобой \nРазбегутся тропинки дорог..."

    "Тоже очень слезная песня. На прощание с лагерем мы ее споем. Но вот слова, я их не полностью знаю. Сбегаю, перепишу и потом тут выложу, в дневник. Тоже хорошая песня. Про мальчика и девочку. Про пионеров, в общем."

    pause (100000000000000000.0)


    scene cg girl_bear with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_450.mp3"


    "Мы знали, что Саманте нравятся наши песни из фильмов и решили разучить и сыграть песню про медведей (сюрприз)."


    scene cg boat_sem_mi_guitar with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_067.mp3"


    "А про Мику и Семёна мне потом Толик рассказал (оказывается, у него тоже есть особенность, как у меня, все подмечать)."

    "Так вот, он рассказал, что периодически Семён с Мику брали гитару и на лодке уплывали (думаю на Остров Дальний). И возможно, там репетировали. (Ну да конечно,  репетировали, так я и поверила)."

    "Но тем не менее, песенки они выучили. А на рояле вечерами (это мне уже Женя рассказала, у нее же музкружок, рядом с библиотекой). И вот, вечерами там трень–трень. А она возьми, да и посмотри,  кому там «делать нечего»."

    "И выяснилось, что это наша зеленоволосая с Семой наяривают. Женя долго подсматривала (интересно, зачем?) Говорит, просто играли в четыре руки. Ничего такого. Прямо чудеса..."


    image an_14_01: # Анимация Алиса лёжа играет на гитаре
        

        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat


    scene an_14_01 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_401.mp3"


    "Ну вот. Еще будут танцы и там мы оторвемся. Алиса обещала выдать мощную сольную партию."

    "Я, правда, ни той ни другой не слышала, но, думаю, Алиса не станет играть отстой. Она вообще рокер и такие соляки выдает, закачаешься. Вот бы мне так…"

    "Пыталась так. Но у меня не получается. Правая рука отлично, а вот пальцы не берут аккорд, растяжка нужна. Алиса сказала «ты короткопалая». Прямо очень обидно."

    "Хотя правда, руки у меня маленькие. Зато папа восхищался. Сказал, «Как у мамы» и еще, «Все принцессы имеют изящные ручки»."

    "Но это не значит, что принцессы не умели играть на инструментах. Вот хотя бы «Бременских музыкантов» взять. Там принцессу, между прочим, приняли в группу бродячих музыкантов."


    scene bg mus_curtains with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "Ну вот и началась подготовка. Мы прямо до утра почти репетировали. Сделали вид что по домикам разошлись (после чердака). А сами, зашторили окна музкружка, чтобы нас не спалила ОД (отбой у нас в лагере это святое)."


    scene cg meeting_far

    "Мы только на пару часиков перед линейкой вздремнули. На линейке у всех глаза были красные, как у кроликов."


    scene bg genda_blured with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Ну и Петрович нас прикрыл. ОД у него спросила: «Все в домиках? Никто не шляется по лагерю?» "


    scene bg hide_bench with dissolve  

    show sp_pe_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "А Петрович ей: «Ну вы же знаете, Ольга Дмитриевна, мимо меня и мышь не проскользнет»."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_102.mp3"


    show an_10_01 

    "Подготовка продолжилась с утра и весь день. Только мы с Алисой в перерыве еще успели в библиотеку сходить, провернуть одно дело. Сейчас расскажу."


    scene bg library2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_418.mp3"


    "Ну вот, готовимся мы к концерту, а между тем я подговариваю Алису попробовать найти в библиотеке документы относящиеся к старому лагерю."

    "Ну и если повезет, то стибрить (слямзить, умыкнуть) ключ от подвала библиотеки. Не на совсем, а на время. И мы в перерыве между репетициями, во время обеда, пошли к Жене."

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Женя обедала прямо в библиотеке. Мы принесли ей печеньки. Ей дали задание протереть все полки и переложить на них книги. Отложить старые папки с верхних полок вниз и отнести эти папки в подвал."

    scene bg lib_spec_stor with dissolve

    show sp_je_001:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Для этого, как сказала Женя, ей дали ключ от спецхрана. Всё надо было сделать до вечера."

    hide sp_je_001

    show sp_vio_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "И Виола сама(!) принесла ей обед в библиотеку. И сказала: «Не отвлекся, Умнова. Сегодня я тебя забираю на весь день.»"

    hide sp_vio_001 with moveoutright

    "И ушла куда–то."

    "Это была большая удача! Теперь не надо было ломать голову как добыть ключ от подвала."


    scene cg je_in_lib with dissolve

    "Женя была грустная. Она работала уже третий час и сильно устала. Мы предложили ей помощь. Она с радостью согласилась. Я сразу полезла на лестницу."


    scene bg library4 with dissolve

    "Меня интересовали старые пожелтевшие папки."


    scene an_d14_24 with dissolve

    "Алиса помогала внизу и, как могла, отвлекала Женю. Вместе они протирали полки и сдували пыль с книг, а потом слегка протирали их."


    scene cg old_map with dissolve

    "Среди книг мне попалась старая карта. И я снова вспомнила про баркас. И подумала, что если мы доплывем на нем до моря, то эта карта может пригодиться. Я аккуратно свернула её и спрятала под рубашку."


    scene bg library4 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    "Почти во всех книгах было много закладок. И даже попадались цветы. Кто-то их высушил в память о ком-то... «Гербарий чувств». (О! хорошее название для рассказа, надо будет не забыть записать)."


    scene cg glade_flowers with dissolve

    "И я тут вспомнила про нашу песню. «Принеси мне цветок полевой». И я представила себе, как будто я в поле, где цветы и небо. И что это песня про меня. А я бегу, бегу по усеянному цветами полю."

    "И я забыла про библиотеку и стала качаться в такт звучащей во мне музыке. Только вот песня немного не про то. Там про мальчика и девочку."

    "В общем, песенка про отношения."


    stop music fadeout 0.5

    queue music "audio/music/z_418.mp3"


    "Помню ещё, наша директриса на прослушке сказала: «А это, Ольга Дмитриевна, не слишком интимно звучит?»"

    "А та ей: «Каждый думает в меру своей распущенности, Маргарита Павловна. А они ещё дети и наших мыслей у них быть не может!»"

    "Вот как отбрила Маргошу! Та аж покраснела вся. А мы за сценой закричали «Ура!» и обнялись. Так песня без правок прошла."


    scene an_d14_24 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_420.mp3"


    "Ой, ну тут я отвлеклась. И значит, тащит Женя тяжеленную стопку папок с полки, а она возьми, да и упади на пол."

 
    image an_14_03: # Анимация Женя сквозняк на лестнице
        

        "images/an/an14day/an_d14_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an14day/an_d14_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


    scene an_14_03 with dissolve

    pause (10000000000000000000.0)

    "И шнурки все развязались, а листы из папок разлетелись по всей библиотеке."


    scene cg folders with dissolve

    "Мы давай их срочно собирать. И тут я показываю Алисе на одну папку. Там схемы лагеря. Но не такие, как мы знаем, что висят на доске информации. Другие, все в каких-то красных пометках и линиях."


    scene cg secret_folder with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "А ещё на папке гриф «Секретно». Ну, думаю, это папки старого лагеря Бурлейка. (Так назывался старый пионерский лагерь). То, что нам надо! Ну вот, Алиса отвлекает Женю. А я эту папку тихо так, хвать и в свой рюкзачок. И сныкала."


    scene bg library3 with dissolve

    "Ну и мы давай песни наши отрядные петь и протирать полочки дальше. Вроде так и было."

    "Там ещё много папок было. Но все они в мой рюкзак бы не поместились. Ну и Женька бы вой подняла, если бы заметила. Она вообще-то аккуратистка."


    scene bg lib_spec_stor2 with dissolve

    "Потом мы понесли папки в Спецхран. Ну это он только называется так. А с виду обычный подвал. Только есть еще одна дверь внизу, железная и очень тяжелая."


    scene cg je_in_lib2 with dissolve

    "В подвале было темно и Женя пошла искать, где свет включается. А мы с Алисой включили фонарик и немного побродили там."

    "Подвал большой. Чего там только не было! Стеллаж с противогазами, всякие книги, еще с царских времен, и даже портреты какие-то. И папки с фотографиями."

    "Одну папку с фото, где все в военной форме, я хотела спрятать под рубашку, но она сильно торчала. Тогда Алиса мне показала, чтобы я вынула фото из папки. И я одну пачку фотографий положила в карман, а вторую сунула за пояс."

    "Ну вот. А один ящик был набит картами. Мы его быстро затолкали в угол, чтобы потом выпотрошить. Потом зажегся свет. Женя быстро вернулась, мы папки сложили и закрыли подвал."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_418.mp3"


    show an_10_01

    "Мы бы еще помогли, но нам надо было репетировать. Только вечером мы смогли рассмотреть нашу «добычу». Вот такая была спецоперация и мы назвали её Спецоперация «Архив»."


    scene bg stage2 with dissolve

    "До вечера еще было время и мы репетировали на открытой сцене и на полянке."

    "Потом Семён сказал Мику: «Поедем хоть на часик отвлечемся, а то голова уже совсем не работает»."


    scene cg boat_sem_mi_guitar with dissolve

    "А она ему: «Ага» и садится в лодку с гитарой. Хех. Обломала Сему. Он наверное хотел «забить ей баки» (как сказала Алиса), но Мику, наш человек, она не повелась."

    "Думаю, она всю прогулку шлифовала проигрыш на гитаре. Хотя... Хотя у Алисы он все равно лучше получается."


    scene bg stage with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_412.mp3"


    "В этом концерте Алиса еще зарубежные песни будет исполнять. И вот эту, для Саманты. Америка, Америка.. Элвиса Пресли. Она даже на английском ее выучила."


    scene cg ul_drums with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_309.mp3"


    "А я не теряла времени и три часа стучала на барабанах."

    "Физрук пришел ругаться. Сказал: «Дай дураку барабан, сам скоро дураком станешь». Это юмор у него такой."


    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"


    "Чему тут удивляться, он же бывший прапорщик. Про них как-то сказал мой папа: «Прапорщики огурцы из банок не едят - голова не пролазит»."

    "Но ОД его отправила на лодочную станцию, чтобы он не мешал. Дала какое-то задание. Он ее слушается. Потому что сохнет по ней."


    scene cg boozy with dissolve

    "А тетя Люба ревнует, идет к Петровичу и говорит: «Налей мне песяшечку (50 грамм) своей Архиповки.» Ну и плачет, а тот ее утешает. Но ОД не смотрит на физрука. Кажется, она на Семёна запала."


    scene cg boat_sem_od with dissolve

    "Это секрет. Но мне кажется, что этот «секрет» знает уже весь лагерь. Иначе как объяснить прогулку ОД на лодке с Семёном? Он сказал, что они осматривали остров, перед предстоящим походом туда нашего отряда."

    "Может оно и так. Но тогда почему Ольга Дмитриевна в последний момент попросила Славю сбегать в их домик и принести ей купальник?"

    "Хотя Славя и Ленка тоже ревнуют, но на Ольгу Дмитриевну не обижаются, она всеобщая любимица. И потом, дело не в ней, а в Семёне. Как говорит моя мама: «Наше дело бабское, ждать да надеяться»."

    "Только когда у меня будут «отношения», я ждать не буду. Это я точно про себя знаю."

    "Ладно, что-то я отвлеклась. Буду писать про концерт."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    show an_10_01

    "Меня вдруг осенило. У нас нет рекламы! Нет объявления о концерте и фото нашего ВИА."


    scene bg fotoc with dissolve

    "Но зато у нас есть Славя и ее фотокружок. Она может нас сфотографировать с гитарами и барабанами. А Семён написал бы объявление. Это была хорошая идея! И мы побежали в фотокружок, он как раз открылся после обеда."


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "И кого вы думаете, мы там увидели? Не догадаетесь никогда. Когда мы вошли, там шла съемка. Они нас не заметили. Славя сидела вся из себя важная, а ее фотографировал... Семён!"

    "А она с яблоком. Ну, типа, она Ева... Хорошо, хотя бы не в костюме Евы."


    scene cg fall with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_460.mp3"


    "А почему я про историю с яблоком знаю. К нам соседка богомольная заходила пока не было родителей и сунула мне брошюрку «Сотворение Мира Господом»."

    "И сказала: «Читай, детка, а то твои родители от тебя правду скрывают, что мир Господь сделал и будет всем безбожникам страшный суд». Ну, я же любопытная. Какие-такие, думаю, еще тайны от меня скрывают."

    "И почитала там про Еву и про яблоко."

    "А потом пришел папа, а я ему про Адама и Еву, а он книжечку у меня забрал, в мусор выкинул и сказал: «Тетку эту с пятого этажа никогда больше к нам в дом не пускай. Она своим детям мозги свернула, а теперь и до нас добралась»."


    scene cg sl_sem_photo with dissolve

    "Ну вот, про Семёна. Он сначала долго возился со светом. Направлял на нее разные лампы. И просил повернуться. То ему тени мешали, то она сидела недостаточно красиво."

    "А мы наблюдали, тихо, они нас не видели. И вот в конце мы увидели такое..."

    "После чего Алиса сказала: «Теперь всё понятно! Это не он ее кадрит, а она его! С ума сойти!»"


    #scene cg sl_sem with dissolve

    "Да... Интересные дела. И неизвестно, что бы мы еще увидели. Но тут Алиса этих голубков вспугнула. А жаль. Я бы на такое посмотрела."


    pause (100000000000000000.0)


    scene bg fotoc with dissolve

    show sp_sl_024:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2  

    "Ну вот, Алиса так прямо вошла, как бы вроде, только что. Славя вскочила и покраснела. Она всегда краснеет, если волнуется."


    scene bg fotoc with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3"


    show sp_sem_025:
        yalign 0.08 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2   

    "Яблоко покатилось. Алиса нагнулась, взяла яблоко, потерла его и протянула Семёну. Он как-то растерялся. А она ему, подделавшись под голос Слави: «Семочка, просто возьми яблочко»."


    scene bg fotoc with dissolve

    show sp_sl_024:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2  

    "Ну тут Славя заерзала и говорит: «Вы зачем пришли?»"


    scene bg fotoc with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1 

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2  

    "А мы с Алисой ей выдали про объявление и фото ВИА."

    "Потом я сказала «Ну если ты занята, то просто можешь дать нам фотоаппарат."


    scene bg fotoc with dissolve

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2  

    "Да, говорит, нет возражений, берите, но только вы мне за него отвечаете. Ну и целую инструкцию нам прочитала, как его хранить, как и куда нажимать, что такое выдержка, диафрагма. Я уже все и не помню."


    scene bg fotoc with dissolve

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2  

    "А Алиса ей: «Не учи ученую. Я знаю, как с фотоаппаратом обращаться. Могу не хуже Семёна снимать»."


    scene bg fotoc with dissolve
 
    "Тут я оглянулась, а Семёна как ветром сдуло. Сбежал."


    show sp_sl_019:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    "А Славя расстроилась."

    hide sp_sl_019


    $ inv_item_12 = True

    scene cg ul_camera with dissolve

    show got_camera

    "Так мы получили фотоаппарат."


    image an_band: #Анимация, смена разных цг с музыкантами
    
        "images/cg/cg_day14/cg mi_sem_stage.webp" with Dissolve(0.5, alpha=True)
        pause 1.5
        "images/cg/cg_day14/cg ul_drums.webp" with Dissolve(0.5, alpha=True)
        pause 1.5
        "images/cg/cg_day14/cg concert.webp" with Dissolve(0.5, alpha=True)
        pause 1.5
        "images/cg/cg_day14/cg al_mi_guitar.webp" with Dissolve(0.5, alpha=True)
        pause 1.5
        "images/cg/cg_day14/cg al_sl_guitar.webp" with Dissolve(0.5, alpha=True)
        pause 1.5 
        repeat


    scene an_band with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    "Потом снимали наш ансамбль. Славе отдали пленку, а она обещала, что они с Семёном утром вывесят красивое объявление о концерте."

    window hide

    pause (100000000000000000.0)


    scene an_d10_01_bg with dissolve

    show an_10_01

    "Представляю их при красном свете в фотолаборатории. Ну прямо «Квартал красных фонарей», как сказал бы мой папа. Он был в командировке в Японии и видел там гейш."

    "Надо Ленке сказать, она точно прибежит им помогать. Я так рассуждаю, нам реклама нужна, а Ленка не даст им отвлекаться."

    "А мы с Алисой побежали в домик и там валялись на кроватях и смеялись, вспоминая, как Славя вся покраснела как помидор. В общем, вспугнули голубков."


    scene cg meeting with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "В общем, не все у нас шло по плану. И всему виной второй отряд. Они почему-то решили устроить забастовку. Есть у них там один баламут. Бывший пионервожатый. Смутьянов его фамилия. Вот он и мутил там воду."


    scene bg stage8 with dissolve

    show sp_smu_007:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 0.5

    show sp_od_025:
        yalign 0.5 subpixel True
        xalign 0.23 subpixel True
        zoom 0.5

    "То ли у них какие-то терки с ОД вышли, то ли они просто решили сачкануть, но в общем, в программе образовалась дыра. И надо было эту дыру как-то заполнить. У нас же все рассчитано до секунды. Ну все, понятное дело, заметались."


    image an_14_02: # Анимация трансформация ОД 3 (взята из 11 дня + 1 кадр)
        
        "images/an/an11day/an_d11_17.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_16.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_17.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_18.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_17.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_19.png" with Dissolve(0.5, alpha=True)
        pause 0.5


    scene an_d11_03_bg

    show an_14_02

    "Ольга Дмитриевна покраснела как «маков цвет», бровки домиком, ломает руки  и все время спрашивает: «Что делать будем?» И почему-то у Семёна. Вроде он как скорая неотложная помощь."

    "Он только плечами пожимает. А у нас, как на зло, ни одного номера больше нет."


    scene bg hide_bench with dissolve 


    stop music fadeout 0.5

    queue music "audio/music/z_451.mp3"
 

    show sp_pe_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И вот тут выручил Петрович!"

    "Оказывается, он в молодости в театральной самодеятельности выступал. С аккордеоном!"


    scene bg genda_blured with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Где я вам аккордеон возьму, Архип Петрович?"


    scene bg hide_bench with dissolve  

    show sp_pe_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe "Есть аккордеон у меня, немецкий, трофейный."


    scene bg genda_blured with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "А что вы на нем играть будете? Надеюсь, не немецкие песенки?"


    scene bg hide_bench with dissolve  

    show sp_pe_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe "Могу и немецкие. Однако я приберег наши военные песни. Катюшу, Синий платочек и в таком роде. В общем, патриотические. Которых все слова знают."

    hide sp_pe_002

    show sp_pe_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Вот я запою, а молодежь подхватит. В наше время все знали эти песни."


    scene bg genda_blured with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_453.mp3"


    show sp_od_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Хорошо, я попробую мобилизовать малышей из хора. Надеюсь, Хетсуне к Дню Памяти с ними репетировала военную тематику. Только уж вы своим скрипучим баритоном не портите впечатление. Сделаете затакт и дети начнут. Ладно?"


    scene bg hide_bench with dissolve  

    show sp_pe_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe "А чем вам мой голос плох? В былые времена все  сестрички из медсанбата приходили послушать, как поет боец Сохатый. Бывало даже, под мой аккордеон танцы устраивали. Я и польки разные знаю и краковяк. Во как!" 


    scene bg genda_blured with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Ну что вы несете, кто сейчас танцует краковяк? Еще скажите мазурку!"


    scene bg hide_bench with dissolve  

    show sp_pe_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    pe " О! Мазурку могу! Хороший танец." 


    scene bg genda_blured with dissolve

    show sp_od_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    od "Нет! Не надо, я вас умоляю. Давайте уж лучше вашу Катюшу с Синим платочком."


    scene cg pe_accordion with dissolve

    "Петрович сходил в свою каптерку и принес аккордеон. Сел на лавочку и ка-а-к запоет дурным голосом, частушки."


    scene cg pe_ul_accordion with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_452.mp3"


    "Все пионеры прибежали. Насилу его Маргарита Павловна с Ольгой Дмитриевной угомонили."

    "А ОД спрашивает: «Вы, Архип Петрович, сегодня принимали?»  А он обиделся. За кого, говорит, Ольга Дмитриевна, вы меня держите. Я на работе не пью. Хотел уйти совсем. Насилу отговорили. А аккордеон у него, и правда, классный!"



    pause (10000000000000000000000.0)


    scene black with fade

    stop music fadeout 1.0

    jump day15

return   
  










