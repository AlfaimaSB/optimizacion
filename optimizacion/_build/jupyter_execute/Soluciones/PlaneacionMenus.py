# Planeaci�n de men�s Soluci�n

## Enunciado

El personal t�cnico de un hospital quiere desarrollar un sistema computarizado de planificaci�n de
men�s. Para comenzar, el hospital llevar� a cabo un piloto para planificar el men� del almuerzo.
Este men� debe incluir 100 gramos (g) de cada uno de los siguientes tres grupos alimenticios ($T$): frutas,
verduras, y carnes. La siguiente tabla presenta el costo por cada 100 g de algunos alimentos sugeridos ($A$), as�
como el porcentaje de macronutrientes (carbohidratos, prote�nas y grasas) y la cantidad, en
miligramos (mg), de vitaminas que contienen 100 g de dichos alimentos.


| ||Vitaminas (mg)|Carbohidratos (%)| Prote�na (%)| Grasas (%)|Costo (\$) por cada 100g|
|:-:|:-|-:|-:|-:|-:|-:|
|**Frutas**|||||||
||Naranja|50.00|8.90|0.80|0.00|570.00|
||Manzana|5.00|10.50|0.30|0.00|650.00|
||Banano|35.00|20.80|1.20|0.30|200.00|
||Pera|12.00|11.70|0.40|0.10|550.00|
|**Verduras**|||||||
||Br�coli|116.00|4.90|3.20|0.20|450.00|
||Espinaca|52.00|4.10|2.50|0.30|600.00|
||Guisantes|23.00|18.20|7.20|0.40|800.00|
||Pepino|9.00|0.70|0.15|2.70|500.00|
||Calabac�n|21.00|7.30|4.20|0.10|450.00|
|**Carnes**|||||||
||Pollo|61.00|1.00|23.00|2.00|1,420.00|
||Res|31.00|2.00|18.00|20.00|4,800.00|
||Cerdo|2.00|1.50|16.00|27.00|2,900.00|


El men� del almuerzo debe contener una cantidad m�nima de cada uno de los cuatro
macronutrientes mostrados en la tabla. Estas cantidades m�nimas son: 100 mg de vitaminas, 25 g de carbohidratos, 17 g de prote�nas y 5 g de grasas. El equipo t�cnico del hospital desea incluir un
modelo de optimizaci�n en el sistema para planear el men� del almuerzo al menor costo posible.

## Formulaci�n
**a.** Formule matem�ticamente un modelo de optimizaci�n de forma general que represente la
situaci�n anterior. Defina clara y rigurosamente:  
- Conjuntos
- Par�metros
- Variables de decisi�n
- Funci�n objetivo
- Restricciones


### Conjuntos 
- $T$: conjunto de tipos de alimentos
- $A$: conjunto de alimentos
- $N$: conjunto de aspectos nutricionales

### Par�metros 
- $l_n$: contenido m�nimo  del aspecto nutriconal $n\in N$ que debe tener el men�
- $k_{an}$: cantidad del aspecto nutricional $n\in N$ que contiene el alimento $a\in A$
- $c_a$: costo por porci�n (100g) del alimento $a\in A$
- $p_{at}: \begin{cases}1&\text{, si el alimento }a\in A\text{ pertenece al tipo de alimento }t\in T\text{;} \\ 0 & \text{, d.l.c.}  \end{cases}$ 


### Variables de decisi�n 
- $x_a$: cantidad de porciones (100g) del alimento $a\in A$ incluidas en el men�

### Funci�n Objetivo
$$
\text{minimizar}  \sum_{a\in A}c_a\cdot x_a \text{  (1)}
$$
### Restricciones
Sujeto a,
\begin{align*}
\sum_{a\in A|p_{at}=1}x_a&=1, &&\forall T\in T;   &(2)\\ 
\sum_{a\in A}k_{an}\cdot x_a&\ge l_n, &&\forall n\in N;   &(3)\\
 x_a&\ge 0,&&\forall a\in A;   &(4)
\end{align*}

La funci�n objetivo (1) minimiza los costos totales. La restricci�n (2) garantiza que el men� tenga una porci�n (100g) de cada tipo de alimento $t \in T$. La restricci�n (3) garantiza que haya un m�nimo $l_n$ de cada aspecto nutricional $n\in N$ en el men�. La restricci�n (4) describe la naturaleza de la variable $x_a$

