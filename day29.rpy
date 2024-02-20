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






    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day28

return 