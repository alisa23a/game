label day11:

    $ days = 11

    stop music

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    play music "audio/audio10day/z_102.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Я обещала написать про странные дела в лагере. Начну по порядку."

    "Петрович. Что-то странное творится с Петровичем. И не только с ним. В этом лагере все не похожи на себя вчерашних."

    "Ну ладно, нас хорошо кормят мы прибавили в весе, но мои грудки явно выросли не за счет котлеток тети Любы. Были просто два пупырышка."

    "А сейчас я вынуждена была одеть на пляж ушитый Алисин купальник, который она мне подарила «на вырост»."

    "У Слави тоже такое… Она жаловалась, что на медосмотре медичка назвала её «ранней» и «аномально зрелой» из-за большой груди. Славя клялась, что до приезда в лагерь у неё была вполне себе детская грудь. (Здесь я не верю)"

    "Детская это у нас с Мику, вот."



   





    image an_11_01: # Анимация с Ульяной, лежащей в комнате и пишущей дневник
        
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

    play music "audio/audio9day/z_025.mp3"

    scene an_d11_01_bg with dissolve

    show an_11_01







    pause (10000000000000000000000.0)


return




























