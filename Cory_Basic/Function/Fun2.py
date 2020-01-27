'''
https://www.youtube.com/watch?v=1Xa_iDqvg94&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=5
'''
#solve equation
#x+4 =9

def solve_eq(equation):
    x,add,num1,equal,num2 = equation.split()
    num1,num2 = int(num1),int(num2)
    return "x =  "+ str(num2 - num1)
print(solve_eq("x + 4 = 9"))
