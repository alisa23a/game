label day12:

    $ days = 12

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music

    play music "audio/music/z_176.mp3"

    scene bg evening_camp with dissolve

    "После вечерней проверки и отбоя мы с Алисой, тихонько взяв всё приготовленное для рыбалки (фонарики, кое-какую еду и куртки, чтобы не замерзнуть ночью), отправились к Петровичу, который уже ждал нас у лодочной станции."


    scene bg boat_fishing_1 with dissolve

    "Он пожурил нас, что мы долго копались."

    pe "Ну теперь ждите пока я скурю еще одну, и понаблюдаю, нет и за вами «хвоста»."

    al "Обижаете, мы очень тихо смылись. А что это лодку снизу так поддевает? И какие то всплески... Вода прямо как будто светится."

    pe "Это рыба играет. А свет от чешуи. Отражает чешуя свет. Эх вы рыбаки-знатоки."

    ul "Мы  в курсе. Читаем научную литературу. Просто спросили, что бы Вас проверить."


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

    pe "Да уж.. специалисты. Проверяют они меня. Зеленые вы еще меня проверять. С такими знаниями, вы не то что сома, а плотвы не поймаете."

    "Было так тихо, что даже звуки падающих с весел капель воды казались нам громкими."


    stop music

    play music "audio/music/z_150.mp3"

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

    show an_12_02

    "Петрович докурил и налег на весла. Берег быстро удалялся. Течение подхватило лодку."

    al "Весла шлепают... А мы не вспугнем сома?"

    pe "Не бойся, девонька, нам еще плыть и плыть. Видите, какое течение? Надо брать ближе к броду, тогда аккурат снесет к омуту."

    pe "Да вы не ерзайте тут! А то, понимаешь, раскачали лодку. Ты, рыженькая, на руле, правее бери, правее! Вот, так держать!"


    stop music

    play music "audio/music/z_178.mp3"


    "Я заметила, что левый берег, вдоль которого мы плыли, стал двигаться быстрее, о чем я и сказала Петровичу."

    pe "(Грозно) \nСам вижу! Похоже нас на водоворот несет. Эх, старый дурак, не угадал, в каком месте надо на стремнину выходить! И не мудрено, темень-то какая!"


    scene bg dwhir

    
    ul "Водоворот, это который Смертельный?"

    pe "Он самый! Только он смертельный осенью, когда вода с дождями прибывает."

    al "Не бойся, Улька, у нас опытный капитан! С Петровичем нам никакие водовороты не страшны!"

    ul "Что-то мне как-то не по себе. А у нас даже спасательных жилетов нет."

    "Лодка со стуком причалила к небольшой пристани."

    pe "Не зевай, Ульянка, хватай цепочку, приматывай лодку, а то унесет нас! Видишь, кол торчит, за него приматывай. А я придержу веслами. Да живее, живее!"

    al "(Помогая закрепить лодку) \nДавай, я."

    ul "Я сама!"





    pause (10000000000000000000000.0)


    scene black with fade

    stop music

    #jump day13

return