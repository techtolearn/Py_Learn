#program write function inside the class

class Stud_Fun:
    def __init__(self,firstname,major,gpa):
        self.firstName = firstname
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa == 3.2:
            return True
        else:
            return False


