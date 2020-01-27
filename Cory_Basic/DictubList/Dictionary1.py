'''
https://www.youtube.com/watch?v=qmWCT_OgrKQ&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=7
dictionary are non sequential means it will not display the values same order everytime
'''


customer =[]

while True:
     createEntry = input('Enter customer (yes/no) : ')
     createEntry = createEntry[0].lower();  #this is not required but it is better to avoid case

     if createEntry == 'n':
         break
     else:
         fname,lname = input('Enter customer name : ').split()
         customer.append({'fname':fname, 'lname':lname})

for cust in customer:
    print(cust['fname'],cust['lname'])
    
