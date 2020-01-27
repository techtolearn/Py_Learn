# https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=31
'''
Using Try/Except Blocks for Error Handling
'''
# Example-1
try:
    f =  open('text.txt')
except Exception as e:
    print(e)
print("\n")

# Example-2
try:
    f =  open('text.txt')
except FileNotFoundError :
    print("Sorry, File does not exist")
print("\n")

# Example-3
try:
    f =  open('test.txt')
    #var= bad_var
except FileNotFoundError :
    print("Sorry, File does not exist")
except Exception as e :
    print(e)
    print("\n")
else:
    print(f.read())
    f.closed
finally:  # this will execute irrespective exception or not to release resources such as database, memory
    print("executing code finally...!")

# example 4 - raise your own exceptions
try:
    f =  open('test.txt')
    if f.name == test.txt:
        raise Exception
except FileNotFoundError :
    print("Sorry, File does not exist")
except Exception as e :
    print("File is currupted!!")
print("\n")
