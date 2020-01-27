#https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4

print("The below programs are example of List")
print("**************************************")
course =['Zoology','Physics','Electronics','ComputerSci','Chemistry']
print(course)
print(course[0])
print(course[0:2])
print(course[-1])
print('\n')

#append,insert and extend

course.append('DataScience')
print(course)
print('\n')
course.insert(1,'MatheMetics')
print(course)
print('\n')
course2 = ['History','Econoics']
course.insert(0,course2)
print(course)   #it will create list of list, to avoid this we use the extend classmethod
print('\n')
course.extend(course2)
print(course)
print('\n')

#remove items
course.remove(course2)
print(course)
print('\n')
deletedVal =course.pop()   #it works like stack.. will remove from the last
print(course)
print(deletedVal)

print('\n')
course.reverse()
print(course)
print('\n')
course.sort()  #ascending order
print(course)
print('\n')
course.sort(reverse=True)   #Desending order
print(course)
print('\n')
sorted(course)    #another method of descending order
print(course)
print('\n')
sorted_course = sorted(course)    #another method of ascending order
print(sorted_course)

print("\n")
print(course.index('Physics'))

print("\n")
print('Art' in course)   #if else condition

print("\n")
for sub in course:
    print(sub)
print("\n")

for index,sub in enumerate(course):  #enumerate will print the index of each item
    print(index,sub)
print("\n")

for index,sub in enumerate(course, start=1):  #enumerate will print the index of each item and will start from index 1
    print(index,sub)

print("\n")
course_str = ','.join(course)   #it will join the coma(you can mention anything, it will join alon with string and print) seperated values and print
print(course_str)

print("\n")
course_str = ','.join(course)   #it will join the coma(you can mention anything, it will join alon with string and print) seperated values and print
new_Str = course_str.split(',')  #it will return back to original list
print(new_Str)


print("*********List are mutable*****************")
print("==========================================")

list1  = ['Mandya','Mysore','Bangalore','Mangalore']
list2 = list1

list1[0] = 'Mclean'   #it will replace Mandya as Mclean in both list1 and list 2
print(list1)
print (list2)
