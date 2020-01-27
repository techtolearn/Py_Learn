'''
https://www.youtube.com/watch?v=-aKFBoZpiqA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=49
Context Managers - Efficiently Managing Resources
'''
from contextlib import contextmanager
import os
# class Open_File():
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
# the above code shows how the below code works
# @contextmanager
# def Open_File(file,mode):
#     try:
#         f = open(file,mode)
#         yield f
#     finally:
#         f.close()
#
# with Open_File('sample.txt', 'w') as f:
#     f.write('Testing')
# print(f.closed)
# *******************************************************
# cwd = os.getcwd()
# os.chdir('sample1')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('sample2')
# print(os.listdir())
# os.chdir(cwd)
  #* we can write as below
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        osnme=os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('sample1'):
    print(os.listdir())


with change_dir('sample2'):
    print(os.listdir())

