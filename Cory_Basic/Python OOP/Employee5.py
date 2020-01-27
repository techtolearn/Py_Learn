#Ref : https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
#program to write getter and setter method

class employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first+'.'+last+'@gmail.com'

    @property   #getter method
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property   #this is getter and we get the value of email so we no need to use the emp1.email() -will remove bracess
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name!!')
        self.first = None
        self.last = None




emp1 =employee("Tavi","satheesh",5412000)
emp1.fullname = 'Satheesh kumar'


print(emp1.email)

#to set the value of new fullname  use the setter method

print(emp1.fullname)
del emp1.fullname
