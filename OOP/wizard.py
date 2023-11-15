
# Una clase (Wizard: la super clase) de la cual se hereda en otras clases
# Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name


    ...



class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Griffindor")
professor = Professor("Severus", "Defense Against The Dark Arts")
