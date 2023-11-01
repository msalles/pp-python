
# esto es lo mismo que el de abajo y sirve para seguir el loop hasta
# que el usuario ponga la respuesta que le estas pidiendo

# while True:
#    n = int(input("¿Cuantas veces? "))
#    if n < 0:
#       continue
#    else:
#        break

while True:
    n = int(input("¿Cuantas veces? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


