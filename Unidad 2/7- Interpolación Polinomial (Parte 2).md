$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
## Error de Interpolación y Fenómeno de Runge

A continuación se presenta el siguiente teorema que explica un concepto importante para este tema, el **Teorema de Error de Interpolación**: *Asuma que $p(x)$ es el polinomio interpolador (de grado $n-1$ o menor) que ajusta $n$ puntos ($x_1$, $y_1$)$,\cdots,$($x_n$, $y_n$). El error de interpolación viene dado por:*
$$f(x) - p (x) = \frac{(x-x_1)(x-x_2)\cdots(x-x_n)}{n!}f^{(n)}(c),$$
*donde el número $c$ se ubica entre el menor y mayor de los número de $x_1$, $x_2$,$\cdots$, $x_n$*.

Esta fórmula está conformada por 3 componente que voy a explicar ahora:
- $n!$: Este término nos induce preliminarmente en la tentativa dirección del error de interpolación (ahí te veo métodos iterativos...), es decir, la diferencia entre $f(x)$ y $p(x)$ disminuye a medida que aumenta nuestro valor de $n$, AUNQUE esto solamente va a ser cierto siempre y cuando las otras 2 componente estén acotadas o crezcan más lento que $n!$, de lo contrario nos hace sentido que sea el mismo $!n$ el que esté provocando un aumento del error entre $f(x)$ y $p(x)$.

- $f^{(n)}(c)$: Este término requiere la computación de la n-ésima derivada de $f(x)$ y evaluarla en un punto $c$ desconocido el cual lo único que sabemos es que se encuentra en el intervalo \[$min($x_1$, $x_2$,$\cdots$, $x_n$), $\max$($x_1$, $x_2$,$\cdots$, $x_n$)\]. Desde el punto de vista de obtener una cota para $f^{(n)}(c)$ nos interesaría obtener el mayor valor de $|f^{(n)}(x)|$ en el intervalo anteriormente mencionado, por lo que en el fondo no es vital obtener el valor de $c$, sino que más bien nos interesa encontrar un valor para poder acotar $f^{(n)}(x)$. Este término junto con sus grados de libertad dependen exclusivamente de la función que estemos interpolando.

- $(x-x_1)(x-x_2)\cdots(x-x_n)$: La importancia de este término recae en la oportunidad que nos entrega, es decir, destaca que el error de interpolación depende de los puntos usados para interpolar. Esto es significativo, ya que con esto nos podemos empezar a plantear la idea de *cambiar nuestros puntos a interpolar* de forma conveniente para reducir lo más posible nuestro error.

Con respecto a el último término del que expliqué, hay un fenómeno interesante que sucede cuando reúnes a un grupo de puntos equiespaciados a interpolar con un polinomio:

