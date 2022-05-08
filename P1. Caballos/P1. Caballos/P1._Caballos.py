#   Practica 1. Caballos
#
#       Paulo Salvatore Partida Escamilla
#       19310483
#       6E2
from random import seed
from random import random
seed(6)

class Caballo:
    Tiempo=0
    PosicionInterna=0
    ID=0
    Grupo=""
    RankingGlobal=0

ListaCaballos=[]
NuevaListaCaballos= []
Speed=[0,0,0,0,0]
NuevoOrdenGrupos=["","","","",""]
Temporal=[]

def TestInfoCaballos():
    for i in range(25):
        print("El caballo #",ListaCaballos[i].ID, ",hizo el tiempo:",ListaCaballos[i].Tiempo,
             ",\nes del grupo:", ListaCaballos[i].Grupo,", y su pos int:", ListaCaballos[i].PosicionInterna,
             "y su ranking Global es:",ListaCaballos[i].RankingGlobal)
        print("==============================================")


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


### Beginning: 

CreacionCaballos()

# Primeras 5 Carreras:
for Carrera in range(5):
    for i in range (5): #Ordena y crea los tiempos
        x=5*Carrera+i   #Escoge una tanda (5*Carrera) y el caballo de ella
        Speed[i]=ListaCaballos[x].Tiempo
    Speed.sort(reverse=True)
    #Asignación de posiciones internas:
    for element in Speed:
        for i in range (5):     #Pasa por todos los caballos del grupo y compara cada uno con cada valor de speed
            x=5*Carrera+i
            if element== ListaCaballos[x].Tiempo:
                ListaCaballos[x].PosicionInterna=Speed.index(element)

# Carrera #06:
i=0
for caballo in ListaCaballos: #Compara las velocidades
    if caballo.PosicionInterna == 0:
        Temporal.append(caballo)
        Speed[i]=caballo.Tiempo
        i+=1
Speed.sort(reverse=True)
#print (Speed)
i=0
for element in Speed: #Ordena los grupos segun quien es el más rapido
    for caballo in Temporal:
        if caballo.Tiempo== element:
            if Speed.index(element)==0:
                caballo.RankingGlobal=1
            NuevoOrdenGrupos[i]=caballo.Grupo
            i+=1
#print (NuevoOrdenGrupos)

#Carrera 07:
x=0
for i in range (25): #Selecciona los caballos a correr
    if ListaCaballos[i].Grupo == NuevoOrdenGrupos[0]: #A2 y A3
        if ListaCaballos[i].PosicionInterna == 1 or ListaCaballos[i].PosicionInterna == 2:
            Temporal[x]=ListaCaballos[i]
            x+=1
    if ListaCaballos[i].Grupo == NuevoOrdenGrupos[1]: #B1 y B2
        if ListaCaballos[i].PosicionInterna == 0 or ListaCaballos[i].PosicionInterna == 1:
            Temporal[x]=ListaCaballos[i]
            x+=1
    if ListaCaballos[i].Grupo == NuevoOrdenGrupos[2]: #C1
        if ListaCaballos[i].PosicionInterna == 0:
            Temporal[x]=ListaCaballos[i]
            x+=1

for i in range (5): #Compara la velocidad de los caballos y asigna posición global.
    Speed[i]= Temporal[i].Tiempo
Speed.sort (reverse=True)
for element in Speed:
    for caballo in Temporal:
        if caballo.Tiempo == element and (Speed.index(element)==0 or Speed.index(element)==1):
            caballo.RankingGlobal= Speed.index(element)+2

##Asignacíón de posiciones globales para grafo:
#Nueva lista ordenada por las velocidades
NuevaListaCaballos= sorted (ListaCaballos, key=lambda x:x.Tiempo, reverse=True)
#Asignación de Ranking global
for element in NuevaListaCaballos:
    for caballo in ListaCaballos:
        if element==caballo:
            caballo.RankingGlobal=NuevaListaCaballos.index(element)+1

### Versión anterior:
##Primer Caballo más rápido
#x=0
#for i in range (25):
#    if ListaCaballos[i].PosicionInterna==0:
#        Speed[x]=ListaCaballos[i].Tiempo
#        x+=1
#Speed.sort(reverse=True)
#y=0
#index=0
#for i in range (25):
#    if Speed[0]== ListaCaballos[i].Tiempo:
#        ListaCaballos[i].RankingGlobal=1
#    if ListaCaballos[i].Tiempo in Speed:
#        index=Speed.index(ListaCaballos[i].Tiempo)
#        NuevoOrdenGrupos[index]=ListaCaballos[i].Grupo

##print (NuevoOrdenGrupos)


###Segundo Caballo
#x=0
#for i in range (25):
#    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[0] and (ListaCaballos[i].PosicionInterna==1 or ListaCaballos[i].PosicionInterna==2):
#        Speed[x]=ListaCaballos[i].Tiempo
#        x+=1
#    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[1] and (ListaCaballos[i].PosicionInterna==0 or ListaCaballos[i].PosicionInterna==1):
#        Speed[x]=ListaCaballos[i].Tiempo
#        x+=1
#    if ListaCaballos[i].Grupo==NuevoOrdenGrupos[2] and ListaCaballos[i].PosicionInterna==0:
#        Speed[x]=ListaCaballos[i].Tiempo
#        x+=1
#Speed.sort(reverse=True)
#for i in range (25):
#    if Speed[0]== ListaCaballos[i].Tiempo:
#        ListaCaballos[i].RankingGlobal=2
#    elif Speed[1]== ListaCaballos[i].Tiempo:
#        ListaCaballos[i].RankingGlobal=3

TestInfoCaballos()
print("/////////////////////////////////////////////////////")
print("Gracias a estos resultados podemos obnservar que en efecto 7 carreras son las minimas para obtener\n"
      " los 2 (o hasta 3) caballos más rápidos de los 25. Siendo los que anteriormente se mostraron con su ranking\n"
      " global de '1', '2' o '3'")
print("/////////////////////////////////////////////////////")


