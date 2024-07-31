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

Es posible interpretar este algoritmo como el "punto medio" de las 2 sumas de Riemann que les enseñé anteriormente:

![[Apuntes_INF-285_2024-v0613.pdf#page=173&rect=75,233,533,491|Apuntes_INF-285_2024-v0613, p.172]]

donde además podemos apreciar que se logró una mejor aproximación del resultado correcto considerando que la solución real es $\int_{-1}^1 exp(x) \,dx \approx 2.35040\cdots$ 

El código que describe el algoritmo anterior es el siguiente:

```python
def midpoint(myfun, m, a, b): 
	# Se tiene que vectorizar la función a integrar almacenada en 
	# myfun para poder manejarla como arreglo. 
	f = np.vectorize(myfun) 
	# Como queremos m particiones, necesitamos m + 1 puntos. 
	x = np.linspace(a, b, m+1) 
	h = (b − a)/m 
	xhat = x [: −1] + h/2  
	w = np.full(m,h)  
	return np.dot(f(xhat),w)
```

## Regla del Trapecio

Tal como indica su nombre, este algoritmo propone aproximar el resultado de la integral mediante el uso de trapecios en cada sub-intervalo en vez de rectángulos. Para $[x_0,x_1]$ tenemos:
$$\int_{x_0}^{x_1}f(x)\,dx \approx (x_1-x_0)\frac{1}{2}(f(x_0) + f(x_1))$$
El error directo en el intervalo $[x_0,x_1]$ inducido por esta aproximación es explícitamente el siguiente:
$$\int_{x_0}^{x_1}f(x)\,dx = \frac{h}{2}(f(x_0) + f(x_1)) - \frac{h^3}{12}f''(\hat{c})$$
donde $h = x_1 - x_0$ y $\hat{c} \in [x_0,x_1]$. El error compuesto en el intervalo $[a=x_0,x_1,\cdots,b=x_m]$ es el siguiente:
$$\begin{aligned}
	\int_a^b f(x) \,dx &= \sum_{i=1}^m \int_{x_i-1}^{x_i} f(x) \,dx \\
	&= \frac{h}{2} \left[ f(a) + f(b) + 2\sum_{i=1}^{m-1} f(x_i) \right] - (b-a)\frac{h^2}{12}f''(\hat{c})
\end{aligned}$$
donde al igual que con la regla del punto medio  $h = \frac{b-a}{m}$ y $\hat{c} \in [a,b]$.

En comparación de la regla del punto medio, la regla del trapecio ajusta el techo de las particiones de modo que esta se alineen lo más posible con la función a derivar:

![[Apuntes_INF-285_2024-v0613.pdf#page=175&rect=77,458,536,712|Apuntes_INF-285_2024-v0613, p.174]]

El código que describe este algoritmo es el siguiente:

```python
def trapezoid(myfun , m, a, b): 
	f = np.vectorize(myfun) 
	x = np.linspace(a, b, m + 1) 
	h = (b − a)/m 
	# Ahopa creamos un arreglo de NumPy largo m + 1 y lo llenamos con valores h.
	w = np.full(m + 1, h) 
	# Miren el mensaje de abajo de este código para saber porqué se manipula este arreglo como se hace en las 2 lineas. 
	w[0] /= 2 
	w [−1] /= 2 
	return np.dot(f(x), w)
```

>[!info] Detalle del Código
>Como bien podremos recordar, el error compuesto del método del trapecio en un intervalo $[a=x_0,x_1,\cdots,b=x_m]$ viene dado por la siguiente fórmula:
>$$\int_a^b f(x) \,dx = \frac{h}{2} \left[ f(a) + f(b) + 2\sum_{i=1}^{m-1} f(x_i) \right] - (b-a)\frac{h^2}{12}f''(\hat{c})$$
>Esta expresión implica que la formula de integración la podemos aproximar de manera general de la siguiente forma:
>$$\begin{aligned}
>	\int_a^b f(x) \,dx &\approx \frac{h}{2} \left[ f(a) + f(b) + 2\sum_{i=1}^{m-1} f(x_i) \right] \\
>	&\approx \frac{h}{2} (f(a = x_0) + f(b = x_m) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{m-1}))
>\end{aligned}$$
>La explicación de este suceso es, de hecho, bastante sencilla. Lo que nos interesa hacer para integrar una función $f(x)$ es obtener la suma de todas las particiones generadas en los intervalos $([x_0,x_1],\ [x_1,x_2],\ [x_2,x_3],\cdots,\ [x_{m-2},x_{m-1}],\ [x_{m-1},x_m])$, donde nos es fácil notar que los puntos $x_0$ y $x_m$ solo se usan 1 sola vez, por lo que sus pesos $w$ bajan a la mitad. 

## Regla de Simpson

Este algoritmo a diferencia de los anteriores propone aproximar el valor de la integral por medio de parábolas, aunque para este caso se necesitarían 3 puntos o 2 sub-intervalos para la derivación de este, es decir, para $[x_0,x_2]$. En particular si integramos una parábola obtenemos lo siguiente:
$$\int_{x_0}^{x_2}ax^2 + bx + c\,dx = (x_1 - x_0)\frac{1}{3}[(ax^2_0 + bx_0 + c) + 4(ax_1^2 + bx_1 + c) + (ax_2^2 + bx_2 + c)]$$
La cual induce la siguiente aproximación:
$$\int_{x_0}^{x_2}f(x)\,dx \approx h\frac{1}{3}[f(x_0) + 4f(x_1) + f(x_2)]$$
Donde el error inducido por esta aproximación es el siguiente:
$$\int_{x_0}^{x_2}f(x)\,dx = \frac{h}{3}(f(x_0) + 4f(x_1) + f(x_2)) - \frac{h^5}{90}f^{(4)}(\hat{c})$$
donde $h = x_1 - x_0 = x_2 - x_1$ y $\hat{c} \in [x_0,x_2]$. La formulación compuesta en el intervalo $[a=x_0,x_1,\cdots,b=x_m]$ es la siguiente:
$$\int_a^b f(x) \,dx = \frac{h}{3} \left(f(x_0) + 4\sum_{i=1}^n f(x_{2i-1})+ 2\sum_{i=1}^{n-1}f(x_{2i}) + f(x_m) \right) - (b - a)\frac{h^4}{180}f^{(4)}(\hat{c})$$

![[Apuntes_INF-285_2024-v0613.pdf#page=176&rect=75,176,533,427|Apuntes_INF-285_2024-v0613, p.175]]

El código que describe este algoritmo es el siguiente:

```python
def simpsons(myfun , m, a, b): 
	f = np.vectorize(myfun) 
	x = np.linspace(a, b, m + 1) 
	h = (b − a) / m 
	w = np.full(m + 1, h / 3) 
	w[1: − 1:2] *= 4 
	w[2: − 1:2] *= 2 
	return np.dot(f(x), w)
```

Nótese que este y los algoritmos anteriores que se estudiaron resuelven finalmente la integral como el producto punto entre un vector de pesos $\bmf{w}$ y unos nodos $\bmf{x}$, es decir:
$$\bmf{w}f(\bmf{x}) = \sum_{i=1}^n w_if(x_i)$$

## Cuadratura Gaussiana

Como acabo de mencionar antes de empezar este último ítem, se llega a representar computacionalmente el resultado de una integral como el producto entre un conjunto de pesos $w_i$ con un conjunto de puntos $x_i$. Por supuesto, existe un algoritmo que nos permite escoger estos 2 conjuntos de la forma mas óptima posible, que corresponde a este mismo algoritmo de la cuadratura Gaussiana, y lo hace mediante la creación de polinomios de grado $2n - 1$.

Consideremos que queremos aproximar la función $f(x)$ por el polinomio $Q(x) = \sum_{i=1}^n L_i(x)f(x_i)$, es decir, por medio de una [[6- Interpolación Polinomial (Parte 1)|interpolación polinomial]], específicamente la [[6- Interpolación Polinomial (Parte 1)#Interpolación de Lagrange|interpolación de Lagrange]]. Nótese que para esta expresión solamente $L_i(x)$ depende de la variable $x$, y que si bien sabemos que los $x_i$ no dependen de $x$, sabemos que son constantes pero desconocidas. Al realizar la integración obtenemos lo siguiente:
$$\begin{aligned}
	\int_{-1}^1 f(x) \,dx &\approx \int_{-1}^1 Q(x) \,dx = \int_{-1}^1 \sum_{i=1}^n L_i(x)f(x_i) \\
	&= \sum_{i=1}^n f(x_i) \underbrace{\int_{-1}^1 L_i(x) \,dx}_{w_i}
\end{aligned}$$
donde recordemos $L_i(x) = \frac{l_i(x)}{l_i(x_i)}$, $l_i(x) = (x-x_1)(x-x_2)\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_n)$ y tiene la propiedad de que $L_i(x_i) = 1$ y $L_i(x_j) = 0$ para $i \neq j$. Además, si nosotros elegimos los $n$ nodos $x_i$, nuestra cuadratura será por lo menos exacta para el polinomio de grado $n-1$. Por lo tanto, la construcción de $L_i(x)$ va a depender exclusivamente por la definición de los nodos $x_i$. Definiremos para este caso los $x_i$ nodos "adecuados" como la raíz del $n$-ésimo polinomio de Legendre $p_n(x)$: 
$$p_n(x) = \frac{1}{2^nn!}\frac{d^n}{dx^n}[(x^2-1)^n]$$
En la siguiente imagen adjunta pueden observar algunos de los valores obtenidos gracias al polinomio de Legendre:

![[s14_integracion.pdf#page=31&rect=30,38,335,181|s14_integracion, p.30]]

La gran ventaja de este algoritmo es que nos permite integrar de manera perfecta todos los polinomios que sean de grado $2n - 1$ o menor. El algoritmo visualmente se puede observar de la siguiente manera:

![[Pasted image 20240730230833.png]]

Y su algoritmo corresponde al siguiente:

```python
def gaussianquad(f, m, a, b): 
	x, w = gaussian_nodes_and_weights(m) 
	return np.dot(w,f(x)) 
def gaussian_nodes_and_weights (m): 5 if m==1: 6 return np.array ([1]) , np.array ([2]) 
	# Why an eigenvalue problems is related to the roots of the Legendre polynomial mentioned before ? (This is a tricky question !) 
	beta = .5 / np.sqrt(1. − (2.* np. arange (1.,m))**(−2)) 
	T = np.diag(beta ,1) + np.diag(beta , −1) 
	D, V = np.linalg.eigh(T) 
	x = D 
	w = 2 * V [0 ,:]**2 
	return x, w
```

Cabe recordar que la integral se ha definido para resolverse por defecto en el intervalo $[-1,1]$, si esto se quisiera replicar a un nuevo intervalo $[a,b]$ tendríamos que aplicar un cambio de variable con la sustitución $t = \frac{2x - a - b}{b - a}$. Por ejemplo:
$$\int_{a}^bf(x)\,dx = \frac{b-a}{2}\int_{-1}^1f(\frac{(b-a)t}{2} + \frac{b+a}{2})\,dt$$
