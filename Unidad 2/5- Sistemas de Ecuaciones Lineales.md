---
cssclasses:
  - t-c
---
$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
Como podrán interpretar del título de este tema, ahora nos vamos a enfocar en algoritmos que nos permitan resolver sistemas de ecuaciones lineales, solo que a diferencia de los temas de [[3- Raíces en 1D (Parte 1)|raíces en 1D]], ahora vamos a prestar especial atención a las características técnicas de las técnicas que se enseñaran. Por ejemplo, la calidad de la solución (cuanto error produce), su tiempo de computación y la cantidad de almacenamiento requerido (cuanta RAM se necesita para computarlo).

Como recordarán, en el [[4- Raíces en 1D (Parte 2)#^446a3c|tema anterior]] mencioné que buscar la raíz de una función podía interpretarse como la búsqueda de la intersección entre una función lineal y la función a la que queremos encontrar su raíz. Al resolver sistemas de ecuaciones lineales en el fondo vamos a hacer los mismo, solo que esta vez buscaremos la intersección entre todas las rectas con sus ecuaciones representativas pertenecientes a un mismo sistema de ecuaciones: 

![[Ecuacion_1.png]]

Tomando como ejemplo la imagen anterior, se nos está proponiendo la búsqueda del punto de intersección entre 2 rectas, la cual viene dada por ($x_s$, $y_s$). Este sistema se puede escribir de la siguiente forma:
$$\begin{align}
a_1x + b_1y =& c_1 \tag{1}\\
a_2x + b_2y =& c_2 \tag{2}
\end{align}$$

^3113b6

El cual anteriormente había explicado que se podía escribir en su forma [[1- Breve Introducción al Álgebra Lineal#^af436c|vectorial]]:
$$\underbrace{\begin{bmatrix} 
a_1 & b_1 \\ 
a_2 & b_2 
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix} 
x \\ y
\end{bmatrix}}_{\bm{\text{x}}} 
= 
\underbrace{\begin{bmatrix} 
c_1 \\ c_2 
\end{bmatrix}}_{\bm{\text{c}}}$$
Donde obtenemos $A\bm{\text{x}} = \bm{\text{c}}$, el cual es un sistema de ecuaciones de 2 ecuaciones y 2 incógnitas que posee solución $\bm{\text{x}} = A^{-1}\bm{\text{c}}$. Sin embargo, este método supone que nosotros tendremos que buscar formas de computar el valor de $A^{-1}$, cosa que puede llegar a ser costoso a niveles computacionales, es por eso que los algoritmos a enseñar en este tema solucionan estos sistemas sin tener que recurrir al cálculo de al inversa de una matriz.

## Métodos Conocidos de Resolución

Durante el curso de MAT-022 vimos 2 formas distintas de solucionar sistemas de ecuaciones lineales que vamos a repasar brevemente para estudiar sus implicancias a nivel computacional.

### Por Substitución
Este es el método más simple por naturaleza, lo único que tenemos que hacer es despejar una variable que tengan en común 2 o más ecuaciones de un mismo sistema y reemplazar su valor en alguna de estas ecuaciones. Tomando como ejemplo la ecuación anterior y despejando la [[5- Sistemas de Ecuaciones Lineales#^3113b6|ecuación 1]] obtenemos:
$$x = \frac{c_1 - b_1y}{a_1} \tag{3}$$ ^977f18

Reemplazando el valor de la ecuación 3 en la [[5- Sistemas de Ecuaciones Lineales#^3113b6|ecuación 2]] obtenemos:
$$a_2\frac{c_1-b_1y}{a_1} + b_2y = c_2$$

Donde finalmente podemos despejar la última incógnita $y$ que queda:
$$y = \frac{c_2-a_2\frac{c_1}{a_1}}{b_2-a_2\frac{b_1}{a_1}} = \frac{a_1c_2 - a_2c_1}{a_1b_2 - a_2b_1} \tag{4}$$
Y para obtener $x$ basta con reemplazar el valor de la ecuación 4 en la [[5- Sistemas de Ecuaciones Lineales#^977f18|ecuación 3]]:
$$x = \frac{c_1b_2 - c_2b_1}{a_1b_2 - a_2b_1}$$

### Regla de Cramer
La regla de Cramer nos dice que las soluciones para cada una de las $x_i$ incógnitas de un sistema de ecuaciones viene dada por la siguiente expresión:
$$x_i = \frac{D_{x_i}}{D_s}$$
Donde $D_{x_i}$ corresponde al [[1- Breve Introducción al Álgebra Lineal#Determinante|determinante]] de la variable $x_i$ y $D_s$ corresponde al determinante del sistema completo. Para el sistema de ecuaciones dado como primer ejemplo tenemos:
$$\begin{align}
x =& \frac{\left| \begin{align} c_1\ &\ b_1\\ c_2\ &\ b_2 \end{align} \right|}{\left| \begin{align} a_1\ &\ b_1\\ a_2\ &\ b_2 \end{align} \right|} \\ \\
y =& \frac{\left| \begin{align} a_1\ &\ c_1\\ a_2\ &\ c_2 \end{align} \right|}{\left| \begin{align} a_1\ &\ b_1\\ a_2\ &\ b_2 \end{align} \right|} 
\end{align}$$

### Análisis Método de Substitución y Regla de Cramer
De ambos métodos enseñados/repasados anteriormente, podemos sacar las siguientes conclusiones:
- El método de substitución es simple en la práctica, pero a la hora de implementarlo puede llegar a ser muy engorroso.
- Método muy simple de explicar pero MUY costoso a nivel computacional. Imagina tener que computar el determinante de cada matriz $n\times n$ que necesites para cada una de las incógnitas que tengas.

El método de substitución es muy engorroso de implementar debido a la potencialmente densa estructura que puede llegar a adoptar la matriz representativa de nuestro sistema de ecuaciones. Ahora, ¿Qué definimos como una estructura no densa para esta matriz? por ejemplo, una [[1- Breve Introducción al Álgebra Lineal#Matriz Diagonal|matriz diagonal]], donde las soluciones se obtienen dividiendo los coeficientes del lado derecho por los elementos de la diagonal de la matriz. Ahora, de forma más generalizada podemos decir que una matriz posee un patrón adecuado para aplicar este método si esta corresponde a una [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|matriz triangular superior]]. Consideremos por ejemplo este sistema de ecuaciones:
$$\begin{align}
ax + by =& d \tag{5}\\
0x + cy =& e \tag{6}
\end{align}$$
Si bien la solución de este sistema no es trivial, es bastante rápido el llegar a obtenerla. Despejando $y$ de la ecuación 6 tenemos:
$$y = \frac{e}{c}$$
Reemplazando en la ecuación 5 obtenemos y despejando $x$ obtenemos:
$$x = \frac{d-b\frac{e}{c}}{a}$$
Por lo que efectivamente resulta muy conveniente aplicar este método para resolver sistemas de ecuaciones que se puedan representar como una matriz triangular superior. El siguiente método del que voy a hablar se encarga específicamente de transformar una matriz cualquiera en una matriz de esta misma estructura.

## Eliminación Gaussiana Simple

Consideremos un sistema de ecuaciones lineales con 2 ecuaciones y 2 incógnitas de la siguiente forma:
$$\begin{bmatrix} 
a_1 & b_1 \\ 
a_2 & b_2 
\end{bmatrix}
\begin{bmatrix} 
x \\ y
\end{bmatrix}
= 
\begin{bmatrix} 
c_1 \\ c_2 
\end{bmatrix}$$
La cual podemos transformar en una matriz extendida:
$$ \left[ \begin{array}{cc|c} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ \end{array} \right] $$
Con esta expresión nosotros podemos realizar una [[1- Breve Introducción al Álgebra Lineal#Operaciones Fila|operación fila]] para poder volver el coeficiente que se ubica en la misma posición en la que se encuentra $a_2$ en 0:
$$R_2 = R_2-\frac{a_2}{a_1}R_1$$
la cual nos indica que el resultado de la fila 2 (expresada por $R_2$) va a ser equivalente a restarle la fila 1 siendo esta multiplicada por el coeficiente $\frac{a_2}{a_1}$, con lo que nuestra matriz extendida queda:
$$ \left[ \begin{array}{cc|c} 
a_1 & b_1 & c_1 \\ 
0 & \left( b_2 - \frac{a_2}{a_1}b_1 \right) & c_2 - \frac{a_2}{a_1}c_1\\ 
\end{array} \right] $$
El cual equivale al siguiente sistema de ecuaciones lineales:
$$\begin{align}
a_1x + b_1y =&\ c_1 \tag{7}\\
0x + \left( b_2 - \frac{a_2}{a_1}b_1 \right) y =&\ c_2 - \frac{a_2}{a_1}c_1 \tag{8}
\end{align}$$
El valor de $y$ entonces lo podemos obtener de la ecuación 8:
$$y = \frac{c_2 - \frac{a_2}{a_1}c_1}{b_2 - \frac{a_2}{a_1}b_1} = \frac{a_1c_2 - a_2c_1}{a_1b_2 - a_2b_1}$$
Ahora podemos reemplazar este valor en la ecuación 7 y obtener el valor de $x$:
$$x = \frac{c_1-b_1y}{a_1} = \frac{c_1b_2 - c_2b_1}{a_1b_2 - a_2b_1}$$
Que corresponden a las mismas soluciones que obtuvimos para el mismo ejemplo con el [[#Por Substitución|método de substitución]].

En resumidas cuentas, el procedimiento para ejecutar el algoritmo es el siguiente:
- Construir la matriz extendida a partir del sistema de ecuaciones lineales $A\bm{\text{x}} = \bm{\text{b}}$.
- Aplicar operaciones fila para transformar el sistema de ecuaciones original, de modo que obtengamos una matriz asociada de forma [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]] y un lado derecho de la forma $U\bm{\text{x}} = \bm{\hat{c}}$.
- Resolver el sistema de ecuaciones resultantes con [[#Backward Substitution|backward sustitution]].

De forma general, nuestra matriz extendida va a tener la siguiente forma:
$$ \left[ \begin{array}{cccc|c} 
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ 
a_{21} & a_{22} &        & a_{2n} & b_2 \\
\vdots &        & \ddots & \vdots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} & b_n
\end{array} \right] 
= 
\left[ \begin{array}{c|c} A & \bm{\text{b}} \end{array} \right]$$
Con lo cual se traduce en el siguiente algoritmo para convertir esta matriz extendida en su forma triangular superior:

```python
for j in range(n):
	for i in range(j+1, n):
		mult = B[i][j]/B[j][j]			
		B[i][j:n+1] = [B[i][k] - mult * B[j][k] for k in range(j, n + 1)]
```

Donde la matriz $C$ es donde se almacena la matriz extendida. 

### Complejidad Computacional de la Eliminación Gaussiana Simple
Para saber la complejidad del algoritmo, basta con estudiar el código anterior para ver la velocidad a la que se termina de ejecutar el algoritmo:

| Línea |  # operaciones  |                 Operación                 |
|:-----:|:---------------:|:-----------------------------------------:|
|  (1)  |       $n$       |                  Conteo                   |
|  (2)  |   $n - j - 1$   |                  Conteo                   |
|  (3)  |       $1$       |                 División                  |
|  (4)  | $2*(n + 1 - j)$ | Multiplicación escalar por vector y resta |

Considerando el anidamiento de las operaciones, obtenemos la siguiente expresión:
$$\sum_{j=1}^{n-1}\ \sum_{i=j+1}^n(1+2(n+1-j)) = \frac{2}{3}n^3 + \frac{1}{2}n^2 - \frac{7}{6}n$$
Con lo que asintóticamente queda una cota de $\theta(n^3)$ como tiempo de ejecución del algoritmo, y realiza una cantidad aproximada de $\frac{2}{3}n^3$ operaciones elementales.

### Backward Substitution

^4d925e

Este término hace referencia a un algoritmo diseñado específicamente para resolver sistemas de ecuaciones lineales que sean de la forma $U\bm{\text{x}} = \bm{\text{b}}$, donde $U$ es una matriz triangular superior y se usa $\tilde{b}$ para denotar al vector del lado derecho:
$$\begin{bmatrix}
u_{11} & u_{12} & \cdots & \cdots      & u_{1n}    \\
0      & u_{22} & \cdots & \cdots      & u_{2n}    \\
\vdots & 0      & \ddots &             & \vdots    \\
\vdots &        & \ddots & u_{n-1,n-1} & u_{n-1,n} \\
0      &        & \cdots & 0           & u_{nn}
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_{n-1} \\
x_n
\end{bmatrix}
=
\begin{bmatrix}
\tilde{b}_1 \\
\tilde{b}_2 \\
\vdots \\
\tilde{b}_{n-1} \\
\tilde{b}_n
\end{bmatrix}$$
Creo que ya se han hecho una idea de como funciona esta forma de sustitución, básicamente vamos a despejar todo nuestro sistema de ecuaciones desde la ecuación más primitiva (la de la fila $n$) hasta la más compleja usando el método de sustitución. Nótese que en la última fila siempre vamos a tener una solución ya dada para una de nuestras incógnitas de nuestro sistema, la que podemos reemplazar en la ecuación ubicada encima de ella para reemplazar otra incógnita más que esté presente en el sistema, después hacemos lo mismo con todas las demás ecuaciones que estén por arriba hasta despejar la última incógnita restante que va a estar en la primera fila.

Algebraicamente hablando, tenemos la expresión para la solución de la última fila expresada de la siguiente forma:
$$u_{n,n}x_n = \tilde{b}_n$$
Con la que obtenemos el valor de $x_n$:
$$x_n = \frac{\tilde{b}_n}{u_{n,n}}$$
Con esto ya podemos escribir la expresión de la penúltima fila ($n-1$) de nuestro sistema de ecuaciones:
$$u_{n-1,n-1}x_{n-1} + u_{n-1,n}x_n = \tilde{b}_{n-1}$$
Gracias a que $x_n$ lo obtuvimos de la ecuación anterior, la única incógnita que hay en en esta iteración es la de $x_{n-1}$:
$$x_{n-1} = \frac{\tilde{b}_{n-1} - u_{n-1,n}x_n}{u_{n-1, n-1}}$$
Y con esto ya podemos obtener la expresión de la i-ésima ecuación:
$$u_{i,i}x_i + \sum_{j = i+1}^{n}u_{i,j}x_j = \tilde{b}_i$$
con la que podemos expresar los resultados de la i-ésima incógnita:
$$x_i = \frac{\tilde{b}_i - \sum_{j = i+1}^{n}u_{i,j}x_j}{u_{i,i}}$$
donde recordemos que tenemos que resolver las incógnitas $x_i$ desde el valor $x_n$ hasta el valor $x_i$, es decir, vamos a iterar sobre $i$ de forma invertida.

### Complejidad Computacional de Backward Substitution
El algoritmo de Backward Substitution viene dado de la siguiente forma:

```python
for i in range(n, 1, -1):
	for j in range(i+1, n):
		b[i] = b[i] - u[i][j] * x[j]			
	x[i] = b[i]/u[i][i]
```

Considerando las operaciones y los ciclos tenemos una cantidad de operaciones elementales dada por:
$$\sum_{i=1}^{n}\left[2 \left(\sum_{j = i+1}^{n} 1 \right) + 1 \right] = n^2$$
Esto implica que este algoritmo de solución posee una complejidad $\theta (n^2)$ además de realizar $n^2$ operaciones elementales.

## Factorización $\text{LU}$ de $A$ 
 
 Ya hemos visto que la eliminación Gaussiana logra obtener las soluciones de un sistema de ecuaciones lineales de la forma $Ax=\bm{\text{b}}$ transformando la matriz izquierda a su forma [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]], quedando un sistema de la forma $Ux = \bm{\tilde{b}}$. Ahora, supongamos que nosotros queremos resolver nuevamente el mismo sistema de ecuaciones lineales, solamente cambiando los valores a la derecha de la matriz. 
 Por ejemplo, resolvemos inicialmente:
 $$\begin{align}
 a_{11}x + a_{12}y =&\ b_1\\
 a_{21}x + a_{22}y =&\ b_2
 \end{align}$$
 Con lo que naturalmente tenemos un sistema de ecuaciones de la forma $Ax=\bm{\text{b}}$, la cual al eliminar de forma Gaussiana obtenemos un sistema de la forma $Ux = \bm{\tilde{b}}$. Supongamos ahora que necesitamos resolver el mismo sistema de ecuaciones, pero con distintos valores a la derecha de nuestras ecuaciones:
 $$\begin{align}
 a_{11}x + a_{12}y =&\ d_1\\
 a_{21}x + a_{22}y =&\ d_2
 \end{align}$$
 Ahora tendremos un sistema de ecuaciones lineales de la forma $Ax=\bm{\text{d}}$, donde tendremos que aplicar nuevamente la técnica de eliminación Gaussiana para transformar nuestro sistema a uno de la forma $Ux = \bm{\tilde{d}}$. 

Hacer estas 2 tareas con lo que hemos aprendido hasta ahora involucra tener que realizar eliminación Gaussiana un total de 2 veces, lo que involucra la realización de 2 veces $\frac{2}{3}n^3$ operaciones elementales de forma aproximada para poder lograrlo según lo que se repasó en el apartado de [[#Complejidad Computacional de la Eliminación Gaussiana Simple]]. Como podrán haber notado, la expresión $U$ aparece repetida en ambas ecuaciones luego de haber transformado la matriz $A$ a su forma [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]], por lo que como pueden haber intuido en este punto existe una forma de optimizar el cálculo de nuevos sistemas de ecuaciones donde solamente cambiemos su lado derecho.

La factorización $\text{LU}$ de $A$ es bastante simple, lo único que hay que hacer es reescribir la expresión $A$ en función del producto entre una matriz [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular inferior]] $L$ y una matriz [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]] $U$, o sea, expresar $A = LU$. Gracias a la técnica de eliminación Gaussiana somo capaces de obtener la matriz $U$, por lo que ahora nos queda descubrir como es que podemos obtener la matriz $L$, y para ello vamos a utilizar las siguientes afirmaciones: ^8d7f72

- Sea $L_{ij}(-c)$ una matriz triangular inferior la cual tiene coeficientes no-cero en su diagonal y en la posición ($i$, $j$). En particular la diagonal está compuesta de solamente 1´s y en la posición ($i$, $j$) está el valor $-c$. Entonces $L_{ij}(-c)A$ representa la operación fila "restar a la fila $i$  el valor de la fila $j$ multiplicada por $c$". Esto quiere decir que es posible representar operaciones fila mediante una transformación lineal. Por ejemplo:
$$A = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
, L_{21}(-c)*A =
\begin{bmatrix}
1 & 0 \\
-c & 1
\end{bmatrix}
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
= 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} - ca_{11} & a_{22} - ca_{12}
\end{bmatrix}$$
 ^c1cb0e
- $L_{ij}^{-1}(-c) = L_{ij}c$, es decir, la matriz inversa de $L_{ij}(-c)$ es igual a $L_{ij}(c)$. Esto significa que $L_{ij}(-c)L_{ij}(c) = I$, donde $I$ corresponde a la [[1- Breve Introducción al Álgebra Lineal#Matriz Identidad|matriz identidad]]. Por ejemplo:
$$\begin{bmatrix}
1 & 0 \\
-c & 1
\end{bmatrix}
^{-1}
\begin{bmatrix}
1 & 0 \\
-c & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
c & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
-c & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
c - c & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}$$
 ^d4e7ab
- La siguiente ecuación matricial es cierta:
$$\begin{bmatrix}
1   & 0 & 0 \\
c_1 & 1 & 0 \\
0   & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1   & 0 & 0 \\
0   & 1 & 0 \\
c_2 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0   & 0 \\
0 & 1   & 0 \\
0 & c_3 & 1
\end{bmatrix}
=
\begin{bmatrix}
1   & 0   & 0 \\
c_1 & 1   & 0 \\
c_2 & c_3 & 1
\end{bmatrix}$$
^31b521

Ahora que poseemos las aseveraciones necesarias, podemos empezar a plantearnos obtener la matriz $L$. Tomemos como ejemplo la siguiente matriz $A$:
$$A = \begin{bmatrix}
1  & 2 & -1 \\
2  & 1 & -2 \\
-3 & 1 & 1
\end{bmatrix}$$
Dado que $A$ es una matriz $3 \times 3$ sabemos que solo necesitamos realizar 3 operaciones fila para transformarla en la matriz triangular superior $U$. Considerando la [[5- Sistemas de Ecuaciones Lineales#^c1cb0e|primera aseveración]] vista, podemos escribir las operaciones fila necesarias para obtener el valor de U:
$$\underbrace{\begin{bmatrix}
1  & 0           & 0 \\
0  & 1           & 0 \\
0  & \frac{7}{3} & 1
\end{bmatrix}}_{L_{3,2}(7/3)}
\underbrace{\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
3 & 0 & 1
\end{bmatrix}}_{L_{3,1}(3)}
\underbrace{\begin{bmatrix}
1  & 0 & 0 \\
-2 & 1 & 0 \\
0  & 0 & 1
\end{bmatrix}}_{L_{2,1}(-2)}
\underbrace{\begin{bmatrix}
1  & 2 & -1 \\
2  & 1 & -2 \\
-3 & 1 & 1
\end{bmatrix}}_{A}
= 
\underbrace{\begin{bmatrix}
1 & 2  & -1 \\
0 & -3 & 0  \\
0 & 0  & -2
\end{bmatrix}}_{U}$$
Cabe recordar en este punto que NO estamos usando la matriz extendida de $A$, por lo que no estamos considerando esa parte derecha del sistema de ecuaciones lineales. La expresión anterior la podemos representar de una forma más simplista:
$$L_{3,2}(7/3)L_{3,1}(3)L_{3,1}(-2)A = U$$
Despejando $A$ y utilizando la [[5- Sistemas de Ecuaciones Lineales#^d4e7ab|segunda aseveración]] obtenemos:
$$\begin{align}
A =&\ L_{3,1}(-2)^{-1}L_{3,1}(3)^{-1}L_{3,2}(7/3)^{-1}U \\
=&\ L_{3,1}(2)L_{3,1}(-3)L_{3,2}(-7/3)U
\end{align}$$
Y para terminar podemos usar la [[5- Sistemas de Ecuaciones Lineales#^31b521|tercera aseveración]] para finalmente llegar a la expresión de $L$:
$$\begin{align} 
A =&\
\underbrace{\begin{bmatrix}
1  & 0 & 0 \\
2  & 1 & 0 \\
0  & 0 & 1
\end{bmatrix}}_{L_{2,1}(2)}
\underbrace{\begin{bmatrix}
1  & 0 & 0 \\
0  & 1 & 0 \\
-3 & 0 & 1
\end{bmatrix}}_{L_{3,1}(-3)}
\underbrace{\begin{bmatrix}
1  & 0           & 0 \\
0  & 1           & 0 \\
0  & \frac{7}{3} & 1
\end{bmatrix}}_{L_{3,2}(-7/3)}
\underbrace{\begin{bmatrix}
1 & 2  & -1 \\
0 & -3 & 0  \\
0 & 0  & -2
\end{bmatrix}}_{U}
\\
=&\ \underbrace{\begin{bmatrix}
1   & 0           & 0 \\
2   & 1           & 0 \\
-3  & \frac{7}{3} & 1
\end{bmatrix}}_{L}
\underbrace{\begin{bmatrix}
1 & 2  & -1 \\
0 & -3 & 0  \\
0 & 0  & -2
\end{bmatrix}}_{U}
\end{align}$$
Con esto podemos interpretar a $L$ como un conjunto de instrucciones operaciones fila expresadas en la forma de transformaciones lineales, los cuales consisten en las operaciones necesarias para realizar la eliminación Gaussiana.  ^a5058e

### Utilización de la Factorización $\bm{\text{LU}}$ 
Tal como nosotros vimos con la [[5- Sistemas de Ecuaciones Lineales#Eliminación Gaussiana Simple|eliminación Gaussiana simple]], es bastante factible aprovechar la estructura [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]] de la matriz $U$ con tal de resolver eficientemente el sistema de ecuaciones. En este caso tenemos además que la matriz $L$ posee una estructura [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular inferior]], cual por supuesto podemos aprovechar para calcular rápidamente el valor de esta matriz mediante *Forward Substitution* (que en esencia es lo mismo que [[5- Sistemas de Ecuaciones Lineales#Backward Substitution|Backward Substitution]], solo que esta vez el sistema de ecuaciones nuevo se resuelve de arriba hacia abajo). Para ejemplificar esto tomemos el siguiente sistema de ecuaciones:
$$Ax = \bm{\text{b}}$$
Supongamos que logramos realizar la factorización $\bm{\text{LU}}$ de $A$: ^b3b0e3
$$\begin{align}
Ax              =&\ \bm{\text{b}} \\
\bm{\text{LU}}x =&\ \bm{\text{b}}
\end{align}$$
Suponiendo además que ya logramos obtener el valor de $\bm{\text{U}}$ mediante el uso de la eliminación Gaussiana, hagamos ahora el cambio de variable $\bm{\text{c}} = Ux$:
$$\begin{align}
\bm{\text{L}}\underbrace{\bm{\text{U}}x}_{\bm{\text{c}}} =&\ \bm{\text{b}} \\
\bm{\text{Lc}}                                           =&\ \bm{\text{b}}
\end{align}$$
Y notemos ahora que obtuvimos un nuevo sistema de ecuaciones lineales en función de $\bm{\text{L}}$! Nótese eso si que esto ha sido posible realizarlo debido a que el producto punto entre $\bm{\text{U}}$ y $x$ nos dan nuevas incógnitas desconocidas. Escribamos el sistema de ecuaciones nuevo en su forma vectorial:
$$\begin{bmatrix}
1       &      0  & \cdots & \cdots      & 0      \\
l_{2,1} & 1       & \ddots & \ddots      & 0      \\
l_{3,1} & l_{3,2} & 1      & \ddots      & 0      \\
\vdots  &         & \ddots & \ddots      & \vdots \\
l_{n,1} & \cdots  & \cdots & l_{n,n-1}           & 1
\end{bmatrix}
\begin{bmatrix}
c_1 \\
c_2 \\
c_3 \\
\vdots \\
c_{n-1} \\
c_n
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\
b_2 \\
b_3 \\
\vdots \\
b_{n-1} \\
b_n
\end{bmatrix}$$
Y en efecto, es evidente decir que usando *Forward Substitution* es posible despejar todos los valores asociados a la matriz $\bm{\text{c}}$. Es más, gracias a haber despejado $\bm{\text{c}}$ ahora nosotros podemos despejar el valor de $x$:
$$\bm{\text{U}}x = \bm{\text{c}}$$
$$\begin{bmatrix}
u_{11} & u_{12} & \cdots & \cdots      & u_{1n}    \\
0      & u_{22} & \cdots & \cdots      & u_{2n}    \\
\vdots & 0      & \ddots &             & \vdots    \\
\vdots &        & \ddots & u_{n-1,n-1} & u_{n-1,n} \\
0      &        & \cdots & 0           & u_{nn}
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_{n-1} \\
x_n
\end{bmatrix}
=
\begin{bmatrix}
c_1 \\
c_2 \\
\vdots \\
c_{n-1} \\
c_n
\end{bmatrix}$$
Como sabemos los valores de la matriz $\bm{\text{U}}$ y los valores de la matriz $\bm{\text{c}}$ entonces basta con usar [[5- Sistemas de Ecuaciones Lineales#Backward Substitution|Backward Substitution]] para finalmente obtener los valores de $x$.

El algoritmo completo para describir la resolución del sistema de ecuaciones lineales original $Ax = \bm{\text{b}}$ entonces es el siguiente:

```python
L,U = computeLU(A)
c = ForwardSubstitution(L,b)
x = BackwardSubstitution(U,c)
return x
```

Notemos que el la cantidad aproximada de operaciones elementales para resolver el sistema de ecuaciones es de $\frac{2}{3}n^3 + 2n^2$ si es que no conocemos $\bm{\text{U}}$, donde el término $\frac{2}{3}n^3$ equivale a la cantidad de operaciones elementales para realizar la eliminación Gaussiana simple para poder obtenerla, mientras que el otro término $2n^2$ equivale a las operaciones elementales para la [[5- Sistemas de Ecuaciones Lineales#Backward Substitution|Backward Substitution]] y la *Forward Substitution* (naturalmente necesitando esta última la misma cantidad de operaciones elementales que la primera). Aunque bien recordemos que resolver un sistema de ecuaciones mediante [[5- Sistemas de Ecuaciones Lineales#Complejidad Computacional de la Eliminación Gaussiana Simple|eliminación Gaussiana simple]] solo tome $\frac{2}{3}n^3 + n^2$ operaciones elementales tomando en cuenta además las operaciones de *Backward Substitution*, el método de factorización $\bm{\text{LU}}$ obtiene la ventaja una vez nosotros sepamos el valor de $\bm{\text{U}}$, necesitando únicamente $2n^2$ operaciones elementales en resolver el mismo sistema de ecuaciones lineal $Ax = \bm{\text{b}}_i$ para valores distintos de $\bm{\text{b}}_i$.

## Factorización $\bm{\text{P}}A = \bm{\text{L}}U$

Hasta ahora he dado a entender de manera implícita que la factorización $\bm{\text{LU}}$ puede aplicarse a cualquier matriz, sin embargo, esto se aleja bastante de la realidad, por ejemplo, en la matriz $\begin{bmatrix} 0 & 2 \\ 3 & 4 \end{bmatrix}$ es imposible realizar esta factorización básicamente porque no existe ninguna forma de realizar alguna operación fila sobre la fila inferior de la matriz tal que el término 3 se haga 0. Además de esto, la factorización $\bm{\text{LU}}$ posee la gran desventaja de que computacionalmente puede ser imprecisa a la hora de devolver resultados. Ejemplifiquemos esta situación en el siguiente ejemplo considerando $\delta = 10^{-20}$:
$$\begin{bmatrix}
\delta & 1 \\
1      & 2
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
1 \\
4
\end{bmatrix}$$
Realizando la factorización $\bm{\text{LU}}$ con [[2- Estándar de Punto Flotante y Pérdida de Importancia#^aeafae|precisión doble]] obtenemos:
$$\begin{bmatrix}
1        & 0 \\
10^{20} & 1
\end{bmatrix}
\begin{bmatrix}
10^{-20} & 1 \\
0        & -10^{20}
\end{bmatrix}
\tag{9}$$
Siendo que tuvimos que haber obtenido:
$$\begin{bmatrix}
1        & 0 \\
10^{20} & 1
\end{bmatrix}
\begin{bmatrix}
10^{-20} & 1 \\
0        & 2-10^{20}
\end{bmatrix}$$
Donde claramente podemos observar que $fl(2-10^{20}) = -10^{20}$, lo que provocará por supuesto un error bastante significativo en la solución final del problema, y en efecto, las soluciones obtenidas al resolver el sistema de ecuaciones usando los valores de la ecuación 9 son:
$$\bm{x}_a = 
\begin{bmatrix}
4 \\
1
\end{bmatrix}$$
siendo que la solución real es de:
$$\bm{x}_a =
\begin{bmatrix}
2 - 10^{-20} \\
1 + 10^{-20}
\end{bmatrix}$$
por lo tanto, la factorización $\bm{\text{LU}}$ ha dado un error demasiado grande a la hora de darnos una solución factible al problema. 

Ahora, consideremos que ahora vamos a alternar las filas de las matrices de nuestro sistema de ecuaciones, de forma que nosotros multiplicaremos todo nuestro sistema de ecuaciones lineales por una matriz $\bm{\text{P}} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$:
$$\begin{align}
Ax =&\ \bm{\text{b}} \\
\bm{\text{P}}Ax =&\ \bm{\text{Pb}}
\end{align}$$
Para el caso anterior obtendremos el siguiente sistema de ecuaciones lineales:
$$\begin{bmatrix}
1      & 2 \\
\delta & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
4 \\
1
\end{bmatrix}$$
Finalmente, la factorización $\bm{\text{LU}}$ de la matriz $\bm{\text{PA}}$ es la siguiente:
$$\bm{\text{P}}A = \bm{\text{L}}U =
\begin{bmatrix}
1        & 0 \\
10^{-20} & 1
\end{bmatrix}
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}$$
Donde al resolver este nuevo sistema de ecuaciones asociado se obtiene:
$$\bm{x}_a = 
\begin{bmatrix}
2 \\
1
\end{bmatrix}$$
lo cual por supuesto es una aproximación muy buena en comparación a usar la factorización $\bm{\text{LU}}$ a secas, y esto tan solo cambiando el orden de las filas, la cual es la idea de esta factorización nueva. Ahora, es posible que no siempre resulte conveniente realizar este tipo de factorización para realizar, por lo que es necesario buscar una forma de decidir la estructura de nuestra *matriz de permutación* $\bm{\text{P}}$.

### Partial Pivoting
Esta técnica es la que se usa para decidir la mejor estructura de $\bm{\text{P}}$ cuando nosotros decidamos usar la factorización $\bm{\text{P}}A = \bm{\text{L}}U$ a la hora de resolver un sistema de ecuaciones lineales. Al ser $\bm{\text{P}}$ una matriz de permutación nos interesa que cada una de sus casillas sea 0 excepto por un 1 por cada fila y columna, algo así como un sudoku, por ejemplo: $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$  posee solamente una casilla con valor 1 para cada fila y columna por separado. 

La idea de Partial Pivoting es dejar el máximo coeficiente, en valor absoluto, de cada columna de nuestra matriz debajo de la diagonal de esta misma, o en términos matemáticos dejar en la diagonal el coeficiente $\max_{i>j}|a_{ij}|$. Ejemplificaré la explicación que acabo de redactar en mesa de encantamientos de la ejecución de esta técnica, así que consideremos la matriz:
$$\underbrace{\begin{bmatrix}
2 & 1 & 5  \\
4 & 4 & -4 \\
1 & 3 & 1
\end{bmatrix}}_{A}
;\ 
\underbrace{\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\bm{\text{P}}}
\ y\ 
\underbrace{\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{L}
$$
Empecemos estudiando la primera columna de la matriz $A$. Primero nos interesa revisar si es que necesitamos realizar modificaciones a la matriz de permutación $\bm{\text{P}}$, y para ello vamos a comparar todos los coeficientes de la primera columna de $A$ para revisar cual de los módulos de estos coeficientes es el mayor, siendo en este caso el valor presente en la segunda fila, el número 4. Para aplicar este cambio en la matriz $A$ basta con cambiar de posición el 1 ubicado en la primera fila de la matriz $\bm{\text{P}}$ hasta la segunda columna:
$$\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\bm{\text{P}}_1}
\underbrace{\begin{bmatrix}
2 & 1 & 5  \\
4 & 4 & -4 \\
1 & 3 & 1
\end{bmatrix}}_{A}
=\ \\
\underbrace{\begin{bmatrix}
4 & 4 & -4 \\
2 & 1 & 5  \\
1 & 3 & 1
\end{bmatrix}}_{A_1}
;\ 
\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\bm{\text{P}}_1}
\ y\ 
\underbrace{\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{L}$$
A partir de aquí podemos notar que la permutación realizada por $\bm{\text{P}}$ la podemos leer de esta forma: *En la matriz $A$ quiero que en la fila $i$ esté fila $j$, donde se tiene que cumplir para todos los valores tales que $\bm{\text{P}}_{ij} = 1$*, es decir, para el ejemplo que acabo de dar, se puede leer como "en la fila 1 de la matriz $A$ tiene que estar la fila 2 de la misma matriz, ya que $\bm{\text{P}}_{1,2} = 1$".
Una vez hayamos elegido nuestro pivote para la columna, necesitamos ahora asignar las [[5- Sistemas de Ecuaciones Lineales#^c1cb0e|operaciones elementales de la matriz]] $L$ necesarias para transformar $A$ a su forma [[1- Breve Introducción al Álgebra Lineal#Matrices Triangulares|triangular superior]]:
$$\underbrace{\begin{bmatrix}
1           & 0 & 0 \\
\frac{1}{2} & 1 & 0 \\
0           & 0 & 1
\end{bmatrix}}_{L_1}
\underbrace{\begin{bmatrix}
4 & 4 & -4 \\
2 & 1 & 5  \\
1 & 3 & 1
\end{bmatrix}}_{A_1}
=\ \\
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & -1 & 7  \\
1 & 3  & 1
\end{bmatrix}}_{A_2}
;\ 
\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\bm{\text{P}}_1}
\ y\ 
\underbrace{\begin{bmatrix}
1           & 0 & 0 \\
\frac{1}{2} & 1 & 0 \\
0           & 0 & 1
\end{bmatrix}}_{L_1}$$
y también necesitamos una nueva operación fila en $L_1$ para terminar de transformar ese 1 en la primera fila a un 0:
$$\underbrace{\begin{bmatrix}
1            & 0 & 0 \\
0            & 1 & 0 \\
-\frac{1}{4} & 0 & 1
\end{bmatrix}}_{L_2'}
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & -1 & 7  \\
1 & 3  & 1
\end{bmatrix}}_{A_2}
=\ \\
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & -1 & 7  \\
0 & 2  & 2
\end{bmatrix}}_{A_3}
;\ 
\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\bm{\text{P}}_1}
\ y\ 
\underbrace{\begin{bmatrix}
1           & 0 & 0 \\
\frac{1}{2} & 1 & 0 \\
\frac{1}{4} & 0 & 1
\end{bmatrix}}_{L_2}$$
Ahora que terminamos con la primera columna de la matriz $A$, tenemos que seguir analizando la siguiente:
$$\underbrace{\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}}_{\bm{\text{P}}_2'}
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & -1 & 7  \\
0 & 2  & 2
\end{bmatrix}}_{A_3}
=\ \\
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & 2  & 2  \\
0 & -1 & 7  
\end{bmatrix}}_{A_4}
;\ 
\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{bmatrix}}_{\bm{\text{P}}_2}
\ y\ 
\underbrace{\begin{bmatrix}
1           & 0 & 0 \\
\frac{1}{4} & 1 & 0 \\
\frac{1}{2} & 0 & 1
\end{bmatrix}}_{L_2}$$
MUY IMPORTANTE, al haber intercambiado las filas 2 y 3 de la matriz $A_3$ también hay que intercambiar las transformaciones hechas en $L_2$, fíjese como se intercambiaron los valores $\frac{1}{2}$ y $\frac{1}{4}$ al aplicar este cambio. Nótese además como es que debido a que estamos revisando la segunda fila de la matriz $A$, no consideramos dentro de la comparación a los valores de la ahora primera fila, y esto es debido a que ya decidimos una vez que alguno de sus coeficientes sean pivotes. Actualizando el valor de $L_2$ tenemos finalmente:
$$\underbrace{\begin{bmatrix}
1 & 0            & 0 \\
0 & 1            & 0 \\
0 & -\frac{1}{2} & 1
\end{bmatrix}}_{L_3'}
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & 2  & 2  \\
0 & -1 & 7  
\end{bmatrix}}_{A_4}
=\ \\
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & 2  & 2  \\
0 & 0 & 8  
\end{bmatrix}}_{A_5}
;\ 
\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{bmatrix}}_{\bm{\text{P}}_2}
\ y\ 
\underbrace{\begin{bmatrix}
1           & 0            & 0 \\
\frac{1}{4} & 1            & 0 \\
\frac{1}{2} & -\frac{1}{2} & 1
\end{bmatrix}}_{L_3}$$
Y por lo tanto, nuestra factorización $\bm{\text{P}}A = \bm{\text{L}}U$ quedaría:
$$\underbrace{\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{bmatrix}}_{\bm{\text{P}}_2}
\underbrace{\begin{bmatrix}
2 & 1 & 5  \\
4 & 4 & -4 \\
1 & 3 & 1
\end{bmatrix}}_{A}
=\ \\
\underbrace{\begin{bmatrix}
1           & 0            & 0 \\
\frac{1}{4} & 1            & 0 \\
\frac{1}{2} & -\frac{1}{2} & 1
\end{bmatrix}}_{L_3}
\
\underbrace{\begin{bmatrix}
4 & 4  & -4 \\
0 & 2  & 2  \\
0 & 0 & 8  
\end{bmatrix}}_{A_5\ =\ U}$$
Nótese que además logramos obtener el valor de la matriz $U$ de nuestro sistema de ecuaciones lineales mientras aplicamos esta técnica!

Finalmente, es posible explicar el procedimiento de este algoritmo de la siguiente forma:
$$\begin{align}
A =&\ U_0 \\
\bm{\text{P}}_1A =&\ U_{\frac{1}{2}} \\
L_1\bm{\text{P}}_1A =&\ U_{1} \\
\bm{\text{P}}_2L_1\bm{\text{P}}_1A =&\ U_{1 + \frac{1}{2}} \\
L_2\bm{\text{P}}_2L_1\bm{\text{P}}_1A =&\ U_{2} \\
\bm{\text{P}}_3L_2\bm{\text{P}}_2L_1\bm{\text{P}}_1A =&\ U_{2 + \frac{1}{2}} \\
L^{-1}\bm{\text{P}}A:= L_3\bm{\text{P}}_3L_2\bm{\text{P}}_2L_1\bm{\text{P}}_1A =&\ U_{3} =: U \\
\end{align}$$
Al terminar el algoritmo, ya debiéramos tener a nuestra disposición los valores de $\bm{\text{P}}$, $L$ y $U$ con los que seremos capaces de resolver nuestro sistema de ecuaciones lineales $Ax = \bm{\text{b}}$:
- Primero tenemos que multiplicar por $\bm{\text{P}}$ a ambos lados de la ecuación:
$$\bm{\text{P}}Ax = \bm{\text{P}}\bm{\text{b}}$$
- Luego, hay que hacer el reemplazo $\bm{\text{P}}A = \bm{\text{L}}U$:
$$LUx = \bm{\text{P}}\bm{\text{b}}$$
- Después hay que resolver $L\bm{\text{c}} = \bm{\text{Pb}}$ usando [[5- Sistemas de Ecuaciones Lineales#^b3b0e3|Forward Substitution]].
- Finalmente, basta con resolver $U\bm{\text{x}} = \bm{\text{c}}$ usando [[5- Sistemas de Ecuaciones Lineales#Backward Substitution|Backward Substitution]]. 

## Método de Newton en $\mathbb{R}^n$

Si bien hasta ahora nos hemos dedicado a estudiar algoritmos que nos permitan resolver sistemas de ecuaciones lineales, ahora vamos a tomarnos un respiro y revisaremos como podemos usar el [[4- Raíces en 1D (Parte 2)#Método de Newton-Raphson|método de Newton]] para resolver sistemas de ecuaciones en $\mathbb{R}^{n \geq 2}$, lo cual nos permitirá solucionar sistemas de ecuaciones no-lineales. Según se acordarán de la materia pasada, este método nos decía que podemos obtener la solución (o [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]]) de una ecuación lineal de la siguiente forma usando una iteración de punto fijo:
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
desde la cual teníamos que empezar proponiendo un *initial guess* que de por sí sea lo suficientemente cercano a la raíz real de $f$. Consideremos ahora el siguiente ejemplo:
$$\begin{align}
x^2 + y^2 =&\ 1 \\
y =&\ x^2
\end{align}$$
Tradicionalmente nosotros podríamos encontrar la solución a este sistema utilizando el método de substitución:
$$y + y^2 = 1$$
lo que nos otorga como resultado $y_{\pm} = \frac{-1\pm \sqrt{5}}{2}$, por lo que las 2 soluciones de $y$ serian:
$$\begin{align}
y_1 \approx&\ 0.61 \\
y_2 \approx&\ -1.61
\end{align}$$
Por supuesto, ahora solo faltaría reemplazar los valores de las soluciones de $y$ para poder obtener la(s) soluciones de $x$. Sin embargo, como ya había mencionado en algún punto, resolver este tipo de ecuaciones por sustitución simplemente es demasiado engorroso a la hora de programarlo (y tomaría además mas tiempo de lo normal poder computar la solución a nuestro problema). Podemos extrapolar el método anterior que nosotros usamos para resolver el sistema a una forma cercana a la del método de Newton:
$$F(\bm{x}) = F\left( \begin{bmatrix} x \\ y \end{bmatrix} \right) = 
\begin{bmatrix} 
x^2 + y^2 - 1 \\ 
y - x^2
\end{bmatrix}
=
\begin{bmatrix} 
0 \\ 
0 
\end{bmatrix}$$
Es decir, estamos buscando un vector $\bm{x} = \begin{bmatrix} x \\ y \end{bmatrix}$ tal que este sea una [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]] de $F$. Proponiendo un método similar al de Newton en 1D se propone la siguiente linealización de $F(\bm{x})$:
$$\begin{align}
\underbrace{F(\bm{x}_{i+1})}_{0} =&\ F(\bm{x}_i) + J(\bm{x}_i) (\bm{x}_{i+1} - \bm{x}_i) + O(||\bm{x}_{i+1} - \bm{x}_i||^2) \\
-F(\bm{x}_i) =&\ J(\bm{x}_i) (\bm{x}_{i+1} - \bm{x}_i) \\
-J^{-1}(\bm{x}_i)F(\bm{x}_i) =&\ \bm{x}_{i+1} - \bm{x}_i \\
\bm{x}_{i+1} =&\ \bm{x}_i - J^{-1}(\bm{x}_i)F(\bm{x}_i)
\end{align}$$
Donde $J(\bm{x}_i)$ es la matriz jacobiana de $F$ evaluada en el punto $\bm{x}_i$. De forma generalizada, podemos escribir la expresión $F(\bm{x})$ de la siguiente forma:
$$F(\bm{x}) = F\left( 
\begin{bmatrix} 
x_1 \\ 
x_2 \\
\vdots \\
x_n
\end{bmatrix} 
\right) = 
\begin{bmatrix} 
f_1(\bm{x}) \\ 
f_2(\bm{x}) \\
\vdots \\
f_n(\bm{x})
\end{bmatrix}
=
\begin{bmatrix} 
f_1(x_1, x_2, \cdots, x_n) \\ 
f_2(x_1, x_2, \cdots, x_n) \\
\vdots \\
f_n(x_1, x_2, \cdots, x_n)
\end{bmatrix}$$
Y lo mismo podemos hacer para la matriz jacobiana $J(\bm{x}_i)$:
$$ J(\bm{x}) = J_F(\bm{x}_i) = J(F) \bigg|_{\bm{x} = \bm{x}_i} = 
\left[ 
	\frac{\partial f_i}{\partial x_j} 
\right] 
\bigg|_{\bm{x} = \bm{x}_i} = 
	\begin{bmatrix} 
		\nabla f_1 \\ 
		\nabla f_2 \\ 
		\vdots \\ 
		\nabla f_n \\ 
	\end{bmatrix} 
\bigg|_{x = x_i} $$
Volviendo al ejemplo inicial, podemos aplicar el método de Newton para nuestra función:
$$F(\bm{x}) = 
\begin{bmatrix}
x^2 + y^2 -1 \\
y - x^2 
\end{bmatrix}
=
\begin{bmatrix}
f_1(x,y) \\
f_2(x,y) 
\end{bmatrix}$$
Por supuesto, lo primero que debemos hacer es obtener la matriz jacobiana de $F$, para lo cual necesitamos los gradientes de nuestras funciones $f_1$ y $f_2$:
$$\begin{align}
\nabla f_1(x,y) =&\ \left< \frac{\partial f_1}{\partial x}, \frac{\partial f_1}{\partial y} \right> = \left< 2x,2y \right> \\
\nabla f_2(x,y) =&\ \left< \frac{\partial f_2}{\partial x}, \frac{\partial f_2}{\partial y} \right> = \left< -2x,1 \right>
\end{align}$$
Por lo que nuestra matriz jacobiana queda:
$$J(\bm{x}) = 
\begin{bmatrix}
2x  & 2y \\
-2x & 1
\end{bmatrix}$$
Finalmente, el método de Newton genera la siguiente iteración de punto fijo de alta dimensión:
$$\begin{align}
	\begin{bmatrix}
	x_{i+1} \\
	y_{i+1}
	\end{bmatrix}
	=&\
	\begin{bmatrix}
	x_i \\
	y_i
	\end{bmatrix}
	-J(\bm{x_1})^{-1}
	\begin{bmatrix}
	f_1(x,y) \\
	f_2(x,y)
	\end{bmatrix}
	\\ \\
	\begin{bmatrix}
	x_{i+1} \\
	y_{i+1}
	\end{bmatrix}
	=&\
	\begin{bmatrix}
	x_i \\
	y_i
	\end{bmatrix}
	\begin{bmatrix}
	2x  & 2y \\
	-2x & 1
	\end{bmatrix}
	^{-1}
	\begin{bmatrix}
	x_i^2 + y_i^2 - 1 \\
	y_i - x_i^2
	\end{bmatrix}
\end{align}$$
Donde esta vez necesitaremos un *initial guess* tanto para $x$ como para $y$, los cuales van a estar almacenado en el vector $\bm{x}$.

Este método de Newton lo podemos representar entonces con el siguiente algoritmo:

```python
X_0 = "Initial Guess"
for i in range(n):
	X_{i+1} = X_i - (J(X_i))**(-1) * F(X_i)
```


## Método Iterativo de Jacobi

Para explicar como funciona este algoritmo iterativo, tomemos la siguiente matriz $A$ la cual vamos a descomponer en 3 matrices $L$, $D$ y $U$:
$$\begin{align}
	A =&\ 
	\begin{bmatrix}
		a_{1,1}   & a_{1,2}   & \cdots & a_{1,n-1}   & a_{1,n}   \\
		a_{2,1}   & a_{2,2}   & \ddots & a_{2,n-1}   & a_{2,n}   \\
		\vdots    & \ddots    & \ddots & \ddots      & \vdots    \\
		a_{n-1,1} & a_{n-1,2} & \cdots & a_{n-1,n-1} & a_{n-1,n} \\
		a_{n,1}   & a_{n,2}   & \cdots & a_{n,n-1}   & a_{n,n}   \\
	\end{bmatrix}
	= L + D + U \\ \\
	
	=&\ 
	\underbrace{
		\begin{bmatrix}
			0         & 0         & \cdots & 0           & 0         \\
			a_{2,1}   & 0         & \ddots & 0           & 0         \\
			\vdots    & \ddots    & \ddots & \ddots      & \vdots    \\
			a_{n-1,1} & a_{n-1,2} & \cdots & 0           & 0         \\
			a_{n,1}   & a_{n,2}   & \cdots & a_{n,n-1}   & 0         \\
		\end{bmatrix}
	}_{L}
	+
	\underbrace{
		\begin{bmatrix}
			a_{1,1}   & 0         & \cdots & 0           & 0         \\
			0         & a_{2,2}   & \ddots & 0           & 0         \\
			\vdots    & \ddots    & \ddots & \ddots      & \vdots    \\
			0         & 0         & \cdots & a_{n-1,n-1} & 0         \\
			0         & 0         & \cdots & 0           & a_{n,n}   \\
		\end{bmatrix}
	}_{D}
	+
	\underbrace{
		\begin{bmatrix}
			0         & a_{1,2}   & \cdots & a_{1,n-1}   & a_{1,n}   \\
			0         & 0         & \ddots & a_{2,n-1}   & a_{2,n}   \\
			\vdots    & \ddots    & \ddots & \ddots      & \vdots    \\
			0         & 0         & \cdots & 0           & a_{n-1,n} \\
			0         & 0         & \cdots & 0           & 0         \\
		\end{bmatrix}
	}_{U}
\end{align}$$

Es decir, $L$ posee todos los coeficiente de la matriz $A$ que se ubican debajo de su diagonal, $D$ posee los que están en la diagonal y $U$ los que están arriba de su diagonal. Cabe recalcar que estas matrices $L$ y $U$ no son las mismas que habíamos visto previamente con la factorización $\bm{\text{P}}A = \bm{\text{L}}U$ o $A = \bm{\text{L}}U$.  

Consideremos un sistema de ecuaciones lineales de la forma:
$$A\bm{\text{x}} = \bm{\text{b}}$$
Reemplacemos $A$ por la factorización que realizamos anteriormente:
$$\begin{align}
	A\bm{\text{x}} =&\ \bm{\text{b}} \\
	(L + D +U)\bm{\text{x}} =&\ \bm{\text{b}} \\
	L\bm{\text{x}} + D\bm{\text{x}} + U\bm{\text{x}} = \bm{\text{b}}
\end{align}$$
Dejando solo $D\bm{\text{x}}$ al lado izquierdo de la ecuación obtenemos:
$$\begin{align}
	D\bm{\text{x}} =&\ \bm{\text{b}} - L\bm{\text{x}} - U\bm{\text{x}} \\
	D\bm{\text{x}} =&\ \bm{\text{b}} - (L + U)\bm{\text{x}}
\end{align}$$
Multiplicando ambos lados por $D^{-1}$ podemos despejar $\bm{\text{x}}$:
$$\begin{align}
	D^{-1}D\bm{\text{x}} =&\ D^{-1}(\bm{\text{b}} - (L + U)\bm{\text{x}}) \\
	\bm{\text{x}} =&\ D^{-1}(\bm{\text{b}} - (L + U)\bm{\text{x}})
\end{align}$$
Con la cual obtenemos una ecuación de iteración de punto fijo de alta dimensión para resolver un sistema de ecuaciones lineales que corresponde al método de Jacobi, la cual puede ser descrito de la siguiente forma:
$$\begin{align}
	\bm{\text{x}}_0 =&\ \text{initial guess} \\
	\bm{\text{x}}_{n+1} =&\ D^{-1}(\bm{\text{b}} - (L + U)\bm{\text{x}_n}) =: G(\bm{\text{x}}_n)
\end{align}$$
Donde la segunda ecuación la podemos interpretar como $\bm{\text{x}}_{n+1} = G(\bm{\text{x}}_n)$, y donde al igual que con el [[5- Sistemas de Ecuaciones Lineales#Método de Newton en $ mathbb{R} n$|método de Newton]], el vector $\bm{\text{x}}_0$ corresponde a un vector que posee los *initial guess* para cada una de las incógnitas de nuestro sistema de ecuaciones.

Además, existen otras 2 formas alternativas de este algoritmo que podemos implementar en diversas situaciones según lo estipulemos conveniente. La primera alternativa seria:
$$\begin{align}
	\bm{\text{x}}_{n+1} =&\ D^{-1}(\bm{\text{b}} - (L + U)\bm{\text{x}_n}) \\
	=&\ D^{-1}(\bm{\text{b}} - (L + U + D - D)\bm{\text{x}_n}) \\
	=&\ D^{-1}(\bm{\text{b}} - (A - D)\bm{\text{x}_n}) \\
	=&\ D^{-1}(\bm{\text{b}} - A\bm{\text{x}_n} + D\bm{\text{x}_n}) \\
	=&\ D^{-1}(\bm{\text{b}} - A\bm{\text{x}_n}) + D^{-1}D\bm{\text{x}_n} \\
	=&\ D^{-1}(\bm{\text{b}} - A\bm{\text{x}_n}) + \bm{\text{x}_n} \\
	=&\ \bm{\text{x}_n} + D^{-1}(\bm{\text{b}} - A\bm{\text{x}_n}) \\
	=&\ \bm{\text{x}_n} + D^{-1}\bm{\text{r}_n} 
\end{align}$$
donde $\bm{\text{r}_n} = \bm{\text{b}} - A\bm{\text{x}}_n$ corresponde al vector residual de la n-ésima iteración, es decir, mientras más pequeño sea nuestro $\bm{\text{r}_n}$ entonces más cerca estaremos de nuestro punto fijo (a no ser que nuestros *initial guess* estén muy alejados de sus soluciones reales, por lo que nuestro residuo nos puede incluso llegar a dar un *falso positivo* a la hora de obtener soluciones).
La segunda forma alternativa la podemos derivar del desarrollo anterior:
$$\begin{align}
\bm{\text{x}}_{n+1} =&\ D^{-1}(\bm{\text{b}} - (L + U)\bm{\text{x}_n}) \\
=&\ D^{-1}\bm{\text{b}} - D^{-1}(L + U)\bm{\text{x}_n} \\
=&\ -D^{-1}(L + U)\bm{\text{x}_n} + D^{-1}\bm{\text{b}} \\
\end{align}$$
De aquí podemos concluir que la matriz $M$ para el método de Jacobi corresponde a $M = -D^{-1}(L + U)$ y el vector constante $\hat{b} = D^{-1}\bm{\text{b}}$.  
