# Transporte de productos l�cteos Visualizaci�n

## Enunciado
La Lechera Ram�rez S.A. es una empresa que produce productos l�cteos y cuenta con cuatro plantas de producci�n en Colombia cuyas capacidades de producci�n mensuales de leche son 1,500, 1,200, 1,400, y 1,000 litros, respectivamente. Estas cuatro plantas suministran leche a los ocho clientes que actualmente tienen, los cuales son distribuidores minoristas de productos. Las demandas mensuales de leche de estos distribuidores son 930, 600, 460, 610, 830, 460, 640 y 240 litros, respectivamente. La Tabla 1 presenta el costo en el que incurre la compa��a al enviar un litro de leche desde cada planta hacia cada distribuidor. 

<p style="text-align: center;"><b>Tabla 1. Costos de distribuci�n</b></p>

|            |**Dist. 1**|Dist. 2|Dist. 3|Dist. 4|Dist. 5|Dist. 6|Dist. 7|Dist. 8|
|:----------:|----------:|------:|------:|------:|------:|------:|------:|------:|
|**Planta 1**|650        |125    |1200   |340    |150    |260    |350    |800    |
|**Planta 2**|250        |200    |250    |600    |150    |950    |1050   |1000   |
|**Planta 3**|600        |350    |400    |260    |150    |300    |450    |600    |
|**Planta 4**|450        |800    |650    |250    |340    |700    |600    |620    |

<div style="text-align:justify">
Formule un modelo general de optimizaci�n lineal que le permita a La Lechera Ram�rez satisfacer la demanda de sus clientes, al menor costo posible. Para esto usted debe seguir los siguientes pasos: 

## Formulaci�n

**1.** Escriba lo(s) conjunto(s), par�metro(s) y variable(s) de decisi�n que utilizar� en el modelo.  

### Conjuntos
- $P$: Plantas
- $D$: Distribuidores

### Par�metros
- $b_i$: oferta de leche de la planta $i\in P$
- $t_j$: demanda de leche del distribuidor $j\in D$ 
- $c_{ij}$: costo de env�o de un litro de leche de la planta $i\in P$ al distribuidor $j\in D$

### Variables de decisi�n
- $x_{ij}$: cantidad (en litros) de leche que van de la planta $i\in P$ al distribuidor $j\in D$

### Restricciones
**2.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que se debe respetar la oferta de las plantas.   

\begin{align}
\sum_{j\in D}x_{ij} &\le b_i, &&\forall i\in P.
\end{align}

**3.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que se debe satisfacer la demanda de los distribuidores.  

\begin{align}
\sum_{i\in P}x_{ij} &\ge t_j, &&\forall j\in D.
\end{align}

**4.** Escriba la(s) restricci�n(es) que describe(n) matem�ticamente el tipo de variable(s) que est� utilizando dentro del modelo.   

\begin{align}
x_{ij} & \ge 0, &&\forall i\in P,j\in D.
\end{align}

### Funci�n Objetivo
**5.** Escriba la funci�n objetivo.

$$
\text{minimizar }  \sum_{i\in P}\sum_{j\in D}x_{ij}c_{ij}
$$

## Formulaci�n matem�tica completa

**Conjuntos:**
- $P$: Plantas
- $D$: Distribuidores

**Par�metros:**
- $b_i$: oferta de leche de la planta $i\in P$
- $t_j$: demanda de leche del distribuidor $j\in D$ 
- $c_{ij}$: costo de env�o de un litro de leche de la planta $i\in P$ al distribuidor $j\in D$

**Variables de decisi�n:**
- $x_{ij}$: cantidad (en litros) de leche que van de la planta $i\in P$ al distribuidor $j\in D$

**Modelo:**

$$
\text{minimizar }  \sum_{i\in P}\sum_{j\in D}x_{ij}c_{ij} \text{ (1)} 
$$

