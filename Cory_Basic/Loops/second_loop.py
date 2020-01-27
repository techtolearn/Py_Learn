#program to write loops

#1.while loop

a,b,c = 0,1,1
while(a<10):
    print(a)
    a=b
    b=c
    c=a+b

print("\n")

#2. if and else

n=10
if n < 0:
    print(str(n)+" is negative number")
elif n > 0:
    print(str(n)+" is positive number")
else:
    print(str(n)+" is zero number")
print("\n")

#3. for loop

words = ['lion','Tiger','Elepant','Eagle']
for w in words:
    print(w+ " word length is :", str(len(w)))

print("\n")
#for loop using eg1 : range

for i in range(6):
    print(i)

print("\n")
#for loop using eg2 : range(a,b)

for i in range(2,8):
    print(i)


print("\n")
#for loop using eg3 : range(a,b,c) - will add 3 to each iteration till result reaches 10

for i in range(0,10,3):
    print(i)
print("\n")
for i in range(-10,-100,-30):
    print(i)
print("\n")

#using list and range   - print the number 0 to 9
print(list(range(9)))
print("\n")

#range using for loop-Loop statements may have an else clause

for n in range (2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n, " equals",x,'*' ,n//x)
            break
    else:
        print(n,"is prime number")
print("\n")
#for range and continue
for i in range(2,10):
    if i%2 == 0:
        print(i, "is even number")
        continue
print("no more than odd number found")


#function
print("\n")
def fib(n):

    a,b,c = 0,1,1
    while(a<n):
        print(a,end=' ')  #print same line
        a=b
        b=c
        c=a+b

fib(10)

print("\n")
# accessing array list
numbers =[[1,2,3],[4,5,6], [7,8,9], [0]]
print(numbers[1][1])
print("\n")

print(numbers[1][0])
print('\n')

for row in numbers:
    print(row)

print('\n')
for row in numbers:
    for col in row:
         print(col)

#translaton with letter
def translationLeter(phrase):
    translation = ' '
    for letter in phrase:
        if letter in 'AEIOUaeiou':
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translationLeter(input("Enter the phrase: ")))
