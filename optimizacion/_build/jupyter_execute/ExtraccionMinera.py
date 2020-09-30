# Extracci�n minera Soluci�n

## Punto 1

### Enunciado
La miner�a de cielo abierto es una actividad industrial que consiste en remover grandes cantidades de suelo para extraer el mineral deseado. Este tipo de minas son comunes en la extracci�n de materiales como: arena, arcilla, cobre y carb�n. Las directivas de una empresa de extracci�n minera desean explotar un conjunto de zonas ($M$), de las cuales se puede extraer un conjunto de diferentes tipos de carb�n ($K$). Se sabe que de la zona $i\in M$ s�lo puede extraerse el carb�n tipo $j\in K$. Para ello, suponga que $a_{ij}$ es un par�metro binario que toma el valor de 1 si en la zona $i\in M$ se puede extraer carb�n del tipo $j\in K$ y 0 en el caso contrario. La Figura 1 presenta un ejemplo en el cual hay 36 zonas y 4 tipos de carb�n. Por ejemplo, para la zona uno se tiene que $a_{11}=0$, $a_{12}=1$, $a_{13}=0$ y $a_{14}=0$ ya que de la zona 1 s�lo puede extraerse el tipo de carb�n 2 (hulla). 

*Figura 1:*
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: lightblue">1</td>
	<td style="text-align:center; background-color: lightblue">2</td>
	<td style="text-align:center; background-color: green">3</td>
    <td style="text-align:center; background-color: green">4</td> 
    <td style="text-align:center; background-color: lightblue">5</td>
    <td style="text-align:center; background-color: green">6</td>
  </tr>
  <tr id="ROW2">
	<td style="text-align:center; background-color: lightblue">7</td>
	<td style="text-align:center; background-color: lightblue">8</td>
	<td style="text-align:center; background-color: purple">9</td>
    <td style="text-align:center; background-color: purple">10</td> 
    <td style="text-align:center; background-color: lightblue">11</td>
    <td style="text-align:center; background-color: green">12</td>
  </tr>
  <tr id="ROW3">
	<td style="text-align:center; background-color: purple">13</td>
	<td style="text-align:center; background-color: green">14</td>
	<td style="text-align:center; background-color: green">15</td>
    <td style="text-align:center; background-color: lightblue">16</td> 
    <td style="text-align:center; background-color: lightblue">17</td>
    <td style="text-align:center; background-color: green">18</td>
  </tr>
  <tr id="ROW4">
	<td style="text-align:center; background-color: purple">19</td>
	<td style="text-align:center; background-color: red">20</td>
	<td style="text-align:center; background-color: green">21</td>
    <td style="text-align:center; background-color: purple">22</td> 
    <td style="text-align:center; background-color: purple">23</td>
    <td style="text-align:center; background-color: purple">24</td>
  </tr>
  <tr id="ROW5">
	<td style="text-align:center; background-color: purple">25</td>
	<td style="text-align:center; background-color: green">26</td>
	<td style="text-align:center; background-color: green">27</td>
    <td style="text-align:center; background-color: red">28</td> 
    <td style="text-align:center; background-color: red">29</td>
    <td style="text-align:center; background-color: red">30</td>
  </tr>
  <tr id="ROW6">
	<td style="text-align:center; background-color: lightblue">31</td>
	<td style="text-align:center; background-color: green">32</td>
	<td style="text-align:center; background-color: lightblue">33</td>
    <td style="text-align:center; background-color: purple">34</td> 
    <td style="text-align:center; background-color: red">35</td>
    <td style="text-align:center; background-color: purple">36</td>
  </tr>
</table>
<br>
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: purple">Antracita</td>
	<td style="text-align:center; background-color: lightblue">Hulla</td>
	<td style="text-align:center; background-color: green">Turba</td>
    <td style="text-align:center; background-color: red">Lignito</td> 
  </tr>
</table>

