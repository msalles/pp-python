
# ESCRIBIR sobre un archivo

name = input("What's your name? ")

# modo para entender
# file = open("names.txt", "a")      # crea el archivo y escribe sobre él añadiendo ("w" si quieres hacerlo todo nuevo cada vez que corras el programa)
# file.write(f"{name}\n")                # escribe el nombre capturado en el archivo
# file.close()                    # cierra el archivo

with open("names.txt", "a") as file:      # "with" se encarga de abrir y cerrar el archivo
    file.write(f"{name}\n")
