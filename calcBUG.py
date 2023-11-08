def main():
    x = int(input("What is x "))
    print("x squared is", square(x))

def square(n):
    return n + n

if __name__ == "__main__":
    main()

# la función square está mal porque tiene suma y no multiplicar.
# Es intencional para probar pytest en el programa que hicimos para checar
# que es test_calcBUG.py
