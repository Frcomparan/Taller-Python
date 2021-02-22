# Ingresar números, indicar el número mayor y menor de la lista así como la media aritmética de la misma

def ingreso():
    tam = int(input("¿Cuántos números deseas ingresar? "))
    lista, may, men, med = [], 0, 0, 0
    for i in range(tam):
        num = int(input("Ingresa un número --> "))
        med += num
        if num > may:
            may = num
        if i == 0:
            men = num
        if num < men:
            men = num
        lista.append(num)
    print(
        f"Lista ingresada: {lista}\nEl número mayor es: {may}\nEl número menor es: {men}\nLa media aritmética es: {med/tam}")


ingreso()
