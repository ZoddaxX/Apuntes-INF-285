En este tema estudiaremos un tipo de problemas que no hemos abordado en este curso, y este corresponde a la resolución de sistemas de ecuaciones en las que existen más ecuaciones que incógnitas. La versión que resolveremos de este problema corresponde al de los mínimos cuadrados. A la hora de obtener los mínimos cuadrados de un sistema de ecuaciones vamos a aprender a realizar aproximaciones lineales sobre un conjunto de datos ($x_i$, $y_i$) para $i \in \{a,2,\cdots,n\}$. Antes de empezar con esto primero nos tenemos que hacer la pregunta, ¿Qué significa hacer una aproximación lineal?

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
\frac{\partial E}{\partial a} =&\ \frac{\partial}{\partial a} \sum_{i=1}^m (y_i - a - bx_i)^2 = \sum_{i=1}^m 2(y_i - a - bx_i)(-1) \\
\frac{\partial E}{\partial b} =&\ \frac{\partial}{\partial a} \sum_{i=1}^m (y_i - a - bx_i)^2 = \sum_{i=1}^m 2(y_i - a - bx_i)(-x_i)
\end{align}$$
