label day26:

    $ style.say_window = style.window

    $ days = 26

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_25_00 = True
    $ im_gal_25_01 = True
    $ im_gal_25_02 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene cg sleeping_alice with dissolve

    stop music fadeout 0.5

    queue music "audio/music/z_017.mp3"


    "Утром я проснулась, а Алиса еще спала. Я не стала ее сразу будить. Она же всю ночь была с Жаном и пришла только под утро, не выспалась."

    "Наверное, сидели на скамеечке, а может быть, ходили на реку. Я поправила на ней одеяло. Алиса чему то улыбалась во сне."

    "Она красивая. И во сне еще красивее... На месте Жана, я бы тоже наверное влюбилась."

    "Так я сидела и смотрела на Алису." 


    stop music fadeout 0.5

    queue music "audio/music/sleep_alisa.mp3"


    "Над лесом, дымкой голубой, витает дух совы \nС тобою вместе лагерь спит, цветные видит сны \nГоняя времени клубок, в нем путая витки \nЛесная кошка выпускает играя коготки"

    "Пока еще не встал рассвет и на реке туман \nПоспи уставший от забот, глазастый хулиган \nПридет к тебе на пятый день, оставив для любви \nНемного грусти. А пока, ты просто, просто спи"

    "Алиса, спи, мой нежный Алисенок \nПрямым и честным, сроду не везло \nВ глазах янтарных, отражается Совенок \nСквозь время, донося твое тепло"

    "Смешных косичек золото ласкает ветерок \nПускай никто не замечает этих стройных ног \nДля тех, кто не способен, сильно так любить \nНе стоит слез своих Алиса, лить"

    "Мы верим то, что Лето снова к нам вернется \nИ Бесконечно только то, о чем поется \nЧто будет летний дождь и новая гроза \nИ станут вновь, веселыми глаза"

    "Алиса, спи мой нежный Алисенок \nПрямым и честным, сроду не везло \nВ глазах янтарных, отражается Совенок \nСквозь время, донося твое тепло"


    pause (1000000000000000000.0)


    scene bg stock3 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Сегодня на складе обнаружили пропажу трех мешков сахара."

    "Тревогу забил Вано. Он послал Толика, которому доверял ключи от склада, за сахаром. Наказав не брать мешки из правого штабеля."

    "Толик вернулся с мешком сахара и доложил, что никакого правого штабеля нет, а есть только одиноко лежащие два мешка. Вано лично отправился проверять наличие сахара. По его подсчетам недоставало трех мешков."

    "Всё это я узнала от Толика. Да, мы перед походом в развалины слямзили немного сахару. Но не мешок, и уж тем более, не три… Было интересно, кто же ещё, кроме нас, наведывается на склад."

    "Юлина кандидатура отпала сразу. Во-первых, ей не нужно было столько. Во-вторых, она физически не унесла бы даже одного мешка. Мешки весили по пятьдесят килограммов. Сама Юля весила меньше."

    "Мы стали думать, на что же понадобилось столько сахару. Между тем, Вано доложил о пропаже Маргоше, а та вызвала милицию."


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_444.mp3"


    "В лагерь приехал УАЗик со следователем, двумя оперативниками и овчаркой. Это было смешно. Из-за трех мешков сахара? Тут что-то было нечисто. Что-то в лагере произошло."


    stop music fadeout 0.5

    queue music "audio/music/z_201.mp3"


    "Самое интересное, что следователь даже не обследовал склад. Зато он долго о чем-то беседовал с Виолой. А потом откозырял ей, как будто она сама была милиционером."

    "Между прочим, на погонах следователя было четыре звездочки. А это, как сказала Алиса, звание капитан милиции."

    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    "– Кому мог козырять капитан? – Спросила Алиса и сама же ответила, – Только майору и выше."

    hide sp_al_037

    "Итак, у нас есть пропавшие три мешка сахара, майор Виола и непонятно зачем приехавший следователь. Но вскоре всё разъяснилось. История с сахаром, как мы и думали, была не единственным происшествием."

    "Это мы узнали от Жени, которая подслушала разговор Виолы и следователя."


    scene cg vio_cop with dissolve

    "Двери библиотеки граничат с медпунктом и Женя может иногда видеть и слышать, что происходит в кабинете Виолы."

    "Нет, сахар и правда исчез, но это был не повод вызывать опергруппу. Дело было серьезнее. Из кабинета Виолы пропали медикаменты."

    "У нас с Алисой было две версии. Первая: что Виола хотела скрыть недостачу лекарств. Вторая: что их правда украли, но в знак протеста."


    scene cg smu_flyer with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_333.mp3"


    "Потому что Смутьянов давно грозился вывести администрацию на чистую воду."

    "Особенно досталось Виоле, которую в листовках он называл не иначе как «доктор смерть», утверждая, что она «опаивает народ опиумом», «впрыскивает дурман», а также «зомбирует при помощи таблеток», чтобы «разделять и властвовать»."

    "В общем, начальство взялось за нас не на шутку. Кража из медпункта была серьезным проступком. Ну и бонусом шли три мешка сахара."


    scene bg camp_artifacts with dissolve
 
 
    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Первое, что сделала следственная группа, это провела обыски по домикам. Особенно искали в домиках второго отряда. В домике Смутьянова даже вскрыли полы."


    scene cg diaries with dissolve

    "Затем Ольга Дмитриевна отобрала у всех дневники."

    "Как она нам сказала по секрету, не чтобы их читать, а чтобы следователи не прочитали. Она явно боялась, что мы как-то замешаны."

    "Чтобы мы ничего такого не подумали, она заперла все дневники в ящик стола, а единственный ключ отдала Славе. Это она сделала вовремя, так как после второго отряда принялись за нас."


    scene bg camp_artifacts with dissolve

    "Попутно выявились некоторые подробности. Например, в одном из домиков младших отрядов нашли самодельные карты. Очевидно, не только нам пришла в голову идея поиграть в картишки."

    "К нам на чердак, слава богу, не заглянули."


    scene cg ivden with dissolve

    "Нашли запрещенную литературу, а именно: книгу «Доктор Живаго» (самиздат) и «Один день Ивана Денисовича»."

    "Нашли в административном корпусе! Дело приняло нехороший оборот."


    scene cg mar_questioning with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Тогда Маргарита Павловна долго беседовала  с Васей в Красном уголке. "


    scene cg vas_questioning with dissolve

    "И как позже нам рассказал Семён, уговорила Васю взять вину на себя. Потом его допросили милиционеры и он «сознался». Сказал, что искренне поверил в листовки Смутьянова и бросил лекарства в реку."


    scene bg camp_artifacts with dissolve

    "Искали Смутьянова, но не нашли. Он прятался у сердобольной тети Любы."

    "Литературу изъяли и сняли Васю с должности пионервожатого. За недопонимание и по малости лет не арестовали."

    "Маргарита Павловна уговорила не раздувать дело до «политического», сказала, что это всего лишь ребенок и все такое."


    stop music fadeout 0.5

    queue music "audio/music/z_527.mp3"


    "Мы с Алисой, конечно же, пришли утешить Васю, и он по секрету рассказал нам, что эти книги брал у нашего завхоза, Майи."

    "Маргоша их, судя по всему, тоже читала. В общем, у нас в лагере оказался кружок диссидентов. Но всё обошлось. Васю поставили на учет и через пару дней отправили домой."


    scene cg vas_jen with dissolve

    "Он трогательно пришёл попрощаться с Женей. Спросил её адрес, но она не дала."

    "Всем было его жалко. Тогда Электроник обнял его и сказал: «Я буду тебе писать». И взял адрес. И тут всех как будто прорвало, все стали брать адрес у Васи. В общем, он уехал расстроенный, но счастливый."

    "А я спросила у Жени, почему она не дала адрес. Она ответила: «Чтобы не давать ложную надежду». Вот как."


    scene cg cop_dog with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1018.mp3"


    "Итогом расследования стала улика, найденная особо натасканной служебно-розыскной собакой, Бураном."
   
    "(Тут я нарисовала Бурана)"

    pause (10000000000000000000000.0)


    "Буран уверенно взял след и прошёл так около километра. Улика лежала в траве. Это был мешок из-под сахара. Нашли его по дороге в старый лагерь. Дальше следы терялись."

    "В общем, теперь мы имели кучу загадок и ни одной разгадки."


    scene cg squad_formation2 with dissolve

    "Дальше — больше."

    "ОД по заданию МП созвала совет отряда и сказала:"

    od "Я вам доверяю. Я знаю, это сделали не вы."
 
    "На совете было решено усилить охрану лагеря и склада."


    scene bg camp_artifacts with dissolve

    "Также было собрание в кабинете директрисы, на которое вызвали всех вожатых и воспитателей. Петровичу, как сторожу, был объявлен выговор. Смутьянова посадили в изолятор на два дня."


    scene bg square with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Наш отряд обязали дежурить по складу. Каждую ночь внутри должен был находиться кто-то из нас. А снаружи бдительно охранять Петрович. Славя составила график дежурства по складу."


    image an_26_01: # Анимация Славя склад сахар
        
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_12.webp" with Dissolve(0.5, alpha=True)
        pause 1.4
        "images/an/an26day/an_d26_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/an_d26_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.7

        repeat



    scene an_d26_01 with dissolve

    "На самом деле, она по секрету сказала нам, что будет там дежурить одна, сама. И что считает делом чести снять пятно недоверия с  тех пионеров, которые не имеют отношения к краже."


    scene cg diaries with dissolve

    "Вот, еще про дневники расскажу."

    "Мы с Алисой решили воспользоваться ситуацией с дневниками, пока их не вернули, и узнать, кто мог украсть сахар, по косвенным уликам. Кто-то что-то видел, кто-то что-то слышал и записал в дневник."

    "Но главная причина, конечно, была в нашем любопытстве. Слишком много тайн возникло в последнее время. А еще мы были уверенны, что Славя уснет и проворонит вора."


    scene an_26_01 with dissolve

    pause (10000000000000000000000.0)


    scene bg stock3 with dissolve

    "Поэтому решили наблюдать в окошко склада и параллельно установить собственное дежурство."

    "Тут заканчиваю про сахар писать. Но не могу не упомянуть версии."


    stop music fadeout 0.5


    queue music "audio/music/z_1017.mp3"


    scene an_d26_02_06 with dissolve

    "Альтернативную версию выдвинул Семён. Он заявил, что сахар крадет кто-то для того, чтобы делать спирт. Его высмеяли. Но этой ночью мне приснился дурацкий сон с этой версией."

    "Тут я нарисовала мой сон"



    image an_26_02: # Анимация сон Семён Юля сахар
        
        "images/an/an26day/dream_sugar/an_d26_02_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.7
        "images/an/an26day/dream_sugar/an_d26_02_37.webp" with Dissolve(0.5, alpha=True)
        pause 1.4
        "images/an/an26day/dream_sugar/an_d26_02_38.webp" with Dissolve(0.5, alpha=True)
        pause 1.8
        "images/an/an26day/dream_sugar/an_d26_02_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.7

        #repeat


    scene an_26_02 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1017.mp3"





    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day27

return 