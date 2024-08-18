$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
En esta sección estudiaremos diversos algoritmos que nos permitan realizar interpolaciones polinomiales sobre ciertos puntos en 1D. 
Definiendo formalmente el concepto de interpolación polinomial tenemos: *Una función $y = p(x)$ interpola los datos ($x_1$, $y_1$)$,\cdots,$($x_n$, $y_n$) si $p(x_i) = y_i$ para cada $i \in \{1,2,\cdots,n\}$*.

A ciencia cierta pueden existir infinitas funciones que puedan usarse para interpolar cierto set de puntos de coordenadas ($x_i$, $y_i$), la gracia es que por lo general, y cuando lo necesitemos, seamos capaces de encontrar la interpolación que sea más fácil de manipular. Tomemos por ejemplo los siguiente puntos del gráfico:

![[Grafico_1.png]] ^d5d9a3

¿Se les ocurre algún polinomio que contenga ambos puntos de este gráfico? lo natural sería pensar en algún polinomio de primer grado de la forma $y = ax + b$, el cual corresponderia al polinomio más primitivo con el que se podrian interpolar estos 2 puntos en una misma función:

![[Grafico_2.png]]

Aunque bien como mencioné anteriormente, pueden existir infinitas funciones las cuales puedan abarcar estos 2 puntos. Aquí va un ejemplo con un polinomio de segundo grado:

![[Grafico_3.png]]

Antes de empezar a estudiar este nuevo tema más a fondo, es necesario introducirles el siguiente teorema de la **Unicidad de la interpolación polinomial**: *Sea ($x_1$, $y_1$)$,\cdots,$($x_n$, $y_n$) $n$ puntos en el plano $\mathbb{R}^2$ con distintos $x_i$, entonces existe un y sólo un polinomio $p(x)$ de grado ($n-1$) o menor que satisface la ecuación $p(x_i) = y_i$ para $i \in \{1,2,\cdots,n\}$*. ^e43636

## Matriz de Vandermonde

