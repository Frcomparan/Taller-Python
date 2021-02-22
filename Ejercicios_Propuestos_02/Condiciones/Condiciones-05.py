#Verificar 3 numeros

def ver_numeros():
    n1 = int(input("Ingresa un número ----> "))
    n2 = int(input("Ingresa un número ----> "))
    n3 = int(input("Ingresa un número ----> "))

    if n1 == n2 == n3:
        print("Los tres números ingresados son iguales")
    elif (n1 == n2 or n1 == n3 or n2 == n3):
        if n1 == n2:
            print(f"Ingresaste dos números iguales, numero repetido: {n1}")
        elif n1 == n3:
            print(f"Ingresaste dos números iguales, numero repetido: {n1}")
        else:
            print(f"Ingresaste dos números iguales, numero repetido: {n2}")
    else:
        print("Ninguno de los números ingresados son iguales")


ver_numeros()