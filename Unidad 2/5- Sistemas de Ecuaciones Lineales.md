---
cssclasses:
  - t-c
---

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
Donde $D_{x_i}$ corresponde al [[|determinante]] de la variable $x_i$ y $D_s$ corresponde al determinante del sistema completo. Para el sistema de ecuaciones dado como primer ejemplo tenemos:
$$\begin{align}
x =& \frac{\left| \begin{align} c_1\ &\ b_1\\ c_2\ &\ b_2 \end{align} \right|}{\left| \begin{align} a_1\ &\ b_1\\ a_2\ &\ b_2 \end{align} \right|} \\ \\
y =& \frac{\left| \begin{align} a_1\ &\ c_1\\ a_2\ &\ c_2 \end{align} \right|}{\left| \begin{align} a_1\ &\ b_1\\ a_2\ &\ b_2 \end{align} \right|} 
\end{align}$$

### Análisis Método de Substitución y Regla de Cramer
De ambos métodos enseñados/repasados anteriormente, podemos sacar las siguientes conclusiones:
- El método de substitución es simple en la práctica, pero a la hora de implementarlo puede llegar a ser muy engorroso.
- Método muy simple de explicar pero MUY costoso a nivel computacional. Imagina tener que computar el determinante de cada matriz $n\times n$ que necesites para cada una de las incógnitas que tengas.

El método de substitución es muy engorroso de implementar debido a la potencialmente densa estructura que puede llegar a adoptar la matriz representativa de nuestro sistema de ecuaciones. Ahora, ¿Qué definimos como una estructura no densa para esta matriz? por ejemplo, una [[|matriz diagonal]], donde las soluciones se obtienen dividiendo los coeficientes del lado derecho por los elementos de la diagonal de la matriz. Ahora, de forma más generalizada podemos decir que una matriz posee un patrón adecuado para aplicar este método si esta corresponde a una [[|matriz triangular superior]]. Consideremos por ejemplo este sistema de ecuaciones:
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
Con esta expresión nosotros podemos realizar una [[|operación fila]] para poder volver el coeficiente que se ubica en la misma posición en la que se encuentra $a_2$ en 0:
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
- Construir la matriz extendida a partir del sistema de ecuaciones lineales $A\bm{\text{x}} = \bm{\text{c}}$.
- Aplicar operaciones fila para transformar el sistema de ecuaciones original, de modo que obtengamos una matriz asociada de forma [[|triangular superior]] y un lado derecho de la forma $U\bm{\text{x}} = \bm{\hat{c}}$.
- Resolver el sistema de ecuaciones resultantes con [[#Backward Substitution|backward sustitution]].

De forma general, nuestra matriz extendida va a tener la siguiente forma:
$$ \left[ \begin{array}{cccc|c} 
a_{11} & a_{12} & \cdots & a_{1n} & c_1 \\ 
a_{21} & a_{22} &        & a_{2n} & c_2 \\
\vdots &        & \ddots & \vdots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} & c_n
\end{array} \right] 
= 
\left[ \begin{array}{c|c} A & \bm{\text{c}} \end{array} \right]$$
Con lo cual se traduce en el siguiente algoritmo para convertir esta matriz extendida en su forma triangular superior:

```python
for j in range(n):
	for i in range(j+1, n):
		mult = C[i][j]/C[j][j]			
		C[i][j:n+1] = [C[i][k] - mult * C[j][k] for k in range(j, n + 1)]
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
Con lo que asintóticamente queda una cota de $\theta(n^3)$ como tiempo de ejecución del algoritmo, y una cantidad aproximada de $\frac{2}{3}n^3$ operaciones elementales.

### Backward Substitution
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