## Implementaci�n

**b.** Resuelva el modelo planteado utilizando la librer�a de PuLP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#%% se importa la libreria de PulP 
import pulp as lp

#-----------------
# Conjuntos
#-----------------

#Tipos de Alimentos
T=["Frutas",
   "Verduras",
   "Carnes"]

#Alimentos
A=["Naranja",
   "Manzana",
   "Banano",
   "Pera",
   "Br�coli",
   "Espinaca",
   "Guisantes",
   "Pepino",
   "Calabac�n",
   "Pollo",
   "Res",
   "Cerdo"]

#Aspectos Nutricionales
N=["Vitaminas",
   "Carbohidratos",
   "Prote�na",
   "Grasas"]


#-----------------
# Par�metros
#-----------------

#Contenido minimo del aspecto nutricional n que debe tener el men�
l={'Vitaminas': 100, 
   'Carbohidratos': 25, 
   'Prote�na': 17, 
   'Grasas': 5}

#Cantidad del aspecto nutricional n que tiene el alimento a
#WATCH OUT: Algunos par�metros en la tabla son "porcentajes" por lo que toca dividirlos por cien para utilizarlos en el modelo y obtener resultados consistentes. 
k={('Naranja', 'Vitaminas'): 50,
   ('Naranja', 'Carbohidratos'): 8.9,
   ('Naranja', 'Prote�na'): 0.8,
   ('Naranja', 'Grasas'): 0,
   ('Manzana', 'Vitaminas'): 5,
   ('Manzana', 'Carbohidratos'): 10.5,
   ('Manzana', 'Prote�na'): 0.3,
   ('Manzana', 'Grasas'): 0,
   ('Banano', 'Vitaminas'): 35,
   ('Banano', 'Carbohidratos'): 20.8,
   ('Banano', 'Prote�na'): 1.2,
   ('Banano', 'Grasas'): 0.3,
   ('Pera', 'Vitaminas'): 12,
   ('Pera', 'Carbohidratos'): 11.7,
   ('Pera', 'Prote�na'): 0.4,
   ('Pera', 'Grasas'): 0.1,
   ('Br�coli', 'Vitaminas'): 116,
   ('Br�coli', 'Carbohidratos'): 4.9,
   ('Br�coli', 'Prote�na'): 3.2,
   ('Br�coli', 'Grasas'): 0.2,
   ('Espinaca', 'Vitaminas'): 52,
   ('Espinaca', 'Carbohidratos'): 4.1,
   ('Espinaca', 'Prote�na'): 2.5,
   ('Espinaca', 'Grasas'): 0.3,
   ('Guisantes', 'Vitaminas'): 23,
   ('Guisantes', 'Carbohidratos'): 18.2,
   ('Guisantes', 'Prote�na'): 7.2,
   ('Guisantes', 'Grasas'): 0.4,
   ('Pepino', 'Vitaminas'): 9,
   ('Pepino', 'Carbohidratos'): 0.7,
   ('Pepino', 'Prote�na'): 0.15,
   ('Pepino', 'Grasas'): 2.7,
   ('Calabac�n', 'Vitaminas'): 21,
   ('Calabac�n', 'Carbohidratos'): 7.3,
   ('Calabac�n', 'Prote�na'): 4.2,
   ('Calabac�n', 'Grasas'): 0.1,
   ('Pollo', 'Vitaminas'): 61,
   ('Pollo', 'Carbohidratos'): 1,
   ('Pollo', 'Prote�na'): 23,
   ('Pollo', 'Grasas'): 2,
   ('Res', 'Vitaminas'): 31,
   ('Res', 'Carbohidratos'): 2,
   ('Res', 'Prote�na'): 18,
   ('Res', 'Grasas'): 20,
   ('Cerdo', 'Vitaminas'): 2,
   ('Cerdo', 'Carbohidratos'): 1.5,
   ('Cerdo', 'Prote�na'): 16,
   ('Cerdo', 'Grasas'): 27}