Sujeto a,
\begin{align*}
\sum_{j\in D}x_{ij} &\le b_i, &&\forall i\in P; &(2)\\
\sum_{i\in P}x_{ij} &\ge t_j, &&\forall j\in D; &(3)\\
x_{ij} & \ge 0, &&\forall i\in P,j\in D. &(4)
\end{align*}

La funci�n objetivo (1) minimiza los costos totales. Las restricci�n (2) describe que se debe respetar la oferta de las plantas. La restricci�n (3) describe que se debe satisfacer la demanda de los distribuidores. La restricci�n (4) describe la naturaleza de la variable $x_{ij}$. 

## Implementaci�n
**g.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Plantas
P=["Planta 1",
   "Planta 2",
   "Planta 3",
   "Planta 4"]

#Distribuidores
D=["Distribuidor 1",
   "Distribuidor 2",
   "Distribuidor 3",
   "Distribuidor 4",
   "Distribuidor 5",
   "Distribuidor 6",
   "Distribuidor 7",
   "Distribuidor 8"]

# Conjunto con todas las duplas (planta, distribuidor)
P_x_D = [(planta, distribuidor) for planta in P for distribuidor in D] 

#-----------------
# Par�metros
#-----------------
b={#planta: oferta de la planta i
   "Planta 1":1500,
   "Planta 2":1200,
   "Planta 3":1400,
   "Planta 4":1000} 

t={#distribuidor: demanda del distribuidor j
   "Distribuidor 1":930,
   "Distribuidor 2":600,
   "Distribuidor 3":460,
   "Distribuidor 4":610,
   "Distribuidor 5":830,
   "Distribuidor 6":460,
   "Distribuidor 7":640,
   "Distribuidor 8":240} 

c={#(planta, distribuidor): costo de envio de un litro de leche desde la planta i al distribuidor j
   ("Planta 1","Distribuidor 1"):650,
   ("Planta 1","Distribuidor 2"):125,
   ("Planta 1","Distribuidor 3"):1200,
   ("Planta 1","Distribuidor 4"):340,
   ("Planta 1","Distribuidor 5"):150,
   ("Planta 1","Distribuidor 6"):260,
   ("Planta 1","Distribuidor 7"):350,
   ("Planta 1","Distribuidor 8"):800,
   ("Planta 2","Distribuidor 1"):250,
   ("Planta 2","Distribuidor 2"):200,
   ("Planta 2","Distribuidor 3"):250,
   ("Planta 2","Distribuidor 4"):600,
   ("Planta 2","Distribuidor 5"):150,
   ("Planta 2","Distribuidor 6"):950,
   ("Planta 2","Distribuidor 7"):1050,
   ("Planta 2","Distribuidor 8"):1000,
   ("Planta 3","Distribuidor 1"):600,
   ("Planta 3","Distribuidor 2"):350,
   ("Planta 3","Distribuidor 3"):400,
   ("Planta 3","Distribuidor 4"):260,
   ("Planta 3","Distribuidor 5"):150,
   ("Planta 3","Distribuidor 6"):300,
   ("Planta 3","Distribuidor 7"):450,
   ("Planta 3","Distribuidor 8"):600,
   ("Planta 4","Distribuidor 1"):450,
   ("Planta 4","Distribuidor 2"):800,
   ("Planta 4","Distribuidor 3"):650,
   ("Planta 4","Distribuidor 4"):250,
   ("Planta 4","Distribuidor 5"):340,
   ("Planta 4","Distribuidor 6"):700,
   ("Planta 4","Distribuidor 7"):600,
   ("Planta 4","Distribuidor 8"):620} 

#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("Transporte",lp.LpMinimize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',P_x_D,lowBound=0,cat='Continuous') #litros de leche que van de la planta i al distribuidor j; aca se a�ade de una vez la naturaleza de las variables

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de minimizacion de costos
problema+=lp.lpSum(x[i,j]*c[i,j] for i in P for j in D), "Costos Totales"

