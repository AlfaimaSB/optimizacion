# Producci�n de cemento Soluci�n

## Enunciado
Artos S.A. es una empresa dedicada a la producci�n de cemento que cuenta con una �nica planta en la ciudad de Barranquilla. La empresa debe determinar la cantidad de toneladas de cemento a producir en cada una de las siguientes 12 semanas. Los costos de producci�n, costos de almacenamiento, as� como la demanda y el precio por tonelada de cemento, var�an semana a semana y se presentan en la siguiente tabla. 



|Semana|Costo de producci�n \[Miles de COP/ton\]|Costo de almacenamiento \[Miles de COP/ton\]|Demanda \[ton\]|Precio \[Miles de COP/ton\]|
|:---:|:---:|:---:|:---:|:---:|
|1|172.8|6.9|95,000|432.0|
|2|178.7|7.2|99,750|440.6|
|3|174.6|8.0|104,738|449.5|
|4|181.4|8.9|109,974|458.4|
|5|183.0|9.0|109,974|467.6|
|6|177.7|7.8|109,974|477.0|
|7|182.8|6.7|120,972|486.5|
|8|186.8|7.3|120,972|496.2|
|9|181.8|7.8|108,875|506.2|
|10|178.3|8.8|97,987|516.3|
|11|173.4|9.2|78,390|526.6|
|12|168.8|8.4|94,068|537.1|

Tenga en cuenta que, al inicio de la planeaci�n, se cuenta con 12,000 toneladas de cemento y que, por especificaciones de la maquinaria, no se puede producir m�s de 110,000 toneladas ni menos de 85,000 toneladas en una semana cualquiera.

## Formulaci�n 
**1.** Formule el problema de optimizaci�n lineal con el fin de determinar la producci�n semanal de Artos y lograr la mayor utilidad posible. Para esto usted debe seguir los siguientes pasos: <br>



**a.** Escriba lo(s) conjunto(s), par�metro(s) y variable(s) de decisi�n que utilizar� en el modelo.

### Conjuntos
- $S$: Conjunto de semanas

### Par�metros
- $d_{i}$: demanda de la semana $i\in S$
- $p_{i}$: precio por tonelada de cemento en la semana $i\in S$
- $c_i$: costo de producir una tonelada de cemento en la semana $i\in S$
- $h_i$: costo de almacenamiento de una tonelada de cemento en la semana $i\in S$
- $I_0$: inventario inicial de toneladas de cemento

### Variables de decisi�n
- $x_{i}$: toneladas de cemento a producir en la semana $i\in S$
- $I_i$: toneladas de cemento que se tienen en inventario al final de la semana $i\in S$


### Restricciones
**b.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que se deben respetar los l�mites de producci�n

\begin{align*}
x_i&\leq 110000, &&\forall i \in S\\
x_i&\geq 85000, &&\forall i \in S\\
\end{align*}

**c.** Escriba la(s) restricci�n(es) lineal(es) que contabiliza(n) el inventario de cada semana

\begin{align*}
I_1&=I_0+x_1-d_1\\
I_i&=I_{i-1}+x_i-d_i,  &&\forall i \in S|i\ge 1
\end{align*}


### Naturaleza de las variables
**d.** Escriba la(s) restricci�n(es) que describe(n) matem�ticamente el tipo de variable(s) que est� utilizando dentro del modelo

\begin{align*}
x_i&\geq 0,&&\forall i \in S\\
I_i&\geq 0,&&\forall i \in S
\end{align*}

### Funci�n Objetivo
**e.** Escriba la funci�n objetivo

\begin{equation*}
    max \sum_{i\in S}d_ip_i-x_ic_i-I_ih_i
\end{equation*}

## Formulaci�n matem�tica completa

**Conjuntos:**
- $S$: Conjunto de semanas

**Par�metros:**
- $d_{i}$: demanda de la semana $i\in S$
- $p_{i}$: precio por tonelada de cemento en la semana $i\in S$
- $c_i$: costo de producir una tonelada de cemento en la semana $i\in S$
- $h_i$: costo de almacenamiento de una tonelada de cemento en la semana $i\in S$
- $I_0$: inventario inicial de toneladas de cemento

**Variables de decisi�n:**
- $x_{i}$: toneladas de cemento a producir en la semana $i\in S$
- $I_i$: toneladas de cemento que se tienen en inventario al final de la semana $i\in S$

