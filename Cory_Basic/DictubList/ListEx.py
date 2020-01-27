'''
https://www.youtube.com/watch?v=A1HUzrvS-Pw&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=6
'''
randList =["string",3.4322,25,'S']

oneToTen = list(range(10))

randList = randList + oneToTen
print(randList)
print('\n')
first3 = randList[0:3]
for i in first3:
    print('{} : {}'.format(first3.index(i),i))
print(first3[0] * 3 )  # it will 3 times of the value of 0th index

print('string' in first3)  # it searches the value in first3 list

print('Index of String is : ',first3.index('string'))

print('how many string are : ',first3.count('string'))

first3[0] ='New String'
for i in first3:
    print('{} : {}'.format(first3.index(i),i))
