# Lo mismo que student3 pero mejorado, checa errores (encapsula)    


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    

def main():
    student = Student.get()
    print(student)           # este cambio sirve con la nueva funcion str


if __name__ == "__main__":
    main()