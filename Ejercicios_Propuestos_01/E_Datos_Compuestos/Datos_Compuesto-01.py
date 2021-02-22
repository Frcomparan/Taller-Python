import random
import math

lista = []
for n in range(0, 15):
    lista.append(random.randrange(0, 100))


print(f"Lista original: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")

par, impar = [], []

for i in lista:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"\nLista de números pares: {par}")
print(f"Lista de números impares: {impar}")