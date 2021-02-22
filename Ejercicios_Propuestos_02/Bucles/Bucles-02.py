# Divisores de un número

def divi():
    num = int(input("Ingresa un número entero --> "))
    divisores = []
    if num > 0:
        for i in range(num):
            if num % (i+1) == 0:
                divisores.append((i+1))
        print(f"Los divisores de \"{num}\" son {divisores}")
    else:
        print("Ingreso un número invalido")


divi()
