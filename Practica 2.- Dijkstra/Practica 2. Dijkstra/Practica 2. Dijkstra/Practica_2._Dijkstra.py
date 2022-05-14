# Paulo Salvatore Partida Escamilla
# 19310483
# 6E2 Inteligencia Artificial
# P2. Dijkstra

import networkx as nx
import matplotlib.pyplot as plt


def TestDic(Diccionario):
    for key in Diccionario:
        print(key, ":", Diccionario[key])

#Inicialización.
DiccNodos=dict.fromkeys(['Inicio','1','2','3','4','5','6','7','8','9','10','11','12','Fin'])
DiccAristas={}

#Asignación de nodos adyacentes y su peso
for key in DiccNodos:
    if key == 'Inicio':
        DiccAristas=dict(zip(['1','2','3'],[8,2,1]))
    elif key == '1':
        DiccAristas=dict(zip(['4','5','6','8'],[8,2,1,0]))
    elif key == '2':
        DiccAristas=dict(zip(['4','5','6','9'],[8,2,1,0]))
    elif key == '3':
        DiccAristas=dict(zip(['4','5','6','10'],[8,2,1,0]))
    elif key == '4':
        DiccAristas=dict(zip(['8','9','11','12'],[8,2,1,0]))
    elif key == '5':
        DiccAristas=dict(zip(['11','Fin'],[8,2]))
    elif key == '6':
        DiccAristas=dict(zip(['7','8','9'],[8,2,1]))
    elif key == '7':
        DiccAristas=dict(zip(['4','5','8','9','10','12'],[8,2,1,0,0,0]))
    elif key == '8':
        DiccAristas=dict(zip(['4','5'],[8,2]))
    elif key == '9':
        DiccAristas=dict(zip(['4'],[8]))
    elif key == '10':
        DiccAristas=dict(zip(['6'],[8]))
    elif key == '11':
        DiccAristas=dict(zip(['4','5','12','Fin'],[8,2,1,0]))
    elif key == '12':
        DiccAristas=dict(zip(['4','5','11','Fin'],[8,2,1,0]))
    elif key == 'Fin':
        DiccAristas=dict(zip(['5','11','12'],[8,2,1]))
    DiccNodos[key]=DiccAristas


#Testeo
TestDic(DiccNodos)

#Muestrame el grafo:

Grafo=nx.Graph()
for nodo in DiccNodos:
    Grafo.add_node(nodo)

for key in DiccNodos:
     for llave in DiccNodos[key]:
         Grafo.add_edge(key,llave)

nx.draw(Grafo, node_color='red', with_labels=True)
plt.show()