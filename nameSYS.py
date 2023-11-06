import sys

# se espera que el usuario escriba su nombre desde línea de comandos al 
# invocar el programa

if len(sys.argv) < 2:
    sys.exit("argumentos insuficientes")
elif len(sys.argv) > 2:
    sys.exit("demasiados argumentos")

print("hola, mi nombre es", sys.argv[1])
