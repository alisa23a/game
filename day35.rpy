label day35:

    $ days = 35

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene bg boat_station2 with dissolve

    "Утром вся наша команда охотников на сома была в сборе."

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Взяли Толика. Вид у него был решительный и заговорщицкий. Он сопел и нес рюкзак с завтраками."

    hide sp_tol_001


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Петрович уже ждал нас на лодочной станции."

    pe "(Ухмыляясь) \nА мальчик-то ваш, вижу, четвертый десяток разменял."

    pe "Плавать-то умеешь?"

    hide sp_pe_005


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Толик кивнул."

    hide sp_tol_001


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Он что у вас, немой?"

    hide sp_pe_005
    

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Да нет, просто волнуется. Он первый раз в такой заварушке."


    scene cg fishing_catfish_boat1 with dissolve

    "Сев в лодку, она откинулась на скамеечку. Все разместились и Петрович неслышно оттолкнувшись веслом, вывел лодку на стремнину. Светало."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ты это, рыжая, бери руль круче к берегу. Как в прошлый раз."


    scene bg boat_stern with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "(Наваливаясь  на руль) \nНе учите ученую."


    scene cg fishing_catfish_boat1 with dissolve

    "Мы проплыли еще с полкилометра, пока течение не вынесло нас на затон. Вода тут была спокойная. Проплыв еще немного, мы очутились почти на самой середине омута."

    "Я стала вглядываться в темную воду стремясь увидеть что-нибудь, похожее на сома. Петрович светил фонариком и немного подгребал одним веслом. Лодка медленно крутилась на месте."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "А ну, молодой-интересный. \n(толкает Толика)"

    pe "Надевай-ка маску и смотри, куда я свечу. Под воду голову, так не увидишь."


    scene cg fishing_catfish_boat2 with dissolve

    "Толик послушно надел маску и наклонившись с борта лодки, погрузил голову в воду."

    pe "Через трубку дыши… Что видишь?"

    "Петрович постучал пальцем по лысой голове Толика."

    pe "Не слышит он меня. Эй, кучерявый!"


    scene cg fishing_catfish_boat2 with dissolve

    tol "Там ничего нет. Водоросли и дно чистое. Только бревно лежит большое... Глубоко очень."

    "Петрович подпрыгнул на месте и схватил Толика за плечо."

    pe "Где видел бревно?!"

    tol "(Показывает пальцем) \nТам вот. Здоровенное такое."


    scene cg fishing_catfish_boat1 with dissolve

    "Петрович налег на весла, потом затормозил. Лодка прошла по инерции и стала."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ну, окунись еще разик."


    scene cg fishing_catfish_boat2 with dissolve

    "Толик опять опустил голову в воду потом резко вынырнул."

    tol "Вот, прям тут, под нами! Огромное бревно!"

    "Петрович выматерился в кулак."

    pe "Не бревно это, дурында. СОМ!"

    "Петрович быстро достал рюкзак, вытащил оттуда свёртки и разложил их."

    pe "Кучерявый, наблюдай пока. Если бревно твоё сдвинется с места, считай, упустили зверя."

    "Алиса помогала разматывать толстую леску, к которой Петрович прикрепил сверток, а я возилась с приманкой. Крючок на этот раз был небольшой."

    ul "(Огорчённо) \nКрючок маловат."

    pe "Не нужен нам сегодня большой. Пусть только заглотит, а уж там пиротехника свое дело сделает."

    "Петрович привязал грузило. Проверил, все ли хорошо закреплено. Толик дышал сквозь трубку тяжело и громко, точь-в-точь как дышат киты в фильмах про природу."

    pe "Опускай!"

    "Алиса аккуратно стала опускать леску с привязанной приманкой и грузилами."

    ul "А тротил?"

    pe "Рано еще. Поставим как потянет."

    "Леска уходила все глубже, но не ослабевала. Глубина была, судя по всему, огромная. Наконец, леска перестала пружинить и груз лег на дно."


    scene bg boat_bow with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "ДНО. Всё, сейчас заглатывать будет."


    scene cg fishing_catfish_boat2 with dissolve

    "Прошло почти полчаса. Вся команда сидела в оцепенении, боясь шелохнуться. Слышно было только, как дышит через трубку кит-Толик. Петрович сидел нахохлившись."


    scene bg boat_stern with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Может, и не сом это был, а точно, бревно? Мало ли утонувших бревен в реке?"


    scene cg fishing_catfish_boat2 with dissolve

    tol "(резко высунув голову из воды) \nБревно, кажись, сдвинулось в сторону лодки! Плывет по дну прямо к нам. Вроде, на приманку идет. Под нами уже, ага... Ага, вот он!"

    "Леска резко натянулась и стала быстро разматываться. Петрович ловко накинул ее на уключину, а сам начал возиться со свертком. Лодку стремительно тянуло по воде, на середину омута."

    "Петрович сбросил леску с уключины и она, звонко тренькнув, стала уходить в воду, утаскивая за собой на глубину сверток."


    scene bg boat_bow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Все, надо поспешать. Минута у нас! Ставьте весла!"


    scene cg fishing_catfish_boat2 with dissolve

    "Между тем, Толик продолжал следить за сомом через маску. Видно было, что он увлечен процессом не меньше других."

    "Азарт охватил всех. Мы схватили лежащее на дне лодки весло, пытаясь приладить его к уключине, но в результате только мешали друг другу."

    "Петрович суетился и кричал на нас. Наконец, весло встало на место, но время было упущено..."


    scene bg boat_bow with dissolve

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ой, мама дорогая! Все, ложитесь-ка все быстро на дно! Голову руками закройте! Рот откройте! Упритесь ногами в борт! Крепче, щас жахнет!"


    scene cg fishing_catfish_boat2 with dissolve

    "Не слышал его слов только Толик... Он продолжал следить за сомом. В спешке, все про него забыли."


    scene cg fishing_catfish_boat4 with dissolve

    "Вдруг из глубины раздался рокот и вода вспучившись, образовала горб, затем горку, и лодка заскользила по этой горке вниз."

    "Наконец, огромный сноп воды со страшным шумом вырвался из глубины и ушел вверх, отшвырнув лодку в сторону. Все повалились друг на друга."

    "Огромная масса воды, падала с неба, заливая и без того начерпавшуюся по самые борта лодку. Весла разметало."

    "Петрович лихорадочно вычерпывал воду шапкой. Он снял с ноги сапог и кинул его помогавшей ему ладошками Ульяне."

    pe "Давай сапогом, так будет сподручнее!"

    "А с неба все падала и падала мелкая водяная пыль. Никто ничего не слышал, все оглохли. Только беззвучно шевелили губами, пытаясь что-то сказать друг другу."

    "По движению губ Алисы я поняла, что та спрашивает про Толика. Вычерпывая воду, я оглянулась. Толика в лодке не было."


    scene cg fishing_catfish_boat3 with dissolve

    "По глади омута расходились круги… вода постепенно обретала свой первоначальный цвет."

    "Лодка накренилась но осталась на плаву. Лихорадочные усилия Петровича и нашей команды вычерпывавших воду не прошли даром."


    scene bg boat_bow with dissolve

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Главное, нет течи. Фу-у-ух... Пронесло. А где кучерявый? Вот, вижу, панамка плавает."

    pe "Неужели выпал за борт? Ай, беда-то какая... Говорил, плавать умеет."


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Так вещь он оглушенный! "


    scene bg boat_bow with dissolve

    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ой, мамочки... Он утонул, наверное!"


    scene cg fishing_catfish_boat3 with dissolve

    pe "А ну-ка дайте мне багор. Что-то там плавает."


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Ульяна, греби руками! Помогай! Вон и весло плавает."


    scene cg fishing_catfish_boat3 with dissolve

    pe "Весла потом соберем. Где малец-то?! Не разгляжу, рюкзак или человек?"

    "Мы стали грести изо всех сил руками к месту, где из воды торчало что-то тёмное."

    pe "(Зацепив багром предмет) \nТак, ну-ка... Тяжелый... Нет. Это не рюкзак."


    scene bg boat_bow with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Сом наверное!"


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Это Толик! Не дышит!"


    scene cg fishing_catfish_boat3 with dissolve

    pe "Погоди хоронить! Раз плавает, значит воздух в легких есть! Ну-ка, втаскивай его в лодку!"

    "Мы втроём с трудом затащили в лодку тело."


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Надо расстегнуть воротник. И трубку изо рта вытащить. Он же ей поперхнулся. И маску снять."


    scene bg boat_bow with dissolve

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Хрипит сердешный... Значит, дышит. Контузило его малость. Говорил я, головы из воды вынимайте."

    pe "Эк его... Кровь в ушах. Как бы барабанные-то перепонки не лопнули. Плохо дело. Оглохнет малец. \n(помогает раздеть Толика)"


    scene bg boat_stern with dissolve

    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "(Открывая глаза) \nГде я?"


    scene bg boat_bow with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Живой! Толик живой!"


    scene bg boat_stern with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Слава богу!"


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Сколько пальцев я тебе показываю, малец?"


    scene bg boat_stern with dissolve

    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "Четыре."
















    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day36

return 