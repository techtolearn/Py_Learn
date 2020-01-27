#Tuple - ordered|indexed|unchangabele|duplicate

my_tuple = ('Cities',['India','Mandya','Madddur'],['America','Virginia','Mc Lean'])
print (my_tuple)
print (my_tuple[0])
print (my_tuple[-1])
print (my_tuple[2][-1])
print(my_tuple[0][1])
print(my_tuple[1][1])
print(my_tuple[0:2]) #print the value present in the index 0,1
print(my_tuple[1][1:3])
print("\n")
#ex : Unachangeble

print("example of unchangable")
print("======================")
#my_tuple[0] = 'Town'  #this will throw an error
#del my_tuple[0] #this will throw an error
print("\n")
my_tuple[1][1] = 'Karadakere'  # where as here it doesn't as it is present in the list [] and it will accept here
print(my_tuple)
print("\n")
del my_tuple[1][1]
print(my_tuple)

print(len(my_tuple))
print(len(my_tuple[1]))
print("\n")

#Condition example
print("in codition example")
print("===================")

print('Cities' in my_tuple)
print('cities' in my_tuple)
print("\n")
print('America' in my_tuple[2])
print("\n")
print(my_tuple[2][0])
print('Amer' in my_tuple[2][0])
