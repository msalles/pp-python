
# Lo mismo que student2 pero mejorado, checa errores (encapsula)    
# se usa "raise" para crear nuestras propias excepciones sin salir del programa


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name!!!")
        if house not in (["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]):
            raise ValueError("Invalid House!")
        self.name = name
        self.house = house
        self.patronus = patronus


    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "Stag":
                return "##"
            case "Otter":
                return "@@"
            case "Jack Russell terrier":
                return "!!"
            case _:
                return "Sin patronus"


def main():
    student = get_student()
    print(student)           # este cambio sirve con la nueva funcion str


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()