label spec_nb_001:


    stop music fadeout 1.0


    play music "audio/music/z_055.mp3"


    image spec_nb_01_an_01: # Анимация тетрадь для особых мыслей
        


        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        #repeat


    scene spec_nb_01_an_01 with dissolve

    pause (10000000000000000000000.0)

    scene an_spec_nb_01_05 with dissolve

    "Ну вот я пишу в тетрадке для особых и разных  мыслей. Такое в дневник нельзя писать, вдруг кто прочтет."

    "Ну вот, дело было так."


    image spec_nb_01_an_02: # Анимация ТДОМ костёр Славя, Лена, Алиса


        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an_spec_nb/an_spec_nb_01/an_spec_nb_01_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat


    scene spec_nb_01_an_02 with dissolve


    pause (10000000000000000000000.0)


    scene an_spec_nb_01_01 with dissolve

    "Мы же жгли костер тогда в первые дни."

    "Ночью, ну когда еще пришли ребята к костру и Семен сыпанул в него покошенной травы, что бы лучше горело."

    "А это оказалась конопля, которую Петрович скосил, по приказу директрисы, но не успел убрать."

    "И мы сбежали от дыма на речку. А ребята отсели подальше, но остались. Говорят, трава прогорела и они еще долго играли на гитаре. Жалели что мы ушли."


    scene bg tdom_night_beach with dissolve

    "Дальше вот что было."


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Слушай, раз уж мы уходим от костра, давай хотя бы искупаемся. В лагерь не хочется. Представляешь, я никогда не купалась ночью!"

    hide sp_ul_012


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ага, мысль хорошая. А вдруг, в воде водятся какие-нибудь ночные сущности? И ам-ням-ням."

    al "Утром найдут следы на песочке и скажут: «Их схрумкали, но мы их не забудем». МИНУТА МОЛЧАНИЯ и БАРАБАННЫЙ БОЙ. И несут два галстука..."

    hide sp_al_005


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно! Линейку торжественную и клятву — отомстить!"

    hide sp_ul_014


    show sp_al_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Кому? Монстру?"

    hide sp_al_003


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не, всё гораздо проще. Скажут - СБЕЖАЛИ недостойные пионерки Ленина и Двачевская. Ну и посмертно нам выговор, лишение нас звания пионеров и вечный позор."

    al "Эх, Ольгу Дмитриевну жалко только. Влетит ей."

    hide sp_al_005


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вообще-то тут какие-то пескари, ну, может, форель или щука водятся. Петрович говорил, что еще раки. И что есть омут тут."

    hide sp_ul_012


    show sp_al_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Вот-вот. ГИГАНТСКИЙ РАК поднимется из глубин омута. \n(делает страшные глаза и руки клешни и приближается к Ульяне)"

    hide sp_al_003


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ааа, не надо! Я щекотки боюсь!"

    hide sp_ul_014


    show sp_al_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я ГОЛОДЕН! Я НЕ ЕЛ ТЫСЯЧУ ЛЕТ!"

    hide sp_al_003


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Сначала догони меня, РАК!"

    hide sp_ul_014


    "Я побежала к реке. Алиса побежала следом, обогнала меня и попробовала ногой воду."


    show sp_al_006:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Теплая!"

    hide sp_al_006


    scene cg tdom_night_swimming with dissolve

    ul "(быстро раздеваясь) \nО-о-о! Классно! К тому же, никого нет. Слушай, давай без купальников! А то, потом сушить. Не высохнет же за ночь."

    al "А давай!"

    "Мы побросали одежду на песок и побежали в воду."


    scene bg tdom_night_beach with dissolve

    al "Вода черная. Если бы не луна, то вообще, как будто в чернилах купаешься."

    ul "Ага, непривычно. Хочу нырнуть, но боюсь."

    al "Смотри, звезды в воде! Как красиво! Ныряем в звезды?"

    ul "Да-а!"

    "И мы нырнули."


    stop music fadeout 1.0


    play music "audio/music/z_131.mp3"



    scene cg tdom_night_swimming2 with dissolve

    "А когда вынырнули, услышали на берегу чьи-то крики и смех."

    al "Улька, ты слышала? Кто-то шарится по берегу, там, где наша одежда. Давай, скорее вылезай!"

    al "Черт!"


    scene cg tdom_night_swimming8 with dissolve


    al "(Кричит в темноту) \nА ну-ка, отойдите от одежды!"

    ul "А как мы выйдем голые? Вот сволочи! Это второй отряд, я узнала Долговязого. Вон, длинный такой, и с ним двое!"

    ul "А ну, положите одежду, придурки! Я всё Ольге Дмитриевне скажу! Я тебя узнала, Долговязый!"

    al "Лучше по хорошему верните! Вы меня знаете!"


    scene bg tdom_night_beach with dissolve


    show sp_gan_001:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    gan "А что ты нам сделаешь? Давай, выходи, рыжая! А мы на тебя посмотрим!"


    scene cg tdom_night_swimming3 with dissolve

    "Мальчишки дразня помахали нам нашей одеждой и попытались убежать, и тут на берегу появился пришедший на крики Семён."


    menu:
        "Семён поможет":
            jump sem_helps
        
        "Семён не поможет":
            jump sem_doesnt_help


