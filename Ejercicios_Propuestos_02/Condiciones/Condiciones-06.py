#Calculor la solucion de una ecuacion de primer grado

def ecu_1er_grado():
    print("Ingresa los coeficientes de la ecuacion de primer grado [ax+b= 0]")
    a = int(input("Ingresa [a] --> "))
    b = int(input("Ingresa [b] --> "))
    if (a == 0) and (b != 0):
        print("La ecuacion no tiene solución")
    elif (a == 0) and (b == 0):
        print("Todos los son solución")
    else:
        result = (-b)/a
        print(f"El valor de la incognita es: {result}")

ecu_1er_grado()