Cada tonelada de carb�n extra�da de la zona $i\in M$ le cuesta a la empresa $c_i$ pesos.  Adicionalmente, cada zona tiene una capacidad m�xima de extracci�n de carb�n de $n_i$ toneladas. Suponga que las directivas desean explotar un m�nimo de $b_j$ toneladas de cada tipo de carb�n $j\in K$.    
<br> 
Usted debe formular un programa lineal que le permita a la empresa decidir cu�nto deben extraer en cada zona de manera que se cumplan los requerimientos a un m�nimo costo. Para esto usted debe seguir los siguientes pasos: 

### Formulaci�n
#### Variables de decisi�n
**a.** Describa la(s) variable(s) de decisi�n que utilizar� en el modelo. 

\begin{align}
x_i: \text{cantidad de carb�n extra�do en la zona $i\in M$ (en toneladas)}\\
\end{align}

#### Restricciones
**b.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) la cantidad de carb�n extra�do del tipo $j\in K$, debe como m�nimo $b_j$.    

*Opci�n 1:*
\begin{align}
\sum_{i\in M}a_{ij}x_i &\ge b_j, &&\forall j\in K.\\
\end{align}

*Opci�n 2:*
\begin{align}
\sum_{i\in M|a_{ij}=1}x_i &\ge b_j, &&\forall j\in K.\\
\end{align}

**c.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que no se pueden extraer m�s de ($n_i$) toneladas de carb�n en la zona $i\in M$.   

\begin{align}
x_i &\le n_i, &&\forall i\in M.
\end{align}

#### Naturaleza de las variables
**d.** Escriba la(s) restricci�n(es) que describe(n) la naturaleza de la(s) variable(s) incluida(s) en el modelo. 

\begin{align}
x_i &\ge 0, &&\forall i\in M.
\end{align}

#### Funci�n Objetivo
**e.** Escriba la funci�n objetivo.

$$
\text{minimizar }  \sum_{i\in M}x_ic_i 
$$

### Formulaci�n matem�tica completa

**Conjuntos:**
- $M$: Zonas
- $K$: Tipos de carb�n

**Par�metros:**
- $a_{ij}:\begin{cases}1&\text{, si en la zona }i\in M\text{ se puede extraer carb�n del tipo }j\in K \\ 0 & \text{, d.l.c}  \end{cases}$
- $c_i$: costo por cada tonelada de carb�n extra�da en la zona $i\in M$  
- $n_i$: capacidad m�xima de extracci�n de carb�n (en toneladas) en la zona $i\in M$
- $b_j$: m�nimo de toneladas a explotar del tipo de carb�n $j\in K$

**Variables de decisi�n:**
- $x_i$: toneladas de carb�n extra�do en la zona $i\in M$  

**Modelo:**

$$
\text{minimizar }  \sum_{i\in M}x_ic_i \text{ (1)} 
$$

Sujeto a,
\begin{align*}
\sum_{i\in M}a_{ij}x_i &\ge b_j, &&\forall j\in K; &(2)\\
x_i &\le n_i, &&\forall i\in M; &(3)\\
x_i &\ge 0, &&\forall i\in M. &(4)
\end{align*}


La funci�n objetivo (1) minimiza los costos totales. La restricci�n (2) describe que la cantidad de carb�n extra�do del tipo $j\in K$ debe ser m�nimo $b_j$ toneladas. La restricci�n (3) describe que no se pueden extraer m�s de ($n_i$) toneladas de carb�n en la zona $i\in M$. La restricci�n (4) describe la naturaleza de la variable $x_i$. 

### Implementaci�n
**g.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Zonas
M=[]
for i in range(1,37):
    M.append(i)

#Tipos de carb�n
K=["Antracita",
   "Hulla",
   "Turba",
   "Lignito"]

