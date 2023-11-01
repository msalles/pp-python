# para evitar el uso de muchos ifs se usa match

name = input("cual es tu nombre?: ")

match name:
    case "Harry" | "Hermione" | "Ron":    # el | equivale a un OR
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("¿Quién?")
