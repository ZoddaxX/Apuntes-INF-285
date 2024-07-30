En esta sección estudiaremos diversos algoritmos que nos permitirán obtener valores de integrales definidas que uno pudiera no resolver algebraicamente. Es por esto que trabajaremos este tema en base a la siguiente definición de **Integración Numérica o Cuadratura**: *Esta consiste en la obtención de la constante $c \in \mathbb{R}$, o por lo menos una aproximación de ella, de una integral definida $c = \int_a^b f(x) \, dx$ utilizando algún método numérico* (no confundir con la constante de integración $c$, esta vez se usa este carácter para representar la solución de la integral).

Por lo general existen diversos métodos para el cual uno podría llegar a aproximar los resultados, aunque algunos pueden terminar siendo mucho más conveniente que otros dependiendo del contexto. Por ejemplo:
- Si la función $f(x)$ ha sido evaluada previamente en puntos típicamente equiespaciados resulta ser más conveniente aplicar la regla de Simpson, Trapecio o Punto Medio.
- Si la función $f(x)$ puede llegar a evaluarse en puntos elegidos arbitrariamente resulta ser mucho más conveniente aplicar Cuadratura Gaussiana.

Antes de empezar a estudiar los algoritmos mencionados anteriormente hay que repasar las primitivas bases de las integrales con las sumatorias de Riemann.

## Suma de Riemann

Recordemos que se dice que una función es integrable cuando las sumas izquierdas y derechas de Riemann convergen al mismo valor $c$, es decir:
$$c = \int_a^b f(x) \, dx$$
La suma de Riemann por la izquierda de una función $f(x)$ viene definida de la siguiente forma:
$$c = \int_a^b f(x) \, dx = \sum_{k=0}^{m-1} f(x_k)(x_{k+1}-x_k) + E_L$$
Donde $E_L$ corresponde al error de aproximación numérica y recordemos que los puntos $x_k$ pertenecen a las particiones o discretizaciones $p = \{x_0, x_1, \cdots, x_m\}$ del intervalo de integración $[a,b]$, donde por supuesto el resultado de esta integral va a ser cada vez más preciso mientras más grande sea el valor de $m$, o sea, mientras más numerosas sean las particiones en el intervalo anterior. Esta suma de Riemann básicamente calcula el área bajo la curva de todas las particiones que se puedan formar debajo de la función $f(x)$, tal y como se puede ver en la siguiente imagen:

![[Apuntes_INF-285_2024-v0613.pdf#page=171&rect=79,352,531,604|Apuntes_INF-285_2024-v0613, p.170]]

Por otro lado, la suma de Riemann por la derecha de una función $f(x)$ se define como:
$$c = \int_a^b f(x) \, dx = \sum_{k=0}^{m-1} f(x_{k+1})(x_{k+1}-x_k) + E_R$$
Donde en este caso $E_R$ corresponde al error de aproximación numérica, además, la suma calcula el área bajo la curva de todas las particiones que se puedan formar por encima de la función $f(x)$ como se puede apreciar en la siguiente imagen:

![[Apuntes_INF-285_2024-v0613.pdf#page=172&rect=79,459,532,711|Apuntes_INF-285_2024-v0613, p.171]]

Por lo tanto, si sabemos de antemano que una función $f(x)$ es en efecto una función integrable podemos usar tanto la suma de Riemann tanto por la izquierda como por la derecha:
$$\begin{align}
	c = \int_a^b f(x) \, dx &\approx \sum_{k=0}^{m-1} f(x_k)(x_{k+1}-x_k) \\
	&\approx \sum_{k=0}^{m-1} f(x_{k+1})(x_{k+1}-x_k)
\end{align}$$
En particular, los $m + 1$ puntos $x_i$ de nuestra partición en el intervalo $[a,b]$ siguen la relación $a = x_0 < x_1 < \cdots < x_{m-1} < x_m$, y si estos puntos se ubican en posiciones equiespaciadas entonces la distancia $x_{k+1} - x_k$ se denota como $h$ o $\Delta x$, aunque para mantener un orden a la hora de explicar el contenido en estos apuntes se va a utilizar $h$ para referirnos a este término.

## Regla del Punto Medio

El problema a resolver es el mismo, estimar el valor de $c = \int_a^b f(x) \, dx$, aunque definiremos que nuestro intervalo $[a,b]$ se va a dividir en $m$ sub-intervalos $[a=x_0,x_1,\cdots,x_i,x_{i+1},\cdots,b=x_m]$. Para simplificar la explicación de este algoritmo vamos a trabajar simplemente con el sub-intervalo $[x_0, x_1]$ el cual luego podemos propagar a los demás.

Este algoritmo se puede construir como el algoritmo que integra una constante $K$, es decir:
$$\int_{x_0}^{x_1}K\,dx = K(x_1-x_0)$$
por lo tanto, si consideramos que en un intervalo $[x_0,x_1]$ pequeño nuestra función de integración es aproximadamente constante obtenemos:
$$\int_{x_0}^{x_1}f(x)\,dx \approx f(x_*)(x_1-x_0),$$
donde $x_* = \frac{x_0 + x_1}{2}$. El error directo en el intervalo $[x_0,x_1]$ generado en esta aproximación es el siguiente:
$$\int_{x_0}^{x_1}f(x)\,dx = f(x_*)h + \frac{h^3}{24}f''(\hat{c})$$
donde además $\hat{c} \in [x_0,x_1]$. El error compuesto en el intervalo $[a=x_0,x_1,\cdots,b=x_m]$ es el siguiente:
$$\begin{aligned}
	\int_a^b f(x) \,dx &= \sum_{i=1}^m \int_{x_i-1}^{x_i} f(x) \,dx \\
	&= \sum_{i=1}^m f(x_{*,i})h + \frac{b-1}{24}h^2f''(\hat{c})
\end{aligned}$$
donde esta vez $h = \frac{b-a}{m}$, $x_{*,i} = \frac{1}{2}(x_{i-1} - x_i)$ y  $\hat{c} \in [a,b]$.  