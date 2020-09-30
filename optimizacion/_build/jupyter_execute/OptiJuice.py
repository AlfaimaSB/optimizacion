# OptiJuice Soluci�n

## Enunciado

OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos aut�ctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la pi�a, la guayaba, el n�spero y el zapote. Cada uno de los tipos de jugo se diferencia de los dem�s en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producci�n de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compa��a espera una demanda m�nima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. 

Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: �Cu�ntos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

## Formulaci�n

### Variables de Decisi�n

**a.** Describa la(s) variable(s) de decisi�n que utilizar� en el modelo. 

\begin{align*}
x_{ki}: \text{cantidad (en litros) del zumo de la fruta $i\in R$ destinados a la producci�n del jugo de tipo $k\in K$}
\end{align*}

### Restricciones

**b.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. 

\begin{align*}
x_{ki} &\ge l_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R;\\
x_{ki} &\le u_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R.
\end{align*}

**c.** Escriba la(s) restricci�n(es) que describe(n) que OptiJuice puede utilizar m�ximo $b_i$ litros de zumo de la fruta $i\in R$. 

\begin{align*}
\sum_{k\in K} x_{ki} &\le b_i, &&\forall i\in R.
\end{align*}

**d.** Escriba la(s) restricci�n(es) que describe(n) que OptiJuice desea cumplir con la demanda m�nima de $d_k$ litros jugo del tipo $k\in K$. 

\begin{align*}
\sum_{i\in R} x_{ki} &\ge d_k, &&\forall k\in K.
\end{align*}

### Naturaleza de las Variables
**e.** Escriba la(s) restricci�n(es) que describe(n) matem�ticamente el tipo de variable(s) que est� utilizando dentro del modelo. 

\begin{align*}
x_{ki} & \ge 0, &&\forall k\in K,i\in R.
\end{align*}

### Funci�n Objetivo

**f.** Escriba la funci�n objetivo que maximiza los ingresos totales.

$$
\text{maximizar }  \sum_{k\in K}\sum_{i\in R}p_kx_{ki}
$$

## Formulaci�n matem�tica

**Conjuntos:**

- $K$: Jugos aut�ctonos
- $R$: Frutas tropicales

**Par�metros:**

- $l_{ki}$%: porcentaje m�nimo de litros de zumo de la fruta $i\in R$ que tiene que tener el jugo del tipo $k\in K$
- $u_{ki}$%: porcentaje m�ximo de litros de zumo de la fruta $i\in R$ que tiene que tener el jugo del tipo $k\in K$
- $b_i$: litros de zumo de la fruta $i\in R$ disponibles
- $d_k$: demanda m�nima (en litros) del jugo de tipo $k\in K$ 
- $p_k$: precio de un litro del jugo de tipo $k\in K$

**Variables de decisi�n:**

- $x_{ki}$: cantidad (en litros) del zumo de la fruta $i\in R$ destinados a la producci�n del jugo de tipo $k\in K$

**Modelo:**

$$
\text{maximizar }  \sum_{k\in K}\sum_{i\in R}p_kx_{ki} \text{ (1)} 
$$

Sujeto a,
\begin{align*}
x_{ki} &\ge l_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R; &(2)\\
x_{ki} &\le u_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R; &(3)\\
\sum_{k\in K} x_{ki} &\le b_i, &&\forall i\in R; &(4)\\
\sum_{i\in R} x_{ki} &\ge d_k, &&\forall k\in K; &(5)\\
x_{ki} & \ge 0, &&\forall k\in K,i\in R. &(6)
\end{align*}

La funci�n objetivo (1) maximiza los ingresos totales. Las restricciones (2) y (3) describen que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. La restricci�n (4) describe que OptiJuice puede utilizar m�ximo $b_i$ litros de zumo de la fruta $i\in R$. La restricci�n (5) describe que OptiJuice desea cumplir con la demanda m�nima de $d_k$ litros jugo del tipo $k\in K$. La restricci�n (6) describe la naturaleza de la variable $x_{ki}$. 

## Implementaci�n

**g.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Jugos
K=["Saludable", 
   "Tropical", 
   "Ma�anero", 
   "Colombiano", 
   "Refrescante", 
   "Light"]

#Frutas
R=["Pi�a", 
   "Guayaba", 
   "N�spero", 
   "Zapote"]

# Conjunto con todas las duplas (pozo,tiempo)
K_x_R = [(jugo, fruta) for jugo in K for fruta in R] 

