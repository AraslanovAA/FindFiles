import os
import shutil

StartDirectory = "C:\\Users\\User\\PycharmProjects\Test"
DestinationDirectory = "C:\\Users\\User\PycharmProjects\Destination"

#files = [f for f in os.listdir(StartDirectory) код на случай если не требуется заглядывать в подкаталоги
#         if ((f.endswith('.txt')) or(f.endswith('.png')))]  прикручу этот код, когда добавлю GUI



AllDerectPng = []#получаем полный путь всех элементов заданного типа в указанном каталоге и подкаталогах
for d, dirs, files in os.walk(StartDirectory):
    for f in files:
        if f.endswith('.txt'):
            path = os.path.join(d,f) # формирование адреса
            dest = os.path.join(DestinationDirectory,f)
            shutil.move(path,dest)
            AllDerectPng.append(path) # добавление адреса в список

#print(files)