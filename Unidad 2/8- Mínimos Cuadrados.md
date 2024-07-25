En este tema estudiaremos un tipo de problemas que no hemos abordado en este curso, y este corresponde a la resolución de sistemas de ecuaciones en las que existen más ecuaciones que incógnitas. La versión que resolveremos de este problema corresponde al de los mínimos cuadrados. A la hora de obtener los mínimos cuadrados de un sistema de ecuaciones vamos a aprender a realizar aproximaciones lineales sobre un conjunto de datos ($x_i$, $y_i$) para $i \in \{a,2,\cdots,n\}$. Antes de empezar con esto primero nos tenemos que hacer la pregunta, ¿Qué significa hacer una aproximación lineal?

![[Grafico_5.png]]

## Interpolación vs Aproximación de Mínimos Cuadrados

La primera pregunta que uno podría plantearse con respecto a este tema es, ¿por que nos interesa hacer una aproximación lineal y no interpolar los datos que pasen por los puntos ($x_i$, $y_i$)? y esto bien puede ser cierto para algunos casos, en los cuales nosotros poseemos una exactitud de los datos con los que queremos trabajar, tal y como lo vimos en el caso de los [[7- Interpolación Polinomial (Parte 2)#Puntos de Chebyshev|puntos de Chebyshev]], sin embargo, ¿Qué pasa si los puntos que nos entregan poseen un error asociado? En esta sección en particular, se considerará que todos los puntos $y_i$ poseen un error aditivo representado de esta forma:
$$y_i = y_i^{(e)} + \epsilon_i,\ i \in \{1,2,\cdots,m\}$$
donde $y_i$ corresponde a un dato al cual nosotros poseemos certeza de cual es su valor, $y_i^{(e)}$ es el dato exacto que nos interesa recuperar y $\epsilon_i$ corresponde al error asociado a la recolección del dato al que tampoco tenemos acceso.

La idea básicamente será obtener una función que logre representar lo mejor posible a todos los datos que nosotros queramos representar, tratando de mantener nuestro desconocido error lo más bajo posible.

## Mínimos Cuadrados por Minimización

Antes de poder aplicar un algoritmo de minimización, es necesario definir la estructura de la aproximación que vamos a utilizar. Para este caso particular vamos a trabajar con una estructura lineal respecto a la data, es decir:
$$\hat{y} = a + bx$$
Donde $\hat{y}$ es el valor que recuperaremos con la aproximación de los mínimos cuadrados. Una vez definida esta estructura con la que minimizar el error cuadrático, podemos construir la función del error cuadrático. La función de error cuadrático $E(·)$ se define de la siguiente forma:
$$\begin{align}
E(a,b) =&\ \sum_{i=1}^m r_i^2 \\
=&\ \sum_{i=1}^m (y_i - \hat{y}_i)^2\\
=&\ \sum_{i=1}^m (y_i - (a + bx))^2\\
=&\ \sum_{i=1}^m (y_i - a - bx)^2
\end{align}$$
Esta función posee 2 grados de libertad dados por los valores de $a$ y $b$, ya que todos los otros componentes son datos exactos. Debido a que no tenemos restricciones sobre $a$ o $b$, este problema de minimización pasa a ser uno de alta dimensión. El procedimiento es bastante directo y sencillo, y de hecho ya lo hemos hecho antes a la hora de buscar el jacobiano de una matriz asociada, solo necesitamos encontrar el punto crítico por medio de resolver $\nabla E = 0$:
$$\nabla E(a,b) = \left< \frac{\partial E}{\partial a}, \frac{\partial E}{\partial a}\right>$$
Por lo que este caso corresponde a:
$$\begin{align}
\frac{\partial E}{\partial a} =&\ \frac{\partial}{\partial a} \sum_{i=1}^m (y_i - a - bx_i)^2 = \sum_{i=1}^m 2(y_i - a - bx_i)(-1) \tag{1} \\
\frac{\partial E}{\partial b} =&\ \frac{\partial}{\partial a} \sum_{i=1}^m (y_i - a - bx_i)^2 = \sum_{i=1}^m 2(y_i - a - bx_i)(-x_i) \tag{2}
\end{align}$$

^adc09c

Igualando $\frac{\partial E}{\partial a}$ a 0 obtenemos la siguiente expresión:
$$\begin{align}
	\sum_{i=1}^m 2(y_i - \overline{a} - \overline{b}x_i)(-1) =&\ 0 \\
	\sum_{i=1}^m (y_i - \overline{a} - \overline{b}x_i) =&\ 0 \\
	\left( \sum_{i=1}^m y_i \right) - \overline{a}m - \overline{b}\left( \sum_{i=1}^m x_i \right) =&\ 0 \\
	m\overline{a} + \left( \sum_{i=1}^m x_i \right)\overline{b} =& \left(\sum_{i=1}^m y_i \right) \tag{3}
\end{align}$$
Esta vez expresé los términos $a$ y $b$ como $\overline{a}$ y $\overline{b}$ debido a que nosotros ahora estamos tomando los puntos de $a$ y $b$ que efectivamente minimizan el error, lo que antes de igualar la derivada a 0 no era necesariamente el caso. Igualando a 0 de todas maneras la [[8- Mínimos Cuadrados#^adc09c|ecuación 2]] obtenemos:
$$\begin{align}
\sum_{i=1}^m 2(y_i - \overline{a} - \overline{b}x_i)(-x_i) =&\ 0 \\
\sum_{i=1}^m (y_ix_i - \overline{a}x_i - \overline{b}x_i^2) =&\ 0 \\
\left( \sum_{i=1}^m y_ix_i \right) - \overline{a}\left( \sum_{i=1}^m x_i \right) - \overline{b}\left( \sum_{i=1}^m x_i^2 \right) =&\ 0 \\
\left( \sum_{i=1}^m x_i \right)\overline{a} + \left( \sum_{i=1}^m x_i^2 \right)\overline{b} =&\ \left( \sum_{i=1}^m y_ix_i \right) \tag{4}
\end{align}$$
Ahora podemos armar un sistema de ecuaciones que involucren las ecuaciones 3 y 4:
$$\begin{bmatrix}
	m                             & \displaystyle\sum_{i=1}^m x_i   \\
	\displaystyle\sum_{i=1}^m x_i & \displaystyle\sum_{i=1}^m x_i^2
\end{bmatrix}
\begin{bmatrix}
	\overline{a} \\
	\overline{b}
\end{bmatrix}
=
\begin{bmatrix}
	\displaystyle\sum_{i=1}^m y_i    \\
	\displaystyle\sum_{i=1}^m y_ix_i
\end{bmatrix}$$
El cual posee la siguiente solución:
$$\begin{align}
	\overline{a} =&\ \frac{(\sum_{i=1}^m x_i^2)(\sum_{i=1}^m y_i) - (\sum_{i=1}^m x_i)(\sum_{i=1}^m y_ix_i)}{m(\sum_{i=1}^m x_i^2) - (\sum_{i=1}^m x_i)^2} \\
	\overline{b} =&\ \frac{m(\sum_{i=1}^m y_ix_i) - (\sum_{i=1}^m x_i)(\sum_{i=1}^m y_i)}{m(\sum_{i=1}^m x_i^2) - (\sum_{i=1}^m x_i)^2}
\end{align}$$
Y con esto hemos sido capaces de encontrar valores para $a$ y $b$ que minimicen lo más posible el error producido.

## Mínimos Cuadrados desde Álgebra Lineal

Esta segunda forma de obtener los mínimos cuadrados se obtienen desde el álgebra lineal. Consideremos la misma expresión que usamos anteriormente para expresar nuestra estimación lineal $y_i \approx \hat{y}_i = a + bx_i$ y re-escribámosla como un sistema de ecuaciones lineales:
$$\begin{align}
	a + bx_1 \approx&\ y_1 \\
	a + bx_2 \approx&\ y_2 \\
	a + bx_3 \approx&\ y_3 \\
	\vdots \phantom{=}&\\
	a + bx_m \approx&\ y_m \\
\end{align}$$
Y para ajustar la aproximación hacia los $y_i$, podemos además añadirle a la parte izquierda de nuestro sistema un error o residuo $r_i$:
$$\begin{align}
	a + bx_1 + r_1 =&\ y_1 \\
	a + bx_2 + r_2 =&\ y_2 \\
	a + bx_3 + r_3 =&\ y_3 \\
	\vdots \phantom{==,,}&\\
	a + bx_m + r_m =&\ y_m \\
\end{align}$$
Utilizando notación matricial tenemos:
$$\underbrace{
	\begin{bmatrix}
		r_1 \\
		r_2 \\
		r_3 \\
		\vdots \\
		r_m
	\end{bmatrix}
}_{\bm{\text{r}}}
=
\underbrace{
	\begin{bmatrix}
		y_1 \\
		y_2 \\
		y_3 \\
		\vdots \\
		y_m
	\end{bmatrix}
}_{\bm{\text{b}}}
-
\underbrace{
	\begin{bmatrix}
		1 & x_1 \\
		1 & x_2 \\
		1 & x_3 \\
		\vdots & \vdots\\
		1 & x_m
	\end{bmatrix}
}_{A}
\begin{bmatrix}
a \\
b
\end{bmatrix}
\tag{5}
$$

^c52b1e

De esta notación podemos extraer algunos puntos importantes:
- La matriz tiene $m$ filas y solo 2 columnas. Se suele utilizar $m$ para denotar la cantidad de filas y $n$ para denotar la cantidad de columnas.

- Si $m > n$ y el [[1- Breve Introducción al Álgebra Lineal#Column Space, Row Space y Rank|Rank]] es $n$, entonces tenemos un sistema de ecuaciones sobre-determinado y [[1- Breve Introducción al Álgebra Lineal#Full Rank|Full Rank]], es decir, existen más ecuaciones dentro de nuestro sistema que incógnitas.

- Si $m = n$, entonces tenemos un sistema de ecuaciones lineales cuadrado, lo cual ya sabemos resolverlo gracias al [[5- Sistemas de Ecuaciones Lineales|tema 5]].

- En caso de que tengamos $m < n$, entonces tendremos un sistemas de ecuaciones bajo-determinado. En este caso la solución no seria única debido a que tendremos un sistema de ecuaciones con más incógnitas que ecuaciones a despejar, por lo que si quisiéramos obtener una respuesta certera tendríamos que imponer restricciones a nuestras variables hasta terminar con por lo menos un sistema cuadrado.

- Es posible que hayan notado que la matriz $A$ posee una estructura similar a la de la [[6- Interpolación Polinomial (Parte 1)#Matriz de Vandermonde|matriz de Vandermonde]], sin embargo, es evidente que para estos casos nuestra cantidad de columnas para esta matriz viene truncada. 

Dado que para este caso de análisis estamos estudiando el caso donde tenemos más filas que columnas, podremos concluir que estamos analizando un sistema de ecuaciones sobre-determinado, el cual poseerá solución única si es que además nuestro sistema es [[1- Breve Introducción al Álgebra Lineal#Full Rank|Full Rank]] (lo recalco de nuevo porque de ser así y alguien se da cuenta, chanchamente puede ir y aplicar alguno de los algoritmos de resolución de sistemas de ecuaciones lineales vistos anteriormente).
Del desarrollo anterior podemos reescribir la [[8- Mínimos Cuadrados#^c52b1e|ecuación 5]] de la siguiente forma:
$$\begin{align}
\bm{\text{r}} =&\ \bm{\text{b}} - A \begin{bmatrix} a \\ b \end{bmatrix} \\
\bm{\text{r}} =&\ \bm{\text{b}} - \begin{bmatrix} \bm{\text{v}}_1 & \bm{\text{v}}_2 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} \\
\bm{\text{r}} =&\ \bm{\text{b}} - a\bm{\text{v}}_1 - b\bm{\text{v}}_2
\end{align}$$
Es decir, estamos buscando la mejor combinación lineal de los vectores $\bm{\text{v}}_1$ y $\bm{\text{v}}_2$ para aproximar el valor de $\bm{\text{b}}$, el cual nos permitirá minimizar lo más posible el valor de residuo $\bm{\text{r}}$, en donde se considera la mejor combinación lineal aquella que minimice el error cuadrático:
$$E(x,y) = ||r||_2^2 = ||\bm{\text{b}} - a\bm{\text{v}}_1 - b\bm{\text{v}}_2||_2^2$$

![[Apuntes_INF-285_2024-v0613.pdf#page=132&rect=109,561,499,727|Apuntes_INF-285_2024-v0613, p.131]]

Como podemos apreciar en esta imagen, debido a que la matriz $A$ es un valor ya conocido y fijo relacionado con el sistema de ecuaciones como tal, dependemos del valor de $\overline{\bm{\text{x}}}$ para poder minimizar el valor del mínimo cuadrado, donde para el ejemplo actual equivale a $\overline{\bm{\text{x}}} = \begin{bmatrix} \overline{a} & \overline{b} \end{bmatrix}^T$. De forma más compacta y con el fin de que se pueda entender lo que se busca desarrollar a continuación se adjunta la siguiente imagen también presente dentro de los apuntes del curso:

![[Apuntes_INF-285_2024-v0613.pdf#page=133&rect=157,546,445,720|Apuntes_INF-285_2024-v0613, p.132]]

Alguno de ustedes probablemente hayan podido inferir que la clave es la ortogonalidad entre $\bm{\text{r}} = \bm{\text{b}} - A\overline{\bm{\text{x}}}$ y $A\bm{\text{x}}$, por lo que si $r$ y $A\bm{\text{x}}$ son ortogonales se debe cumplir que su producto cruz es 0, lo que se traduce en la siguiente expresión:
$$\begin{align}
	(A\bm{\text{x}})\ ^*\ \bm{\text{r}} =&\ 0 \\
	(A\bm{\text{x}})\ ^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}}) =&\ 0 \\
	\bm{\text{x}}^*\ A^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}}) =&\ 0 
\end{align}$$
Considerando que $\bm{\text{x}} \neq 0$, tenemos que buscar otra combinación de términos con los cuales podamos concluir que la ecuación se pueda llegar a cumplir:
$$\begin{align}
	\bm{\text{x}}^*\ A^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}}) =&\ 0 \\
	\bm{\text{x}}^*\ (A^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}})) =&\ 0
\end{align}$$
por lo que nuestra única conclusión posible que es que la expresión $A^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}})$ debe ser 0:
$$\begin{align}
	A^*\ (\bm{\text{b}} - A\overline{\bm{\text{x}}}) =&\ 0 \\
	A^*\ \bm{\text{b}} - A^*\ A\overline{\bm{\text{x}}} =&\ 0 
