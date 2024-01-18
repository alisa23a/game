label day19:

    $ days = 19

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Сегодня ночью было землетрясение. Ну, не то что бы землетрясение, скорее какая-то вибрация и гул, как если бы под лагерем проходила ветка метро. Мы с Алисой даже проснулись и пообсуждали этот странный шум."


    scene cg communications with dissolve

    "Петрович говорил, что в окрестностях лагеря под землей есть шахты. Но что они давно не используются, с самой войны. А вдруг там все ещё кто-то есть? Я поделилась с Алисой своими мыслями."

    "Она меня сначала высмеяла: «Призраки рудокопов гоняют тележки по узкоколейкам, катаются. Сегодня у них праздник и они развлекаются». Но когда звуки и вибрация повторились, она задумалась."

    pause (10000000000000000000000.0)


    scene cg communications2 with dissolve

    "На карте Петровича фиолетовые линии проходили прямо под лагерем, и одна из них проходила под памятником Генде. В этом месте на линии стоял кружочек. И я решила поделиться своей очередной догадкой с Алисой."

    "А что, если фиолетовые линии это и есть старое метро? Тогда где-то на линии должен быть вход в него. Линии сходятся на библиотеке, но там ничего нет. Во всяком случае там, куда мы смогли проникнуть."

    "Не обследованными остались только медпункт и подвал. Но туда мы попасть не могли. На здании библиотеки на карте Петровича тоже стоял кружочек."

    "Если мои предположения насчет метро верны, то это должны быть или выходы или какие то технические шахты, ну, например, воздуховоды."

    "Я знала про метро, потому что папа, когда писал статью про наше метро, спускался туда с рабочими и брал меня с собой."

    "И они объясняли папе что из каждой ветки метро по пути следования поезда, наверх всегда идут небольшие шахты в которых располагаются кабеля, воздухозаборники и технические аварийные колодцы."

    pause (10000000000000000000000.0)


    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1  

    ul "Я предлагаю обследовать памятник."


    scene bg auhouse_crop2

    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Сомневаюсь, что там что-то есть. На линейках я стою рядом с постаментом и от скуки всегда разглядываю его. Это монолит."


    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1  

    ul "Зачем ты тогда разглядываешь его?"


    scene bg auhouse_crop2  

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Затем, что читаю закрашенные на нём надписи. Пионеры, уезжая, ежегодно оставляют свои подписи и год заезда и всякие другие словечки."

    al "Типа: «Тут были Жорик и Димон 5 отряд. Самара. 1962 г». Прямо как наши солдаты на Рейхстаге."

    al "Я узнавала у ОД, и она сказала, что эти надписи потом заставляют закрашивать пионеров следующего заезда. Они бледные и почти не видны под слоями краски, но от дождей снова проступают."


    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1  

    ul "Монолит, говоришь? Но мы стоим со стороны лица памятника, а по бокам постриженные кусты. И еще, сзади памятника тоже кусты. Их-то ты не обследовала?"


    scene bg auhouse_crop2

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Вот делать мне нечего, лазать по кустам."


    scene bg auhouse_crop1

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1  

    ul "А я бы слазила."

    hide sp_ul_012

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Вот, снова трясет."


    scene bg auhouse_crop2

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Мне кажется, если за памятником что-то и есть, то скорее всего бытовка с метлами, граблями, совочками и ведрами. Это сплошь и рядом. Вот тебе и «техническое помещение». "

    "Но если ты настаиваешь, то пойдем, проверим. До утра еще два часа."


    scene cg pe_bench with dissolve

    "Мы взяли фонарики и пошли на площадь. С лавочки нас окликнул Петрович."

    pe "Что это вы про ночам ходите, гаврики? Наверное, замыслили какое-нибудь новое баловство?"


    scene cg al_ul_pe_bench with dissolve

    al "Нет, мы вчера тут потеряли одну вещь, когда играли в казаки разбойники и прятались друг от друга в кустах."

    pe "Ценная, наверное?"

    al "Ну не ценная, но подарок. Для нас — ценная как память. Брелок-фонарик для ключей."

    pe "Так я скажу дворничихе Любе, она у нас подрабатывает на пол-ставки уборкой территории. Если найдет что, то кликну вас. А сейчас, можете отдыхать."

    al "Не, мы сами поищем. Всё равно, если в кустах, она не увидит. Она же только площадь подметает. Жди ещё субботника. Малыши найдут, потом у них ищи-свищи наш брелочек."

    pe "Ну, если охота пуще неволи, то тогда, ищите, конечно."


    scene bg genda with dissolve

    "Памятник стоял в конце площади и мы отошли далеко от лавочки Петровича."

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1  

    ul "Всё, можно не бояться, дед не заметит. Спокойно пошарим за памятником."

    
    scene cg genda_closet with dissolve

    pause (10000000000000000000.0)


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Давай. Смотри, как ты и говорила, там есть дверка. Замок плёвый, если что, я его гвоздем открою. Неплотно прилегает. Свети в щель. Видишь что-нибудь?"

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1 
    with dissolve

    ul "Ага, вижу. Метлу лопату и ведро."

    hide sp_ul_013


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Ой, не могу, сыщики! Шерлок Холмсы!"

    hide sp_al_003


    show sp_ul_016:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1 
    with dissolve

    ul "(Обижено) \nЧего ты смеешься?"

    hide sp_ul_016


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тихо, а то Петровича приманишь! Он любит со своей колотушкой прохаживаться. Сейчас припрется."


    scene cg al_ul_grass with dissolve

    "Я легла на траву и смотрела в небо стараясь не обижаться. Алиса тоже легла рядом. Земля была теплой и пахло травой."

    "Вдруг Алиса замолчала и уставившись куда-то вверх, сказала:"

    al "Улька… Улька, смотри!"

    ul "Ну да, звезды сегодня красивые. Но луны нет. Куда смотреть-то. На Медведицу? Не, она отсюда не видна за деревьями. Надо от реки её смотреть."

    al "Какая медведица?! Смотри на Генду…"

    ul "Ну, смотрю, и что?"

    al "Ну ты и тормоз, смотри лучше!"

    ul "Да смотрю я. Ничего не вижу."

    al "Куда смотрит Генда?"

    ul "(Неуверенно) \nЭ-э-э, так... Он же вроде должен смотреть на площадь? Ну, то есть на... Когда мы на линейке..."

    stop music fadeout 1.0


    play music "audio/music/z_015.mp3"

    scene bg genda_looks_right with dissolve

    al "А сейчас он стоит к ней спиной и смотрит..."


    scene bg genda_looks_right with dissolve

    "(Обе хором) \nНа библиотеку!"


    scene cg al_ul_grass with dissolve

    ul "Не Генда, а прямо Каменный Гость какой-то."

    al "(Восхищенно) \nАф-фигеть! И никто никогда не замечал! Мы первые."

    ul " Алис, не хочешь пожать ему руку?"

    al "Э-э-э... Как Дон Жуан? Нет уж. Только после тебя."

    pause (10000000000000000000000.0)


