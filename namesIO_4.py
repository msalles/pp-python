
# lo mismo que version 3 pero ahora almacenados
# en una variable "students" para después ordenarlos
# Recordar que aquí sólo estamos leyendo de un archivo CSV, después escribiremos CSV


#Version clara

# students = []

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")     # corta, separa en cada coma y almacena en cada variable
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")



# Version simplificada

students = []
    
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")     # corta, separa en cada coma y almacena en cada variable
        student = {"name": name, "house": house}
        students.append(student)

# Ahora los vamos a ordenar primero
# Nótese que hacemos una gunción y llamamos a esa función dentro de otra función

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):            # se puede añadir ", reverse=True"
                                                          # se puede poner una función lambda en la key
                                                          # key=lambda student: ["name"]
                                                          # y borrar la función get_name completamente
    print(f"{student['name']} is in {student['house']}")



# Se puede cambiar fácilmente a que ordene por casas y no por nombres


# students = []
    
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")     # corta, separa en cada coma y almacena en cada variable
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house):            # se puede añadir ", reverse=True"
#     print(f"{student['name']} is in {student['house']}")

