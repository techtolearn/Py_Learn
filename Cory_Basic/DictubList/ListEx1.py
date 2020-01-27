'''
https://www.youtube.com/watch?v=A1HUzrvS-Pw&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=6
'''

import random
import math
# program to generate 5 random numbers from the list 1 to 9
numList = []
for i in range(5):
    numList.append(random.randrange(1,9))

for i in numList:
    print(i)
