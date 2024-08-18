$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
Como ya he mencionado en el tema anterior, los problemas de valor frontera BVP se caracterizan ya que dependen de una variable espacial supongamos $x$ en vez de una variable temporal $t$. Un ejemplo de BVP es el siguiente: $y''(x) = 0$ para $x \in ]0,1[$ , $y(0) = c_1$ y $y(1) = c_2$. En pocas palabras, se nos acaba de preguntar si es que existe una función para cualquier $x \in ]0,1[$ tal que su segunda derivada sea 0 para cualquier $x$, donde al evaluar esta mismo en los puntos 0 y 1 obtengamos las constantes $c_1$ y $c_2$ respectivamente.
Estudiemos ahora las 3 componentes del problema anterior:
- Tenemos una ODE (*Ordinary Differential Equation*): $y''(x) = 0$.
- Tenemos una condición de borde: $y(0) = c_1$ y $y(1) = c_2$.
- Se tiene un intervalo espacial para el cual queremos obtener las soluciones de la ODE: $x \in ]0,1[$ .

Es fácil notar que una solución rápida al problema descrito anteriormente puede ser la función $y(x) = c_1 + (c_2 - c_1)x$. Al igual que con las [[11- Ecuaciones Diferenciales Ordinarias#Problemas de Valor Inicial - IVP|IVP]], todas las condiciones anteriores tienen que cumplirse para considerar una solución como válida.

Al tener condiciones de borde en vez de condiciones iniciales en las [[11- Ecuaciones Diferenciales Ordinarias#Problemas de Valor Inicial - IVP|IVP]], nos vemos obligados a tomar un enfoque distinto para poder resolver este tipo de problemas, y en este curso vamos a ver 2 métodos para lograrlo.

## Método del Disparo

Este método en resumidas cuentas transforma un problema de BVP en un problema de [[11- Ecuaciones Diferenciales Ordinarias#Problemas de Valor Inicial - IVP|IVP]]. Ahora, ¿Cómo es que lo logra? Repasemos algunas características que definen estos tipos de problemas:
- <u>IVP</u>: Una ODE, 1 condición inicial y el dominio o intervalo de tiempo.
- <u>BVP</u>: Una ODE, 2 condiciones de borde y el dominio o intervalo espacial.

Como era de esperarse, la única diferencia evidente corresponde a las condiciones que nos dan para resolver los problemas. Consideremos ahora el mismo [[11- Ecuaciones Diferenciales Ordinarias#Problemas de Valor Inicial - IVP|IVP]] presentado anteriormente, $y''(x) = 0$ para $x \in ]0,1[$ , $y(0) = c_1$ y $y(1) = c_2$. Ahora, realicemos la interpretación $x \rightarrow t$, con esto podemos obtener el [[11- Ecuaciones Diferenciales Ordinarias#Problemas de Valor Inicial - IVP|IVP]] renombrando la condición de borde $y(0) = c_1$ como condición inicial y agregando la condición inicial para la derivada, es decir:
$$\begin{aligned}
	y''(y) &= 0 \\
	y(0) &= c_1 \\
	y'(0) &= \alpha
\end{aligned}$$
Este problema en realidad se acaba de transformar en un [[11- Ecuaciones Diferenciales Ordinarias#Sistemas Dinámicos|sistema dinámico]], sin embargo, todavía queda por ver que hacemos con la condición $y(1) = c_2$ y que es exactamente el valor de $\alpha$. Continuemos desarrollando la ODE de segundo orden en el sistema dinámico:
$$\begin{aligned}
	\dot{y}_1    &= y_2 \\
	\dot{y}_2(t) &= 0   \\
	y_1(0)       &= 0 \\
	y_2(0)       &= \alpha 
\end{aligned}$$
Con esto nosotros podemos ver que se introduce el valor de $\alpha$ (el cual nos es desconocido) con el fin de poder obtener toda la data necesaria para el tiempo en $t = 0$. En este punto, nosotros somos capaces de aplicar cualquier [[11- Ecuaciones Diferenciales Ordinarias|solver de problemas de IVP]] que nosotros hayamos aprendido para solucionar el problema, aunque todavía tenemos que considerar algunos detalles más. Supongamos que ahora queremos utilizar algún solver para resolver este sistema dinámico en su forma general utilizando $\alpha = 0$, entonces tendremos una versión discreta de $y_1(t)$ para este valor de $\alpha$:
$$\left\{ y_{1,0}^{|0|},\ y_{1,1}^{|0|},\ y_{1,2}^{|0|},\cdots,\ y_{1,N-1}^{|0|},\ y_{1,N}^{|0|} \right\}$$
Después de resolver el problema, obtendremos una aproximación numérica con la cual podemos extraer el valor de $y_{1,N}^{|0|}$, el cual es una aproximación de $y_1(1)$, por lo que fácilmente podemos comprobar si se cumple la condición $y(1) = c_2$. Sin embargo, es evidente que muchas de las soluciones de este tipo de [[11- Ecuaciones Diferenciales Ordinarias#Sistemas Dinámicos|sistemas dinámicos]] no va a ser con $\alpha = 0$, por lo que tendremos que ir ajustando este valor hasta obtener el valor que nosotros deseamos con un nuevo $\alpha = \alpha_1$:
$$\left\{ y_{1,0}^{|\alpha_1|},\ y_{1,1}^{|\alpha_1|},\ y_{1,2}^{|\alpha_1|},\cdots,\ y_{1,N-1}^{|\alpha_1|},\ y_{1,N}^{|\alpha_1|} \right\}$$
En un principio esto nos puede dar a entender de que este sub-problema se ha transformado en uno de búsqueda de raíces, el cual sabemos resolver gracias a lo visto en el [[3- Raíces en 1D (Parte 1)|tema 3]] y [[4- Raíces en 1D (Parte 2)|tema 4]]. La siguiente función a mostrar nos permite obtener el valor de $y_{N,0} - c_1$ dado un valor de $\alpha$ que nos permitirá decidir si el valor de alpha introducido es lo suficientemente cercano o no:

```python
# Consideraremos a los valores de "c1" y "c2" como conocidos. 
def ErrorSecondBoundaryCondition(alpha,N =1000): 
	y0 = np.zeros(2) 
	y0[0] = c1 
	y0[1] = alpha 
	def f_IVP(t, y): 
		y1,y2 = y 
		dydt = [y2,0] 
		return dydt 
	# Consideraremos que las dimensiones de la variable de salida serán de (N+1) x 2 
	y = SolverIVP(0,1,N,y0,f_IVP)
	return y[-1,0] - c2
```

Remarcando que el código anterior no corresponde a la solución completa del sistema dinámico, este se encarga de decirnos que tan bueno es el valor de $\alpha$ ingresado para poder obtener la solución final del sistema dinámico. SolverIVP en este caso corresponde a algún solver que resuelva la última ecuación mencionada, los cuales se encuentran en el [[11- Ecuaciones Diferenciales Ordinarias|tema 11]]. Con esto y con ayuda de algún algoritmo de búsqueda de raíces (puede ser más adecuado utilizar el [[3- Raíces en 1D (Parte 1)#Método de la Bisección|método de la bisección]]) nosotros tenemos que llegar a algún $\alpha$ tal que la función *ErrorSecondBoundaryCondition* devuelva un valor lo suficientemente cercano a 0.

## Diferencias Finitas para ODE

Si en algún momento se preguntaron si era posible aproximar numéricamente los valores de las derivadas de ciertas funciones, la respuesta es un rotundo SI. Justamente este método busca aproximar los valores de las derivadas presentes en un problema de valor frontera con el fin de armar un algoritmo con el que podamos obtener una solución óptima para nuestro problema.

Recordemos primero la definición de la primera derivada de una función:
$$y'(x) = \lim\limits_{h\to0} \frac{y(x+h) - y(x)}{h}$$
Ahora, nosotros estamos trabajando en una cierta frontera para la cual nosotros queremos obtener la aproximación de $y'(x)$ sobre un conjunto discreto de estos bordes, por lo que vamos a utilizar el siguiente conjunto de pares ordenados para intentar lograrlo:
$$\left\{ (x_0,y_0), (x_1,y_1), (x_2,y_2), \cdots, (x_N,y_N) \right\},$$
donde $y_i$ representa la aproximación desconocida de $y(x_i)$ para $x_i = ih$, con $i \in \{0,1,2,\cdots,N\}$ y $h = \frac{b-a}{N}$. Vamos a considerar que estamos discretizando el dominio $\Omega = [a,b]$, donde $x \in \Omega$. Para el problema mencionado anteriormente recordemos que las condiciones de frontera dada nos dan los valores $a = 0$ y $b = 1$.

Ahora que poseemos este conjunto de pares ordenados, vamos a definir una formula para poder finalmente aproximar el valor de la derivada requerida:
$$y'(x) = \lim\limits_{h\to0} \frac{y(x_i+h) - y(x_i)}{h} = \lim\limits_{h\to0} \frac{y(x_{i+1}) - y(x_i)}{h} \approx \frac{y_{i+1} - y_i}{h}$$
Esta aproximación se le conoce como *Forward Difference*. De esta forma podemos obtener otras 2 aproximaciones adicionales con el orden de aproximación de cada una:
$$\begin{aligned}
	y'(x) = \lim\limits_{h\to0} \frac{y(x_i+h) - y(x_i)}{h} + \mathcal{O}(h) &\approx \frac{y_{i+1} - y_i}{h}, \bm{\text{Forward Difference}} \\
	y'(x) = \lim\limits_{h\to0} \frac{y(x_i) - y(x_i-h)}{h} + \mathcal{O}(h) &\approx \frac{y_i - y_{i+1}}{h}, \bm{\text{Backward Difference}} \\
	y'(x) = \lim\limits_{h\to0} \frac{y(x_i+h) - y(x_i-h)}{2h} + \mathcal{O}(h^2) &\approx \frac{y_{i+1} - y_{i-1}}{2h}, \bm{\text{Backward Difference}}
\end{aligned}$$
Con estas nuevas definiciones, finalmente podemos generar una expresión para la segunda derivada de $y$:
$$\begin{aligned}
	y''(x_i) &= \frac{\bm{\text{Forward Difference}} - \bm{\text{Backward Difference}}}{h} + \mathcal{O}(h^2) \\ 
	&= \frac{\frac{y(x_i+h) - y(x_i)}{h} - \frac{y(x_i) - y(x_i-h)}{h}}{h} + \mathcal{O}(h^2) \\
	&= \frac{y(x_i+h) - 2y(x_i) - y(x_i-h)}{h^2} + \mathcal{O}(h^2) \\
	&\approx \frac{y_{i+1} - 2y_i - y_{i-1}}{h^2}
\end{aligned}$$
Para explicar como vamos a aplicar esto en la resolución de algún BVP, tomemos como ejemplo el problema de valor frontera que di al inicio de este tema, es decir: $y''(x) = 0$ para $x \in ]0,1[$ , $y(0) = c_1$ y $y(1) = c_2$. Por como definimos anteriormente anteriormente las aproximaciones a las derivadas de $y(x)$, necesitamos definir un conjunto de pares $(x_i,y_i)$ donde realizar nuestra discretización, por simplicidad usaremos 5 puntos:
$$\left\{ (x_0,y_0), (x_1,y_1), (x_2,y_2), (x_3,y_3), (x_4,y_4) \right\}$$
A partir de estos puntos nosotros conocemos que $x_i = ih$, $h = \frac{1-0}{4} = \frac{1}{4}$ e $i \in \{0,1,2,3,4\}$, donde gracias a las condiciones de borde obtenemos además que $y_0 = c_1$ y $y_4 = c_2$. Con esto solamente nos queda por despejar 3 incógnitas: $y_1$, $y_2$ y $y_3$. Estos valores es posible obtenerlos a partir de la discretización de la ODE dada en el problema, la cual corresponde en este caso a $y''(x) = 0$, por lo que necesitamos aproximar el valor de $y''(x) = 0$ en los puntos $x_1$, $x_2$ y $x_3$:
$$\begin{aligned}
	x = x_1,\ y''(x_1) = 0 \implies \frac{y_2 - 2y_1 + y_0}{h^2} = 0 \\
	x = x_2,\ y''(x_2) = 0 \implies \frac{y_3 - 2y_2 + y_1}{h^2} = 0 \\
	x = x_3,\ y''(x_3) = 0 \implies \frac{y_4 - 2y_3 + y_2}{h^2} = 0 \\ 
\end{aligned}$$
Reemplazando los valores conocidos $y_0$ y $y_4$ dentro de estas ecuaciones y moviéndolos al lado derecho de las ecuaciones, podemos formar el siguiente sistema de ecuaciones solucionable:
$$\begin{aligned}
	y_2 - 2y_1       &= -c_1 \\
	y_3 - 2y_2 + y_1 &= 0 \\
	-2y_3 + y_2      &= -c_2
\end{aligned}$$
El cual escrito de manera matricial queda:
$$\begin{bmatrix}
	-2 & 1  & 0  \\
	1  & -2 & 1  \\
	0  & 1  & -2 
\end{bmatrix}
\begin{bmatrix}
	y_1 \\
	y_2 \\
	y_3
\end{bmatrix}
=
\begin{bmatrix}
-c_1 \\
0 \\
-c_2
\end{bmatrix}$$
Sistema que nosotros podemos resolver con lo aprendido en el [[5- Sistemas de Ecuaciones Lineales|tema 5]] y [[9- GMRes|tema 9]].