#-----------------------------
# Restricciones
#-----------------------------
#sum(j in D)x_ij <= b_i forall i in P
for i in P:
    problema+= lp.lpSum(x[i,j] for j in D) <= b[i], "Oferta de la planta "+i   #se respeta la oferta de cada planta 

#sum(i in P)x_ij >= t_j forall j in D
for j in D:
    problema+= lp.lpSum(x[i,j] for i in P) >= t[j], "Demanda del distribuidor "+j #se satisface la demanda de cada distribuidor 
    
#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("Transporte.lp")

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')

#Valor �ptimo del plan de transporte  
print("\nTransporte - Costos totales = $", round(lp.value(problema.objective),2))
print()

#Imprimir variables de decisi�n
print("Variables de decisi�n")
print("              ","D1","D2","D3","D4","D5","D6","D7","D8",sep='\t')
for i in P:
    print(i,end='\t')
    for j in D: 
        print(round(x[i,j].value()),end='\t')
    print()

### Visualizaci�n de resultados

En esta ocasi�n exploraremos una forma diferente de visualizar la soluci�n. En los ejercicios anteriores hemos optado por imprimir los valores que toman las variables y acomodarlos en tablas. Ahora, revisaremos la forma de visualizar los datos para un mejor entendimiento de la soluci�n. Para esto, tendremos la coordenadas de las plantas y los distribuidores guardadas en diccionarios. Importaremos el paquete de matplotlib y dise�aremos funciones que nos permitir�n agregar elementos a los gr�ficos. 

#### NetworkX

#se importan las librerias que se utilizar�n para la visualizaci�n
import networkx as nx
import matplotlib.pyplot as plt

#Coordenadas de las plantas
coordenadasPlantas={#planta: (x, y)
                    "Planta 1":(9.5,12),
                    "Planta 2":(7,5),
                    "Planta 3":(5,14),
                    "Planta 4":(2.5,9.5)}

#Coordenadas de los distribuidores
coordenadasDistribuidores={#distribuidor: (x, y)
                           "Distribuidor 1":(5.5,9),
                           "Distribuidor 2":(8,9),
                           "Distribuidor 3":(5,8),
                           "Distribuidor 4":(6,10),
                           "Distribuidor 5":(7,10),
                           "Distribuidor 6":(7.5,15),
                           "Distribuidor 7":(8,17),
                           "Distribuidor 8":(1,15)}

#se crean dos conjuntos auxiliares para los labels de los nodos de las plantas y distribuidores
labelsPlantas={n:n[-1] for n in P}
labelsDistribuidores={n:n[-1] for n in D}

#se crea un conjunto auxiliar para los labels de los arcos
coordenadasTodo=coordenadasPlantas
coordenadasTodo.update(coordenadasDistribuidores)

#Se guarda la soluci�n en un vector
xSol={(i,j):x[i,j].value() for i in P for j in D if x[i,j].value()>0.1}

#Se modifican las dimensiones de la visualizaci�n
plt.rcParams["figure.figsize"] = 6,4
plt.rcParams["figure.dpi"] = 200

#Creaci�n de un modelo de grafos dirigidos.
G=nx.DiGraph()

#Dibujar los nodos de plantas y distribuidores.
nx.draw_networkx_nodes(G,coordenadasPlantas,nodelist=P,node_color='skyblue',node_size=100)
nx.draw_networkx_nodes(G,coordenadasDistribuidores,nodelist=D,node_color='lightgray',node_size=100)

#Dibujar los labels de los nodos de plantas y distribuidores.
nx.draw_networkx_labels(G,coordenadasPlantas,labelsPlantas,font_size=10)
nx.draw_networkx_labels(G,coordenadasDistribuidores,labelsDistribuidores,font_size=10)

