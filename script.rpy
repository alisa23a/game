# Вы можете расположить сценарий своей игры в этом файле.

init:
    transform flip:
        xzoom -1.0

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

define ul = Character('Ульяна', color="#ff3366")

define al = Character('Алиса', color="#ff6600")

define pi = Character('Пионер', color="#66ff99")

define pe = Character('Петрович', color="#996666")

define smu = Character('Смутьянов', color="#ff3300")

define allchar = Character('Все', color="#ffffff")

define sl = Character('Славя', color="#ffff66")

define shu = Character('Шурик', color="#6699ff")

define el = Character('Электроник', color="#ff9999")

define le = Character('Лена', color="#660099")

define je = Character('Женя', color="#CC9900")

define mi = Character('Мику', color="#00ff99")

define ats = Character('Атсуи', color="#336600")

define sam = Character('Саманта', color="#0066CC")

define sem = Character('Семён', color="#999999")

define tol = Character('Толик', color="#996600")

define guys = Character('Мальчики', color="#99CCFF")

define od = Character('Ольга Дмитриевна', color="#ffffff")

define ln = Character('Любовь Никаноровна', color="#ffff99")

define vio = Character('Виола', color="#6633CC")

define al_ul = Character('Алиса и Ульяна', color="#ffffff")

define gan = Character('Долговязый', color="#996633")

define vas = Character('Вася', color="#ff9966")

define uv = Character('Юля', color="#ffd700")

define fi = Character('Тарас Юрьевич', color="#3333ff")

define mp = Character('Маргарита Павловна', color="#ba55d3")

define gan = Character('Долговязый', color="#cc9966")

define zh = Character('Жан', color="#add8e6")

define pis = Character('Пионеры', color="#b22222")

define gop1 = Character('Главный', color="#778899")

define gop2 = Character('Амбал', color="#b8860b")

define gop3 = Character('Дрищ', color="#bc8f8f")

define pch1 = Character('Первый браконьер', color="#ffffff")

define pch2 = Character('Второй браконьер', color="#ffffff")

define pch3 = Character('Третий браконьер', color="#ffffff")

define may = Character('Майя Марковна', color="#dc143c")

define elya = Character('Эля', color="#b0c4de")

define manneq = Character('Главный манекен', color="#d3d3d3")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
#label start:

    #scene bg room

    #show eileen happy

    #e "Вы создали новую игру Ren'Py."

    #e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    #return

label splashscreen:

    scene black

    pause(0.5)

    ## Видео пока закомментированы, чтобы не скипать их каждый раз

    #scene campfire with fade

    #pause(0.05)

    #scene black with fade

    $ renpy.movie_cutscene('video/intro.webm')

    scene black with fade

    # $ renpy.movie_cutscene('video/prologue.webm')

    # scene black with fade

    # $ renpy.movie_cutscene('video/first_morning.webm')

    # scene black with fade

    pause(0.05)

    return

# label start:

    # scene dp page00 

    # pause(200000000)
    
    # e "Вот так выглядит текстовый блок по умолчанию"

    # show screen info_stand

    # pause(200000000)

    # #return


label info_stand:

    stop music

    show screen info_stand
    
    pause (1000000000000)
    
    return
