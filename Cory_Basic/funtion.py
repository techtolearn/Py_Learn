#https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8
#Python Tutorial for Beginners 8: Functions

#method 1
def hello_fun():
    print("Hello world!!")
hello_fun()
print("\n")

#method 2
def hello_fun():
    return "Hello world!!"
print(hello_fun())
print(len(hello_fun()))
print(hello_fun().upper())
print(hello_fun().lower())
text = hello_fun().split(' ')
print(text,"\n")



#method 3
def hello_fun(greeting):
    return '{} world!!'.format(greeting)
print(hello_fun('Hello'),'\n')

#method 4
def hello_fun(greeting, name='Python'):
    return '{},{} world!!'.format(greeting,name)
print(hello_fun('Hello'),'\n')

#method 5
def hello_fun(greeting, name='Python'):
    return '{} world!! {}'.format(greeting,name)
print(hello_fun('Hello'),'\n')


#Method 6 example of Postion argument(args* means value) and keyword argument (**kwargs - means Key and value) like dictionay

def student_info(*args, **kwargs):
    print(args)
    print(kwargs,'\n')

student_info('Computer Sci','Scocialogy','History', name='Supritha',age='21',place='Bangalore')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs,'\n')
course = ('Computer Sci','Scocialogy','History')  # values should be in the form of Tuple - ()
student = {'name':'Supritha','age':'21','place':'Bangalore'}          # Key and values should follow dictionary sytax
student_info(*course, **student)


#exmpale to find the number of days of each month and including leap year

months =['0','31','28','31','30','31','30','31','31','30','31','30','31']
def is_leapYear(year):
    """ Returns True for leap years, False for non leap years"""
    return year % 4 ==0 and (year % 100 != 0 or year % 400 ==0)

def days_month(year,month):
    """ Retruns the number of days in that month in that year"""
    if not 1 <=  month <= 12:  # if 13 given then also should verify - not use the OR operator here
        print('Invalid month')

    if month ==2 and is_leapYear(year):
        return 29
    return(months[month])


print(is_leapYear(2020))
print(days_month(2020,2))

