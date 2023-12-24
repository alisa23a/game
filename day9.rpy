label day9:
    
    stop music

    play music "audio/audio9day/z_026.mp3" noloop

    scene cg alise_guitar with dissolve:
        # Start at full image
        crop (0,0, 1920, 1080) size (1920, 1080)
        subpixel True
        # Over 3.0 seconds move to focus on the cropped area and rescale up to size
        linear 1.0 crop (0, 157, 1468, 826) size (1920, 1080)

    "Когда я вернулась с отмели, то застала Алису играющую на гитаре."

    "Думаю, она играла, что бы отвлечься. Она переживала за меня потому, что я пришла позже, чем мы договаривались. Она быстро отложила гитару."

    stop music

    play music "audio/audio9day/z_023.mp3"

    scene bg auhouse_crop2
    
    show sp_al_045:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну слава богу! \n(обнимает)"
    
    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Никто меня не хватился?"

    scene bg auhouse_crop2
    
    show sp_al_045:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Нет. Ты надежно прикрыта легендой о твоей простуде. Кстати, надо нагнать температуру и отправить тебя к Виоле. Я уже приготовила кусочек сахара с каплей йода. Это сработает. Съешь."

    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Ладно. А есть другой способ?"

    scene bg auhouse_crop2
    
    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Есть, но он тебе не понравится."

    scene bg auhouse_crop1
    
    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Интересно, интересно…"

    scene bg auhouse_crop2
    
    show sp_al_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Понимаешь, (краснеет), нужно очистить луковицу, слегка надрезать ее, чтобы сок выделялся и поместить... Ну в общем... Поместить ее в «одно место», И через полчаса... "

    scene bg auhouse_crop1
    
    show sp_ul_024:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Ужас какой!"
    
    hide sp_ul_024
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Нет. Это точно, мне не подходит. Лучше сахар. Сахар, это нормально. А есть чем померить температуру?"

    scene bg auhouse_crop2
    
    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Вынимает градусник) \nА это что? Выпросила у медички."

    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "(Кидает сахар с йодом в рот и ставит себе градусник) \nЯ знаю, по лицу вижу, что ты хочешь спросить про Пионера, но молчишь из деликатности. Ну спроси."

    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Да хочу. Тебе там понравилось? Расскажешь? Какой он вообще? Он был, надеюсь, джентльменом?"

    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "Да.. Он хороший. Ничего такого не позволял себе. Если ты об этом. Ловили рыбу. Я поймала несколько. Сама! Представляешь! Но главное, он много рассказал об истории лагеря. Про всякие странные вещи.. "

    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Какие?"

    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    ul "На всю ночь рассказов. В общем, меня распирает от желания поделиться. Но вечером. Сначала нужно сделать алиби. Посмотри, есть температура?"

    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Забирая градусник) \nОго, аж тридцать восемь и два. Быстро йод сработал. Беги в медпункт. Выпроси еще один день. Думаю, мы сможем метнуться и посмотреть окрестности."


    image injection:
        
        "images/an/an9day/injection/injection_01-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_02-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_01-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_02-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_03-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_04-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_05-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_06-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_07-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_06-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_05-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_04-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_03-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an9day/injection/injection_02-min.png" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    scene injection_bg-min

    stop music
    
    play music "audio/audio9day/z_018.mp3"

    show injection
 
    "И я побежала в медпункт. Виолета Церновна всплеснула руками при виде температуры. Я хотела убежать."
 
    "Но не тут-то было! Она тут же вколола мне какое-то лекарство. А я так боюсь уколов! Но я выдержала, я же настоящий пионер-ленинец. Зато она сразу дала мне освобождение еще на один день."

    stop music

    play music "audio/audio9day/z_020.mp3"

    scene cg alise_guitar with dissolve:
        # Start at full image
        crop (0,0, 1920, 1080) size (1920, 1080)
        subpixel True
        # Over 3.0 seconds move to focus on the cropped area and rescale up to size
        linear 1.0 crop (0, 157, 1468, 826) size (1920, 1080)

    pause (109.0)
 
    scene bg auhouse_crop1

    stop music

    play music "audio/audio9day/z_023.mp3" 
 
    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45
   
    "Дорога, ведущая от лагеря куда-то в лес, постоянно меня манила. И я завела с Алисой разговор."

    ul "А почему бы нам не сбежать после обеда вместо пляжа в лес? Толик бы нас прикрыл. В случае чего, скажешь потом, что тебя срочно позвали на кухню чистить картошку. А я болею."

    scene bg auhouse_crop2
    
    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "А зачем нам в лес?"
 
    scene bg auhouse_crop1
    
    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Ну, помнишь ту дорогу? Как думаешь, куда она ведет? Ни разу Ольга Дмитриевна не ответила мне на этот вопрос. Может, там ТАЙНА?"

    scene bg auhouse_crop2

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Везде тебе тайны мерещатся, Ленина. Ну дорога и дорога. Старая. Видно, что по ней сто лет никто не ездил. В ту сторону нам запрещено ходить, слышала же? Она аж за поселок Горняков идет. Там глухомань. Заблудимся, что потом?"

    scene bg auhouse_crop1

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Ну хотя бы одним глазком глянуть и сразу обратно! Я же вижу, ты тоже хочешь посмотреть. Тетя Люба говорила, что как-то раз там рысь видели. Ну, на дороге. Она зимой приходила."

    scene bg auhouse_crop2

    show sp_al_045:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Откуда тетя Люба знает-то?"

    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Ну, она же поселковая. Живет рядом, а на лето устраивается кашеварить в лагерь. Петрович про нее рассказывал. А рысь, она пришла в лагерь, может от голода? Что-то стащила на кухне и ушла по этой дороге."

    ul "Петрович еще с ружьем ходил по следу, но не нашел ее. И хорошо. Рыську было бы жалко. Она ничего плохого никому не делала."

    scene bg auhouse_crop2

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Подумав) \nХорошо. Давай так, сбегаем по быстрому. Если дорога совсем плохая будет, мы вернемся. Ладно? Сейчас я фонарики и рюкзак возьму."


    stop music

    play music "audio/audio9day/z_019.mp3"

    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "И надо забежать в столовку, взять сухарей, я знаю, где тетя Люба их сушит. И воды."

    scene bg auhouse_crop2

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Вода там есть, наверно. С горы много ручьев стекает. Флягу возьмем и если что, наберем. Вон, жара какая. Тащить лишнее? Нет уж, увольте! Чеши за сухарями, а я рюкзак соберу."


    scene bg road_to_nowhere

    stop music

    play music "audio/audio9day/z_012.mp3"

    "Через пол часа мы уже бодро шагали по старой дороге, которой решено было дать название - ДОРОГА В НИКУДА."

    scene bg road_to_nowhere2

    "Дорога долго петляла по лесу и наконец, вывела нас на небольшую полянку на опушке леса с толстым дубом на краю."

    "Там Алиса предложила мне съесть часть припасов."

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Пойдем налегке."

    hide sp_al_005

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А когда я съем припасы, они что, улетучатся?"

    hide sp_ul_014

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Нет."











    pause (10000000000000000.0)

























return
    