# Planeaci�n de men�s

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


## Implementaci�n

**b.** Resuelva el modelo planteado utilizando la librer�a de PuLP en Python. �Cu�l es la soluci�n
�ptima del problema? 



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


```{toctree}
:hidden:
:titlesonly:


..\Soluciones\PlaneacionMenus
```
