# https://www.youtube.com/watch?v=DZwmZ8Usvnk&index=6&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
# Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements


# difference between == and is (Object identity)

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b ,'  - because a of Id is not same b of id')  # here system will not compare the assigned value rather it compares id of a and b, check below example
print("\n")
print("***Id of a and b is not equal")
print(id(a))
print(id(b))

print("\n")

# False checking values will return for the below conditions always
# False value:- eg: condition = False ,if condition:
# None  - eg: condition = none ,if condition:
# zero any numeric data type - eg: condition = 0 ,if condition:
# any empty sequence ..[] ()  - eg: condition = '',() or [] ,if condition:
# any empty mapping.. {} - eg: condition = {} ,if condition:

condition ={}
if condition:
    print ('condition is true')
else:
    print('condition is false')

#if elif statment
age =21
if age > 16:
    print("you are old enough to drive")
elif age < 16:
    print("you are not old enought to drive")
else:
    print("you are eligible to drive")


# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7
# Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops

# break and continue in loop

nums =[1,2,3,4,5,6]
for num in nums:
    if num == 3:
        print("Found!!")
        break
    print(num)
print("\n")

nums =[1,2,3,4,5,6]
for num in nums:
    if num == 3:
        print("Found!!")
        continue
    print(num)

print("\n")
# Nested loop
nums =[1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num,letter)
print("\n")
#range keyword
for i in range(10):
    print(i)
print("\n")
for i in range(1,10):
    print(i)
print("\n")
#while loop
print("****while Loop****")
print("==================")
x=0
while x<10:
    print(x)
    x+=1

