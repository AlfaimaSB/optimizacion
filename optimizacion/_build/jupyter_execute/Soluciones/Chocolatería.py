# Chocolater�a Soluci�n

## Enunciado

La chocolater�a Perla Caribe es un peque�o emprendimiento que fabrica y comercializa chocolates artesanales con cacao de distintas variedades comprado directamente a agricultores locales. Actualmente producen dos tipos de chocolates: chocolate oscuro y chocolate blanco. Una unidad de cualquier tipo de chocolate pesa 60g. Una unidad de chocolate oscuro se vende a 7,000 COP y una unidad de chocolate blanco se vende a 6,000 COP. Los costos asociados a materia prima, mano de obra y dem�s costos operacionales equivalen a 3,500 COP por cada unidad de chocolate oscuro y 2,000 COP por cada unidad de chocolate blanco. 

La producci�n de estos chocolates requiere de dos ingredientes en com�n: manteca de cacao y az�car. Por cada unidad de chocolate oscuro se requiere 6g de manteca de cacao y 21 g de az�car. Por cada unidad de chocolate blanco se requiere 22g de manteca de cacao y 18g de az�car. Cada semana, la chocolater�a Perla Caribe tiene disponible 12kg de manteca de cacao y 20kg de az�car. La demanda de chocolate oscuro es ilimitada, pero a lo sumo le demandan 315 unidades de chocolate blanco por semana.

La chocolater�a Perla Caribe quiere maximizar su utilidad (ingresos menos costos). Formule un modelo matem�tico que represente la situaci�n y que les permita cumplir con su objetivo. 

## Formulaci�n

**a.** Escriba t�rmino a t�rmino la(s) variable(s) de decisi�n que utilizar� en el modelo. 

\begin{align*}
x_1: \text{unidades de chocolate oscuro producidos cada semana} \\
x_2: \text{unidades de chocolate blanco producidos cada semana}
\end{align*}


**b.** Escriba t�rmino a t�rmino la(s) restricci�n(es) lineal(es) y descr�bala(s)

Restricciones asociadas a la disponibilidad de recursos: 

\begin{align*}
6x_1 + 22x_2 \leq 12,000\\
21x_1 + 18x_2 \leq 20,000
\end{align*}

Restricciones asociadas a la demanda de productos: 

\begin{align*}
x_1 \leq 10,000
\end{align*}

Restricciones asociadas a tipo de variables: 

\begin{align*}
x_1 \geq 0\\
x_2 \geq 0
\end{align*}

**c.** Escriba t�rmino a t�rmino la funci�n objetivo que maximiza la utilidad.

$$
\text{maximizar }  (\$7,000 - \$3,500)x_1 + (\$6,000-\$2,000)x_2
$$

## Formulaci�n matem�tica

**Variables de decisi�n:**

- $x_1$: unidades de chocolate oscuro producidos cada semana
- $x_2$: unidades de chocolate blanco producidos cada semana


**Modelo:**

$$
\text{maximizar }  \$3,500x_1 + \$4,000x_2 \text{ (1)} 
$$

Sujeto a,
\begin{align*}
6x_1 + 22x_2 &\leq 12,000; &(2)\\
21x_1 + 18x_2 &\leq 20,000; &(3)\\
x_2 &\leq 10,000; &(4)\\
x_1 &\geq 0; &(5)\\
x_2 & \geq 0. &(6)
\end{align*}

La funci�n objetivo (1) maximiza las utilidades. Las restricciones (2) y (3) describen que se debe respetar la disponibilidad de manteca de cacao y az�car, respectivamente. La restricci�n (4) garantiza no se sobrepase la demanda m�xima de chocolate blanco. La restricciones (5) y (6) describen la naturaleza de la variables $x_1$ y $x_2$, respectivamente. 

## Implementaci�n

**e.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-------------------------------------
# Creaci�n del objeto problema en PuLP
#-------------------------------------
problema = lp.LpProblem("Perla",       #Nombre
                        lp.LpMaximize) #Sentido de la optimizaci�n

#-----------------------------
# Variables de Decisi�n
#-----------------------------
#Unidades de chocolate oscuro producidas cada semana
x_1 = lp.LpVariable("C_oscuro",            #Nombre
                    lowBound = 0,          #Cota inferior
                    upBound = None,        #Cota superior
                    cat = lp.LpContinuous) #Tipo de variable
#Unidades de chocolate blanco producidas cada semana
x_2 = lp.LpVariable("C_blanco",            #Nombre
                    lowBound = 0,          #Cota inferior
                    upBound = None,        #Cota superior
                    cat = lp.LpContinuous) #Tipo de variable

#-----------------------------
# Funci�n objetivo
#-----------------------------
#(1) Crea la expresi�n de maximizaci�n de utilidades 
problema += 3500*x_1 + 4000*x_2, "Utilidades Totales"

#-----------------------------
# Restricciones
#-----------------------------
#(2) Respeta la disponibilidad de manteca de cacao 
problema += 6*x_1 + 22*x_2 <= 12000, "Manteca_cacao"
#(3) Respeta la disponibilidad de azucar
problema += 21*x_1 +18*x_2 <= 20000, "Azucar"
#(4) Garantiza que la producci�n no sobrepase a lo demandado
problema += x_2 <= 315, "Demanda"

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("Perla.lp")

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
#Imprimir el valor de la funci�n objetivo
print("\nFunci�n objetivo = $", round(lp.value(problema.objective),2))
#Imprimir el valor de las variables
print("Fabricar ",x_1.value(),"\t unidades de chocolate oscuro")
print("Fabricar ",x_2.value(),"\t unidades de chocolate blanco")

## Cr�ditos

Equipo Principios de Optimizaci�n<br>
Instancias: Alfaima Solano<br>
Fecha: 30/09/2020