![[Apuntes_INF-285_2024-v0613.pdf#page=120&rect=180,464,429,718|Apuntes_INF-285_2024-v0613, p.119]]

Cuando uno crea un polinomio interpolador para este tipo de conjunto de puntos, se suelen producir "puntas" en los extremos de los puntos a interpolar, además de otras que se ubican entremedio de estos puntos que no son tan precipitados. Ahora, miremos lo que pasa si es que añadimos más puntos a interpolar a la gráfica:

![[s09_interpol_2.pdf#page=9&rect=14,43,351,220|s09_interpol_2, p.8]]

Las puntas que se ubicaban entremedio de los puntos a interpolar parecen estabilizarse y adecuarse al polinomio que uno termina buscando, sin embargo, se suelen acentuar las "puntas" que se ubican en los extremos de nuestros puntos. Este evento es conocido como el **Fenómeno Runge**, el cual es posible normalizar gracias a la utilización de los Puntos de Chebyshev.

## Puntos de Chebyshev

Con el fin de poder simplificar los análisis, se va a utilizar la siguiente restricción:
$$-1 \leq x_1, x_2,\cdots,x_n \leq 1$$
Además, todos los puntos $x$ con los cuales se vana a evaluar los polinomios interpoladores deben cumplir que $x \in [-1,1]$. ^f4e002

Para poder ejemplificar un caso para el cual nosotros queremos minimizar el error que genera el Fenómeno de Runge, podemos empezar a analizar el caso en el que se quieren encontrar 2 puntos $x_1$ y $x_2$, donde nuestra función a minimizar es la siguiente:
$$w(\hat{x}_1, \hat{x}_2) = \max_{x \in [-1,1]} |(x-\hat{x}_1)(x-\hat{x}_2)|$$
La cual corresponde al peor caso del módulo de la expresión $(x-x_1)(x-x_2)\cdots(x-x_n)$ explicada en el caso anterior. Para ser más específicos, el procedimiento considera que el procedimiento de minimización se aplique sobre el cuadrado unitario $[0,1]^2$ y entregue los valores de $x_1$ y $x_2$, lo que podemos traducir en la siguiente expresión:
$$
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
	
\begin{align}
	[x_1, x_2] =&\ \argmin_{\hat{x}_1, \hat{x}_2 \in [-1, 1]} \max_{\substack{x \in [-1, 1]}} |(x - \hat{x}_1)(x - \hat{x}_2)| \\
	=&\ \argmin_{\hat{x}_1, \hat{x}_2 \in [-1, 1]} w(\hat{x}_1, \hat{x}_2) 
\end{align}$$
lo que quiere que nosotros estamos buscando minimizar este peor caso de error. La función $\argmin$ indica que retorna los valores $x_1$ y $x_2$ que minimicen la expresión $w(\hat{x}_1, \hat{x}_2)$, la cual a su vez entrega el valor máximo de $|(x - \hat{x}_1)(x - \hat{x}_2)|$ considerando que $\hat{x}_1$ y $\hat{x}_2$ son valores fijos. Con suficiente entendimiento matemático, estudio teórico y haberse tomado en serio el laboratorio de Estadística Computacional (o simplemente revisando el código disponible en uno de los apuntes hechos personalmente por el profesor [Bonus - 05 - Finding 2 Chebyshev PointsGraphically.ipynb](https://github.com/tclaudioe/Scientific-Computing/tree/master/SC1v2)) uno debiera ser capaz de hacer el siguiente mapa de calor:

![[Apuntes_INF-285_2024-v0613.pdf#page=121&rect=169,316,444,571|Apuntes_INF-285_2024-v0613, p.120]]

Este mapa de calor de dominio $[-1,1]^2$ nos ilustra la cantidad de error obtenida al ubicar los puntos en 2 posiciones, en donde obtenemos los mínimos al ubicar nuestros puntos $x_1$ y $x_2$ exactamente por encima de los puntos blancos. Estos puntos pueden corresponder a:
$$[x_1,x_2] = [0.707106781186547, −0.707106781186547]$$
o bien podríamos tomar:
$$[x_1,x_2] = [−0.707106781186547, 0.707106781186547].$$
Esta respuesta consiste de 2 pares de soluciones que son simétricas, por lo que obtendremos el mismo resultado eligiendo una o la otra. Lo que sí este método hace que sea necesario ejecutar una cantidad demasiado grande de operaciones elementales para poder resolverlo cada vez que sea necesario, y aquí es cuando finalmente llegamos al método de los puntos de Chebyshev. Para el caso de 2 puntos, la solución algebraica corresponde a:
$$\begin{align}
	x_1 =&\ \cos{\frac{\pi}{4}} = \frac{\sqrt{2}}{2} \approx 0.70710678118654752440084436210484903928483593768847 \\
	x_1 =&\ \cos{\frac{3\pi}{4}} = -\frac{\sqrt{2}}{2} \approx -0.70710678118654752440084436210484903928483593768847
\end{align}$$
Naturalmente, y como podrán haber intuido, estos resultados han sido obtenidos gracias al **Teorema de Chebyshev**: *La elección de los números reales $-1 \leq x_1,x_2,\cdots,x_n \leq 1$ que hace el valor de*
$$\max_{-1 \leq x \leq 1}{|(x-x_1)\cdots(x-x_n)|}$$
*lo más pequeño posible es:*
$$x_i = \cos\left(\frac{(2i-1)\pi}{2n}\right),\ i\in\{1,2,\cdots,n\}$$
*y el valor mínimo es $\frac{1}{2^{n-1}}$, el cual es alcanzado por:*
$$(x-x_1)\cdots(x-x_n) = \frac{1}{2^{n-1}}T_n(x)$$
*Donde $T_n(x) = \cos(n\arccos(x))$ es polinomio de Chebyshev de grado $n$*.

En resumidas cuentas, el error de interpolación se minimiza si es que los $n$ puntos de interpolación $[-1,1]$ se eligen como las raíces del polinomio de interpolación de Chebyshev $T_n(x)$ de grado $n$. Podemos intuir además de que a veces incluso necesitamos de menos puntos para poder interpolar una función, por lo que además de aumentar la precisión con la que se logra construir el polinomio se puede reducir considerablemente la cantidad de operaciones necesarias para poder evaluar a este mismo.

Ahora, ¿Qué sucede si es que no consideramos el [[7- Interpolación Polinomial (Parte 2)#^f4e002|supuesto]] que nosotros definimos anteriormente? en ese caso tendremos que realizar un cambio de intervalo para poder calcular los nuevos puntos. Con esto lograremos que los puntos tengan la misma posición relativa en $[a,b]$ a como los teníamos en $[-1,1]$. El proceso de ajuste y traslación de los puntos es el siguiente:
$$x_i = \frac{b+a}{2} + \frac{b-a}{2}\cos\left(\frac{(2i-1)\pi}{2n}\right),\ i\in\{1,2,\cdots,n\}$$
donde la siguiente desigualdad se cumplirá en el intervalo $[a,b]$:
$$|(x-x_1)\cdots(x-x_n)| \leq \frac{\left(\frac{b-a}{2}\right)^n}{2^{n-1}}$$