#-----------------
# Par�metros
#-----------------
a={#(zona, tipo de carb�n): 1 si en la zona i se puede extraer carb�n del tipo j, 0 d.l.c.
    (1,"Antracita"):0,
    (1,"Hulla"):1,
    (1,"Turba"):0,
    (1,"Lignito"):0,
    (2,"Antracita"):0,
    (2,"Hulla"):1,
    (2,"Turba"):0,
    (2,"Lignito"):0,
    (3,"Antracita"):0,
    (3,"Hulla"):0,
    (3,"Turba"):1,
    (3,"Lignito"):0,
    (4,"Antracita"):0,
    (4,"Hulla"):0,
    (4,"Turba"):1,
    (4,"Lignito"):0,
    (5,"Antracita"):0,
    (5,"Hulla"):1,
    (5,"Turba"):0,
    (5,"Lignito"):0,
    (6,"Antracita"):0,
    (6,"Hulla"):0,
    (6,"Turba"):1,
    (6,"Lignito"):0,
    (7,"Antracita"):0,
    (7,"Hulla"):1,
    (7,"Turba"):0,
    (7,"Lignito"):0,
    (8,"Antracita"):0,
    (8,"Hulla"):1,
    (8,"Turba"):0,
    (8,"Lignito"):0,
    (9,"Antracita"):1,
    (9,"Hulla"):0,
    (9,"Turba"):0,
    (9,"Lignito"):0,
    (10,"Antracita"):1,
    (10,"Hulla"):0,
    (10,"Turba"):0,
    (10,"Lignito"):0,
    (11,"Antracita"):0,
    (11,"Hulla"):1,
    (11,"Turba"):0,
    (11,"Lignito"):0,
    (12,"Antracita"):0,
    (12,"Hulla"):0,
    (12,"Turba"):1,
    (12,"Lignito"):0,
    (13,"Antracita"):1,
    (13,"Hulla"):0,
    (13,"Turba"):0,
    (13,"Lignito"):0,
    (14,"Antracita"):0,
    (14,"Hulla"):0,
    (14,"Turba"):1,
    (14,"Lignito"):0,
    (15,"Antracita"):0,
    (15,"Hulla"):0,
    (15,"Turba"):1,
    (15,"Lignito"):0,
    (16,"Antracita"):0,
    (16,"Hulla"):1,
    (16,"Turba"):0,
    (16,"Lignito"):0,
    (17,"Antracita"):0,
    (17,"Hulla"):1,
    (17,"Turba"):0,
    (17,"Lignito"):0,
    (18,"Antracita"):0,
    (18,"Hulla"):0,
    (18,"Turba"):1,
    (18,"Lignito"):0,
    (19,"Antracita"):1,
    (19,"Hulla"):0,
    (19,"Turba"):0,
    (19,"Lignito"):0,
    (20,"Antracita"):0,
    (20,"Hulla"):0,
    (20,"Turba"):0,
    (20,"Lignito"):1,
    (21,"Antracita"):0,
    (21,"Hulla"):0,
    (21,"Turba"):1,
    (21,"Lignito"):0,
    (22,"Antracita"):1,
    (22,"Hulla"):0,
    (22,"Turba"):0,
    (22,"Lignito"):0,
    (23,"Antracita"):1,
    (23,"Hulla"):0,
    (23,"Turba"):0,
    (23,"Lignito"):0,
    (24,"Antracita"):1,
    (24,"Hulla"):0,
    (24,"Turba"):0,
    (24,"Lignito"):0,
    (25,"Antracita"):1,
    (25,"Hulla"):0,
    (25,"Turba"):0,
    (25,"Lignito"):0,
    (26,"Antracita"):0,
    (26,"Hulla"):0,
    (26,"Turba"):1,
    (26,"Lignito"):0,
    (27,"Antracita"):0,
    (27,"Hulla"):0,
    (27,"Turba"):1,
    (27,"Lignito"):0,
    (28,"Antracita"):0,
    (28,"Hulla"):0,
    (28,"Turba"):0,
    (28,"Lignito"):1,
    (29,"Antracita"):0,
    (29,"Hulla"):0,
    (29,"Turba"):0,
    (29,"Lignito"):1,
    (30,"Antracita"):0,
    (30,"Hulla"):0,
    (30,"Turba"):0,
    (30,"Lignito"):1,
    (31,"Antracita"):0,
    (31,"Hulla"):1,
    (31,"Turba"):0,
    (31,"Lignito"):0,
    (32,"Antracita"):0,
    (32,"Hulla"):0,
    (32,"Turba"):1,
    (32,"Lignito"):0,
    (33,"Antracita"):0,
    (33,"Hulla"):1,
    (33,"Turba"):0,
    (33,"Lignito"):0,
    (34,"Antracita"):1,
    (34,"Hulla"):0,
    (34,"Turba"):0,
    (34,"Lignito"):0,
    (35,"Antracita"):0,
    (35,"Hulla"):0,
    (35,"Turba"):0,
    (35,"Lignito"):1,
    (36,"Antracita"):1,
    (36,"Hulla"):0,
    (36,"Turba"):0,
    (36,"Lignito"):0} 

