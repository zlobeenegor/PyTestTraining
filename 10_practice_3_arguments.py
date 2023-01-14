# Renamer
import os
root = os.path.dirname(__file__) # отслеживаем текущую директорию
files =  os.listdir(root) 
print('Program Directory and file name is:')
print (root)
print(files)

arg = []
for f in files:
    if os.path.isfile (os.path.join (root, f)):
        if os.path.splitext(f)[-1] == '.txt':
            arg.append (os.path.join (root, f))
print (arg)

newFName = input ('Enter ne files name:')
if newFName:
     for i, f in enumerate (arg):
          d = os.path.dirname(f)
          name, ext = os.path.splitext(os.path.basename(f))
          print (1, d)
          print (name)
          print (ext)
          fName = newFName + '_' + str(i+1).zfill(2) + ext
          fullPath = os.path.join(d, fName)
          os.rename(f,fullPath)  
input()