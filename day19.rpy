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


    play music "audio/music/z_123.mp3"

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


    play music "audio/music/z_147.mp3"

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

    al "Ручка с четырьмя разными стержнями. Можно писать Зеленым, Красным. Черным, и Оранжевым. Саманта подарила."


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


    scene cg murzilka2 with dissolve

    je "Не поверите, но тут сохранился даже один из первых номеров Мурзилки. 1924 года!"


    scene cg murzilka3 with dissolve

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

 








    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day20

return 