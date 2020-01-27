#  https://www.youtube.com/watch?v=ve2pmm5JqmI&index=26&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Tutorial: Automate Parsing and Renaming of Multiple Files
'''
import os

#Example1
# os.chdir('F:\Learning\Java\Derek Banas\Java')
# print(os.getcwd())
#
# for f in os.listdir():
#     f_name,f_ext = os.path.splitext(f)  # it will split based text baed on dot. - gives filename and extension separate
#     f_course,f_format,f_general,f_num=f_name.split() # split based on space between file
#     f_num=f_num.zfill(2)  # this will make f_num with 2 digits by padding 0 if necessary
#     new_name = '{}-{}{}'.format(f_num,f_course,f_ext)
#     os.rename(f,new_name)  # this will replace old filename into new file name

#Example2
os.chdir('F:\Learning\Java\Derek Banas')
i=0
for f in os.listdir():
    i+=1
    f_name,f_space= os.path.splitext(f)
    f_name='{}{}'.format(f_name,'.mp4')
    os.replace(f,f_name)

