#Formacion de poker
import random
corazon = ("cA","c2","c3","c4","c5","c6","c7","c8","c9","cJ","cQ","cK")
picas = ("pA","p2","p3","p4","p5","p6","p7","p8","p9","pJ","pQ","pK")
trebol =("tA","t2","t3","t4","t5","t6","t7","t8","t9","tJ","tQ","tK")
rombos = ("rA","r2","r3","r4","r5","r6","r7","r8","r9","rJ","rQ","rK")
baraja = corazon + picas + trebol + rombos

barajar = list(baraja)
random.shuffle(barajar)

def poker(cartas):
    mazo = random.sample(cartas,5)
    print(f"Mazo actual: \n{mazo}")
    for i in range(2):
        rev =mazo[i]
        cont = 0
        for j in range(0,5):
            carta=mazo[j]
            if rev[1] == carta[1]:
                cont += 1
        if cont > 3:
            print("Felicidades\n tienes \nun poker\n")
            break
    else:
        print("No tienes poker")

poker(barajar)
#mazo_prueba= ["a2","b2","c1","a2","d2"]