Este algoritmo es posiblemente el más intuitivo y directo a la hora de obtener interpolaciones polinomiales. Tomemos como ejemplo los mismo punto mostrados con [[6- Interpolación Polinomial (Parte 1)#^d5d9a3|esta imagen]], o sea, vamos a tomar 2 puntos de coordenadas ($x_1$, $y_1$) y ($x_2$, $y_2$), para el cual vamos a proponer un polinomio interpolador de primer grado con la siguiente forma:
$$p(x) = a_1x + a_0$$
La razón por la que se elige este polinomio es porque este posee 2 grados de libertad (dados por $a_1$ y $a_0$) además que se tenemos que cumplir 2 condiciones, $p(x_1) = y_1$ y $p(x_2) = y_2$, con las cuales podemos formar el siguiente sistema de ecuaciones:
$$\begin{align}
p(x_1) =&\ a_0 + a_1x_1 = y_1 \\
p(x_2) =&\ a_0 + a_1x_2 = y_2 
\end{align}$$
La cual podemos expresar de la siguiente forma matricial:
$$\begin{bmatrix}
	1 & x_1 \\
	1 & x_2
\end{bmatrix}
\begin{bmatrix}
	a_0 \\
	a_1 
\end{bmatrix}
=
\begin{bmatrix}
	y_1 \\
	y_2 
\end{bmatrix}$$
Y por supuesto, en este punto debería ser trivial tener que resolver este sistema de ecuaciones con la cantidad de técnicas de resolución de [[5- Sistemas de Ecuaciones Lineales|Sistemas de Ecuaciones Lineales]] aprendidas hasta ahora. Si usamos la misma lógica para intentar interpolar 3 puntos dentro de un plano entonces obtenemos la siguiente matriz:
$$\begin{bmatrix}
	1 & x_1 & x_1^2 \\
	1 & x_2 & x_2^2 \\
	1 & x_3 & x_3^2
\end{bmatrix}
\begin{bmatrix}
	a_0 \\
	a_1 \\
	a_2
\end{bmatrix}
=
\begin{bmatrix}
	y_1 \\
	y_2 \\
	y_3 
\end{bmatrix}$$
Con lo que ya podemos notar la forma general con la que podemos expresar una matriz para una cantidad $n$ de puntos, la que denominaremos como la **Matriz de Vandermonde** $V$:
$$\underbrace{
	\begin{bmatrix}
		1      & x_1     & x_1^2     & \cdots & x_1^{n-2}     & x_1^{n-1}     \\
		1      & x_2     & x_2^2     & \cdots & x_2^{n-2}     & x_2^{n-1}     \\
		\vdots & \vdots  & \ddots    & \vdots & \vdots        & \vdots        \\
		1      & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-2} & x_{n-1}^{n-1} \\
		1      & x_n     & x_n^2     & \cdots & x_n^{n-2}     & x_n^{n-1}     \\
	\end{bmatrix}
}_{V}
\begin{bmatrix}
	a_0 \\
	a_1 \\
	\vdots \\
	a_{n-2} \\
	a_{n-1}
\end{bmatrix}
=
\begin{bmatrix}
	y_1 \\
	y_2 \\
	\vdots \\
	y_{n-1} \\
	y_n 
\end{bmatrix}$$
Notemos que no importan el orden en el que se encuentren cada uno de los valores $x_i$, sin embargo, si queremos obtener una solución única al problema es importante que todas las filas sean [[1- Breve Introducción al Álgebra Lineal#Dependencia e Independencia Lineal|linealmente independientes]] entre si, ya que de lo contrario existirían 2 o más filas iguales dentro de nuestra matriz, por lo que de existir alguna solución al sistema de ecuaciones esta no seria única, y es más, esto lo podemos corroborar con la definición de [[1- Breve Introducción al Álgebra Lineal#Determinante|determinante]], ya que nosotros terminaríamos obteniendo un determinante equivalente a 0. Como último punto a mencionar, esta matriz puede terminar requiriendo demasiadas operaciones elementales para poder resolverla, ya que crece de forma exponencial la cantidad de operaciones que hay que realizar a medida que se necesitan interpolar más puntos.

## Interpolación de Lagrange

Este nuevo método de obtener interpolaciones posee la ventaja a diferencia del método anterior de que no se hace necesario resolver un sistema de ecuaciones de antemano, sino que mas bien se logra con una definición particular y muy conveniente sobre la estructura de un polinomio. La estructura del polinomio interpolador de $n$ puntos de interpolación tiene la siguiente forma:
$$\begin{align}
	p(x) =&\ y_1L_1(x) + y_2L_2(x) + \cdots + y_nL_n(x) \\
	     =&\ \sum_{i=1}^n y_iL_i(x),
\end{align}$$
donde $L_i(x_i) = 1$ y $L_i(x_j) = 0$ para $i \neq j$ e $i, j \in \{1,2,\cdots,n\}$. Esta definición nos permite obtener $y_k$ cuando uno evalúa $p(x_k)$, es decir:
$$\begin{align}
	p(x_k) =&\ y_1\underbrace{L_1(x_k)}_{0} + y_2\underbrace{L_2(x_k)}_{0} + \cdots + y_k\underbrace{L_k(x_k)}_{1} + \cdots + y_n\underbrace{L_n(x_k)}_{0} \\
	       =& y_k
\end{align}$$
Por supuesto, gracias a esta estructura se ve muy sencillo el obtener el valor de $y_k$, aunque todavía nos queda lograr encontrar una expresión para la expresión $L_i(x)$ que cumpla justamente con las propiedades anteriores. Definamos primero a $l_i(x)$ de la siguiente forma:
$$l_i(x) = \prod_{k=1, i \neq k}^n (x - x_k) = (x - x_1)(x - x_2)\cdots(x - x_{i-1}) (x - x_{i+1})\cdots(x - x_n)$$
Lo que simplemente expresa el producto entre todos los términos ($x - x_k$), sin incluir el término ($x - x_i$). De esta forma se logra que $l_i(x)$ sea 0 al evaluarlo en cualquier $x_k \neq x_i$, sin embargo, todavía tenemos que trabajar más esta expresión, ya que no siempre se va a cumplir que $l_i(x_i) = \prod_{k=1, i \neq k}^n (x_i - x_k) = 1$. Definamos ahora sí a la función $L_i(x)$ de la siguiente forma:
$$\begin{align}
L_i(x) =&\ \frac{l_i(x)}{l_i(x_i)} \\
=&\ \frac{(x - x_1)(x - x_2)\cdots(x - x_{i-1}) (x - x_{i+1})\cdots(x - x_n)}{(x_i - x_1)(x_i - x_2)\cdots(x_i - x_{i-1}) (x_i - x_{i+1})\cdots(x_i - x_n)}
\end{align}$$
Y ahora que logramos encontrar expresiones para los valores de $L_i(x)$ e $y_i$ ya podemos interpolar varios puntos sin tener que usar la matriz de Vandermonde, y es más, este método lo hace dándonos el *polinomio minimal* o de menor grado posible para lograrlo.

Tomemos ahora como ejemplo el mismo de la [[6- Interpolación Polinomial (Parte 1)#^d5d9a3|primera imagen mostrada en este tema]] y construyamos su polinomio con la forma de una interpolación de Lagrange:
$$p(x) = y_1L_1(x) + y_2L_2(x),$$
donde $L_1(x) = \frac{(x-x_2)}{(x_1-x_2)}$ y $L_2(x) = \frac{(x - x_1)}{x_2 - x_1}$. En la siguiente imagen podemos apreciar como quedaría nuestra nueva recta interpolada:

![[Grafico_4.png]]


## Interpolación Baricéntrica

Y aquí tenemos nuestro tercer algoritmo para poder realizar interpolaciones polinomiales. Este algoritmo es de hecho derivable del mismo método de interpolación de Lagrange, además de que permite reducir considerablemente la cantidad de operaciones elementales necesarias para poder evaluar nuestro polinomio construido (ya en para Lagrange tenemos que evaluar en nuestro polinomio obtenido todos los productos $(x - x_1)(x - x_2)\cdots(x - x_{i-1}) (x - x_{i+1})\cdots(x - x_n)$ del numerador de cada $L_i(x)$ con tal de poder evaluar finalmente $p(x)$), y además, existe la posibilidad de que necesitemos menos operaciones elementales para poder armar nuestro polinomio interpolador. 

Definamos a $l(x)$ de la siguiente forma:
$$l(x) = \prod_{k=1}^n (x - x_k)$$
Notemos que con esta definición estamos diciendo que, a diferencia de como habíamos definido $l_i(x)$ en Lagrange, si existe el término ($x - x_i$) dentro de la multiplicatoria. Obtengamos ahora nuestra expresión $l_i(x)$:
$$l_i(x) = \frac{l(x)}{(x-x_i)}$$
Con lo que obtenemos una definición de $l_i(x)$ que es equivalente al caso anterior. Ahora, es posible obtener el denominador de $L_i(x)$ que estamos buscando de la siguiente forma:
$$w_i = \frac{1}{l_i(x_i)} = \frac{1}{l'(x_i)}$$
Por lo que finalmente podemos expresar $L_i(x)$:
$$L_i(x) = \frac{l(x)}{(x-x_i)}w_i$$
Así que con esto podemos re-escribir la interpolación de Lagrange:
$$\begin{align}
p(x) =&\ \sum_{i=1}^n y_iL_i(x) \\
=&\ \sum_{i=1}^n y_i\frac{l(x)}{(x-x_i)}w_i \\
=&\ l(x)\sum_{i=1}^n y_i\frac{w_i}{(x-x_i)} \tag{1}
\end{align}$$

^166f7b

Si bien esto ya supone una ligera mejora con respecto a la interpolación de Lagrange, todavía no terminamos de obtener la expresión de la interpolación baricéntrica. Utilicemos la ecuación que acabamos de obtener y usémosla para interpolar la constante 1. Haciendo uso del [[6- Interpolación Polinomial (Parte 1)#^e43636|Teorema de la Unicidad de la Interpolación Polinomial]] obtenemos:
$$\begin{align}
p(x) =&\ l(x)\sum_{i=1}^n \underbrace{y_i}_{1}\frac{w_i}{(x-x_i)} \\
=&\ l(x)\sum_{i=1}^n \frac{w_i}{(x-x_i)} \\
=&\ 1
\end{align}$$
Lo que nos entrega la siguiente identidad:
$$1 = l(x)\sum_{i=1}^n \frac{w_i}{(x-x_i)}$$
Desde la cual podemos despejar $l(x)$:
$$l(x) = \frac{1}{\sum_{i=1}^n \frac{w_i}{(x-x_i)}}$$
Y por último, si reemplazamos $l(x)$ con la definición que habíamos obtenido con la [[6- Interpolación Polinomial (Parte 1)#^166f7b|ecuación 1]] obtenemos:
$$\begin{align}
p(x) =&\ l(x)\sum_{i=1}^n y_i\frac{w_i}{(x-x_i)} \\
=&\ \frac{\sum_{i=1}^n y_i\frac{w_i}{(x-x_i)}}{\sum_{i=1}^n \frac{w_i}{(x-x_i)}}
\end{align}$$
Lo que ahora sí corresponde a la expresión de la interpolación baricéntrica! Esta fórmula nos permite evaluar nuestro polinomio $p(x)$ a velocidades mucho mas rápidas que con la interpolación de Lagrange, esto es debido a que podemos observar de la expresión $l_i(x) = (x - x_1)(x - x_2)\cdots(x - x_{i-1}) (x - x_{i+1})\cdots(x - x_n)$ que esta depende de los valores que recibamos de $x$, y esta misma hay que evaluarla para cada $L_i(x)$ existente en nuestro polinomio, lo que hace que nos demoremos una cantidad de $O(n^2)$ en evaluar nuestro polinomio para algún $x$. Sin embargo, gracias a la interpolación polinomial hemos logrado reducir la expresión de $l_i(x)$ al valor $w_i = \frac{1}{l_i(x_i)}$, el cual al depender de $x_i$ en vez del valor de $x$ pues esto hace que SOLO necesitemos calcular cada $w_i$ de nuestro polinomio una sola vez, lo que implica que la primera evaluación del polinomio tenga un tiempo de $O(n^2)$ para que las evaluaciones subsiguientes tengan un tiempo de $O(n)$ en calcularse, ya que simplemente tendríamos que calcular las sumatorias del numerador y denominador de la fracción, aparte de tener que resolver esta misma.

