# pgm for add sub mult etc using fun

def add(a,b):
    c=a+b
    print(c)

def substraction(a,b):
    return(a-b)

def multiplcation(a,b):
    return(a*b)

def division(a,b):
    c=a/b
    print(c)


a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

print("substraction of " +str(a)+ " and " +str(b)+ " is :",substraction(a,b))
print("Multiplication of " +str(a)+ " and " +str(b)+ " is :",multiplcation(a,b))
print("\n")

i=5
def f(arg=i):
    print(arg)

i=6
f()
print("\n")
def  raise_power(base,num_power):
    result =1;
    for i in range(num_power):
        result=result * base
    return (result)


print(str(a) +" to the power "+str(b)+" of :",raise_power(a,b))
