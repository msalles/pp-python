students = ["Harry", "Hermione", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

gryffindors2 = {student: "Gryffindor" for student in students}

print("Se ha creado una lista de diccionarios a partir de students")
print(gryffindors)
print()
print("se ha creado un diccionario a partir de students")
print(gryffindors2)


"""
en gryffindors: Para tener una lista de diccionarios
en gryffindors2 tengo un solo diccionario se usa Dict Comprehension
"""