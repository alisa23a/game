label day4:

    $ style.say_window = style.window

    $ days = 4

    $ adv_1 = False
    $ adv_3 = True
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = False

    $ im_gal_03_00 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False


    pause (1000000000000000000.0)


    hide screen current_day


    $ show_quick_menu = True


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"


    scene an_d10_01_bg with dissolve

    show an_10_01

    "Сегодня я буду писать подробно. Очень много впечатлений. Нужно вспомнить всё. Мне кажется, это очень важно.  С того времени, как я приплыла в лагерь на лодке, случилось много чего. Но всё по порядку."

    "Алиса, оказывается, меня искала и очень волновалась."


    stop music fadeout 0.5

    queue music "audio/music/z_516.mp3"


    scene bg lakedeep4 with dissolve

    "Она бегала даже в лес и на речку, думая, что я могла утонуть, если меня затащило в водоворот. В лесу она кричала моё имя. У неё был фонарик."

    "Она светила, пока батарея не кончилась и хотела уже идти к Ольге Дмитриевне, рассказать, что я пропала, но потом увидела меня, идущую от реки."

    "Она поругала меня, но совсем немножечко. Хорошо, что она не пошла к Ольге Дмитриевне. Иначе скандала было бы не избежать. И тогда всё, конец. Значит, я везучая."


    scene bg starry_sky with dissolve

    "Котлеты были холодные, и мы решили их разогреть на костре. Компот Алиса перелила в бутылку из под кефира. Мальчишки развели костер, но мы к ним не пошли. Алиса сказала, что мы разожжём свой."


    #Анимация костёр в ночи

    image campfire_night:
        
        "images/an/an4day/an_d04_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat


    scene campfire_night with dissolve

    pause (1000000000000000000.0)


    "Костер мы развели на холме на опушке леса, с видом на реку. Пришлось уйти от лагеря, и мы были одни. Алиса сказала, что свет от лагеря мешает увидеть звезды."

    "Мы жгли веточки, которые я нашла наощупь в лесу, а Алиса ходила за мной, как будто тоже собирать, но я знала что теперь она просто боится, что я опять потеряюсь."

    "Я очень ей благодарна. Она хорошая. Вот тут размазались чернила... Это я плачу."


    #Анимация Ульяна у костра

    image al_ul_campfire:
        
        "images/an/an4day/an_d04_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

  
        repeat



    stop music fadeout 0.5

    queue music "audio/music/z_180.mp3"


    scene al_ul_campfire with dissolve

    pause (1000000000000000000.0)


    "Мы жарили котлетки, и они казались нам намного вкуснее, чем в столовой. Потом мы стали петь и смотрели на звезды."

    "Я не удержалась и рассказала Алисе про реку, тропинки и Семёна."

    "Она не поверила, но сказала, чтобы я никому не рассказывала, иначе  весь отряд будет смеяться. Ещё сказала, чтобы я поменьше ходила одна, и если очень уж невмоготу, то чтобы брала её с собой."


    #Анимация Ульяна у костра моргает

    image ul_campfire_blinking:
  
        "images/an/an4day/an_d04_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.5  
        "images/an/an4day/an_d04_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_39.webp" with Dissolve(0.5, alpha=True)
        pause 9.5
  
        repeat



    stop music fadeout 0.5

    queue music "audio/music/z_478.mp3"


    scene ul_campfire_blinking with dissolve

    "Потом она рассказала о своей жизни до того, как приехала в лагерь. Рассказала о своём отчиме, и о том, что между ними произошло. Я прям не дышала, так внимательно слушала её."

    "Но я не буду тут писать. Она взяла слово, что я никогда никому не буду рассказывать про неё. И я как пионер встала и торжественно отсалютовала."


    scene an_d04_39 with dissolve

    pause (1000000000000000000.0)



    #Анимация Алиса у костра моргает

    image al_campfire_blinking:
        
        "images/an/an4day/an_d04_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an4day/an_d04_37.webp" with Dissolve(0.5, alpha=True)
        pause 9.5
  
        repeat


    scene al_campfire_blinking with dissolve

    "Алиса так смеялась, что чуть не упала в костер. Она сказала, что на таких как я Земля держится."

    "Но это, думаю, она просто дразнила меня. Папа во всяком случае, так не считает. Он говорит, что клятвы  были хороши для рыцарей, а сейчас никто не клянется."

    "Алиса снова стала смеяться и сказала что я, наверное, «последний рыцарь»."

    scene an_d04_37 with dissolve

    pause (1000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_301.mp3"


    scene cg al_ul_campfire_dance with dissolve

    "А еще мы танцевали у костра, потому что в лагере включили музыку и нам было хорошо её слышно."

    "Я смотрела на Алису, как она танцует, сняв свой галстук, рубашку и юбку, сделав накидку на бедра из рубашки, под которой был купальник. Его она надела, чтобы вылавливать меня, утопшую, из реки."

    "Мы были одни, и нас никто не видел. В свете костра её тело было как у эфиопских женщин. Гладкое и стройное. Я знаю это точно потому, что отец показывал мне фотографии этих женщин из экспедиции в Эфиопию."

    "Только у неё тело было белое. Я прямо залюбовалась! Если бы только у меня было такое..."

    "Я спросила у неё, а знает ли она о волшебной красоте своего тела? Она сказала просто: «Да, я знаю»."

    "Потом она увидела, как я смотрю на ее грудь и сказала:"

    al "Маленькая, не грусти! Пройдет немного времени, и у тебя будут милые грудки."

    scene cg al_ul_campfire_dance with dissolve

    pause (1000000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_196.mp3"


    scene cg tickling with dissolve

    "Я хотела обидеться. Мальчишкам я бы такого точно не простила. Но вместо этого мы стали хохотать и кататься по траве. Она щекотала меня и приговаривала:"

    al "Растите, растите, Ульянины яблочки!"

    "От неё пахло чем-то вкусным. Я уткнулась в её волосы и шею лицом и только повизгивала от щекотки и удовольствия, вяло пытаясь отбиваться. Так хорошо мне было только с бабушкой. Она тоже здорово пахла."

    scene cg tickling with dissolve

    pause (1000000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    scene bg forest_night with dissolve

    "Но вдруг! Мы услышали, как за нашей спиной затрещали ветки."

    "Мы вскочили. Из-за костра, слепящего глаза, не было видно, кто стоит в тени кустов. Я сильно испугалась, мальчишки стращали нас медведями. Я не верила тогда, но вдруг это правда?"


    scene bg al_ul_campfire_empty with dissolve

    show sp_al_039:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Я спряталась за Алису. У неё в руке я увидела маленький перочинный нож, который мы взяли, для того, чтобы делать палочки для котлет. Вид у неё был решительный. Она крикнула в темноту:"

    "Эй, извращенец, если ты не трус, выйди на свет!"


    scene bg forest_night with dissolve

    show sp_sem_025:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Из кустов вышел... Семён."

    "Вид у него был сконфуженный. Наверное, он не ожидал, что его шпионаж раскроется. Мы не знали, как долго он наблюдал из своего укрытия."


    scene bg al_ul_campfire_empty with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Он подошёл и сел к костру. Потом взял палочку и стал с невозмутимыми видом шевелить ею угли."


    scene bg al_ul_campfire_empty with dissolve

    show sp_al_039:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Стало неуютно. Алиса спрятала нож и спросила:"

    al "Чего ты припёрся, Семён? Разве у костра в лагере мало девочек?"

    "Семён улыбнулся. Такую улыбку папа назвал бы фальшивой. Я сама так улыбаюсь, когда он смотрит мой дневник."


    scene bg al_ul_campfire_empty with dissolve

    show sp_sem_019:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    sem "Можно посидеть с вами?"

    "Алиса взяла меня за руку и подняла с земли вещи."


    scene bg al_ul_campfire_empty with dissolve

    show sp_al_039:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_ul_012:
        yalign -0.2 subpixel True
        xalign 1.0 subpixel True
        zoom 1.0


    al "Сиди сколько хочешь, трава ничейная. А мы пойдём. Правда, Уля?"

    "Я хотела сказать, что пусть сидит с нами, но Алиса сделала значительные глаза, и я кивнула. Мы пошли."


    stop music fadeout 0.5

    queue music "audio/music/z_480.mp3"


    scene cg sem_campfire with dissolve

    "Я ещё оглядывалась на силуэт, сидящий у костра, а Алиса ни разу не обернулась."

    pause (1000000000000000000000.0)

    scene cg sem_campfire with dissolve


    scene bg square with dissolve

    show sp_ul_012:
        yalign -0.2 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0


    "Когда мы шли в лагерь, я спросила её:"

    ul "Скажи, тебе нравится кто-нибудь из мальчиков в лагере?"


    scene bg square with dissolve

    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Она пожала плечами. Свет от лагерных фонарей уже хорошо освещал её лицо."


    scene bg square with dissolve

    show sp_ul_012:
        yalign -0.2 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0

    ul "А Семён?"


    scene bg square with dissolve

    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса остановилась и посмотрела на меня с серьезным видом."

    al "Скажи, как может нравится парень, который уже на второй день пытается повесть лапшу на уши сразу трём девочкам из отряда?"

    "Она прямо так и сказала: ЛАПШУ НА УШИ."

    al"А то, что он живёт, как ты сама мне рассказывала, в домике со взрослой женщиной? Ведь там даже нет перегородки, и кровати стоят рядом?"


    scene bg square with dissolve

    show sp_ul_013:
        yalign -0.2 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0

    "Алиса уставилась на меня. Я молчала. Я не знала, что сказать. Я в этом разбиралась не очень. Как сказал папа, во мне «не проснулся инстинкт»."

    "Я сказала Алисе про инстинкт."


    stop music fadeout 0.5

    queue music "audio/music/z_153.mp3"


    scene bg square with dissolve

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И вдруг она из серьёзной сразу стала несерьёзной. Она снова так хохотала, что наверное даже Семён у костра услышал, хотя мы ушли уже довольно далеко."

    al "Ты моё рыжее чудо!"

    "Алиса смеялась, и слезы катились у нее из глаз."

    scene bg square with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Потом она вытерла их и сказала, обняв меня за плечи:"

    al "Дай бог, чтобы он проснулся как можно позже."


    stop music fadeout 0.5

    queue music "audio/music/z_055.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Очень хочется написать про то, что было ночью."

    "Я писала, что испортила замок в кружке умелые руки, чтобы на ночь эти мальчишки не смогли закрыть дверь в свою мастерскую?"

    "Я сначала хотела рассказать Алисе, чтобы она пошла со мной и постояла на страже, пока я буду осматривать эту куклу-робота. Но потом я поняла, что она не одобрит меня."

    "Я и так принесла ей много хлопот, а тут ещё и это."

    "Я сильно крепилась, чтобы не пойти. Но не выдержала. Я лежала с закрытыми глазами и ждала, пока Алиса уснёт."

    "Потом тихонечко встала и на цыпочках прошла к двери, взяв с собой всю одежду и фонарик Алисы."


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


    scene bg square with dissolve

    "Оделась я уже на улице. Лагерь спал. Даже мальчишки, которые сидели у костра, уже ушли."

    "Лагерь ночью не похож на себя. Всё стало сразу каким-то таинственным. Или это я просто волновалась. Когда я добралась до места, моё сердце колотилось, как ненормальное."


    scene bg mus_stairs with dissolve

    "Я постояла возле двери в мастерскую. Там было тихо. От моего толчка дверь не открылась. Должно быть, мальчишки вытащили из замочной скважины мою спичку."

    "Я огорчилась. Но потом увидела, что между дверью и косяком есть маленькая щелочка. Я посветила туда фонариком Алисы."

    "Батарейка села, но слабенького света было достаточно, чтобы увидеть, что с той стороны дверь держит какой-то крючок."

    "Я вспомнила, что моя бабушка всегда закрывала курятник изнутри. Она это делала, чтобы соседские мальчишки не воровали яички."

    "Она брала кочергу и, просунув в щель между дверью и косяком, приподнимала крючок, на который закрывалась дверь изнутри и аккуратно опускала его, притянув дверь. Крючок падал с той стороны в петельку. Здорово, правда?"

    "Я подумала, что хитрые мальчишки придумали такой же способ. Значит, где-то должно было быть то, чем они это сделали."

    "Я поискала вокруг, и за метлой, которая стояла возле крыльца, нашла спрятанный длинный железный прут с загнутым кончиком. А вот и ключ! Глупые мальчишки. А ещё кибернетики!"


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    scene bg handmade2 with dissolve

    "Крючок поднялся легко, и дверь открылась. В темноте я сначала не увидела ничего, кроме наваленных кучей коробок. Но за ними была спрятана эта кукла."

    "Я боялась включать свет. Но любопытство взяло верх. Я перетащила коробки к окну и щёлкнула выключателем."


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    scene cg ul_elya_workshop with dissolve

    "Эта штука оказалась вся опутана проводами. Её руки были как настоящие. Даже пальцы у неё были. Я потянула куклу за руку. Мне было интересно, может ли она сжать что-то «рукой»."

    "Пальцы куклы были гибкими. Я погладила её и подумала что назову её про себя Лолой. Вряд ли эта кукла может ходить и говорить, но выглядела она прямо как настоящий робот."

    "На спине у неё были какие-то переключатели и кнопочки. Я не удержалась и нажала одну. И чуть не умерла от страха!"

    "Кукла схватила меня за руку и повернула ко мне голову. Металлический голос внутри глухо произнес:"


    elya "Я изделие номер 410, Эля Троник. Задайте команду, задайте команду."

    "В эту секунду я поняла смысл фразы Алисы «подмочить репутацию»."


    stop music fadeout 0.5

    queue music "audio/music/z_1005.mp3" noloop


    scene cg ul_elya_diary2 with dissolve

    "Я закричала от страха, а в соседнем домике сразу зажегся свет. Я кинулась к выходу, забыв обо всём."


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    scene cg ul_elya_diary3 with dissolve

    "Конечно, дверь я не закрыла, но успела щелкнуть выключателем. Скатившись кубарем с крыльца, я бросилась в кусты. Пробежав вдоль домиков, углубилась в лес."


    scene cg ul_running_forest with dissolve

    "Я бежала, и мне казалось, что за мной гонится вся команда кибернетиков во главе с куклой-роботом."

    "Пробежав еще немного, я поняла, что наверное слегка заблудилась, так как огоньков лагеря нигде не было видно."

    "Я села под какое-то дерево. Мне хотелось плакать от злости, что я так глупо сама себя выдала и ещё струсила. Теперь Алиса точно не будет прикрывать мои проступки."

    "Только бы найти дорогу в лагерь и тихонечко прошмыгнуть в кровать, пока она ещё не проснулась."

    "С этими мыслями я пошла, натыкаясь в темноте на кусты и старые стволы деревьев, лежащие на земле. Ветки больно били меня по лицу и рукам."


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    scene bg dark_forest with dissolve

    "Фонарик не горел и как я его ни трясла, зажигаться не собирался. Я прошла ещё немного и подумала, что наверное иду куда-то в сторону от лагеря."

    "Вдруг в лунном свете я увидела какую-то полоску между деревьями. Я очень обрадовалась и быстро пошла в эту сторону. Это была тропинка!"

    "Но ведь все тропинки ведут к лагерю, подумала я. И теперь я точно попаду домой, в какую бы сторону я ни пошла."

    "Я шагала теперь быстрее и даже тихонечко пела свою любимую песню «Взвейтесь кострами»."


    scene bg ruins2 with dissolve

    "Вдруг тропинка оборвалась возле порога какого-то дома в лесу. Это были почти развалины."

    "Папа бы сказал про него, «Двухэтажный сарай» Так он называл дом бабушки."

    "Мне очень не хотелось идти дальше, но тропинок больше не было. Я всматривалась в темные окна этого мрачного дома. Лунный свет делал его каким-то сказочным и ненастоящим."

    "Вдруг он все-таки обитаем? Я заметила маленький огонек внутри, как будто кто-то зажёг свечу, а может мне это только показалось. Интересно, кто бы это мог быть?"

    "Почему никто, даже Ольга Дмитриевна, не сказал нам про эти развалины? Было страшнее, чем когда я открывала дверь в мастерскую. Но я все-таки вошла внутрь."


    stop music fadeout 0.5

    queue music "audio/music/z_125.mp3"


    scene bg ruins3 with dissolve

    "На полу лежали какие-то стеклышки, которые звонко хрустнули, когда я наступила на них. Тот свет, который я приняла за свет свечки, заметался и потух."

    "Я стояла, затаив дыхание и боясь шелохнуться. Но никакого света и звуков больше не было. Показалось."

    "От света луны, который падал сквозь выбитые окна второго этажа и провалившийся пол, были видны остатки поломанной мебели. Мои глаза привыкли к полутьме, и я стала различать мелкие предметы."

    "Я ещё раз потрясла фонарик. К моему облегчению, он неожиданно заработал. Наверное, батарейка отдохнула."


    scene cg ul_ruins with dissolve

    "Комната была довольно большой. На стене висел ковер, один угол которого свисал вниз. Я сделал несколько шагов, чтобы рассмотреть рисунок. На ковре была изображена большая кошка."

    "Точнее, силуэт кошки, чем-то напоминающий человеческий. Странная кошка."

    "Когда мы ездили с папой в Ленинград, там тоже было много каменных львов у парадных подъездов. Многие были с человеческими глазами и напоминали своими мордами лица людей."

    "Папа сказал, что раньше художники рисовали животных, о которых им рассказывали, но сами никогда их не видели. И многие изображения были с человеческими лицами."

    "Этот гобелен, наверное, был очень старым. Кто же всё-таки зажигал огонек? Пока я разглядывала кошку, эта мысль не давала мне покоя."


    scene cg ul_ruins2 with dissolve

    pause (1000000000000000000.0)


    scene cg ul_ruins3 with dissolve

    "Вдруг, мне показалось, что кошка на ковре смотрит в мою сторону. Глаза её поблескивали и были точь-в-точь как живые. Но ведь сначала её глаза были закрыты!"

    "Я могла бы поспорить с кем угодно, что они были закрыты! Я отступила назад."


    scene cg ul_ruins4 with dissolve

    "Неожиданно темный кошачий силуэт отделился от ковра и двинулся прямо на меня!"


    scene cg ul_running_forest with dissolve

    "Никогда ещё я не бегала так быстро. Я мчалась сквозь лес напролом, падая и обдирая коленки с локтями, вскакивала и снова мчалась. Мне даже кричать было страшно..."


    stop music fadeout 0.5

    queue music "audio/music/z_1003.mp3"


    scene cg reeds1 with dissolve

    "Неожиданно лес перешел в густые заросли камыша. Но я так испугалась, что готова была бежать даже сквозь заросли и остановилась, только почувствовав под ногами воду."


    stop music fadeout 0.5

    queue music "audio/music/z_1020.mp3"


    "За камышами открылась широкая полоска воды. Я обернулась. За спиной остался коридор из примятых стеблей, тропинкой уходящий в сторону леса.  Вот так дела... Опять река."

    "Я всё ещё прислушивалась, не зашуршит ли камыш. Мне казалось что ВОТ-ВОТ из него на меня бросится эта огромная кошка с человеческими глазами.  Я беспомощно озиралась вокруг."

    "Возвращаться тропинкой в камышах, где могла прятаться страшная зверюга, мне не хотелось. Светало."


    stop music fadeout 0.5

    queue music "audio/music/z_004.mp3"


    scene cg reeds2 with dissolve

    "Вдруг где-то рядом я услышала скрип и шлёпанье."

    "Из зарослей камыша показалась плывущая мимо меня лодка. Она была видна смутным силуэтом на фоне покрытой туманом реки."

    "Отступать было некуда и я подумала, что лучше если бы этот человек забрал меня в лодку, чем возвращаться той же дорогой. Поэтому я набрала воздуха и громко крикнула:"

    ul "Дяденька рыбак!"


    stop music fadeout 0.5

    queue music "audio/music/z_1007.mp3"


    "Шлёпанье стихло. И теперь лодка плыла беззвучно. Очевидно, человек перестал грести и прислушивался. Я испугалась, что лодка так и проплывёт мимо и заорала уже изо всей силы:"

    ul "Дяденька, я тут, плывите сюда!"


    stop music fadeout 0.5

    queue music "audio/music/z_004.mp3"


    scene cg reeds3 with dissolve

    "Наконец лодка развернулась и человек стал грести в мою сторону.  В лодке оказался мальчик, а вовсе никакой не дяденька. У него на шее был красный галстук."


    scene an_001_001-min with dissolve

    "Он помог мне влезть и оттолкнувшись веслом, направил лодку дальше от зарослей."


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3"


    ul "Ты кто?"

    pi "Пионер"

    "Он ответил каким-то слишком уж спокойным голосом и налег на вёсла. Как будто встреча с девочкой в камышах ранним утром была для него обычным делом."

    "На дне лодки я увидела ведро с плескавшейся рыбой. Удочки лежали тут же. Я силилась вспомнить его, но так и не вспомнила."

    "А ведь я уже знала в лицо всех мальчиков в лагере. Наверное, новенький. Но когда же он успел приехать? Ведь солнце ещё даже не встало, а автобус всегда приезжал только после обеда."


    #Анимация Пионер моргает

    image pi_blinking:
  
        "images/cg/cg_day4/cg pi_blink1.webp" with Dissolve(0.5, alpha=True)
        pause 0.5  
        "images/cg/cg_day4/cg pi_blink2.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/cg/cg_day4/cg pi_blink1.webp" with Dissolve(0.5, alpha=True)
        pause 9.5
  
        repeat


    scene pi_blinking with dissolve

    "Я вглядывалась, но так и не смогла увидеть его глаз. Густая челка закрывала их почти полностью."


    scene an_001_001-min with dissolve

    ul "Как ты видишь сквозь свои волосы?"

    "Он улыбнулся одним ртом. Это было так неожиданно, что я вздрогнула."

    pi "Тому, кто всё видит, глаза не нужны."

    ul "Ну и подумаешь! Не хочешь со мной разговаривать, так и скажи. А не строй из себя непонятно что"

    ul "Мог бы хоть спросить меня о чем-то, а не грести молча. Ты ведь даже не знаешь как меня зовут."

    ul "Кстати, куда мы плывём? Мне нужно в лагерь, а ты плывёшь по течению. Разве лагерь там?"

    "Пионер хмыкнул."

    pi "Какая разница? Ведь река всё равно течет по кругу. По течению легче."

    ul "Почему по кругу?"

    "Я плюхнулась на дно лодки, потому что от резкого рывка ускорившейся лодки, меня бросило назад."


    scene cg pi_blink1 with dissolve

    pi "Потому. Тебе-то уж, Ульяна, это хорошо должно быть известно."


    stop music fadeout 0.5

    queue music "audio/music/z_201.mp3"


    scene an_001_001-min with dissolve

    "Я онемела. Откуда он знает моё имя, ведь я не говорила ему?"

    ul "А может, я не Ульяна, а Марьяна!"


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3"


    "Пионер снова засмеялся одним ртом."

    pi "Ты — Ульяна Ленина, твой папа — известный журналист. У такого образованного человека могла бы быть более смышлёная дочь."

    "Пионер продолжал грести. Я молчала. Мне захотелось сказать ему что-то обидное, чтобы увидеть, как с этого мальчишки слетит его спесь."

    ul "Вы тут с Ольгой Дмитриевной на всех досье собираете? Ты её помощник, да? Как я сразу не догадалась? У нас таких называют сексотами."

    "Пионер перестал грести и наклонился ко мне, упершись локтями в весла."

    pi "А что ты знаешь про Ольгу Дмитриевну?"

    ul "Знаю, что у неё в домике живет Семён!"

    "Пионер снова налёг на вёсла."

    pi "Ах, этот, Семён. Да ты не так уж мало знаешь..."

    "Я вдруг почувствовала, что этот мальчик — просто находка для нас с Алисой.  Надо было срочно разговорить его. Он, конечно, странный, но похоже в курсе всего, что происходит в лагере."

    ul "Ты про тропинки знаешь?"

    "Пионер кивнул. Тогда я решилась."

    ul "Там в лесу есть старые развалины. И мне показалось..."


    stop music fadeout 0.5

    queue music "audio/music/z_208.mp3" noloop


    "Он не дал договорить и быстро закрыл мне рот ладонью. От этого лодка развернулась и сделала на воде круг. Волна ударила в борт и лодка, остановившись, закачалась."


    stop music fadeout 0.5

    queue music "audio/music/z_124.mp3"


    pi "Больше ни слова."

    "Он наклонился к моему уху и заговорщицки прошептал:"

    pi "САХАР."

    "Я ждала, что он скажет ещё что-нибудь, но он молчал."

    ul "Что — «сахар»?"

    pi "Она любит сахар. Когда ты пойдёшь туда снова, возьми с собой сахар."

    "Между тем лодку снесло к берегу и она уткнулась носом в песок. Пионер выпрыгнул из неё и прихватив своё ведёрко и удочки, стал быстро удаляться. Я опешила:"

    ul "Эй, ты, с чёлкой! Ты даже не подашь мне руку? Это невежливо! Я даже не знаю, куда идти!"


    scene cg ul_pi_leaving with dissolve

    "Пионер оглянулся и помахал мне ведёрком."

    pi "Иди вот по этой тропинке. Тут недалеко. Если что, приходи к реке. Я сам тебя найду!"

    "И он исчез. В моей голове смешались разные чувства и мысли. Я вспомнила любимое выражение отца – «Каша в голове».  Да, это было самое точное определение того, что творилось в этот момент в моей голове."

    "Я побежала по тропе, на которую указал мне Пионер. Только бы Алиса ещё не проснулась!"


    scene cg ul_pi_leaving with dissolve

    pause (10000000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    scene bg auhouse4 with dissolve

    "Я влетела в домик, не раздеваясь кинулась в свою кровать и завернулась в одеяло. Оставив щелочку, я смотрела на кровать Алисы. Интересно, она вставала ночью?"

    "От звука хлопнувшей двери Алиса проснулась. Приподняв голову, она обвела взглядом комнату. Было ясно, что она ещё не проснулась полностью. Я накрылась с головой и замерла."

    "Глубоко вздохнув, Алиса опустилась на подушку, повернулась ко мне спиной и засопела."

    "Пронесло! Раздеваться под одеялом было неудобно, но я справилась. Я отогнала всякие мысли, от которых точно бы не уснула."

    "И, кажется, провалилась в сон так глубоко, что когда сыграл пионерский горн, которым нас будили каждое утро, Алисе пришлось долго меня тормошить."


    show sp_al_043:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Когда она убедилась, что разбудить меня не удастся, то отступилась."

    "Оглядев мои поцарапанные коленки, сказала:"

    al "Опять тебя черти носили где-то ночью."


    scene bg auhouse3 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "И уходя, бросила:"

    al "Крикну за тебя на линейке. Оторва..."



    scene black with fade

    stop music fadeout 1.0

    jump day5


return
    