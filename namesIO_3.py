
# Version clara    

# with open("names.csv") as file:
    # for line in file:
        # row = line.rstrip().split(",")     # corta y separa en cada coma
        # print(f"{row[0]} is in {row[1]}")


# version que almacena en variables distintas

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")     # corta, separa en cada coma y almacena en cada variable
        print(f"{name} is in {house}")

