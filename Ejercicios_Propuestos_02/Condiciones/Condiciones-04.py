#Multiplis

def multiplo():
    n1 = int(input("Ingresa un número---> "))
    n2 = int(input("Ingresa un número---> "))
    if n1 < n2:
        if n2%n1==0:
            print(f"\n{n1} es multiplo de {n2}")
        else:
            print(f"\n{n1} no es multiplo de {n2}")
    elif n1 > n2:
        if n1%n2==0:
            print(f"\n{n2} es multiplo de {n1}")
        else:
            print(f"\n{n2} no es multiplo de {n1}")
    else:
        print(f"\nIngreso dos números iguales: {n1}")
multiplo()