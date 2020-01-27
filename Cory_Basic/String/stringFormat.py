# https://www.youtube.com/watch?v=vTX3IwquFkc&index=22&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates
'''
import datetime

person = {'name':'Satheesh','age':37}
sentence = 'My name is '+person['name']+ ' and I am '+str(person['age'])+' years old'
print(sentence)
print("\n")

#method1 -  without place holder {}
strFormat = 'My name is {} and I am {} years old'.format(person['name'],person['age'])
print(strFormat)
print("\n")

#method2 -  with place holder {0}
strFormat = 'My name is {0} and I am {1} years old'.format(person['name'],person['age'])
print(strFormat)
print("\n")


#method3 -  with place holder {0 with parameter}
strFormat = 'My name is {0[name]} and I am {1[age]} years old'.format(person,person)
print(strFormat)
print("\n")

#method4 -  with place holder  with parameter and format we don;t required to mention twice as it is one lst
strFormat = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(strFormat)
print("\n")

#method4 -  another way of wirting
strFormat = 'My name is {name} and I am {age} years old'.format(**person)
print(strFormat)
print("\n")


#method 4 -  another way of wirting
l = ['Tanvi Satheesh',2]
strFormat = 'My name is {0[0]} and I am {0[1]} years old'.format(l)
print(strFormat)
print("\n")

#xml tag generation
tag='h1'
text ='this is header line'

tagName = '<{0}>{1}</{0}>'.format(tag,text)
print(tagName)
print("\n")

#using class
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('Pritesh',35)
per = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(per)
print("\n")

#method 5 = directly pasying key and value as parameter
per1 = 'My name is {name} and I am {age} years old.'.format(name='Pritesh',age=35)
print(per1)
print("\n")

#formatin string using numbers

for i in range(1,11):
    numForm = 'the value is  {}'.format(i)
    print(numForm)
print("\n")

#display start with 0 prefix - 0 pad upto 2 digit
for i in range(1,11):
    numForm = 'the value is  {:02}'.format(i)
    print(numForm)
print("\n")

#foramte with decimal
pi = 3.1415932
numPrint = 'Pi value is \t {:.2f}'.format(pi)
print(numPrint)
print("\n")

#foramte for seperated with coma for largervalues - )

bytes = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(bytes)
print("\n")

#fomrate and print dates

my_Date = datetime.datetime(2019, 1, 13,  12, 2, 12)
print('date format is ',my_Date)
print("\n")
my_Date1 = '{:%B %d, %Y} '.format(my_Date)
print('date format is ',my_Date1)
print("\n")

#format date in different ways

form_Date = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_Date)
print(form_Date)
print("\n")

