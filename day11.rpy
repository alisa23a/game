label day11:

    $ days = 11

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

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
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5


    "Так вот, про Петровича. Ещё когда он повел нас смотреть лебедку на пристани, я обратила внимание, что он как будто помолодел. Но на лавочке он был старенький, когда рассказывал про войну!"

    "Тут даже Алиса, которая вечно смеется над моими фантазиями, вынуждена была согласиться. И не только мы с Алисой заметили."

    "Я даже сказала: \n«Архип Петрович, а вы как будто помолодели»."


    scene cg boozy


    "А он засмущался и ответил: \n«Да, доченька, я же пью свой эликсир на травах. Секретный. Я бы вам рассказал про состав, но вам молодеть нельзя. Вы и так молодые»."

    "Все ещё засмеялись тогда. Вот первая странность."

    # stop music

    # play music "audio/music/z_148.mp3"

    scene an_d11_03_bg
    
    image an_11_03: # Анимация трансформация ОД
        
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

        repeat

    show an_11_03

    pause (10000000000000000000000.0)

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















    # image an_11_01: # Анимация с Ульяной и Алисой на ночной рыбалке
        
        # "images/an/an11day/an_d11_01.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_02.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_03.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_04.png" with Dissolve(0.5, alpha=True)
        # pause 1.0
        # "images/an/an11day/an_d11_05.png" with Dissolve(0.5, alpha=True)
        # pause 1.0
        # "images/an/an11day/an_d11_06.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_01.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_03.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_04.png" with Dissolve(0.5, alpha=True)
        # pause 1.0
        # "images/an/an11day/an_d11_07.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_08.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_09.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
        # "images/an/an11day/an_d11_10.png" with Dissolve(0.5, alpha=True)
        # pause 0.5
  
        # repeat

    # stop music

    # play music "audio/music/z_025.mp3"

    # scene an_d11_01_bg with dissolve

    # show an_11_01







    pause (10000000000000000000000.0)


return




























