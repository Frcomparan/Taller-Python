import math


figuras = []


def main():
    op = 1
    while op != 0:
        op = int(input("\nOpciones: \n \
            1.- Crear figura \n \
            2.- Listar una clasificacion de figuras\n \
            3.- Listar todas las figuras \n \
            4.- Mostrar la suma de todas las area \n \
            5.- Mostrar la suma de todos los perimetros \n \
            6.- Limpiar lista \n \
            0.- Salir \n \
            Elige una opcion ---> "))
        if op == 1:
            op2 = int(input("\nOpciones: \n \
            1.- Crear un cuadrado \n \
            2.- Crear un triangulo\n \
            3.- Crear un circulo \n \
            Elige una opcion ---> "))
            if op2 == 1 or op2 == 2 or op2 == 3:
                menu_figuras(op2)
            else:
                print("Ingreso una opción invalida")

        elif op == 2:
            buscar = input("¿Qué figura deseas revisar? ")
            buscar = buscar.capitalize()
            ver1 = buscar == "Cuadrado" or buscar == "Triangulo" or buscar == "Circulo"
            if ver1:
                if buscar == "Triangulo":
                    tipo = input("¿Qué tipo de triangulo buscas? ")
                    buscar += f" {tipo}"
                    print(buscar)
                listar_clasificacion(buscar)
            else:
                print("Ingreso una opcion de figura no valida")
        elif op == 3:
            imprimir()
        elif op == 4:
            sumador_areas()
        elif op == 5:
            sumador_perimetro()
        elif op == 6:
            figuras.clear()
            print("La lista ha sido vaciada")
        elif op == 0:
            print("Cerrando.....")
        else:
            print("Ingreso una opción invalida")


def dimesiones_validas(l1,l2,l3):
    if l1 > l2 and l1 >l3:
        return ((l2 + l3) >l1)
    if l2 > l1 and l2 >l3:
        return ((l1 + l3) >l2)
    if l3 > l2 and l3 >l1:
        return ((l2 + l1) >l3)

def menu_figuras(op2):
    if op2 == 1:
        lado = float(input("Ingresa la medida del lado del cuadrado: "))
        new = crear_cuadrado(lado)
        figuras.append(new)
        print("Cuadrado creado")
    if op2 == 2:
        lado1, lado2, lado3 = float(input("Ingresa la medida del primer lado: ")), float(input(
            "Ingresa la medida del segundo lado: ")), float(input("Ingresa la medida del tercer lado: "))
        if dimesiones_validas(lado1,lado2,lado3):
            new = crear_triangulo(lado1, lado2, lado3)
            figuras.append(new)
            print("Triangulo creado")
        else:
            print("Las dimensiones ingresadas no son validas")
    if op2 == 3:
        radio = float(input("Ingresa el radio del circulo: "))
        new = crear_circulo(radio)
        figuras.append(new)
        print("Circulo creado")



def imprimir():
    for i in range(len(figuras)):
        print(f" \
        Figura {i+1}: \n \
        {figuras[i]}")


def sumador_areas():
    sum_ar = 0
    for i in figuras:
        sum_ar += i['area']
    print(f"La suma de todas las areas es: {sum_ar}")


def sumador_perimetro():
    sum_per = 0
    for i in figuras:
        sum_per += i['perimetro']
    print(f"La suma de todas los perimetros es: {sum_per}")


def listar_clasificacion(buscar):
    c = 0
    for i in figuras:
        if i['tipo'] == buscar:
            print(i)
        else:
            c += 1
    if c == (len(figuras)):
        print("No hay figuras relacionadoas con la clasificacion de figuras")


def crear_cuadrado(lado):
    area = lado**2
    per = lado * 4
    new_cuadrado = {"tipo": "Cuadrado", "area": area, "perimetro": per}
    return new_cuadrado


def crear_triangulo(lado1, lado2, lado3):
    per = lado1 + lado2 + lado3
    tipo = ""
    area = 0
    altu = 0
    if lado1 == lado2 == lado3:
        tipo = "Triangulo equilatero"
        altu = ((lado1)*(math.sqrt(3)))/2
        area = (lado1 * altu)/2
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        tipo = "Triangulo isosceles"
        if lado1 == lado2:
            altu = math.sqrt((lado1**2)-(lado3**2)/(4))
            area = (lado3*altu)/2
        elif lado1 == lado3:
            altu = math.sqrt((lado1**2)-(lado2**2)/(4))
            area = (lado2*altu)/2
        else:
            altu = math.sqrt((lado2**2)-(lado1**2)/(4))
            area = (lado1*altu)/2
    else:
        tipo = "Triangulo escaleno"
        sp = (lado1+lado2+lado3)
        area = math.sqrt(sp*(sp-lado1)*(sp-lado2)*(sp-lado3))
    new_triangulo = {"tipo": tipo, "area": area, "perimetro": per}
    return new_triangulo


def crear_circulo(radio):
    area = (math.pi)*(radio**2)
    perimetro = (math.pi)*(radio)
    new_circulo = {"tipo": "Circulo", "area": area, "perimetro": perimetro}
    return new_circulo


main()
