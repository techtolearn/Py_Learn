'''
https://www.youtube.com/watch?v=02edODXdHgs&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=3
lower case value [a-z  97 to 122  so we have to converting add and substract 23 so it will handle both upper and lower
upper case value [A-Z  65 -90
'''
normal_string = input("enter the string in Upper case : ")

scret_string = ''
for char in (normal_string):
    scret_string+=str(ord(char) - 23)
    print(scret_string)
print(scret_string)

normal_string=''
for i in range(0,len(scret_string)-1,2):  # it takes only 2 two char
    char_code = scret_string[i] + scret_string[i+1]
    #print(char_code)
    normal_string += chr(int(char_code)+ 23)
print(normal_string)

