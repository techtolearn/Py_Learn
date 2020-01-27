#https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=21
'''
Python Tutorial: Sorting Lists, Tuples, and Objects
'''

#List sorting

from operator import attrgetter

li = [9,3,1,6,5,8,0,7,4,2]

s_li = sorted(li)
print("Sorted list using sorted function : ",s_li)
s_li = sorted(li,reverse=True)
print("Sorted list using sorted function : ",s_li)
print("\n")
li.sort()
print("Sorted list sorted method without variable: ",li)
li.sort(reverse=True)
print("Sorted list sorted method without variable: ",li)
print("\n")

# tuple sorting using only sorting funtion and no sort method availble
tub = [9,3,1,6,5,8,0,7,4,2]
s_tup = sorted(tub)
print("Sorted tuple using sorted function : ",s_tup)
s_tup = sorted(tub,reverse=True)
print("Sorted tuple using sorted function : ",s_tup)
print("\n")


# Dictionary sorting using only sorting funtion and no sort method availble and it sorts only key
student  ={'name': 'Supritha','age':22,'course':['computer Sci','Electronics']}

s_dic = sorted(student)
print("Dictionary sort: \t",s_dic)
s_dic = sorted(student,reverse=True)
print("Dictionary sort: \t",s_dic)
print("\n")

#sorting using abs key word for negative values

li = [9,3,1,-6,5,-8,0,7,-4,-2]
a_li = sorted(li)
print("Sorted list using sorted function : ",a_li)
a_li = sorted(li,key=abs)
print("Sorted list using sorted function : ",a_li)
print("\n")

class employees:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary =salary

    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)

e1 = employees('Satheesh',38,6798789)
e2 = employees('Prithesh',35,5344645)
e3 = employees('Anshuman',41,5378788)

employee = [e1,e2,e3] # created list for the variable before sort


# Method 1 use custom function
def emp_sort(emp):
    return  emp.name  #as you change the name,age or sal here, sort will act accordingly
emps = sorted(employee,key=emp_sort)
print(emps)
emps = sorted(employee,key=emp_sort, reverse=True)
print(emps)
print("\n")

# Method 2 using lamda key
emps1 = sorted(employee,key=lambda  e : e.name)
print(emps1)
print("\n")

# Method 3 using attrgetter method - from operator package improt attrgetter
empsAttr = sorted(employee,key=attrgetter('age'))
print(empsAttr)
