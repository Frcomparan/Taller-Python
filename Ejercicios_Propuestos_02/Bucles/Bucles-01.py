# Lectura y clasificación de números

def class_numero():
    lista, suma = [], 0
    for i in range(6):
        n = int(input("Ingresa un número --> "))
        lista.append(n)
        suma += n
    for i in lista:
        if i % 2 == 0:
            print(f"{i} es número par", end=" y ")
            c = 0
            for j in range(i):
                if i % (j+1) == 0:
                    c += 1
            if c == 2:
                print("es número primo")
            else:
                print("no es número primo")
        else:
            print(f"{i} es número impar", end=" y ")
            c = 0
            for j in range(i):
                if i % (j+1) == 0:
                    c += 1
            if c == 2:
                print("es número primo")
            else:
                print("no es número primo")
    return f"La suma de los números ingresados es: {suma}"


print(class_numero())
