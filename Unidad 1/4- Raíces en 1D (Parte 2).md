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

De paso les he adjuntado un código de Python para que puedan graficar las $g(x)$ con las $n$ iteraciones que gusten: [[Diagrama de Cobweb]]

Visualicemos ahora un diagrama para una $g(x)$ que efectivamente converja. Tomemos:
$$g(x) = -\frac{1}{2}x + \frac{3}{2}$$
Definamos nuestro *initial guess* $x_0$ como 2.7, haciendo unas 20 iteraciones nosotros obtenemos los siguientes resultados:
$$ \begin{array}{lll} 
x_0 = 2.7 & x_7 = g_1(x_6) = 0.986719 & x_{14} = g_1(x_{13}) = 1.0001 \\ 
x_1 = g_1(x_0) = 0.15 & x_8 = g_1(x_7) = 1.00664 & x_{15} = g_1(x_{14}) =  0.999948 \\ 
x_2 = g_1(x_1) = 1.425 & x_9 = g_1(x_8) = 0.99668 & x_{16} = g_1(x_{15}) = 1.00003 \\ 
x_3 = g_1(x_2) = 0.7875 & x_{10} = g_1(x_9) = 1.00166 & x_{17} = g_1(x_{16}) = 0.999987 \\ 
x_4 = g_1(x_3) = 1.10625 & x_{11} = g_1(x_{10}) = 0.99917 & x_{18} = g_1(x_{17}) = 1.00001 \\ 
x_5 = g_1(x_4) = 0.946875 & x_{12} = g_1(x_{11}) = 1.00042 & x_{19} = g_1(x_{18}) = 0,999997\\ 
x_6 = g_1(x_5) = 1.02656 & x_{13} = g_1(x_{12}) = 0.999792 & x_{20} = g_1(x_{19}) = 1,0000 \end{array} $$
Es evidente que en este caso hay una clara convergencia hacia 1. Para las primeras 6 iteraciones de este caso nuestro diagrama se ve así:

![[Cobweb_2.png]]

### Convergencia Lineal de Iteración de Punto Fijo
Para poder analizar la convergencia de una iteración de punto fijo, es necesario introducir el **Teorema del valor medio**: *Sea $f$ una función continua en el intervalo \[$a$, $b$] y diferenciable en el intervalo ]$a$, $b$\[. Entonces existe un número $c$ entre $a$ y $b$ tal que:* 
$$f´(c) = \frac{f(b) - f(a)}{b-a}$$

Ahora es necesario definir la convergencia lineal de forma matemática: *Sea $e_i = |x_i - r|$ el error absoluto del paso $i$ de un método iterativo. Si se cumple:*
$$\lim\limits_{i\to\infty}\frac{e_{i+1}}{e_i} = S < 1$$
*Se dice entonces que el método obedece "convergencia lineal" con tasa S*.

Finalmente, gracias a este teorema, definición y [[Apuntes_INF-285_2024-v0613.pdf#search=Demostración. Sea xi el i -ésimo termino de la iteración|esta demostración]] podemos concluir lo siguiente con respecto a este algoritmo que si asumimos que hay una función $g(x)$ que nosotros hayamos encontrado y que sea continua y diferenciable, que tiene un punto fijo $g(r) = r$ y que además $S = |g´(r)| < 1$, entonces la iteración de punto fijo converge linealmente con tasa $S$ al punto fijo $r$ para ciertos *"initial guesses"* que estén lo suficientemente cerca de r. Es decir, para que el algoritmo funcione lo suficientemente bien, y si es que la serie $x_i$ no termina divergiendo, entonces necesitaríamos estimar un *initial guess* adecuado para que el algoritmo otorgue resultados positivos.

### Teoremas y Definiciones Útiles
