def main():
    x = int(input("Da el valor de x: "))
    if es_par(x):
        print("el valor de x es PAR")
    else:
        print("el valor de x es IMPAR")

def es_par(n):
    return True if n % 2 ==0 else False
    # se puede tambien escribir solamente como: return n % 2 == 0

main()