#program to write "set {}"   -unorder|unindexed|no duplicate
#Ref:https://www.youtube.com/watch?v=Q_7U3NLMXcA
my_set = {2,(3),('rama','ganesh')}
my_set
print(my_set)

print("Accessing for loop instead index")
print("--------------------------------")
for set in my_set:
    print(set)
print("\n")

my_set.add("Ganesh")
my_set.update(["ganesh","ekadantha"])  #multiple elements can be added using [] brackets

print(my_set)
my_set.add("Ganesh")
print(my_set)

print("Remove and Discard difference")
print("-----------------------------")
my_set.discard("ganesh")
print(my_set)
my_set.remove("Ganesh")
print(my_set)

my_set.discard("ganesh")   #when execute repetativly it will not throw an error - can be used wheter you are not sure the element has been removed or not
print(my_set)
#my_set.remove("Ganesh")   #this cannot be used repeatativly
#print(my_set)

print("pop and clear difference")
print("--------------------------")

my_set.pop()
print(my_set)
my_set.clear()
print(my_set)
print("\n")
print("covert to list to a set")   #it will not directly accept list where as it accept tuples
print("--------------------------")
# the below code should work, I am not sure why it is throwing an error
my_list = [2,3,1]
print(my_list)
#my_set1 = set(my_list)
#print(my_set1)

#UNION | INTERSECTION | DIFFERENCE

A = {1,2,3,'A','B','C'}
B = {3,4,5,'C','D','E'}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)
print(B - A)

print(A.symmetric_difference(B))
print(A ^ B)
