'''
https://www.youtube.com/watch?v=DEwgZNC-KyE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=59
My video on Comprehensions:
https://www.youtube.com/watch?v=3dt4O...

My video on Generators:
https://www.youtube.com/watch?v=bD05u...

What is a T-Shaped Skillset?
https://en.wikipedia.org/wiki/T-shape...

'''
# import os,glob
#
# os.chdir('F:/Mobile\MotoG4/WhatsupImage/Sent')
# for file in glob.glob("*.jpg"):
#     print(file)

# Fibonaci series
#  c=a+b, a=b,b=c
# a,b = 0,1
# for i in range(0,10):
#     print(a," ",b," ",a+b)
#     a, b=b,  a+b
#logic for each itereation a = b, b=a+b result a=a+b


#list , tup, Dict and set

# my_list = [10,20,30,40,50]
# for i in my_list:
#     print(i)
# print('\n')
# my_tup =(1,2,3,4,5)
# for i in my_tup:
#     print(i)
# print('\n')
# my_dict = {'name':'Satheesh','Dob':1980,'place':'Virginia'}
# for key,val in my_dict.items():  #iteritems and items = iteritems one item at time where as items put entier items at a time, iteritems has been removed from python 3
#     print("My {} is : {}".format(key,val))
# print('\n')
#
# my_set={5,10,15,20,25,10,5,20,35}  #set always displayas unique value and ignore duplicate
# for i in my_set:
#     print(i)

# note : xrange = yields one result at a time where as range put entire range of number into memory at one but range is getting replaced with xrange in python3

# List comprhension
my_list = [10,20,30,40,50]
sqare = [num*num for num in my_list]
print(sqare)

#generator  - yield keyword says there is generator

def fib(num):
    a,b=0,1
    for i in range(0, num):
        yield "{}: {}".format(i+1,a)
        a, b=b, a+b
for item in fib(10):
    print(item)

