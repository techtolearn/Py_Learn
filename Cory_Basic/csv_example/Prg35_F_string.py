# https://www.youtube.com/watch?v=nghuHvKLhJA&index=35&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Quick Tip: F-Strings - How to Use Them and Advanced String Formatting
'''

#general format
# first_name = 'Tanvi'
# last_name = 'Satheesh'
#
# sentence = 'My daughter name is {} {}'.format(first_name,last_name)
# print(sentence)
# print("\n")
# #F-string format
# sentence = f'My Daughter name is {first_name} {last_name}'
# print(sentence)
# print("\n")
# #F-string format - can used along with functiona or method
# sentence = f'My Daughter name is {first_name.upper()} {last_name.upper()} and length of  name is {len(first_name+last_name)}'
# print(sentence)


#example when pass the data using dictionary

# person ={'Name':'Tanvi Satheesh','Age': '2'}
# sentence = 'My daughter name is {} and her age is  {} years old'.format(person['Name'],person['Age'])
# print(sentence)
# print("\n")
#
# #note we use double code to avoid impact of single quote in F-string
# sentence = f"My daughter name is {person['Name']} and her age is  {person['Age']} years old"
# print(sentence)
# print("\n")
#
# #perform calculation
# sentence = f'4 times 11 is  {4*11}'
# print(sentence)
# print("\n")
# for n in range(1,11):
#     sentence = f'The value of n is {n:02}'  #0 padding :02
#     print(sentence)
# print("\n")
# #formate decimals
# pi = 3.14159265
# sentence = f'PI is qual to {pi}'
# print(sentence)
# sentenceAfterFormat = f'PI is qual to {pi:.4f}'  #four decimal and rounded
# print(sentenceAfterFormat)


#date format
from datetime import datetime
birthday =  datetime(2017, 4,8)
sentence = f'My daughter birthday is on {birthday}'
print(sentence)

sentenceafterFormat = f'My daughter birthday is on {birthday:%B %d, %Y}'
print(sentenceafterFormat)
