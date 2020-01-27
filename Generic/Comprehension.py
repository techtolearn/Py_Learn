#reference - https://www.youtube.com/watch?v=3dt4OGnU5sM
#program to write using comprehensive methods

import sys
num =[1,2,3,4,5,6,7,8,9,10]
my_list = []

for n in num:
    my_list.append(n)
print(my_list)
print("\n")


 #same can be written as below
print("***comprehensive method****")
print("===========================")
my_list = [n for n in num]
print(my_list)
print("\n")


#same can be written using map and lambda as below -some times it dosn't covert so it is not showing result
print("***map and lambda method****")
#print("===========================")
my_list = list(map(lambda n :n, num))
print(my_list)
print("\n")

#another example with similar problem displaying square of each number
print("***Square of each numbers****")
print("=============================")
my_list = []
for n in num:
     my_list.append(n*n)
print(my_list)
print("\n")

#same can be written as below
print("***comprehensive method****")
print("===========================")
my_list = [n*n for n in num]
print(my_list)
print("\n")


#same can be written using map and lambda as below -some times it dosn't covert so it is not showing result
print("***map and lambda method****")
#print("===========================")
my_list = list(map(lambda n : n*n, num))
print(my_list)
print("\n")



#3rd example  finding even number from the list
print("***Find even****")
print("=================")
my_list= []
for n in num:
    if n%2 ==0:
        my_list.append(n)
print(my_list)
print("\n")
#same can be written as below
print("***comprehensive method****")
print("===========================")
my_list = [n for n in num if n%2 ==0]
print(my_list)
print("\n")

print("***filter and lambda method****")
print("===============================")
my_list = list(filter(lambda n: n%2 ==0,num))
print(my_list)
print("\n")

#$rd example  print letter and num
print("***letter num****")
print("=================")
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
print("\n")

#same can be written as below
print("***comprehensive method****")
print("===========================")
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)
print("\n")

print("***filter and lambda method****")
print("===============================")
my_list=list(map(lambda letter,num : (letter,num),'abcd',range(4)))
print(my_list)
print("\n")

#print zip function works as 1 to 1 map
name =['satheesh','Tanvi','Divya','Lokesh']
surname = ['Basavegowda','satheesh','Jaikumar','Sridhar']

#print zip function works as 1 to 1 map
name = zip(name,surname)
print(list(name))
print("\n")


# example using zip
name =['satheesh','Tanvi','Divya','Lokesh']
surname = ['Basavegowda','satheesh','Jaikumar','Sridhar']
my_dct = {}
for name, surname in list(zip(name, surname)):
    my_dct[name] = surname
print(my_dct)

#same can be written as below

my_dct = {}
print("***comprehensive method****")
print("===========================")
my_dct = {name:surname for name,surname in list(zip(name,surname))}
print(my_dct)


print (sys.path)
