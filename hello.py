# Preguntar al usuario su nombre y saludarlo

nombre = input("¿Cómo te llamas? ")

# Remueve espacios en blanco izq y der de la variable string
nombre = nombre.strip()

# Capitaliza la variable string
nombre = nombre.capitalize()

# Capitaliza todos los inicios de la variable string
nombre = nombre.title()

# hace lo mismo pero en una sola línea
nombre = nombre.strip().title()

#Se puede hacer TODo en una sola línea:
# nombre = input("¿Cómo te llamas? ").strip().title()


print("hola,", nombre)
print(f"hola, {nombre}")