datosZonas={#zona: [costo por cada tonelada de carb�n extra�da en la zona i, capacidad m�xima de extracci�n de carb�n (en toneladas) en la zona i] 
            (1):[16,189],
            (2):[6,196],
            (3):[11,143],
            (4):[8,136],
            (5):[5,106],
            (6):[25,151],
            (7):[16,170],
            (8):[17,129],
            (9):[25,184],
            (10):[8,122],
            (11):[15,146],
            (12):[8,190],
            (13):[10,160],
            (14):[20,109],
            (15):[6,133],
            (16):[17,198],
            (17):[6,138],
            (18):[20,107],
            (19):[5,117],
            (20):[8,150],
            (21):[25,171],
            (22):[11,103],
            (23):[8,157],
            (24):[7,143],
            (25):[7,170],
            (26):[28,130],
            (27):[26,140],
            (28):[27,126],
            (29):[9,180],
            (30):[24,153],
            (31):[15,108],
            (32):[14,132],
            (33):[22,105],
            (34):[20,145],
            (35):[19,145],
            (36):[8,114]}  

#par�metros indexados en las zonas
(c, n)=lp.splitDict(datosZonas)


b={#m�nimo de toneladas a explotar del tipo de carb�n j
    ("Antracita"):862,
    ("Hulla"):898,
    ("Turba"):562,
    ("Lignito"):742}  

#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("Extracci�n Minera",lp.LpMinimize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',M,lowBound=0,cat='Continuous') #toneladas de carb�n extra�do de la zona i; aca se a�ade de una vez la naturaleza de las variables

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de minimizaci�n de costos
problema+=lp.lpSum(x[i]*c[i] for i in M), "Costos Totales"

#-----------------------------
# Restricciones
#-----------------------------
#sum(i in M)a_ij*x_i >= b_j forall j in K
for j in K:
    problema+= lp.lpSum(a[i,j]*x[i] for i in M) >= b[j], "M�nimo toneladas de extracci�n del tipo de carb�n "+j #se garantiza el m�nimo de toneladas extraidas del tipo de carb�n j

#x_i <= n_i*y_i forall i in M
for i in M:
    problema+= x[i] <= n[i], "M�ximo toneladas de extracci�n de la zona "+str(i)   #se garantiza el m�ximo de toneladas de carb�n que se pueden extraer de la zona i

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("ExtraccionMinera.lp")

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
print("\nExtracci�n Minera - \033[1m Costos totales \033[0m = $", round(lp.value(problema.objective),2))
print()

#Imprimir variables de decisi�n
print('\033[1m'"Extracci�n de las zonas"'\033[0m')
for i in M:
    if x[i].value()>0.5:
        for j in K:
            if a[i,j]==1:
                print(str(i)+": "+str(x[i].value())+" toneladas de "+j)




## Punto 2

### Enunciado
Ahora considere el escenario en que la empresa incurre en un costo fijo de $q_i$ pesos cuando decide extraer carb�n de la zona $i\in M$. Por lo tanto, si se decide explotar la mina $i\in M$, no se pueden extraer m�s de ($n_i$) toneladas de carb�n. Pero si no se decide explotar, la extracci�n de carb�n en esa zona debe ser igual a cero (0). Para esto usted debe seguir los siguientes pasos: 

