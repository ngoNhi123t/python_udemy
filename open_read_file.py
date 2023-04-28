f = open('practice.txt','w+')
f.write('This is a test string')
f.close
import os
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(C:\\))

import shutil
shutil.move('practice.txt','C:\\Users\\Marcial')
os.listdir()
shutil.move('C:\\Users\\Marcial\practice.txt',os.getcwd())
os.listdir()

###NOTE: The os module provides 3 methods for deleting files:

#os.unlink(path) which deletes a file at the path your provide
#os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
#shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
#All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal. ___

#Install the send2trash module with:

#pip install send2trash
import send2trash
os.listdir()
send2trash.send2trash('practice.txt')
os.listdir()

### WALK

os.getcwd()
os.listdir()
for folder, sub_folders, files in os.walk('Exam_Top_Level'):
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
    # Now look at subfolders
    ### tìm file 
   
