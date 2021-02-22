# Ingresar números e identificar si son mayores al primer # ingresado

def ingresar():
    tam = int(input("¿Cuántos números deseas ingresar? "))
    lista = []
    for i in range(tam):
        num = int(input("Ingresa un números --> "))
        lista.append(num)
        if lista[0] > num:
            print(
                f"El número ingresado es menor al primer elemento: \"{lista[0]}\"")
    print(f"Lista ingresada: \n{lista}")


ingresar()
