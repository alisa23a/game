label day2:

    $ style.say_window = style.window

    $ days = 2

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


    image an_10_01: # Анимация с Ульяной, лежащей в комнате и пишущей дневник
        
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_03.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_04.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_02.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_05.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_07.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_06.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_01.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_09.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an10day/an_d10_08.png" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat


    scene an_d10_01_bg with dissolve

    show an_10_01

    "Вчера устала и не написала про домик. Нас поселили в домиках."


    scene bg auhouse_crop2
  
    show sp_al_045:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Со мной живет Алиса, и мы с ней уже почти друзья. У неё тоже рыжие волосы. При ней никто не осмеливается меня дразнить - «рыжий-рыжий конопатый, убил дедушку лопатой»."

    "Классно, что у меня такая подружка. Она старше меня. Но это ничего, ей можно доверять. Она сильная. Почти такая же, как я. Обещала научить меня играть на гитаре и нырять. Я ныряю, но пока плохо."


    scene an_d10_01_bg with dissolve

    "Мальчики в лагере тоже есть. Но пока никто из них мне не понравился, чтобы дружить."

    "У них какие-то детские интересы. Скучные. Другое дело Алиса. Еще она научила меня делать карточный фокус. Надо потренироваться и показать его, когда будет концерт в лагере."

    "Правда, папа просил меня не «проявлять инициативы», как он это называет. Он сказал даже хуже, что я «в каждой бочке затычка». Но его нет и некому мне запретить. А тут много интересного."

    "Есть кружки и футбол, и еще сегодня мы пойдем на реку купаться. Но об этом я напишу завтра."


    scene cg dining_crowded with dissolve

    "Кормят тут хорошо, но не как у бабушки."

    scene cg dining_crowded with dissolve

    pause (1000000000000000000000.0)




    stop music fadeout 0.5

    queue music "audio/music/z_197.mp3"

    scene cg dining_crowded2 with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2


    "Сегодня в столовой я подложила многоножку в тарелку одному мальчику. Он смешной. У него какое-то глупое лицо. Хотя, в целом он милый."

    "Кажется, он приехал сегодня утром, позже меня. Хотела показать ему лагерь, но передумала. Папа сказал «будь с парнями осторожней. Кто знает, что у них на уме?»."

    "А этот мальчик, Семён, так его зовут, вообще странный. Смотрит на девочек, как сказала Алиса, «как кот на сливки». Ей показалось, что он смотрел на неё именно так и она отшила его, сказав «глаза сломаешь»."


    scene an_d10_01_bg with dissolve

    "Вообще я буду записывать её выражения, они всегда попадают в точку. Если я захочу дружить с Семёном, то посоветуюсь с ней. Она очень взрослая, не то что я. Ну, я тоже, но она взрослее."


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"

    "Вот перечитала и мне кажется, что я пишу скучно. Но пока в лагере мало что произошло. Я еще наверстаю."


    scene bg auhouse_crop2
  
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Я подумала и дала почитать Алисе (мы с ней, как она сказала, теперь «не разлей вода»). Она не стала смеяться, как те мальчики, а похвалила."

    "Но сказала, что я неправильно пишу, сухо и неинтересно, потому что похоже на «протокол заседания». Алиса попыталась объяснить мне: «Ты должна описывать свои чувства «через призму событий»."

    "Это сложно для меня, но кажется я поняла, что она имеете в виду. «Если ты хочешь стать журналисткой или писателем, ты должна писать интересно». Черт, ну какая же она умная!"

    "Ведь я ей даже не говорила, что хочу стать писателем. Как она догадалась? А еще она сказала, что я не должна показывать свой дневник никому вообще, даже ей. «Это личное»."

    "И что она точно бы никому не показала свой дневник. Мне кажется, у неё была какая-то страшная история в жизни, она переживает всё, что происходит вокруг, очень остро."


    scene an_d10_01_bg with dissolve

    "Папа называет таких  «ранимые» Интересно, я ранимая? Все, нас зовут на речку. Потом допишу."


    scene an_d10_01_bg with dissolve

    pause (1000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day3


return
    