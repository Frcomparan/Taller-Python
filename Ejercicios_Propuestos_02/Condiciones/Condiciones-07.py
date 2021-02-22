#Ecuación de segundo grado
import math
def ecu_2do_grado():
    print("Ingresa los valores de la ecuacion de segundo grado, con formato: ax^2 + bx + c = 0")
    a = int(input("Ingresa el valor de [a] --> "))
    b = int(input("Ingresa el valor de [b] --> "))
    c = int(input("Ingresa el valor de [c] --> "))
    disc = (b**2)-(4*a*c)
    if a == 0 and b == 0 and c != 0:
        print("La ecuación ingresada no tiene solucion")
    elif a == 0 and b == 0 and c == 0:
        print("Todos los números son solucion")
    elif a == 0 and b != 0:
        result = (-c)/b
        print(f"El valor de la incognita es: {result}")
    elif disc>0:
        result1 = ((-b) + math.sqrt(disc))/(2*a)
        result2 = ((-b) - math.sqrt(disc))/(2*a)
        print(f"Hay dos soluciones: {result1} y {result2}")
    elif disc < 0:
        print("La ecuación no tiene solución real")
    else:
        result = -b/(2*a)
        print(f"Hay una unica solucion: {result}")

ecu_2do_grado()
    
 