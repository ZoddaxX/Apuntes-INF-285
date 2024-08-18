$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
En todos los problemas que hemos estudiado hasta el momento, ya sea Raíces en 1D, Sistemas de Ecuaciones y Mínimos Cuadrados siempre hemos considerado que la incógnita es una variable $x$, o bien la mayoría de veces un vector $\bmf{x}$ con varias incógnitas. Ahora vamos a considerar que nuestra incógnita por despejar es una función $y(t)$ o $y(x)$ dependiendo de si se trata de una variable temporal o espacial respectivamente.

Cuando nuestro problema dependa de una variable temporal, es decir, buscamos una función $y(t)$, entonces estamos hablando de un *Problema de Valor Inicial*, o IVP del inglés *Initial Value Problem*, y si depende de una variable temporal, es decir, buscamos una función $y(x)$, entonces estamos ante un *Problema de Valor de Frontera*, o BVP del inglés *Boundary Value Problem*.

Para aspectos prácticos del curso, vamos a estudiar solamente los problemas que no pidan despejar funciones que dependan de 1 sola variable, lo que quiere decir que no vamos a revisar formas de solucionar las infames IVBP (o *Initial Value Boundary Problem*) o funciones similares de la forma $y(x,t)$, $y(x,t,z)$, etc...

## Problemas de Valor Inicial - IVP

Un ejemplo de IVP clásico es el siguiente: $y'(t) = y(t)$ con $y(0) = 1$ para $t \in [0,T]$. Básicamente nos están preguntando si es que existe alguna función tal que su derivada sea la misma que que la función como tal. Si bien la solución a este problema puede parecer trivial, el punto aquí es en destacar las componentes del problema:
- Tenemos una ODE (*Ordinary Differential Equation*): $y'(t) = y(t)$
- Tenemos una condición inicial: $y(0) = 1$
- Y finalmente tenemos un intervalo para el cual se quiere resolver nuestra ODE: $t \in [0,T]$

La ODE es la que nos define cual es la ecuación que la función $y(t)$ debe satisfacer. Por ejemplo, la solución al problema anterior es $y(t) = \exp(t)$, ya que al evaluar $y(0)$ efectivamente obtenemos el valor 1, se cumple que su derivada es la misma que su función original y además es una función diferenciable para todo el intervalo $[0,T]$, por lo que debido a que se cumplieron las 3 soluciones anteriores sabemos que esta solución es correcta. Para este caso particular ha sido posible resolver el problema de forma algebraica y explícita, sin embargo, existen problemas para los cuales no se puede obtener una solución de esta forma, por lo que debemos recurrir a métodos de aproximación numérica que nos permitan encontrar nuestra función incógnita.

La forma general de un IVP con la que vamos a trabajar en este curso es la siguiente:
$$\begin{aligned}
	\dot{y} &= f(t, y(t)) \\
	y(0) &= y_0 \\
	t &\in [0,T] 
\end{aligned}$$
donde $\dot{y}$ representa la derivada de la función $y(t)$ con respecto a $t$, en caso de que aparezcan 2 puntos ($\ddot{y}$) entonces corresponde a la segunda derivada con respecto a $t$. $f(\cdot, \cdot)$ es una función de 2 variables que recibe como primer argumento la variable $t$ y como segundo argumento la función $y(t)$. Ocupando el problema dado de ejemplo a principios de este tema, donde la ODE corresponde a $\dot{y} = y$, utilizando la notación de IVP la función $f(t,y(t))$ corresponde a $f(t,y(t)) = y(t)$, es decir, solo dependía del segundo argumento. $y_0$ es la condición entregada, el cual para el ejemplo del problema este corresponde a 1. Por último, $T$ es el tiempo máximo donde uno quiere resolver la ODE.

Los IVP pueden clasificarse en 2 categorías:
- Sistemas No-Autónomos: $\dot{y} = f(t,y)$, es decir, la función $f$ depende explícitamente de $t$.
- Sistemas Autónomos: $\dot{y} = f(y)$, es decir, la función $f$ solo depende del segundo argumento $y(t)$.

Un ejemplo de sistema no-autónomo es el siguiente:
$$\begin{aligned}
	\dot{y} &= ty + t^3 \\
	y(0) &= 1 \\
	t &\in [0,1]
