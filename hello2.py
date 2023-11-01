def hello2(to="world automatico"):
    print("hello,", to)


hello2()
nombre = input("¿Cómo te llamas? ")
hello2(nombre)

"""
el parámetro entrecomillado en la funcion es asignado
por default a world, y si se manda un argumento para 
el parámetro desde el programa entonces 
la función usa el parámetro asignado.
"""
