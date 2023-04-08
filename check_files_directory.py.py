import os

for root,dirs,files in os.walk(".",topdown=False):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(name))



import os
pwd = os.getcwd()
list_directory = os.listdir(pwd)
for directory in list_directory:
    print(directory)
