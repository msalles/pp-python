
# Forma simple
try:
    x = int(input("da el valor de x "))
    print(f"x vale {x}")
except ValueError:
    print("x NO es un número entero")


# Mejor forma
try:
    x = int(input("da el valor de x "))
except ValueError:
    print("x NO es un número entero")
else:
    print(f"x vale {x}")

# La mejor forma es hacer el loop para no salir del programa

while True:
    try:
        x = int(input("da el valor de x "))
    except ValueError:
        print("x NO es un número entero")
    else:
        break

print(f"x vale {x}")


# Si voy a captar muchas entradas del usuario, lo convertimos en función

def main():
    x = get_int()
    print(f"x vale {x}")


def get_int():
    while True:
        try:
            x = int(input("da el valor de x "))
        except ValueError:
            print("x NO es un número entero") # se puede poner el comando pass en lugar de esto
        else:
            break
    return x


main()