\end{align}$$
Lo cual podemos reducir a:
$$A^*\ A\overline{\bm{\text{x}}} = A^*\ \bm{\text{b}}$$
Expresión a la cual se le conoce como las **Ecuaciones Normales**, el que nos va a permitir obtener una expresión explícita para $\overline{\bm{\text{x}}}$:
$$\overline{\bm{\text{x}}} = (A^*\ A)^{-1} A^*\ \bm{\text{b}}$$
Aunque por lo general no es necesario obtener la inversa de $A$, suele ser suficiente con resolver el sistema de ecuaciones lineales asociado $A^*\ A\overline{\bm{\text{x}}} = A^*\ \bm{\text{b}}$, donde gracias a que la matriz $A^*\ A$ es una matriz cuadrada de dimensiones $n \times n$ es posible, nuevamente, utilizar [[5- Sistemas de Ecuaciones Lineales|alguno de los algoritmos vistos anteriormente]].

Ahora, revisemos nuevamente el problema de los cuadrados propuesto en la [[8- Mínimos Cuadrados#^c52b1e|ecuación 5]]:
$$\underbrace{
	\begin{bmatrix}
		r_1 \\
		r_2 \\
		r_3 \\
		\vdots \\
		r_m
	\end{bmatrix}
}_{\bm{\text{r}}}
=
\underbrace{
	\begin{bmatrix}
		y_1 \\
		y_2 \\
		y_3 \\
		\vdots \\
		y_m
	\end{bmatrix}
}_{\bm{\text{b}}}
-
\underbrace{
	\begin{bmatrix}
		1 & x_1 \\
		1 & x_2 \\
		1 & x_3 \\
		\vdots & \vdots\\
		1 & x_m
	\end{bmatrix}
}_{A}
\begin{bmatrix}
a \\
b
\end{bmatrix}
$$
Construyamos ahora las Ecuaciones Normales $A^*\ A\overline{\bm{\text{x}}} = A^*\ \bm{\text{b}}$:
$$\begin{bmatrix}
	1   & 1   & 1   & \cdots & 1   \\
	x_1 & x_2 & x_3 & \cdots & x_m \\
\end{bmatrix}
\begin{bmatrix}
	1 & x_1 \\
	1 & x_2 \\
	1 & x_3 \\
	\vdots & \vdots\\
	1 & x_m
\end{bmatrix}
\begin{bmatrix}
\overline{a} \\
\overline{b}
\end{bmatrix}
=
\begin{bmatrix}
	1   & 1   & 1   & \cdots & 1   \\
	x_1 & x_2 & x_3 & \cdots & x_m \\
\end{bmatrix}
\begin{bmatrix}
	y_1 \\
	y_2 \\
	y_3 \\
	\vdots \\
	y_m
\end{bmatrix}
$$
Multiplicando las matrices obtenemos:
$$\begin{bmatrix}
	m                             & \displaystyle\sum_{i=1}^m x_i   \\
	\displaystyle\sum_{i=1}^m x_i & \displaystyle\sum_{i=1}^m x_i^2
\end{bmatrix}
\begin{bmatrix}
	\overline{a} \\
	\overline{b}
\end{bmatrix}
=
\begin{bmatrix}
	\displaystyle\sum_{i=1}^m y_i    \\
	\displaystyle\sum_{i=1}^m y_ix_i
\end{bmatrix}$$
Lo que equivale a exactamente lo mismo que obtuvimos con el método anterior, solo que esta vez llegamos a ello utilizando un método y punto de vista distintos.

## Factorización $QR$ 