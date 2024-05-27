label day16:

    $ style.say_window = style.window

    $ days = 16


    show screen current_day with fade


    queue music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg watchmans_cabin with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_015.mp3"


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

    "С утра Петрович ушел на рыбалку и мы наконец, смогли пробраться к нему в сторожку."

    "Это было нетрудно, потому что дверца из душевой выходила на склад, а сторожка была пристройкой к нему и имела внутреннюю дверь. Её-то, Петрович никогда и не закрывал."

    scene bg showers2 with dissolve   

    "Мы оторвали шпингалеты в душевой и проникли в склад, а оттуда в сторожку."

    "План этот, мы готовили с вечера и заранее обследовали душевые. Душевые не запирались. Мы даже включили воду в душе, так, на всякий случай, для конспирации, и она громко падала на пол."

    "Мы сделали это, чтобы создать видимость того, что пошли мыться. В таких случаях, ОД требовала, чтобы душевую запирали изнутри. Чтобы мальчики не подглядывали. Чем мы и воспользовались."

    scene bg watchmans_cabin_2 with dissolve   

    "Теперь никто не мог нам помешать. На наше счастье, карта оказалась в незапертом ящике."

    "Возможно, память стала подводить старика и он не закрыл ящик, хотя ключ от ящика торчал прямо в замочке. Наверное, вечером Петрович изучал карту. А утром спешил на рыбалку и забыл запереть."


    scene cg petrovichs_map with dissolve 

    "Карта была довольно большой и подробной. Мы разложили ее на столе и открыли окно, чтобы в каморке стало светлее. Потом поставили треногу. Как сказала Алиса, снимали по науке."

    "Алиса настояла на том, чтобы мы сделали несколько снимков. Карта не умещалась в наш объектив полностью и мы снимали ее частями. В спешке мы даже не успели ничего на ней толком рассмотреть."

    "Нам надо было еще проявить пленку и напечатать фотографии карты."

    "Это тоже было проблемой, т.к. ключи от фотостудии были у Слави. Но мы договорились с ней, что воспользуемся ее реактивами и ванночкой."

    "Алиса, оказывается, умела проявлять и печатать и нам никого не пришлось просить. Иначе пришлось бы раскрыть тайну карты."


    scene bg watchmans_cabin_2 with dissolve

    "Когда мы закончили, то Алиса посмотрела на часы. Оказывается, мы провозились целых два часа."

    "С улицы уже доносился голос Петровича. Он уже вернулся, и на наше счастье, задержался у столовой, болтая с тетей Любой, которой всегда отдавал улов."

    "Но мы успели. Сунув карту в ящик, мы кинулись через потайную дверь, в душевую."
 

    scene cg al_ul_shower with dissolve
 
 
    stop music fadeout 0.5

    queue music "audio/music/z_043.mp3"
 

    "Потом, немного постояли в воде, чтобы выйти с мокрыми волосами."


    scene bg square_day with dissolve

    "Когда мы вышли во двор, все было тихо. Только мимо вели на спортивную площадку малышей из пятого отряда. Они закричали нам Салют! Мы им тоже отсалютовали по пионерски."


    scene bg fotoc with dissolve

    "Вечером, мы проявили пленку и отпечатали фото в Славиной лаборатории."

    show sp_sl_001:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with Dissolve(0.3)

    "Славя порывалась нам помогать. Но Алиса сказала, что фотографии не те, что можно кому-то показывать."

    hide sp_sl_001

    show sp_sl_003:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with Dissolve(0.3)

    "Славя понимающе захихикала и сказала: «Вот, значит, зачем вам был нужен фотоаппарат. Ну потом, как-нибудь покажете, что получилось?»"

    hide sp_sl_003

    "Мы, конечно, пообещали. И она отстала. Надеюсь, мы ей не подкинули случайно глупую идею."

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with Dissolve(0.3)
  
    "Алиса прямо так и сказала: «Вот дуреха. Надеюсь на ее благоразумие»."


    scene cg petrovichs_map with dissolve 


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "И вот карта… Тут я ее не буду прикладывать, подробную, потому что нельзя. Это секретная карта. Вдруг кто ни будь украдет мой дневник."

    "А что бы было красиво, я нарисую кусочек карты, без знаков и дорог, как иллюстрацию."

    "Дальше было вот что. Мы нашли на карте самолет. Петрович его аккуратно нарисовал карандашиком. Но вокруг одни болота и никакой тропинки к этому месту на карте не было."

    "То есть, была, но она обрывалась. Дальше он шел, наверное, по каким-то своим приметам."


    scene bg auhouse_crop2
    
    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Думаю, шел по кочкам. Болотные люди ходят по кочкам. У них еще шест такой с собой. Ну, чтобы щупать дно. И на случай, если провалятся, то шест выручит."


    scene bg auhouse_crop1
    
    show sp_ul_025:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ой, что-то мне страшно... Загибнем мы в тех болотах. Говорил же Петрович, что без него туда не пройти."


    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Подожди. А вот через болота идет какая-то дорога. Написано, узкоколейка."


    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Но ее еще до войны строили, а может при царе-батюшке. Она, поди, сгнила вся или в болото ушла."


    scene bg auhouse_crop2
    
    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Нет, не может быть. Если и ушла, то не совсем. Я знаю, например, что прежде чем дорогу строить, насыпали насыпь. Иначе, почва поезд не удержит."


    scene bg auhouse_crop1
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Думаешь, по насыпи дойти? Тут, правда, недалеко получается от дороги до самолета, если конечно Петрович правильно все нарисовал."


    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Да, тут недалеко. Хотя, часть пути придется все равно прыгать с кочки на кочку. Но вот, смотри, деревьев тут нет. Может, тут когда-то был запасной аэродром? И к нему пытался дотянуть лётчик, что бы сесть?"


    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Да, а что. Неплохая идея. Спрятать в болотах аэродром. И немцы ни в жизнь бы не догадались. Наверное, он был резервный."


    scene bg auhouse_crop2
   
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Дорога проходит от тоннеля. Если выйдем на дорогу в поселок, то она пересекает железку. И пойдем по ней. Но железка идет на мост, а узкоколейка от нее ответвляется и идет в болота. По карте вроде так."

    hide sp_al_005
   
    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Только не пойму, что это за сарайчик нарисован на карте рядом с узкоколейкой. Может, станция какая? Или склад? Что там?"


    scene bg auhouse_crop1
    
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Пока не доберемся, не узнаем. Но нас интересует не это. Нас интересует самолет. Хотя... Тоже интересно."


    scene bg auhouse_crop2
    
    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Ладно, сегодня уже не успеем. Завтра с утра пойдем. Надо Толика предупредить, что бы нас подстраховывал."


    scene bg auhouse_crop1
    
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Он будет проситься с нами."


    scene bg auhouse_crop2
    
    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    
    al "Нет. Не в этот раз."


    scene bg square_day with dissolve 


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    "И вот, значит, что было потом. Мы начали готовиться к походу и я побежала на склад, выпросить у Вано Артабековича «сухой паек»."

    "Этот паек предназначался для походов. Хранились пайки на складе заведующего столовой и выдавались только по распоряжению ОД. Но я знала, что если я попрошу, то Вано Артабекович не сможет мне отказать."

    "Он всегда мне все разрешал, если попрошу. Но я всего один раз просила. Это когда мы с Алисой вечером сильно хотели есть после купания в реке."

    show sp_sem_015:
        yalign 0.08 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2


    "И тут по дороге меня останавливает Семён. Я заметила, что он весь вымазался красками. Наверное, что-то рисовал."

    "Он хватает меня за руку, тянет с собой куда-то и просит, чтобы я ему позировала. Вот прямо как в фильмах о художниках."

    "И тут у меня сразу возникла мысль, что это новое приключение. Тем более, меня никто никогда не рисовал. Вот будет здорово, когда я привезу домой свой портрет и покажу папе."

    "Не всякую девочку рисуют. А тут такое. С другой стороны, надо было готовиться к походу. И я была в нерешительности. Он так умоляюще смотрел."

    "Но я не пошла. Потому что меня ждала Алиса."

    "И я вспомнила слова папы, когда он говорил:"

    "«Если наметила одно дело, никогда не отвлекайся. Делай сначала его, потом остальные. Иначе ничего из тебя в жизни не выйдет. Будешь как мама, с ученой степенью в библиотеке работать простым библиотекарем»."

    "Но я не планировала быть библиотекарем, поэтому сказала Сёмену, что через два дня я готова ему помочь, но сегодня не смогу. Он очень расстроился."


    image an_16_01: # Анимация Ульяна Вано столовая
        

        "images/an/an16day/an_d16_00.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an16day/an_d16_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


  
        repeat


    scene an_16_01 with dissolve

    "А я побежала на склад. В общем, паек я получила, даже два. А когда уходила, Вано  Артабекович сказал: «Приходи, сладкая, когда хочешь. Дядя Вано всегда тебе рад»."

    "И при этом он так смешно пучил глаза, поглаживал свое толстое брюхо, улыбался и причмокивал. Было смешно и я чуть не засмеялась. Жаль, Алиса не видела."

    "Я вспомнила, что говорили про него Петрович и ОД. Что он странный. Только никакой он оказался не странный, а просто смешной."


    #pause (10000000000000000000000.0)


    scene black with fade

    stop music fadeout 1.0

    jump day17

return  
