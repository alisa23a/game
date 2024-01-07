label day14:

    $ days = 14

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music


    play music "audio/music/z_400.mp3"

    scene cg meeting_far with dissolve

    "За суетой с нашими с Алисой похождениями все как то забыли о том, что мы должны были устроить праздник в честь приезда Саманты. Но ОД напомнила нам об этом тем же вечером. Мы побежали готовиться."

    "Собственно, событий должно было быть аж три. Первое в честь приезда Саманты, второе в честь празднования Годовщины Лагеря и третье, заключительный прощальный концерт перед отъездом (до которого было еще время)."

    scene cg meeting with dissolve

    "Но приезд Саманты, как сказал бы Петрович, мы «профукали». Даже построения толком не получилось. Ее внезапное появление застало всех врасплох."

    "Поэтому решено было провести творческий вечер и все, что приготовлено, просто почитать со сцены."

    scene bg stage3 with dissolve

    "А у нас ничего приготовлено не было. Если малыши седьмого и восьмого отрядов хотя бы выучили стишки, то у нас, как сказал бы мой папа, «И бык не валялся»."

    show sp_mi_012:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve 

    "Выручила Мику. Она была заведующей музыкального кружка. И вот что она предложила. Она напишет песню, а мы ее разучим и споем хором. Так и сделали."

    hide sp_mi_012


    scene bg stage2 with dissolve

    "Песня получилась неплохая. Называлась «Наш Совенок». Но хор не сложился. Потому, что пели - «кто в лес, а кто по дрова». И как она не билась, ничего не выходило."


    scene bg stage4 with dissolve

    show sp_tol_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_at_001:
        yalign 0.0 subpixel True
        xalign 0.65 subpixel True
        zoom 1.2

    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 0.35 subpixel True
        zoom 1.2

    show sp_sem_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "У Толика вообще не было слуха, Атсуи забывала слова, Женя стеснялась, а Семен не пел, а издавал какие-то непотребные звуки."


    scene bg stage4 with dissolve

    show sp_od_001:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    show sp_sl_003:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Как сказала про него ОД, «Ржет как конь стоялый». А Славя засмеялась. Надо спросить у Слави, что такое «конь стоялый», все-таки она у нас селянка."


    scene bg stage4 with dissolve

    show sp_al_005:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    "Тогда, Алиса предложила сделать ВИА. Ну то есть вокально-инструментальный ансамбль. И спеть эту песню с эстрады."


    scene cg al_sl_guitar with dissolve

    "И конечно начались репетиции. Алиса со Славей полностью ушли в «процесс». Подбирали репертуар. Но надо было решить вопрос с организацией. На чем играть, где, когда."


    scene bg mus with dissolve

    "Ну вот, ВИА. Инструменты в музкружке были. И всем эта идея понравилась, особенно мальчикам, это освобождало их от необходимости петь, потому что ВИА был женским."


    stop music

    play music "audio/music/z_306.mp3"

    scene cg ul_drums with dissolve

    "Стали распределять, кто на чем будет играть. Я, конечно, сразу села за барабаны."


    scene cg miku_piano with dissolve

    "Мику, как самая грамотная музыкантша, взяла на себя клавишные и вокал."


    scene cg al_sl_guitar with dissolve

    "Славя с Алисой гитары и вокал."


    scene cg al_mi_guitar

    "Мику у нас вообще была «многостаночица». В перерывах между игрой на клавишных, она успевала ещё на ритм-гитаре помочь, там где Алиса выходила в соло импровизацию."


    scene cg mi_sem_stage

    "А фон держал Семен, он оказывается мог играть на бас-гитаре, его Мику научила." 


    scene cg mi_sem_training

    "(И где это они и когда репетировали, почему я не знаю?!)"





    pause (10000000000000000000000.0)


    scene black with fade

    stop music

    #jump day15

return   
  










