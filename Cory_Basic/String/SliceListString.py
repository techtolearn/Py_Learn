# https://www.youtube.com/watch?v=ajrtAuDg3yw&index=19&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''

Slice the list and string
my_list[start:end:step]
'''


my_list = [0,1,2,3,4,5,6,7,8,9]

print(my_list[0])
print(my_list[0:9])
print(my_list[-10:-1])
print(my_list[2:])
print(my_list[:-2])

print("\n Slice example")
# slice  if you want to skip sum numbers  note: if start digit is positive then step value should also positve , if negative then it should negative
print(my_list[0:9:2])  # it means it will skip every after 2 digits
print(my_list[0:9:3])
print(my_list[0:-1:2])
print(my_list[-1:2:-1])
print(my_list[1:-2:1])
print(my_list[::-1])
print(my_list[::1])


# string slice
print("\n Slice String")
simple_url = 'https://wwww.google.com'  # again it will stored in index

#reverse string
print(simple_url[::-1])

#print .com only
print(simple_url[-4:])
print(simple_url[19:])
print(simple_url[len(simple_url)-4:])

print(simple_url[8:19])
print(simple_url[-15:-4])
print(simple_url[-15:-4:2])
