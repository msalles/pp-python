def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(3)


def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        for j in range(size):      # for del renglón, por eso se pone el print al finalizar
            print("#", end="")
        print()


main()
