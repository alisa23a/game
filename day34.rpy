label day34:

    $ days = 34

    play music "audio/music/z_300.mp3"

    show screen current_day with fade

    $ show_quick_menu = False

    pause (1000000000000000000.0)

    hide screen current_day

    $ show_quick_menu = True


    stop music fadeout 1.0


    play music "audio/music/z_176.mp3"


    scene bg camp_artifacts with dissolve

    "В связи с ночным происшествием, администрацией лагеря было принято решение не проводить утреннюю линейку, а дать пионерам поспать до 10-11 часов."

    "Потом малышей увели до обеда  на пляж, а старшие группы были предоставлены самим себе."


    scene bg attic2 with dissolve

    "Вместо того, что бы идти как обычно в кружки, мы собрались на чердаке и обсудили всем отрядом то, как мы будем строить баркас."

    "История с Толиком не стала достоянием гласности по двум причинам. Во первых, теперь у нас был компромат на Толика."


    scene bg fi_cabin2 with dissolve  

    show sp_tol_007:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2


    "Мы дождались когда он появится в своей комнатке и нагрянули туда с допросом. Точнее, это был не допрос, а элементарное давление."

    "Стоило только нам заикнуться что мы поставим отряд в известность относительно его предательства, он сразу же готов был сделать для нас что угодно."

    "Взамен он выдал все планы дирекции по лагерю, о которых мы и понятия не имели. Раскрыл причины внутренних дрязг между Виолой и ОД и рассказал о всех слабых сторонах директрисы."

    "Второй причиной было то, что мы хотели завербовать Толика, и нас устраивало то, что ОД ни о чем не будет догадываться. Так нам легче было делать свои дела."


    scene bg attic2 with dissolve

    show sp_tol_001:
        yalign 0.05 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2

    "Поэтому на момент сбора отряда Толик был уже с нами. Он из кожи вон лез, что бы вновь заручиться нашим доверием."


    stop music fadeout 1.0


    play music "audio/music/z_1016.mp3"


    scene bg pfis with dissolve

    "На совете отряда мы решили, что в рабочую команду войдут Семён, Толик, кибернетики, Славя, Лена, Атсуи, Алиса и я. Женя осуществляла информационное прикрытие. Вместе дело пойдет быстрее."

    "К сожалению, времени у нас было немного. Это был обеденный перерыв и время, которое выделялось на занятия в кружках. Иначе бы заметили наше отсутствие."

    "Получалось не больше трех часов в день."

    "Кибернетики сразу решили перевезти и на остров кучу всякого нужного материала: краски, ткань, фанеру, клей и много чего другого."

    "Больше всего мы боялись, что Смутьянов и его команда прознают про нашу затею. Они могли наябедничать директрисе, как это сделали мы на них."

    "Или приплыть и всё поджечь. Второй вариант был бы непоправимым несчастьем. И мы строго соблюдали конспирацию."

    "Ну вот.. Все это было до обеда. После обеда кибернетики уже вовсю начали реализовывать наш план."

    "С роботом у них не ладилось, и они с энтузиазмом, как сказала Алиса, «сменили пластинку»."

    "Славя и Лена решили заняться пошивом. Нужен был парус и всякие мелочи."

    "Кибернетики были не прочь взять нас с собой, но мы с Алисой не могли оказать им сейчас какой либо существенной помощи, а только путались бы под ногами."

    "Тем более, что места в лодке было мало."

    "Особенно, если учесть, что кроме инструментов и всяких нужных им материалов, они взяли с собой Атсуи, которая, наслушавшись наших рассказов о ракушках, хотела понырять возле острова Пирожок."

    "Зато они пообещали нам, что позовут нас, когда нужно будет красить борта."


    scene bg camp_artifacts with dissolve

    "В общем, вскоре мы занялись своими обычными делами."

    "После обеда мы заметили суету в лагере. Взмыленный Тарас Юрьевич, жестикулируя  и делая страшные глаза, что-то взволнованно рассказывал Петровичу."

    "Конечно, я сразу же подобралась поближе, чтобы подслушать, и вот что я узнала."


    scene bg boat_station4 with dissolve


    "Когда физрук пошёл проверять ограждение в «лягушатнике», чтобы отвести туда пятый и шестой отряды купаться, то обнаружил, что ограждения нет."

    "Исчезли две лодки, а также, исчез бакен, который обычно показывал, куда нельзя заплывать на лодках. Даже один понтон сорвало и унесло на дальний пляж."

    "Бакен был привязан к тяжелому бетонному кубу, лежащему на дне, и сорвать его могла только страшная сила. Понтон тоже весил не одну сотню килограмм."


    scene bg camp_artifacts with dissolve

    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2

    fi "Это все проклятая рыбина. Никто такого бы не смог сделать. Еще до обеда все было нормально."

    hide sp_fi_015


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Не надо было привязывать сеть с уловом к понтону. Я же говорил тебе, Тарас! Теперь ты веришь, что он существует?"

    hide sp_pe_005


    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2
    with dissolve

    fi "Я готов в сам убить эту тварь. У меня есть ружье."

    hide sp_fi_015


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Не смеши, что ему твое ружье. Ты его еще найди, этого сома. То, что он стал днем появляться у берега, да еще прямо у лагеря, покинул омут. Вот, что меня беспокоит."

    hide sp_pe_005


    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2
    with dissolve

    fi "Пока мы его не убьем, я не пущу никого в воду. Представляешь, если он утащит ребенка!"

    hide sp_fi_015


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Он корову легко утащит, не то, что ребенка. Нет, так его не убить. Тут надо шарахнуть наверняка."

    pe "Есть у меня одна мыслишка. И помощники есть. А ты объявляй запрет. Надо огородить весь берег флажками, таблички повесить. Проинструктировать вожатых."

    hide sp_pe_005


    "Появилась Ольга Дмитриевна."


    show sp_od_022:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    od "(Встревожено) \nПочему отряды еще здесь? Вы же должны были отвести их на пляж."

    hide sp_od_022


    show sp_fi_015:
        yalign 0.1 subpixel True
        xalign 0.8 subpixel True
        zoom 1.2
    with dissolve

    fi "Тут такое дело, Ольга... \n(что-то шепчет на ухо ОД)"

    hide sp_fi_015


    show sp_od_026:
        yalign 0.0 subpixel True
        xalign 0.45 subpixel True
        zoom 1.1
    with dissolve

    od "Господи! Дети! Всем немедленно покинуть зону купания! Всем вожатым немедленно собраться в лекционном зале музкружка! \n(убегает)"

    hide sp_od_026


    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Тут подошла Алиса. Петрович подозвал нас."

    pe "Так, гаврики. Есть у меня для вас дело!"


    scene bg watchmans_cabin_2 with dissolve

    "Он завел нас в свою сторожку и разложил на столе уже знакомую нам карту."

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    pe "Узнаете место?"


    scene bg watchmans_cabin with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "Омут?"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Он самый. В прошлый раз не удалось словить зверя, но в этот раз мы его точно поймаем."


    scene bg watchmans_cabin with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    al "Так он же рвет все лески и даже канаты. Бесполезно."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2
    with dissolve

    "Петрович порылся в стоявшем под столом ящике и положил на стол какой-то сверток."

    pe "Тут нужна хитрость. Глядите, чем мы его брать будем."

    pe "Тротил! Его у меня много."


    scene bg watchmans_cabin with dissolve

    show sp_ul_050:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    show sp_al_018:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 

    "Мы с Алисой отпрянули."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Не бойтесь, дурехи. Он не опасный. К нему нужно взрыватель сперва прикрепить. Вот тогда жахнет."

    scene bg watchmans_cabin with dissolve

    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    "Я потыкала пальцем сверток."

    hide sp_ul_013


    show sp_al_018:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Не трогай! С ума сошла?"

    hide sp_al_018


    show sp_ul_013:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "И как мы его будем брать этой штукой? Если она рванет, то весь лагерь сбежится."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Эх, молодо-зелено! Так то же если на воздухе. А мы под водой."

    pe "И надо меру знать. Вот три палочки свяжем вместе, самое то будет. Больше нельзя. А то вся рыба в реке всплывет."

    pe "Контузию ему будем делать. Глушить, значит."


    scene bg watchmans_cabin with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "Я о таком только в книжках читала. У нас никто рыбу не глушит, только сетями или удочкой ловят."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Он сети рвет или утаскивает. Нет, тут надо по науке. Будем глушить рыбину!"


    scene bg watchmans_cabin with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А можно, мы возьмем еще одного мальчика? Он надежный. Мы его с собой хотим на дело взять важное. Вот как бы его и проверим. Ну, в общем, еще один человек лишним не будет."


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Берите вашего мальчика. Только вы за него отвечаете. Чтобы молчок! Значит, завтра утром часов в пять, пока вода еще прозрачная, на лодке поплывем."

    pe "Он в омуте на самой серёдке ляжет, на глубине. Его в это время видно будет, маску возьмём. Пусть ваш мальчик наблюдает, а мы будем всё снаряжение готовить. Прямо над ним опустим."

    "Петрович водил пальцем по карте."

    pe "Тут, значит, опустим, а сюда отплывем. До лагеря аккурат километр. Он приложил линейку. Никто даже не проснется."


    scene bg watchmans_cabin with dissolve

    show sp_al_004:
        yalign 0.1 subpixel True
        xalign 1.0 subpixel True
        zoom 1.2 
    with dissolve

    al "А если лодку разорвет? Мы все утонем!"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Так кто же с лодки глушит? Вот чудачка! Сперва ему надо дать заглотать приманку, а к ней привязать поводок, как потянет."

    pe "Взрыватель заводим, отпускаем, пусть на глубину тянет. Через пол минуты шарахнет. Мы далеко будем. И вот..."

    "Петрович протянул нам свёрток с ватой."

    pe "Заткнёте ушки свои нежные."


    scene bg watchmans_cabin with dissolve

    show sp_ul_012:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.1

    ul "А Вы?"


    scene bg watchmans_cabin_2 with dissolve

    show sp_pe_005:
        yalign 0.0 subpixel True
        xalign 0.0 subpixel True
        zoom 1.2

    pe "Так я глухой почти. Мне и так хорошо."
















    pause (10000000000000000000000.0)

    scene black with fade

    stop music

    jump day35

return 