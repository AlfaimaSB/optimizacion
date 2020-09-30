# OptiJuice

## Enunciado

OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos aut�ctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la pi�a, la guayaba, el n�spero y el zapote. Cada uno de los tipos de jugo se diferencia de los dem�s en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producci�n de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compa��a espera una demanda m�nima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. 

Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: �Cu�ntos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

## Formulaci�n

**a.** Describa la(s) variable(s) de decisi�n que utilizar� en el modelo. 



**b.** Escriba la(s) restricci�n(es) lineal(es) que describe(n) que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. 


**c.** Escriba la(s) restricci�n(es) que describe(n) que OptiJuice puede utilizar m�ximo $b_i$ litros de zumo de la fruta $i\in R$. 


**d.** Escriba la(s) restricci�n(es) que describe(n) que OptiJuice desea cumplir con la demanda m�nima de $d_k$ litros jugo del tipo $k\in K$. 


**e.** Escriba la(s) restricci�n(es) que describe(n) matem�ticamente el tipo de variable(s) que est� utilizando dentro del modelo. 


**f.** Escriba la funci�n objetivo que maximiza los ingresos totales.


## Implementaci�n

**g.** Resuelva el modelo planteado utilizando la librer�a de PulP en Python. �Cu�l es la soluci�n
�ptima del problema? 



## Cr�ditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 05/09/2020


```{toctree}
:hidden:
:titlesonly:


OptiJuice
```
