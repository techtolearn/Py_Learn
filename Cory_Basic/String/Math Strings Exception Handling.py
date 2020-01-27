'''https://www.youtube.com/watch?v=02edODXdHgs&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=3
'''

#exception handling
while True:

    try:
        number = int(input('Enter the number : '))
        break
    except ValueError:
        print("you didn't enter the number")

    except:
        print("please enter the number")

print("Awesome! you enter the nmber is {} ".format(number))
