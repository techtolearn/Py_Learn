# https://www.youtube.com/watch?v=QVdf0LgmICw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=18

'''
 LEGB - Local,Enclosed,Global and Builtin variables
'''

# Example 1 for Identify local and global
y= 'global y'
def test():
    x='local x'
    print(x)

test()
print(y)
print("\n")

# Example 2 for Identify local and global when variable name same

x = 'global y'

def test():
    x='local x'
    print(x)

test()   #this will call x from test method
print(x)  #this will get it from class variable
print("\n")


# Example 2 for Identify local and global when global variable set in any of  test function inside the class
x = 'global y'

def test():
    global x   # here it will use the global variable name to set (overriding)the local value, here both local and global will have the local value
    x='local x'
    print(x)

test()      # this will call x from test method
print(x)    # this will get it from class variable
print("\n")

''' 
Example of Built in functions
'''

# nested function

def outerFun():
    x = 'outer x'
    def innerFun():
        x = 'inner x'
        print(x)
    innerFun()    # when call this function it will go call the Inner values
    print(x)  #we are still printing outer function call values and then we call the outer function
outerFun()


#enclosing scope
print("\n")
def outerFun():
    x = 'outer x'
    def innerFun():
        #x = 'inner x'
        print(x)  # this will print the global variable value from inside function as there is no loacal value
    innerFun()
    print(x)
outerFun()


#enclosing scope  - nonlocal  will be used to set global var locally but actual global variable will not be changed
print("\n")
def outerFun():
    x = 'outer x'
    def innerFun():
        nonlocal  x
        x = 'inner x'
        print(x)  # this will print the global variable value from inside function as there is no loacal value
    innerFun()
    print(x)
outerFun()


#enclosing scope  -  innner function behaviors
'''
Here when inner function looks for value from its body, since it didn't find, it gives priority to immidiate x values which is
outer function x variable value, again if it doesn't find outer also, then it look for next immidadiate variable function value or 
global value finally
'''

print("\n")
x = 'global x'
def outerFun():
    x = 'outer x'
    def innerFun():
        nonlocal  x
        #x = 'inner x'
        print(x)  # this will print the global variable value from inside function as there is no loacal value
    innerFun()
    print(x)
outerFun()
print(x)
