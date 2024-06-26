label day12:

    $ style.say_window = style.window

    $ days = 12

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = True
    $ adv_15 = False



    $ im_gal_11_00 = True



    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day

    $ show_quick_menu = True


    scene bg pfis with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_012.mp3"


    "После разговора с Пионером, я всерьез задумалась о баркасе. Кто бы мог его починить, если не кибернетики. Начать надо с обычной лодки. Пусть починит старую, что лежит на Рачьей отмели."

    scene bg ul_el_boat

    "Надо же на чем-то добраться до Острова. Заодно, можно будет сбегать из лагеря и кататься когда захочется. Но стимул… Так просто никого из них от их идеи с роботом не оторвать. Должна быть веская причина."

    "Я заметила, что Электроник симпатизирует Жене. «На эту кнопку стоит нажать», как сказал бы мой папа."

    scene bg handmade

    "После завтрака я заскочила в мастерскую, где кибернетики в сотый раз переделывали свою куклу и поманила Электроника пальцем."

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Слушай.. Пойдем я тебе что-то покажу."

    hide sp_ul_013

    show sp_el_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Да ну, опять твои глупые идеи. Не впутывай меня в очередную историю. У всех еще на слуху случай с лягушонком и котлетой."

    hide sp_el_001

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да нет же! Это другое. Это касается Жени."

    hide sp_ul_013

    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Что? Жени? Ну ладно... Пойдем."


    scene bg fbeach


    stop music fadeout 0.5

    queue music "audio/music/z_198.mp3"


    "Мы ушли довольно далеко от лагеря по берегу реки, пока не уткнулись в старую лодку, лежащую на берегу."

    scene bg fbeach at flip

    show sp_el_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Ну и.. Я весь во внимании."

    scene bg fbeach

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Видишь лодку? Мог бы ты ее починить?"

    hide sp_ul_013


    scene bg fbeach at flip

    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "(Обследуя лодку) \nНу в принципе ничего сложного, она в неплохом состоянии. Тут вот рассохлось, тут немного подшпаклевать, заклеить дыру стеклотканью с эпоксидкой и так, по мелочам."

    el "А зачем? На станции же есть лодки и вполне себе целые. И при чем тут Женя?"


    scene bg fbeach

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Вот, мы подошли к главному. Только это большой секрет. Обещай, что никому ничего не скажешь, особенно своему другу Шурику. Он любит сболтнуть лишнего."


    scene bg fbeach at flip

    show sp_el_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Обещаю."


    scene bg fbeach

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Так вот. Как-то мы гуляли тут, я, Женя и Алиса. Ну ты знаешь, Женю вытащить на пляж купаться и кататься на лодке, невозможно. Она стесняется."

    hide sp_ul_012
    
    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Но увидев лодку, она сказала, что покаталась бы подальше от лагеря с нами, если бы конечно эта лодка была на ходу."
    
    scene bg fbeach at flip

    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Ну, да."


    scene bg fbeach

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Все лодки на станции контролирует завхоз и Славя тоже вечно присматривает и докладывает ОД кто куда катается. А тут есть возможность сгонять на остров и никто ни о чем не догадается. Эта лодка не стоит на учете."

    ul "Если починишь, я уговорю Женю, чтобы ты покатал нас. Тем более, что грести толком никто из нас не умеет."

    
    scene bg fbeach at flip

    show sp_el_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Хм. Идея заманчивая... Ладно. Я подумаю. Только вы очень рискуете. Это не близкое путешествие. Нужно будет уложиться до отбоя, если я починю эту лоханку и мы сможем выехать после ужина."
 
    hide sp_el_003

    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    el "Да, кстати, нужно будет достать весла. И это... Где мы ее потом прятать будем?"


    scene bg fbeach

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Это я беру на себя."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    show an_10_01

    "Как я уже писала, в лагере много чего происходит. Например, играют в разные игры. В садовника, в колечко, в классики, в победу, в апанаса, в царя горы, в казаки разбойники и другие, все не перечислишь."

    "Но вот одна из игр, которую придумал (как позже выяснилось) Смутьянов, произвела в лагере настоящий переворот. Был даже большой шум по этому поводу с участием директрисы, собрание и костер, который мы назвали Инквизиция."

    "Ну так вот, расскажу по порядку. Все началось с тренировки Тараса Юрьевича по надеванию противогазов. Оказывается, в нашей стране каждый должен быть готов к ядерному или химическому нападению."

    "А для этого надо уметь правильно действовать (так он сказал)."


    scene bg acthall with dissolve

    "И нас собрали в актовом зале (музкружке), куда физрук велел принести целый ящик противогазов и всяких плакатов. На плакатах были нарисованы схемы ядерного нападения."

    show sp_fi_012:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2   

    "Нам раздали противогазы и Тарас Юрьевич сам показывал как надо их надевать. Было смешно. Потому что мы никогда не видели физрука в противогазе. А он в нём был похож на слоника."

    "Потом все стали надевать и стали похожи на стадо слонов. Физрука позвали к директрисе и он сказал – «Ждите меня и не балуйтесь!»"

    hide sp_fi_012


    stop music fadeout 0.5

    queue music "audio/music/z_075.mp3"


    "Но как только он ушел, такое началось! Стадо слоников бегало по музкружку под звуки рояля и трубило хоботами."

    "В основном, это были малыши. Но если честно, идея дурачиться исходила от нашего отряда. Потому что Мику стала играть собачий вальс и все стали бегать. Ну и понеслось."

    show sp_fi_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2   

    "Бог знает, до чего бы мы там доигрались, но вскоре пришел Тарас Юрьевич и, как он сам выразился, «привел всех к общему знаменателю»."

    hide sp_fi_003

    "Я тоже бесилась, но совсем чуть-чуть. Поэтому было обидно, когда меня одну выгнали из зала. Но я подглядывала в щелочку в двери и всю лекцию про атомный взрыв запомнила."

    "И вот тут самое интересное. Тарас Юрьевич рассказал, что после взрыва все кто не спрячется, будут заражены и превратятся в зомби. Будет Апокалипсис (я специально записала это слово новое)."

    "И даже показал этих зомби. Всем понравилось, и когда лекция закончилась, все стали изображать зомби."


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_smu_003:
        yalign -0.0 subpixel True
        xalign 0.4 subpixel True
        zoom 1.2

    "И тут Смутьянов выдвинул идею играть в «Зомби апокалипсис»."

    hide sp_smu_003


    image an_12_03: #Анимация летучие мыши

        "images/an/an12day/an_d12_20.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_21.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_22.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_23.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat            

    scene bg square with dissolve

    show an_12_03

    "И мы разделились на зараженных и не зараженных. Ну, по желанию конечно. Зомбаками стали весь второй отряд и часть малышей. И также, кто-то из третьего отряда. У нас в зомбаки пошел Семён и кибернетики."

    "И они объявили что они мутанты и вампиры, придумали что на Совенок опустилась вечная мгла и всякие правила. В общем, кого укусят тот становится зомбак. Они разработали тайный шифр, свое знамя и эмблему."

    "Потом придумали, что убивает зомби и правила. Их убить, оказывается, почти невозможно. Я была на «светлой стороне», а со мной Алиса, Славя, Атсуи, Саманта и Мику."


    scene black with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_193.mp3"


    show sp_sem_014:
        yalign -0.0 subpixel True
        xalign 0.5 subpixel True
        zoom 0.7

    "Семён стал главным вампиром."


    scene cg lena_vamp with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_192.mp3"   

    
    pause (10000000000000000000.0)

    "А Ленка сначала была на нашей стороне, но потом от нас сбежала."

    "Позже мы узнали, что она «девушка главного вампира» (ну кто бы сомневался)."


    scene bg square with dissolve

    show an_12_03

    "Толик был за нас, но от нас переманили Женю. Она правда нас успокоила, сказала что будет «засланным казачком» . И все зомбаки нарисовали себе черные тени под глазами."


    scene cg zhenya_vamp with dissolve

    pause (10000000000000000000.0)

    "Лучше всего тени шли Жене. Она была такая «грустная вампирша». Она  нарисовала себе кровь вокруг губ, изменила прическу (кстати, ей идет). Жуткое зрелище."


    scene bg square with dissolve

    show an_12_03

    "В общем, лиха беда начало. Придумали свой вампирский язык. И мы не понимали, когда вампиры в столовке о чем-то при нас договаривались, потому что они говорили на тарабарском языке."

    "И было страшно. Смотрят на тебя и о чем-то говорят и улыбаются. А ты не понимаешь. А они может, говорят, как они тебя съедят вечером... Жуть."


    scene bg full_moon with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_194.mp3"   


    "А еще в лагере стали выть по ночам. Особенно когда луна. Страшно было. Хоть мы и знали что это наши вампиры воют понарошку. Но волки в горах не знали и отзывались."

    "Тогда становилось действительно страшно. Даже вампирам."


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"   


    "Но буча началась не из-за этого, а из-за СИМВОЛИКИ."

    "Смутьянов придумал эмблему вампиров. Они там переделали эмблему Совенка и у них получился «темный Совенок», а лагерь они переименовали в «Беспросветный». Бывший Совенок."


    scene black with dissolve

    show cg emblem
 
 
    pause (100000000000000.0)


    "Ну и вот, все зомбаки пришили себе эту эмблему. И бегали в ней. И шла игра полным ходом."

    "Начальство лагеря сначала ничего не понимало (как позже скажет директриса, «масштаба трагедии») и думало, что мы играем в догонялки и всякие «секреты»."

    "Но потом, у кого-то отвалилась эмблема (когда очередную «жертву» поймали и несли на убой). А Петрович нашел эту эмблему и отнес Ольге Дмитриевне, а та директрисе. Ну и начался шум. Расследование."

    "Директриса кричала «Так мы тут до черных галстуков доиграемся! У нас образцовый лагерь, позор! Это политическое дело!»"

    "И прям все с похоронными лицами и физрук такой серьезный. И вся администрация. Только что милицию не вызвали."


    scene bg square_day with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_195.mp3"


    show sp_fi_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    

    "Тарас Юрьевич на линейке со всех сорвал эмблемы, всех заставил умыться и убрать краску (а еще клыки заставили отклеивать)."


    scene cg large_campfire with dissolve

    "А потом, все отряды построили и торжественно отвели на поляну слетов. Там разожгли пионерский костер и сожгли всю «нечисть» (ну, то есть наши эмблемы, повязки, шифры и знамя зомбаков)."

    scene cg large_campfire

    pause (100000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_083.mp3"


    "И Маргарита Павловна произнесла пламенную речь. Ну, типа «фашизм не пройдет». Прямо настоящая инквизиция. Все было круто. Мне понравилось. Но я так и не поняла, при чем тут фашизм."

    "Мы с Алисой по этому факту вели расследование и в интересах расследования украли вещдоки (вещественные доказательства) и спрятали."

    "Потом физрук и с ним «правильные пионеры» искали по домикам остатки атрибутики вампиров, но нашу нычку не нашли."


    scene cg vamp_banner with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_196.mp3"


    "Они, например, не знали, что одно запасное черное знамя, Вампиры отдали Шурику (он был самым фанатичным вампиром и пользовался у них уважением) и он его обернул вокруг тела (так не нашли). А потом отнес нам и мы спрятали."

    "В общем, вампиры ушли потом в подполье. Глаза уже не красили, но говорили на своем языке. И еще неделю были всякие укушенные, которых обращали в нечисть."

    "Потом, постепенно, всем надоело в это играть и их вампирское сообщество распалось. Нам было жалко вампиров, все-таки с ними было весело. Но им пришла амба. Как сказал Семён «Такова селява»."

    "Вот то, что мы сохранили с Алисой. Для Истории."


    scene bg evening_camp with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


    "После вечерней проверки и отбоя мы с Алисой, тихонько взяв всё приготовленное для рыбалки (фонарики, кое-какую еду и куртки, чтобы не замерзнуть ночью), отправились к Петровичу, который уже ждал нас у лодочной станции."


    scene bg boat_fishing_1 with dissolve

    "Он пожурил нас, что мы долго копались."

    pe "Ну, теперь ждите, пока я скурю еще одну, и понаблюдаю, нет ли за вами «хвоста»."

    al "Обижаете, мы очень тихо смылись. А что это лодку снизу так поддевает? И какие-то всплески... Вода прямо как будто светится."

    pe "Это рыба играет. А свет от чешуи. Отражает чешуя свет. Эх вы рыбаки-знатоки."

    ul "Мы  в курсе. Читаем научную литературу. Просто спросили, чтобы Вас проверить."


    image an_12_01: # Анимация Петрович, Ульяна и Алиса в лодке, всплеск
        

        "images/an/an12day/an_d12_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_10.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_11.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_12.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_13.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat

    scene an_d12_01_bg with dissolve
    
    show an_12_01

    pe "Да уж. Специалисты. Проверяют они меня. Зеленые вы еще меня проверять. С такими знаниями вы не то что сома, а плотвы не поймаете."

    "Было так тихо, что даже звуки падающих с весел капель воды казались нам громкими."


    image an_12_02: # Анимация Петрович, Ульяна и Алиса в лодке, плывут
        

        "images/an/an12day/an_d12_14.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_15.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_16.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_17.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_18.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an12day/an_d12_19.png" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat

    scene an_d12_02_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_004.mp3"


    show an_12_02

    "Петрович докурил и налег на весла. Берег быстро удалялся. Течение подхватило лодку."

    al "Весла шлепают... А мы не вспугнем сома?"

    pe "Не бойся, девонька, нам еще плыть и плыть. Видите, какое течение? Надо брать ближе к броду, тогда аккурат снесет к омуту."

    pe "Да вы не ерзайте тут! А то, понимаешь, раскачали лодку. Ты, рыженькая, на руле, правее бери, правее! Вот, так держать!"


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Я заметила, что левый берег, вдоль которого мы плыли, стал двигаться быстрее, о чем я и сказала Петровичу."

    pe "(Грозно) \nСам вижу! Похоже нас на водоворот несет. Эх, старый дурак, не угадал, в каком месте надо на стремнину выходить! И не мудрено, темень-то какая!"


    scene bg dwhir with dissolve

    
    ul "Водоворот, это который Смертельный?"

    pe "Он самый! Только он смертельный осенью, когда вода с дождями прибывает."

    al "Не бойся, Улька, у нас опытный капитан! С Петровичем нам никакие водовороты не страшны!"

    ul "Что-то мне как-то не по себе. А у нас даже спасательных жилетов нет."

    "Лодка со стуком причалила к небольшой пристани."

    pe "Не зевай, Ульянка, хватай цепочку, приматывай лодку, а то унесет нас! Видишь, кол торчит, за него приматывай. А я придержу веслами. Да живее, живее!"

    al "(Помогая закрепить лодку) \nДавай, я."

    ul "Я сама!"


    scene bg first fishing with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_179.mp3"


    al "Ой, да это маленькая пристань! Откуда она тут? "

    pe "Всё, вылезайте. Да рюкзаки не забудьте, а я снасть возьму. Откуда... Вот этими руками сделана. \n(показывает мозолистую ладонь)"

    pe "Тут её никто не видит. Громко сказано, пристань! Четыре доски да сваи, вот и вся пристань."

    al "А почему тут?"

    pe "Заповедное место. Клёв тут отличный. Щука сюда любит захаживать. А наши поселковые браконьеры, как узнают, так сейчас же сюда и нагрянут. Вы уж не болтайте нигде про то, что видели."

    ul "Будем немы как рыбы."


    scene bg fishing_dialogue with dissolve


    pe "Ну, пошевеливайтесь. Вот так, через камыши идите, светите фонариком. Тропинку видите? Вот по ней и идите. Она точно к омуту нас выведет."

    "Тропинка, петляя, вывела нас, как и говорил Петрович, к широкой полоске тихой воды. Это была протока от впадающего в Бурлейку ручья."

    "Название ручья мы не знали. И на карте его не было. Поэтому я назвала его Скрытный. Непременно нанесу его на свою секретную карту."


    scene bg little_pier with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_182.mp3"


    ul "Ой, красиво как! И луна со звездами в воде светится дорожкой. Интересно, тут глубоко?"

    al "Не шуми, сома вспугнешь!"

    pe "Глубину никто не мерил, только я как-то закинул донку, там метров двадцать будет лески. Прямо с лодки с грузилом, так она на дно не легла, вертикально стояла. Вот сама и подумай, какая тут глубина."


    scene bg fishing_dialogue2 with dissolve


    ul "А с виду не скажешь."

    pe "Потому, что туман покрывает воду. Течение тут быстрое, но на глубине. А сверху вроде тихая вода. Обманывает омут."

    pe "Тут ещё драга раньше работала, золото мыли. В царское время. Я вам намедни рассказывал. Ну и вычерпали много грунта со дна. Видите, холм большой?"

    al "Какая большая гора песку. Это всё со дна?"

    pe "А то. Этот холм у нас местные уже лет тридцать копают и вывозят. Как строить что, песок завсегда нужен. А он, холм этот, всё не кончается."

    ul "Может в нем золотой песок остался? Я бы покопала."

    pe "До тебя все перерыли. Охотников много. Первым делом костер разведем и посидим тихо. Перед каждым делом подумать нужно. Настроиться. Через час он должен начать плескать. Всегда в одно время, в двенадцать ночи."

    al "Пунктуальный Сом."


    scene bg fishing_dialogue1 with dissolve


    pe "Видите ручей? За ним протока, а слева холм.  Там полянка хорошая, там разводите. А я заброшу прикормку. Запах ему нужен, чтобы к берегу подошел. На мелководье его, если что, потянем."

    ul "А мы не прозеваем сома?"

    pe "Нет. Багор у меня. Как крикну «Подсобляйте!», чтобы сразу бежали ко мне и навалились разом. Во мне и шестьдесят кило не будет, утащит. Вы хоть и тощие, а всё какой-никакой  довесок."

    al "Я не тощая, а стройная. Правда, Улька?"

    ul "Правда. Деда, а если он вас будет тащить, мы вас будем держать. Не бросим, мы верные."

    pe  "Не бойся, милая, рыба хитрая, а рыбак хитрее. Видишь, на багре веревка привязана? Вон я её за бревно, что от упавшего дерева, привязал."

    ul  "Небось, бревно не утащит."

    pe  "Там пудов пять будет. Да нас ещё трое. Главное, багром его зацепить, уж тогда он от нас не вырвется. Ну, иди к костру, а я покурю малость. Пока греб, прямо замаялся без курева."


    scene cg fishing_campfire with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_180.mp3"


    "Прошло уже два часа, а сом всё не показывался. Минули обещанные Петровичем двенадцать часов."

    pe "Видать, нынче не свезло. \n(размотал длинный сверток с удочками)"

    pe "А ну-кась, идите ко мне! Прикормил-то я хорошо. Вон, вижу, ходит рыба. А его величество, будь он неладен, не изволил пожаловать. Так половим."

    ul "Деда, а кто ещё ночью пасется? Кого ловить?"

    pe "Ну как же… Известное дело, угорь, карась, лещ, крупная плотва. Тут в иные времена такой клев, только успевай вытаскивать! Помогайте разматывать."

    pe "Ты, Рыжая, вон там стань, а ты, малая, ей помогай. Сачок рядом положи. Если большой лещ, то под него сачком подводи. Да не пугайтесь, коль угорь клюнет. А то он шибко на змею похож."


    scene cg fishing_civil with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_076.mp3"


    "Пошла рыбалка. Алисе везло. Она то и дело выдергивала из воды блестящие в лунном свете, бьющиеся тела."
 
    "Мне попадалась только плотва. Я сопела и упорно не желала менять место. Мне казалось, что рядом с Алисой обязательно должно повезти. Та прикрикивала на меня, когда я пристраивала свой поплавок рядом."
 
    al "Запутаешь же мне  леску, дурында!"
    
    "Петрович же с методичностью автомата таскал угрей, не вынимая цигарки изо рта. Снимая рыбу с крючка, качал головой, наблюдая, как мы препираемся."

    "Ведра у Алисы и Петровича наполнялись быстро. Только в моём, лежали и хватали воздух, выпучив глаза, несколько плотвичек."


    scene cg catfish3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_149.mp3"


    pe "Тихо! А ну, ходи от берега!"

    "Петрович бросил удочку и леопардовым скоком кинулся к рюкзаку, рядом с которым лежал багор."

    pe "Кажись, он!"  

    "Мы быстро ретировались, наблюдая за хищными движениями Петровича."

    "Старик преобразился. Он был как сжатая пружина. Багор в его руке мрачно поблескивал. Он крался вдоль бревна, к которому до этого привязал снасть и что-то бормотал."

    pe "Давай, милый, давай."

    "Дрожащей рукой Петрович вытащил фонарик и подняв его вверх включил так, что луч уперся в небо."

    ul "Что он делает?"


    scene bg pool_big_catfish_bloody_night with dissolve

    al "Светит вверх. Охотники так делают. Я раз такое видела. Зверь или рыба не видят так  фонарика,  луч вверх уходит, а в нужный момент резко вниз на добычу. Раз! И готово."

    "Брошенная удочка Алисы вдруг дернулась и медленно поползла к воде. Алиса молнией метнулась к ней. Но Петрович оказался проворнее. Не успела Алиса поднять удилище, как в воздухе сверкнул нож и леска со звоном оборвалась."

    "Не ожидавшая такого поворота Алиса, наклонившаяся назад, чтобы компенсировать сопротивления лески, упала на спину. Потом обиженно поднялась и, потирая ушибленное место, воскликнула:"

    al "Вы чего, Петрович! У меня же клевало!"

    pe "Клевало-то клевало, да только беда бы вышла. Его на твою леску не возьмёшь."

    "Петрович вытащил из рюкзака большой моток капроновой веревки с огромным крючком, от которого шел стальной тросик. На крючке, завернутая в промасленную бумагу уже торчала насаженная приманка."

    "Сняв бумагу, Петрович с любовью оглядел кусок чего-то жирного и розового, понюхал его и поморщился."

    pe "Вот, свининка,  лежалая, как раз дух дала. Он тухлятинку-то любит. И чтобы запах обязательно был."

    al "Да уж. Запах, прямо скажем, не запах, а вонища."

    "Петрович усмехнулся. Размахнувшись, он ловко забросил приманку почти на середину омута и стал тихонько потягивать её на себя, как бы выбирая нить."

    "Щас, на дно ляжет, вот тогда самое оно и начнется. Не зевай! Держи крепче! Ты, малая, становись ей за спину, а я багор возьму."

    "Но очевидно, сом был очень голодным. Почти сразу капроновая нить резко натянулась и опрокинув нас с Алисой, быстро стала уходить под воду."


    scene cg catfish2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    pe "Врешь, гад! Не уйдешь!"

    "Свободной рукой Петрович схватил ускользающую веревку и жилы на его худой сухой руке вздулись от напряжения. Лицо с клочковатой жиденькой бородкой перекосило. Желтые прокуренные зубы обнажились в счастливом оскале." 

    "Увлеченные его азартом, мы тоже заорали «Ааа!», которое, если честно, от сильного напряжения было больше похоже на «Ыыы!»"

    "Между тем, скорость движения «лески» только возросла. Как будто на ней не висело три тела и не волочилось привязанное бревно в пять пудов весом."

    "Петрович бешено колотил по земле багром, стараясь воткнуть его в песок и затормозить наше движение. Но багор, как назло, всё время срывался. Песок не держал. Кромка воды приближалась стремительно."

    "Вдруг на поверхности воды появился огромный бурун и из него показалась круглая и блестящая, с темными точками наростов, голова. Затем спина и огромный хвостовой плавник."

    "Это был настоящий монстр! Сом был явно больше нашей лодки. Значительно больше! Хвост сделал сильный взмах и махина снова погрузилась, утаскивая нас в воду."

    "Петрович упал, но ему удалось зацепиться багром за корень ивы, растущей у самой кромки воды. Я тоже упала."

    "Когда я встала, то увидела удаляющуюся по воде Алису. Она была как катер на подводных крыльях и ее несло на середину омута. Веревка еще сильнее натянулась и лопнула."

    pe "Бросай, не держи! Утянет же!"

    "Петрович бросился к воде, в горячке машинально пытаясь снять с себя разорванную рубаху."

    ul "Алиса, держись! Я уже плыву! \n(ныряет в воду)" 

    "А когда я вынырнула, то увидела Алису. Было заметно, что она сильно устала и уже плыла мне навстречу. Но течение относило нас не на песчаный пляж, а на стремнину."


    scene bg ushallow with dissolve

    "Я знала по рассказам Петровича, что рядом с омутом, вниз по течению была мель и была еще возможность до нее добраться, если мы справимся с течением. Я сделала знак Алисе, чтобы она гребла в сторону протоки."

    "Алиса вцепилась в мою руку и мы вместе ухватились за багор. Пыхтя, Петрович выволок наши мокрые, обессиленные тушки на берег. Но у нас не было сил подняться."

    "Петрович опустился рядом. Очевидно, забег с багром вдоль берега и борьба с течением, отняли у него последние силы."

    
    stop music fadeout 0.5

    queue music "audio/music/z_088.mp3"


    "Неожиданно, он расхохотался. Мы тоже начали смеяться. Сначала нервно, а потом всё более задорно."

    al "Даа, спецотряд не знающих пощады охотников на сомов! ОХотников НЕпобедимых и МОГУчих! Сокращённо «ОХ, НЕ МОГУ»! Ох, не могу, сейчас умру от смеха!"

    "Алиса так хохотала, что слезы катились у неё из глаз. Я не отставала. Но больше всех смеялся Петрович. А сом… Сом, видно, ушел к себе в домик, в свой глубокий омут."


    scene cg fishing_campfire with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_180.mp3"


    "Мы посидели немного у костра. Потом, по совету Петровича, распотрошили и присолили рыбку. Аккуратно сложили ее в ведро и закрыли целлофаном. Затем вернулись на Маленькую пристань."


    scene bg little_pier2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_181.mp3"


    "Наша лодочка  мирно покачивалась на воде, привязанная рачительным хозяином крепкой цепочкой. Цепочка позвякивала. Лодка тоже время от времени покачивалась, издавая сдвоенный стук лежащих на дне весел."

    "Странное сочетание звуков... В целом, картинка была, как сказала бы Ольга Дмитриевна, «идиллическая» и просилась на холст художника. Как будто и не было никакой  битвы с Сомом и кутерьмы со спасением."

    "И я подумала, что глядя на мирно качающуюся на воде лодку, можно и не заметить, как пролетают годы, войны, людская суета. И в голову полезла, как сказал бы мой папа, «всякая детская философия»."

    "Но вскоре Петрович окликнул нас, потому, что надо было возвращаться."

    "Я поудобнее устроилась в лодке и подумала. Может и хорошо, что мы его не поймали, этого Сома. Иначе, никакой легенды бы не было. А так – есть. И еще появилась новая легенда, легенда о том, как мы ловили Большого Сома."




    #pause (10000000000000000000000.0)


    scene black with fade

    stop music fadeout 1.0

    jump day13

return