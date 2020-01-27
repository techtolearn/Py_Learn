# https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=36
'''
Generators - How to use them and the benefits you receive
Generator will not hold any value while printing hence it is good for performance
'''

def Square_number(nums):
    result = []
    for n in nums:
        result.append(n*n)
    return result

sqare = Square_number([1,2,3,4,5])
print(sqare)
print("\n")

#example of using yield generator

def square_yield(num):
    for i in(num):
        yield (i*i)   # yield will not hold any value it will print one by one

sqare = Square_number([1,2,3,4,5])
for num in sqare:
    print(num)

print("\n")
# using  list comprhensive method
my_num = (x*x for x in [1,2,3,4,5])
print(list(my_num))


print("\n")
# using list comprhensive method
my_num = [x*x for x in [1,2,3,4,5]]
print(my_num)
# or
for num in my_num:
    print(num)
