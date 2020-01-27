class person(object):
    def __init__(self, name):
         self.name = name
    def reveal_Identity(self):
        print('My name is : {}'.format(self.name))

class superMan(person):
    def __init__(self,name,heroname):
        super(superMan,self).__init__(name)
        self.heroname = heroname
    def reveal_Identity(self):
        super(superMan,self).reveal_Identity()
        print("...And I am {}".format(self.heroname))


NameofPerson = person('Satheesh')
NameofPerson.reveal_Identity()
print('\n')
superhero = superMan("Tanvi","satheesh")
superhero.reveal_Identity()
