#https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4
#Tuble can not be modified where list can ,hence list is non mutable
print("The below programs are example of Tuple")
print("**************************************")
#not it will perform all the action as we performed in list except modification or append

# print("*********List are mutable*****************")
# print("==========================================")
# list1  = ('Mandya','Mysore','Bangalore','Mangalore')
# list2 = list1
# list1[0] = 'Mclean'   #it will not replace Mandya as Mclean in both list1 and list 2 in tuple
# print(list1)
# print (list2)


print("The below programs are example of set")
print("**************************************")
list1  = {'Mandya','Mysore','Bangalore','Mangalore'}
print(list1) #unlike  tuple and list, it doesn;t keep the order of list, it keeps change the position of string for each exection

list1  = {'Mandya','Mysore','Bangalore','Mangalore','Mandya'}
print(list1)  # it will automatically skip the duplicate

print("\n")
list2  = {'Mandya','Mysore','Belgaum','Mangalore','Darawada'}

print(list1.intersection(list2))   #print common elements between two sets
print(list1.difference(list2))   #print the difference of list 1
print(list1.union(list2))       #print the not common element


print("\n")
print("Empty list creation using list,tuple and set")

empt_list = []
empt_list = list()


empt_tuple = ()
empt_tuple =tuple()

empt_set = {}
empt_set = set()
