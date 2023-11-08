
# Lo mismo que que el 4 pero utilizando el módulo de CSV de python
# Esta es la MEJOR VERSION porque protege el código

import csv

students = []
    
with open("names2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: ["name"]):
    print(f"{student['name']} is in {student['home']}")

