#Asignaturas de un estudiante

"""
materia = []
calificacion = []
estudiante, semestre = input("Ingrese el nombre del estudiante: "), input("Ingrese el semestre del estudiante")
"""

materia = []
estudiantes = []
op = 1
while op!=0:
    op = int(input(f"\
    Opciones\n \
    1.-Registrar estudiante\n \
    2.-Mostrar estudiantes\n \
    3.-Salir\n \
    Eliga una opcion---> "))
    if op == 1:
        estudiante, semestre = input("Ingrese el nombre del estudiante: "), input("Ingrese el semestre del estudiante: ")
        rango = int(input("¿Cúantas materia tendra la carga academica? --> "))
        for i in range(rango):
            materia.append(input("Ingresa la materia a asignar: "))
        alumno = {"Nombre":estudiante,"Semestre":semestre,"Materias":materia}
        estudiantes.append(alumno)
    elif op==2:
        print(f"Estudiantes con carga academica: \n{estudiantes}")