#-----------------
# Par�metros
#-----------------
l={#(jugo, fruta): porcentaje m�nimo de litros de la fruta i en el jugo k
   ("Saludable", "Pi�a"):0.32,
   ("Saludable", "Guayaba"):0.27, 
   ("Saludable", "N�spero"):0.12, 
   ("Saludable", "Zapote"):0.13, 
   ("Tropical", "Pi�a"):0.18, 
   ("Tropical", "Guayaba"):0.30, 
   ("Tropical", "N�spero"):0.31, 
   ("Tropical", "Zapote"):0.34, 
   ("Ma�anero", "Pi�a"):0.07, 
   ("Ma�anero", "Guayaba"):0.31, 
   ("Ma�anero", "N�spero"):0.28, 
   ("Ma�anero", "Zapote"):0.22, 
   ("Colombiano", "Pi�a"):0.11, 
   ("Colombiano", "Guayaba"):0.05,
   ("Colombiano", "N�spero"):0.15,
   ("Colombiano", "Zapote"):0.18,
   ("Refrescante", "Pi�a"):0.46,
   ("Refrescante", "Guayaba"):0.50,
   ("Refrescante", "N�spero"):0.02,
   ("Refrescante", "Zapote"):0.43,
   ("Light", "Pi�a"):0.36,
   ("Light", "Guayaba"):0.19,
   ("Light", "N�spero"):0.14,
   ("Light", "Zapote"):0.40} 

u={#(jugo, fruta): porcentaje m�ximo de litros de la fruta i en el jugo k
   ("Saludable", "Pi�a"):0.95,
   ("Saludable", "Guayaba"):0.83, 
   ("Saludable", "N�spero"):0.66, 
   ("Saludable", "Zapote"):0.87, 
   ("Tropical", "Pi�a"):0.92, 
   ("Tropical", "Guayaba"):0.76, 
   ("Tropical", "N�spero"):0.69, 
   ("Tropical", "Zapote"):0.56, 
   ("Ma�anero", "Pi�a"):0.81, 
   ("Ma�anero", "Guayaba"):0.61, 
   ("Ma�anero", "N�spero"):0.28, 
   ("Ma�anero", "Zapote"):0.94, 
   ("Colombiano", "Pi�a"):0.82, 
   ("Colombiano", "Guayaba"):0.88,
   ("Colombiano", "N�spero"):0.63,
   ("Colombiano", "Zapote"):0.98,
   ("Refrescante", "Pi�a"):0.60,
   ("Refrescante", "Guayaba"):0.85,
   ("Refrescante", "N�spero"):0.73,
   ("Refrescante", "Zapote"):0.78,
   ("Light", "Pi�a"):0.50,
   ("Light", "Guayaba"):0.55,
   ("Light", "N�spero"):0.82,
   ("Light", "Zapote"):0.91} 

b={#fruta: litros disponibles de la fruta i
   "Pi�a":4318, 
   "Guayaba":1902, 
   "N�spero":2683, 
   "Zapote":1111}  

d={#jugo: demanda del jugo k
   "Saludable":1200, 
   "Tropical":925, 
   "Ma�anero":1865, 
   "Colombiano":1035, 
   "Refrescante":2231, 
   "Light":1353} 

p={#jugo: precio del jugo k
   "Saludable":9000, 
   "Tropical":5000, 
   "Ma�anero":6000, 
   "Colombiano":10000, 
   "Refrescante":7000, 
   "Light":8000} 

#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("OptiJuice",lp.LpMaximize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',K_x_R,lowBound=0,cat='Continuous') #litros de la fruta i para producir el jugo k, aca se a�ade de una vez la naturaleza de las variables

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de maximizaci�n de ingresos
problema+=lp.lpSum(p[k]*x[k,i] for k in K for i in R), "Ingresos Totales"

#-----------------------------
# Restricciones
#-----------------------------
for k in K:
    for i in R:
        #x_ki >= l_ki*sum(j in R)x_kj forall k in K, i in R
        problema+= x[k,i] >= l[k,i]*lp.lpSum(x[k,j] for j in R), "M�nimo fruta "+i +" -jugo "+k  #se garantiza el m�nimo de fruta i en el jugo k
        
        #x_ki <= u_ki*sum(j in R)x_kj forall k in K, i in R
        problema+= x[k,i] <= u[k,i]*lp.lpSum(x[k,j] for j in R), "M�ximo fruta "+i +" -jugo "+k  #se garantiza el m�ximo de fruta i en el jugo k

#sum(k in K)x_ki <= b_i forall i in R
for i in R:
    problema+= lp.lpSum(x[k,i] for k in K) <= b[i], "l�mite fruta "+i #se garantiza que no se utilice m�s fruta de la que hay disponible

#sum(i in R)x_ki <= d_k forall k in K
for k in K:
    problema+= lp.lpSum(x[k,i] for i in R) <= d[k], "Demanda m�nima jugo "+k #se satisface la demanda
    
#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("OptiJuice.lp")

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

#Valor �ptimo del portafolio de Petroco    
print("\nOptiJuice - Ingresos totales = $", round(lp.value(problema.objective),2))
print()

#Imprimir variables de decisi�n
print("Variables de decisi�n")
print("              ","Pi�a", "Guayaba", "N�spero", "Zapote",sep='\t')
for k in K:
    print(k,round(x[k,"Pi�a"].value(),2),round(x[k,"Guayaba"].value(),2),round(x[k,"N�spero"].value(),2),round(x[k,"Zapote"].value(),2),sep='\t')






## Cr�ditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 05/09/2020