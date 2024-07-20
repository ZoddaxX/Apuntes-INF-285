---
cssclasses:
  - t-c
---

## Método o Iteración de Punto Fijo

Este método es uno de los más directos y a la vez versátiles a la hora de encontrar **puntos fijos** para una función (no confundir con una [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]]), los cuales podremos usar para encontrar efectivamente las raíces que uno necesita obtener.

Introduzcamos primero el **teorema de los límites continuos**: *Sea $f$ una función continua en un vecindario de $x_0$, y suponga que $\lim\limits_{n \to \infty} x_n=x_0$. Entonces:*
$$\lim\limits_{n \to \infty} f(x_n) = f\left(\lim\limits_{n \to \infty} x_n\right) = x_0$$
Esto significa que los límites pueden trasladarse al interior de funciones que sean continuas sin alterar el resultado. ^71d850

Este teorema es el que se aprovecha con este algoritmo para obtener el punto fijo de una función $g(x)$. Consideremos que poseemos una secuencia $x_i$ la cual puede o no converger a medida que esta secuencia se acerca al infinito, donde en caso de que $g(x)$ sea continua y la serie $x_i$ converja en un punto $r$, entonces podemos llamar a $r$ un punto fijo de $g$. Entonces, si conocemos $g(x)$, que $\lim\limits_{i\to\infty}x_i = r$ y haciendo uso del [[4- Raíces en 1D (Parte 2)#^71d850|teorema de los límites continuos]] tenemos:
$$g(r) = g\left(\lim\limits_{i\to\infty}x_i\right) = \lim\limits_{i\to\infty}g(x_i) = \lim\limits_{i\to\infty}x_i+1 = r$$
Es decir, se cumple que $g(r) = r$, lo que corresponde a la definición de punto fijo. ^8e518c

Ahora, ya mencioné anteriormente que un punto fijo no es lo mismo que una [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]], por lo que se estarán preguntando de qué nos sirve entonces saber esto para obtener las raíces de una función $f(x)$, y la respuesta es bastante sencilla, basta con obtener una función $g(x)$ derivable de $f(x)$ la cual nosotros sepamos que su punto fijo es una raíz de $f(x)$. 

Voy a ejemplificar el como podemos obtener la función $g(x)$ para el caso $f(x) = x^3 + x - 1$. La cosa es que para este caso no existe una única función $g(x)$ tal que su punto fijo $r$ sea una raíz de $f(x)$, solamente que algunas funciones convergerán más rápidamente que otras al resultado que nosotros esperamos. 3 formas de obtener un $g(x)$ para este caso son:

- Despejando $x$ del segundo término de $f(x)$:
$$x = 1 - x^3 = g_1(x)$$
- Despejando $x$ del término cúbico de $f(x)$ obtenemos:
$$x = \sqrt[3]{1-x} = g_2(x)$$
- Si uno se siente gracioso también lo puede hacer de la siguiente forma:
$$\begin{align}
x^3 + x - 1 &= 0 & / &+ 1\\
x^3 + x &= 1 & / &+ 2x^3\\
3x^3 + x &= 2x^3 + 1 \\
x(3x^2 + 1) &= 2x^3 + 1 \\
x &= \frac{2x^3 + 1}{3x^2+1} = g_3(x)
\end{align}$$

Ahora que ya hablé de las bases necesarias para emplear este algoritmo puedo explicarles sobre su funcionamiento práctico. Básicamente vamos a empezar desde un "supuesto inicial" o *initial guess* el cual vamos a ir evaluando dentro de $g(x)$ para empezar a iterar sobre la serie $x_i$ con la que vamos a obtener en algún momento nuestro punto fijo $r$, [[4- Raíces en 1D (Parte 2)#^8e518c|tal como habíamos mencionado anteriormente]]:
$$\begin{align}
i=0:\ &x_0 = \text{"initial guess"}\\
i=1:\ &x_1 = g(x_0) \\
i=2:\ &x_2 = g(x_1) \\
\vdots \\
i=n:\ &x_n = g(x_{n-1})
\end{align}$$
Por lo tanto, nuestro algoritmo podría verse de la siguiente manera:

```markdown
x_0 = "Initial Guess"
for i in range(1, n):
    x_i = g(x_{i-1})
```

Como pequeño ejercicio para poder visualizar mejor el algoritmo, pueden tomar su calculadora científica de preferencia (o de forma mucho más práctica, Python), elegir un número real cualquiera y a este valor aplicarle la función $\cos$, luego al resultado volver a aplicarle la función $\cos$ y así hasta que vean que el resultado empieza a variar casi nada, momento en el que el número debiera ser de aproximadamente $0.73908513321516$.

### Diagrama de Cobweb
Anteriormente hablé de casos en el que las series $x_i$ terminaban convergiendo al tender a infinito, pero, ¿Qué pasa entonces cuando esto no es así?
Tomemos la siguiente función $g(x)$:
$$g_1(x) = -\frac{3}{2}x + \frac{5}{2}$$
Definamos nuestro *initial guess* $x_0$ como 1.1, haciendo unas 20 iteraciones nosotros obtenemos los siguientes resultados:
$$ \begin{array}{lll} 
x_0 = 1.1 & x_7 = g_1(x_6) = -0.708594 & x_{14} = g_1(x_{13}) = 30.1929 \\ 
x_1 = g_1(x_0) = 0.85 & x_8 = g_1(x_7) = 3.56289 & x_{15} = g_1(x_{14}) = -42.7894 \\ 
x_2 = g_1(x_1) = 1.225 & x_9 = g_1(x_8) = -2.84434 & x_{16} = g_1(x_{15}) = 66.6841 \\ 
x_3 = g_1(x_2) = 0.6625 & x_{10} = g_1(x_9) = 6.7665 & x_{17} = g_1(x_{16}) = -97.5261 \\ 
x_4 = g_1(x_3) = 1.50625 & x_{11} = g_1(x_{10}) = -7.64976 & x_{18} = g_1(x_{17}) = 148.789 \\ 
x_5 = g_1(x_4) = 0.240625 & x_{12} = g_1(x_{11}) = 13.9746 & x_{19} = g_1(x_{18}) = -220.684 \\ 
x_6 = g_1(x_5) = 2.13906 & x_{13} = g_1(x_{12}) = -18.462 & x_{20} = g_1(x_{19}) = 333.526 \end{array} $$
Es evidente que los valores de nuestra serie están divergiendo, y una interesante forma de visualizarlo es mediante un diagrama de Cobweb, el cual es un gráfico que grafica la evolución de los valores $x_i$ obtenidos en un plano cartesiano y los va uniendo en cada iteración $i$, de modo que se va dibujando una línea entre las coordenadas ($x_i$, $x_{i+1} = g(x_i)$) y ($x_{i+1}$, $x_{i+1}$), y entre ($x_{i+1}$, $x_{i+1}$) y ($x_{i+1}$, $x_{i+2} = g(x_{i+1})$). Para las 6 primeras iteraciones de este ejemplo tenemos que nuestro diagrama de Cobweb se ve de esta forma:

![[CobWeb_1.png]] 

Y como se puede apreciar gracias a las pequeñas flechas de las esquinas del gráfico, efectivamente los valores están divergiendo de algún punto que buscamos.

De paso les he adjuntado un código de Python para que puedan graficar las $g(x)$ con las $n$ iteraciones que gusten en la carpeta de código útil adjunto con este vault. 

Visualicemos ahora un diagrama para una $g(x)$ que efectivamente converja. Tomemos:
$$g(x) = -\frac{1}{2}x + \frac{3}{2}$$
Definamos nuestro *initial guess* $x_0$ como 2.7, haciendo unas 20 iteraciones nosotros obtenemos los siguientes resultados:
$$ \begin{array}{lll} 
x_0 = 2.7 & x_7 = g_1(x_6) = 0.986719 & x_{14} = g_1(x_{13}) = 1.0001 \\ 
x_1 = g_1(x_0) = 0.15 & x_8 = g_1(x_7) = 1.00664 & x_{15} = g_1(x_{14}) =  0.999948 \\ 
x_2 = g_1(x_1) = 1.425 & x_9 = g_1(x_8) = 0.99668 & x_{16} = g_1(x_{15}) = 1.00003 \\ 
x_3 = g_1(x_2) = 0.7875 & x_{10} = g_1(x_9) = 1.00166 & x_{17} = g_1(x_{16}) = 0.999987 \\ 
x_4 = g_1(x_3) = 1.10625 & x_{11} = g_1(x_{10}) = 0.99917 & x_{18} = g_1(x_{17}) = 1.00001 \\ 
x_5 = g_1(x_4) = 0.946875 & x_{12} = g_1(x_{11}) = 1.00042 & x_{19} = g_1(x_{18}) = 0.999997\\ 
x_6 = g_1(x_5) = 1.02656 & x_{13} = g_1(x_{12}) = 0.999792 & x_{20} = g_1(x_{19}) = 1.0000 \end{array} $$
Es evidente que en este caso hay una clara convergencia hacia 1. Para las primeras 6 iteraciones de este caso nuestro diagrama se ve así:

![[CobWeb_2.png]]

Si se fijan bien en la imagen, es posible interpretar de aquí que la búsqueda de raíces no es mas que buscar la intersección entre una recta y una función que no necesariamente va a ser lineal! (al menos si lo vemos desde el punto de vista de la iteración de punto fijo, recordemos que en la práctica para este algoritmo estamos buscando un punto fijo para nuestra función $g(x)$) ^446a3c
### Convergencia Lineal de Iteración de Punto Fijo
Para poder analizar la convergencia de una iteración de punto fijo, es necesario introducir el **Teorema del valor medio**: *Sea $f$ una función continua en el intervalo \[$a$, $b$] y diferenciable en el intervalo ]$a$, $b$\[. Entonces existe un número $c$ entre $a$ y $b$ tal que:* 
$$f'(c) = \frac{f(b) - f(a)}{b-a}$$ ^63be27

Ahora es necesario definir la **convergencia lineal** de forma matemática: *Sea $e_i = |x_i - r|$ el error absoluto del paso $i$ de un método iterativo. Si se cumple:*
$$\lim\limits_{i\to\infty}\frac{e_{i+1}}{e_i} = S < 1$$
*Se dice entonces que el método obedece "convergencia lineal" con tasa S*. ^f07d7d

Finalmente, gracias a este teorema, definición y [[Apuntes_INF-285_2024-v0613.pdf#search=Demostración. Sea xi el i -ésimo termino de la iteración|esta demostración]] podemos concluir lo siguiente con respecto a este algoritmo que si asumimos que hay una función $g(x)$ que nosotros hayamos encontrado y que sea continua y diferenciable, que tiene un punto fijo $g(r) = r$ y que además $S = |g´(r)| < 1$, entonces la iteración de punto fijo converge linealmente con tasa $S$ al punto fijo $r$ para ciertos *"initial guesses"* que estén lo suficientemente cerca de r. Es decir, para que el algoritmo funcione lo suficientemente bien, y si es que la serie $x_i$ no termina divergiendo, entonces necesitaríamos estimar un *initial guess* adecuado para que el algoritmo otorgue resultados positivos.

## Teoremas y Definiciones Útiles

En esta sección se van a mencionar algunos teoremas que se van a usar en algunos puntos en el futuro.

Primero partiré definiendo de manera más precisa el concepto de convergencia local el cual ya me he referido anteriormente. *Un método iterativo es llamado localmente convergente a $r$ si el método converge a $r$ para "initial guesses" lo suficientemente cercanos a $r$*. Esta definición nos dice que de existir una vecindad ($r - \epsilon$, $r + \epsilon$) para $\epsilon > 0$ de tal forma que al escoger algún "*initial guess*" o $x_0$ que pertenezca a esta misma vecindad se genere una convergencia, entonces decimos que ese método converge localmente hacia la raíz de $r$.

Luego tenemos al **Teorema del valor intermedio** (no confundir con el Teorema del [[4- Raíces en 1D (Parte 2)#^63be27|valor medio]]): *Sea $f$ una función continua en un intervalo \[$a$, $b$], entonces $f$ recorre cada valor entre $f(a)$ y $f(b)$, lo que implica que debe existir un número $c \in$ \[$a$, $b$] tal que $f(c) = y$*.

Después viene el **Teorema de Rolle**: *Sea $f$ una función continua y diferenciable en un intervalo \[$a$, $b$] y asumiendo que $f(a) = f(b)$, entonces sabemos que existe un punto $c$ tal que $f´(c) = 0$*. 

Y finalmente terminamos con posiblemente uno de los teoremas más importantes de este curso, el **Teorema de Taylor**: *Sea $x$ y $x_0$ números reales, y $f(x)\ k+1$ veces continuamente diferenciable en el intervalo entre $x$ y $x_0$, entonces existe un número $c$ tal que:* 
$$f(x) = f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots + \frac{f^k(x_0)}{k!}(x-x_0)^k + \frac{f^{k+1}(c)}{(k+1=!}(x-x_0)^{k+1}$$
Cabe destacar que este teorema es valido para cada triada de ($x$, $x_0$, $c$), de forma que si llegara a cambiar alguno de estos 3 valores para una misma función $f$, entonces lo más probable es que los otros 2 valores también terminen cambiando sus resultados finales. ^f6fed6

## Método de Newton-Raphson

El [[4- Raíces en 1D (Parte 2)#^f6fed6|Teorema de Taylor]] nos indica la siguiente afirmación al considerar los primeros 3 términos de la expansión para una función $f(x)$:
$$f(x) = f(x_0) + f'(x_0)(x-x_0) + \frac{f''(c)}{2!}(x-x_0)^2$$
Supongamos ahora que estamos interesados en obtener una [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]] de la función $f(x)$ la cual vamos a llamar $r$:
$$f(r) = f(x_0) + f'(x_0)(r-x_0) + \frac{f''(c)}{2!}(r-x_0)^2$$
Gracias a que $r$ es una raíz de $f(x)$, entonces sabemos que $f(r) = 0$:
$$0 = f(x_0) + f'(x_0)(r-x_0) + \frac{f''(c)}{2!}(r-x_0)^2$$
Despejando el $r$ ubicado en el término lineal:
$$\begin{align}
-f'(x_0)(r-x_0) =&\ f(x_0) + \frac{f''(c)}{2!}(r-x_0)^2 \\
r-x_0 =&\ -(f'(x_0))^{-1}f(x_0) -(f'(x_0))^{-1}\frac{f''(c)}{2!}(r-x_0)^2 \\
r=&\ x_0 - \frac{f(x_0)}{f'(x_0)} - \frac{\frac{f''(c)}{2}(r-x_0)^2}{f'(x_0)} 
\end{align}$$
Ahora, aunque nosotros acabamos de obtener un valor exacto para obtener la raíz $r$, esta sigue dependiendo del valor de $f''(c)$ el cual desconocemos, es por eso que vamos a trabajar esta ecuación bajo el supuesto de que $(r-x_0)^2$ es un número lo suficientemente pequeño como para "despreciar" todo el valor que se está restando en esta expresión (cosa que se aplica sí y solo si $|r-x_0|<1$), por lo que nosotros seremos capaces de obtener una raíz aproximada de $r$ la que denominaremos $x_1$ transformando la expresión anterior de la siguiente forma:
$$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}$$
Expresión que si generalizamos para una i-ésima iteración, obtenemos:
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} :=g_N(x_i)$$
Donde $g_N(x_i)$ corresponde a la función de Newton-Raphson para el término $x_i$. Cabe recalcar que para que este método sea efectivo necesitamos tomar un $x_0$ o *"initial guess"* lo suficientemente cercano a $r$ para cumplir el ya mencionado supuesto que se debía cumplir de $|r-x_0|<1$.

En pocas palabra, el algoritmo nos queda de la siguiente forma:

```markdown
x_0 = "Initial Guess"
for i in range(n):
    x_{i+1} = x_i - f(x_i)/f'(x_i)
```

Tomemos como ejemplo ahora la función $f(x) = x^3+x-1$, donde tenemos que $f'(x) = 3x^2 + 1$. Al construir la iteración de punto fijo de Newton obtenemos lo siguiente:
$$\begin{align}
x_{i+1} =&\ x_i - \frac{f(x_i)}{f'(x_i)} \\
x_{i+1} =&\ x_i - \frac{x_i^3 + x_i - 1}{3x^2 + 1} \\
x_{i+1} =&\ \frac{2x_i^3 + 1}{3x^2 + 1} := g_N(x_i)\\
\end{align}$$
Aplicando este método para un *"initial guess"* de -0.7, tenemos que este algoritmo nos devuelve los siguientes valores para las primeras 7 iteraciones:

| $i$ |    $x_i$     |    $e_i$     | $\frac{e_i}{e_{i-1}^2}$ |
| :-: | :----------: | :----------: | :---------------------: |
| $0$ |    $-0.7$    |    $1.38$    |            -            |
| $1$ |    $0.12$    |    $0.55$    |        $0.2906$         |
| $2$ |    $0.95$    |    $0.27$    |        $0.8933$         |
| $3$ |    $0.73$    |   $0.052$    |        $0.6924$         |
| $4$ |   $0.6845$   |   $0.0022$   |        $0.8214$         |
| $5$ |  $0.682332$  | $0.00000437$ |        $0.8527$         |
| $6$ | $0.68232780$ | $0.00000000$ |        $0.8541$         |
| $7$ | $0.68232780$ | $0.00000000$ |           ---           |

Donde gracias a los valores de $\frac{e_i}{e_{i-1}^2}$ podemos decir que efectivamente se logró obtener una [[4- Raíces en 1D (Parte 2)#^f07d7d|convergencia lineal]].

### Convergencia Cuadrática del Método de Newton
Antes de explicar como y cuando este método converge de forma cuadrática es necesario introducir el concepto de **convergencia cuadrática**: *Sea $e_i$ el error de la iteración i-ésima de un método iterativo. La iteración converge cuadráticamente si:*
$$\lim\limits_{i\to\infty}\frac{e_{i+1}}{e_i^2} = M < \infty$$
En pocas palabras, esto quiere decir que para todas las iteraciones posibles en un método iterativo la razón entre el error del siguiente término con su error actual al cuadrado deben aproximarse a una constante que sea finita $M$ para poder decir que esta efectivamente está convergiendo de forma cuadrática. Cabe recalcar además que una convergencia de tipo cuadrática converge más rápido que una de tipo [[4- Raíces en 1D (Parte 2)#^f07d7d|lineal]], lo que implica además que permiten encontrar la raíz más rápido de lo normal.

Ahora, la convergencia cuadrática de este método se explica con el siguiente teorema: *Sea $f(x)$ una función dos veces continuamente diferenciable y $f(r) = 0$. Si $f'(r)\neq 0$, entonces el método de Newton es local y cuadráticamente convergente a $r$. El error $e_i$ en el paso $i$ satisface lo siguiente:*
$$\lim\limits_{i\to\infty}\frac{e_{i+1}}{e_i^2} = M,$$
*donde el valor de $M$ para este método corresponde a:*
$$M = \frac{|f''(r)|}{2|f'(r)|}$$
He de recalcar nuevamente que el método de Newton-Raphson solamente converge de forma cuadrática en situaciones donde $f'(r) \neq 0$. Para el lector más enfrascado en la teoría matemática y que le interesa saber porqué este método converge bastante rápido dada esta condición de $f$, entonces son bienvenidos a revisar los apuntes de profesor con la [[Apuntes_INF-285_2024-v0613.pdf#search=Demostración. La demostración contienen 2 componentes: (i) Demostrar que converge localmente y (ii) demostrar que converge cuadráticamente.|demostración]].

### Convergencia Lineal del Método de Newton
Por supuesto, como estarán intuyendo del párrafo anterior, Newton Raphson converge de forma [[4- Raíces en 1D (Parte 2)#^f07d7d|lineal]] siempre y cuando $f'(r) \neq 0$. Asumamos que $r$ es una [[3- Raíces en 1D (Parte 1)#^a184d7|raíz]] de $f$ y que esta función es además diferenciable. Entonces si $0 = f(r) = f'(r) = \cdots = f^{(m-1)}(r)$, pero $f^{(m)}(r) \neq 0$, entonces decimos que la raíz $r$ posee multiplicidad $m$. Además, si es que se llega a dar el caso de que $m > 1$ entonces la función $f$ posee una raíz múltiple, caso contrario ($m = 1$) $f$ solo posee una raíz simple.

Con esto explicado, podemos introducir el siguiente teorema de convergencia lineal del Teorema: *Asumiendo que $f$ es una función ($m + 1$) - veces continua, diferenciable en \[a, b] y tiene una multiplicidad $m$ en la raíz $r$. Entonces el método de Newton es linealmente convergente a $r$ con tasa $S$:*
$$\lim\limits_{i\to\infty}\frac{e_{i+1}}{e_i} = \frac{m-1}{m} = S \neq 0$$
Y por supuesto, gracias a este teorema es que tenemos la oportunidad de además estudiar la multiplicidad de la raíz que nosotros estamos buscando, idea la cual podemos aplicar realizando una pequeña modificación al Método de Newton: *Si $f$ es ($m + 1$) - veces continua y diferenciable en \[a, b], donde hay una raíz $r$ de multiplicidad $m > 1$, entonces el método de Newton modificado:*
$$x_{i+1} = x_i - m\frac{f(x_i)}{f'(x_i)}$$
*converge local y cuadráticamente a $r$*.