#https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2


greeting ="Hello"
name =  "Satheesh"
message = '{}, {}.welcome to Python course!!'.format(greeting,name)
message1 = f'{greeting}, {name}.welcome to Python course!!'
message2 =  greeting +', '+name.upper()+'.welcome to Python course!!'
print(message)
print(message1)
print(message2)
print("\n")
print(len(message))
print("\n")
name = name.replace("Satheesh","Tanvi")
print(message1)
print(name)
print(name.upper())
print(name.lower())
print(name[0:2])
print(name[3:])
print(name[:3])
print('\n')
Name = 'Hello world'
print(Name.count('Hello'))   #here it count the word
print(Name.count('l'))      #here it count single char
print('\n')
Name = Name.find('world')   #tells the position which start from
print(Name)

print('\n')
print(dir(name))  #system will tell you that how method are being used

#use full to find the sysntax for each function for the givin string var
print('\n')
print(help(str))   #it will give all systanx
print('\n')
print(help(str.lower))   #it will give the spcific syntax for the defined method for given string