# Библиотека


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene cg dead_pilot2 with dissolve

    "Планшет, который мы принесли с Алисой из похода на болота, содержал ценные сведения и дополнил те документы, которые мы стащили из подвала библиотеки."

    "Но для полной ясности нужно было найти еще и архивы прииска. Возможно, они были в Доме На Болотах, а возможно, в подвале библиотеки."

    "И мы решили наведаться к Жене ещё раз. Нужно было установить, что связывало медные рудники, прииск и лабораторию."


    scene cg communications with dissolve

    "Карта Петровича ясно показывала, что фиолетовые, непонятного назначения линии, идущие от всех трех объектов, сходились в одной точке. И это была Библиотека."

    "Её здание было старое, дореволюционное. Это тоже наводило на мысли."
  

    scene cg jenya_lib with dissolve

    "Когда мы пришли в библиотеку, Женя, по своему обыкновению, спала опёршись локтями о столик. Мы решили было прокрасться мимо неё, но она услышала шорох и подняла голову."

 
    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "Мы это, за литературой. Нет ли чего-нибудь про ведьм, колдунов? И всякие страшилки."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "(Зевая) \nВы немного опоздали. Всю такую литературу забрала Лена, сказала для Слави."

    "Я не хотела давать из читального зала, но она же наш вожак и староста. Я подумала, что у неё книги точно будут в сохранности. Вы же знаете её принципиальность. Лена обещала, что Славя никому не даст больше читать."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "А ты не помнишь, какие именно книги взяла Лена?"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "А вот список книг, которые она взяла. Я их вычеркнула. Странно, но все эти книги в библиотеке были. Такое впечатление, что Лена знала о том, что они есть. Даже помогла мне их найти."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    ul "Ой, а мы тоже хотим эти книги!"

    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Нет, эти уже на руках, но есть похожая литература, вот, берите из списка те, что не вычеркнуты, они у меня есть. Перепишите те, что вам понравятся."


    scene cg grass_magic with dissolve

    "Вот тут в основном народные лечебные рецепты. Травы и всякие народные заговоры."


    scene cg witchs_hammer with dissolve

    "Это «Молот ведьм»."


    scene cg papus with dissolve

    "А это, старое издание Папюса – «Магия» и «Каббала», две книги в одной."


    scene cg woodoo with dissolve

    "А вот книга – «Африканские народные верования, обычаи и культ Вуду», это интересно будет."


    scene cg mystery_book with dissolve

    "Михайлов, Таинственные явления. Тут целых шесть книг в одном томе."


    scene cg lucifers_throne with dissolve

    "Ну и Еремей Парнов – тут о магии и оккультизме. Тамплиеры и прочее."


    scene cg iquisitions_history with dissolve

    "Вот, возьмите «Историю Инквизиции», Ли Генри Чарльз под редакцией Лозинского. Там всякие архивные документы про сожжение ведьм есть. Только вам, наверное, трудно будет через ять читать. Издание дореволюционное."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2


    al "Женя, откуда ты всё это знаешь, когда ты успела прочитать? Как не зайдем, ты спишь."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "А мы читаем по ночам."


    scene bg library2 with dissolve


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    ul "Мы? С кем это ещё? У нас таких книгоглотов,  раз-два и обчёлся."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Семен интересуется. Он, кстати, говорит, что у него ночами бессонница."


    scene cg sem_je_lib with dissolve

    je "Приходит. Мы читаем и обсуждаем книги. Он, оказывается, очень начитанный и много знает."

    je "Это он мне подсказал религиозную тематику. Я раньше не особо ею интересовалась. А она очень интересная. Вот почитаете «Историю инквизиции» и поймете, что я права."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "Кто бы мог подумать. А по нему и не скажешь. А что еще у тебя брал читать Семен? Может по криптографии там, или  про всякие шифры?"


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Да кстати, ты сказала и я вспомнила."


    scene cg code with dissolve

    je "Он брал одну книжку про фокусы и вторую, кажется, как раз про шифры. Но она в такой детской манере написана. Ну, типа, как самому придумать шифр и играть в тайную переписку с другом."

    je "Ничего серьезного, я даже удивилась зачем ему детская литература. Но он отшутился: «Для лучшего знания детской психологии»."


