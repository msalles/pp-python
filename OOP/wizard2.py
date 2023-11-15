# Una clase (Wizard: la super clase) de la cual se hereda en otras clases
# Inheritance

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def ___str___(self):
        