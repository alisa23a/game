label day11:

    $ days = 11

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music

    play music "audio/music/z_147.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Я обещала написать про странные дела в лагере. Начну по порядку."

    "Петрович. Что-то странное творится с Петровичем. И не только с ним. В этом лагере все не похожи на себя вчерашних."



    image an_11_02: # Анимация с Ульяной и Алисой сравнивает грудь
        
        "images/an/an11day/an_d11_11.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_12.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_11.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_13.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_11.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_13.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_14.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_13.png" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat



    scene an_d11_02_bg with dissolve

    show an_11_02

    pause (10000000000000000000000.0)

    "Ну ладно, нас хорошо кормят мы прибавили в весе, но мои грудки явно выросли не за счет котлеток тети Любы. Были просто два пупырышка."

    "А сейчас я вынуждена была одеть на пляж ушитый Алисин купальник, который она мне подарила «на вырост»."

    "У Слави тоже такое… Она жаловалась, что на медосмотре медичка назвала её «ранней» и «аномально зрелой» из-за большой груди. Славя клялась, что до приезда в лагерь у неё была вполне себе детская грудь. (Здесь я не верю)"

    "Детская это у нас с Мику, вот."


    scene bg winch

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Так вот, про Петровича. Ещё когда он повел нас смотреть лебедку на пристани, я обратила внимание, что он как будто помолодел. Но на лавочке он был старенький, когда рассказывал про войну!"

    "Тут даже Алиса, которая вечно смеется над моими фантазиями, вынуждена была согласиться. И не только мы с Алисой заметили."

    "Я даже сказала: \n«Архип Петрович, а вы как будто помолодели»."


    scene cg boozy


    "А он засмущался и ответил: \n«Да, доченька, я же пью свой эликсир на травах. Секретный. Я бы вам рассказал про состав, но вам молодеть нельзя. Вы и так молодые»."

    "Все ещё засмеялись тогда. Вот первая странность."

    stop music

    play music "audio/music/z_148.mp3"

    scene an_d11_03_bg
    
    image an_11_03: # Анимация трансформация ОД 1
        
        "images/an/an11day/an_d11_15.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_16.png" with Dissolve(0.5, alpha=True)
        pause 0.5
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

        #repeat


    image an_11_03_2: # Анимация трансформация ОД 2
        
        # "images/an/an11day/an_d11_15.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_16.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
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

        repeat


    show an_11_03

    pause (4.5)
    
    show an_11_03_2

    "А Ольга Дмитриевна с первого дня тоже, как будто помолодела. Ну, то есть, она была молодая, но теперь стала, как старшеклассница."

    "Воздух тут такой целебный. Ольга Дмитриевна рассказывала, что территория лагеря соседствует с заповедником, где растут всякие целебные травы."

    "Надо все проверить насчет трав. Поспрашивать у Петровича. Буду наблюдать странности дальше."

    scene an_d10_01_bg with dissolve

    show an_10_01

    "И ещё странность, это землетрясение."

    "Ну, не то, чтобы настоящее. Но иногда земля как будто вибрирует. Петрович сказал, «привыкайте» и что тут сейсмическая зона."

    "Но я думаю, что это компрессор работает в столовой. Он ночью иногда тарахтит."

    "Если стать рядом, то прямо пол «ходуном ходит». Может, это передается на расстояния? Под лагерем же шахты были и всякие пустоты. Вот лагерь и «резонирует». Это я тоже еще никому не рассказывала."

    stop music

    play music "audio/music/z_102.mp3"

    "Только знаешь ты, мой читатель. Наверное, когда кто-то первый раз прочтет, я буду уже старушка. Это же секретный дневник. Но все старые люди публикуют мемуары. Может и я опубликую."

    "Когда секреты перестанут быть секретами."


    stop music

    play music "audio/music/z_175.mp3"

    scene bg pool_big_catfish_night

    "После рассказа Семена у костра про то, что в Омуте, живет Большой сом, мы с Алисой серьезно задумались."

    "История прямо скажем, криминальная. Особенно,  если учесть, что с этим связано большинство местных историй о пропавших в омуте  людях. Вот есть Омут, который так и называется, омут Большой Сом."

    "Если даже в народных преданиях есть такое место, то не может быть, чтобы такого сома не существовало в жизни."

    scene cg catfish

    "Я вот так его себе представляю, огромный, зубастый с загребущими ластами. Хватает этими лапищами-ластами и утаскивает всяких беспечных купальщиков.  А потом ам ням ням... И поминай, как звали."

    "В общем ОН местная легенда И как будто, этой легенде, уже сто лет."

    "И что с этим Сомом связаны всякие страшилки. Например, что он утащил девочку (ту самую) и поселковую собаку, чуть не утопил рыбака. И что он утаскивает уток и всякую живность, которая рискует плавать возле омута."

    "Надо было внести ясность. Нас удивляло, что никто не пытался поймать сома. Ужас, который он наводил на поселковых жителей, наверное, был слишком велик."


    scene bg pool_big_catfish_morning

    "Мы с Алисой рассуждали так."

    "Во-первых, не может один сом жить так долго. Возможно, это просто потомки Большого Сома. И они точно, не большие. Прямо скажем – сомята по сравнению с легендой."

    "Но мы пионерки и должны нести свет знаний в «неокрепшие умы» аборигенов."


    stop music

    #play music "audio/music/z_177.mp3"

    play music "audio/music/z_023.mp3"

    scene bg watchmans_cabin with dissolve

    "В общем, было решено запастись всякими снастями для поимки Сома. А снасти были только у Петровича. И мы пошли к нему."

