label day24:

    $ days = 24

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True

    stop music fadeout 1.0


    play music "audio/music/z_533.mp3"


    scene cg al_awaking2 with dissolve

    "Когда я проснулась, мы уже лежали обнявшись. Алиса еще спала. Было прохладно, и мы, наверное, инстинктивно прижались друг к другу, чтобы не замерзнуть."

    "Я огляделась. Это действительно была маленькая уютная полянка в лесу. С огромными желтыми цветами и бабочками."

    "Я любовалась ими и жалела, что так мало знаю о природе. Таких бабочек и цветов я раньше никогда не видела."

    "Где-то далеко послышался странный звук. Но как я ни прислушивалась, не смогла понять, что это. Может быть, нас зовут ребята? Было ещё слишком рано, чтобы нас хватились в лагере."

    "Я растолкала Алису. Какое то время мы вместе смотрели на порхающих бабочек. Алиса была очарована ими как и я."

    image an_23_01: # Анимация с Ульяной Алисой, наблюдающими за бабочками
        
        "images/an/an23day/an_d23_01.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_02.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_04.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_05.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_06.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_07.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_08.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_09.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_10.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_11.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_12.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_03.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_13.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_14.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_15.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_16.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    scene an_23_01 with dissolve

    pause (10000000000000000000000.0)


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"
   

    scene bg glade with dissolve

    "Но, как бы там ни было, надо было идти на звук. Алиса выглядела забавно. К ее волосам прилипли листья и веточки, куртка тоже была вымазана чем-то белым, наверное глиной."

    "Я сказала ей об этом. Она ответила, мол, на себя посмотри. И действительно, я немного порвала шорты и тоже была в глине."

    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Где же это мы нашли эту глину? Ничего же такого не было."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Да уж нашли. Кстати, белая глина это признак осадочных пород, точнее известняка."

    "Алиса задумчиво разглядывала белые от глины пальцы."

    al "А осадочные породы сюда может вынести только река. Причем, подземная река. Река наверняка впадает в Бурлейку, так-как она течет по ущелью. Все остальные реки это её притоки. Что это значит?"

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Это значит, что надо искать белую глину. Она выведет нас к притоку, а тот к Бурлейке. И вот мы спасены, потому что если идти вверх по течению Бурлейки, то мы точно придем в лагерь!"

    hide sp_ul_021


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Соображаешь, Ленина!"

    hide sp_al_037


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но в лагерь нам еще рано... Нас будут искать у озера. Значит, надо идти вверх по течению ручья и тогда, он выведет нас на тропу по которой мы шли к озеру."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Почему это?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да потому, что тропа подрезает склон, и все ручьи, идущие со склона, рано или поздно пересекают тропу. Что мы и видели, когда шли к озеру. Я насчитала тогда три ручья."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Офигеть у тебя аналитические способности. Мне такое даже в голову бы не пришло. Хотя с луной мы облажались. И да, это была моя идея, каюсь."

    hide sp_al_056


    scene bg white_stream with dissolve

    "Мы пошли назад, чтобы найти место, где перемазались глиной. Выяснилось, что это ручей, который мы не заметили ночью. Очень маленький ручей и мутно-белый от глины. Мы пошли вверх по течению и скоро вышли на тропу."
 

    scene bg path with dissolve

    "Нашей радости не было предела. Но как выяснилось, это была «не та» тропа. Тропа сначала шла вдоль ручья, потом свернула налево."

    "И тут мы задумались. Идти по ручью или следовать дальше по тропе? Было заманчиво идти по тропе и посовещавшись, мы пошли по ней."

    "Тропа привела нас к подножью горы, дальше она терялась. Это был тупик. Мы прошли еще немного и вскоре уперлись в скалу которая была вся в террасах, похожих на дорожки, идущие вдоль склона."

    "Оставалось, или повернуть назад, или ещё пройти по террасе."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "С террасы скалы откроется вид на реку и мы сориентируемся. Тут довольно высоко."

    hide sp_al_056


    stop music fadeout 1.0


    play music "audio/music/z_1020.mp3"
   

    scene bg burleyka with dissolve

    "И действительно, скоро нам открылся вид на Бурлейку."

    "Это было очень красиво. Река в этом месте входила в ущелье, стены которого сужались, образуя каньон. Вода ускорялась и неслась по каньону, как по желобу, с большой скоростью."

    "Был даже слышен отдаленный рев этого потока. Это и был тот самый звук, что мы слышали в лесу. Так вот почему она Бурлейка! Мы двинулись назад, по террасе, и вдруг Алиса указала мне на склон:"


    stop music fadeout 1.0


    #play music "audio/music/z_480.mp3"
    play music "audio/music/z_492.mp3"


    scene bg terrace with dissolve


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Смотри, там что-то есть. Давай, посмотрим?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но это же на одну террасу ниже. Это нам не по пути."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ерунда, тут метров пять высоты, это несложно."

    hide sp_al_055
 

    scene bg cave2 with dissolve


    "Я согласилась, мы спустились и оказались напротив входа в грот. Грот уводил куда-то вглубь скалы. Со стен капали капли. А с потолка свисали длинные каменные сосульки."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Сталактиты. Давай отобьем кусочек, на память?"

    hide sp_al_055

    "Она постучала по сталактиту и не без труда отбила небольшой кусок. Он заискрился внутри фиолетовым блеском. Красота!"


    image an_23_02: # Анимация аметистовая жеода
        
        "images/an/an23day/an_d23_17.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_18.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_19.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_20.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_21.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
        "images/an/an23day/an_d23_22.webp" with Dissolve(0.5, alpha=True)
        pause 0.5
  
        repeat

    scene an_23_02 with dissolve

    pause (10000000000000000000000.0)


    scene bg cave2 with dissolve


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Это, наверное, жеода. Нам такую показывали в музее геологии, когда мы были на экскурсии. Если повезет, то это друза аметиста."

    hide sp_al_055


    "Мы хотели уходить, но я заметила что-то напоминающее бусинку. Я нагнулась и подняла её."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Это не природная. Это носил человек. Видишь, как она обработана? Если я не ошибаюсь, это сердоликовая бусина. Давай посмотрим, возможно, найдём ещё."

    hide sp_al_056


    scene cg beads with dissolve

    "Мы стали разгребать влажную от стекающей со стен воды глину у своих ног и нашли еще пять точно таких же бусин, но уже нанизанных на полуистлевшую нить."


    scene bg cave2 with dissolve

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Смотри, высохшее, тонкое сухожилие.  Мумифицировалось. Вот какие они были, древние нитки!"

    hide sp_al_056


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Тут была стоянка древнего человека! Пещера сохраняет всё. Микроклимат."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ну, не такого уж и древнего, слишком хорошо обработано. Но то, что эти люди жили в этой пещере – факт."


    scene bg white_stream with dissolve

    "Я положила находки в рюкзак. Больше мы ничего не нашли и отправились вниз по террасе, а потом вскоре нашли начало нашей тропы. Дошли по ней до ручья и снова пошли по нему."


    stop music fadeout 1.0


    play music "audio/music/z_140.mp3"
   

    scene bg coast3 with dissolve

    "Наш ручей привел нас на огромные песчаные плесы, тянущиеся вдоль Бурлейки."

    "Это было очень дикое место, потому что на девственном песке тянувшемуся на километры, не было видно ни одного следа."

    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ещё очень рано, мы успеем прийти в лагерь раньше группы. Другого такого случая побегать голышом у нас не будет."


    scene cg dunes_swimming with dissolve

    "Алиса принялась снимать с себя одежду. Вскоре её блестящие, белые ягодицы замелькали на фоне песка. Она с разгону бросилась в воду и замахала мне рукой:"

    al "Ну же, давай!"

    pause (10000000000000000000000.0)


    "Я тоже разделась и последовала её примеру. Вода была прохладной, но приятной. Мы ныряли и плавали, потом бегали голышом по берегу и играли в догонялки."

    "Потом вымазались в песке, зарывая друг друга по очереди, потом свалились в изнеможении, подставляя тела солнцу и загорая до самого полудня."


    stop music fadeout 1.0


    play music "audio/music/z_152.mp3"

    scene bg dunes with dissolve


    "Припекало. Идти никуда не хотелось."


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Всё! Ополаскивайся и пошли. Если они послали Васю в лагерь сообщить о нас, (только он и ОД знают дорогу), то нас точно ищут все отряды, включая администрацию. Будет настоящее светопреставление."

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Но идти до лагеря сутки."

    hide sp_ul_019


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Усмехнувшись) \nВасе? Ты шутишь? Видела его костыли длиннющие? Он домчит до лагеря за пару часов."

    hide sp_al_037


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "И никакие не костыли. Я видела его ноги..."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Заинтересованно)  \nНу-ну... Когда это ты видела его ноги?"

    hide sp_al_055


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Утром, он как раз искупался и готовил нам кофе. Красивые ноги, между прочим."

    hide sp_ul_021


    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Улыбаясь) \nПонятно. Смотри, Жене, похоже, они тоже понравились."

    hide sp_al_037


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Скажешь тоже. Мне Вася в этом смысле не интересен. Я бы за Женьку только радовалась. Он про нее расспрашивал, кстати."

    hide sp_ul_021


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Ух ты. Расскажешь?"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Давай-ка думать лучше, как выбираться. Допустим, мы не встретим отряд и пойдем в лагерь."

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Если придём рано, нас отругают и накажут."

    al "А если придем через день, то все очень переволнуются и будут рады, что мы просто живы. Сочиним слезную историю вроде той, что рассказала нам Ольга Дмитриевна."

    hide sp_al_055


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну да. Убегали от медведя, голодали, чуть не сорвались со скалы, чуть не утонули в реке, болоте, и всё такое."

    hide sp_ul_023

 
    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Оглядывает Ульяну) \nНу и вид у тебя, Улька! Видела бы ты себя перемазанную в песке. Так надо будет явиться в лагерь."

    hide sp_al_037


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Что, голыми?"

    hide sp_ul_023
 
 
    # stop music fadeout 1.0


    # play music "audio/music/z_1014.mp3"


    scene bg coast3 with dissolve

    "Алиса стала хохотать, я тоже, и мы стали бороться и кататься по песку, окончательно перемазавшись."

    "В результате, я победила, сев на Алису сверху. Конечно, я думаю, что она поддалась мне, но это мелочи."

    al "Сдаюсь, сдаюсь!"


    stop music fadeout 1.0


    play music "audio/music/z_009.mp3"


    "Ополоснувшись, мы собрали вещи, оделись и пошли по левому берегу вверх по течению."


    scene cg footprints with dissolve

    "С этой стороны реки мы никогда еще не были, но знали что скоро начнутся камыши и болото. Поэтому мы взяли правее и вскоре снова вошли в лес. На этот раз реку было хорошо слышно и мы не боялись заблудиться."

    "Через полчаса мы вышли на опушку леса и миновав её, вошли в заросшую цветами долину, по которой пролегала маленькая чуть заметная тропка. Алиса наклонилась, показав мне на неё."


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene cg footprints2 with dissolve

    "На тропе явственно отпечатался след чьей-то босой, очень маленькой, ноги."

    pause (10000000000000000000000.0)


    scene cg footprints3 with dissolve

    al "Никого не напоминает?"

    al_ul "(В один голос) \nЮЛЯ!"














    pause (10000000000000000000000.0)
  
  
    scene cg map_fragment with dissolve


    "Вот я срисовала тут и карту и следы."

    pause (10000000000000000000000.0)


    scene cg fooptprints_comparison with dissolve


    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day25

return 

