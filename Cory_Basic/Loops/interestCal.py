#prg1
#https://www.youtube.com/watch?v=swQEbZ6ez1I&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=2
import random
import math
# principle, rateOfInterest = input('Enter your Principle and Rate of interest ? :  ').split()
#
# principle = float(principle)
# rateOfInterest = float(rateOfInterest) * .01  # rounding of two digit floating number
#
# for i in range(10):
#       principle = principle+principle*rateOfInterest
#
# print('Investment for 10 year is : {:.2f}'.format(principle))
#prg2 odd number

# for i in range(1,21):
#     if i%2 != 0:
#         print(i)

#prg3 Random number generatoin

randomNum = random.randrange(1,51)
print(randomNum)

# prg 4 - built tree

tree_hieght = eval(input('how tall tree is  : '))

space = tree_hieght - 1
hashes =1
stump_spaces = tree_hieght - 1
while tree_hieght!=0:
    for i in range(space):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    space-=1;
    hashes+=2;
    tree_hieght-=1
for i in range(stump_spaces):
    print(' ',end="")
print('#')