#Costo por porci�n (100g) de alimento a
c={'Naranja': 570,
   'Manzana': 650,
   'Banano': 200,
   'Pera': 550,
   'Br�coli': 450,
   'Espinaca': 600,
   'Guisantes': 800,
   'Pepino': 500,
   'Calabac�n': 450,
   'Pollo': 1420,
   'Res': 4800,
   'Cerdo': 2900}

#Si el alimento a pertenece al tipo de alimento t
p={('Naranja', 'Frutas'): 1,
   ('Naranja', 'Verduras'): 0,
   ('Naranja', 'Carnes'): 0,
   ('Manzana', 'Frutas'): 1,
   ('Manzana', 'Verduras'): 0,
   ('Manzana', 'Carnes'): 0,
   ('Banano', 'Frutas'): 1,
   ('Banano', 'Verduras'): 0,
   ('Banano', 'Carnes'): 0,
   ('Pera', 'Frutas'): 1,
   ('Pera', 'Verduras'): 0,
   ('Pera', 'Carnes'): 0,
   ('Br�coli', 'Frutas'): 0,
   ('Br�coli', 'Verduras'): 1,
   ('Br�coli', 'Carnes'): 0,
   ('Espinaca', 'Frutas'): 0,
   ('Espinaca', 'Verduras'): 1,
   ('Espinaca', 'Carnes'): 0,
   ('Guisantes', 'Frutas'): 0,
   ('Guisantes', 'Verduras'): 1,
   ('Guisantes', 'Carnes'): 0,
   ('Pepino', 'Frutas'): 0,
   ('Pepino', 'Verduras'): 1,
   ('Pepino', 'Carnes'): 0,
   ('Calabac�n', 'Frutas'): 0,
   ('Calabac�n', 'Verduras'): 1,
   ('Calabac�n', 'Carnes'): 0,
   ('Pollo', 'Frutas'): 0,
   ('Pollo', 'Verduras'): 0,
   ('Pollo', 'Carnes'): 1,
   ('Res', 'Frutas'): 0,
   ('Res', 'Verduras'): 0,
   ('Res', 'Carnes'): 1,
   ('Cerdo', 'Frutas'): 0,
   ('Cerdo', 'Verduras'): 0,
   ('Cerdo', 'Carnes'): 1}

#%%
#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("Planeaci�nMen�s",lp.LpMinimize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',A,lowBound=0,cat='Continuous') #Cantidad de porciones del alimento a incluidas en el men�

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de minimizaci�n de costos
problema+=lp.lpSum(c[a]*x[a] for a in A)

#-----------------------------
# Restricciones
#-----------------------------
#Se garantizan 100 gramos por cada tipo de alimento
for t in T:
    problema+=lp.lpSum(x[a] for a in A if p[a,t]==1)==1, "100 gramos del tipo de alimento " + t
    
#Se garantiza el requerimiento m�nimo de cada aspecto nutricional
for n in N:
    problema+=lp.lpSum(k[a,n]*x[a] for a in A)>=l[n], "M�nimo aspecto nutricional " + n

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#%%
#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("Planeaci�nMen�s.lp")

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')

#Valor �ptimo del costo del men�  
print("\nPlaneaci�n Men�s - Costos Totales = $", round(lp.value(problema.objective),2))

#Imprimir variables de decisi�n
print("Variables de decisi�n\n")
for t in T:
    print(t)
    for a in A:
        if p[a,t]==1:
            print("\t",a,":",round(x[a].value()*100,1),"gramos")

<div style="text-align:justify"><strong>c.</strong> Varios aspectos pr�cticos no fueron tenidos en cuenta en el modelo planteado
anteriormente. Algunos de estos aspectos son: la inclusi�n de alimentos de los otros cuatro
grupos alimenticios, la planeaci�n de men�s para desayunos, almuerzos y cenas; la
planeaci�n de men�s para que los pacientes reciban men�s variados de comida a lo largo
de la semana; y men�s especiales para pacientes con ciertas restricciones, entre otros.
Discuta en detalle c�mo podr�a tener en cuenta estos aspectos dentro de un modelo de
optimizaci�n en el sistema de planeaci�n del hospital.
</div>

## Cr�ditos

Desarrollador: Camilo Aguilar Le�n<br>
Fecha: 08/09/2020