### Formulaci�n
#### Variables de decisi�n
**a.** Describa la(s) variable(s) de decisi�n adicional(es) que utilizar� en el modelo. 

\begin{align*}
y_i:\begin{cases}1&\text{, si se decide explotar la zona }i\in M \\ 0 & \text{, d.l.c}  \end{cases}
\end{align*}

#### Restricciones
**b.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que si se decide explotar la mina $i\in M$, no se pueden extraer m�s de ($n_i$) toneladas de carb�n. Pero que, si no se decide explotar, la extracci�n de carb�n debe ser igual a cero.    

\begin{align}
x_i &\le n_iy_i, &&\forall i\in M.
\end{align}

#### Naturaleza de las variables
**c.** Escriba la(s) restricci�n(es) que describe(n) la naturaleza de la(s) variable(s) adicional(es).

\begin{align}
y_i &\in \text{{0,1}}, &&\forall i\in M.
\end{align}

#### Funci�n Objetivo
**e.** Escriba la funci�n objetivo.

$$
\text{minimizar }  \sum_{i\in M}y_iq_i+\sum_{i\in M}x_ic_i
$$

### Formulaci�n matem�tica completa

**Conjuntos:**
- $M$: Zonas
- $K$: Tipos de carb�n

**Par�metros:**
- $a_{ij}:\begin{cases}1&\text{, si en la zona }i\in M\text{ se puede extraer carb�n del tipo }j\in K \\ 0 & \text{, d.l.c}  \end{cases}$
- $c_i$: costo por cada tonelada de carb�n extra�da en la zona $i\in M$  
- $n_i$: capacidad m�xima de extracci�n de carb�n (en toneladas) en la zona $i\in M$
- $b_j$: m�nimo de toneladas a explotar del tipo de carb�n $j\in K$
- $q_i$: costo fijo si se decide extraer carb�n de la zona $i\in M$

**Variables de decisi�n:**
- $x_i$: toneladas de carb�n extra�do en la zona $i\in M$ 
- $y_i:\begin{cases}1&\text{, si se decide explotar la zona} i\in M \\ 0 & \text{, d.l.c}  \end{cases}$ 

**Modelo:**

$$
\text{minimizar }  \sum_{i\in M}y_iq_i+\sum_{i\in M}x_ic_i \text{ (1)} 
$$

Sujeto a,
\begin{align*}
\sum_{i\in M|a_{ij}=1}x_i &\ge b_j, &&\forall j\in K; &(2)\\
x_i &\le n_iy_i, &&\forall i\in M; &(3)\\
x_i &\ge 0, &&\forall i\in M; &(4)\\
y_i &\in \text{{0,1}}, &&\forall i\in M. &(5)
\end{align*}


La funci�n objetivo (1) minimiza los costos totales. La restricci�n (2) describe que la cantidad de carb�n extra�do del tipo $j\in K$ debe ser m�nimo $b_j$ toneladas. La restricci�n (3) describe que si se decide explotar la mina $i\in M$, no se pueden extraer m�s de ($n_i$) toneladas de carb�n, pero que si no se decide explotar, la extracci�n de carb�n debe ser igual a cero. Las restricciones (4) y (5) describen la naturaleza de las variables $x_i$ y $y_i$. 

### Implementaci�n
**f.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Zonas
M=[]
for i in range(1,37):
    M.append(i)

#Tipos de carb�n
K=["Antracita",
   "Hulla",
   "Turba",
   "Lignito"]

