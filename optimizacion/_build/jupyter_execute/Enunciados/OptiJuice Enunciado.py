# Producci�n de jugos

## Enunciado

OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos aut�ctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la pi�a, la guayaba, el n�spero y el zapote. Cada uno de los tipos de jugo se diferencia de los dem�s en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producci�n de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compa��a espera una demanda m�nima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. La informaci�n mencionada se presenta en las Tablas 1 a 4. 

Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: �Cu�ntos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

<p style="text-align: center;"><b>Tabla 1. M�nimo porcentaje de las frutas en los jugos</b></p>

<table class="egt">
    
  <tr>  
    <th>M�nimo porcentaje</th> 
    <th colspan="5";style="text-align:center">Frutas</th>
  </tr>
    
  <tr>
    <th style="text-align:center">Jugos</th>
    <td style="text-align:center"><i>Pi�a (%)</i></td>
    <td style="text-align:center"><i>Guayaba (%)</i></td>
    <td style="text-align:center"><i>Nispero (%)</i></td>
    <td style="text-align:center"><i>Zapote (%)</i></td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Saludable</i></td>
    <td style="text-align:center">32</td>
    <td style="text-align:center">27</td>
    <td style="text-align:center">12</td>
    <td style="text-align:center">13</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Tropical</i></td>
    <td style="text-align:center">18</td>
    <td style="text-align:center">30</td>
    <td style="text-align:center">31</td>
    <td style="text-align:center">34</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Ma�anero</i></td>
    <td style="text-align:center">7</td>
    <td style="text-align:center">31</td>
    <td style="text-align:center">28</td>
    <td style="text-align:center">22</td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Colombiano</i></td>
    <td style="text-align:center">11</td>
    <td style="text-align:center">5</td>
    <td style="text-align:center">15</td>
    <td style="text-align:center">18</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Refrescante</i></td>
    <td style="text-align:center">46</td>
    <td style="text-align:center">50</td>
    <td style="text-align:center">2</td>
    <td style="text-align:center">43</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Light</i></td>
    <td style="text-align:center">36</td>
    <td style="text-align:center">19</td>
    <td style="text-align:center">14</td>
    <td style="text-align:center">40</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 2. M�ximo porcentaje de las frutas en los jugos</b></p>

<table class="egt">
    
  <tr>  
    <th>M�ximo porcentaje</th> 
    <th colspan="5";style="text-align:center">Frutas</th>
  </tr>
    
  <tr>
    <th style="text-align:center">Jugos</th>
    <td style="text-align:center"><i>Pi�a (%)</i></td>
    <td style="text-align:center"><i>Guayaba (%)</i></td>
    <td style="text-align:center"><i>Nispero (%)</i></td>
    <td style="text-align:center"><i>Zapote (%)</i></td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Saludable</i></td>
    <td style="text-align:center">95</td>
    <td style="text-align:center">83</td>
    <td style="text-align:center">66</td>
    <td style="text-align:center">87</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Tropical</i></td>
    <td style="text-align:center">92</td>
    <td style="text-align:center">76</td>
    <td style="text-align:center">69</td>
    <td style="text-align:center">56</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Ma�anero</i></td>
    <td style="text-align:center">81</td>
    <td style="text-align:center">61</td>
    <td style="text-align:center">28</td>
    <td style="text-align:center">94</td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Colombiano</i></td>
    <td style="text-align:center">82</td>
    <td style="text-align:center">88</td>
    <td style="text-align:center">63</td>
    <td style="text-align:center">98</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Refrescante</i></td>
    <td style="text-align:center">60</td>
    <td style="text-align:center">85</td>
    <td style="text-align:center">73</td>
    <td style="text-align:center">78</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Light</i></td>
    <td style="text-align:center">50</td>
    <td style="text-align:center">55</td>
    <td style="text-align:center">82</td>
    <td style="text-align:center">91</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 3. Litros disponibles de cada fruta</b></p>

<table class="egt">
    
  <tr>  
    <th style="text-align:center">Frutas</th> 
    <th style="text-align:center">Litros disponibles</th>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Pi�a</i></td>
    <td style="text-align:center">4,318</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Guayaba</i></td>
    <td style="text-align:center">1,902</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Nispero</i></td>
    <td style="text-align:center">2,683</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Zapote</i></td>
    <td style="text-align:center">1,111</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 4. Demanda m�nima y precio de cada jugo</b></p>

<table class="egt">
    
  <tr>  
    <th style="text-align:center">Jugos</th> 
    <th style="text-align:center">Demanda m�nima</th>
    <th style="text-align:center">Precio</th>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Saludable</i></td>
    <td style="text-align:center">1,200</td>
    <td style="text-align:center">9,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Tropical</i></td>
    <td style="text-align:center">925</td>
    <td style="text-align:center">5,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Ma�anero</i></td>
    <td style="text-align:center">1,865</td>
    <td style="text-align:center">6,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Colombiano</i></td>
    <td style="text-align:center">1,035</td>
    <td style="text-align:center">10,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Refrescante</i></td>
    <td style="text-align:center">2,231</td>
    <td style="text-align:center">7,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Light</i></td>
    <td style="text-align:center">1,353</td>
    <td style="text-align:center">8,000</td>
  </tr>
    
</table>

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

Equipo Principios de Optimizaci�n<br>
Instancias: Juan Felipe Rengifo M, Camilo Aguilar<br>
Fecha: 05/09/2020


```{toctree}
:hidden:
:titlesonly:


..\Soluciones\OptiJuice
```
