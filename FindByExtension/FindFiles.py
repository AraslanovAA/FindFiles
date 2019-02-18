import os
import shutil
#для GUI надо чекбоксы: залезать в подкаталоги
#радиобаттоны: копировать/перемещать файлы
# opendirectory enddirectory
# эдит для ввода перебираемых расширений и кнопка чтоб все запустить как минимум
StartDirectory = "C:\с телефона"
DestinationDirectory = "C:\\Users\\User\PycharmProjects\Destination"

#files = [f for f in os.listdir(StartDirectory) код на случай если не требуется заглядывать в подкаталоги
#         if ((f.endswith('.txt')) or(f.endswith('.png')))]  прикручу этот код, когда добавлю GUI



#получаем полный путь всех элементов заданного типа в указанном каталоге и подкаталогах
AllUsedNames = []
for d, dirs, files in os.walk(StartDirectory):
    for f in files:
        if f.endswith('.jpg'):
            path = os.path.join(d,f) # формирование начального адреса
            for Elem in AllUsedNames:
                 if (Elem == f):#проверяем, не использовалось ли это имя ранее, чтобы не потерять файл
                    f = f.replace('.jpg','(1).jpg')
            dest = os.path.join(DestinationDirectory,f)
            shutil.move(path,dest)
            AllUsedNames.append(f) # запомниаем сохранённые имена