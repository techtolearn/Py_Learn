# https://www.youtube.com/watch?v=CqvZ3vGoGs0&index=9&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
# Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library

print("importing.. my module")

test = 'Hello world'

def find_index(ListOfVal,searchval):
    for i,target in enumerate(ListOfVal):
        if target == searchval:
             return  'Searched values is found at the index['+ str(i) +'] is : '+searchval #we cannot directly concatenate string and int value hence we need to convert str(i)
    return -1;

