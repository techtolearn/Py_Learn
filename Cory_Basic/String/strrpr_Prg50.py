'''
https://www.youtube.com/watch?v=5cvM-crlDvg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=50
Python Tutorial: str() vs repr()
'''
import  datetime
import pytz
# example 1
# a =[1,2,3,4]
# b='Sample String'
#
# print(str(a))
# print(repr(a))
#
# print(str(b))
# print(repr(b))

# example 2
a = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
b= str(a)

print('str(a) :  {}'.format(str(a)))
print('str(b) :  {}'.format(str(b)))
print('\n')
print('repr(a) :  {}'.format(repr(a)))
print('repr(b) :  {}'.format(repr(b)))