#    scene bg watchmans_cabin_ul_al

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 0.6
    with Dissolve(0.3)
    
    show sp_ul_012:
        yalign 0.4 subpixel True
        xalign 0.7 subpixel True
        zoom 0.5
    with Dissolve(0.3)


    "Мы всё так честно ему рассказали, что хотим поймать этого сома. А когда изловим, то отнесем его на кухню и пусть в лагере будет рыбный день. День Большого Сома. Если, конечно, это все не сказки бабушки Арины."

    scene bg watchmans_cabin_2 with dissolve
    
    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2

    "Петрович нас внимательно выслушал и сел думать."

    "Три самокрутки выкурил. Наконец, он сказал:"

    hide sp_pe_003

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2
    with Dissolve(0.3)

    pe "Великое дело вы задумали. Но никто его ещё не словил. Потому как он очень хитрый. Я тут уж почитай всю жизнь живу, а такого не слыхивал."

    pe "Сам ловил в Омуте. Давно на него зуб точу. Два раза он мне показался. Даже лодку попортил. Весло перекусил и сожрал весь улов. Сети рвет. Леску на него надо особую. Правду говорю. Я с тех пор там не рыбачу."

    hide sp_pe_002

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2
    with Dissolve(0.3)

    pe "Но, наверное, мне удачи нет. Старый стал. А вам, молодежи, может и будет счастье. Только дело это непростое. Ночью его надо брать. Днем он вовсе не показывается."

    pe "Оттого многие тут в лагере думают, что все это выдумки старого деда. Мол, «закусывать надо». Я не обижаюсь. Люди так устроены. Потому что если гром не грянет, мужик не перекрестится."

    hide sp_pe_003

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2
    with Dissolve(0.3)

    pe "Дам я вам снасть, что припасал на Сома. Там крючок кованый и трос от него стальной. Простую леску он перекусит, что твою нитку. А тащить его, тут надо силу особую. Без меня вам с ним не справиться."

    pe "Я буду на берегу наблюдать. Сачок у меня есть особый на крупную рыбу. Но боюсь, тут понадобится багор."

    pe "А то, что ему сто лет – это правда."


    stop music

    play music "audio/music/z_154.mp3"

    #scene bg watchmans_cabin_ul_al

    scene bg watchmans_cabin with dissolve

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 0.6
    
    show sp_ul_012:
        yalign 0.4 subpixel True
        xalign 0.7 subpixel True
        zoom 0.5

    "Мы не стали откладывать поимку чудовища, а решили сразу же вечером пойти на реку. Петрович дал нам снасти и, посмеиваясь, сказал:"

    scene bg watchmans_cabin_2 with dissolve
    
    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2

    pe "Конечно, вы его сегодня не поймаете, но тренировка - большое дело. Наловите на хорошую уху, глядишь, и с сомом справитесь. Ничего не наловите, значит, проверите мои раколовки. Всё какой-никакой улов."

    #scene bg watchmans_cabin_ul_al

    scene bg watchmans_cabin with dissolve

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 0.6

    
    show sp_ul_012:
        yalign 0.4 subpixel True
        xalign 0.7 subpixel True
        zoom 0.5


    "Но мы с Алисой прямо серьезно настроились на сома. Говорят же, что новичкам везет."

    scene bg watchmans_cabin with dissolve

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Мы с Пионером аж шесть рыб поймали в прошлый раз. Так что я опытная. А ты?"

    hide sp_ul_012

    show sp_al_013:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    al "Меня как-то наши мальчишки у нас в городе звали рыбачить ночью. Там тоже есть река. Но я знала, зачем они меня зовут. Поэтому не пошла."

    hide sp_al_013

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    al "Так что, у меня с тобой будет первая рыбалка."

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Если честно, то у меня тоже только вторая рыбалка. Да и то,  первую рыбу мне помог поймать пионер. Я больше для форсу сказала. Не хотела казаться совсем неумехой."

    ul "Ну и чтобы ты не подумала, что у нас ничего не получится. Очень хочется поймать сома."

    hide sp_ul_013

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    al "Да ладно. Не поймаем, так не поймаем. Просто порыбачим. Классно же. Приключение. Спасибо тебе, Улька. Ты самый честный человек. \n(Ласково взъерошила Ульяне волосы)"

    hide sp_al_006

    "Мне стало как-то тепло от слов Алисы. Все-таки она лучшая подруга! "


    stop music

    play music "audio/music/z_170.mp3"

    scene bg crsh

    "И мы пошли на рачью отмель. Потому что идти к омуту было страшно.  Может, сом приплывет к нам. Он же на раков тоже, небось, охотится. А там их тьма-тьмущая."

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Алис, а сомы на раков охотятся? "

    hide sp_ul_012

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    al "(Разматывая удочки) \nНаверное. Может, обычные и нет, а наш огромный. Не удивлюсь, если он их за обе щеки уплетает. Всё живое хрумкает.  Ему же массу поддерживать надо."

    al "Не зря нам запретили ночью купаться. Ольга Дмитриевна точно в курсе про сома."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Да... Ладно, закину я подальше. Тут у берега мелко, а он любит, наверное, глубину."

    hide sp_ul_012

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.3

    al "Эй! Не заходи в воду! Я за тебя переживаю. Вдруг он рядом где-то?"

    hide sp_al_004

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    ul "Глупости. Он же когда плывет, волну большую поднимает, как буксир. Я смотрела как плывут буксиры. Так что я его за километр увижу."

    hide sp_ul_014


    image an_11_01: # Анимация с Ульяной и Алисой на ночной рыбалке
        
        "images/an/an11day/an_d11_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_04.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_05.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_04.png" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an11day/an_d11_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an11day/an_d11_10.png" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    stop music

    play music "audio/music/z_153.mp3"

    scene an_d11_01_bg with dissolve

    show an_11_01

    "И мы стали рыбачить. Не знаю, то ли Петрович нам самую лучшую наживку дал, то ли и вправду повезло, но в тот раз у нас прямо клевало. Алиса вытащила трех рыбок, а я аж пять! Правда, небольших. Но на уху, точно, хватило."

    "У моих рыбок, были оранжевые плавнички, а Алиса поймала серебристых. Не знаю как они называются, но красивые. Ещё щучка сорвалась. Она сильно билась и я её упустила. Жалко было до слез. Очень хотелось удивить Петровича."

    "Сом так и не пришел. Хотя, мы пошли на хитрость, сделали из одной рыбки наживку. Прямо пол рыбы насадили на крючок."

    "Попался только рак. Он вцепился в рыбу и ни в какую не хотел отпускать. Еле клешни разжали. Так он в авоську и попал с рыбой и потом в уху."


    stop music

    play music "audio/music/z_155.mp3"


    #scene bg watchmans_cabin_ul_al

    scene bg watchmans_cabin with dissolve

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 0.6
    
    show sp_ul_012:
        yalign 0.4 subpixel True
        xalign 0.7 subpixel True
        zoom 0.5

    "Петрович сильно удивился, когда мы ему показали улов. Он не спал. Он же сторож. И сразу засуетился с ухой."


    scene bg watchmans_cabin_2

    show sp_pe_001:
        yalign 0.0 subpixel True
        xalign 0.477 subpixel True
        zoom 1.2

    pe "Ишь ты, вижу потрудились. А я думал, что ужинать будем вхолостую. Картошки наварил, колбаска у меня и сыр припасены. А тут, прямо целый улов! И впрямь, удачливые. С вами можно рискнуть и на Большого Сома."

    hide sp_pe_001

    "Мы хотели показать, что бывалые рыбаки, но пока ждали уху, уснули. Под утро нас разбудил Петрович и сказал, что рыбка нас ждет."

    "Достал котелок, завернутый в тряпицу, чтобы не остыл. Уха получилась отличная. И мы так натрескались, что еле-еле встали из-за стола. А нам ещё на линейку утром."

    #scene bg watchmans_cabin_ul_al

    scene bg watchmans_cabin with dissolve

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.9 subpixel True
        zoom 0.6

    
    show sp_ul_012:
        yalign 0.4 subpixel True
        xalign 0.7 subpixel True
        zoom 0.5


    "В общем, так закончилась наша первая рыбалка. Назовем её ТРЕНИРОВКА. И теперь у нас появилась уверенность.  Мы же теперь, вроде как, рыбаки со стажем."

    scene cg catfish

    "Так что, берегись, сомище! Мы идем за тобой!"

    scene bg square 

    "Пока мы шли в наш домик, я изображала Большого Сома, который гонится за Алисой."

    show sp_al_037 with moveinleft:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.3

    pause (0.5)

    hide sp_al_037 with moveoutright

    show sp_ul_021 with moveinleft:
        yalign 0.05 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2

    pause (0.5)

    hide sp_ul_021 with moveoutright



    "Алиса притворно боялась и кричала -  «Пожалей меня большой Сом, я тебе еще пригожусь!» А я ей – «Конечно, пригодишься, спасешь меня от голода, моя вкусная»."

    show sp_al_037 with moveinleft:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.3

    pause (0.5)

    hide sp_al_037 with moveoutright

    show sp_ul_021 with moveinleft:
        yalign 0.05 subpixel True
        xalign 0.47 subpixel True
        zoom 1.2

    pause (0.5)

    hide sp_ul_021 with moveoutright

    "Но Алиса так быстро улепетывала, что я еле ее догнала. Не хотел быть завтраком Сома."

    scene cg pillow_fight with dissolve

    "Ну а в домике, мы устроили битву подушками, которую прервал звук горна, зовущего всех на утреннюю линейку."



    #pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day12

return




    # show sp_al_037 at flip:
        # yalign 0.0 subpixel True
        # xalign 0.9 subpixel True
        # zoom 0.6
    # with Dissolve(0.3)
    
    # show sp_ul_019:
        # yalign 0.4 subpixel True
        # xalign 0.7 subpixel True
        # zoom 0.5
    # with Dissolve(0.3)























