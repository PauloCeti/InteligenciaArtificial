# Paulo Salvatore Partida Escamilla
# 19310483
# 6E2 Inteligencia Artificial
# P2. Dijkstra 

#Significado de los nodos:
#v1
#•	Inicio. Tienes identificada a tu crush
#•	1. Presentarte sin hablarle antes
#•	2.  Buscarla en redes sociales  y presentarte por ahí
#•	3.  Contactar a un amigo de ella y pedirle que los presente
#•	4. Invitarla a salir
#•	5. Decirle que te gusta
#•	6. Investigar/ preguntarle sobre sus gustos
#•	7. Establecer platica con ella sobre lo que les gusta a los dos
#•	8. Darle un regalo
#•	9. Darle pequeños detalles
#•	10. Conocer a sus amigos y hacerlos mis amigos
#•	11. Besarla
#•	12. Demostrar atención por su bienestar (físico y mental)
#•	Final. Conquistas a tu crush
# v2:
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


def TestDic(Diccionario):
    for key in Diccionario:
        print(key, ":", Diccionario[key])

#Inicialización.
DiccNodos=dict.fromkeys(['Inicio','1','2','3','4','5','6','7','Fin'])
DiccAristas={}

#Asignación de nodos adyacentes y su peso

#Conexión entre nodos.
# v1:
#Nodo	Posibles nodos aledaños
#1	4,5,6,8
#2	4,5,6,9
#3	4,5,6,10
#4	8,9,11,12
#5	11, Fin
#6	7,8,9
#7	4,5,8,9,10,12
#8	4,5
#9	4
#10	6
#11	4,5,12, Fin
#12	4,5,11, Fin
#v2:
#Nodo	    Posibles nodos aledaños
#Inicio 	1,2
#1	        3,4
#2	        4
#3	        5,6,7
#4	        3,5,7
#5	        3
#6	        3,7, Fin
#7	        3,6, Fin


for key in DiccNodos:
    if key == 'Inicio':
        DiccAristas=dict(zip(['1','2'],[4,1])) #[Nodos adyacentes],[Dificultad/Peso arista]
    elif key == '1':
        DiccAristas=dict(zip(['3','4'],[6,3]))
    elif key == '2':
        DiccAristas=dict(zip(['4'],[2]))
    elif key == '3':
        DiccAristas=dict(zip(['5','6','7'],[4,6,3]))
    elif key == '4':
        DiccAristas=dict(zip(['3','5','7'],[2,3,2]))
    elif key == '5':
        DiccAristas=dict(zip(['3'],[4]))
    elif key == '6':
        DiccAristas=dict(zip(['3','7','Fin'],[6,3,5]))
    elif key == '7':
        DiccAristas=dict(zip(['3','6','Fin'],[3,3,1]))
    elif key == 'Fin':
        DiccAristas=dict(zip(['6','7'],[5,1])) 
    DiccNodos[key]=DiccAristas


#Testeo
TestDic(DiccNodos)

#///////////////////////////  Grafo  ///////////////////////////

Grafo=nx.Graph()
#for nodo in DiccNodos:
#    Grafo.add_node(nodo, color= "blue")

#Asignación de propiedades y relación entre nodos y aristas
for nodo in DiccNodos:
     Grafo.add_node(nodo, color= "blue")
     for llave in DiccNodos[nodo]:
         Grafo.add_edge(nodo,llave,color="black",value=(str(DiccNodos[nodo].get(llave))+" udif"))
         #udif= Unidades de Dificultad


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


#### NEXT STEPS:
# 1. Verificar que los udif entre nodos sean coherentes (0 codigo)
# 2. Diseñar el algoritmo Dijkstra para identificar la ruta por los nodos con menos udif's (0 grafos)
# 3. Modificar los valores de las propiedades de estos nodos y aristas para destacar el camino más rapido
#    (100% grafo)