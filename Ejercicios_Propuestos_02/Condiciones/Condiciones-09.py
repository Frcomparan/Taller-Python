#Convertir centimetros
def centimetros():
    cen=float(input("Ingresa una distancia en centimetros --> "))
    kil = cen/1000
    met = cen/100
    mil = cen * 10
    print(f"Kilometros: {kil}km\nMetros: {met}m\nCentimetros: {cen}cm\nMilimetros: {mil}mm")

centimetros()