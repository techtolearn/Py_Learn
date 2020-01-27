'''
https://www.youtube.com/watch?v=qmWCT_OgrKQ&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=7
'''
def factorial(num):

    if num<=1:
        return 1
    else:
     result = num * factorial(num -1)
     print (result)
     return result

print('4! = ',factorial(4))


def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        result = fib(n-1)+fib(n-2)
    return  result

numFibValue = int(input('How many Fibonacci values you should found: '))
i=1
while i< numFibValue:
    fibValue = fib(i)
    print(fibValue)
    i+=1
print('all done')