#Dibujar arcos del diagrama con sus respectivos litros de leche enviados.
nx.draw_networkx_edges(G,coordenadasTodo,xSol,width=5, edge_color='c',arrows=True)
nx.draw_networkx_edge_labels(G,coordenadasTodo,edge_labels=xSol,font_size=6)
nx.draw_networkx(G,coordenadasTodo,with_labels=True)

#Borrar ejes, agregar titulo y mostrar la ventana del diagrama.
plt.axis('off')
nx.draw(G)
plt.suptitle("Distribuci�n La Lechera Ram�rez S.A.",fontsize=20)
plt.show()

#### Matplotlib

#se importa la libreria que utilizar� para la visualizaci�n
import matplotlib.pyplot as plt

#Coordenadas de las plantas
coordenadasPlantas={#planta: (x, y)
                    "Planta 1":(9,12),
                    "Planta 2":(7,6),
                    "Planta 3":(5,14),
                    "Planta 4":(2.5,10.5)}

#Coordenadas de los distribuidores
coordenadasDistribuidores={#distribuidor: (x, y)
                           "Distribuidor 1":(5.5,9),
                           "Distribuidor 2":(8,10),
                           "Distribuidor 3":(5,8),
                           "Distribuidor 4":(6,10),
                           "Distribuidor 5":(7,10),
                           "Distribuidor 6":(7.5,15),
                           "Distribuidor 7":(7,17),
                           "Distribuidor 8":(1,15)}

#Se guarda la soluci�n en un vector
xSol={(i,j):x[i,j].value() for i in P for j in D}

#funci�n para pintar las plantas
def pintarPlantas(pPlantas,pAx):
    xP=[i for (i,j) in pPlantas.values()]
    yP=[j for (i,j) in pPlantas.values()]
    pAx.scatter(xP,yP,c='green',marker='s',s=200,zorder=2)
    return pAx

#funci�n para pintar los distribuidores
def pintarDistribuidores(pDistribuidores,pAx):
    xD=[i for (i,j) in pDistribuidores.values()]
    yD=[j for (i,j) in pDistribuidores.values()]
    pAx.scatter(xD,yD,c='red',s=100,zorder=2)
    return pAx

#funci�n para pintar la soluci�n
def pintarSoluci�n(pSolucion,pPlantas,pDistribuidores,pAx):
    for (i,j),val in pSolucion.items():
        if val>0:
            pAx.plot([pPlantas[i][0],pDistribuidores[j][0]],[pPlantas[i][1],pDistribuidores[j][1]],c='orange',zorder=1,label=val)
    return pAx

#funci�n para pintar los numeros de cada planta
def pintarNumPlantas(pPlantas,pAx):
    for i,pos in pPlantas.items():
        pAx.text(pos[0]-0.08,pos[1]-0.12,i[-1],fontsize=12,color='white')
    return ax

#funci�n para pintar los numeros de cada distribuidor
def pintarNumDistribuidores(pDistribuidores,pAx):
    for i,pos in pDistribuidores.items():
        pAx.text(pos[0]-0.06,pos[1]-0.12,i[-1],fontsize=8,color='black')
    return pAx

fig, ax = plt.subplots(figsize=(10,10))

#se definen la dimensi�n de los ejes y se borran los labels de los ejes
ax.set_xlim([0,10])
ax.set_ylim([2,20])
ax.set_xticks([])
ax.set_yticks([])

ax=pintarSoluci�n(xSol,coordenadasPlantas,coordenadasDistribuidores,ax)
ax=pintarDistribuidores(coordenadasDistribuidores,ax)
ax=pintarNumDistribuidores(coordenadasDistribuidores,ax)
ax=pintarPlantas(coordenadasPlantas,ax)
ax=pintarNumPlantas(coordenadasPlantas,ax)

## Cr�ditos

Equipo Principios de Optimizaci�n<br>
Edici�n: Camilo Aguilar, Juan Felipe Rengifo M<br>
Fecha: 20/09/2020