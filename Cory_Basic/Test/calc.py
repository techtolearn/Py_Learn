'''
https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=57
Unit Testing Your Code with the unittest Module
'''


def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if (y==0):
        raise ValueError('Cannot divide by zero')
    return x / y
