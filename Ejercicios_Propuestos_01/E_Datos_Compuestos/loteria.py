#Preguntar numeros de loteria al usuario

numero_ganadores = []
for i in range(6):
    numero_ganadores.append(int(input("Ingresa el primer numero ganador: ")))

numero_ganadores.sort()
print(f"Los números ganadores son: {numero_ganadores}")