#-----------------
# Par�metros
#-----------------
a={#(zona, tipo de carb�n): 1 si en la zona i se puede extraer carb�n del tipo j, 0 d.l.c.
    (1,"Antracita"):0,
    (1,"Hulla"):1,
    (1,"Turba"):0,
    (1,"Lignito"):0,
    (2,"Antracita"):0,
    (2,"Hulla"):1,
    (2,"Turba"):0,
    (2,"Lignito"):0,
    (3,"Antracita"):0,
    (3,"Hulla"):0,
    (3,"Turba"):1,
    (3,"Lignito"):0,
    (4,"Antracita"):0,
    (4,"Hulla"):0,
    (4,"Turba"):1,
    (4,"Lignito"):0,
    (5,"Antracita"):0,
    (5,"Hulla"):1,
    (5,"Turba"):0,
    (5,"Lignito"):0,
    (6,"Antracita"):0,
    (6,"Hulla"):0,
    (6,"Turba"):1,
    (6,"Lignito"):0,
    (7,"Antracita"):0,
    (7,"Hulla"):1,
    (7,"Turba"):0,
    (7,"Lignito"):0,
    (8,"Antracita"):0,
    (8,"Hulla"):1,
    (8,"Turba"):0,
    (8,"Lignito"):0,
    (9,"Antracita"):1,
    (9,"Hulla"):0,
    (9,"Turba"):0,
    (9,"Lignito"):0,
    (10,"Antracita"):1,
    (10,"Hulla"):0,
    (10,"Turba"):0,
    (10,"Lignito"):0,
    (11,"Antracita"):0,
    (11,"Hulla"):1,
    (11,"Turba"):0,
    (11,"Lignito"):0,
    (12,"Antracita"):0,
    (12,"Hulla"):0,
    (12,"Turba"):1,
    (12,"Lignito"):0,
    (13,"Antracita"):1,
    (13,"Hulla"):0,
    (13,"Turba"):0,
    (13,"Lignito"):0,
    (14,"Antracita"):0,
    (14,"Hulla"):0,
    (14,"Turba"):1,
    (14,"Lignito"):0,
    (15,"Antracita"):0,
    (15,"Hulla"):0,
    (15,"Turba"):1,
    (15,"Lignito"):0,
    (16,"Antracita"):0,
    (16,"Hulla"):1,
    (16,"Turba"):0,
    (16,"Lignito"):0,
    (17,"Antracita"):0,
    (17,"Hulla"):1,
    (17,"Turba"):0,
    (17,"Lignito"):0,
    (18,"Antracita"):0,
    (18,"Hulla"):0,
    (18,"Turba"):1,
    (18,"Lignito"):0,
    (19,"Antracita"):1,
    (19,"Hulla"):0,
    (19,"Turba"):0,
    (19,"Lignito"):0,
    (20,"Antracita"):0,
    (20,"Hulla"):0,
    (20,"Turba"):0,
    (20,"Lignito"):1,
    (21,"Antracita"):0,
    (21,"Hulla"):0,
    (21,"Turba"):1,
    (21,"Lignito"):0,
    (22,"Antracita"):1,
    (22,"Hulla"):0,
    (22,"Turba"):0,
    (22,"Lignito"):0,
    (23,"Antracita"):1,
    (23,"Hulla"):0,
    (23,"Turba"):0,
    (23,"Lignito"):0,
    (24,"Antracita"):1,
    (24,"Hulla"):0,
    (24,"Turba"):0,
    (24,"Lignito"):0,
    (25,"Antracita"):1,
    (25,"Hulla"):0,
    (25,"Turba"):0,
    (25,"Lignito"):0,
    (26,"Antracita"):0,
    (26,"Hulla"):0,
    (26,"Turba"):1,
    (26,"Lignito"):0,
    (27,"Antracita"):0,
    (27,"Hulla"):0,
    (27,"Turba"):1,
    (27,"Lignito"):0,
    (28,"Antracita"):0,
    (28,"Hulla"):0,
    (28,"Turba"):0,
    (28,"Lignito"):1,
    (29,"Antracita"):0,
    (29,"Hulla"):0,
    (29,"Turba"):0,
    (29,"Lignito"):1,
    (30,"Antracita"):0,
    (30,"Hulla"):0,
    (30,"Turba"):0,
    (30,"Lignito"):1,
    (31,"Antracita"):0,
    (31,"Hulla"):1,
    (31,"Turba"):0,
    (31,"Lignito"):0,
    (32,"Antracita"):0,
    (32,"Hulla"):0,
    (32,"Turba"):1,
    (32,"Lignito"):0,
    (33,"Antracita"):0,
    (33,"Hulla"):1,
    (33,"Turba"):0,
    (33,"Lignito"):0,
    (34,"Antracita"):1,
    (34,"Hulla"):0,
    (34,"Turba"):0,
    (34,"Lignito"):0,
    (35,"Antracita"):0,
    (35,"Hulla"):0,
    (35,"Turba"):0,
    (35,"Lignito"):1,
    (36,"Antracita"):1,
    (36,"Hulla"):0,
    (36,"Turba"):0,
    (36,"Lignito"):0} 

