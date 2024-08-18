$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
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
$$\overline{\bm{\text{x}}} = (A^*\ A)^{-1} A^*\ \bm{\text{b}}$$ ^a7f86c

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

La factorización $QR$ es útil cuando se quieren obtener los mínimos cuadrados sin tener que computar las [[8- Mínimos Cuadrados#^a7f86c|Ecuaciones Normales]]. Esto no quiere decir que las Ecuaciones Normales no sean necesarias o que sean menos eficientes de computar, es simplemente una herramienta adicional para tener como opción cuando se necesite (como en el certamen).

### Estructura de $Q$ y $R$
La factorización $QR$ impone la siguiente estructura para las matrices $Q$ y $R$:
$$A = QR$$
Donde $R$ corresponde a una matriz [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]], y $Q$ es una [[|matriz unitaria]] con la particularidad adicional de que sus columnas $q_i$ deben generar el mismo espacio vectorial que las columnas $a_i$, es decir, se debe cumplir que $\text{Range}(A)= \text{Range}(B)$. 

Para fines de mejorar la comprensión de esta estructura de factorización, se introducen los siguientes 2 teoremas:
- *Para cualquier matriz $A \in \mathbb{C}^{m \times n}$ y matriz $Q \in \mathbb{C}^{m \times m}$ unitaria, tenemos:*
$$||QA||_2 = ||A||_2,\ ||QA||_F = ||A||_F$$
  El cual nos indica que el producto por una matriz unitaria no afecta a la [[1- Breve Introducción al Álgebra Lineal#Norma|norma 2 matricial o norma de Frobenius]] de la matriz resultante. Es gracias a este teorema que podemos utilizar en esta sección la siguiente implicancia:
  $$||Q\bm{\text{x}}||_2 = ||\bm{\text{x}}||_2,$$
  lo que implica que las matrices unitarias no cambian la [[1- Breve Introducción al Álgebra Lineal#Norma|norma 2 vectorial]].

- *Para cualquier matriz $Q \in \mathbb{C}^{n \times n}$ unitaria se tiene que $|\lambda| = 1$, donde $\lambda$ es un* [[|valor propio]] *de $Q$* 

Por último, es importante recordar esta propiedad de las [[|matrices unitarias cuadradas]]: *Sea $Q \in \mathbb{C}^{m \times m}$, entonces:*
$$Q^{-1} = Q^*$$
Si $Q \in \mathbb{C}^{m \times m}$, entonces $Q^{-1} = Q^T$. Esto significa que si quisiéramos resolver un sistema de ecuaciones lineales de la forma $Q\bm{\text{x}} = \bm{\text{b}}$, entonces la solución seria simplemente $\bm{\text{x}} = Q^*\bm{\text{b}}$., lo que implicaría que no seria necesario aplicar $\bm{\text{P}}A\bm{\text{L}}U$ y otro algoritmo de solución.

En el siguiente punto donde se habla del algoritmo de solución de este tipo de factorización solo puedo desear que: 1- Les haya ido bien en MAT-022.  2- Les haya gustado el apartado de matrices del curso. De incumplirse alguna de estas condiciones lo más probable es que les termine dando asco esta parte.

### Ortonormalización de Gram-Schmidt
La ortonomalización de Gram-Schmidt es uno de varios algoritmos que nos otorga esta factorización y, para bien o para mal, consistirá en el procedimiento que veremos en detalle. En pocas palabras, vamos a ir construyendo columna a columna nuestra matriz $Q$ y coeficiente por coeficiente nuestra matriz [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]] $R$ a partir de la matriz $A$.


> [!important] ¡MUY IMPORTANTE!
> En este punto es importante destacar que existen 2 variantes de la factorización QR para una matriz $A \in \mathbb{R}^{m \times n}$, con $m > n$. Una es la factorización QR-reducida, es decir $\hat{Q} \hat{R}$, y la otra es la factorización QR-full, es decir $QR$. Cabe destacar que ambas describen exactamente a la matriz $A$, es decir,
>
> $$A = \hat{Q} \hat{R} = QR$$
>
> La diferencia es que $\hat{Q} \in \mathbb{R}^{m \times n}$ y $\hat{R} \in \mathbb{R}^{n \times n}$, mientras que $Q \in \mathbb{R}^{m \times m}$ y $R \in \mathbb{R}^{m \times n}$. En particular se cumple la siguiente relación,
>
> $$Q = [\hat{Q}, \check{Q}],$$
> $$R = \begin{bmatrix} \hat{R} \\ \underline{\underline{0}} \end{bmatrix},$$
>
> donde $\check{Q} = [\mathbf{q}_{n+1}, \ldots, \mathbf{q}_m] \in \mathbb{R}^{m \times (m-n)}$ y $\underline{\underline{0}}$ es la matriz nula de dimensión $(m-n) \times n$. Es decir, las primeras $n$ columnas de la matriz $Q$ corresponden a la matriz $\hat{Q}$ y las siguientes $(m-n)$ columnas, corresponde a la matriz $\check{Q}$ que además contiene vectores ortonormales respecto de las columnas de $\hat{Q}$ y entre ellos mismos (no, yo tampoco entendí casi nada de esta parte). Por otra parte, las primeras $n$ filas de nuestra matriz $R$ corresponden a la matriz $\hat{R}$, donde las columnas que quedan están compuestas de coeficientes nulos. Gracias a las definiciones anteriores, es posible verificar las identidades anteriores resolviendo el producto $QR$:
> $$\begin{align}
> 	QR =&\ \begin{bmatrix} \hat{Q} & \check{Q} \end{bmatrix} \begin{bmatrix} \hat{R} \\ \underline{\underline{0}} \end{bmatrix} \\
> 	=&\ \hat{Q}\hat{R} + \check{Q}\underline{\underline{0}} \\
> 	=&\ \hat{Q}\hat{R} \\
> 	=&\ A
> \end{align}$$
> Y es debido a esto que primero vamos a construir la factorización QR-reducida, es decir $\hat{Q} \hat{R}$.

Para describir este algoritmo, consideremos la matriz $A \in \mathbb{R}^{m \times n}$, con $m > n$, la cual podemos describir en el siguiente formato de vectores columna:
$$A = \begin{bmatrix} \bm{\text{a}}_1, & \bm{\text{a}}_2, & \cdots, &\bm{\text{a}}_n \end{bmatrix}$$
donde $a_i \in \mathbb{R}^m$ con $i \in \{1,2,\cdots,n\}$. De esta forma podemos escribir convenientemente la identidad $A = \hat{Q}\hat{R}$:
$$\begin{bmatrix} \bm{\text{a}}_1, & \bm{\text{a}}_2, & \cdots, &\bm{\text{a}}_n \end{bmatrix} = 
\underbrace{
	\begin{bmatrix}
		\bm{\text{q}}_1, & \bm{\text{q}}_2, & \cdots & \bm{\text{q}}_n
	\end{bmatrix}
}_{\hat{Q}}
\underbrace{
	\begin{bmatrix}
		r_{11} & r_{12} & r_{13} & \cdots & r_{1n} \\
		0      & r_{22} & r_{23} & \cdots & r_{2n} \\
		0      & 0      & r_{33} & \cdots & r_{3n} \\
		\vdots & \vdots & \ddots & \ddots & \vdots \\
		0      & \cdots & \cdots & 0      & r_{nn}
	\end{bmatrix}
}_{\hat{R}}$$
Recordando que la matriz $Q$ es [[|ortonormal]], esto implica que sus columnas $\bm{\text{q}}_i$ deben ser ortogonales entre sí y que su [[1- Breve Introducción al Álgebra Lineal#Norma|norma-2]] de cada una de sus columnas debe ser 1, por lo que podemos expresar las siguientes condiciones para las columnas de $Q$:
$$\begin{align}
	\bm{\text{q}}_i^T\bm{\text{q}}_j =&\ 0 &, \text{para}\ i \neq j \tag{6} \\
	||\bm{\text{q}}_i||_2^2 =&\ 1 \tag{7}
\end{align}$$

^b40e5e

Multiplicando las matrices $\hat{Q}$ y $\hat{R}$ obtenemos:
$$\begin{bmatrix} \bm{\text{a}}_1, & \bm{\text{a}}_2, & \cdots, &\bm{\text{a}}_n \end{bmatrix} = 
\begin{bmatrix}
	r_{11}\bm{\text{q}}_1, & r_{12}\bm{\text{q}}_2 + r_{22}\bm{\text{q}}_2, & \cdots, & \displaystyle\sum_{i = 1}^k r_{ik}\bm{\text{q}}_i, & \cdots, & \displaystyle\sum_{i = 1}^n r_{in}\bm{\text{q}}_i 
\end{bmatrix}$$
De la igualdad obtenida para la primera columna obtenemos la siguiente ecuación:
$$\overbrace{\bmt{a}_1}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{11}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{1}}_{\text{\textcolor{red}{Desconocido}}} \tag{8}$$ ^93dad4

En este caso obtenemos una ecuación para 2 incógnitas, o al menos eso parece a simple vista... ¿Recuerdan que anteriormente mencioné que a un sistema de ecuaciones para estos casos podíamos añadir condiciones para nuestras incógnitas hasta que nuestro sistema tuviera una solución fija? Pues estas condiciones ya las tenemos, y estas equivalen a las [[8- Mínimos Cuadrados#^b40e5e|ecuaciones 6 y 7]]! Sin embargo, ¿Cómo podemos usar estas propiedades de la ortonormalidad para despejar $r_{11}$ y $\bmt{q}_1$? como con las nuevas condiciones podemos formar un sistema de ecuaciones con más ecuaciones que incógnitas, podemos tomarnos la libertad de escoger cualquiera de estas 2 a la hora de obtener estos valores, lo que nos deja con 2 alternativas:
- Multiplicar por la izquierda por $\bmt{q}_1^*$, es decir, obtener el producto interno con respecto a $\bmt{q}_1$. 
- Obtener la [[1- Breve Introducción al Álgebra Lineal#Norma|norma 2]] en ambos lados de la ecuación.

Para el caso de la primera alternativa obtenemos:
$$\begin{align}
	\bmt{a}_1 =&\ r_{11}\bmt{q}_1 \\
	\bmt{q}_1^*\bmt{a}_1 =&\ r_{11} \underbrace{\bmt{q}_1^T\bmt{q}_1}_1 \\
	\bmt{q}_1^T\bmt{a}_1 =&\ r_{11},
\end{align}$$
donde naturalmente se utilizó que $\bmt{q}_1^T\bmt{q}_1 = ||\bm{\text{q}}_1||_2^2 = 1$, o sea, la [[8- Mínimos Cuadrados#^b40e5e|ecuación 7]]. Aún así, todavía nos quedan componentes desconocidas a ambos lados de la ecuación, por lo que en el fondo acabamos de llegar a un punto muerto, así te toca probar con nuestra segunda alternativa:
$$\begin{align}
	\bmt{a}_1 =&\ r_{11}\bmt{q}_1 \\
	||\bmt{a}_1||_2 =&\ ||r_{11}\bmt{q}_1||_2 \\
	||\bmt{a}_1||_2 =&\ |r_{11}|\ \underbrace{||\bmt{q}_1||_2}_1 \\
	||\bmt{a}_1||_2 =&\ |r_{11}|,
\end{align}$$
donde ahora acabamos de utilizar el hecho de que los vectores son unitarios. Podemos notar ahora que nosotros si somos capaces de calcular el lado izquierdo $||\bmt{a}_1||_2^2$ de la ecuación, ahora, el lado derecho debido al valor absoluto de la expresión $|r_{11}|$ nos obliga a tomar una decisión entre $||\bmt{a}_1||_2$ y $-||\bmt{a}_1||_2$. Este último punto nos vuelve a demostrar que la factorización $QR$ no es única, aunque para términos prácticos del curso vamos a considerar el valor positivo (a no ser que en algún momento se diga lo contrario), es decir:
$$r_{11} = ||\bmt{a}_1||_2$$
Esto implica que de aquí en adelante vamos a considerar que todos los coeficientes de la diagonal $\hat{R}$ son positivos. Con esto hecho ahora tenemos lo siguiente:
$$\overbrace{\bmt{a}_1}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{11}}_{\text{\textcolor{cyan}{Conocido}}}\ \ \underbrace{\bmt{q}_{1}}_{\text{\textcolor{red}{Desconocido}}}$$
Y ahora para obtener $\bmt{q}_1$ basta con despejarlo de esta misma ecuación:
$$\bmt{q}_1 = \frac{\bmt{a}_1}{r_{11}}$$
Por lo que ahora sabemos despejar la primera ecuación de nuestro sistema de ecuaciones completo, así que ahora queda buscar la expresión general de esta estrategia de despeje. Tomemos ahora el caso de nuestra segunda ecuación:
$$\overbrace{\bmt{a}_2}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{12}}_{\text{\textcolor{red}{Desconocido}}}\overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{22}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{2}}_{\text{\textcolor{red}{Desconocido}}}$$
Siguiendo el mismo camino que hicimos anteriormente:
$$\begin{align}
	\bmt{q}_1^T\bmt{a}_2 =&\ r_{12}\ \underbrace{\bmt{q}_1^T\bmt{q}_1}_1 + r_{22}\ \underbrace{\bmt{q}_1^T\bmt{q}_2}_0 \\
	\bmt{q}_1^T\bmt{a}_2 =&\ r_{12}
\end{align}$$
Por lo que debido a que ya tenemos los valores de $\bmt{a}_2$ y $\bmt{q}_1$ podemos despejar tranquilamente la incógnita $r_{12}$, con lo que el estado de nuestra ecuación seria la siguiente:
$$\overbrace{\bmt{a}_2}^{\text{\textcolor{cyan}{Conocido}}} = \overbrace{r_{12}}^{\text{\textcolor{cyan}{Conocido}}}\ \ \overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{22}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{2}}_{\text{\textcolor{red}{Desconocido}}}$$
Ahora, fíjense en la estructura de la ecuación cuando mueva todos los valores conocidos hasta ahora hacia la izquierda:
$$\overbrace{\bmt{a}_2}^{\text{\textcolor{cyan}{Conocido}}} -\overbrace{r_{12}}^{\text{\textcolor{cyan}{Conocido}}}\ \ \overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{22}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{2}}_{\text{\textcolor{red}{Desconocido}}}$$
Lo que acaba de pasar es que se armó una ecuación con la misma forma que la de la [[8- Mínimos Cuadrados#^93dad4|ecuación 8]], por lo tanto podemos aplicar la misma técnica de la [[1- Breve Introducción al Álgebra Lineal#Norma|norma-2]] que usamos anteriormente para poder despejar el valor de $r_{22}$:
$$\begin{align}
	\bmt{a}_2 - r_{12}\bmt{q}_1 =&\ r_{22}\bmt{q}_2 \\
	 ||\bmt{a}_2 - r_{12}\bmt{q}_1||_2 =&\ ||r_{22}\bmt{q}_2||_2 \\
	 =&\ r_{22}\ \underbrace{||\bmt{q}_2||_2}_1 \\
	 =&\ r_{22} 
\end{align}$$
Con lo que podemos concluir que $r_{22} = ||\bmt{a}_2 - r_{12}\bmt{q}_1||_2$, con lo que actualizamos una vez más el estado de nuestra ecuación:
$$\overbrace{\bmt{a}_2}^{\text{\textcolor{cyan}{Conocido}}} -\overbrace{r_{12}}^{\text{\textcolor{cyan}{Conocido}}}\ \ \overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} = \overbrace{r_{22}}^{\text{\textcolor{cyan}{Conocido}}}\underbrace{\bmt{q}_{2}}_{\text{\textcolor{red}{Desconocido}}}$$
Por lo que al igual que con la ecuación que resolvimos anteriormente podemos obtener el valor de $\bmt{q}_2$ con tan solo igualar manipular un poco esta ecuación:
$$\bmt{q}_2 = \frac{\bmt{a}_2 - r_{12}\bmt{q}_1}{r_{22}}$$
Con lo que finalmente hemos resuelto la segunda ecuación de nuestro sistema de ecuaciones! Ahora por completitud y para que todos estén 100% seguros de que no hay que usar otro truco arcano para resolver algún problema nuevo que se nos presente en las subsiguientes ecuaciones de nuestro sistema vamos a resolver una tercera ecuación:
$$\overbrace{\bmt{a}_3}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{13}}_{\text{\textcolor{red}{Desconocido}}}\overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{23}}_{\text{\textcolor{red}{Desconocido}}}\ \ \overbrace{\bmt{q}_{2}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{33}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{3}}_{\text{\textcolor{red}{Desconocido}}}$$
De lo que hemos aprendido anteriormente podemos despejar los valores $r_{13}$:
$$\begin{align}
	\bmt{a}_3 =&\ r_{13}\bmt{q}_1 + r_{23}\bmt{q}_2 + r_{33}\bmt{q}_3 \\
	\bmt{q}_1^T\bmt{a}_3 =&\ r_{13}\bmt{q}_1^T\bmt{q}_1 + r_{23}\bmt{q}_1^T\bmt{q}_2 + r_{33}\bmt{q}_1^T\bmt{q}_3 \\
	=&\ r_{13}\underbrace{\bmt{q}_1^T\bmt{q}_1}_1 + r_{23}\underbrace{\bmt{q}_1^T\bmt{q}_2}_0 + r_{33}\underbrace{\bmt{q}_1^T\bmt{q}_3}_0 \\
	=&\ r_{13}
\end{align}$$
y el valor de $r_{23}$:
$$\begin{align}
	\bmt{a}_3 =&\ r_{13}\bmt{q}_1 + r_{23}\bmt{q}_2 + r_{33}\bmt{q}_3 \\
	\bmt{q}_2^T\bmt{a}_3 =&\ r_{13}\bmt{q}_2^T\bmt{q}_1 + r_{23}\bmt{q}_2^T\bmt{q}_2 + r_{33}\bmt{q}_2^T\bmt{q}_3 \\
	=&\ r_{13}\underbrace{\bmt{q}_2^T\bmt{q}_1}_0 + r_{23}\underbrace{\bmt{q}_2^T\bmt{q}_2}_1 + r_{33}\underbrace{\bmt{q}_2^T\bmt{q}_3}_0 \\
	=&\ r_{23}
\end{align}$$
Ahora, podemos obtener $r_{33}$ moviendo todas las variables conocidas y aplicando, nuevamente, [[1- Breve Introducción al Álgebra Lineal#Norma|norma-2]]:
$$\begin{align}
	\bmt{a}_3 - r_{13}\bmt{q}_1 - r_{23}\bmt{q}_2 =&\ r_{33}\bmt{q}_3 \\
	||\bmt{a}_3 - r_{13}\bmt{q}_1 - r_{23}\bmt{q}_2||_2 =&\ r_{33}\ ||\bmt{q}_3||_2 \\
	=&\ r_{33}
\end{align}$$
Y finalmente, ahora que tenemos todas las incógnitas de nuestra ecuación menos el término $\bmt{q}_3$ vamos a, nuevamente, despejar de la misma ecuación que tenemos este valor:
$$\bmt{q}_3 = \frac{\bmt{a}_3 - r_{13}\bmt{q}_1 - r_{23}\bmt{q}_2}{r_{33}}$$
Con lo que hemos sido capaces de obtener todos los términos desconocidos... de nuevo.

Finalmente, podemos generalizar las ecuaciones de nuestro sistema de ecuaciones $A = \hat{Q}\hat{R}$ de esta forma:
$$\overbrace{\bmt{a}_k}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{1,k}}_{\text{\textcolor{red}{Desconocido}}}\overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{2,k}}_{\text{\textcolor{red}{Desconocido}}}\ \ \overbrace{\bmt{q}_{2}}^{\text{\textcolor{cyan}{Conocido}}} + \cdots + \underbrace{r_{k-1,k}}_{\text{\textcolor{red}{Desconocido}}}\ \ \overbrace{\bmt{q}_{k-1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{k,k}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{k}}_{\text{\textcolor{red}{Desconocido}}}$$
Donde las expresiones de los términos desconocidos de la ecuación se expresan de la siguiente forma:
$$\begin{align}
	r_{i,k} =&\ \bmt{q}_i^T\bmt{a}_k, & \text{para } i \in \{1,2,\cdots,n\} \\
	r_{k,k} =&\ \left|\left| \bmt{a}_k - \sum_{i=1}^{k-1}r_{i,k}\bmt{q}_i \right|\right|_2 \\
	\bmt{q}_k =&\ \frac{\bmt{a}_k - \sum_{i=1}^{k-1} r_{i,k}\bmt{q}_i}{r_{k,k}}
\end{align}$$
Lo cual es válido para $k \in \{1,2,\cdots,n\}$. Este procedimiento es el que se conoce como la Ortonormalización Clásica de Gram-Schmidt, el cual podemos formalizar en el siguiente algoritmo:

```python
for k in range(1, n):
	y = A[k]
	for i in range(1, k):
		R[i][k] = Transpose(Q[i]) * A[k]
		y = y - R[i][k] * Q[i]		
	R[k][k] = Norm_2(y)
	Q[k] = y / R[k][k]
```

El único problema de este algoritmo es que asume que todas las ecuaciones son linealmente independientes entre sí, ya que de lo contrario obtendríamos algún coeficiente nulo y no se podría continuar con el algoritmo (por lo que este podría usarse además para verificar la linealidad de un sistema...).

Ahora, existe una forma alternativa de expresar este algoritmo que nos permita corregir lo más posible el error computacional que pueda surgir al usar aritmética de [[2- Estándar de Punto Flotante y Pérdida de Importancia#^aeafae|punto flotante]]. Tomemos como ejemplo la tercera ecuación que despejamos:
$$\overbrace{\bmt{a}_3}^{\text{\textcolor{cyan}{Conocido}}} = \underbrace{r_{13}}_{\text{\textcolor{red}{Desconocido}}}\overbrace{\bmt{q}_{1}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{23}}_{\text{\textcolor{red}{Desconocido}}}\ \ \overbrace{\bmt{q}_{2}}^{\text{\textcolor{cyan}{Conocido}}} + \underbrace{r_{33}}_{\text{\textcolor{red}{Desconocido}}}\ \ \underbrace{\bmt{q}_{3}}_{\text{\textcolor{red}{Desconocido}}}$$
Al igual que en el caso anterior, acá se obtiene que $r_{13} = \bmt{q}_1^T\bmt{a}_3$, la diferencia radica en la forma en la que expresamos el resultado de $r_{23}$ en adelante. En este caso nosotros por ortogonalidad consideramos que $\bmt{q}_2^T\bmt{q}_1 = 0$, sin embargo, debido a que operaremos en precisión doble entonces no haremos esta suposición:
$$\begin{align}
	\bmt{a}_3 =&\ r_{13}\bmt{q}_1 + r_{23}\bmt{q}_2 + r_{33}\bmt{q}_3 \\
	\bmt{a}_3 - r_{13}\bmt{q}_1 =&\ r_{23}\bmt{q}_2 + r_{33}\bmt{q}_3 \\
	\bmt{q}_2^T(\bmt{a}_3 - r_{13}\bmt{q}_1) =&\ r_{23}\bmt{q}_2^T\bmt{q}_2 + r_{33}\bmt{q}_2^T\bmt{q}_3 \\
	=&\ r_{23}\underbrace{\bmt{q}_2^T\bmt{q}_2}_1 + r_{33}\underbrace{\bmt{q}_2^T\bmt{q}_3}_0 \\
	=&\ r_{23}
\end{align}$$
por lo que esta vez obtenemos $r_{23} = \bmt{q}_2^T(\bmt{a}_3 - r_{13}\bmt{q}_1)$, lo que es matemáticamente equivalente al resultado de $r_{23}$ obtenido anteriormente, pero computacionalmente es muy importante, esto es debido a que al considerar $r_{13}\bmt{q}_1$ en $(\bmt{a}_3 - r_{13}\bmt{q}_1)$ y luego multiplicar por la izquierda el valor $\bmt{q}_2^T$, el coeficiente $r_{23}$ y posteriormente el coeficiente $r_{33}$ y vector $\bmt{q}_3$ van capturando y corrigiendo la inexactitud de la computación.

El nuevo algoritmo quedaría de la siguiente manera:

```python
for k in range(1, n):
	y = A[k]
	for i in range(1, k):
		r[i][k] = Transpose(Q[i]) * A[k]
		y = y - R[i][k] * y		
	R[k][k] = Norm_2(y)
	Q[k] = y / R[k][k]
```