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

    "Взяли Толика. Вид у него был решительный и заговорщицкий. Он сопел и нёс рюкзак с завтраками."

    hide sp_tol_001


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Петрович уже ждал нас на лодочной станции."

    pe "(Ухмыляясь) \nА мальчик-то ваш, вижу, четвёртый десяток разменял."

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

    show sp_pe_010:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ты это, рыжая, бери руль круче к берегу. Как в прошлый раз."


    scene bg boat_stern with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "(Наваливаясь  на руль) \nНе учите учёную."


    stop music fadeout 1.0


    play music "audio/music/z_004.mp3"


    scene cg fishing_catfish_boat1 with dissolve


    "Мы проплыли ещё с полкилометра, пока течение не вынесло нас на затон. Вода тут была спокойная. Проплыв ещё немного, мы очутились почти на самой середине омута."

    "Я стала вглядываться в темную воду стремясь увидеть что-нибудь, похожее на сома. Петрович светил фонариком и немного подгребал одним веслом. Лодка медленно крутилась на месте."


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene bg boat_bow with dissolve

    show sp_pe_010:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "А ну, молодой-интересный. \n(толкает Толика)"

    pe "Надевай-ка маску и смотри, куда я свечу. Под воду голову, так не увидишь."


    scene cg fishing_catfish_boat2 with dissolve

    "Толик послушно надел маску и наклонившись с борта лодки, погрузил голову в воду."


    pause (10000000000000000000000.0)


    pe "Через трубку дыши... Что видишь?"

    "Петрович постучал пальцем по лысой голове Толика."

    pe "Не слышит он меня. Эй, кучерявый!"


    scene cg fishing_catfish_boat2 with dissolve

    tol "Там ничего нет. Водоросли и дно чистое. Только бревно лежит большое... Глубоко очень."


    stop music fadeout 1.0


    play music "audio/music/z_131.mp3"


    "Петрович подпрыгнул на месте и схватил Толика за плечо."

    pe "Где видел бревно?!"

    tol "(Показывает пальцем) \nТам вот. Здоровенное такое."


    scene cg fishing_catfish_boat1 with dissolve

    "Петрович налег на вёсла, потом затормозил. Лодка прошла по инерции и стала."


    scene bg boat_bow with dissolve

    show sp_pe_010:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ну, окунись ещё разик."


    scene cg fishing_catfish_boat2 with dissolve

    "Толик опять опустил голову в воду потом резко вынырнул."

    tol "Вот, прям тут, под нами! Огромное бревно!"

    "Петрович выматерился в кулак."

    pe "Не бревно это, дурында. СОМ!"


    stop music fadeout 1.0


    play music "audio/music/z_202.mp3"



    "Петрович быстро достал рюкзак, вытащил оттуда свёртки и разложил их."

    pe "Кучерявый, наблюдай пока. Если бревно твоё сдвинется с места, считай, упустили зверя."

    "Алиса помогала разматывать толстую леску, к которой Петрович прикрепил свёрток, а я возилась с приманкой. Крючок на этот раз был небольшой."

    ul "(Огорчённо) \nКрючок маловат."

    pe "Не нужен нам сегодня большой. Пусть только заглотит, а уж там пиротехника своё дело сделает."

    "Петрович привязал грузило. Проверил, все ли хорошо закреплено. Толик дышал сквозь трубку тяжело и громко, точь-в-точь как дышат киты в фильмах про природу."

    pe "Опускай!"

    "Алиса аккуратно стала опускать леску с привязанной приманкой и грузилами."

    ul "А тротил?"

    pe "Рано ещё. Поставим как потянет."

    "Леска уходила все глубже, но не ослабевала. Глубина была, судя по всему, огромная. Наконец, леска перестала пружинить и груз лег на дно."


    scene bg boat_bow with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "ДНО. Всё, сейчас заглатывать будет."


    stop music fadeout 1.0


    play music "audio/music/z_171.mp3"


    scene cg fishing_catfish_boat2 with dissolve

    "Прошло почти полчаса. Вся команда сидела в оцепенении, боясь шелохнуться. Слышно было только, как дышит через трубку кит-Толик. Петрович сидел нахохлившись."


    scene bg boat_stern with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Может, и не сом это был, а точно, бревно? Мало ли утонувших бревен в реке?"


    scene cg fishing_catfish_boat2 with dissolve

    tol "(Резко высунув голову из воды) \nБревно, кажись, сдвинулось в сторону лодки! Плывёт по дну прямо к нам. Вроде, на приманку идёт. Под нами уже, ага... Ага, вот он!"

    "Леска резко натянулась и стала быстро разматываться. Петрович ловко накинул её на уключину, а сам начал возиться со свертком. Лодку стремительно тянуло по воде, на середину омута."

    "Петрович сбросил леску с уключины и она, звонко тренькнув, стала уходить в воду, утаскивая за собой на глубину сверток."


    scene bg boat_bow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Все, надо поспешать. Минута у нас! Ставьте вёсла!"


    stop music fadeout 1.0


    play music "audio/music/z_202.mp3"


    scene cg fishing_catfish_boat2 with dissolve

    "Между тем, Толик продолжал следить за сомом через маску. Видно было, что он увлечён процессом не меньше других."

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

    "Вдруг из глубины раздался рокот и вода вспучившись, образовала горб, затем горку, и лодка заскользила по этой горке вниз."


    scene cg fishing_catfish_boat4 with dissolve



    $ renpy.music.set_volume(0.00, delay=1.0, channel='music')


    play miscSounds "audio/music/z_041.mp3" noloop


    pause (10000000000000000000000.0)


    stop miscSounds fadeout 1.0


    $ renpy.music.set_volume(1.00, delay=1.0, channel='music')


    "Наконец, огромный сноп воды со страшным шумом вырвался из глубины и ушёл вверх, отшвырнув лодку в сторону. Все повалились друг на друга."

    "Огромная масса воды, падала с неба, заливая и без того начерпавшуюся по самые борта лодку. Вёсла разметало."

    "Петрович лихорадочно вычерпывал воду шапкой. Он снял с ноги сапог и кинул его помогавшей ему ладошками Ульяне."

    pe "Давай сапогом, так будет сподручнее!"

    "А с неба всё падала и падала мелкая водяная пыль. Никто ничего не слышал, все оглохли. Только беззвучно шевелили губами, пытаясь что-то сказать друг другу."

    "По движению губ Алисы я поняла, что та спрашивает про Толика. Вычерпывая воду, я оглянулась. Толика в лодке не было."


    scene cg fishing_catfish_boat3 with dissolve

    "По глади омута расходились круги... Вода постепенно обретала свой первоначальный цвет."

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

    al "Так ведь он оглушенный!"


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

    pe "Вёсла потом соберем. Где малец-то?! Не разгляжу, рюкзак или человек?"


    stop music fadeout 1.0


    play music "audio/music/z_004.mp3"


    "Мы стали грести изо всех сил руками к месту, где из воды торчало что-то тёмное."

    pe "(Зацепив багром предмет) \nТак, ну-ка... Тяжелый... Нет. Это не рюкзак."


    stop music fadeout 1.0


    play music "audio/music/z_177.mp3"


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

    pe "Погоди хоронить! Раз плавает, значит воздух в лёгких есть! Ну-ка, втаскивай его в лодку!"

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


    stop music fadeout 1.0


    play music "audio/music/z_017.mp3"


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


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Жить будет!"


    scene bg boat_stern with dissolve

    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "Я смотрю, он плывёт. И тут, ка-а-ак жахнуло! Потом ничего не помню. Круги какие-то цветные в глазах..."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "На-ка, вот, хлебни."

    "Петрович протянул Толику флягу."


    scene bg boat_bow with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ой, а можно и мне водички!"


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Дура, там водка!"


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "(Обижено) \nЯ гадость не пью. Никакая не водка, а чистая настойка. Рецепт секретный. «Сохатовка» на травах. Мёртвого поднимет."


    scene bg boat_stern with dissolve

    show sp_tol_005:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    tol "А где сом?"

    scene bg boat_bow with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "О, точно, настойка животворящая!"


    scene bg boat_bow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Жахнуло хорошо. Я всё-таки вместо трех, на всякий случай, пять положил палочек тротила. Наверняка чтоб..."

    pe "Должен он, сердешный, всплыть... Не может не всплыть. Если он не глухой, вроде меня."


    scene cg fishing_catfish_boat1 with dissolve

    "Мы собрали плавающие в воде вёсла и всматривались в туман, покрывший омут."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Ну, вот теперь, полный порядок. Жаль, ваши завтраки утопли. Но я кое-что взял с собой."

    pe "У меня тут на моем корабле \n(Петрович постучал по борту лодки рукой)"

    pe "Все прикручено «по штормовому». Так что..."

    "Петрович достал из бардачка под сиденьем кулёк с едой."

    pe "Угощайтесь."


    scene bg boat_bow with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ой, котлетки!"


    scene bg boat_stern with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Класс... А я жрать хочу, прямо сил нет."


    scene bg boat_bow with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "(Глядя на уплетающего за обе щеки Толика) \nПереволновались потому что. Завсегда от волнения аппетит."


    scene cg fishing_catfish_boat1 with dissolve

    "Лодка скользила по поверхности уснувшего в тумане омута. Ничего больше не напоминало о только что разыгравшейся рукотворной стихии."

    "Вдруг, от неожиданного толчка, всех бросило вперёд."


    stop music fadeout 1.0


    play music "audio/music/z_202.mp3"


    scene bg boat_bow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Что за черт! Нету тут мели. Топляк наверное..."


    scene cg fishing_catfish_boat1 with dissolve

    "В тумане было видно что-то большое и чёрное, в которое с размаху врезалась лодка."


    scene bg boat_bow with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Перебегая на нос лодки) \nОй... Это же... Это же ОН! СОМЯРА НАШ!"

    hide sp_ul_021


    scene bg boat_bow with dissolve


    show sp_pe_008:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "(Хватая багор) \nА ну-ка в сторону, мелочь! На корму все... Щас, пока не утонул, надо его привязать. Если проснётся, нам хана."

    pe "Пока контуженый, надо его буксировать к берегу и выволакивать на сушу.  Времени мало. Как он ещё не очнулся. Наверное, сильно его шандарахнуло..."


    stop music fadeout 1.0


    play music "audio/music/z_018.mp3"


    scene cg fishing_catfish_boat1 with dissolve

    "Сома зацепили багром, багор привязали к корме. Все ликовали."

    "Ульяна перевязала голову Толика галстуком. Кровь больше не шла. Толик в красной повязке выглядел как заправский пират."

    "Гребли все. Трое на одном весле и Петрович, как самый опытный, на втором."


    scene bg boat_bow with dissolve

    show sp_pe_010:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Рыжая, давай на корму, на руль, а то мы шас точно заплывём не туда. Видишь, нас в камыши несет. К пирсу правь. На лодочную станцию. Там есть за что привязать."


    scene cg fishing_catfish_boat1 with dissolve

    "Алиса села за руль. Неожиданно лодку качнуло."


    stop music fadeout 1.0


    play music "audio/music/z_149.mp3"


    scene bg boat_bow with dissolve

    show sp_pe_009:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Просыпается. Греби сильнее!"


    scene cg fishing_catfish_boat1 with dissolve

    "До берега оставалось совсем немного. Сом стал проявлять признаки беспокойства."

    "С торчащим из хвоста багром, он пытался шевелить туловищем и передним и плавниками."

    "Огромные усы волочились, как змеи, и создавали жуткое зрелище. Какую-то не то рыбу, не то осьминога."

    pe "Давай!"

    "Петрович налёг на весло. Раздался треск. Повреждённое взрывом весло лопнуло и разлетелось в щепы. Но лодка уже ткнулась в песчаный берег затона."

    pe "Ну-ка, гаврики! Быстро на берег, привязывай багор!"


    scene bg boat_station2 with dissolve


    "Мы с Алисой побежали выполнять команду, прихватив с собой толстенную верёвку, привязанную к багру."


    scene bg boat_bow with dissolve

    show sp_pe_009:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Петрович стоял на носу лодки и изо всех сил колотил сома по голове целым веслом. Тот извивался и пучил маленькие глазки. Вода вокруг лодки окрасилась в бурый цвет."

    "Мы с Алисой привязали багор и быстро вернулись."


    scene bg boat_stern with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Дайте мне, Архип Петрович. Я ножом его. Надо в центр, между глазами... Я видела в одном фильме."


    scene bg boat_bow with dissolve

    show sp_pe_009:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "(Озверело вращая глазами) \nОтойди, дурёха! А то под весло попадёшь. Ножичек убери, он ему — как слону дробина. Тут бы лом!"


    scene bg boat_station2 with dissolve

    "Ещё утром я заприметила за пирсом противопожарный ящик и сейчас побежала к нему. Ящик был не заперт, и там, среди прочего, хранилась тяжёлая кирка. Я схватила её."

    "Кирка весила килограммов десять, не меньше, и я успела запыхаться, пока притащила её к пирсу."


    scene bg boat_stern with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Улька! Вот зараза! Ну все найдёт!"


    scene bg boat_bow with dissolve

    show sp_pe_009:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Вот это уже дело."


    scene bg boat_station2 with dissolve

    show sp_tol_012:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Неожиданно стоявший в растерянности Толик рванулся ко мне, выхватил у меня кирку и подбежав со стороны пирса к торчащей из воды голове сома всадил кирку по самую рукоять в черное тело рыбины."

    "Хрясь!"

    "Сом сильно дёрнулся и обмяк."

    hide sp_tol_012


    stop music fadeout 1.0


    play music "audio/music/z_1002.mp3"


    "Толик медленно сел на пирс, свесил ноги, посмотрел на дело своих рук, на торчащую из головы сома кирку и заплакал."

    "Петрович обессилено повалился на дно лодки. Мы тоже попадали рядом в изнеможении."


    scene bg boat_stern with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я подёргала Петровича за рукав."

    ul "Петрович, а что с ним?"


    scene bg boat_bow with dissolve

    show sp_pe_002:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Да вот... Тут ведь психология, понимаешь. На войне такое часто было. Первый раз живое убить страшно."

    pe "Ничего, отойдет. Охотник он будет — что надо... Если, конечно, стресс этот переживет. Стре-е-есс. Понимаешь."

    "Было видно, что Петровичу, любящему щеголять научными словами, нравилось слово «стресс»."


    stop music fadeout 1.0


    play music "audio/music/z_206.mp3"


    scene bg boat_station2 with dissolve

    "Из лагеря на пирс сбегались любопытные пионеры."

    pis "Чем это вы его? Вот Громадина! Афффигеть... Не, такое надо рассказать дома... Не поверят."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    "Расталкивая толпу детей сгрудившихся на пирсе, к нам пробиралась Ольга Дмитриевна."

    od "ОПЯТЬ ЛЕНИНА И ДВАЧЕВСКАЯ! Да сколько же можно! Что вы снова натворили!"

    od "И Вы, Архип Петрович, взрослый уже. Старый, можно сказать, человек, такое себе позволяете! Чем вы думали! Они же дети!"

    od "Кто зачинщик этого всего?! Ты, Двачевская?"

    hide sp_od_022


    stop music fadeout 1.0


    play music "audio/music/z_333.mp3"


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я выступила вперёд."

    ul "Я, Ольга Дмитриевна. Это я всех подговорила, а Архип Петрович нас спасал. И вообще, прибежал потом. Он не при чём."

    ul "Там СОМ. Он нас чуть не утащил. Мы купались. А вот Толик спас. Видите, он убил гадину!"

    hide sp_ul_019


    "Все загалдели."


    show sp_od_026:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    od "(Побледнев) \nКак, чуть не утащил? Ужас какой!"

    hide sp_od_026


    stop music fadeout 1.0


    play music "audio/music/z_155.mp3"


    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Появился физрук. Со знанием дела оглядев плавающую возле пирса тушу сома, он сказал:"

    fi "Так... Рыбу надо вытащить. Тут все должны помогать."

    fi "Я сейчас верёвки принесу со станции, обвяжем, и все отряды чтобы встали каждый у своей верёвки. Помните, как мы проводили соревнования по перетягиванию каната?"

    pis "ПОМНИМ!"

    fi "Вот. Какой отряд первый дотянет сома до станции, тот получит самый вкусный его кусочек!"

    hide sp_fi_015


    scene cg catfish_pulling with dissolve


    "Все дружно построились в цепочку по отрядам."

    "Вскоре общими усилиями огромное тело втащили на понтон станции."


    pause (10000000000000000000000000.0)


    scene bg boat_station2 with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    show sp_ln_002:
        yalign -0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.05

    "Физрук, вооружившись топором, вознамерился разделать сома на части. Рядом с ним уже суетилась Любовь  Никаноровна."


    stop music fadeout 1.0


    play music "audio/music/z_197.mp3"


    scene bg boat_station2 with dissolve

    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    od "Тарас Юрьевич, прекратите! Дайте, я хоть детей уведу. Не нужно им это видеть. Фу... Кровищи-то сколько."

    od "Пошли, дети! Так, все построились по отрядам и за мной! Первый отряд останется, поможет на кухне, остальные, ша-а-гом марш!"

    hide sp_od_022


    "Дети с неохотой, постоянно оглядываясь, двинулись в сторону лагеря. Какой-то мальчишка, отстав, спрятался в кустах, но тут же был мной обнаружен."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "А ну, брысь отсюда, недомерок! Сказано же — ТОЛЬКО ПЕРВЫЙ ОТРЯД!"

    hide sp_ul_019


    stop music fadeout 1.0


    play music "audio/music/z_058.mp3"


    "Вскоре на пристань прибыли трое репортеров Совёнка из редакции одноимённой стенной газеты. Разделку сома пришлось на время отложить."

    "Они сделали несколько фотографий Петровича, Алисы и моих на фоне сома. Толик фотографироваться отказался. Вскоре репортеры убежали."


    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    fi "С чего начнем?"

    hide sp_fi_015


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Потроха вынимай, заберу, Тузику скормлю. Остальное поруби на кухню, будет ребятишкам рыбный день."

    hide sp_pe_005

    "Так и сделали. Первый отряд отпустили, после того как они помогли отнести остатки сома на кухню."


    scene bg auhouse2 with dissolve

    "Все собрались в нашем с Алисой домике и обсуждали рыбалку."

    "Неожиданно появился пионер, рассыльный, из тех что приносили записки, сообщил, что нас с Алисой зовёт к себе сторож, и убежал."

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Странно. Может, у Петровича неприятности? Вроде, складно врали..."


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene bg watchmans_cabin with dissolve

    "На пороге сторожки мы застали Петровича, кормящего с рук Тузика."

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "А, рыбаки-пиротехники. Пришли, значит. А у меня тут для вас есть диковинка."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Петрович проводил нас внутрь, посадил за стол, а потом вытащил из кармана тряпицу, положил на стол и развернул."

    pe "Как думаете, что это?"


    scene cg engineer_badge_cufflinks with dissolve

    pause (10000000000000000000000.0)


    scene bg watchmans_cabin with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Не знаю... Похоже на значок какой-то. Только старый очень. Наверное, коллекционный. И вот это, я такие видела у отца. Кажется, запонки."

    hide sp_al_004


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Это классная штука. Мой папа собирал значки. За такой он Вам отсыпал бы, знаете сколько денег? Сразу видно, он старинный. Очень ценный, наверное."

    hide sp_ul_012


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Не угадали. Вот в одном вы правду говорите, знак это. Сейчас никто не знает такого. И я бы не знал, если бы такой сам раньше не видел."

    pe "А видел я его у нашего горного инженера. Это эмблема горного инженера, еще царская. Такие только они носили. И точно, запонки его. Но это не самое интересное ребятушки..."

    pe "А самое интересное, вот что. Принес я потроха сома, чтобы значит, Тузика угостить. Ну  понятно, сразу удалил желчь и все несъедобное. А вот печень и желудок очень собаки уважают."

    pe "Да и я печени оставил малость себе. Угощу вас, как Любаша приготовит. Хотя, вас сегодня, видно, накормят так, что на мой гостинец и смотреть не захотите..."

    pe "Так вот, разрезаю я желудок, чтобы почистить, а там вот это."


    scene bg watchmans_cabin with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Эмблема горного инженера?!"

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "С ума сойти. Это значит что... Сом его тавось?"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Вот! Тут, понимаешь, главная тайна будет. Сома-то ловят на лягушку, и на медведку он идет, и всяко на червя и рыбку мелкую, не брезгует."

    pe "Но если что крупнее взял, то потом будет ловиться и на это. Я же свинину  ему в прошлый раз на приманку, не просто так  приготовил, тухлую, потому как..."

    "Петрович многозначительно выдержал паузу."

    pe "Потому как, она с человечиной схожа. Слышали рассказы вожатых, что тут утаскивали детей? А вот. Вам не расскажут."

    pe "А не пускали вас вниз по реке купаться, потому что сами знают, что тут были случаи. Утаскивал наш сом пионеров-то."

    pe "А если сом раз человечины пробовал, то уж всегда потом будет. Вот почему я его поклялся извести. Людоед он! И зуб у меня на него вырос."


    scene bg watchmans_cabin with dissolve

    show sp_ul_050:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А почему вы нам, дедушка, сразу не сказали?"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "А потому, что вы бы испугались и мне помогать не стали. Тут психическая хитрость."


    scene bg watchmans_cabin with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Я вот что думаю... Говорят, сомы живут до сорока лет. А когда он инженера утащил, то уже большой был. Ему сейчас, наверное, по размеру и возрасту лет сорок и есть."

    al "Отнимаем сорок лет, получается 1926 год. Ну, рос он еще лет двадцать, потому как получается, что он уже большой был, когда утянул инженера."

    al "И получается, в начале пятидесятых примерно он сюда приезжал, инженер этот. Или, около того."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_003:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Петрович, потрясенный дедуктивными способностями Алисы, только ахал."

    pe "Ну, ты, девонька, и голова. Вот оно, молодое поколение! Я бы сроду не додумался от сома посчитать."

    pe "Я ведь как кумекал, что году в тридцать втором он вернулся. Ан нет, позже получается. После войны значит. Старый он был. Потому и не смог вырваться от сома."

    pe "Да...  Век живи, век учись."


    scene bg watchmans_cabin with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Алиса, ты прямо Шерлок Холмс!"

    hide sp_ul_012


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса покраснела."

    al "Скажешь тоже. Это же элементарно..."


    scene bg watchmans_cabin with dissolve

    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al_ul "(Обе в один голос) \nВАТСОН!"



    scene bg watchmans_cabin with dissolve

    show sp_ln_003:
        yalign 0.13 subpixel True
        xalign 0.45 subpixel True
        zoom 1.3

    "Дружное веселье прервала заглянувшая в сторожку Любовь Никаноровна."

    ln "Идите, я вам там печень пожарила. Она огромная. Отнесёте своим. Угостите. Там на весь отряд хватит."

    hide sp_ln_003


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А можно мы значок и запонки эти возьмём, Архип Петрович? Нам очень надо. Для истории лагеря. \n(соврала она и покраснела)"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "А на что оно мне? Конечно. Берите."


    stop music fadeout 1.0


    play music "audio/music/z_155.mp3"


    scene bg watchmans_cabin with dissolve
 
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Точно, бери Алиса. У нас же база вещественных доказательств должна быть. Мы же расследуем."


    $ inv_item_08 = True

    show got_badge


    pause (1000000000000000000000000000000.0)


    scene bg camp_artifacts with dissolve 

    "Мы забрали эмблему и запонки и вышли из сторожки."

    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я сома есть не буду. Он людей жрал."

    hide sp_al_001


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я тоже."






    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day36

return 