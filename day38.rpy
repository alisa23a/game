label day38:

    $ style.say_window = style.window

    $ days = 38

    $ adv_1 = False
    $ adv_3 = False
    $ adv_5 = False
    $ adv_7 = False
    $ adv_10 = False
    $ adv_12 = False
    $ adv_15 = True

    $ im_gal_37_00 = True
    $ im_gal_37_01 = True


    show screen current_day with fade


    play music "audio/music/z_300.mp3"


    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    scene bg oldcem6 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_197.mp3"


    "Нам не давала покоя история с магией и куклой. И мы с Алисой решили еще раз сходить на кладбище."

    "Кроме оплавленных свечей и пентаграммы, мы нашли и то, чего сначала не заметили. В золе костра мы обнаружили остатки рыжих волос, которые были аккуратно связаны в косичку."

    "Именно то, что они были в косичке, и сохранило их от полного сгорания."


    scene cg pentagram with dissolve

    "Алиса долго рассматривала пентаграмму, а потом наклонилась и соскребла белую краску, которой она была нарисована. Внимательно разглядывая её, она вдруг сказала:"


    scene bg oldcem6 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Это свинцовые белила. Такие используют художники. Много у нас в лагере художников?"

    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Нет. Лена хотела вести кружок ИЗО, но она не сделала объявления по группам, и к ней ходил только Семён. В основном же, она рисует сама."

    ul "Часто ходит на «пленэр», как она это называет, на реку. Или рисует лес и горы. Два раза Семён ей позировал."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Так, теперь давай сопоставим все имеющиеся у нас факты."


    scene cg woodoo_doll with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_130.mp3"


    "Кукла сшита профессионально, а шьет у нас только Лена."


    scene cg lena_painter with dissolve

    "Краски художественные и хранятся они только у Лены."


    scene cg oldcem_figure with dissolve

    "Издалека плохо было видно, но всё же это была молодая девушка, а не женщина. Скорее всего, подросток."


    scene cg grass_magic with dissolve

    "Лена брала у Жени книги по травам, колдовству и магии."


    scene cg woodoo_doll with dissolve

    "Кукла с рыжими волосами, это мы с тобой. Только у нас во всем лагере (ну кроме Васи) рыжие волосы."

    "Тебя она не ревнует к Семёну, остаюсь только я."


    scene bg oldcem6 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Значит, порчу наводили на меня. И наводила её Ленка. Мотивация была только у неё. Именно она и приходила ночью на кладбище!"

    al "Вот только где она взяла мои волосы?"

    al "Я вроде стриглась в первый день. Боже, я вспомнила! Меня же стригла Ленка!"


    hide sp_al_004


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Точно, это она! Больше некому!"

    hide sp_ul_013


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Вот и попалась наша Леночка. Можно обижаться на человека, но желать ему зла, болезней или смерти — это уже чересчур."

    hide sp_al_001


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Мы не ябеды. Надо дать человеку шанс исправится."

    hide sp_ul_013


    show sp_al_001:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Это понятно Но.. Представь, она тут волхвует на моё здоровье, вон сколько булавок воткнула в куклу, а мы ей шанс?"

    hide sp_al_001


    show sp_al_002:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Даже если она раскается, то я ее вряд ли прощу. Как мы потом вообще будем жить вместе после того, что произошло? Об этом ты подумала?"

    hide sp_al_002


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но ОД не скажем."

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Естественно."

    hide sp_al_004


    scene bg auhouse3 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_017.mp3"


    show sp_mi_016:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1


    "После обеда к нам зашла Мику. Она увлеченно рассказывала о своих малышах. Спросила, почему последние дни мы не приходим на её кружок."

    hide sp_mi_016


    show sp_mi_022:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    "Слово за слово, мы разговорились, и Мику вдруг расплакалась и призналась, что чувствует себя одиноко."

    "Что все мы как-то отдалились от неё. Занятия с детьми не могли заменить ей полноценного общения с нами."

    "Она сказала, что Славя с Леной все время куда-то уходят. Кибернетики вечно заняты своими делами в кружке умелые руки, или уплывают на остров и заняты баркасом."

    "Атсуи уходит с ними, а Саманта не особенно часто появляется в клубе."

    "Толик всё время занят с физруком и ОД и бегает по их поручениям. Семён охотнее проводит время в библиотеке, а ей неловко мешать им с Женей."

    "Остаемся только мы с Алисой, но у нас, как ей показалось, какие-то свои тайны, в которые мы её не посвящаем. В общем, выглядела она расстроено."


    scene bg auhouse2 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_201.mp3"



    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Поэтому, посовещавшись, шепотом, мы решили посвятить Мику в историю с магией вуду."

    "Мы рассказали ей о кладбище и о том что кто-то наводит порчу. Показали куклу. Но взяли с нее слово ничего никому не рассказывать."


    scene bg auhouse3 with dissolve

    show sp_mi_016:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "У Мику загорелись глаза. Она дала клятву молчать как рыба. Расстались мы с обнимашками. Она убежала окрыленная."


    scene bg camp_artifacts with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_130.mp3"


    "Через час о магии знал уже весь отряд. Мику проболталась. Вышло это, как она сама сказала, СЛУЧАЙНО."


    scene bg attic2 with dissolve

    "Все, кроме Лены и Толика, собрались на чердаке."

    "Начались споры о том, кто может таким заниматься. В общем, был большой переполох. Мы сто раз пожалели, что доверились самой большой болтушке в отряде."

    "Не знаю, кто выдвинул идею о том, что не присутствующая на нашем собрании Лена могла быть причастна к магии."

    "Очевидно, все решили, что раз она брала книги по магии в библиотеке, значит, это она."

    "Лену бурно защищала Славя. Но её голос одиноко тонул в охватившей всех жажде ПОКАРАТЬ ВЕДЬМУ. Это было похоже на массовый психоз."

    "Мы тоже пытались защитить Лену, но нас никто не слушал. Все галдели и спорили."

    "Наконец, поставили на голосование и постановили, вызвать Лену на товарищеский суд и устроить ей допрос."

    "Мы с Алисой посовещались и решили не рассказывать в отряде про Дом на Болотах, потому что не были уверены, действительно ли та таинственная девушка, которую мы видели, имеет отношение к магии."


    scene bg attic3 with dissolve


    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_023.mp3"



    "Собрание отряда назначили на тот же день, вечером. Решили собраться после отбоя снова на нашем чердаке."

    "Толик, думая что речь пойдет о нем, испугавшись разоблачения, не пришёл. Когда все пришли, то мы закрыли дверь изнутри на ключ."


    show sp_je_001:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1
    with dissolve

    "Выбрали председателем Женю, потому что Славя, как подруга Лены, отказалась."


    scene bg attic3 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Решено было заслушать нас с Алисой и предъявить обвинение Лене в колдовстве против Алисы. Она публично должна была сознаться, раскаяться и просить прощения."

    "Отряд должен был вынести решение, оставаться ли ей в отряде."

    "Или мы будем ходатайствовать перед ОД, чтобы её от нас убрали, исключили из первого отряда и перевели в другой домик с формулировкой «как утратившую доверие своих товарищей»."

    "Ольге Дмитриевне решили сказать, что причина не подлежит оглашению, и мы ставим её перед фактом. А если она будет настаивать на том, чтобы Лена осталась, мы объявим забастовку."


    scene bg attic3 with dissolve

    show sp_le_016:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Пока мы с Алисой рассказывали события ночи, и какое мы провели расследование, Лена всё время молчала."



    stop music fadeout 0.5 fadeout 1.0

    queue music "audio/music/z_131.mp3"


    "Потом встала и попыталась уйти. Но дверь была заперта и её усадили назад."


    scene cg lynching with dissolve

    "Она стала запираться и на все вопросы говорить НЕТ. На нее напирали и сказали, что она не уйдет отсюда, пока мы не вынесем решения."


    pause (10000000000000000000000.0)


    scene bg attic3 with dissolve

    show sp_le_020:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Тогда Лену накрыла истерика. Она кричала, что мы все её ненавидим и только ищем повода от неё избавится. (Это было неправдой)."

    "А ещё, что мы придумали нелепую причину, что это подло, и что она чиста, как первый снег."


    scene bg sl_le_room2 with dissolve

    show sp_mi_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    show sp_al_004:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Тогда мы послали Алису и Мику, провести обыск в её домике. Они вернулись с уликами. Книгами по магии, травами и чёрным плащом."


    scene bg attic3 with dissolve

    show sp_le_020:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Отпираться стало бессмысленно. Даже мы с Алисой уже стали верить в то, что это она."

    "Но Лена упала на пол в истерике, её держали, а у неё изо рта шла пена. Она кричала ужасные вещи и бросалась на всех. Пришлось её связать простыней."


    scene cg lynching with dissolve

    "Поскольку Лена не созналась, решено было ходатайствовать перед ОД о её отчислении из отряда. Мы вели протокол собрания, всё как положено. Проголосовали почти единогласно."

    "Воздержались только Славя и Семён."

    "Решение Лене зачитали, с перечислением всех её проступков. Не забыли и драку в походе."


    scene bg attic3 with dissolve

    show sp_le_020:
        yalign 0.0 subpixel True
        xalign 1.0 subpixel True
        zoom 1.1

    "Потом мы открыли дверь и развязали её. Лена убежала, рыдая."

    hide sp_le_020 with moveoutright


    "У всех было подавленное состояние. Но все понимали, что иначе было нельзя."

    "В ТУ ЖЕ НОЧЬ ЛЕНА... ИСЧЕЗЛА."



    pause (10000000000000000000000.0)

    scene black with fade

    stop music fadeout 1.0

    jump day39

return