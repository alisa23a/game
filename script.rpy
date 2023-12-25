# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

define ul = Character('Ульяна', color="#ff3366")

define al = Character('Алиса', color="#ff6600")

define pi = Character('Пионер', color="#66ff99")

define pe = Character('Петрович', color="#33ff66")

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
