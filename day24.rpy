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


    stop music fadeout 1.0


    play music "audio/music/z_495.mp3"


    scene bg yulya_hous with dissolve

    "Маленькие следы привели нас к заброшенному домику в лесу."


    pause (10000000000000000000000.0)

    "Некоторое время, мы наблюдали из кустов, но никакого движения возле домика не обнаружили."


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Наверное, это и есть убежище девочки-кошки."

    hide sp_ul_019

 
    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Давай называть её Юлей. И пожалуйста, больше не трогай её хвост. Будем относиться к ней как к обычной девочке. Думаю, она очень ранима."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Ну да. Я подумала, если бы у меня был хвост и меня бы дразнили, то я тоже... Была бы ранимой. Ну что, зайдем в домик?"

    hide sp_ul_019

 
    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Погоди, надо оглядеться. Что-то тут не так."

    hide sp_al_056


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.2 xanchor 0.5 yanchor 0.0 zoom 1.2



    pause (10000000000000000000000.0)

    "Мы обошли домик и везде на деревьях вокруг него свисали с веток гирлянды нанизанных на веревочки грибов."

    "Мы шли, раздвигая эти свисающие «шторки». Иногда их было так много, что за ними не видно было самого домика. Одни грибы были почти свежие, заготовленные недавно, другие очень сухие."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Странно, но ведь грибы могут портиться от дождей. Я не заметила ни одного плесневелого гриба. Тут что, никогда не бывает дождей?"

    al "И потом, они же не могут висеть тут вечно? Значит, где-то есть целый склад этих грибов."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Помнишь тот ливень, когда мы ходили к самолету? Здесь не просто дожди, тут бывает что-то вроде репетиции Вселенского Потопа."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Да, помню. Но кода мы вернулись, я спрашивала у всех, и мне сказали, что никакого дождя в лагере не было."

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Чудеса чудесатые. Там идет дождь, а тут прямо заповедник хорошей погоды."

    hide sp_ul_019


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Не трогай гриб! Ты что, уже жуешь? Сумасшедшая! А вдруг они ядовиты?!"

    hide sp_al_057


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Я только маленький кусочек. Попробовать, насколько они высохли."

    hide sp_ul_021


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Выплюнь сейчас же!"

    hide sp_al_057


    "В кустах раздался шорох. Потом ещё. Было ощущение, что кто-то наблюдает за нами, но не показывается. В этой ситуации входить в домик было бы верхом неуважения к хозяину. И кажется, Алиса это тоже поняла."


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Эй, Юля! Мы знаем, что ты здесь. Выйди, пожалуйста... Мы заблудились. Мы не искали твоё убежище. Просто наткнулись на твои следы. Нам нужна помощь."

    hide sp_al_056


    stop music fadeout 1.0


    play music "audio/music/z_480.mp3"


    scene cg yulya_bushes with dissolve

    "Из-за дерева появилась любопытное личико. Какое-то время Юля смотрела на нас своими огромными глазищами. Потом вышла, и я увидела, что она всё в том же коричневом платьице, в котором была в развалинах."

    "Бедняжка. Наверное, у неё не во что переодеться. Так и бегает, босая и в стареньком платьице."


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.2 xanchor 0.5 yanchor 0.0 zoom 1.2


    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    "Я посмотрела на Алису. По выражению её лица я поняла, что мы думаем об одном и том же."

    "Алиса нагнулась к моему уху и прошептала:"

    hide sp_al_057

    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Интересно, а под платьем у неё что-нибудь надето?"

    hide sp_al_056


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Тоже шёпотом)\nВот-вот. И я подумала. Особенно, когда она задирает этот свой хвост."

    hide sp_ul_019


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "А чего ей его задирать? Её же никто не гладит. Ну, я так думаю. "

    hide sp_al_056

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Кстати, интересная мысль. Надо погладить и посмотреть, поднимется хвостик или нет. Обычные кошки задирают. Вот тогда и узнаем."

    hide sp_al_055


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    uv "(Выходя из-за дерева) \nУ меня есть всё, что есть у вас и даже больше. Я таскаю нижнее белье с веревок у вас в лагере. Только мне редко подходят размеры ваших пионерок."

    uv "(Приподнимает платье) \nЭто вы хотели увидеть?"

    hide sp_iul_009


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "(Краснея, шепчет) \nЧерт, услышала. Я и забыла, что у кошек отличный слух. Но я же шепотом, а до неё никак не меньше двадцати метров."

    hide sp_al_056

    "Трусики действительно были. И они были розовые."


    scene cg yulya_hide with dissolve

    uv "(Идет к домику и манит рукой) \nМожете войти. Это действительно моё убежище. Но оно не одно. Есть ещё. Когда начинается потоп, я ухожу в Пещеру."

    uv "Но потоп всегда происходит в долине. Тут никогда не бывает дождей."

    pause (10000000000000000000000.0)


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.2 xanchor 0.5 yanchor 0.0 zoom 1.2


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1


    ul "Тогда зачем ты уходишь?"

    hide sp_ul_019   


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "Из осторожности."

    hide sp_iul_009


    stop music fadeout 1.0


    play music "audio/music/z_478.mp3"


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.4 xanchor 0.5 yanchor 0.0 zoom 1.4


    pause (10000000000000000000000.0)


    scene bg yulya_room with dissolve

    "Мы вошли за ней в домик. В нём тоже с потолка и отовсюду, откуда только было можно, свисали пучки. Только не грибов, а трав."

    "Было чисто, в углу стояли кровать и тумбочка, почти как в нашем домике. Еще стол, на нем свечи, а в небольшой кладовочке много всяких баночек и ступа."
  
    "Уют жилищу придавал, непонятно как оказавшийся тут, камин. Рядом с камином стояли стулья и одно кресло, в воздухе витал запах трав."


    scene bg yulya_bath with dissolve

    "В пристройке была обычная ванна."


    scene bg yulya_room with dissolve


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    uv "(Наблюдая за гостями) \nА вы, наверное, думали, что я живу в норе, без удобств?"

    uv "Нет. Этот домик когда-то был охотничьим домиком хозяина Прииска. Тут всё есть. Даже часть стен из кирпича, камин, ванна и туалет. Я слежу, чтобы всё это не обветшало."

    hide sp_iul_009


    show sp_ul_033:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "С ума сойти!"

    hide sp_ul_033


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Да уж... А с виду  хибара. И не подумаешь, что внутри так уютно."

    hide sp_al_055


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "Так было задумано владельцем. Он сделал домик под древнюю избушку снаружи и обустроил его с удобствам внутри. Богатый был."

    uv "Всё это тащили сюда за много километров от основной дороги. Места тут глухие."


    scene bg yulya_finrplace with dissolve


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Книги на полочке, ты читаешь? Ой и бумажные снежинки... Сама вырезала? И мячик! Не его ли так долго искал Тарас Юрьевич?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Он самый. А нас поругали. А он вот где."

    hide sp_al_055


    show sp_iul_010:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "(Краснея) \nЧитаю. А мячик я взяла поиграть. На время. Честное слово. Снежинки я вырезала. Тут нет зимы, но я помню ее по детству. Вы же не заберете мячик?"

    hide sp_iul_010


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Нет. Если что, мы тебя не видели и про мяч не знаем. \n(подмигивает)"


    scene bg yulya_room with dissolve


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "(Садясь на стул) \nА почему у стульев такие короткие ножки?"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Не дожидаясь ответа Юли) \nПочему-почему, логику включи. Отпилила она их. Ей на взрослых стульях неудобно. Она же маленькая!"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Да, как-то я не подумала. А можно спальню посмотреть?"


    scene bg yulya_bed with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Да... Но у меня там беспорядок. Я не ждала гостей."

    hide sp_iul_009


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Уже просунув нос в спальню) \nУх ты! Круто! Как тут уютно! Хa! Беспорядок. Не видела ты нашу с Алисой комнату."

    hide sp_ul_021


    scene bg yulya_room with dissolve

    show sp_al_057:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    "(Алиса делает страшные глаза)"


    scene bg yulya_bed with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "У тебя тут просто идеальный порядок. А почему везде семь свечей?"

    hide sp_ul_021


    scene bg yulya_room with dissolve

    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "Ну.. Эээ… Не знаю.. У нас всегда были семь свечей.. Когда еще у меня был дом и родители.. Но я их почти не помню. А вот свечи, помню. Так больше  похоже на настоящий дом."

    hide sp_iul_009


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Улька хватит все выспрашивать! Это неделикатно. А что это за запах? Как будто варится что? Вкусно пахнет."

    hide sp_al_055


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "Рыбка. Наловила в Озере."


    scene cg yulya_fishing3 with dissolve

    pause (10000000000000000000000.0)


    scene bg yulya_room with dissolve

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Так вот кто рыбачил на другом берегу! Мы тебя видели! Только не знали, что это ты. Даже лодку хотели взять. Ну, с разрешения конечно. Думали, какой-то рыбак."

    hide sp_ul_021


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "Я вас заметила, когда вы всем отрядом ещё шли по Тропе. Ну и шуму же от вас!"

    uv "А когда вы пришли к Озеру, то распугали там всю рыбу. Мне пришлось ждать вечера, пока вы угомонитесь и ловить на свет от фонаря."

    hide sp_iul_009


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "Как это, на свет от фонаря?"


    scene cg yulya_fishing2 with dissolve


    # show sp_iul_009:
        # yalign 0.1 subpixel True
        # xalign 1.0 subpixel True
        # zoom 1.2 

    uv "Просто. Рыба же любопытна. Она плывет на свет. А тут я её..."


    scene bg yulya_room with dissolve


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Лапой?!"

    hide sp_ul_019


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "(Толкая Ульяну и обращаясь к Юле) \nОна хотела сказать, что ты не пользуешься удочкой."

    hide sp_al_055


    show sp_iul_008:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "(Улыбаясь) \nДа, «лапой»."

    uv "(Показывает свои маленькие аккуратные ручки) \nВидите когти? Они очень острые. Растут быстро. Приходится их стачивать."

    hide sp_iul_008

    "Юля кивнула на стоящий посреди комнаты, весь исцарапанный, столб."


    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ух ты! Когтеточка! Прямо как у настоящей кош... Ой, я хотела сказать не это. А столб тоже всегда тут был?"

    hide sp_ul_021


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    uv "Да, на него вешали ружья и добычу всякую. Мне повезло. Не нужно выходить каждый раз из домика и портить деревья."

    hide sp_iul_009


    stop music fadeout 1.0


    play music "audio/music/z_417.mp3"


    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Скажи, а вот эти грибы... Ты их ищешь по всему лесу? Или они растут где-то в одном месте?"

    hide sp_al_055


    scene cg yulya_mushrooms with dissolve


    uv "(Манит з собой) \nВот, видите? Растут. Прямо возле домика. Это один вид грибов. А в лесу много всяких."

    pause (10000000000000000000000.0)

    uv "А в старом лагере растут необычные грибы, их больше нигде нет. Эти вот, я запасаю, чтобы питаться. А другие для лечения. Есть еще есть для снов..."


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.4 xanchor 0.5 yanchor 0.0 zoom 1.4


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al_ul "(Переглянувшись, вместе) \nКАК ДЛЯ СНОВ?!"


    scene bg yulya_hous with dissolve:
        xpos 0.5 ypos -0.4 xanchor 0.5 yanchor 0.0 zoom 1.4

    show sp_ul_021:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Ой, как интересно... Наверно, это таинственные, заколдованные, волшебные грибы!"


    hide sp_ul_021


    show sp_al_056:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    al "Все-то тебе везде тайны мерещиться. Я вот думаю... Наши там уже наверное обедают. Эх..."


    scene bg yulya_fireplace2 with dissolve

    "Алиса хищно поглядела в сторону камина, где виднелся котелок и откуда шел соблазнительный пар."


    scene bg yulya_room with dissolve

    show sp_al_055:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Чёт и мы проголодались. Правда, Улька?!"

    hide sp_al_055


    show sp_ul_019:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1
    with dissolve

    ul "(Сглатывая слюну) \nАга, очень проголодались! Там в котелке грибы?"

    hide sp_ul_019


    scene bg yulya_finrplace with dissolve


    show sp_iul_009:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    uv "(Засуетившись) \nНет, не грибы. Это рыбка. Сейчас. Садитесь за стол. Только хлеба у меня нет. Я его не ем."


    scene bg yulya_room with dissolve

    show sp_al_037:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 


    show sp_ul_023:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    al_ul "(Cтремительно усаживаясь за стол, хором) \nДа кому он нужен!"

 





    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    #jump day25

return 

