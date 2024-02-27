label day31:

    $ days = 31

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"


    scene cg od_sl_earful with dissolve

    "После Дня Рождения Жени к нам утром пришел Семен и рассказал о том, что Ольга Дмитриевна как-то прознала, что нас не было всю ночь. Шум поднимать не стала, но вызвала Славю."

    "Ну, та ей все как на духу и выложила. И про конкурс, и по купание ночью. В общем, она же правильная пионерка. Ну, вы понимаете."

    "Но в конце Семен сказал, что все уладил."


    scene bg odhouse7 with dissolve

    show sp_sem_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    "Он объяснил ОД, что ситуация, когда дочь директрисы фактически является зачинщиком мероприятия, делает историю очень щекотливой, и что тут надо осторожно спустить все «на тормозах»."

    "Потому что Маргоша повесит всех собак на ОД. А Женьку будет выгораживать."


    scene bg odhouse6 with dissolve

    show sp_od_022:
        yalign 0.03 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2 
    with dissolve

    "Ну, ОД задумалась." 


    scene cg od_je_earful with dissolve

    "Потом она позвала Женю, и они о чем-то очень долго беседовали. Как результат, всё замяли. В общем, Женя сказала, когда уходила от ОД, что беспокоиться больше не о чём."


    scene bg camp_artifacts with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2 

    "Но физрук (думаю, по заданию ОД) провел обыск по всем домикам. Наверное, искали спиртное. Но, понятно, не нашли."


    scene bg oldcamp_hide with dissolve

    "Думаю, оно (если осталось) все еще в той нычке в Старом лагере, на чердаке. В рюкзачке."

    "И я подумала, что надо его перепрятать. Мало ли. Один раз пронесло. Но не факт."


    stop music fadeout 1.0


    play music "audio/music/z_010.mp3"


    scene cg pioneers_message with dissolve

    "И тут, как раз в разгар беседы, снова прибежал «почтовый голубь» (мальчик из 7 отряда) и принес мне записку. Я дала ему конфет, и он убежал."

    "Записка была от Пионера. Я очень обрадовалась."

    "А Семен все пытался через плечо почитать, что там написано. Но получил щелчок по носу. И все спрашивал: «От кого, от кого?»"

    "Понятное дело, я не сказала. Хотя, он давил на то, что между друзьями (а мы друзья) не может быть тайн. А про Женьку однако он мне ничего не рассказал. Друг, называется. Так что..."

    "В общем, в записке была просьба встретиться (вот она)."

    pause (10000000000000000000000.0)


    scene bg nbeach with dissolve

    "Но не на отмели. Пионер написал, что заберет меня с Ближнего пляжа, и я побежала туда."


    scene bg auhouse3 with dissolve

    "А потом бегом назад, вспомнила, что я не взяла купальник. Схватила еще Мишку своего плюшевого (он приносит удачу). И понеслась как ветер."

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    "Алиса что-то вслед мне крикнула. Но я уже не разобрала."


    stop music fadeout 1.0


    play music "audio/music/z_004.mp3"


    scene an_d31_06 with dissolve

    "В общем, Пионер уже ждал. Мы обогнули остров Ближний и попали прямо на середину реки. Нас понесло течение."


    image an_31_01: # Анимация Ульяна Пионер в лодке с медведем
        
        "images/an/an31day/an_d31_01.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_02.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_03.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_02.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_03.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_04.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_03.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_02.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_05.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
        "images/an/an31day/an_d31_06.webp" with Dissolve(0.5, alpha=True)
        pause 1.0
       
        repeat


    scene an_31_01 with dissolve
    
    pause (10000000000000000000000.0)

    scene an_d31_06 with dissolve

    "И я спросила:"

    ul "А куда мы плывем? К чему такая спешка? Ты же говорил, что тебе надо на время скрыться, и что тебя ищет Генда. Уже нет?"

    pi "Он и сейчас ищет. Я хотел тебе показать остров Дальний и кое что рассказать."

    pi "Я узнал, что у вас будет поход на остров. Причем, после обеда уже объявят сбор. Но мы быстро метнемся туда и обратно. Успеешь."

    ul "Но мы же все равно туда пойдем, смысл?"

    pi "Там были боевые действия. Петрович не рассказывал? Так вот, я покажу тебе, куда ходить нельзя."

    pi "Есть неразорвавшиеся мины и много всего. Там чистили, но не всё. Остров изрезан валунами, и там очень густой кустарник."

    pi "В истоках ручья есть склад немецких боеприпасов и есть оружие. Оно в смазке лежало все годы. Абсолютно рабочее. Если попадет кому-то в руки, будет беда."

    pi "Тем более, что немцы заминировали склад."

    ul "А ты за меня испугался или за наш отряд?"

    pi "(Покраснев) \nЗа всех. Ну и за тебя особенно."


    stop music fadeout 1.0


    play music "audio/music/z_012.mp3"


    scene bg far_island_rocks with dissolve

    "И скоро мы были у острова. Течение быстро донесло лодку. Но причалили мы с другой стороны. Этого берега я не знала."

    show location_open_rocky_coast with dissolve


    pause (10000000000000000000000.0)


    hide location_open_rocky_coast
 

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А где баркас? Мы его решили починить."

    hide sp_ul_021
 
 
    show sp_pi_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Это самая скалистая часть острова. Баркас за тем мысом. На заброшенном пляже. Пошли, кое-что покажу."

    hide sp_pi_001

    "Он отвел меня через огромные валуны в северную часть острова. Там, действительно, «чёрт ногу сломит»."

    "Показал, где склад немцев. Мы в него не пошли. Он только сломал веточки вокруг и сказал: «Будет вам примета»."


    scene bg far_island_beach with dissolve

    "Потом снова сели в лодку, обогнули остров слева (ну, если на карте смотреть) и высадились на берег."

    "Мы там искупались. Потом он взял меня за руку и сказал:"


    stop music fadeout 1.0


    play music "audio/music/z_1013.mp3"


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Не стоит тут задерживаться надолго. Остров только с виду спокойный. Когда будете тут в походе, знайте, что ближе к вечеру тут происходят странные вещи, а ночью появляются огни."

    hide sp_pi_009


    show sp_ul_036:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот здорово! Люблю такое. А то я про упырей и вурдалаков только в книжках читала. Оборотней. Вот бы посмотреть на них!"

    hide sp_ul_036


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Оборотней? Да, тут полно оборотней. Больше всего их в вашем лагере."

    pi "А ты в курсе, что тут рядом есть Дом с привидениями? Или, как все его называют, Дом на Болотах."

    hide sp_pi_009


    show sp_ul_036:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, мне рассказывала Юля про него. Покажешь?"

    hide sp_ul_036


    scene bg shouse_far with dissolve

    pi "Вон он, виден отсюда. Смотри. Расскажу. Но мы туда не пойдем, я просто покажу тебе его издали. В полнолуние там особенно страшно. Дом давно заброшен."

    pi "Но по ночам из него слышен женский голос. Точнее, детский."


    show sp_ul_047:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что? Там живет ребенок?"

    hide sp_ul_047


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Не совсем. Ну что, хочешь его увидеть?"

    hide sp_pi_009


    show sp_ul_042:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да что за вопросы! Конечно! А можно, я потом расскажу Алисе про это?"

    hide sp_ul_042


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "С ним связана одна легенда. Там жила до революции одна семья. Муж, жена и дочь. Девушка, дочь, была очень красивая. Отец ее был горный инженер и работал на прииске."

    pi "В те годы прииск был богатый и владел им один золотопромышленник. Он и положил глаз на девочку. Ей было примерно лет как тебе."

    pi "Он остановился в доме инженера, когда приехал из столицы по делам. В одну из ночей он попытался совратить девочку."

    hide sp_pi_009


    show sp_ul_049:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И что, она утопилась? Прямо, как пишут в книжках? У-у, какая страшная и интересная история!"

    hide sp_ul_049


    scene cg shouse_girl2 with dissolve

    pi "Нет, всё было еще хуже. Она зарезала его. Отец узнал о трагедии поздно, он был на руднике."


    scene bg shouse_far with dissolve

    show sp_ul_047:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И что было дальше? Она утопилась?"

    hide sp_ul_047


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Вот ты неугомонная! Утопленница в этой истории была. Это её мать. А утопилась она с горя. Потому что девочку так и не нашли потом. Даже историю с совращением люди, как мне кажется, додумали."

    hide sp_pi_009


    show sp_ul_048:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А девочка что?"

    hide sp_ul_048


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Девочку долго искали. Было следствие. Следователь жил неделю в поселке, но так и уехал ни с чем."

    pi "У него были только два вещественных доказательства. Нашли её туфельки на берегу. И ещё нож в крови. Ну, ты понимаешь. Людская молва и всё такое."

    pi "Отец лишился сразу двух любимых людей. Очень горевал. Потом была революция. Всем стало не до происков. И история эта стала легендой."

    hide sp_pi_009


    show sp_ul_048:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А девочка что?"

    hide sp_ul_048


    scene cg shouse_girl with dissolve

    pi "Девочка исчезла. Но местные говорят, что в доме живет привидение."

    pi "Возможно, это мать девочки. По местной легенде, каждую ночь, когда идет сильный дождь, в доме зажигается свет."

    pi "И как будто даже видели, как утопленница подходит к окну и смотрит. Ищет дочь. И если увидит какую-нибудь девочку, то забирает ее себе."


    scene cg drowned with dissolve

    pi "Другие наоборот говорят, что она появляется ночью в омуте, и утаскивает купающихся. Хотя, это легенда, конечно. Надеюсь, ты не купаешься ночью?"


    scene bg shouse_far with dissolve

    show sp_ul_049:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет..."

    "И тут я соврала от страха, что не купаюсь. А сама подумала, что надо предупредить всех, чтобы ночью больше не купались."

    hide sp_ul_049


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "И ещё, третья версия, что утром, когда туман, они обе появляются разом. Всё зависит от фантазии местных рассказчиков."

    pi "Впрочем, тут вокруг конопля растет. Ты, наверно, понимаешь, откуда у них такие глюки? Курят тут все."

    hide sp_pi_009


    show sp_ul_048:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И ты тоже?"

    hide sp_ul_048


    show sp_pi_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    pi "Я вообще не курю. Не умею."

    hide sp_pi_009

    "И мы прошли вдоль берега до самого того места, откуда дом с острова стал хорошо виден."


    scene bg shouse3 with dissolve

    pi "А вот и дом... Смотри!"

    ul "Да, вижу. Какой он черный! И страшный. Ух, аж мурашки по телу. Особенно после твоих рассказов. Сплаваем туда?"

    pi "Нет уж. Я ещё не сошёл с ума."


    stop music fadeout 1.0


    play music "audio/music/z_012.mp3"


    scene bg far_island_beach with dissolve

    "Мы вернулись на пляж и болтали. Ещё купались и сидели мокрые обнявшись, и... (Но об этом я не буду тут писать)."

    "Хоть ничего такого, чего боится Алиса (она вечно: «Смотри, что бы ничего такого!»), у нас не было."

    
    scene bg camp_artifacts with dissolve

    "К обеду я была уже в лагере и на обеде рассказала Алисе про поездку с Пионером."

    "А после обеда, как и сказал Пионер, для нашего отряда объявили сбор и сказали, что мы идем в Третий Поход НА ОСТРОВ."




    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day32

return 