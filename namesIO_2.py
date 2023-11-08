
# LEER de un programa


# version 1 (lees y luego haces iteración)
# with open("names.txt", "r") as file:        # lee todas las lineas del archivo
    # lines = file.readlines()
# for line in lines:
    # print("hello", line.rstrip())

# version 2 (todo en uno)
# with open("names.txt", "r") as file:
    # for line in file:
        # print("Hello,", line.rstrip())


# version3 (lee y ordena según un orden al imprimir)
# names = []

# with open("names.txt") as file:
    # for line in file:
        # names.append(line.rstrip())

# for name in sorted(names):
    #print(f"Hello, {name}")



# version 4, lo mismo que version 3 pero más compacto
names = []

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())

