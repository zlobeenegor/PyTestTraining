# This program creat folder

import os

path = r'E:\STDPython'

projectname = input('Enter the name of project: ')
print ('Your project name is: ' + projectname)

folders = \
[ ['input', [
     ['src',[]],
     ['doc',[]],
  ]],   
  ['output',[
     ['render',[]],
     ['video', []],
  ]],    
  ['scenes',[]],
  ['assets',[
     ['charcter', []],
     ['location', []],
  ]]
] 

#function is checks if the folder exists and creates the new folder
def createFolder(path):
    if not os.path.exists (path):
        os.mkdir (path)

#function is checks if the folder exists and creates the folder lower level used recursion
def build (root, data):
    if data:
        for d in data:
            #print (d)
            name = d[0]
            path = os.path.join(root,name)
            createFolder(path) 
            build(path,d[1])
            
if projectname:
    fullPath = os.path.join (path,projectname)
    createFolder(fullPath)
    build(fullPath,folders)

input()
