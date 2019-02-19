import os
import shutil
#todo: случай когда файл с атким именем уже и меется в папке назначения, хотя очевидно задача не для этого предназнаена
def ReplaceByExtencionWhichCat(startDirectory,endDirectory,Extencions, do):
    for f in os.listdir(startDirectory):
        for i in Extencions:
            if f.endswith(i):
                dest = os.path.join(endDirectory, f)
                path = os.path.join(startDirectory, f)
                if do == 1:
                    shutil.copy(path, dest)
                else:
                    shutil.move(path,dest)


def ReplaceByExtencion(startDirectory,endDirectory, Extencions,do):
    '''получаем полный путь всех элементов заданного типа в указанном каталоге и подкаталогах
     перемещаем найденные элементы в конечную директорию'''
    AllUsedNames = []
    for d, dirs, files in os.walk(startDirectory):
        for i in Extencions:
            for f in files:
                if f.endswith(i):
                    path = os.path.join(d,f) # формирование начального адреса
                    for Elem in AllUsedNames:
                         if (Elem == f):#проверяем, не использовалось ли это имя ранее, чтобы не потерять файл
                            f = f.replace(i,'(1)'+i)
                    dest = os.path.join(endDirectory,f)
                    if do == 1:
                        shutil.copy(path,dest)
                    else:
                        shutil.move(path,dest)
                    AllUsedNames.append(f) # запомниаем сохранённые имена