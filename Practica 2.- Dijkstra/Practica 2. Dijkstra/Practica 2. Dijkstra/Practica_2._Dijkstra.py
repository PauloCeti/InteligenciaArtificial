# Paulo Salvatore Partida Escamilla
# 19310483
# 6E2 Inteligencia Artificial
# P2. Dijkstra 

#Significado de los nodos v2:
#•	Inicio. Tienes identificada a tu crush
#•	1. Presentarte sin hablarle antes
#•	2.  Buscarla en redes sociales  y presentarte por ahí
#•	3. Invitarla a salir
#•	4. Investigar/ preguntarle sobre sus gustos y platicar sobre ello
#•	5. Darle un regalo / pequeños detalles
#•	6. Besarla
#•	7. Demostrar atención por su bienestar (físico y mental)
#•	Final. Conquistas a tu crush

import networkx as nx
import matplotlib.pyplot as plt


def TestDic(Diccionario):   #Función que muestra el valor de cada nodo y sus conexiones
    for key in Diccionario:
        print(key, ":", Diccionario[key])

#///////////////////////////  Inicialización  ///////////////////////////

DiccNodos=dict.fromkeys(['Inicio','1','2','3','4','5','6','7','Fin'])
DiccAristas={}

#///////////////////////////  Nodos adyacentes y sus udif  ///////////////////////////

#Conexión entre nodos. v2:
#Nodo	    Posibles nodos aledaños
#Inicio 	1,2
#1	        Inicio,3,4
#2	        Inicio,3,4
#3	        1,2,4,5,6,7
#4	        1,2,3,5,7
#5	        3,4
#6	        3,7, Fin
#7	        3,4,6, Fin
#Fin        6,7

for key in DiccNodos:       
#Se establecen todas las conexiones de los nodos en sus diccionarios aun cuando ya hayan
#quedado establecidas en diccionarios de sus nodos aledaños, es decir:

# == Aun cuando ya se definió en otros, cada diccionario guarda sus conexiones individuales. ==

    if key == 'Inicio':
        DiccAristas=dict(zip(['1','2'],[6,1])) #[Nodos adyacentes],[Udif's]
    elif key == '1':
        DiccAristas=dict(zip(['Inicio','3','4'],[6,7,4]))
    elif key == '2':
        DiccAristas=dict(zip(['Inicio','3','4'],[1,6,1]))
    elif key == '3':
        DiccAristas=dict(zip(['1','2','4','5','6','7'],[7,6,6,1,8,1]))
    elif key == '4':
        DiccAristas=dict(zip(['1','2','3','5','7'],[4,1,6,1,4]))
    elif key == '5':
        DiccAristas=dict(zip(['3','4'],[1,1]))    
    elif key == '6':
        DiccAristas=dict(zip(['3','7','Fin'],[8,5,6]))
    elif key == '7':
        DiccAristas=dict(zip(['3','4','6','Fin'],[1,4,5,1]))
    elif key == 'Fin':
        DiccAristas=dict(zip(['6','7'],[6,1])) 
    DiccNodos[key]=DiccAristas

#Testeo
TestDic(DiccNodos)

#///////////////////////////  Dijkstra Algorithm  ///////////////////////////

def get_key(val, pos, Dicc):
    j=0
    for key, value in Dicc.items():
        if val==value:
            if pos==j:
                return key
            else:
                j=j+1
    return "Key does not exist"

CaminoMasCorto=[]
Temporal=[]
nodo='Inicio'
while(len(CaminoMasCorto)==0 or CaminoMasCorto[-1]!= 'Fin'):
        if nodo == 'Fin':
            CaminoMasCorto.append(nodo)
        else:
            if nodo == 'Inicio':
                CaminoMasCorto.append(nodo)
            for NodoAledaño in DiccNodos[nodo]:
                Temporal.append(DiccNodos[nodo].get(NodoAledaño))
            Temporal.sort()
            i=0
            Pos=0
            NextNodo=get_key(Temporal[i],Pos,DiccNodos[nodo])
            while (NextNodo in CaminoMasCorto):
                i=i+1
                if Temporal[i]== Temporal[i-1]:
                    Pos=Pos+1
                NextNodo=get_key(Temporal[i],Pos,DiccNodos[nodo]) 
            CaminoMasCorto.append(NextNodo)
            Temporal.clear()
            nodo=CaminoMasCorto[-1] 

print("El camino más corto es:",CaminoMasCorto) #debería de ser Inicio-2-4-5-3-7-Fin


#///////////////////////////  Grafo  ///////////////////////////

Grafo=nx.Graph()


#Asignación de propiedades y relación entre nodos y aristas
for nodo in DiccNodos:
     Grafo.add_node(nodo, color= "green")
     for llave in DiccNodos[nodo]:
         Grafo.add_edge(nodo,llave,color="black",value=(str(DiccNodos[nodo].get(llave))+" udif"))
         #udif= Unidades de Dificultad

#Modificación de los colores de  nodos y aristas de la ruta más corta:

for nodo in CaminoMasCorto:
    Grafo.nodes[nodo]['color']="red"
    if nodo != 'Fin':
        Grafo[nodo][CaminoMasCorto[CaminoMasCorto.index(nodo)+1]]['color']='red'

#Obten los colores de los nodos y edges:

edges,EdgCol=zip(*nx.get_edge_attributes(Grafo, 'color').items())
nodes, NodCol=zip(*nx.get_node_attributes(Grafo, 'color').items())

#Obtiene el valor de los edges (aristas)
EdgLab=nx.get_edge_attributes(Grafo, 'value')

#Posición para el comando de show lables.
pos=nx.spring_layout(Grafo)

#Prueba para mostrar los valores y propiedades de las aristas.
    #print(nx.get_edge_attributes(grafo, 'color'))
    #print("//////////////////")
    #print(edglab)

nx.draw(Grafo,pos, node_color=NodCol, edge_color=EdgCol, with_labels=True)
nx.draw_networkx_edge_labels(Grafo,pos,edge_labels=EdgLab)
plt.show()


