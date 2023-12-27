label day9:
    
    $ days = 9
    
    stop music

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

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
    
    show sp_al_053:
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
    
    show sp_al_052:
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
    
    show sp_al_052:
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


    # stop music

    # play music "audio/audio9day/z_019.mp3"

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

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А когда я съем припасы, они что, улетучатся?"

    hide sp_ul_013

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Нет."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Но тогда получается, мы все равно несем их, только внутри? Не получается НАЛЕГКЕ."

    hide sp_ul_012

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну ты вредина! Какая разница? Ну они тогда правильно распределятся по организму."

    hide sp_al_006

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А разве в моем рюкзаке они распределены неправильно? Я положила как ты учила – все тяжелое вниз, а легкое наверх. Вот когда я несу рюкзак, то моя котлетка находится в нем, а рюкзак ниже уровня пояса, так?"

    hide sp_ul_013

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну, так."

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Вот. Теперь я съедаю котлетку и она попадает в желудок. Так?"

    hide sp_ul_013

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну... так."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А желудок находиться выше уровня пояса! Значит центр тяжести нарушается. И получается не налегке, а НАТЯЖЕЛЕ! Нет, так не пойдет. Пусть уж лучше мои котлетки будут в рюкзаке, пока мы идем."

    hide sp_ul_012

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А сейчас пока съедим твои. Правильно я придумала?"

    hide sp_ul_014

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Удивлённо) \nВот хитрюга! Ладно, давай сначала мои."

    hide sp_al_006

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Смотри, что это там среди веток?"

    hide sp_ul_013

    show sp_al_010:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Где? Я не вижу. Ты покажи рукой."

    hide sp_al_010



    scene bg lyhouse_empty

    ul "Так вот же дуб! Ну, ты слепая, что ли? Видишь такую большую ветку? Там что-то есть. Вон, пятнистое такое, «мелькается». Вот, снова... Вот же, вот!"


    al "Мелькается? Ну когда, Ленина, ты русский язык выучишь? Нет такого слова. Да, что-то там есть. Теперь и я вижу."


    stop music
    
    play music "audio/audio9day/z_023.mp3"

    scene bg lyhouse

    pause (10000000000000000.0)

    show sp_al_054:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ой. Это же... Это же ОНА, Рысь! Бежим! Да не к дереву, глупая! Куда?! Назад! Прячься!"

    hide sp_al_054

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А чего бояться? Ну кошечка. Ну немного больше, чем Тузик. Она точно не злая. Вспугнешь её своими воплями. \nКыс-кыс-кыс."

    hide sp_ul_014

    show sp_al_054:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Куда ты?! Она не даст себя погладить! Это же дикая зверюга."

    hide sp_al_054

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А я ей котлетку! Ну-ка, дай мне мой рюкзак."

    hide sp_ul_012

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну ты отчаянная... Ладно, держи котлету. Просто кинь её возле дерева. Она сама возьмет, если захочет. Только не подходи к ней! Я слышала, они на жертву прыгают сверху. Так охотятся. Бац, на холку и кранты!"

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "(Бросая котлету) \nКыс-кыс-кыс... Давай, кушай, маленькая. Смотри, обнюхивает. Нет, не взяла. Убегает! Это ты виновата. Зверюга, зверюга! Она, может, обиделась."

    hide sp_ul_012


    scene bg lyhouse_empty


    stop music
    
    play music "audio/audio9day/z_025.mp3"

    pause (10000000000000000.0)

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ничего она не обиделась, просто она ест сырое мясо, а не как мы, котлеты. Ладно, она уже не вернется. Красивая. Ты видела? Грациозно так спрыгнула с дерева. Рассказать кому, ведь не поверят. Эх, фотоаппарат бы!"

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Да, фотик бы не помешал. Надо будет одолжить в нашей фотостудии. Обидно. Уже столько всякого интересного случилось, а мы не фотографировали. Что останется в памяти, когда мы будем старенькими? Что покажем внукам?"

    hide sp_ul_013

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Скажут, врёшь ты все, бабушка Алиса! \n(Передразнивает Алису)"

    hide sp_ul_014

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну, до этого еще далеко. Ещё нафотаем всяко-разно. Я лично, бабушкой не буду."

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Я тоже до старости доживать не буду. Скучно это. Идешь такая карга, с клюкой, а все тебе место уступают на лавочке. «Садитесь, бабуля!» Фу, кошмар! Лучше умереть молодой, со знаменем в руках, за рабочее дело. Как дедушка Ленин."

    hide sp_ul_012

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Так вот, он как раз умер не со знаменем, а в кресле. Больной и малость не в себе. И к тому же, он уже стареньким был."

    hide sp_al_005

    show sp_ul_016:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Не верю! Его Каплан убила! Я читала! Нет, Ленин всегда молодой! Так в песне поется!"

    hide sp_ul_016

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Собирая рюкзаки) \nЛадно, уговорила. Умрем молодыми. Пошли уже! Нам еще идти вон до той горы, а вернуться нужно до вечерней проверки."

    al "Давай так, если еще что-то интересное попадется, то задержимся на часик. А если нет, то быстро назад. А то заблудимся в потемках."

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Дорога же есть. И фонарики мы взяли. Нет, не заблудимся. А вот тропка идет от дуба. Давай одним глазком глянем? Там точно ТАЙНА. Я же чую. Я всегда такое чую."

    hide sp_ul_013

    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Слегка поколебавшись) \nНу ладно. Только одним глазком! Чуйка у неё, понимаешь! А вот я чую, опоздаем мы на вечернюю проверку. И влетит нам, мама не горюй!"

    hide sp_al_044

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Не влетит. Пошли! Пошли! \n(Тянет Алису за руку)"

    hide sp_ul_014

    "Мы пошли по тропинке, но вскоре та упёрлась в скалу и закончилась."
    
    scene bg cave
    
    stop music
    
    play music "audio/audio9day/z_015.mp3"

    pause (10000000000000000.0)

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну вот и вся твоя тайна. \n(насмешливо). \nИ что твоя чуйка? Где тайна?"

    hide sp_al_003

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Погоди, смотри. \n(раздвигает руками кусты) \nВидишь, нора?"

    hide sp_ul_013

    show sp_al_010:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Фу ты. Вот это да! В такую нору медведь пролезет. Не, я туда не пойду. А вдруг там и впрямь медведь или рысь? Не думаю, что им понравится, что мы вломились к ним в дом."

    hide sp_al_010

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Нет, это не нора. Смотри-ка, колея какая-то. Да, вот, точно, остатки какой-то тележки. Наверное, тут что-то возили из этой пещеры."

    hide sp_ul_013

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Да, пожалуй. Вот и остатки груза в тележке. Это знаешь что?"

    hide sp_al_005

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Что? Камешки какие-то и блестят очень. Прямо как стеклышки! Красиво, радуга."

    hide sp_ul_012

    # stop music
    
    # play music "audio/audio9day/z_014.mp3"


    scene cg mica

    al "Это слюда!"

    al "Тут, видно, слюдяные шахты были. Слюду добывали."

    scene bg cave

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Только судя по тележке, очень давно. Видишь, от колеса только ободок остался. И тот проржавел давно. И скобы какие-то."

    stop music fadeout 1.0

    play music "audio/audio9day/z_014.mp3"

    scene bg in_cave

    "Было немного страшно, конечно, но любопытство было сильней. Мы вошли в пещеру и остановились, вглядываясь в сумрак."

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "А зачем слюда?"

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Ну, раньше её вместо стекол использовали в окнах. Конечно тускло. Но свет все-таки хоть какой-то. Крыши крыли вместо черепицы как в поселке Горняков. И ещё в приборах вроде, как изолятор. Это надо у кибернетиков спросить."

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Можно я кусочек слюды возьму?"

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Нет, ты так быстро захламишь наш маленький домик. Да и не нужен он тебе. Еще булыжники мы с собой не таскали."

    hide sp_al_004

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "(Тут же забыв о слюде) \nА давай пойдем туда? Мне страсть как хочется в пещеру! Я в пещерах никогда не была."

    hide sp_ul_012

    # stop music fadeout 1.0

    # play music "audio/audio9day/z_013.mp3"

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Мы на пещеру не рассчитывали. Заблудимся. У нас даже веревки нет. Если там ходы запутанные, то как выберемся без веревки? И потом, батареек хватит максимум на час. Нет. Если идти, то надо хорошо подготовиться."

    al "И знаешь, лучше с кем-то из старших. Или хотя бы с отрядом."

    hide sp_al_005

    stop music fadeout 1.0

    play music "audio/audio9day/z_016.mp3"

    show sp_ul_016:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "(С сожалением) \nВот жалость-то какая."

    hide sp_ul_016

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Да, ты права. Это я немного увлеклась. Ты мудрая. Что-то мне в голову сразу про веревку и батарейки не пришло."

    hide sp_ul_013


    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "Зато мы можем съесть наши котлеты прямо в пещере. Пещерный ужин, представляешь? Это же романтично. Я вот в пещере никогда не ужинала еще."

    hide sp_al_006

    show sp_ul_014:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "(Насмешливо) \nАга, и не завтракала и не обедала и не полдничала и не..."

    hide sp_ul_014


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al "(Толкает ее) \nДа ладно тебе! \n(Обе смеются)"

    hide sp_al_003

    show sp_ul_012:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "Хорошо, доставай."

    hide sp_ul_012


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 0.5
    
    al " Только чур, как съедим бутерброды, сразу назад в лагерь. Договорились?"

    hide sp_al_005

    show sp_ul_013:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 0.45

    ul "(Вздохнув) \nДоговорились."

    hide sp_ul_013

    jump day10



return
    