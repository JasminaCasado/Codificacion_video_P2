import os

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

def selectVideo():
    print("Videos disponibles\n")
    print("1. bbb_160x120")
    print("2. bbb_360x240")
    print("3. bbb_480")
    print("4. bbb_720")
    print("5. bbb_1080\n")

    select = pedirNumeroEntero()

    if select == 1:
        return'bbb_160x120.mp4'

    elif select == 2:
        return'bbb_360x240.mp4'

    elif select == 3:
        return'bbb_480.mp4'

    elif select == 4:
        return'bbb_720.mp4'

    elif select == 5:
        return'bbb_video.mp4'


def dataInfo():
    video = selectVideo()
    #print(video)
    codec = f"ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of " \
               f"default=noprint_wrappers=1 {video}"
    size = f"ffprobe -v error -show_entries format=size -of default=noprint_wrappers=1 {video}"
    bit_rate = f"ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of " \
               f"default=noprint_wrappers=1 {video}"
    height = f"ffprobe -v error -select_streams v:0 -show_entries stream=height -of " \
               f"default=noprint_wrappers=1 {video}"

    os.system(codec)
    os.system(bit_rate)
    os.system(height)

def renameFile(old_name, new_name, file_path):

    #old_name = input('Enter the file name: ')
    #new_name = input('Enter the new name of the file: ')
    #file_type = input('Enter the file type: ')

    commandOld = file_path + old_name
    #print(commandOld)
    commandNew = file_path + new_name
    #print(commandNew)
    os.rename(commandOld, commandNew)

def resizeFile():
    video = selectVideo()
    w = input('Escalado a lo ancho: ')
    h = input('Escalado a lo alto: ')
    output = input('Nombre y formato de salida: ')
    command = f"ffmpeg -i {video} -vf scale={w}:{h} {output}"
    os.system(command)

def change_codec():
    video = selectVideo()
    new_codec= input('Introduce el nuevo video code') # libx264
    output = input('Nombre y formato de salida: ')
    command = f"ffmpeg -i {video} -c:v {new_codec} -crf 30 -b:v 0 -strict experimental {output}"

    os.system(command)


salir = False
opcion = 0

while not salir:

    print ("1. Opcion 1 : Codec, Bit Rate y Weight video")
    print ("2. Opcion 2 : Rename video")
    print ("3. Opcion 3 : Resize video")
    print ("4. opcion 4 : Modificar Codec de video")
    print ("5. Salir")

    # print ("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        dataInfo()

    elif opcion == 2:
        file_path = input('En que ruta esta el video?')
        video = input("Que video quieres renombrar (recuerda el formato!)")
        #print(video)
        new_name = input("Que nombre quieres poner al video (recuerda el formato!)")
        #print(new_name)

        renameFile(video, new_name, file_path+'/')

    elif opcion == 3:
        resizeFile()

    elif opcion == 4:
        change_codec()

    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")

print ("Fin")
