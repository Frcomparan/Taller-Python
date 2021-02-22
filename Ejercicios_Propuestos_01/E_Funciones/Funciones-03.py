# Relacion existente entre dos numero

num1 = 5
num2 = 10

def relacion(a,b):
    if a>b:
        return (f"{a} es mayor que {b} ---> 1")
    elif a<b:
        return (f"{a} es mayor que {b} ---> -1")
    else:
        return (f"{a} es igual a {b} ---> 0")

print(relacion(num1,num2))
print(relacion(num2,num1))
print(relacion(num1,num1))