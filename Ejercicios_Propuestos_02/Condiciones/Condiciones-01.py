#NÚMERO ENTERO
def div_exacta():  
    n1 = int(input("Ingresa un número: "))
    n2 = int(input("Ingresa otro número: "))
    red = n1%n2
    if  red == 0:
        print(f"La división entre {n1} y {n2} es exacta, residuo igual a: {red}")
    else:
        print(f"La división entre {n1} y {n2} no es exacta, residuo igual a: {red}")

div_exacta()
