style ReadAlDi_text:
    color "#fff"
    font "fonts/mateur-webfont.ttf"
    size 50


screen read_alice_diary:

    tag menu
    zorder 300
    modal True

    style_prefix "InvItemStyleTitle"

    button:
        xpos 485 ypos 284
        xsize 940 ysize 65
        idle_background "gui/bg_1x1_transparent.png"
        hover_background "gui/bg_1x1_transparent.png"
        style_prefix "ReadAlDi"
        text "Читать дневник Алисы" xalign (0.5) yalign (0.5)
        #focus_mask True
        action Hide ("read_alice_diary"), Jump("alice_diary")



# screen alice_diary:

    # add "cg al_diary" 





screen brick_wall:

    # Кирпич

    tag menu
    modal True
    zorder 300

    add "inv_012_001"

    imagebutton:
        xpos 1563 ypos 511
        idle "images/investignation/12/brick.png"
        hover "images/investignation/12/brick.png"
        action Hide ("brick_wall")


label start_investignation_12:

    scene bg secret2

    "Когда я нашла заколку Алисы, я подумала, что ничего странного в этом нет. Заколка лежала под лавочкой недалеко от нашего домика. Может быть, Алиса сидела там с кем-то из мальчишек."

    "Но потом я вспомнила, что Алиса никогда не садилась на эту лавочку. Она сказала, что эту лавочку видно из окна домика Мику. А Мику — известная болтушка."

    "Поэтому никакая это не нычка, а скорее, антинычка. Значит, тут Алиса точно сидеть не могла. Тогда что тут делает её заколка? Загадка..."

    "И я на всякий случай заглянула еще раз под лавочку. Ничего больше не нашла."


    scene inv_012_001

    "Но зато я обнаружила, что за скамейкой, в кирпичном фундаменте домика, как будто один кирпич стоит криво. Я попробовала его вытащить."


    show screen brick_wall


    pause (10000000000000000000000.0)


    image inv_012: # Анимация кирпичи

        # "images/investignation/12/inv_012_001.webp" with Dissolve(0.5, alpha=True)
        # pause 0.5
        "images/investignation/12/inv_012_002.webp"
        pause 0.1
        "images/investignation/12/inv_012_003.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_004.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_005.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_006.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_007.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_008.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_009.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_010.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_011.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_012.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_013.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_014.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_015.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_016.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_017.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_018.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_019.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_020.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_021.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_022.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_023.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_024.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_025.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_026.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_027.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_028.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_029.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_030.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_031.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_032.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_033.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_034.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_035.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_036.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_037.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_038.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_039.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_040.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_041.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_042.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_043.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_044.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_045.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_046.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_047.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_048.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_049.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_050.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_051.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_052.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_053.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_054.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_055.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_056.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_057.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_058.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_059.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_060.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_061.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_062.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_063.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_064.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_065.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_066.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_067.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_068.webp" with Dissolve(0.5, alpha=True)
        pause 0.1
        "images/investignation/12/inv_012_069.webp" with Dissolve(0.5, alpha=True)
        pause 0.1


    scene inv_012

    $ renpy.pause(7, hard=True)


    "Он вынулся легко. Образовался тайник. Я сунула туда руку и вытащила дневник. Это был дневник Алисы. Так вот где она, оказывается, его прячет!"

    $ item_alice_diary = True


    "И я долго не позволяла себе его открыть, хотя это было легче легкого. Я хотела положить его на место, но потом подумала: я, как настоящий репортер-писатель, должна быть в курсе всего."

    "А вдруг Алиса потеряет дневник? И только я сохраню воспоминания и запишу их."

    "И вот я сказала себе, что мне как подруге неверное можно заглянуть. Все равно я сохраню тайну. И потом, возможно ей нужна помощь, а сама она не скажет, она очень гордая."

    "А потом я скажу Алисе, что читала. И так будет честно. Но не сразу скажу, а когда уже всё закончится. Или не скажу. Я ещё не решила."

    "И я подумала, что смогу прочитать дневник потом, при более удобном случае. А пока нужно было положить его обратно. Что я и сделала."

    scene black

    jump secret2_ds



