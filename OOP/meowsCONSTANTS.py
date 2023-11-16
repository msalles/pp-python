# las constantes se manejan como constantes de clase
# y se manejan en mayúsculas por convención

""" 
Se utiliza esta notación para hacer los docstrings, la
info de tu programa
"""
        
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()

