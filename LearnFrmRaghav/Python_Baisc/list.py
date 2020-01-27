#list example  ( list [] - ordered|indexed|changable|duplicate)

my_list = [['India','Mandya','Madddur'],['America','Virginia','Mc Lean']]
print (my_list)
print (my_list[0])
print (my_list[1][-1])
print(my_list[0][1])
print(my_list[1][1])
print(my_list[1:2])
print(my_list[1][1:3])
print("\n")
#Order
#my_list[1] = ['Virginia','America','Mc Lean']
#print (my_list)

#Indiexed
#my_list[0] = ['Virginia','America','Mc Lean']
#print (my_list)
#print(len(my_list))

my_list[0].append('boston')
my_list[1].append('London')
my_list[1].append('Paris')
my_list[1].remove('Paris')
my_list[0].insert(2,'Florida')
my_list[1].insert(2,'New York')

print (my_list)
#Pop example
print("Pop Function")
print("=============")
my_list.pop() #it wil delete the last indiex default unless you specified indiex
#my_list.pop(0) #it wil delete the 0 indiex
my_list[0].pop(3)
print (my_list)
print("\n")

#Del and clear example
print("Del and clear Function")
print("======================")
del my_list
print('list deleted')
print("\n")
my_list  = ['Virginia','America','Mc Lean']
print (my_list)
my_list.clear()
print (my_list,'--cleared thelist')
print("\n")

#Reverse example
print("Revers Function")
print("===============")
my_list  = ['Virginia','America','Mc Lean']
print (my_list)
my_list.reverse()
print (my_list)
print("\n")

my_list1 = ['New Jercey',my_list,my_list]
print (my_list)
print (my_list1)
print (my_list1[1][1])
my_list.clear()
if my_list:
    print(my_list)
else:
    print('no elements are present')

