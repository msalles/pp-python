# Una clase (Wizard: la super clase) de la cual se hereda en otras clases
# Inheritance

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def ___str___(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts}, Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 20)
print(potter)

weasley = Vault(50, 30, 10)
print(weasley)

total = potter + weasley
print(total)
