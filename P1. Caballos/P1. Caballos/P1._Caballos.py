#   Practica 1. Caballos
#
#       Paulo Salvatore Partida Escamilla
#       19310483
#       6E2
from random import seed
from random import random
seed(1)

class Caballo:
    Tiempo=0
    PosicionInterna=0
    ID=0
    Grupo=""
    RankingGlobal=0

ListaCaballos=[]
Speed=[0,0,0,0,0]
NuevoOrdenGrupos=["","","","",""]

def TestInfoCaballos():
    for i in range(25):
        print("El caballo #",ListaCaballos[i].ID, ",hizo el tiempo:",ListaCaballos[i].Tiempo,
             ",\nes del grupo:", ListaCaballos[i].Grupo,", y su pos int:", ListaCaballos[i].PosicionInterna,
             "y su ranking Global es:",ListaCaballos[i].RankingGlobal)

def CreacionCaballos():
    for i in range(25):
        ListaCaballos.append(Caballo())
        ListaCaballos[i].ID=i
        # Numero random entre 0-1, multiplicado por 100, redondeado a 2 decimas:
        ListaCaballos[i].Tiempo=(round(random()*100, 2))
        if i<5:
            ListaCaballos[i].Grupo="a"
        elif i<10:
            ListaCaballos[i].Grupo="b"
        elif i<15:
            ListaCaballos[i].Grupo="c"
        elif i<20:
            ListaCaballos[i].Grupo="d"
        elif i<25:
            ListaCaballos[i].Grupo="e"

CreacionCaballos()

# Primeras 5 Carreras:
for Carrera in range(5):
    for i in range (5): #Crea la lista de velocidades del grupo
        x=5*Carrera+i
        Speed[i]=ListaCaballos[x].Tiempo
    Speed.sort(reverse=True)
    for element in Speed:
        for i in range (5):     #Pasa por todos los caballos del grupo y compara cada uno con cada valor de speed
            x=5*Carrera+i
            if element== ListaCaballos[x].Tiempo:
                ListaCaballos[x].PosicionInterna=Speed.index(element)

#Primer Caballo más rápido
x=0
for i in range (25):
    if ListaCaballos[i].PosicionInterna==0:
        Speed[x]=ListaCaballos[i].Tiempo
        x+=1
Speed.sort(reverse=True)
y=0
index=0
for i in range (25):
    if Speed[0]== ListaCaballos[i].Tiempo:
        ListaCaballos[i].RankingGlobal=1
    if ListaCaballos[i].Tiempo in Speed:
        index=Speed.index(ListaCaballos[i].Tiempo)
        NuevoOrdenGrupos[index]=ListaCaballos[i].Grupo

#print (NuevoOrdenGrupos)


##Segundo Caballo
x=0
for i in range (25):
    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[0] and (ListaCaballos[i].PosicionInterna==1 or ListaCaballos[i].PosicionInterna==2):
        Speed[x]=ListaCaballos[i].Tiempo
        x+=1
    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[1] and (ListaCaballos[i].PosicionInterna==0 or ListaCaballos[i].PosicionInterna==1):
        Speed[x]=ListaCaballos[i].Tiempo
        x+=1
    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[2] and ListaCaballos[i].PosicionInterna==0:
        Speed[x]=ListaCaballos[i].Tiempo
        x+=1
Speed.sort(reverse=True)
for i in range (25):
    if Speed[0]== ListaCaballos[i].Tiempo:
        ListaCaballos[i].RankingGlobal=2
    elif Speed[1]== ListaCaballos[i].Tiempo:
        ListaCaballos[i].RankingGlobal=3

TestInfoCaballos()



