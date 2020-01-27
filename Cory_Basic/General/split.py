'''
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt
'''
# note while entering you have to give space between each entry
# num1,operator,num2 = input('enter the input with operator ? ').split()
# num1 = int(num1)
# num2 = int(num2)
#
# if operator == '+':
#     print('{} + {} = {}'.format(num1,num2,num1+num2))
# elif operator == '-':
#     print('{} - {} = {}'.format(num1,num2,num1-num2))
# elif operator == '*':
#     print('{} * {} = {}'.format(num1,num2,num1*num2))
# elif operator == '/':
#     print('{} / {} = {}'.format(num1,num2,num1/num2))
# else:
#     print('Invalid operator')


# Example 2  using eval - will convert user input into integer

# num = input('enter the age')
# print(type(num))
# print('\n')
# num = eval(input('enter the age'))
# print(type(num))


#Exampl3 Rounding the number

num = input('Enter the Float number :  ')
num = float(num)
print('Rounding of given {} is  : {:.2f}'.format(num,num))


