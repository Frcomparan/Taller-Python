#Calcular el dia siguiente con dia,mes,año con numeros enteros
def dia_siguiente_e():
    fecha = input(f"Escribe una fecha [Usando el formato dia,mes,año (00/00/0000)]: ")
    dia = int(fecha[slice(0,2)])
    mes = int(fecha[slice(3,5)])
    año = int(fecha[slice(6,10)])
    if mes > 12:
        return("El mes ingresado no existe")
    elif mes == 2 and dia > 29:
        return("La fecha ingresada no existe")
    elif (mes == 1 or mes ==3 or mes ==5 or mes ==7 or mes ==8 or mes ==10 or mes ==12) and dia > 31:
        return("La fecha ingresada no existe")
    elif (mes == 4 or mes ==6 or mes ==9 or mes ==11) and dia>30:
        return("La fecha ingresada no exite")
    else:
        if dia < 28:
            dia += 1
        else:
            if mes == 1 or mes ==3 or mes ==5 or mes ==7 or mes ==8 or mes ==10 or mes ==12:
                if dia < 31:
                    dia += 1
                else:
                    dia = 1
                    if mes < 12:
                        mes += 1
                    else:
                        mes = 1
                        año += 1 
            elif  mes == 4 or mes ==6 or mes ==9 or mes ==11:
                if dia < 30:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                dia = 1
                mes += 1
    return (f"{dia}/{mes}/{año}")


print(dia_siguiente_e())