\end{aligned}$$
El cual posee solución conocida $y(t) = 3\exp{(t^2/2)} − t^2 − 2$, donde es posible notar que $f(t, y(t)) = ty + t^3 = \dot{y}$, lo que la hace no-autónoma. Un ejemplo de sistema autónomo es el siguiente:
$$\begin{aligned}
	\dot{y} &= cy(1 - y) \\
	y(0) &= y_0 \\
	t &\in [0,1]
\end{aligned}$$
El cual posee solución conocida:
$$y(t) =
\begin{cases}
	1, & \text{para } y_0 = 1 \\
	1 - \frac{1}{1 + \frac{y_0}{1 - y_0}\exp{(ct)}}, & \text{para } y_0 \neq 1
\end{cases}$$
el cual al ser $f(t, y(t)) = cy(1 - y) = \dot{y}$ es un sistema autónomo, ya que este no depende del valor de la variable $t$.

### Método de Euler

Ya hemos visto anteriormente la forma general de una IVP, y podemos empezar a trabajar con ella. tomando la expresión $\dot{y} = f(t, y(t))$ e integrándola entre $t = 0$ y $t = t_1$ obtenemos:
$$\int_0^{t_1} \dot{y}(s) \, ds = \int_0^{t_1} f(s, y(s)) \, ds$$
donde es posible notar que podemos aplicar el Teorema Fundamental del Cálculo en la parte izquierda, con lo que obtenemos:
$$y(t_1) - y(0) = \int_0^{t_1} f(s, y(s)) \, ds$$
Despejando $y(t_1)$ al lado izquierdo y utilizando la condición inicial $y(0) = y_0$ obtenemos:

$$y(t_1) = y_0 + \int_0^{t_1} f(s, y(s)) \, ds \tag{1}$$ ^67c7d8

Finalmente nos es posible aplicar lo que aprendimos en la sección de [[10- Integración Numérica|integración numérica]] para poder despejar finalmente el valor de la integral de la derecha para obtener el valor de $y(t_1)$. Ahora, antes de aplicar cualquier algoritmo es necesario preguntarnos sobre si es realmente necesario hacer esto, por ejemplo, ¿Es realmente necesario aplicar un algoritmo numérico si nosotros conocemos $f(t, y(t))$? Por supuesto, la respuesta a esta pregunta depende mucho del contexto, lo único que sabemos es la expresión de $f(t, y(t))$ y que $y(0) = y_0$, pero desconocemos son los valores de $y(t)$ para $t = [0,t_1]$.

Ahora, si nosotros decidiéramos utilizar un algoritmo numérico para resolverlo, ¿Cuál seria el mejor algoritmo a usar para obtener la mejor aproximación de la integral $\int_0^{t_1} g(s) \,ds$? La respuesta nuevamente es DEPENDE. Apliquemos los algoritmo numéricos que hemos aprendido anteriormente a la integral en cuestión:

- **Suma de Riemann por la izquierda**: $\int_{0}^{t_1} g(s) \, ds \approx g(0) \, (t_1 - 0) = f(0, y(0)) \, t_1 = f(0, y_0) \, t_1.$

- **Suma de Riemann por la derecha**: $\int_{0}^{t_1} g(s) \, ds \approx g(t_1) \, (t_1 - 0) = f(t_1, y(t_1)) \, t_1.$

- **Regla del punto medio**: $\int_{0}^{t_1} g(s) \, ds \approx g \left( \frac{t_1 + 0}{2} \right) (t_1 - 0) = f \left( \frac{t_1}{2}, y\frac{t_1}{2} \right) t_1.$

- **Regla del trapecio**: $\int_{0}^{t_1} g(s) \, ds \approx \left( g(0) + g(t_1) \right) \frac{(t_1 - 0)}{2} = \frac{f(0, y_0) + f(t_1, y(t_1))}{2} \, t_1.$

- **Regla del Simpson**: $\int_{0}^{t_1} g(s) \, ds \approx \left( g(0) + 4g \left( \frac{t_1}{2} \right) + g(t_1) \right) \, \frac{(t_1 - 0)/2}{3} = \left( f(0, y_0) + 4 f \left( \frac{t_1}{2}, y\frac{t_1}{2} \right) + f(t_1, y(t_1)) \right) \, \frac{t_1}{3}.$