datosZonas={#zona: [costo fijo si se decide extraer carb�n de la zona i, costo por cada tonelada de carb�n extra�da en la zona i, capacidad m�xima de extracci�n de carb�n (en toneladas) en la zona i] 
        (1):[240,16,189],
        (2):[155,6,196],
        (3):[240,11,143],
        (4):[125,8,136],
        (5):[177,5,106],
        (6):[342,25,151],
        (7):[157,16,170],
        (8):[457,17,129],
        (9):[396,25,184],
        (10):[411,8,122],
        (11):[341,15,146],
        (12):[469,8,190],
        (13):[402,10,160],
        (14):[186,20,109],
        (15):[404,6,133],
        (16):[344,17,198],
        (17):[290,6,138],
        (18):[340,20,107],
        (19):[482,5,117],
        (20):[472,8,150],
        (21):[394,25,171],
        (22):[102,11,103],
        (23):[330,8,157],
        (24):[433,7,143],
        (25):[205,7,170],
        (26):[394,28,130],
        (27):[156,26,140],
        (28):[298,27,126],
        (29):[134,9,180],
        (30):[462,24,153],
        (31):[432,15,108],
        (32):[362,14,132],
        (33):[127,22,105],
        (34):[203,20,145],
        (35):[417,19,145],
        (36):[215,8,114]} 

#par�metros indexados en las zonas
(q, c, n)=lp.splitDict(datosZonas)

b={#m�nimo de toneladas a explotar del tipo de carb�n j
    ("Antracita"):862,
    ("Hulla"):898,
    ("Turba"):562,
    ("Lignito"):742} 

#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("Extracci�n Minera",lp.LpMinimize)

#-----------------------------
# Variables de Decisi�n
#-----------------------------
x=lp.LpVariable.dicts('x',M,lowBound=0,cat='Continuous') #toneladas de carb�n extra�do de la zona i; aca se a�ade de una vez la naturaleza de las variables
y=lp.LpVariable.dicts('y',M,cat='Binary') #1 si se decide explotar la zona i, 0 d.l.c. ; aca se a�ade de una vez la naturaleza 

#-----------------------------
# Funci�n objetivo
#-----------------------------
#Crea la expresi�n de minimizaci�n de costos
problema+=lp.lpSum(x[i]*c[i]+y[i]*q[i] for i in M), "Costos Totales"

#-----------------------------
# Restricciones
#-----------------------------
#sum(i in M |a_ij=1)x_i >= b_j forall j in K
for j in K:
    problema+= lp.lpSum(x[i] for i in M if a[i,j]==1) >= b[j], "M�nimo toneladas de extracci�n del tipo de carb�n "+j #se garantiza el m�nimo de toneladas extraidas del tipo de carb�n j

#x_i <= n_i*y_i forall i in M
for i in M:
    problema+= x[i] <= n[i]*y[i], "Maximo toneladas de extracci�n si se decide explotar la zona "+str(i)   #se garantiza el m�ximo de toneladas de carb�n que se pueden extraer si se decide explotar la zona i

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("ExtraccionMinera.lp")

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
print("\nExtracci�n Minera - \033[1m Costos totales \033[0m = $", round(lp.value(problema.objective),2))
print()

#Imprimir variables de decisi�n
print('\033[1m'"Extracci�n de las zonas"'\033[0m')
for i in M:
    if x[i].value()>0.5:
        for j in K:
            if a[i,j]==1:
                print(str(i)+": "+str(x[i].value())+" toneladas de "+j)

## Cr�ditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 12/09/2020