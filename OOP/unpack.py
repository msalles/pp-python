def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(*coins), "Knuts")
print(total(**coins2), "Knuts")

"""
El asterisco a coins hace el unpacking de la lista para pasar los argumentos a total
Se ejemplifica en lista (coins) y en diccionario (coins2)
"""
