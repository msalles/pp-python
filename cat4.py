def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Da el valor de n "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
