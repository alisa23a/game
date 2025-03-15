label day50:

    $ style.say_window = style.window

    $ days = 50

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_49_00 = True


    show screen current_day with fade


    #play music "audio/music/z_181.mp3"
    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene cg ul_grown_up with dissolve


    stop music fadeout 0.5

    play music "audio/music/z_1015.mp3"


    "А на следующий день за мной приехал дядя Жора. Он меня не узнал. Я думала сначала, что это потому, что я вся зареванная. Но потом вспомнила, что я уже взрослая. Он привез мне новые вещи от папы."


    pause (10000000000000000000000.0) 


    "Я зашла в раздевалку, надела их и долго смотрела на себя. И подумала, вот ты какая, Ульяна Владимировна. Суровая."

    "А может, это от того, что чёрная майка. Не знаю. Дядя Жора сказал, что новые джинсы идут к черной майке."

    "Но я свою красную, хоть и старенькую, ни за что не выброшу, возьму с собой. Хоть Семён её и порвал тогда, немного. Будет память о первом поцелуе..."

    "Я вышла в обновках. Дядя Жора смотрел долго через очки, а потом сказал: «Да ты невеста уже». Откуда ему знать, сколько мне сейчас лет. Это же НАША ТАЙНА!"


    scene cg way_home with dissolve

    "Он приехал на своей машине. Ну не на своей, а на той, на которой работал. Такой грузовичок."

    "Я попрощалась со всеми, и мы поехали домой."

    "В дороге я всё думала. Осталось еще очень много вопросов и неразрешенных загадок."

    "Что будет с Элей и Смутьяновым?"

    "Куда делась Виола? Найдет ли ее Семён, чтобы вернуться?"

    "Где бродит Тузик?"

    "Зачем Петровичу столько золота?"

    "Что станет с душами, заключенными в бункере, и правда ли Пионеру с Петровичем удалось уничтожить коллайдер?"

    "На этом я пока свой дневник закончу. Потом допишу. Дома."





    # pause (10000000000000000000000.0)

    # scene black with fade

    #stop music

    jump finalcredits2





###############################################################

###################################### ending credit screen

transform credits_scroll(speed):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 600
    linear speed ypos -86000

screen credits():

    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"


    timer 105.0 action Return() #46.5 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(1500.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            xsize 1000
            null height 450

            text "Дневник Ульяны":
                font "fonts/mateur-webfont.ttf"
                color "#fff"
                size 80
                xalign 0.5

            null height 75

            text "Визуальная новелла":
                color "#fff"
                size 50
                xalign 0.5

            null height 75

            text "По мотивам визуальной новеллы «Бесконечное Лето»":
                color "#fff"
                size 30
                xalign 0.5

            null height 150

            text "Создатели игры выражают благодарность всем, кто тем или иным образом были причастны к её созданию. Авторам идей, сюжетов, стихов, музыки, песен, сценариев, монтажа, рисунков, и особенно редактору.":
                xalign 0.5

            null height 150

            text "Также мы благодарим всех поклонников визуальной новеллы «Дневник Ульяны». Тех, кто на протяжении двух лет оставался с нами, поддерживая в нас волю и желание довести проект до его полного завершения.":
                xalign 0.5

            null height 150

            text "Руководитель проекта:":
                bold True
                size 30
                xalign 0.5

            text "Феликс Ясневский":
                size 30
                xalign 0.5

            null height 75

            text "Сценарий:":
                bold True
                size 30
                xalign 0.5
     
            text "Саша Сад":
                size 30
                xalign 0.5

            null height 75

            text "Кодинг:":
                bold True
                size 30
                xalign 0.5

            text "Алексей Урклин, Алиса Фамина":
                size 30
                xalign 0.5

            null height 75

            text "Графика:":
                bold True
                size 30
                xalign 0.5

            text "Саша Сад, Сергей Иванов, Алиса Фамина":
                size 30
                xalign 0.5

            text "(При создании некоторых изображений использовались ИИ-инструменты)":
                size 20
                xalign 0.5

            null height 75

            text "Анимация:":
                bold True
                size 30
                xalign 0.5

            text "Саша Сад":
                size 30
                xalign 0.5

            null height 75

            text "Редактор:":
                bold True
                size 30
                xalign 0.5

            text "Валентин Семёнов (Семён Зимний)":
                size 30
                xalign 0.5

            null height 75

            text "Подбор музыки:":
                bold True
                size 30
                xalign 0.5

            text "Саша Сад":
                size 30
                xalign 0.5

            null height 150


            text "В игре были использованы оригинальные песни":
                size 30
                xalign 0.5

            text "Феликса Ясневского":
                size 35
                xalign 0.5


            null height 30

            text "Цветок полевой\nЗнаменосец\nСиний чулок\nКукла\nЗвездная река\nДари любовь\nДари себя\nЖми на курок\nКогда хирург\nКотик\nЛюбовь и эпидемия\nМалышка\nНас повенчала ночь\nОранжевый рассвет \nОсенний автостоп\nПусть будет так\nРыжие \nУдивительный мир\nХудожница\nЯркая краска\nНе уходи\nМарш правильных пионеров\nСиняя дверь\nРыжее чудо\nСпи Алиса\nСквозь бирюзу твоих волос":
                size 30
                xalign 0.5


            null height 150

            text "Выражаем благодарность художникам, чьи работы были использованы при создании визуальной новеллы «Дневник Ульяны»:":
                bold True
                size 24.5
                xalign 0.5

            null height 75

            add "images/cg/cg_oth/cg credits.webp": # adding a picture in-between the text
                zoom 0.75
                xalign 0.5

            null height 75

            text "Сделано на Ren'Py":
                size 30
                xalign 0.5

            null height 75

            text "© 2024":
                size 30
                xalign 0.5

            null height 75

            text "Напишите свой отзыв об игре Дневник Ульяны в официальной группе ВКонтакте:":
                size 30
                xalign 0.5

            null height 75

            textbutton "https://vk.com/ulyanas_diary":
                xalign 0.5
                action OpenURL("https://vk.com/ulyanas_diary")


style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5


label finalcredits2:

    $ im_gal_50_00 = True
    $ im_gal_50_01 = True

    $ show_quick_menu = False

    $ renpy.block_rollback()

    scene cg way_home with dissolve

    show screen credits

    $ renpy.pause (3000.0, hard=True) # or however long it takes to scroll through in a reasonable speed
 
    hide screen credits 

    $ renpy.music.set_volume(0.00, delay=2.0, channel='miscSounds')
 
    scene cg way_home with dissolve

    $ renpy.pause(2.0, hard=True)

    #return


    #jump day50

return