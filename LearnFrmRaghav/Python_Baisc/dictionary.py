#dictionary{K,V} unordered|Changable|indexed|no duplicate

my_dict ={
    "class" : "Computer Science",
    "Name"  : "Supritha",
    "Place" : "Banaglore",
    "Age"   : 21
}
print(my_dict)
print("\n")

print(my_dict["Name"])
print(my_dict.get("Name"))
print(my_dict.values())
print("\n")

for x in my_dict:
    print(my_dict[x]) #accessing values
print("\n")

for x,y in my_dict.items():  #accessing both key and values
    print(x," : ",y)
print("\n")

my_dict["Place"] = "Mysore"   #update dictionary
print(my_dict)

my_dict["Qualification"] = "Engineering"
print(my_dict)


my_dict.pop("Qualification")
print(my_dict)

my_dict.popitem()  #remove last item default
print(my_dict)

del my_dict["Place"]
print(my_dict)

my_dict.clear()
print(my_dict)


