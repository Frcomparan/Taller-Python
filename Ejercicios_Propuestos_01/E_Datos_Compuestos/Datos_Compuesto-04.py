lista = []
for i in range(1,11):
    lista.append(i)

print(f"Lista original: {lista}")

for i in lista[-1:-11:-1]:
    if i == 1:
        print(i)
    else:
        print(f"{i}", end=", ")