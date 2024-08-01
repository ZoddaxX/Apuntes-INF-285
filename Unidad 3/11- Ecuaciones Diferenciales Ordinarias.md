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