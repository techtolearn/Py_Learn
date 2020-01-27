''''
https://www.youtube.com/watch?v=sugvnHA7ElY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=56
if __name__ == '__main__'
'''

#print("First Module name : {}".format(__name__))
#output of this print is  : __main__

#putting condition here - Method 1
# print('This always be run')
# if (__name__ ==  '__main__'):
#     print('Run from directly from this module')
# else:
#     print('Run from import first_module')


#method 2
print('This always be run')

def main():
     print('Run from directly from this module')

if(__name__ == '__main__'):
    main()
