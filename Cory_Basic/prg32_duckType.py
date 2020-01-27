# https://www.youtube.com/watch?v=x3v9zMX1s4s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=32
'''
Duck Typing and Asking Forgiveness, Not Permission (EAFP)
'''
import os

#Example 1
# class Duck:
#
#     def quack(self):
#         print('Quack, quack')
#     def fly(self):
#         print('Flap,flap!')
#
# class Person:
#     def quack(self):
#         print("I'm quacking like a Duck!")
#     def fly(self):
#         print("I'm Flaping my like arms!")

# def quack_and_fly(thing):
#  #Not Duck-Typed (Non-Pythonic)
#     if isinstance(thing,Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('This has to be a Duck')
#         print()
#
# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)

#Example 2
# def quack_and_fly(thing):
#      #Not Duck-Typed (Non-Pythonic)
#         thing.quack()
#         thing.fly()
#         print()
#
# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)

#Example 3
# def quack_and_fly(thing):
#      #LYBL (Non-Pythonic)
#      if hasattr(thing,'quack'):   #itwill check  this attribue is exist in the object
#          if callable(thing.quack()):
#              thing.quack()
#
#      if hasattr(thing,'fly'):
#          if callable(thing.quack()):
#              thing.fly()
#      print()

#Example 4
# def quack_and_fly(thing):
#      #EAFP (Easier to Ask Forgiveness Permission)(Pythonic)
#      try:
#          thing.quack();
#          thing.fly()
#          thing.bark()  # to check exception intentionally given
#      except AttributeError as e:
#         print(e)
#      print()
#
#
# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)

#Example 5

# person = {'name':'satheesh','age':'38','job':'Programmer'}
#
# #LBYL (Non-Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm {name}. I'm {age} year's old and I'm a {job}".format(**person))
# else:
#     print('Missing some keys')
# print()
# #EAFP (Non-Pythonic)
# try:
#     print("I'm {name}. I'm {age} year's old and I'm a {job}".format(**person))
# except Exception as e:
#     print("Missing {} key".format(e))

#Example 6
# #LBYL (Non-Pythonic)
# my_list = [1,2,3,4,5,6]
#
# if len(my_list) >=6:
#     print(my_list[5])
# else:
#     print('that index does not exist')
# print()
# #pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print('that index does not exist')

#Example 6  from python docs
my_file = "/tmp/test.txt"

#Race condtion
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print("File cannot be accessed")

#Non-Race condtion
try:
    f=open(my_file)

except IOError as e:
    print("File cannot be accessed")
else:
    with f:
        print(f.read())