label sem_helps:


    stop music fadeout 1.0


    play music "audio/music/z_125.mp3"


    al "Сёма, держи их!"

    ul "Держи!"


    scene cg tdom_night_swimming4 with dissolve

    "Семён догнал одного пионера, повалил и выкрутил ему руку. Остальные нерешительно выглядывали из кустов, и только кто-то крикнул: «Беги, Серега!»"

    sem "А вы ему помогите. Что, слабо?"

    gan "Ой, мне так больно!"

    sem "Скажи им, чтобы принесли одежду или я сломаю тебе руку. Ты же у них за главного."

    gan "Да, пацаны, отдайте им шмотки!"

    "Один из сообщников Договязого вышел из кустов и бросил одежду на песок рядом с Семёном. Семён отпустил Долговязого."


    scene bg tdom_night_beach with dissolve


    show sp_gan_003:
        yalign 0.15 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    gan "(Убегая и грозя кулаком) \nНу погоди, рыжая, и ты тоже, еще встретимся!"

    hide sp_gan_003


    stop music fadeout 1.0


    play music "audio/music/z_478.mp3"


    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2
    with dissolve

    sem "Девочки, вот одежда. Я в лагерь."


    scene cg tdom_night_swimming8 with dissolve

    al_ul "Спасибо! Сёма, ты... Ты просто классный!"


    scene cg tdom_night_swimming6 with dissolve

    ul "Как скрутил длинного, а ведь тот выше него."

    al "Как думаешь, ОН ушел?"

    ul "Не знаю. Ну и что с того? В конце концов, он нас выручил. Ладно, давай быстро, а то еще кто-нибудь придет!"


    scene bg tdom_night_beach with dissolve

    "Мы выбрались из воды и быстро оделись."


    show sp_al_004:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Задумчиво) \nДа... Возможно, я на его счет и ошибалась."

    al "А может, это он подослал Долговязого и компанию."

    al "Знаешь, есть такой метод. Типа «Вы будто хулиганы, понарошку, а я вас разгоню». Так мальчишки знакомятся с девочками. Ну типа, играют в героя."

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, это было бы коварство. Но я не думаю, что здесь этот вариант. Очень уж тот вырывался."

    ul "К тому же, Сёма ему, кажется, фингал поставил и руку серьезно вывихнул. Он хромал и за руку держался. Не, точно он в бешенстве был."

    ul "Да, как бы Сёму не подкараулили завтра. Я знаю эту компанию. Они не успокоятся."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ладно. Оделась? Гады, такой вечер обломали. Пойдем. Завтра посмотрим."

    al "Если что, мы им наваляем. Толика, Шурика с Электроником подключим."

    al "Видела, как они качаются каждое утро с гантелями? Толик вот с такой бицухой! Я проверяла, как камень бицепсы. Не то, что эти дрыщи."

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, они побоятся."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "В лазейку пойдем, а то на входе придется объясняться, чего это мы в таком виде."

    hide sp_al_005


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ага."

    hide sp_ul_012

    "И мы побежали в лагерь."

    jump spec_nb_002


label sem_doesnt_help:


    stop music fadeout 1.0


    play music "audio/music/z_125.mp3"


    al "Сёма, держи их!"

    ul "Держи!"


    stop music fadeout 1.0


    play music "audio/music/z_478.mp3"


    scene bg tdom_night_beach with dissolve

    show sp_sem_001:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    sem "(Усмехаясь) \nОни уже убежали. Сами виноваты. Не надо было оставлять одежду. Вы что совсем голые? Интересное кино!"

    sem "Ладно. Сейчас пойду в лагерь, может девчонки вам что-то из своей одежды дадут."

    sem "А то у меня тут есть полотенце большое, тебе, Алиса. А Ульяне могу дать свою рубашку. Ей как платье будет."


    scene cg tdom_night_swimming7 with dissolve

    al "(Подумав) \nХорошо. Оставь рубашку и полотенце на берегу. Сам иди. Не надо девчонкам ничего говорить."

    al "Я разберусь завтра с этими идиотами. Ульяна говорит, что знает одного. Второй отряд."


    scene bg tdom_night_beach with dissolve

    show sp_sem_012:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    "Семён снял рубашку и шорты."

    sem "Вот. Ульяне рубашку она ей до колена будет, тебе шорты и полотенце. Но вы мои должники, если что. С вас завтра костер с картошкой."

    sem "Зря вы от нас сбежали, мы еще у костра попели. Вас не хватало."


    scene cg tdom_night_swimming8 with dissolve

    al "Спасибо. Хорошо. Обещаем. Отойди, нам одеться надо."


    scene bg tdom_night_beach with dissolve

    show sp_sem_012:
        yalign 0.05 subpixel True
        xalign 0.5 subpixel True
        zoom 1.2

    sem "Пусть Ульяна даст честное пионерское слово. Я ей верю."


    scene cg tdom_night_swimming8 with dissolve

    ul "Честное пионерское!"


    scene cg al_ul_dressing with dissolve

    "Семён ушёл. Мы выбрались из воды и быстро оделись."   


    pause (10000000000000000000000.0)


    al "Я всё равно ему не верю. Ну фартануло парню. Сидел сейчас в кустах, наверное, и смотрел, как мы тут голые одевались."

    ul "Зря ты так. Хотя..."

    al "В лазейку пойдем, а то на входе придется объясняться, чего это мы в таком виде."

    ul "Ага."

    hide sp_ul_012

    "И мы побежали в лагерь."

    jump spec_nb_002




    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump spec_nb_002

return 
    