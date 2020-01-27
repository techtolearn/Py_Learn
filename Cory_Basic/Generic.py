#Genric example1
#find the file path
#print(sys.path)  # it will all file path and supported libraries path

#Genric example2
#assume that the file you are trying to import from outside of the python root directory
#first you have to append the file directory to sys.path and then you can import
'''
import sys
sys.path.append('C:\\Learning\\Generic') #this path where my Comprehension is located
from Comprehension import * # now you can call any fun defined inside the Comprehension

print (sys.path)'''

#Genric example3
''' common stand lib modules
1.random
2.math
3.datetime
4.calender
5.os'''

#check the where the some standar libraries are available
import random
import math
import datetime
import calendar
import os
import sys
import builtins

course = ['Mandya','Mysore','Belgaum','Mangalore','Darawada']
course_name = random.choice(course)
print(course_name)  #it will give path for the random file where it is avaible

rad = math.radians(90)
print(rad)
print(math.sin(rad))


today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

print (os.getcwd())  # it will give the current working dir

print("\n")
print(sys.executable)
print(sys.version)
print(dir(os)) # dir(libraryname) -- it will tell us all the built in functions


print("\n")
print(dir(builtins))  # dir(libraryname) -- it will tell us all the built in functions