- **Cuadratura Gaussiana**: $\int_{0}^{t_1} g(s) \, ds \approx \sum_{i=1}^{n} \hat{w}_i g(\hat{x}_i) = \sum_{i=1}^{n} \hat{w}_i f(\hat{x}_i, y(\hat{x}_i)).$

Para poder decidir que algoritmo nos conviene usar, tenemos que observar el término que se encuentra a la derecha del último signo igual de cada expresión. Esto en general depende de $y(t)$ evaluado en diversos tiempos, es decir, necesitamos los valores de $\{y(0), y(t_{\frac{1}{2}}), y(t_1)\}$ y para todos los $\hat{x}_i$ de la cuadratura Gaussiana. Sin embargo, solo conocemos $y(0) = y_0$. Por lo tanto solo podemos aplicar el algoritmo de la [[10- Integración Numérica#Suma de Riemann|suma de Riemann]] por la izquierda, por ahora...

#### Forward Euler
Ya que hemos decidido usar la suma de Riemann para resolver la integral en la [[11- Ecuaciones Diferenciales Ordinarias#^67c7d8|ecuación 1]], podemos expresar la aproximación del valor de $y(t_1)$ de la siguiente forma:
$$y(t_1) = y_0 + \int_0^{t_1} f(s, y(s)) \, ds \approx y_0 + f(0, y_0)t_1,$$
el cual podemos obtener formalmente la aproximación de $y(t_1)$, la cual llamaremos $y_1$:
$$y_1 = y_0 + f(0,y_0)t_1$$
De modo general obtenemos:
$$y_{i+1} = y_i + f(t_i,y_i)(t_{i+1} - t_i)$$
esto para los valores de $i \in \{0,1,2,\cdots\}$, donde recordemos que $y_0$ es conocido. Este algoritmo corresponde al método de Euler (o en esta versión, Forward Euler).
El código del algoritmo es el siguiente:

```python
def eulerMethod(t0, T, N, y0, f): 
	t = np.linspace(t0 , T, N+1) 
	h = (T − t0) / N 
	y = np.zeros(N + 1) 
	y[0] = y0 
	for i in np.arange(N): 
		y[i+1] = y[i] + f(t[i],y[i]) * h 
	return t, y
```

Donde las variables de entrada son las siguientes:
- $t_0$: Tiempo de la condición inicial $y(t_0) = y_0$.
- $T$: Tiempo final del intervalo a obtener la aproximación numérica, es decir, $t = [t_0, T]$, lo que implica que $T > t_0$.
- $N$: Número de puntos de la discretización temporal (básicamente, son la cantidad de puntos correspondientes a las particiones de la [[10- Integración Numérica#Suma de Riemann|suma de Riemann]]). El número de puntos totales al final será de $N + 1$, ya que también se incluye la condición inicial como un punto adicional. Es por esto que al final se considera $h = \frac{T - t_0}{N}$.
- $y_0$: Es nuestra condición inicial $y(t_0) = y_0$.
- $f$: Es la función $f(t,y)$ definida en el IVP $\dot{y} = f(t,y)$.

La salida de este algoritmo corresponden a los vectores $t$ y $y$ de dimensiones $N + 1$, los cuales nos entregan información sobres las coordenadas $(t_i,y_i)$ por el que pasa la función. Más adelante aprenderemos formas de resolver numéricamente las ODEs y IVPs de orden superior, mejor conocidas como Sistemas Dinámicos.

![[Apuntes_INF-285_2024-v0613.pdf#page=189&rect=132,215,471,401|Apuntes_INF-285_2024-v0613, p.188]]

#### Backward Euler
En el método de Forward Euler nosotros obtuvimos la siguiente aproximación para el valor de 
$y(t_1)$:
$$y(t_1) = y_0 + \int_0^{t_1} f(s, y(s)) \, ds \approx y_0 + f(0, y_0)t_1,$$
Ahora, si nosotros intentamos aproximar este valor usando [[10- Integración Numérica#Suma de Riemann|sumas de Riemann]] por la derecha en vez de por la izquierda obtenemos la siguiente aproximación:
$$y(t_1) = y_0 + \int_0^{t_1} f(s, y(s)) \, ds \approx y_0 + f(t_1, y(t_1))t_1,$$
Si intentamos obtener una ecuación para $y_1$ al igual que en el algoritmo anterior obtenemos la siguiente expresión:
$$y_1 = y_0 + f(t_1, y_1)t_1$$
Sin embargo, en esta expresión aparece el término de $y_1$ en ambos lados de la ecuación, lo que nos lleva a plantear el siguiente problema, ¿Cómo podemos despejar el valor de $y_1$? podemos intentar llevar los término dependientes de $y_1$ a un lado de la ecuación:
$$y_1 - f(t_1, y_1)t_1 = y_0$$
Aunque todavía no se ve una forma clara de despejar esta incógnita. Intentemos ahora llevar todos los términos al lado izquierdo de la ecuación:
$$y_1 - f(t_1, y_1)t_1 - y_0 = 0$$
Debido a que $t_1$, $y_0$ y $f(t,y)$ son valores conocidos, podemos denotar este lado izquierdo como una función de $y_1$, es decir:
$$\hat{f}(y_1) = y_1 - f(t_1, y_1)t_1 - y_0 = 0$$
Si se fijan bien, el problema se acaba de transformar en uno de búsqueda de ceros, por lo que nosotros podemos aplicar algún algoritmo aprendido de [[3- Raíces en 1D (Parte 1)|raíces en 1D]] para poder resolver este problema. De modo general, debemos resolver este problema de búsqueda de ceros para cada iteración o paso de tiempo:
$$\hat{f}_i(y_{i+1}) = y_{i+1} - y_i - f(t_{i+1}, y_{i+1})(t_{i+1} - t_i) = 0$$
para $i \in \{0,1,2,\cdots,N-1\}$. Este algoritmo corresponde al Método de Backward Euler, y su código es el siguiente:

```python
def backwardEulerMethod(t0 ,T, N, y0, f): 
	t = np.linspace(t0 , T, N+1) 
	h = (T − t0) / N 
	y = np.zeros(N+1) 
	y[0] = y0 
	for i in np.arange(N): 
		f_hat= lambda x: x − y[i] − f(t[i+1],x) * h 
		# La función "find_root" corresponde al algoritmo de raíces que nosotros escogimos. Los inputs usados son la función anónima "f_hat" y el initial guess y_i. 
		x = find_root(f_hat ,y[i]) 
		y[i+1] = x 
	return t, y
```

## RK2: Runge-Kutta de Segundo Orden 

Anteriormente les había mencionado que solamente parecía posible despejar el valor de $y(t_1)$ de la [[11- Ecuaciones Diferenciales Ordinarias#^67c7d8|ecuación 1]], y habíamos notado que solamente era posible usar [[10- Integración Numérica#Suma de Riemann|sumas de Riemann]] para poder despejarlo, o al menos eso es así si es que no trabajamos más con la ecuación. RK2 usa específicamente el [[10- Integración Numérica#Regla del Punto Medio|método del punto medio]] para poder hacer el despeje, y a continuación les explicaré como es que lo logra. 

Aproximando el valor de $y(t_1)$ con el del método del punto medio obtenemos:
$$y(t_1) = y_0 + \int_0^{t_1} f(s, y(s)) \, ds \tag{1} \approx y_0 + f(\frac{t_1}{2}, y\frac{t_1}{2})(t_1-0)$$
donde anteriormente habíamos visto que esto no era una solución factible debido a que $y(\frac{t_1}{2})$  todavía sigue siendo un valor que desconocemos, por lo tanto, nosotros podemos estimar este valor con el [[11- Ecuaciones Diferenciales Ordinarias#Método de Euler|método de Euler]], de esta forma nosotros obtendremos $k = y_0 + \frac{t_1}{2}f(0, y_0)$, por lo que obtendremos el siguiente algoritmo para el método de Runge-Kutta de Segundo Orden:
$$\begin{aligned}
	k_1 &= f(t_i,y_i) \\
	y_{i+1} &= y_i + hf\left( t_i + \frac{h}{2}, y_i + \frac{h}{2}k_1 \right)
\end{aligned}$$
Lo que se traduce en el siguiente código de Python:

```python
def RK2(t0, T, N, y0, f): 
	t = np.linspace(t0, T, N+1) 
	h = (T − t0) / N 
	y = np.zeros(N+1) 
	y[0] = y0 
	for i in np.arange(N): 
		k1 = f(t[i],y[i]) 
		y[i+1] = y[i] + f(t[i] + h/2, y[i] + k1 * h/2) * h 
	return t, y
```

Se lo que mas de uno estará pensando, debido a que estamos calculando una aproximación numérica usando otro algoritmo de aproximación entonces, ¿no tendremos un error mayor de lo normal? y la realidad es que no, y de hecho, esto en parte va a nuestro favor. Resulta que este algoritmo es un método de orden 2, es decir, su error es de $\mathcal{O}(h^2)$, lo que significa que si reducimos $h$ por la mitad entonces el error se terminaría reduciendo 4 veces, por lo que podríamos llegar a una misma aproximación numérica sin usar un $h$ tan pequeño, aparte de que llegaríamos al resultado deseado en un menor tiempo de computación.

## RK4: Runge-Kutta de Cuarto Orden

Este algoritmo es el siguiente:
$$\begin{aligned}
	k_1 &= f(t_i, y_i) \\
	k_2 &= f\left( t_i + \frac{h}{2}, y_i + \frac{h}{2}k_1 \right) \\
	k_3 &= f\left( t_i + \frac{h}{2}, y_i + \frac{h}{2}k_2 \right) \\
	k_4 &= f(t_i + h, y_i + hk_3) \\
	y_{i+1} &= y_i + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}$$
(No me miren así, ni en el ppt ni en los apuntes oficiales sale la explicación de como se formó este algoritmo >:\[ ) El código del algoritmo es el siguiente:

```python
def RK4(t0, T, N, y0, f): 
	t = np.linspace(t0, T, N+1) 
	h = (T − t0) / N 
	y = np.zeros(N+1) 
	y[0] = y0 
	for i in np.arange(N): 
		k1 = f(t[i],y[i]) 
		k2 = f(t[i] + h/2, y[i] + k1 * h/2)
		k3 = f(t[i] + h/2, y[i] + k2 * h/2)
		k4 = f(t[i] + h, y[i] + k3 * h)
		y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) * h/6 
	return t, y
```

Con una explicación muy parecida a la de segundo orden, este algoritmo al ser de cuarto orden posee un error de $\mathcal{O}(h^4)$, por lo que si llegamos a reducir su $h$ por la mitad entonces estamos reduciendo su error unas 16 veces.

## Sistemas Dinámicos

Los sistemas dinámicos pueden interpretarse como una extensión de los IVP. Por ejemplo, consideremos el siguiente problema de valor inicial o IVP en 2 variables:
$$\begin{aligned}
	\dot{x} &= f_1(t, x, y) \\
	\dot{y} &= f_2(t, x, y) \\
	x(0) &= x_0 \\
	y(0) &= y_0
\end{aligned}$$
donde tanto $x(t)$ como $y(t)$ son funciones temporales (dependen del tiempo) y $f_1$ con $f_2$ son funciones de 3 variables. Para que nosotros seamos capaces de aplicar la teoría que hemos aprendido hasta ahora en este tema, es necesario reescribir el problema a su forma vectorial:
$$\begin{aligned}
	\dot{\bmf{y}} &= \bmf{F}(t, \bmf{y}) \\
	\bmf{y}(0) &= \bmf{y}_0
\end{aligned}$$
donde para este caso $\bmf{y}(t) = \left<x(t), y(t)\right>^T$, $\bmf{F}(t) = \left< f_1(t,\bmf{y}), f_2(t,\bmf{y})\right>^T$ y $\bmf{y}(0) = \left< x_0, y_0 \right>^T$. Entonces acabamos de crear un IVP vectorial el cual vamos a llamar Sistema Dinámico. 

Por completitud les presento el paso a paso de las versiones vectoriales de los algoritmos vistos anteriormente: ^7323b4

- **Método de Euler**:
$$\bmf{y}_{i+1} = \bmf{y}_i + \bmf{F}(t_i, \bmf{y}_i)h$$
- **Backward Euler** (recuerden que "findRoot" corresponde al algoritmo que uno decide usar para encontrar la raíz de $\bmf{y}_{i+1}$):
$$\begin{aligned}
	\bmf{G}(\bmf{x}) &= \bmf{x} - \bmf{y}_i - \bmf{F}(t_i, \bmf{x})h \\
	\bmf{y}_{i+1} &= \text{findRoot}(\bmf{G}(\bmf{x}), \bmf{y}_i)
\end{aligned}$$
- **RK2**:
$$\begin{aligned}
	\bmf{k}_1 &= \bmf{F}(t_i, \bmf{y}_i) \\
	\bmf{y}_{i+1} &= \bmf{y}_i + h\bmf{F}(t_i + \frac{h}{2}, \bmf{y}_i + \frac{h}{2}\bmf{k}_1)
\end{aligned}$$
- RK4:
$$\begin{aligned}
	\bmf{k}_1 &= \bmf{F}(t_i, \bmf{y}_i) \\
	\bmf{k}_2 &= \bmf{F}(t_i + \frac{h}{2}, \bmf{y}_i + \frac{h}{2}\bmf{k}_1) \\
	\bmf{k}_3 &= \bmf{F}(t_i + \frac{h}{2}, \bmf{y}_i + \frac{h}{2}\bmf{k}_2) \\
	\bmf{k}_4 &= \bmf{F}(t_i + h, y_i + hk_3) \\
	\bmf{y}_{i+1} &= \bmf{y}_i + \frac{h}{6}(\bmf{k}_1 + 2\bmf{k}_2 + 2\bmf{k}_3 + \bmf{k}_4)
\end{aligned}$$

Cabe destacar que estos sistemas funcionan para una cantidad indeterminada de dimensiones, o sea, pueden formarse Sistemas Dinámicos de $N$ dimensiones.

Para dar un ejemplo de Sistema Dinámico, tomemos un problema que nos va a devolver a los cursos de Física (buuuuuuuuu). Consideremos que tenemos un péndulo simple con pivote en un punto $\bmf{P}$ y con una barra rígida de largo $l$ con masa despreciable en comparación a la partícula de masa $m$ en el extremo opuesto al pivote. Considerando la segunda Ley de Newton obtenemos la siguiente ecuación del ángulo $\theta$ formado entre la vertical bajo el pivote y la barra rígida:
$$\begin{align}
	ml\ddot{\theta} &= -mg\sin(\theta) \tag{2} \\
	\theta(0) &= \theta_0 \\
	\dot{\theta}(0) &= \omega_0
\end{align}$$
donde $g$ corresponde a la aceleración de gravedad, $\theta_0$ es el ángulo inicial y $\omega_0$ es la velocidad angular inicial. Intentemos reescribir la ecuación 2 tratando de despejar $\ddot{\theta}$:

$$\ddot{\theta} = \frac{g}{l}\sin(\theta) \tag{3}$$ ^207df0

Esta ecuación todavía no posee la misma estructura de una IVP que necesitamos para empezar a ejecutar algún algoritmo visto en el curso, ni mucho menos el de un Sistema Dinámico, por lo tanto necesitamos re-rescribir nuestro sistema de ecuaciones. Hagamos el siguiente cambio de variable:
$$\begin{aligned}
	y_1(t) = \theta(t) \\
	y_2(t) = \dot{\theta}(t) \\
\end{aligned}$$
Derivando las ecuaciones con respecto a $t$ obtenemos:
$$\begin{aligned}
	\dot{y}_1(t) = \dot{\theta}(t) \\
	\dot{y}_2(t) = \ddot{\theta}(t) \\
\end{aligned}$$
donde si nos fijamos bien, el lado derecho de la primera ecuación posee la misma forma de la función $y_2(t)$ y la segunda ecuación corresponde a la misma expresión de la [[11- Ecuaciones Diferenciales Ordinarias#^207df0|ecuación 3]]. Realizando estos reemplazos en nuestro sistema de ecuaciones dejando todo en función de las variables $y_1(t)$ y $y_2(t)$ además de eliminar la dependencia de $t$ por mera simplicidad (o sea, esto último no es necesario hacerlo), nuestro sistema de ecuaciones queda de la siguiente forma:
$$\begin{aligned}
	\dot{y}_1 &= y_2 \\
	\dot{y}_2 &= -\frac{g}{l}\sin(y_1)
\end{aligned}$$
El cual ahora si que si posee la forma de un Sistema Dinámico, donde $\bmf{y} = \left< y_1(t), y_2(t) \right>^T$ y $\bmf{F}(t,\bmf{y}) = \left< \bmf{y}_2, -\frac{g}{l}\sin(\bmf{y}_1) \right>^T$, por lo que ahora basta con aplicar alguna de las [[11- Ecuaciones Diferenciales Ordinarias#^7323b4|formas matriciales]] de algoritmo que hemos visto en este tema para obtener las distintas posiciones del péndulo para algún segmento de tiempo $t$ dado. 