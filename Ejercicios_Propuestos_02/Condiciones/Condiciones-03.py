#Número mayor, menor o igual

def mayor_o_menor():
    n1 = int(input("Ingresa un número---> "))
    n2 = int(input("Ingresa un número---> "))
    if n1 < n2:
        print(f"\n{n1} es menor a {n2}")
    elif n1 > n2:
        print(f"\n{n1} es mayor a {n2}")
    else:
        print(f"\nIngreso dos números iguales: {n1}")

mayor_o_menor()