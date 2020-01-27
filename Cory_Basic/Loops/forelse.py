'''
https://www.youtube.com/watch?v=Dh-0lAyc3Bc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=60
Else Clauses on Loops
'''

my_list = [1,2,3,4,5]
for i in my_list:
    print(i)
    if i == 5:
        break
else:
    print('Hit the for/Else statiement!')
print('\n')

def  find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value == target:
         break
    else:
        return -1
    return i

my_list = ['Tanvi','Satheesh','Divya']
indx_location = find_index(my_list,'Divya')
print('Location of the target index is {} '.format(indx_location))
