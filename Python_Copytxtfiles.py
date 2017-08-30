import shutil
import os

source = os.path.normpath("C:/Users/singi/Desktop/Folder_A/")
sourcelist = os.listdir(source)
destination = os.path.normpath("C:/Users/singi/Desktop/Folder_B/")
for file in sourcelist:
    shutil.move(source + "\\" + file, destination)
    print(destination + "\\" + file)

    

