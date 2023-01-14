# Работа с файлами
'''
Исходные данные:
    путь размещения файла: E:\STDPython\09_practice_1_sequences\frame
    файлы:
        'text101.txt'
        'text102.txt'
        'text105.txt'
        'text106.txt'
        'text107.txt'
        'text115.txt'
        'text85.txt'
        'text86.txt'
        'text87.txt'
        'text88.txt'
        'text89.txt'
        'text90.txt'
        'text91.txt'
        'text92.txt'
        'text93.txt'
        'text94.txt'
        'text95.txt'
        'text96.txt'
        'text97.txt'
        'text98.txt'
        'text99.txt'
задача:
1. Сформировать листинг файлов из директории
2. Разделить название файла на имя и расширение
3. Сформировать новое имя для файла
4. Найти пропущенные кадры. Кадр = порядковый номер файла
5. Вывести сообщение  пропущенных файлах
'''
import os
import shutil
 
path = r'E:\STDPython\09_practice_1_sequences\frame'
correctname = 'shot_001'
padding = 4

#1.list of files

tmp = os.listdir(path)
files=[]
for t in tmp:
    if os.path.isfile (os.path.join(path,t)): #Исключаем из множества папки
        files.append(t) # добавляем во множество только файлы, исключая папки

#2.Separate name of file

frames = []
for f in files:
    name, ext = os.path.splitext(f) #Делим элемент во мнодестве на расширение + имя
    fullName = name
    while name[-1].isdigit(): #Выделяем текстову часть файла
        name = name [:-1]
    digits = int(fullName.replace (name,'')) #Выделяем индекс кадра (порядковый номер файла)
    frames.append(digits)
offset = min(frames)-1 # Меняем индекс кадров
        
#3.Generate new name of files

outFolder = os.path.join(path,correctname)
if not os.path.exists(outFolder):
    os.mkdir(outFolder) # Проверяем наличие и создаем папку 'correctname'
for i, f in enumerate(files):  # Формируем кортеж с присвоением индекса файла каждому файлу в кортеже
    old = os.path.join (path,f)
    name,ext = os.path.splitext(f)
    newName = correctname + '_' + str(frames[i]-offset).zfill(padding) + ext #Генерируем новое имя файла
    new = os.path.join (path, correctname, newName)
    if os.path.exists(new):
        os.remove(new)
    shutil.copy2(old, new) #Копируем новые файлы в новую директорию
    
#4.Search missing files

fullRange = range(min(frames), max(frames))
miss=[]
for i in fullRange:
     if not i in frames:
         miss.append(i)


#5.Result message


print ('Miss frames: \n', miss)

# Удаление старых файлов

a = input ('Remove old files [y/n]?:')
print(a)
if a == 'y' or a == 'Y':
    for f in files:
        os.remove(os.path.join(path,f))
print('Complete')        
input()