label alice_diary:

    #$ config.rollback_enabled = False

    scene cg al_diary

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_017.mp3"

    scene cg al_desk with dissolve

    "{b}Запись 1{/b} \nСегодня нам раздали дневники. Спохватились. Уже неделя почти, как мы в лагере. Не иначе очередная показуха. Хотя не похоже. Мы не обязаны их сдавать. Ладно."

    "Все какое-то развлечение. Напишу что ни будь. В лагере скучно…  мальчики какие-то мягкотелые, все строятся под администрацию. Если хоть один стрельнет у меня сигаретку, я сильно удивлюсь."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_206.mp3"

    scene spectacle_17 with dissolve

    "{b}Запись 2{/b} \nВчера навела шороху во втором отряде. Там у них есть Лысый, которого все слушаются. Бывший вожатый. Интересно, за что его разжаловали. Наверное умничал много."

    "Пошла послушала, что он им впаривает.  Похоже, хочет устроить какую-то бузу в лагере. Кажется, он слегка съехал головой на трудах основоположников марксизма ленинизма."

    "Не смогла слушать больше, вышла из укрытия и сказа ему все, что думаю по поводу его идей."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_173.mp3"

    scene cg al_gan_fight with dissolve

    "Его прихвостень, Долговязый, что-то тявкнул по поводу моей прически (и сразу получил в печень)."

    "Теперь обзывается только издалека. Как только я к нему, сразу убегает со всех ног. Трусливое ничтожество."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"

    scene cg ul_grass with dissolve

    "А вот еще. То, что было до дневников. Приехала новенькая  девочка, Ульяна. Совсем малышка. Её определили в наш отряд. Теперь она моя подшефная."

    pause (100000000000000000000.0)


    "Ей лет двенадцать. Нас познакомила ОД. Будет жить в моем домике. Очень сообразительная. Ужасная непоседа, я таких люблю."

    "Но идейная — ужас. Любит Ленина и может говорить о нем бесконечно. Не удивлюсь, если выясниться, что она изучила все труды вождя. Сколько там томов, уже не помню."

    "В отличие от тоже идейного Лысого, она хочет счастья всем, а не себе лично. Это я уважаю. Хотя идейно мы расходимся. Не верю я в коммунистическое общежитие для умных и дураков в одном флаконе."


    scene cg ul_poster with dissolve

    "Можно хоть сейчас фотографировать её на плакат для иллюстрации нашего светлого будущего. Из таких, наверное, и были первые революционеры."


    scene cg ul_grass with dissolve
 
    "С её приездом стало весело. А то я уже подумывала убраться отсюда пораньше."


    scene bg burleyka2 with dissolve

    "Речка и горы конечно хорошо, но ходить строем и слушать всякую ахинею от вожатых и директрисы, это невыносимо."


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"

    scene bg stadium with dissolve

    show sp_fi_004:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2

    "Физрук, Тарас Юрьевич (Т.Ю. — как его тут за глаза называют пионеры, они всем дали сокращённые имена) вообще тупой как пробка. Боже, как же он меня раздражает."

 
    scene cg al_stadium_yp with dissolve

    "Стоило мне надеть спортивную форму, как он стал пялиться на мои ноги."

    pause (100000000000000000000.0)

    "Да, ноги у меня — что надо, только не про него. Вот чёрт озабоченный. Может, это издержки от чрезмерных занятий спортом? Тестостерон там всякий."

    "Я слышала, спортсменам от этого таблетки дают. Надо сказать Виоле Церновне, пусть пропишет ему пилюль от «хотелок». Заодно «антиглупин», хотя это, наверное, не лечится."


    scene cg ul_portr with dissolve

    "{b}Запись 3{/b} \nМы всё больше сближаемся с Ульяной. Вообще она классная. Думает мои мысли. Мы во всём похожи. Не говоря уже что обе золотоволосые (мы не рыжие!)"

    "Вчера мыла ей голову. Без косичек она выглядит старше. Наверное в будущем станет настоящей красавицей. Она уже сейчас очень мила. Надо научить её каким-нибудь приёмам от мальчишек. Мы же теперь команда."


    scene bg camp_artifacts with dissolve

    show sp_od_024:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.0


    show sp_may_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Из лагерного начальства я выделила бы Ольгу Дмитриевну и завхоза Маю. Они классные тетки."


    scene bg camp_artifacts with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1


    "Еще Петровича, сторожа. Он добрый, хоть и напускает на себя суровость."


    scene bg camp_artifacts with dissolve

    show sp_ln_002:
        yalign 0.1 subpixel True
        xalign 0.47 subpixel True
        zoom 1.1

    "Наша повар Любаня тоже добрая. Любаней мы зовём её между собой, но на людях называем её уважительно — Любовь Никаноровна."

    "Она просто прелесть. Всегда кладет мне лишнюю порцию. Говорит, я напоминаю ей её племянницу, которую она (она бездетная) очень любит."


    stop music fadeout 0.5

    queue music "audio/music/z_152.mp3"

    scene bg auhouse_crop1 with dissolve
    
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Ульяна куда-то ходила вчера ночью. Я ее искала. Слава богу, обошлось."


    scene cg uv_branch with dissolve

    "Несёт какую-то околесицу про развалины, в которых живет кошка величиной с человека, которая как белка лазает по деревьям."

    "В общем, фантазерка. Она — как я в детстве. Тоже любила фантазировать. Но люди-коты... Этого даже я не придумала бы."


    scene cg ul_martian_diary with dissolve
 
    "Или вот, недавно играли с ней в космонавтов, понаделали из коробок скафандров и прыгали, изображая невесомость. Потом дрались подушками."

    "Одна кровать не выдержала и развалилась. Хлипкие у них тут лежанки."

    "Приходил Петрович (он в лагере  за столяра), сказал: «Сколько тут работаю, кровати не ломались, а за вами двоими — только успевай чинить»."

    "Это он наверное про замок в кружке Умелые руки, что испортила Ульяна. Интересно, кто ему сказал. В общем, с ней не соскучишься."


    stop music fadeout 0.5

    queue music "audio/music/z_009.mp3"

    scene cg ul_sleeping_house with dissolve

    "Сейчас набегалась и спит. Нам всегда дают час после обеда, чтобы мы поспали. Говорят, это полезно детям. Называется «Тихий час». Но у нас он редко бывает тихим."


    scene bg abandbeach with dissolve

    "Обычно мы обследуем окрестности или бежим на дальний пляж. На него запрещено ходить, потому что там нет ограждения. Зато можно купаться когда хочешь. Никто нас не видит и мы жжём костер. Мечтаем."



    stop music fadeout 0.5

    queue music "audio/music/z_022.mp3"

    scene bg camp_artifacts with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2



    "{b}Запись 4{/b} \nХочу написать про одного парня из нашего отряда. Он самый взрослый из пионеров. По виду даже комсомолец."


    scene cg al_sem_wash with dissolve

    "Вечером, когда я пошла к умывальнику, он наблюдал за мной. Я поняла, что он пришел туда не случайно. Наверное, шёл за мной от самого нашего домика. Для конспирации держал в руках мыло и полотенце."

    "Это было глупо, потому что в домике вожатой, где он живет, есть умывальник и даже душ. Спалился."

    "Пока я мыла ноги он чуть глаза не сломал. Когда я закончила, он подошел. Пытался знакомиться."

    "Он симпатичный, мне он понравился еще в первый день приезда. Но вчера я навела о нем справки. Оказалось, что он клеит всех девочек нашего отряда подряд. Это его не красит."

    "Я ему сказала об этом. Прямо там. Он ответил, что я слишком прямолинейная, и ему это во мне нравится. Да, я такая. Надо сразу расставлять всё на места."

    "Ещё раньше я узнала, что его поселили с Ольгой Дмитриевной. Она явно выделяет его среди прочих мальчиков. Позволяет ему то, чего не позволяет другим. Никогда не наказывает. Даёт всякие задания."

    "Любимчик? Терпеть не могу отличников и любимчиков. Надо будет послать Ульянку за ним пошпионить. Надеюсь, он не сексот. Только соглядатаев нам в отряде не хватало."

    "Назад шли вместе. Он спросил, люблю ли я цветы, пригласил на поляну за лагерем, обещал показать какой-то красивый пляж и водопад."

    "Ну понятно, зачем. Я сказала, что возьму с собой Ульяну. Он смутился (не ожидал). Потом сказал: «Ну ладно, бери мелкую»."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"

    scene bg camp_artifacts with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "{b}Запись 5{/b} \nСемён продолжает за мной ухаживать. Пытался несколько раз заговорить со мной, оставшись наедине."

    "Но Мику проговорилась, что он приглашал на эту поляну её и Ленку тоже. Вот же кот мартовский. Не знал, что Мику страшная болтушка. Теперь слухи о нем подтвердились. Конспирация провалилась."


    scene cg al_sem_swim with dissolve

    "Я бы сказала, что он очень настойчив. На пляже сегодня, когда я плавала к бакену, он тоже приплыл туда."

    "Мы были там почти одни (ну не считая Ленки, она за ним хвостиком ходит). Он отбросил свою обычную дипломатию и разоткровенничался."

    "Сказал, что давно положил на меня глаз (Давно? Неделя прошла всего как мы тут!) Сказал, что я ему нравлюсь, но что он боится ко мне подойти, так как не хочет меня обидеть, как он выразился, «словом и делом»."

    "Ха! Попробовал бы он «делом», был бы не жилец. Но я ему этого не сказала. Просто выслушала молча."

    al "Вон, Леночка на берегу знаки подает, сучит ножками от нетерпения и машет ручками. Хочет, чтобы ты надул ей круг."

    "И я поплыла к берегу, давая понять, что разговор окончен."

    "Но он догнал, загородил мне дорогу и опять за своё. Я поднырнула и быстро поплыла. Это было неожиданно, и он отстал, так и не смог меня догнать. В общем, надоел."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_301.mp3"

    scene cg dinner_frog with dissolve

    "{b}Запись 6{/b} \nСегодня быт смешной случай в столовой. Ульяна подложила Ленке лягушку в тарелку. Вот умора. Шуму было много. Леночка ревела как белуга."

    "Но скорее не из-за лягушки, а потому что Семен принес мне лишнюю порцию котлет. Она ревнует ко мне, это видно сразу. Славя тоже повелась на него. Ну прямо герой любовник."
 
    pause (100000000000000000000.0)
 
 
    scene cg all_hands_behind with dissolve


    "Вечером пришел к нам в домик на чай и принес конфеты и пирожные. Я знаю, что Ульяна любит сладкое и разрешила ему остаться ненадолго (хотя мне очень не хотелось)."

    "За чаем он пытался расположить меня к себе и сказал странную вещь."

    "Оказывается, те таблетки что даёт нам Виолетта Церновна, имеют какой-то побочный эффект, о котором он обещал рассказать, «когда сможет мне доверять». Сказал, это будет наша тайна."

    "Дешевый трюк. В общем, на кривой козе решил подъехать. Насчет таблеток, может, и не врет. Это мы проверим."

    "В общем, всё было довольно безобидно, но когда он уходил, то не выдержал и полез целоваться. Получил две затрещины. Очень надеюсь,  что я не сломала ему его красивый нос."

    "С чего-то он решил, что со мной так можно. Парень, конечно, не должен быть мямлей. Но это уже хамство. Кажется, он окончательно упустил свой шанс."

    "Хорошо, что Ульяна не видела этого финала. Подумала бы чёрт-те что."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_002.mp3"

    scene cg stage_spect with dissolve


    "Второй раз он подошел на концерте, когда мы играли спектакль, зажал меня за кулисами, стал извиняться за реку и попытался обнять."

    pause (100000000000000000000.0)


    scene cg al_hands with dissolve

    "Я оттолкнула его и сказала:"

    al "Ты спятил, что ли?! Нам сейчас выходить на сцену, ты мне весь грим смажешь. Нос зажил уже? Могу повторить!"

    sem "Из твоих рук, не то что побои, даже яд принял бы"

    "Рассмешил. Что-что, а чувство юмора, у него есть."

    pause (100000000000000000000.0)


    scene cg stage_spect with dissolve


    "Спектакль прошёл с успехом. Начальство было в восторге. Кстати, выяснилось, что Семен хороший рассказчик. После спектакля смешно пародировал все роли и МП (директрису)."


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    sem "Это было гениально дети! Гениально!"

    "И мы хохотали. Как выяснилось, в Семене талантов, выражаясь словами нашего сторожа Петровича, «Как в Тузике блох»."

    "После спектакля хотел подойти ко мне, но мы с Улькой специально убежали пораньше."


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"

    scene cg al_sem_table with dissolve

    "Третий раз (и это все в один день!)"

    "В столовой в обед я специально села за отдельный столик. Не хотелось ни с кем разговаривать."

    "Так этот гусь взял и подсел ко мне со своей тарелкой и компотом. Сел напротив меня. Вот, думаю, черт. Я нарочно отвернулась."

    "И вроде всё нормально было, а потом он стал под столом трогать ногой мою ногу. Я задумалась, не сразу поняла."

    "Раньше я бы ему влепила ногой в коленку. Но в этот раз просто посмотрела и спокойно и так ему говорю:"

    al "Знаешь, когда первоклассник хочет обратить на себя внимание девочки, он дергает её за косички. Ты мне сейчас напоминаешь такого первоклассника. Сколько тебе лет, Сёма?"

    sem "Я перепробовал обычные методы. Без вариантов. Вот, сработало. Слушай. Пойдем после ужина на лавочку у раздевалки, есть разговор."

    "Я знала, что он хочет мне сказать и ответила:"

    al "Сёма, ты зря тратишь время."

    sem "Я всё равно буду тебя там ждать."

    "Но я так и не пошла."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"

    scene cg vano_cops with dissolve

    "{b}Запись 7{/b} \nСегодня была неприятная история с нашим заведующим столовой. Он оказался педофилом. Не хочу писать подробностей."

    "Вспомнила своего отчима. Не обломилось ему, но все равно он присел на пять лет. Мать со мной не разговаривает с тех пор. Мне она не поверила. Ему поверила. Это самое  неприятное."

    "Не хочу думать обо всём этом. Жалко Ульяну. Но всё обошлось. Наверное, у нас обеих есть ангел-хранитель."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_076.mp3"

    scene bg attic with dissolve

    "Вот ещё новая новость. Мы организовали нычку у нас в домике на чердаке."


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Там играли в карты всем отрядом, и я проиграла Семёну. Пришлось целоваться. Чёрт меня дернул играть на желания. Целуется он здорово, надо признать (ещё один талант). Но это не повод."


    stop music fadeout 0.5

    queue music "audio/music/z_111.mp3"

    scene cg_bikers with dissolve

    "{b}Запись 8{/b} \nСегодня в лагерь приехали мотоциклисты. Как-то договорились с МП, что будут у нас харчеваться."

    "У них палаточный городок за нашим лагерем. Они нас катали на своих «аппаратах»."

    pause (100000000000000000000.0)


    scene cg_jean with dissolve

    "Пока катались, я познакомилась с Жаном. Он француз. Выглядит потрясающе. Похож на какого-то актера (не могу вспомнить). Очень красивый. Весь в черной коже и с длинными волосами. В общем, фирмач."

    "Приехал с нашими мотоциклистами, у них там какое-то мотоциклетное шоу в Крыму. Решили потренироваться в окрестностях лагеря. Мотоциклисты все взрослые парни. Всем уже за двадцать."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_420.mp3"

    scene cg sl_al_bikers with dissolve

    "Было заметно, что они впечатлены нашими девушками. Ещё бы. У нас в отряде самые красивые девочки в лагере. Славя одна чего стоит. Поэтому нас катали больше всех."
 
    pause (100000000000000000000.0)
 
 
    scene cg sl_jean with dissolve
 
    "А было так. Сначала Жан ухаживал за Славей, потом увидел меня."

    pause (100000000000000000000.0)


    scene cg al_jean_bench with dissolve

    "В общем, кажется, я ему нравлюсь. Это очень заметно. Общается с тех пор только со мной и ни на кого не смотрит."

    pause (100000000000000000000.0)

 
    scene cg sl_crying_day2 with dissolve

    "К слову сказать, Славя давно сохнет по Семёну, но тот её игнорирует."

    "И я подумала тогда. Если бы Жан с ней подружился, то я была бы за них рада. Но Жан хочет общаться только со мной."

    pause (100000000000000000000.0)


    scene cg al_jean_bench with dissolve

    "Семён, между тем, весь извёлся. Три раза подходил к нам, когда мы с Жаном сидели, болтали. Искал предлога для разговора с Жаном. Но я предупредила Жана, чтобы он с ним не связывался."


    stop music fadeout 0.5

    queue music "audio/music/z_012.mp3"

    scene cg al_jean_beach with dissolve

    "В этот же день мы поехали с Жаном на реку, купались."

    "Он рассказывал о своей стане, Франции, о Париже, о себе, и какой у него дом."

    "Много шутил. Смешил меня весь вечер. И ещё, у него приятный акцент."

    "Я думаю, он порядочный человек. Несколько раз я даже споткнулась для виду, и он подхватывал меня под руку, чтобы я не упала, но тут же сразу отпускал. И ничего такого себе ни разу не позволил."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_002.mp3"

    scene cg sem_al_boat with dissolve

    "{b}Запись 9{/b} \nСегодня я попросила вожатого второго отряда, Васю, покатать меня по реке."

    "Я села в лодку и отвернулась, засмотревшись на журавля. Он красиво пролетал над станцией и улетел куда-то в сторону моря. А потом пролетел ещё клин журавлей."

    "Я не заметила, как наша лодка отошла от берега."


    stop music fadeout 0.5

    queue music "audio/music/z_004.mp3"

    "И когда повернулась, чтобы сказать Васе, что мы слишком быстро плывем, то увидела улыбающуюся физиономию Семена."

    "Он греб на середину реки и нас начало сносить к омуту. Я спросила:"

    al "Где Василий?"

    sem "Васю я отправил. У него есть девочки из его отряда, пусть их выгуливает."

    "И я поняла, что он просто выгнал Ваську из лодки и сел сам. Вася, конечно, ему не соперник. И молча проглотил обиду. А что он мог сделать, против этого амбала?"

    al "Греби быстро к берегу, идиот. Иначе я прыгну в воду и доплыву сама."

    "Он ответил, что поступил так из-за того, что я его игнорирую, а разговор важный, и мне от него не отвертеться."

    "Между тем, нас снесло к омуту и было очень далеко плыть назад, к тому же, я боюсь омута, там запросто можно попасть в водоворот."

    "Я разозлилась, но он направил лодку к берегу и сказал:"

    sem "Не вопрос, я тебя высажу, где скажешь. Только дай слово, что сначала выслушаешь меня."

    pause (100000000000000000000.0)


    stop music fadeout 0.5

    queue music "audio/music/z_152.mp3"

    scene bg coast4 with dissolve
  
    "Мы причалили выше омута, там где Петрович привязывал лодку (там есть небольшой пляж), но Семен взял меня за руку и пошел по тропе к ручью."


    scene bg fishing_dialogue1_evening with dissolve

    "Там было поваленное дерево он сел на него. Я поняла, что это надолго. Я разрешила ему сказать всё, что он хочет, но при условии, что он сразу отвезет меня назад."

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2


    sem "Садись. Тут так тихо, нам никто не помешает поговорить. Обещаю, что я не буду к тебе приставать, можешь даже сесть от меня подальше."


    scene cg al_sem_lighter with dissolve

    "Я показала, что не боюсь его, села рядом положила ему голову на плечо, и спросила:"












    pause (100000000000000000000.0)

    scene black

    jump day49_cont







