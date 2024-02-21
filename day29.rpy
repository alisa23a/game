label day29:

    $ days = 29

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    image an_29_01: # Анимация Ольга Дмитриевна разговор
        
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


        repeat


    scene an_29_01 with dissolve


    pause (10000000000000000000000.0)


    scene cg od_book_talk with dissolve

    "Неожиданно Ольга Дмитриевна вызвала нас к себе."

    "Когда мы вошли, у нее на столе лежала книга «Унесенные ветром». И Алиса прошептала: «Так вот что она все время читает на пляже. А нам Женя эту книгу не дала»."

    od "Есть задание, которое я никому кроме вас не могу поручить. Вы вроде самые хулиганистые..."

    od "В хорошем смысле... \n(поправилась она)"

    od "И наверняка вы найдете подход к таким же пионерам. Поэтому я попрошу вас об одной услуге."


    scene cg book_room with dissolve


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    "Мы обе обратились в слух. Это было неожиданно."


    scene cg od_book_talk with dissolve

    od "Во втором отряде есть мальчик. Проблемный мальчик. Бывший староста отряда. Его даже назначали вожатым."

    od "Так вот... \n(откашлялась)"

    od "Он убежал куда-то на реку и скрывается в шалаше. Дети из второго отряда носят ему туда еду. Он шлет записки."

    od "Мы с Маргаритой Павловной решили не применять к нему никаких наказаний, пока он сам не поймет свои ошибки. Хотя, он, конечно, сбивает с толку отряд и плохо влияет на лагерь."


    scene cg book_room with dissolve


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al "А что от нас-то нужно, Ольга Дмитриевна? Мы же его знаем поверхностно. Ну, пару раз купались вместе и еще на спортплощадке виделись."

    al "Он если не бузит, то просто сидит на лавочке. Никогда не играет. Он какой-то нелюдимый."


    scene cg od_book_talk with dissolve

    od "Очень даже «людимый»."

    od "Скажу больше. Он буквально загипнотизировал весь свой отряд. Пользуется у них непререкаемым авторитетом. Нового вожатого почти никто не слушается. Создал какую-то секту. Имени себя."

    "В её голосе прозвучало плохо сдерживаемое раздражение."

    od "В общем, так. Найдите его и побеседуйте. Как пионеры с пионером. Не говорите, что я вас послала."

    od "Тебе, Двачевская, я дам посмотреть характеристику на него. Только верни мне её после обеда, хорошо? Эти документы выносить нельзя. Но вы же меня не подведете?"


    scene cg book_room with dissolve


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    al "Хорошо, сделаем что сможем. Правда, Улька?"

    hide sp_ul_012


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    ul "Любое задание пионерской организации пионеру по плечу!"


    scene cg od_book_talk with dissolve

    "Ну вот и ладненько. Уговорите его вернуться. Остальное я беру на себя. Это надо сделать до приезда его родителей. Они приедут в субботу."


    scene bg camp_artifacts with dissolve

    "С папкой «Личное дело Владимира Смутьянова» под мышкой,  мы вышли на улицу."


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve


    al "Так вот где собака порылась. Они боятся что родители, не обнаружив сына, устроят скандал."


    scene bg auhouse2 with dissolve

    "Мы пришли в наш домик и сели пить компот с печеньками, которые принесли из столовой."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"


    scene cg smu_docs with dissolve

    al "Та-а-ак. Посмотрим, что за перец такой этот Смутьянов."


    "Я устроилась рядом с ней поудобнее и мы открыли папку. Там лежали какие-то бумаги и среди них ХАРАКТЕРИСТИКА."

    "{i}Владимир Ильич Смутьянов. Родился г. Сумы. Отец – директор кирпичного завода. Мать – домохозяйка. В лагере – староста второго отряда.{/i}"

    "{i}Отличник. До появления в лагере ни в чем подозрительном замечен не был. По отзывам преподавателей своей школы – тихий, незаметный, вежливый.{/i}"

    "{i}Однако, после первых трех дней нахождения в лагере, начал вести себя странно.{/i}"

    "{i}В беседах у костра высказал теорию лучшего устройства лагеря, которая сводилась к лозунгу: «Взять всё да и поделить».{/i}"

    "{i}Имеет приверженцев своей теории среди пионеров. Оказывает заметное влияние на неокрепшие умы. Устраивает ночные маевки на полянке за лагерем.{/i}"

    "{i}Раздает всем оформленные от руки листовки с карикатурами на администрацию и призывами оказать сопротивление режиму и не ходить строем, а также требовать надбавки к пайку в столовой.{/i}"

    "{i}Энергичен, всё время что-то пишет в блокнот и бормочет «Я им тут устрою». Физрука назвал «малютой скуратовым», за что был посажен в изолятор лагеря, из которого устроил побег при помощи соратников.{/i}"

    "{i}Построил шалаш, скрывается в камышах, куда последователи «смутьянизма» приносят ему украденные в столовой сухари и котлеты.{/i}"

    "{i}Пишет капитальный труд – «Лагеря и мракобесие в современной России». Нуждается в особом присмотре и оргвыводах.{/i}"


    stop music fadeout 1.0


    play miscSounds "audio/music/z_001.mp3"

    $ renpy.music.set_volume(0.50, delay=1.0, channel='miscSounds')

    play music "audio/music/z_131.mp3"


    scene bg crsh with dissolve

    "После обеда мы отправились на Рачью отмель."

    "Мы прошли её всю. Никого не было. Только на берегу догорал оставленный кем-то костер. В камышах мы нашли аккуратно сложенные жерди и ветки от шалаша."


    scene bg crsh2 with dissolve

    show sp_al_056 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    al "Ага, понятно. Далеко от шалаша он не ушел. Наверное, затаился в камышах. Надо позвать его, но как?"

    al "Он вообще-то заносчивый, и если давить на его трусость, то он тут же начнет опровергать и выдаст себя."

    hide sp_al_056

    show sp_al_037 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Громко что бы слышал тот, кто прячется в камышах) \nБорцы за всеобщее счастье в кустах трусливо не прятались, а сражались и встречали опасности лицом к лицу!"
 
    al "Мы думали, что придем и увидим не мальчика, но мужа!"
   

    scene bg crsh3 with dissolve

    "Через минуту сзади послышался шелест камыша и на песчаный берег вышел Смутьянов."

    show sp_smu_009:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1
    with dissolve

    "Вид у него был помятый, но гордый. В руках он держал кусок, явно украденной из буфета, краковской колбасы. Не переставая жевать, он подозрительно оглядел нас и обошел по кругу."

    "Потом, вытянув руку в нашу сторону и указывая почему-то на меня этим огрызком колбасы, с пафосом произнес:"

    hide sp_smu_009

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1
    with dissolve

    smu "Во-первых, я не трус. Во-вторых, это греческое выражение, к классовой борьбе отношения не имеющее."

    smu "Если вы хотите заманить меня в западню по просьбе вашей, узурпировавшей власть воспитательницы, то зря стараетесь."


    scene bg crsh2 with dissolve

    show sp_al_056 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al "Никто тебя никуда не заманивает. И прекрати говорить дурацкими лозунгами. Ты не на митинге. Мы к тебе пришли с предложением."


    scene bg crsh3 with dissolve

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1

    smu "(Сложив руку на груди и приняв независимую позу) \nЯ весь во внимании."

    smu "Чем вы можете меня удивить, говоря с чужого голоса? Вы же там, в первом отряде, все зомбированы лагерной пропагандой. Трясетесь за свои пайки. Режим хорошо кормит своих холуев!"


    scene bg crsh2 with dissolve

    show sp_al_057 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al "Ну ты, недовождь. Полегче на поворотах. А то я тебе за такие слова твою лобастую голову быстро подрихтую."

    al "У меня рука тяжелая. Спроси у долговязого. Кстати, вот уж кто холуй, так холуй. Он украл для тебя колбасу с кухни?"


    scene bg crsh3 with dissolve

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1

    smu "Не шей мне кражу, рыжая."


    scene bg crsh2 with dissolve

    show sp_al_056 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al "Так вот, милиция уже интересовалась пропажей продуктов с кухни. Оттуда за последние три дня исчезли не только сахар но и другие вещи."

    al "Твои «соратники» между прочим, кормят тебя, воруя со склада. А это уже уголовка."

    al "Ольга Дмитриевна пока прикрывает ваш отряд и тебя лично. Следователю ничего не сказала. Но если ты не вернешься и не побеседуешь с директором, то на вас повесят, в том числе и сахар."

    al "А тебе, как вдохновителю и организатору, вообще светит колония. Будешь излагать основы марксизма-ленинизма тамошним уркам, домушникам и щипачам."

    al "Кстати, за саботаж спектакля, листовки и попытку сколотить секту из пионеров, отдельная статья. Тут политика. И уже даже Маргарита Павловна при всех её связях, не сможет тебе помочь."


    scene bg crsh3 with dissolve

    show sp_smu_008:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1

    smu "(Бледнея) \nЧто, всё так серьезно?"


    scene bg crsh2 with dissolve

    show sp_al_056 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al "Серьезнее некуда. Кстати, когда слух о твоих художествах дойдет до твоего отца, то он пожалует сюда. Насколько я знаю от Ольги Дмитриевны, лично знакомой с ним, нрав у него крутой."


    scene bg crsh3 with dissolve

    "Окончательно сникший Смутьянов сел на песок и стал ковырять палочкой в костре. Он думал. Из кустов показались головы мальчиков второго отряда и тут же исчезли. Послышался звук убегающих ног."

    "Смутьянов злобно посмотрел в сторону удаляющегося топота."

    show sp_smu_011:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1
    with dissolve

    smu "Сволочи. Трусливое, безыдейное быдло. Вот так, старайся для них. Чуть что, сразу дают слабину. Я этого так не оставлю. Я им покажу."

    "Мы с Алисой переглянулись. Его перекошенное, злобное, вымазанное в золе лицо, было омерзительно. Он погрозил в пространство кулаком. Потом вдруг резко повернулся к нам, вскочил на ноги и сказал:"


    play miscSounds "audio/music/z_001.mp3"


    play music "audio/music/z_022.mp3"


    hide sp_smu_011


    show sp_smu_002:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1
    with dissolve

    smu "Ладно, банкуйте. Ваша взяла."


    scene bg crsh3 with dissolve

    "Подойдя к камышам, он вытащил из них небольшой рюкзак и волоча его за собой, двинулся за нами."

    show sp_smu_001:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1
    smu "СТОП!"


    scene bg crsh2 with dissolve

    scene bg crsh2 with dissolve

    show sp_al_056 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    "Мы вопросительно посмотрели на него."


    scene bg crsh3 with dissolve

    show sp_smu_008:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1

    smu "У вас, случайно, нет хлеба? \n(виновато пряча глаза)"

    smu "Они носят мне манную кашу в целлофановых пакетиках, идиоты. Я на неё уже смотреть не могу. Сегодня первый раз принесли колбасу. Нету хлеба? Жрать очень хочется."


    scene bg crsh2 with dissolve

    show sp_al_037 at flip:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    al "Даа... Для героя, поднявшего благородное знамя борьбы с эксплуатацией, у тебя довольно жалкий вид."

    al "Пойдем, накормят тебя в столовой, распоряжение уже такое от директрисы Любови Никаноровне поступило. И неплохо бы тебе помыться. А то ты чешешься весь. Как тебя тут раки ночью не съели!"


    scene bg crsh3 with dissolve

    show sp_smu_003:
        yalign 0.05 subpixel True
        xalign 0.46 subpixel True
        zoom 1.1

    smu "(Заметно повеселев) \nРаки что! Тут крысы водятся. Наверное, со столовой объедки выбрасывают, вот они и прикормились. И еще, кто-то воет по ночам на том берегу. Короче, место гиблое."


    scene bg crsh with dissolve

    "И мы все вместе отправились в лагерь. А Алиса улыбалась, подмигивала мне и на ходу насвистывала какую то веселую мелодию."


    stop music fadeout 1.0


    stop miscSounds fadeout 1.0


    play music "audio/music/z_516.mp3"


    scene cg od_alter with dissolve

    "После Случая с Вано мы как-то сблизились с Ольгой Дмитриевной. И я спросила ее, не знает ли она, откуда доносятся звуки и вибрация в лагере. Ольга Дмитриевна как будто задумалась."

    od "А почему это тебя так интересует? Ты первая, кто задает мне этот вопрос."


    scene bg odhouse7 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ольга Дмитриевна, согласитесь, странно, что никто кроме нас с Алисой не чувствует вибраций. И этот странный звук, который как бы из-под земли."


    scene cg od_alter with dissolve

    "Раньше мне казалось, что это только у меня такое ощущение. Оказывается, вы тоже его слышите?"


    stop music fadeout 1.0


    play music "audio/music/z_417.mp3"


    image an_29_02: # Анимация памятник качается
        
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat


    scene an_29_02 with dissolve


    pause (10000000000000000000000.0)


    scene bg odhouse7 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ну да, мы тоже. А вот памятник, он всегда стоит так, как стоял? Мне кажется он поворачивается время от времени."


    scene cg od_alter with dissolve

    od "Ну, то история простая. Его ремонтировали в прошлом году. Он стоит на таком шпиле, как флюгер и от вибрации возможно немного поворачивается."

    od "Да, это, наверное, шокирует. Но я за три года привыкла. Пионеры не замечают. Раньше он был закреплен и стоял неподвижно."

    od "Но потом при реставрации рабочие потеряли болты от крепежа, и он остался стоять на центральной вращающейся основе. Он тяжелый, поэтому стоит как Александрийский столп в Питере, сам по себе."


    stop music fadeout 1.0


    play music "audio/music/z_197.mp3"


    scene bg odhouse7 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Фух, отлегло. А мы с Алисой думали, что он как Каменный гость, оживает каждую ночь. А вот еще странность, Вы не слышали у себя над головой каких-нибудь шагов?"


    scene cg od_alter with dissolve

    od "На чердаке? Нет. Все чердаки законсервированы. Ключи у завхоза. Не вздумайте проверять. Маргарита Павловна этого не поймет и будет большой скандал. Надеюсь, вы туда не лазали?"


    scene bg odhouse7 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ну что вы, конечно, нет!"

    ul "Вот, еще хочу спросить. Вы никогда не видели тут большую кошку в окрестностях лагеря? Просто мы с Алисой не только видели её, но и общались. Она как человек. У неё есть имя, Юля."


    scene cg yulya_bushes with dissolve

    od "А, эту? Это не кошка. Точнее, это девочка, которая вообразила себя кошкой."

    od "Она тут давно живет. Некоторые думают что она из поселка. Возможно, сирота. Освоилась и живет. Где-то в районе озера. Петрович видел несколько раз, как она ловит рыбу. Очень ловкая. Прямо Маугли."

    od "Раньше её подкармливали в столовой. Оставляли ей еду, и она ночью забирала. Но потом вездесущие пионеры решили поймать ее. И вспугнули. Больше она не приходит."


    scene bg odhouse7 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А вам не кажется, что это ненормально, что девочка живет сама по себе и ни с кем не общается? Она умеет разговаривать и она не глупая."


    scene cg od_alter with dissolve

    od "Я сама была бы только за то, чтобы она жила в лагере и общалась с детьми. Но она пуглива. А Маргарита Павловна считает её дикаркой и говорит, что она мутант."

    od "В принципе, она тоже наверное была бы не против, но она боится эпидемии. Мало ли чем болеет эта девочка? Сначала нужен карантин."


    scene cg vio_skeleton with dissolve

    od "Если бы Виолетта Церновна, которая не раз мне намекала сделать ей прививки от бешенства и разных болезней, провела карантин, то возможно эта, как её, Юля? Стала бы членом общества."


    pause (10000000000000000000000.0)


    scene cg vio_iul with dissolve

    od "Но вот мне кажется, что как раз Виолетту Церновну она боится больше всего."


    pause (10000000000000000000000.0)


    scene cg iul_uniform with dissolve

    ul "Вот здорово! А потом бы мы приняли её в пионеры!"


    pause (10000000000000000000000.0)


    scene cg iul_reading with dissolve

    od "Прежде её нужно отмыть, привить, и образовать."

    od "Неплохо бы ей, прежде чем стать в ряды пионеров, что-нибудь почитать. Она, наверное, имеет образование не выше ученика третьего класса. Вопрос, умеет ли она вообще читать?"


    pause (10000000000000000000000.0)


    scene bg odhouse7 with dissolve

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Вот и проверим. Значит, вы не против?"


    scene cg od_alter with dissolve

    od "А отряд знает про Юлю?"


    scene bg odhouse7 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Мы с Алисой их познакомим. Уверена, она всем понравится."


    stop music fadeout 1.0


    play music "audio/music/z_492.mp3"


    scene an_d28_01 with dissolve

    ul "И да, скажу вам по секрету. Это, возможно, не Вано воровал белье с веревок. Ну надо же ей во что-то одеваться!"


    scene cg od_alter with dissolve

    od "Я так и думала. Хотя он тоже воровал. У него в бытовке нашли кучу нижнего детского белья. Целая коробка. Сейчас ищем хозяев. Хотя... Там с у него коллекция с трех заездов. Маловероятно, что найдем."


    scene bg odhouse7 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "У меня пропал красный купальник, майка и двое розовых трусов."

    hide sp_ul_013


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "И у меня трусы белые с синей каёмкой."


    scene cg od_alter with dissolve

    od "Да, вроде такие были. Посмотрите потом. Ладно, приводите вашу Юлю, мы сделаем собрание отряда. Но должна сказать, её вид может шокировать детей."

    od "Ей придется или снять хвост и ушки или, если уж она вбила себе в голову, что она кошка, прятать их под юбку и панамку. Хорошо?"


    scene bg odhouse7 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "ДА! Мы с ней решим этот вопрос."


    stop music fadeout 1.0


    play music "audio/music/z_022.mp3"


    scene al_ul_iul_story with dissolve

    "В тот же день мы с Алисой рассказали отряду о Юле. Были всякие споры."

    "Никто сначала не верил, потом все стали очень хотеть её увидеть и интересовались, пьет ли она молоко как кошка, спит ли она в коробке, и всякие глупые вопросы такого рода. Ну, вы понимаете."

    "И наконец, все уже ждали её появления в лагере. Осталось только уговорить саму Юлю."


    pause (10000000000000000000000.0)


    scene bg auhouse2 with dissolve

    "А я сказала Алисе:"


    scene bg auhouse_crop1 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Слушай, Ольга Дмитриевна думает, что у неё хвост не настоящий!"


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну и пусть думает. Какая разница? Лишь бы она не купалась голышом. А это я беру на себя."


    stop music fadeout 1.0


    play music "audio/music/z_516.mp3"


    scene cg yulya_hide with dissolve

    "Мы направились в старый лагерь, чтобы разыскать Юлю."

    "Но искать её не пришлось. Возле переправы мы заметили знакомую фигурку. Казалось, она ждет нас."

    "Юля явно была рада встрече. Она помахала нам рукой и быстро пошла в лес, маня нас за собой. Мы догнали ее и пошли вместе по тропинке. Мы рассказывали ей все новости лагеря, а она нам лесные новости."

    "Я задала ей те же вопросы, что и Ольге Дмитриевне. Про памятник она ничего не знала, а про вибрацию сказала, что в эти дни обычно снятся вещие сны."

    "Только нужно съесть какие-то ягоды. Она назвала их Ягоды Забвения. И ты получишь ответы на свои вопросы."


    scene bg opine2 with dissolve

    "Эти ягоды растут неподалеку от сосны Совы. Это небольшая горка в лесу, на вершине которой растет одинокая сосна, и на ней есть дупло совы. Сова очень старая."

    "Задавать сове вопросы, как говорил Пионер, можно, но она всё равно не ответит. Ты не знаешь птичьего языка. А она не говорить по человечески."

 
    scene bg iul_hide1 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "При чем же тут ягоды?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
 
    uv "Узнаешь."


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.4 xanchor 0.5 yanchor 0.0 zoom 1.4


    "Когда мы пришли к избушке, Юля накормила нас вкусной кашей «из одуванчиков», как её назвала Алиса."


    scene bg yulya_fireplace2 with dissolve

    "На самом деле, одуванчиков там не было, зато было какое-то зерно и травы. На вид, каша как каша. Чем-то напомнила овсянку."


    scene bg yulya_room with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Там есть сахарные грибы?"


    scene bg yulya_room2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Нет. Их жуют отдельно и ни с чем не смешивают."


    stop music fadeout 1.0


    play music "audio/music/z_495.mp3"


    scene bg jusu with dissolve

    "А потом Юля повела нас показывать свои ПРИПАСЫ, которые мы уже видели раньше, но были и другие."


    scene bg jusu2 with dissolve

    "Для этого в специальном дупле был оборудован склад. Это было огромное дерево, и мы бы никогда не заметили, что в нем есть дупло и лазейка туда, если бы Юля не показала нам её."

    "Она приоткрыла плетеную заслонку из веток и листьев папоротника, и мы увидели..."


    scene bg iul_hide1 with dissolve

    show sp_al_058:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Боже! Так вот где оказались недостающие три мешка сахара!"


    scene bg jusu2 with dissolve

    "Сахар был не в мешках, он был насыпан в деревянные березовые бочки из-под извести, аккуратно вымытые внутри."


    scene bg iul_hide1 with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Юля, откуда эти бочки?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Строители оставили, когда ремонтировали лагерь."


    scene bg iul_hide1 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ну ты запасливая! Неужели сама все принесла?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Нет. У меня есть помощник. Только не спрашивайте кто, я всё равно не скажу."


    scene bg iul_hide1 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Разве твои припасы не могут отсыреть? Или их не могут стащить и съесть другие животные?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "У всех есть свои охотничьи угодья. Никто не ворует друг у друга. А дожди тут чрезвычайно редки, как если бы на небе был прозрачный зонтик. Охотничьи угодья есть даже у ежа и черепахи."


    stop music fadeout 1.0


    play music "audio/music/z_214.mp3"


    image an_29_03: # Анимация гроза над Бурлейкой
        
        "images/an/an29day/an_d29_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an29day/an_d29_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
      

        repeat


    scene an_29_03 with dissolve

    pause (10000000000000000000000.0)


    scene an_d29_44 with dissolve


    "А если идет вдруг дождь, все о нем знают заранее, потому что сначала сильные молнии и гром. Три часа сверкает и грохочет. Все прячут припасы. Потом настоящий потоп. Но он проходит в долине."

    "Здесь — туман и маленький дождик, который быстро заканчивается. Но в долине у реки может продолжаться три дня. Однажды дождь шел неделю."


    stop music fadeout 1.0


    play music "audio/music/z_492.mp3"


    scene bg iul_hide1 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я задумалась. И действительно, я не припомнила ни одного серьезного дождя за всё время, пока мы были в лагере. Кроме того случая на болотах."

    ul "Но что-то же питает реку и ручьи? Всё тут как-то странно. Как будто, какой-то волшебник выращивает живность в большом аквариуме, создавая там микроклимат и время от времени подсыпая корм."


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Так и есть. Дождь, это когда моют «аквариум». Только в него потом подсаживают новую «живность», или наоборот."


    scene bg iul_hide1 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А ты?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Мы старожилы, мы постоянная величина. А еще ваша Виола, Ольга и Пионер. Возможно и вы станете, надо только дождаться дождя."
   

    scene bg iul_hide1 with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А что с теми, кого смывает дождь?"


    scene bg iul_hide2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    "Юля пожала плечами и замолчала. Потом встрепенулась и спросила:"

    uv "А хотите, я покажу вам охотничьи угодья Ежа и Черепахи?"


    scene cg iul_boat_river with dissolve

    "Мы согласились и Юля повела нас в сторону реки. Оказывается, у неё была своя лодка."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Лодку тоже украла?"

    hide sp_al_055


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Юля молча кивнула."


    stop music fadeout 1.0


    play music "audio/music/z_067.mp3"


    scene bg dark_forest with dissolve

    "Когда мы перебрались на другую сторону реки, то оказались в районе, который был значительно ниже по реке, чем даже Дальний пляж. Оттуда по тропе мы пошли в сторону горы."


    scene cg peak_dv_03 with dissolve

    "Затем лес расступился и перед нами открылся вид на скалу."


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Это же... Пик имени твоего имени! Пик Двачевской!"

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "О, да. Ну и устала же я тогда на него взбираться. Наверное, наш вымпел до сих пор там."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А что ему сделается. Ты, наверное, первая, кто туда смог забраться."

    hide sp_ul_021


    scene bg hetu with dissolve

    "Затем мы прошли через лес, растущий у подножья скалы."

    "Вскоре деревья расступились и мы вышли на небольшую, освещенную солнцем прогалину, через которую протекал ручей, образуя небольшой пруд."

    uv "Тише. Мы уже пришли. Видите маленький ручеек, поросший травой, а на кочке Черепаху? Она очень старая и всегда живет тут. Скоро появится и Еж."

    "И действительно, вскоре мы увидели Ежа. Было ощущение, что они нас не боятся."

    uv "Это потому что вы со мной."


    pause (1000000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_022.mp3"


    scene bg hetu2 with dissolve

    "Мы ещё полюбовались на уморительно забавного Ежа, как он смотрит на нас своими бусинками глазками и все время принюхивается, а потом стали спускаться вниз по склону."


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    uv "А ещё тут есть старые штольни. Там много змей, и поэтому туда не стоит ходить. Когда-то тут были туристы, они спустились в одну из штолен, и больше их никто не видел."

    uv "Это было как раз перед очередным дождем. Вода потопа уходит в штольни и поэтому вокруг всегда сухо."

    hide sp_iul_009


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Наверное, они об этом не знали. Получается, что эти штольни выполняют роль сифона в аквариуме. Если они перестанут работать, мы все тут утонем."

    hide sp_al_056


    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно! Это аквариум!"


    scene cg ul_fishes with dissolve

    "И тут я представила, как все мы превращаемся в рыбок. Алиса — оранжевая рыбка, я — маленькая красная, Женька — синяя, Ленка — фиолетовая, Мику — зеленая, Саманта — неоновая, Атсуи — тритончик."

    "Ольга Дмитриевна — блестящая как ставридка, Славя — рыба Луна, а директриса — Барракуда. Петрович, понятное дело, рак отшельник. Я бы и дальше фантазировала, но... Тут меня толкнула Алиса:"

    scene bg hetu2 with dissolve


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ты что спишь? Идем."

    hide sp_al_055

    "Оказывается, я так размечталась, что сошла с тропы и остановилась."


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Догоняя  Алису и Юлю) \nКогда-то я читала книжку, роман «Затерянный мир». Похоже, мы сейчас в таком затерянном мире."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ага, я тоже читала, классная книжка. Похоже, как там. Только, правда, динозавров не хватает. Но медведи — тоже ничего."


    scene cg dino with dissolve

    "И мы стали фантазировать про то, что было бы, будь тут динозавры. А Юля только улыбалась, слушая нас, пока не вывела нас к реке."


    stop music fadeout 1.0


    play music "audio/music/z_480.mp3"


    scene bg burleyka2 with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    uv "Если пойдете вдоль берега, выйдете на дальний пляж и оттуда на лодочную станцию."

    hide sp_iul_009


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al_ul "Постой! Мы же тебе главного не сказали! Хочешь в наш отряд? Будешь как мы, пионеркой!"


    scene cg iul_uniform with dissolve

    "И мы наперебой стали рассказывать, как будет классно, и что мы уже уговорили Ольгу Дмитриевну, и что никто не против, и все ждут только её согласия."


    scene bg burleyka2 with dissolve

    show sp_iul_010:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    uv "(Помрачнев) \nЯ давно хочу, но Пионеру это может не понравиться."

    hide sp_iul_010


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Пионеру?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Они друзья. Хорошо, Пионера я беру на себя."






















    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day28

return 