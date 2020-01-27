# https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=20
'''
Python Tutorial: Comprehensions - How they work and why you should be using them
'''

nums = [0,1,2,3,4,5,6,7,8,9]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

print("\n Comprhension method")
my_list = [n for n in nums ]
print(my_list)
print("\n")

#Seond example

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

print("Comprhension method")
my_list = [n*n for n in nums ]
print(my_list)

#exmple

#same can be written using map and lambda as below -some times it dosn't covert so it is not showing result
print("***map and lambda method****")
#print("===========================")
my_list = list(map(lambda n :n, nums))
print(my_list)

my_list = []
my_list = list(map(lambda n : n*n, nums))
print(my_list)
print("\n")


#using filter and lambda
print("***Filter and lambda method****")
#print("==============================")

my_list = []
for n in nums:
    if n%2 ==0:
        my_list.append(n)
print(my_list)


my_list = list(filter(lambda n : n%2==0, nums))
print(my_list)
print("\n")

print("***range  method****")
print("====================")
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))   # append always take one argument, if you want append more than one then use extra bracket
print(my_list)



print("\n")
print("***Zip  method****")
print("====================")
F_Name = ['Satheeh','Tanvi','Divya']
L_Name = ['Kumar','Satheesh','Jaikumar']
Name = zip(F_Name,L_Name)
print(list(Name))

print("\n")
print("***Dictionary  method****")
print("====================")
F_Name = ['Satheeh','Tanvi','Divya']
L_Name = ['Kumar','Satheesh','Jaikumar']

my_dict={}
for F_Name,L_Name in list(zip(F_Name,L_Name)):
    my_dict[F_Name]= L_Name

print(my_dict)


#Compreshnesive method

my_dict = { F_Name: L_Name for F_Name,L_Name in list(zip(F_Name,L_Name))}
print(my_dict)

#Set Method  -- will be used to display the unique values mixed list of values
nums =[1,1,2,1,3,4,3,4,5,3,4,5,6,5,7,3,2,8]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
#Compreshnesive method

my_set = { n for n in nums}
print(my_set)
print("\n")


# generators
nums = [0,1,2,3,4,5,6,7,8,9]
def gen_fun(nums):
    for n in nums:
        yield n*n
my_gen = gen_fun(nums)
for i in my_gen:
    print(i)
print("\n")
#Compreshnesive method

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)

