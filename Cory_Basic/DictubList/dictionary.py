#https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5
#working with key and values

student  ={'name': 'Supritha','age':22,'course':['computer Sci','Electronics']}
student['phone'] = 9865654231   #singel key update
student['name'] = 'Harstha'

student.update({'name': 'Shobitha','age':18,'course':['Physics','Chemistry']})  #update all at once
#both will perform the same action
print(student['name'])
print(student.get('name'))
print("\n")
# if the key value is not found
# print(student['phone'])  #it will throw error
print(student.get('phone'))  # it will simply print as none
print(student.get('phone','Values not found'))
print("\n")


#del student['age']
print(student)
print("\n")

#capture deleted value
age = student.pop('age')

print(student)
print(age)

#lenth of the keys
print("\n")
print(len(student))
print(student.keys())
print(student.values())
print(student.items())  #will print both key and values

print("\n")
#for loop to print the item
for key,val in student.items():
    print(key,val)