# ВЫБОР
# СПРОСИТЬ ПРО КНИГУ
# НЕ СПРАШИВАТЬ


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.75 subpixel True
        zoom 1.2

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1

    al "В общем, когда он принесет назад эту детскую книжку про фокусы и шифры, мы сразу к тебе. У нас Ульяна фокусами увлекается. Правда Ульяна?"

    hide sp_ul_013


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.15 subpixel True
        zoom 1.1
    with dissolve

    ul "Это дело я люблю."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Ладно. Только он ее уже принес. Вон она, в зеленой обложке, берите. Она не ценная, я могу дать вам ее с собой.  Кстати, это Лена сказала ему, что я читаю по ночам, он и пришел. Она, тоже иногда заходит. Чай пьем."

    stop music fadeout 1.0


    play music "audio/music/z_131.mp3"

    scene cg lena_painter with dissolve

    je "Она принесла две картины свои. Натюрморты. Вы знали, что она рисует?"


    scene bg library2 with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    ul "(Быстро пряча книгу про фокусы в рюкзак) \nЧё это делается вообще в лагере?! Тут талант на таланте, а мы не в курсе. Алиса! Какие же мы с тобой репортеры-следователи, если ничего не знаем про отряд?"

    hide sp_ul_013


    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    al "Теперь знаем. Надо же... Наши пташки спелись на почве искусства. Не спят ночами. Беседуют о высоком. Всяких рыжих в тусовку не берут. Ну да ладно. Не больно-то надо. У нас своя «свадьба»."

    hide sp_al_004


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1

    ul "Да... У нас своя."

    stop music fadeout 1.0


    play music "audio/music/z_081.mp3"

    scene bg attic_inside with dissolve

    al "Жень, если надоест читать, приходите всем трио к нам с Ульяной на чердак. "

    al "Теперь можно не только в карты перекинуться, но и вечеринку устроить. Семен, кстати, сам предлагал мне как-то тет-а-тет. Отвлечетесь немного от своей истории."


    scene bg library2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    al "И ещё, у меня есть мармелад свежий. А еще классные шариковые ручки, две штуки."

    al "Одну могу презентовать. Оранжевую."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "Мармеладки? Ух ты! А какая ручка?"


    scene cg pen_orange with dissolve

    al "Ручка с шестью разными стержнями. Можно писать Синим, Зеленым, Красным, Черным, Оранжевым и Жёлтым. Саманта подарила."


    scene bg library with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    je "(С загоревшимися глазами) \nУх, ну обалдеть! Мне как раз надо журнал оформлять. Я хочу разными чернилами выписки делать. За такую ручку проси что хочешь."

    je "Тогда сегодня вечером, ладно? Не съешьте все мармеладки! Оставьте бедному библиотекарю."


    scene bg library2 with dissolve

    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2

    al "Ладно не сомневайся, тебя не забудут. Сладкоежка."

    hide sp_al_006


    show sp_ul_016:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    ul "(Чуть не плача) \nПочему ты не сказала... Я тоже такую ручку хочу!"

    hide sp_ul_016


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve

    al "Не плакай."


    scene cg pen_green with dissolve

    al "У меня две, твоя будет зеленая."


    scene bg camp_artifacts with dissolve

    "Мы вышли из библиотеки на площадь."


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Зачем ты про Семена, она же передаст Ленке. Он правда один на один тебе предлагал на чердаке «тусить»? Ленка же с ума сойдет."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Нет конечно, это я выдумала. Но зато, теперь сто процентов, вся компания прибежит к нам. Лена захочет взять ситуацию под контроль."

    hide sp_al_005


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну ты и продуманная."

    hide sp_ul_014


    show sp_al_006:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "А то. Реклама «двигатель торговли»."

    hide sp_al_006


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Как ты думаешь, зачем Лене магия и всякие травы? Она же для себя просила, это же ясно."

    hide sp_ul_013


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Факт, не для Слави. Это надо срочно выяснить. Я думаю, тут замешан Семен. И потом, Семен, оказывается, ходит ночью в Жене. Тебе это ни о чем не говорит? Кого он у нас ещё не окучивал?"

    hide sp_al_005


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Остались Мику и Атсуи. К Саманте он подкатывать боится. Там Мегги. Она его в бараний рог согнет. Видела, какие у неё мышцы? А пресс?"

    ul "Она утром при мне подъем переворотом десять раз подряд на турнике сделала и «солнышко» в придачу. Потом еще отжалась на спор 42 раза."

    hide sp_ul_013


    show sp_al_018:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Афигеть! Даже я такое не могу."

    hide sp_al_018


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, круто. Еще круче то, что теперь у нас есть зацепка. Если шифр в этой книге подойдет у тому, что в дневнике у Семена, мы узнаем все его тайны."


    scene cg semyons_diary with dissolve

    pause (10000000000000000000000.0)


    scene cg code with dissolve

    pause (10000000000000000000000.0) # Не убирать паузу


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene bg auhouse2 with dissolve

    "Не успели мы вернуться из библиотеки, как к нам постучалась Женя.  Я испугалась. Неужели Женя заметила пропажу документов, что мы стащили в прошлый раз?  Вид у неё был расстроенный."


    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    with dissolve
    
    je "Слушайте, девочки, вы самые активные. Ульяна, вроде пишет даже что-то. Ну, я имею в виду, историю лагеря. Тут такое дело. В нашей библиотеке нет журнала для детей."


    scene cg murzilka with dissolve

    je "Я просила Ольгу Дмитриевну как-то доставить в лагерь номера журнала «Мурзилка», но ей всё некогда."


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    
    je "Маме  говорила, так она только отмахнулась. А у нас проблема. «Пионерскую правду» младшие отряды не читают, им скучно. А вот картинки разглядывать всякие, стихи, сказки, это то, что надо."

    "Сказок, кстати, тоже в библиотеке кот наплакал.  И ещё переводилки нужны и раскраски.  Может быть,  Ульяна станет выпускать лагерный вариант журнала «Мурзилка»?"

    "И рассказывать там о лагерных новостях, тех, что интересны именно детям? Семен не оказывается иллюстрировать. Ну, что скажете?"


    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А что... Я хоть и занята, но если Алиса с Семеном помогут... И ты, то мы справимся."


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ммм, ну не знаю. Когда писать-рисовать-то это всё? По ночам разве. У нас и так день не резиновый.  Улька, тебе решать. Но учти, дети не поймут, если ты вдруг пропустишь выпуск журнала из-за своих дел."

    al "А Семена я не особо хочу видеть."


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    
    je "Может, Лена поможет? Она, вроде, тоже рисует."


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да, вот, точно! С Ленкой будет интереснее. Она же никакой нагрузки не несет, кроме своего кружка и кройки и шитья. И тот, два раза в неделю. Пусть помогает."


    scene bg auhouse2 with dissolve

    show sp_je_001:
        yalign 0.05 subpixel True
        xalign 0.45 subpixel True
        zoom 1.2
    
    je "Часть статей могут писать наши. Вот, скажем, Мику и Атсуи. Пусть пишут о том, что им ближе."

    je "Смотрите, сектор водный — Атсуи, сектор про лес и всякую природу — Ульяна, сектор спорта — Алиса, сектор  техники — кибернетики. Вот целая редколлегия по секторам!"


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Технические моменты дети не поймут. Но если в популярной форме... Скажем, как сделать  телефон из спичечных коробков и нитки. Мы в такое в детстве играли."



    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Точно! Мы тоже! А еще делали из мыла, спичек, резинки и катушки от ниток трактор и он бегал!"


    scene cg murzilka3 with dissolve

    je "Не поверите, но тут сохранился даже один из первых номеров Мурзилки. 1924 года!"


    scene cg murzilka2 with dissolve

    je " И один номер 1942 года. Видно, его выпускали даже во время войны."


    stop music fadeout 1.0


    play music "audio/music/z_170.mp3"

    scene bg library3 with dissolve

    "В тот же день мы собрались в библиотеке на первую редколлегию «Мурзилки». ОД одобрила. Конечно, это нагрузка. Но я же будущий репортер и журналист. А тут такой случай!"

    "Теперь у меня две нагрузки: «Пионерская правда» и «Мурзилка». Прямо голова кругом. Пойду полежу, подумаю. Пусть всё, как говорит Петрович, «устаканится» в голове."

    "Заодно напишу статью про День памяти. Скоро его отмечать. Надо готовиться."


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Когда мы вернулись к себе,  Алиса почему-то все время смотрела на меня ЗНАЧИТЕЛЬНО и качала головой."


    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Что ты так смотришь?"


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Ничего... Зашьемся мы с этим журналом, чует мое сердце. Взвалили на себя. Все ты..."


    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Но ты же меня поддержала!"


    scene bg auhouse_crop2 with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Да. Но потом здраво рассудила и поняла, что мы не справимся."


    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Слушай, кажется, я вспомнила, что Толик рассказывал, что ушел со второго курса педучилища, где учился по специальности литература и русский язык! Вот кто нам поможет!"


    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "Точно! Это выход. Будет писать статейки, пока мы будем в отлучке! Давай, сгоняй к нему, он живет в бытовке физрука."


    scene bg auhouse_crop1 with dissolve
   
    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Я там никогда не была. Тарас Юрьевич никого туда не пускает."

    scene bg auhouse_crop2 with dissolve

    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    al "У тебя теперь есть повод.  Все, беги!"


    stop music fadeout 1.0


    play music "audio/music/z_002.mp3"

    scene bg fi_cabin with dissolve

    "Я поднялась по лестнице в бытовку Тараса Юрьевича. Я знала, что физрук сейчас на пляже и наблюдает за купанием младших групп. Я рассчитывала застать Толика одного. Так и случилось."

    "Толик открыл на мой стук, очень удивился и какое-то время переминался с ноги на ногу, видно решая, пропускать ли меня внутрь. Затем все же впустил."

    "Это было, пожалуй, единственное помещение в лагере (кроме бомбоубежища), где мы с Алисой еще не были."


    scene bg fi_cabin2 with dissolve

    "В полутьме помещения я разглядела кровать, боксерскую грушу, свисающую с потолка и кучу всяких спортивных снарядов. Там были гири, гантели, штанга."

    "Ну, в общем, обычная спортивная бытовка как у нас в школе. Только с кроватью и небольшим шкафчиком для книг. Второй кровати не было. Это было странно."

    "И тут я вспомнила, что тетя Люба никогда не уезжала домой после смены, а оставалась в пристройке, рядом со столовой, где у нее была комнатка. Меня тут же осенила догадка."

    "Тарас Юрьевич никогда не спал в своей бытовке! Так-так... Я посмотрела на Толика. Толик был потный и смущенный. Он дышал как после тяжелой физической работы."


    stop music fadeout 1.0


    play music "audio/music/z_012.mp3"

    scene bg fi_cabin3 with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А что ты делал? Почему такой красный?"

    hide sp_ul_012


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Ну, вообще-то я занимаюсь спортом. Качаюсь."

    hide sp_tol_001


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, заметно. Никогда не видела тебя без майки. Думала, ты просто стесняешься лишнего веса. А это, оказывается мышцы."

    hide sp_ul_012


    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Извини, я ополоснусь. Посиди пока на лавочке. Вот тут. Стульев у нас нет. Мне даже угостить тебя нечем."

    hide sp_tol_007


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ничего. Не бери в голову. Я посижу. Подожду."


    scene bg fi_cabin2 with dissolve

    "Толик выскользнул из помещения и я осталась одна. Наверное, побежал в душевую. В бытовке не было ванной. Только умывальник. А это значило, что каждый раз Толик после занятий бегал через площадку в нашу душевую."

    "И я подумала, что теперь буду знать, когда он заканчивает свою гимнастику и при необходимости перехвачу его рядом с раздевалкой. Из нашего домика спортивная площадка была как на ладони."


    scene bg fi_cabin3 with dissolve

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Вскоре он вернулся. От него пахло мылом, свежим телом и каким-то одеколоном. Наверняка, заскочил в домик к кибернетикам и одолжил у них одеколон. Странно, я никогда не видела у него щетины."

    "По возрасту, он должен был постоянно бриться. Папа, например, брился два раза в день. Может, борода у Толика не росла так же, как и волосы на голове? Загадка."

    "В руках у Толика был пакет с  чаем, сахар, печенье и конфеты."

    hide sp_tol_001

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ого, да ты подготовился. Хе-хе."

    hide sp_ul_012

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "(Смущаясь) \nТы первая девушка, пришедшая ко мне в гости, за три года, что я тут работаю."

    hide sp_tol_001


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Девушка? Громко сказано. Ну ладно. Приятно чувствовать себя старше. А то все — малявка, да малявка."

    hide sp_ul_014


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Сейчас поставлю чай. Угощайся конфетами. Или подождешь чаю? У меня кипятильник есть."

    hide sp_tol_001


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Подожду. А пока расскажу тебе, зачем пришла."

    hide sp_ul_012


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Я слушаю..."

    hide sp_tol_001


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "Тут я изложила ему Женину идею и намекнула, что хотела бы видеть его в редколлегии. И что мы с Алисой надеемся, что он сможет взять на себя часть работы по написанию материала для детского журнала."

    hide sp_ul_012


    show sp_tol_003:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Я готов. Но я догадался. Я думаю, что вы хотите, чтобы я взял на себя ВСЮ работу по материалам. Это ведь так?"

    tol "Нет, я не против и очень даже рад. Но если вы будете относиться ко мне как к полноправному члену вашей команды. Надеюсь это не слишком жесткое условие?"

    hide sp_tol_003


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul " Ну, у нас сектора. К тебе будет стекаться материал от кибернетиков, Слави, Мику, Атсуи, Лены. Просто тебе нужно будет это все привести в стройный вид. Ну и от себя что-то... Ты же наблюдательный."

    "К тому же, ты был вожатым седьмого отрада. Знаешь чем живут малыши. Ты лучшая кандидатура."

    hide sp_ul_012


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Вот и чай. Пей. Печенье... Я взял самое лучшее в нашем буфете. Ладно, я согласен. Только побудь еще, поговори со мной. Ладно?"

    hide sp_tol_001


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Хорошо. Не беспокойся, пока я все вкусняшки не съем, я не уйду. У нас уйма времени."

    hide sp_ul_012


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    "Толик радостно засуетился."

    hide sp_tol_001


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Кокетливо) \nА сколько весит вон та гиря? Ты так легко ее переставил одной рукой, можно сказать, почти пальцами. Ты, наверное, очень сильный."

    hide sp_ul_014


    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    tol "Да нет... Не скажу, что очень. В ней едва будет тридцать шесть килограмм. Вот Александр Засс, он же Железный Самсон..."

    hide sp_tol_001


    show sp_ul_024:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    "(Роняя на пол конфеты от удивления) \nПогоди, погоди... Сколько, ты сказал? Тридцать шесть? Это что же, получается... Она весит почти как я?!"

    hide sp_ul_024


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene an_d10_01_bg with dissolve

    show an_10_01

    "Я успела написать статью про День Павших в боях во время Великой Отечественной войны. Статья попала в нашу газету. Во второй половине дня, после обеда, был проведен слет, посвященный ДНЮ ПАВШИХ. Это слет проходил ежегодно."


    stop music fadeout 1.0


    play music "audio/music/z_900.mp3"

    scene cg squad with dissolve

    "Мы с Алисой успели на Поляну Слетов к концу митинга и пристроились в колонну, идущую на мемориал павшим в борьбе с фашизмом, который находился на Кладбище горняков."

    "Впереди шел первый отряд, за ним второй и так далее."

    "Мы замыкали строй малышей из восьмого отряда. Алиса сказала, что не хочет идти на кладбище, но я настояла, потому, что там точно будет перекличка и мы должны будем показаться на глаза Ольге Дмитриевне."

    stop music fadeout 1.0


    play music "audio/music/z_124.mp3"

    "Перед тем как пойти, мы взяли бутерброды и что-нибудь почитать. Не то, что бы мы не уважали память павших, просто митинги обычно затягивались и превращались в страшную рутину."

    "Одно дело было возложить цветы и отсалютовать. Другое, стоять под нещадно палящим солнцем и слушать разглагольствования Тараса Юрьевича. Можно было почитать в тени, а на заключительной стадии присоединиться."


    scene bg oldcem5 with dissolve

    "Я никогда не была на кладбище горняков, а Алиса была. Потому что она проиграла Семену в карты и ходила туда на спор ночью."

    "Я спросила её, выполнил ли Семен свою часть уговора, условием которого было поцеловать Мегги при всем отряде."

    "Она ответила, что он пока не решился. Но срок истекает."

    "Если он так и не решится, то это будет позор. Папа говорил, что карточный долг, это «долг чести», и что до революции были случаи, когда тот, кто не мог отдать долг чести, кончал жизнь самоубийством."

    "Но тогда время был другое. Надо было взять с Семена ЧЕСТНОЕ ПИОНЕРСКОЕ СЛОВО. Хотя, я думаю, Семен сдержит свое обещание."


    scene bg oldroad with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    ul "А тебе было страшно одной на кладбище ночью?"

    hide sp_al_012


    scene bg oldroad with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Еще как!"

    hide sp_al_004

    "Сама я той ночью спала и факт нахождения Алисы на кладбище должны были подтвердить вызвавшиеся идти позади неё Семен, Лена и Славя. Я спросила Алису:"


    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну что, они подтвердили?"

    hide sp_ul_012


    show sp_al_005:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Там что-то ухнуло, наверное, филин или какая-то ночная птица, и они так перетрусили, что убежали. Но они видели, как я входила в ворота. Так что, ЗАЧЕТ."

    hide sp_al_005


    show sp_ul_014:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И что, Семен тоже убежал?"

    hide sp_ul_014


    show sp_al_003:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Славя сказала, что он обогнал её."

    hide sp_al_003



    "Это было так смешно, что мы громко засмеялись. А вожатая восьмого отряда на нас посмотрела с негодованием и сказала: «Как можно смеяться в такую минуту, это же ДЕНЬ ПАМЯТИ!»"

    "Мы пожали плечами и снова хихикали, но в кулак, чтобы она не слышала. Ну посудите сами – если день памяти, значит что же, НЕ ЖИТЬ теперь совсем? Только ходить с кислым лицам и без конца вздыхать?"

    "Глупость какая. Думаю, павшие этого бы не хотели. Ведь на репетиции, когда я пала в спектакле, как Мальчиш-Кибальчиш, все наоборот весело шли и салютовали мне. И были радостные лица. Я же была памятником и всё помню."


    scene bg oldcem6 with dissolve

    "Мы вышли по старой дороге к обнесенному забором кладбищу. Оно и правда было старым и заброшенным."

    "Только тропинка, натоптанная несколькими поколениями пионеров, ведущая к мемориалу, была свежая и ухоженная. "

    "Мемориал представлял собой просто длинную мраморную плиту-постамент, на котором была нарисована звезда и выбиты имена. Больше ничего не было."

    "На постамент взошла наша администрация, во главе с МП и начался митинг."

    "Я подумала, если тела павших лежат под плитой, то наверное им неуютно, что Маргарита Павловна со всей компанией, на них встали сверху."

    "Этими мыслями я поделилась с Алисой. Наши мысли совпали."


    stop music fadeout 1.0


    play music "audio/music/z_023.mp3"

    scene bg oldclock with dissolve

    "Мы тихо спрятались за стеной небольшой часовни , там была тень и не так жарко."

    "Алиса сказала, что митинг будет идти почти час пока все не выскажутся. Значит, можно спокойно почитать."

    "И мы расположились поудобнее, достали бутерброды и стали читать. Это были две книжки из читального зала, которые нам дала Женя под честное слово. Про ведьм и инквизицию."

    "На второй страничке, я заснула."

    "Потом меня разбудила Алиса. Она смотрела куда-то в угол церкви, где был алтарь, и сказала шепотом, что там кто-то есть. Мы спрятали рюкзак с книгами и пошли посмотреть."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"

    scene bg oldclock2 with dissolve

    "Что-то, услышав нас, действительно шевельнулось, а потом метнулось через дверь вверх по ступенькам в старую часовню. "


    scene cg shadow with dissolve

    "Мы услышали топот убегающих ног. Алиса прямо зарычала от злости и крикнула, что если это Толик опять подсматривает чтобы доложить ОД, то ему хана."

    "И мы побежали на звук. Но не догнали, потому что этот КТО-ТО ловко перемахнул через подоконник и скрылся за оградой."


    scene bg oldclock2 with dissolve

    "Когда мы подбежали к окну часовни и посмотрели вниз, то опешили. Там было ОЧЕНЬ высоко."


    show sp_al_044:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Это не Толик. На такие фокусы по уровню физической подготовки способны в лагере только два человека, Мегги и Семен."

    hide sp_al_044


    scene bg oldcem4 with dissolve

    "И мы продолжили погоню. Мы сбежали вниз по лесенке и побежали в ту сторону, куда исчез незнакомец. Пробежав около сотни метров, мы остановились. И Алиса крикнула:"


    show sp_al_007:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2
    with dissolve

    al "Семен выходи! Мы знаем, что это ты."

    hide sp_al_007

    "Но никто не отозвался. Мы услышали звук горна, извещающий, что митинг окончен, и все отряды пошли в лагерь. Мы сразу побежали, чтобы пристроиться к колонне."


    stop music fadeout 1.0


    play music "audio/music/z_058.mp3"

    scene bg square with dissolve

    "Когда мы вернулись в лагерь, стало темнеть. Потом был праздничный ужин. Давали котлеты по-киевски с пюрешкой, салат с сыром и оливками и по одному пирожному «корзинка». Ну и ситро."

    "На каждый стол поставили по три бутылки, уже открытые заранее открывалкой и прикрытые опять крышкой, так что её можно было снять руками."

    "Потом все пошли на Поляну Слетов, смотреть огромный пионерский костер. Мы тоже пошли."

    "Вообще у нас палили костры по любому поводу. Обычно право первой поднести огонь всегда выпадало мне. Но тут я задержалась, и мы с Алисой опоздали к началу."


    scene cg sasha2 with dissolve

    "Выбрали какую-то другую девочку. Кажется, Сашу Бременскую, из второго отряда."

    "Она была такая вся из себя умница и красавица. Ну как в рекламных отчетах о классах, где одни отличники. Но она не задавалась и за это мы ее уважали."


    scene cg sasha with dissolve

    "А еще она занималась в цирковой студии и показывала на концерте номер «каучук». Это где надо было быть очень гибкой. Там она подняла розу, прогнувшись назад, взяв ее  зубами со сцены, не опираясь на руки. Очень эффектно."

    "Но нам потом она показала еще более интересный номер. Она написала на листке бумаги стихи.  Ногами, прогнувшись. Это была фантастика."


    scene cg large_campfire_night with dissolve

    "Но я отвлекалась. Так вот."

    "Было красиво. Костер разожгли из старых ящиков, которые лежали на складе общепита. Их было много. Можно было жечь всю ночь. Нам даже разрешали подкидывать издалека дощечки."

    "Но стоять рядом с этим адским пламенем было невозможно. Тарас Юрьевич, заранее огородил периметр костра на безопасном расстоянии колышками с верёвкой, и за них никто не заходил."


    stop music fadeout 1.0


    play music "audio/music/z_130.mp3"


    "И когда мы сидели так в темноте и любовались костром, я вдруг вспомнила, что мой рюкзак со всякими вещественными доказательствами МЫ ЗАБЫЛИ НА КЛАДБИЩЕ!"


















    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day20

return 