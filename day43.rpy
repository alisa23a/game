label day43:

    $ style.say_window = style.window

    $ days = 43


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (100000000000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/track5.mp3"


    show sp_mp_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25

    "После истории с неудавшимся «восстанием», организованным Смутьяновым, были сделаны, как выразилась МП, «оргвыводы»."

    "Директриса не смогла дозвониться на «Большую землю». Очевидно, провод замкнул. Поэтому станция в райцентре отключила его."

    hide sp_mp_004

    show sp_pe_003:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Петрович долго возился с проводом, много раз пытаясь подключить аппарат, но всё тщетно."

    hide sp_pe_003


    show sp_smu_003:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Смутьянова так и не нашли."

    hide sp_smu_003 with moveoutright


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса еще тогда сказала:"

    al "Зачем мы ищем это гуано? Как известно, ОНО не тонет. Ничего с ним не случилось. Сидит где-то в кустах, наблюдает и обдумывает очередную пакость."

    hide sp_al_056


    show sp_mp_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    "МП распорядилась устроить в лагере Большую Уборку. Чтобы устранить последствия «смуты», как она это назвала."

    "Заодно уборка должна была отвлечь пионеров от дурных мыслей, если таковые у них остались, и вернуть в строй."

    "Чтобы малыши не мешали уборке, младшие отряды отправили с их вожатыми в поход по Старой дороге."

    hide sp_mp_004


    scene cg meeting with dissolve

    "Руководить уборкой было поручено Ольге Дмитриевне."

    "Она раздала всем имевшийся на складе инвентарь. Метлы, краску для бордюров, тряпки, ведра. Предстояло подмести всю территорию лагеря и прибраться в домиках."

    "Ольга погрузилась в уборку со всем имевшимся у неё энтузиазмом. Наверное, ей это нужно было, чтобы собраться. Есть такие люди, им нужно что-то делать, чтобы не раскисать."

    "Честно говоря, мы тоже обрадовались, потому что все понимали, это необходимо. И дружно принялись за дело."


    scene bg camp_artifacts with dissolve

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Мне не нравилось подметать. Много пыли и вообще."

    "Я взяла тряпочку, ведро с мыльной водой и стала протирать все перила и ступеньки в домиках, на кухне, в медпункте. Закончив, я села, чтобы перевести дух."


    scene bg genda_looks_left with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я села возле памятника Генды. Отсюда был виден весь лагерь. Было любопытно, кто как убирается."


    scene bg camp_artifacts with dissolve

    show sp_sl_020:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Вот Славя, она махала метлой с каким-то ожесточением."

    hide sp_sl_020


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса как будто танцевала."

    hide sp_al_055


    show sp_je_017:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Женя подметала очень аккуратно, коротким движениями и каждые три минуты, сгребала всё в совочек."

    hide sp_je_017


    scene bg camp_artifacts with dissolve

    show sp_tol_009:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    show sp_shu_004:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Мальчишки подняли страшную пыль."


    scene bg camp_artifacts with dissolve

    show sp_at_021:
        yalign 0.1 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "А Атсуи сбегала к Петровичу за шлангом и поливала площадь."

    "Ей нравилась вода. Вся мокрая но довольная, она то и дело обливала визжащих «уборщиков» на площади. И надо сказать, скоро пыли не стало совсем. Атсуи сильно помогла нам со шлангом."

    hide sp_at_021


    "Эта водная «феерия», как её назвала Алиса, понравилась всем. Притащили еще два шланга и вскоре все обливались водой. Стояли невообразимые шум, визг и суета."


    show sp_pe_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Петрович, наблюдавший все это со своей лавочки, только довольно кряхтел и повторял: «Эх, молодежь... Ух, молодёжь!» Пока, наконец, «молодежь» не облила и его."

    "Он пригрозил им своей клюкой, но был очень доволен вниманием пионерок."

    hide sp_pe_001


    "Облитые водой, наши девчонки, в прилипших облегающих маечках и шортиках, выглядели довольно пикантно (это слово я заимствовала у Семена, надо запомнить)."

    "Сразу было видно, у кого развились, как сказал бы мой папа, «вторичные половые признаки»."

    "У меня они не развились, поэтому я не обливалась. Иначе сразу стало бы видно, что я похожа на мальчишку."


    scene cg genda_plate_05 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_023.mp3"


    "Грустно поразмышляв на эту тему, я принялась протирать на памятнике табличку «ГЕНДА НАШ ОСНОВАТЕЛЬ»."


    pause (10000000000000000000000000000.0)



    "И вдруг осознала, что не обращала внимания, что кроме слова «ГЕНДА», там есть еще надпись «НАШ ОСНОВАТЕЛЬ»."

    "Вот надо же! Интересно, чего это он тут основал? Никогда и никто не рассказывал о роли этого человека в становлении лагеря."

    "Все воспринимали его скульптуру, просто как украшение, не особо задумываясь, что и зачем."

    "Я ещё раз прошлась тряпочкой по серебристой табличке и она прямо засверкала. Внизу я увидела какие-то буквы очень мелким шрифтом. Я нагнулась, чтобы рассмотреть."

    "У меня очень хорошее зрение. Папа всегда просил меня прочитать что-нибудь на этикетках в магазине. И я поняла, что даже я не вижу этот шрифт."

    "Я сбегала в домик и взяла лупу Алисы."

    "Увеличенная в четыре раза, надпись гласила: «ОТКРЫВАТЬ ТОЛЬКО В СЛУЧАЕ АВАРИИ!»"

    "Это было странно."


    scene cg genda_plate_06 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_201.mp3"


    "Я нажала на верхний край таблички и она ушла в постамент, как бы повернувшись вокруг своей оси."


    pause (10000000000000000000000000000.0)


    "Памятник вздрогнул и стал поворачиваться. Я испугалась и вернула табличку на место, сильно стукнув ногой по её нижнему краю."


    scene cg genda_plate_05 with dissolve

    "Табличка приняла начальное положение. Памятник скрипнув, снова встал на место."

    "Я почувствовала, как мои руки и ноги покрылись мурашками, а волосы немного приподнялись. Так у меня иногда бывает от сильного страха."

    "Вот так дела! Надо было срочно рассказать обо всем Алисе."


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Алиса сначала не поверила. Слишком уж все было фантастично."

    al "Да мы сто раз смотрели эту табличку! Помнишь, еще искали, где проходит фиолетовая линия на карте под памятником."

    al "Нашли эту дверцу для садового инструмента в постаменте. Правда, открывать не стали. Но и так было видно в щелочку метлы и ведра. Сейчас ими делают уборку."

    hide sp_al_056


    show sp_ul_020:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Насупившись) \nНу что я, врать буду? Обидно, что ты не веришь."

    ul "Говорю же, она поворачивается. Там мелкий шрифт, оттого и не разглядели сразу. И еще пылью покрыто. А я стерла пыль. И вот она — НАДПИСЬ."

    hide sp_ul_020


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ну просто, табличка старая, наверное, она уже еле держится, ты задела, она и перекосилась. Господи... У страха глаза велики."

    hide sp_al_056


    scene bg genda4 with dissolve

    "Мы подошли к памятнику."

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Алиса внимательно разглядывала табличку. Попросила лупу."

    al "Да, действительно надпись есть. Сейчас нажму... Куда, ты говоришь, надо нажимать?"

    hide sp_al_056


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Стой! Не надо! Он только успокоился! Видишь, Генда смотрит теперь на наш домик? Он повернулся, как раньше, сейчас нажмешь, и опять начнется. Мало нам революций?"

    hide sp_ul_033


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Если я правильно поняла, то табличка лишь закрывает рычаг. Назовем его «стоп-кран». Так что, если рычаг не трогать, то все останется как было."

    al "Ну, отойди... Я попробую."


    scene cg genda_plate_06 with dissolve

    "Алиса решительно нажала на верхний край таблички, и она одним краем ушла в углубление. Стал виден находящийся внутри рычаг."


    scene bg genda4 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, все как ты и сказала. Пусть будет так. Теперь у нас есть возможность останавливать машину в случае необходимости."

    al "Но что-то подсказывает мне, что это экстренный вариант остановки и, скорее всего, рычаг сам вернется в прежнее положение."

    al "Надо посмотреть, на сколько хватит его автономности."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Чего-чего? Ну-ка, повтори, я запишу... Новое слово. \n(достает из кармашка блокнот и ручку)"

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(По слогам) \nАВ-ТО-НОМ-НОС-ТИ... Записала? Это значит, самостоятельности."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, спасибо."

    hide sp_ul_021


    scene cg genda_plate_05 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_017.mp3"


    "Мы вернули табличку на место."


    scene bg genda_looks_right with dissolve

    "Уборка подходила к концу. Вибрация больше не ощущалась. Генда стоял правильно. Мы дружно с облегчением выдохнули."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну вот... Вернемся к нашим планам."

    al "У нас еще три пункта. На карте фиолетовые линии идут к ШАХТАМ, в сторону МЕДПУНКТА, и куда-то за БОЛОТА, в сторону старой ЛАБОРАТОРИИ."

    al "С чего начнем?"


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_102.mp3"


    show sp_may_001:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3

    "Вдруг мы услышали голос Майи."
    
    may "Маргарита Павловна! Кончайте с уборкой! Связь дали!"

    hide sp_may_001


    show sp_mp_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.25
    with dissolve

    "Мы увидели как Маргарита Павловна, смешно качая бедрами, побежала в административку."

    hide sp_mp_009


    show sp_fi_015:
        yalign 0.15 subpixel True
        xalign 0.0 subpixel True
        zoom 1.3
    with dissolve

    "За ней метнулся физрук, на ходу рявкнув:"

    fi "Лопаты и метлы отдать Архипу Петровичу! Всем мыть руки и в столовую! Вожатым построить отряды согласно расписанию приема пищи! Первыми идут малыши!"

    hide sp_fi_015


    scene cg documents_black_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_176.mp3"


    "По документам, которые мы нашли в архиве получалось, что после взрыва всё оборудование и взрывчатку для горных работ спрятали в шахте."

    "Но на шахте висел замок. Да и двери туда давно не открывались. Возможно, правда, Петрович наведывался туда за динамитом, чтобы глушить потом рыбу."

    "Так что ключ, если и был, то только у него."


    scene bg watchmans_cabin_2 with dissolve

    "И мы выкрали связку ключей, когда Петровича не было в каптёрке."

    "Мы уже знали, какие ключи на его связке какие замки открывают, но там висел ещё один неизвестный нам ключ. Здоровенный. Вот он, наверное, и был от того огромного замка на дверях шахты."


    scene bg stels with dissolve

    "И мы смылись, сразу после обеда."


    scene bg mcity2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_132.mp3"


    "Дорогу мы знали, потому что проходили мимо поселка ещё когда шли в ПЕРВЫЙ ПОХОД на Пик Двачевской."

    "Правда, тогда мы не спустились к шахте. Ольга Дмитриевна очень торопилась. Но теперь всё было иначе. Мы пришли туда, когда ещё не было двух часов, и у нас была куча времени."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Слушай, Алиса, а что Петрович говорил про то, что там всё заминировано? Начнем открывать замок, а там как бабахнет!"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Может и заминировано, но точно не вход. Как бы дед ходил туда регулярно? Вот сама подумай. Он же и разминировал, наверное, сам. И небось написал «МИНЫ». Чтобы такие как мы, не лазали."

    hide sp_al_056


    scene bg mcity with dissolve

    "И мы отправились к ШАХТЕ. До Поселка горняков дошли довольно быстро. Вход в шахту находился  тут же."

    "Собственно поселок построили у входа в шахту. Время экономили. Поспал, покушал и сразу за работу. Какая еще дорога."


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    "Мы огляделись. Поселок, и без того не веселый,  сейчас выглядел просто зловеще. Я посмотрела на Алису. Было заметно, что ей тоже не по себе."


    scene bg bunker5 with dissolve

    "Над входом в шахту была еле различимая расплывшаяся от времени надпись. Видно было, что ее неоднократно замазывали и снова писали поверх краски."


    pause (10000000000000000000000.0)


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Смотри, правда, замок. И написано — «ВХОД ВОСПРЕЩЕН, ОСТАЛИСЬ НЕРАЗМИНИРОВАННЫЕ УЧАСТКИ!»"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну да, написано аккуратно."

    hide sp_al_056


    "Мы попробовали, подходит ли тот здоровый ключ к этому замку. Замок открылся так, как если бы был смазан буквально вчера."

    "Но с дверью пришлось повозиться. Она никак не хотела открываться. Наконец, Алиса притащила какую-то железяку, которую нашла в поселке, и использовала её как рычаг."


    stop music fadeout 0.5

    queue music "audio/music/z_044.mp3"


    "Дело пошло. Из тоннеля пахнуло сыростью."


    scene bg bunker10 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Опять рельсы, такие же, как в пещере, видишь?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет, эти шире. Тут, похоже, дело было поставлено с размахом."

    hide sp_ul_019


    "Мы включили фонарики и пошли вперед. Через десять минут мы уперлись во вторую дверь. Под неё уходили рельсы."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ты видишь хоть какие-то следы медной руды?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет, может, дальше. Но я в руде не разбираюсь."

    hide sp_ul_019


    "Через какое то время тоннель разошелся в двух направлениях. Направо уходили рельсы, а налево нет. Мы пошли по левому, с ровным полом."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Смотри, стенки забетонированные, гладкие. Никакая это не шахта. Скорее, бункер. Не удивлюсь, если выясниться, что меди тут никогда и не было."

    hide sp_al_056


    scene bg bunker2 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Через несколько метров путь нам преградила огромная дверь."

    "Алиса посветила на дверь. Скорее это была даже не дверь а огромный люк. На нем не было замка. Ниже, едва заметно, наискось, краской под трафарет было написано:"

    "«ПРОХОДА НЕТ! МИНЫ!»"


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Смотри  краска почти свежая. Думаю, это уже дело рук Петровича. Смотри, вон и трафаретка валяется. Торопился, набивал впопыхах."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И что теперь делать?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну не возвращаться же назад! Или ты струсила?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Если честно, то ДА… Я за тебя боюсь."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Тогда тянем жребий."

    "Алиса достала спички."

    al "Тянешь ты. Если короткая, возвращаемся. Если длинная, идём дальше. Согласна?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Согласна."

    hide sp_ul_019


    "Я вытянула длинную. Мы попробовали открыть люк. Он не поддавался."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Такие огромные люки не открывают руками. Должна быть кнопка."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Какая кнопка? Тут и электричества-то нет. Она же автоматическая."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Много ты понимаешь. Если там пружина, то достаточно нажать где-нибудь, и засов сработает на открытие. Как в сейфах. Я в фильмах видела."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну вот же слева пульт какой-то. Правда, он, наверное, не рабочий давно."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ну-ка, дай посмотрю. \n(жмет на все кнопки)"

    hide sp_al_056


    "Неожиданно по периметру люка зажглись огоньки, а над головой — два плафона. Раздался рокот и гул."


    scene bg bunker13 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_045.mp3" noloop



    "Люк медленно и плавно открылся. Он был толстенный."


    stop music fadeout 0.5

    queue music "audio/music/z_177.mp3"


    "Хорошо что мы успели отскочить в сторону."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Махина..."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Наверное, на случай бомбардировки делали. Странно. Значит электричество все-таки есть. Где же источник? Тут же с войны, наверное, все заброшено."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Петрович — мастер на все руки. Помнишь, как он с лебедкой управился? Починил. Только что ему тут было надо?"

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Да, судя по рокоту снизу, мы запустили генератор. Он сейчас работает."


    scene bg bunker3 with dissolve

    "Мы прошли проем и углубились в длинный коридор, закончившийся тупиком. В полу мы увидели квадратный люк и лестницу, опускавшуюся вертикально вниз. "

    "Перед нами опять встал вопрос, спускаться или вернуться назад. В этот раз мы подбросили монетку. Выпало, идти до конца. Меня это УСТРАИВАЛО. Похоже, Алису тоже."


    scene bg bunker7 with dissolve

    "Пройдя немного, мы уперлись еще в одну дверь. На ней был какой-то знак."

 
    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"
 
 
    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Знак радиоактивности."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Может, не пойдем? А то будем радиоактивные. Папа говорил, что это вредно."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "(Бурчит) \nДверей понатыкали, как собак не резаных..."

    al "Оно, конечно вредно... Но на знаке тоже краска свежая. Это Петрович глаза отводит. Как с «минами»."

    hide sp_al_056


    scene bg bunker12 with dissolve


    "С дверью тоже заминки не возникло, потому что прямо рядом на стене была кнопка. Эта дверь тоже открылась автоматически."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Фу-у-ух... Ну, слава Богу, сработало. А то я думала, тут куковать будем."

    hide sp_al_056


    "Коридор за дверью уперся в стену."


    scene bg bunker9 with dissolve

    "Вверх опять шла лестница."


    stop music fadeout 0.5

    queue music "audio/music/z_046.mp3"


    pause (10000000000000000000000.0)


    scene bg bunker8 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_171.mp3"


    "Поднявшись по ней, мы попали в какое-то захламленное помещение."

    "Под ногами то и дело хрустело стекло. Присмотревшись, мы заметили, что это остатки каких-то лабораторных склянок."

    "Там были пробирки и еще какие-то странные стеклянные шары и фарфоровые тигли."


    scene bg bunker4 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_417.mp3"


    "Мы прошли дальше и попали в довольно просторное помещение."

    "Под потолком, находились большие лампы, как в операционной. Все заливал тусклый, мягкий , зеленый, идущий откуда-то сверху, свет."

    "Когда наши глаза привыкли, мы стали различить детали и заметили, что в воздухе летают какие-то маленькие, светящиеся зеленым светом, шарики."

    "Они были как светлячки, только во много раз больше и шуршали в воздухе."

    "Шарики висели неподвижно, но каждый раз, когда мы начинали двигаться, они выстраивались в небольшую стайку и двигались за нами."

    "Алиса подняла руку, шарики тут-же отлетели в сторону и сгруппировались в небольшую зеленоватую тучку. Они как-будто общались между собой."


    stop music fadeout 0.5

    queue music "audio/music/z_1013.mp3"


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Аффигеть... Да они как живые!"

    hide sp_ul_021


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Пуганые. Смотри, реагируют на жесты. Они точно, разумны. Или что-то вроде того."

    al "Как эти твари тут очутились, чем питаются, и что это вообще такое? Никогда ничего подобного не видела."

    al "Кажется, они преследуют нас. Смотри, при каждом нашем движении они тоже перемещаются. Мне страшно."

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что тут страшного? Ну, подумаешь, светляки какие-то."

    ul "Хотя, смотри, все вокруг как будто залито какой-то зеленой жидкостью. Может, эти штуки — испарения этой жидкости?"

    ul "А что, если с ними попробовать пообщаться? Сейчас я дотронусь до одного."

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Стой! Ни в коем случае! Может, они состоят из чего-то едкого. Вроде кислоты."

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Разумная кислота? Не смеши. Ой, они снова начали двигаться. Сейчас я проверю, слышат ли они звук."

    ul "(Кричит) \nШАРИКИ, БРЫСЬ!"

    hide sp_ul_021

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Смотри! Они улетели в дальний конец комнаты. С ума сойти. Стой, я их сейчас смогу посчитать, наконец."

    al "Один, два, три... Их двадцать восемь. Если, конечно, где-то не прячется еще парочка."

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Шарики, КО МНЕ!"

    hide sp_ul_021


    stop music fadeout 0.5

    queue music "audio/music/z_1005.mp3" noloop


    show sp_al_058:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А-а-а! Не делай так! Они летят к нам!"

    hide sp_al_058


    stop music fadeout 0.5

    queue music "audio/music/z_131.mp3"


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Шарики, СТОЙТЕ!"

    ul "Вот видишь, они слушаются. Мои милые шарики."

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Твои милые? Ты очень беспечна, если не сказать, безрассудна. Эти штуковины нам не друзья."

    al "Но, что точно, так это то, что они понимают команды."

    al "Послушай, надо уходить. Уже поздно."

    al "Но нет, не то... Во первых, мне тут страшно, во вторых, мы не знаем, с чем мы столкнулись."

    al "Судя по всему, это лаборатория. Пусть и заброшенная. А эти, медузы, или шаровые молнии, не знаю, как их назвать. Э-э-э..."

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Светлячки!"

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Хорошо, пусть светлячки. Они явно разумны, и кажется, чего-то от нас хотят. В общем, мы потом это обсудим."

    al "Сейчас я от страха даже не могу говорить, не то что соображать. И кажется, я мокрая... Отступаем к двери. Вроде, они тебя слушаются. Скажи им замереть и валим!"

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да легко. Мои шарики меня слушаются."

    ul "ШАРИКИ, замрите!"

    ul "Если ты настаиваешь, пойдем. Но я бы одного поймала и забрала с собой."

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Сумасшедшая!"

    hide sp_al_057


    "Алиса потащила меня к выходу."


    scene bg bunker11 with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я поняла, как я их назову! Шуршавчики! Они же так мило шуршат. Ты слышала?"

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "К ЧЕРТУ! Ты ненормальная. Уходим!"

    hide sp_al_057


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Извини, но я вернусь. Я забыла там рюкзак."

    hide sp_ul_019


    scene bg bunker4 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_130.mp3"


    "Я выскользнула из рук Алисы и бросилась в лабораторию. Я вспомнила, что в соседнем помещении видела много стеклянных баночек с крышками. Я метнулась туда, схватила одну и решила сделать немыслимое."

    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Один шарик, быстро в баночку!"

    "Я вытянула руку с баночкой. Стая шариков понеслась ко мне. Наверное, все хотели попасть в неё. Но я быстро закрыла крышку, как только в неё влетел первый."

    ul "(Шепотом) \nВсё! За остальными приду потом. Сидите тут тихо."

    "Шарики какое-то время кружились вокруг, потом среагировав на команду «БРЫСЬ!» снова улетели в дальний конец комнаты."

    hide sp_ul_023


    scene bg bunker11 with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_202.mp3"


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Я выпрыгнула наружу, захлопнула дверь и прокричала сквозь неё:"

    ul "МЫ ЕЩЕ ВЕРНЕМСЯ, ШУРШАВЧИКИ! НЕ СКУЧАЙТЕ!"

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Я хотела уже бежать за тобой! Что ты так долго возилась?"

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Потом скажу. Бежим."

    hide sp_ul_021


    scene bg bunker with dissolve

    "Мы долго бежали по коридору, по лестницам, и кажется, немного заблудились, потому что я точно помню, что мы так долго раньше не шли. Это был какой-то совсем другой тоннель."


    scene bg bunker6 with dissolve

    "Наконец, мы уперлись в казалось бы знакомую дверь. Фух... Значит, показалось."

    "Но, когда мы вышли на поверхность, выяснилось, что это был совершенно другой выход."


    scene bg mcity2 with dissolve

    "Странно. Но рассуждать было некогда. Пробежав по склону и нагромождению валунов, поросших густым кустарником, мы нашли тропу и спустились по ней в поселок Горняков."


    scene an_d10_01_bg with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_011.mp3"



    show an_10_01

    "Ну вот, потом было много событий. Но, обо всем по порядку."

    "Начну с костра."

    scene cg campfire_aka_day with dissolve

    "Когда мы вернулись в лагерь, то узнали, что все наши пошли жечь костёр на то место, где в первые три дня мы сидели вместе. Оттуда видно Рачью отмель."

    "Мы пошли к ним. Там все галдели о том, что сходили бы еще раз в поход, но все плановые походы для старших групп закончились."

    "Только малышей еще водили в ближние маршруты. Но мы там все исследовали и они нам были уже неинтересны."

    "Потом начались, как всегда у костров, всякие истории. Решили, что каждый расскажет интересную историю из своей жизни."


    scene bg aulane with fade


    show sp_shu_002:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_el_002:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    "Последними были Шурик с Электроником. Они опоздали к началу вечеринки, но были очень возбуждены."

    "Они закричали: «Вот мы вам сейчас расскажем историю!»"


    scene cg all_campfire_evening with dissolve


    stop music fadeout 0.5

    queue music "audio/music/z_1016.mp3"


    "Мы придвинулись поближе, чтобы не пропустить ни слова. И действительно, история оказалась удивительной. Чем-то похожей на сказку о Буратино."

    "Тем более, что, как утверждали оба, она произошла только что, буквально час назад, когда они собирали робота."


    scene cg shu_el_robot with dissolve

    "Ну вот... Не успели кибернетики закончить своего робота, потому что ничего у них не получалось. Каких-то там деталей не хватало, чтобы кукла заработала."

    "Ну и руки не сделали ей, потому что нужных пружинок не нашли, а как сказал Электроник, «гидравлику мы бы не потянули»."

    "В общем, механическую решили делать, что-то вроде часов в театре Образцова. А вместо кукушки она говорила бы всякие слова."

    "И только они собрались на обед, как вдруг, кукла задвигала головой и руками."

    "(Тут я нарисовала, как я это себе представляю)."


    image an_43_01: # Анимация кибирнетики робот

        "images/an/an43day/an_d43_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_23.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_24.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_25.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_26.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_27.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_28.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_29.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_30.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_31.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_32.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_34.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_33.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_36.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_35.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_37.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_39.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_38.webp" with Dissolve(0.5, alpha=True)
        pause 0.5


    show an_43_01


    pause (10000000000000000000000.0)


    scene cg all_campfire_evening with dissolve

    "А потом она им стала глазки делать. Ой, умора. Ну и фантазеры."

    "Алиса смеялась и сказала, что кибернетики переплюнули по части выдумки даже меня. Все развеселились. Байка получилась веселая. Прямо научная."

    "Не знала, что у изобретателей такое хорошее чувство юмора. Я думала они зануды и сухари."


    scene bg aulane with fade


    show sp_shu_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    show sp_el_003:
        yalign 0.05 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2


    "Вот только кибернетики с нами не веселились, а так обиделись, что ушли."

    hide sp_shu_001 with moveoutright

    hide sp_el_003 with moveoutright


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Чего это с ними, мы же по дружески."


    scene cg all_campfire_evening with dissolve

    "В общем, вечер получился очень интересный. Я назвала его «ВЕЧЕР УДИВИТЕЛЬНЫХ ИСТОРИЙ»."


    stop music fadeout 0.5

    queue music "audio/music/z_214.mp3"


    "Снова началась вибрация. Мы чувствовали ее даже у костра. Потом пошел сильный дождь. Прямо потоп. Все бросили костер и побежали в домики."


    image an_43_02: # Анимация гроза над «Совёнком»

        "images/an/an43day/an_d43_40.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_41.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_42.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_43.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_44.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_45.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_46.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_47.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_48.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_49.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_50.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_51.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_52.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_53.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an43day/an_d43_54.webp" with Dissolve(0.5, alpha=True)
        pause 0.5

        repeat

    show an_43_02

    pause (10000000000000000000000.0)


    scene an_d43_44 with dissolve

    "Дождём залило всю площадь, и мы бежали по щиколотку в воде. Все произошло внезапно. Огромные черные тучи появились как «черт из табакерки»."

    "Грохотал такой гром, что у меня чуть не лопнули барабанные перепонки."


    scene bg oldroad2 with dissolve

    "Вожатые 8-го, 7-го, 6-го и 5-го отрядов должны были сводить малышей по Старой дороге."


    scene bg cave with dissolve

    "Маршрут  включал в себя посещение пещеры."


    scene bg mcity2 with dissolve

    "Затем Поселка горняков."

    scene an_d43_44 with dissolve

    "В назначенное время ушедшие в поход группы не вернулись."

    "Дождь  становился сильнее. Предположительно отряды заблудились или пережидали дождь в пещере."

    "Появился один из вожатых и сообщил, что они не рискнули вести малышей по скользкому склону под дождём. Сейчас они в пещере с остальными вожатыми."

    "МП хотела отправить детям воду, еду и одеяла, чтобы они смогли продержаться ночь в пещере, но начался настоящий ураган, и дойти до пещеры, да ещё и с грузом, стало нереально."

    "Половина лагеря этой ночью не спала. Вся администрация уж точно."




    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day44

return