meses_esc_a_num = {"Ene":1,"Feb":2,"Mzo":3,"Abr":4,"May":5,"Jun":6,"Jul":7,"Ago":8,"Sep":9,"Oct":10,"Nov":11,"Dic":12,}
meses_num_a_esc = {1:"Ene",2:"Feb",3:"Mzo",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10:"Oct",11:"Nov",12:"Dic"}
def dia_siguiente_e():
    print("CLAVE DE MESES: \nEnero: Ene\nFebrero: Feb \nMarzo: Mzo \nAbril: Abr\nMayo: May \n \
        Junio: Jun\nJulio: Jul\nAgosto: Ago\nSeptiembre: Sep\nOctubre: Oct\nNoviembre: Nov\nDiciembre: Dic")
    fecha = input(f"Escribe una fecha [Usando el formato dia,mes,año (00/XXX/0000)]: ")
    dia = int(fecha[slice(0,2)])
    mes = meses_esc_a_num[(fecha[slice(3,6)])]
    año = int(fecha[slice(7,11)])
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
    return (f"{dia}/{meses_num_a_esc[mes]}/{año}")


print(dia_siguiente_e())