\begin{equation*}
    max \sum_{i\in S}d_ip_i-x_ic_i-I_ih_i\text{ (1)}
\end{equation*}

\begin{align*}
x_i&\leq 110000, &&\forall i \in S; &(2)\\
x_i&\geq 85000, &&\forall i \in S; &(3)\\
I_1&=I_0+x_1-d_1,&& &(4)\\
I_i&=I_{i-1}+x_i-d_i,  &&\forall i \in S|i\ge 1;  &(5)\\
x_i&\geq 0,&&\forall i \in S; &(6)\\
I_i&\geq 0,&&\forall i \in S; &(7)
\end{align*}

La funci�n objetivo (1) maximiza las utilidades totales. Las restricciones (2) y (3) garantizan que para cada semana $i\in S$ la producci�n $x_i$ respete los l�mites de producci�n. Las restricciones (4) y (5) contabilizan los inventarios para cada semana $i \in S$. Las restricciones (6) y (7) describen la naturaleza de las variables $x_i$ y $I_i$.

## Implementaci�n
**2.** Resuelva su modelo. Reporte sus resultados de una manera amigable

#%%se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Semanas
S=[i for i in range(1,13)]

#-----------------
# Par�metros
#-----------------
#Se cargan todos los par�metros del modelo
parametros={# Semana: (costo producci�n,costo almacenamiento,demanda,precio)
    1:(172.8,6.9,95000,432.0),
    2:(178.7,7.2,99750,440.6),
    3:(174.6,8.0,104738,449.5),
    4:(181.4,8.9,109974,458.4),
    5:(183.0,9.0,109974,467.6),
    6:(177.7,7.8,109974,477.0),
    7:(182.8,6.7,120972,486.5),
    8:(186.8,7.3,120972,496.2),
    9:(181.8,7.8,108875,506.2),
    10:(178.3,8.8,97987,516.3),
    11:(173.4,9.2,78390,526.6),
    12:(168.8,8.4,94068,537.1)}

#Se separan los par�metros del diccionario general
#Semana: costo de producci�n por tonelada en la semana i
c={i:parametros[i][0] for i in parametros.keys()}

#Semana: costo de almacenamiento por tonelada en la semana i
h={i:parametros[i][1] for i in parametros.keys()}

#Semana: demanda de la semana i
d={i:parametros[i][2] for i in parametros.keys()}

#Semana: precio por tonelada en la semana i
p={i:parametros[i][3] for i in parametros.keys()}


#Inventario inicial de toneladas de cemento
I0=12000

#%%
#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("Inventarios",lp.LpMaximize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',S,lowBound=0,cat='Continuous') #toneladas de cemento a producir en cada semana
I=lp.LpVariable.dicts('I',S,lowBound=0,cat='Continuous') #toneladas de cemento en inventario en cada semana

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de maximizaci�n de utilidades
problema+=lp.lpSum(d[i]*p[i]-x[i]*c[i]-I[i]*h[i] for i in S), "Utilidades Totales"

#-----------------------------
# Restricciones
#-----------------------------
for i in S:
    #Se garantiza que se respeten los limites de producci�n
    problema+=x[i]<=110000, "L�mite superior de producci�n en la semana "+ str(i)
    problema+=x[i]>=85000, "L�mite inferior de producci�n en la semana "+ str(i)
    
    
#Contabilizar los inventarios de cada semana  
problema+=I[1]==I0+x[1]-d[1], "Inventario en la semana 1"
for i in S:
    if i > 1:
        problema+=I[i]==I[i-1]+x[i]-d[i], "Inventario en la semana "+ str(i)

        
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
problema.writeLP("Inventarios.lp")


#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')

#Valor �ptimo del portafolio de Petroco    
print("\nInventarios - Utilidades totales = $", round(lp.value(problema.objective),2)*1000)
print()

#Imprimir variables de decisi�n
print("Variables de decisi�n")
print("Semana","Producci�n (ton)", "Inventario (ton)",sep='\t\t')
for i in S:
    print(i,str(round(x[i].value(),2))+ " \t",round(I[i].value(),2),sep='\t\t')


## Cr�ditos

Desarrollador: Camilo Aguilar Le�n<br>
Fecha: 25/09/2020