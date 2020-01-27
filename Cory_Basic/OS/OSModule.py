#  https://www.youtube.com/watch?v=tJxcKyFMTGo&index=23&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

'''
Python Tutorial: OS Module - Use Underlying Operating System Functionality
'''
import os
from datetime import datetime

print(dir(os))  #list out all the methods present in os package

print(os.getcwd()) #originaal dir - C:\Learning\Cory_Basic
os.chdir('/Users/Satheeshkumar/Desktop')  # now you are in the desktop directory
print(os.getcwd())

print(os.listdir())  # list out all the files and folder on desktop dir

'''
Creating directory  
'''
os.mkdir('test') # can create dir - at main level and cannot be subdir
os.makedirs('test1/test1') # can create dir and subdir
print(os.listdir())
os.rmdir('test') # can remove dir - at main level and cannot remove subdir
os.removedirs('test1/test1') # can remove dir and subdir
print(os.listdir())
print("\n")

# Renameing file
# os.mkdir('tests')
# print(os.listdir())
# os.rename('tests','Test')  # rename dir
# os.rename('Test.txt','test.txt') # rename file

print(os.stat('test.txt'))   # list the option of attributes of give file
print('size of the file is : \t',os.stat('test.txt').st_size)# particalar attirbute results
print("\n")
# date time conversion
mod_time = os.stat('test.txt').st_mtime;
print('last modification of the file is : \t',datetime.fromtimestamp(mod_time))# readable format


'''
os.walk - it will go to upto 3 level to find the file
'''
for dirpath,dirname,filename in  os.walk('/Users/Satheeshkumar/Desktop/'):
    print('Current path   : ',dirpath)
    print('directory name : ',dirname)
    print('file name      : ',filename)
    print()

'''
get all environment variables
'''
print(os.environ)
print('Environment variable for path is :\n',os.environ.get('path'))

file_path = os.path.join(os.environ.get('path'),'text.txt') #if you want join any path
print(file_path)
print('Environment variable for path is :\n',os.environ.get('path'))
print(os.path.exists(file_path))
print("\n")
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt')) # split the extension of the file
