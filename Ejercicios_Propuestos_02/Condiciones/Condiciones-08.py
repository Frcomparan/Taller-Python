#Calcular area de Triangulo o circulo
import math
def ar_triangulo(b,a):
    area = (b*a)/2
    return area

def ar_circulo(rad):
    area = (math.pi)*(rad**2)
    return area

def areas():
    do = input("¿Qué quieres hacer?\n1.-Calcular el área de un triángulo [T/t]\n2.-Calcular el área de un circulo [C/c]\nElige una opcion ---> ")
    if do=="T" or do =="t":
        a = float(input("Ingresa la altura del triángulo --> "))
        b = float(input("Ingresa la base del triángulo --> "))
        print(f"El área del triángulo es: {ar_triangulo(a,b)}")
    elif do=="C" or do == "c":
        rad = float(input("Ingresa el radio del circulo --> "))
        print(f"El área del circulo es: {ar_circulo(rad)}")
    else:
        print("Ha ingresado un valor no valido")

areas()
