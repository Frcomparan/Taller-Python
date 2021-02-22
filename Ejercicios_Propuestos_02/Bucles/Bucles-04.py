# Calcular cantidad de números negativos ingresados

def negativo():
    tam = int(input("¿Cuántos números desea ingresar? "))
    lista, c = [], 0
    for i in range(tam):
        num = int(input("Ingresa un número --> "))
        lista.append(num)
        if num < 0:
            c += 1
    print(
        f"\nLista ingresada: {lista} \nEl total de números negativos ingresados es: {c}\n")


negativo()
