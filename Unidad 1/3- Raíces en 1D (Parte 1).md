$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
En esta sección estudiaremos diversos algoritmos para poder descubrir las raíces de funciones que sean de 1D, es decir, vamos a buscar para funciones de la forma $f(x):\mathbb{R}\rightarrow\mathbb{R}$ cierto valores raíces que denotaremos como $r$ que posee un dominio en $\mathbb{R}$ tal que $f(r)=0$. ^a184d7

Con el fin de poder determinar cual de los algoritmos que se van a estudiar es el más adecuado, es necesario analizar ciertos puntos de lo anteriormente mencionado.

Con respecto al dominio de $f(x)$ nos preguntaremos:
- ¿Existe alguna estimación gruesa para la que nosotros podamos intuir donde se ubica(n) la(s) raíces de la función?
- ¿El dominio de la función $f(x)$ es un intervalo acotado?

Luego, si consideramos a la función $f(x)$ como tal:
- ¿Poseemos la definición de la función $f(x)$? (es decir, sabemos si $f(x)$ es una parábola, pseudo-parábola, un polinomio, etc..?)
- ¿Podemos aplicar el algoritmo de búsqueda de raíces directamente en esta función o tendremos que realizarle una transformación previa?

Finalmente, considerando a la raíz $r$:
- ¿Existe un valor dentro del intervalo de dominio dado tal que nosotros podamos obtener un valor de $r$ compatible?

Estas preguntas son importantes plantearlas a la hora de resolver un problema el cual nosotros decidamos que es clave y eficiente hacer una búsqueda de raíces. 

## Método de la Bisección

Para decidir si es que este algoritmo es el adecuado para identificar una raíz, definimos el siguiente teorema:

*Sea $f$ una función continua en \[$a$, $b$] (o sea, en un intervalo acotado) para el cual se satisface que $f(a)f(b)<0\phantom{}$, entonces $f$ posee una raíz $r$ entre los valores $a$ y $b$, de modo que se satisface $a<r<b$ y que $f(r)=0$*.

Esto quiere decir que si se llegara a cumplir $f(a)f(b)<0$ entonces sabemos al 100% de que hay una raíz en el intervalo abierto $(a, b)$ aunque todavía no sabemos cual es exactamente, sin embargo, que no se cumpla esta condición NO SIGNIFICA que no exista una raíz entre $a$ y $b$. 

Ahora, nuestro algoritmo va a recibir 3 parámetros: $a$, $b$ y $f$, o si queremos reducir el tiempo en el que el algoritmo encuentre una solución podemos implementar un cuarto parámetro $\text{TOL}$, en donde este último corresponde a una cantidad de tolerancia (o error) que se va a permitir para determinar en qué momento se detendrá el algoritmo (y con cuanta precisión habremos encontrado la raíz $r$). Dependiendo de la implementación del algoritmo que uno aplique, nosotros podemos asumir que se cumple $f(a)f(b) < 0$ o podemos corroborar durante la ejecución que se cumpla el teorema anterior. El primer paso a seguir consiste en dividir el intervalo \[$a$, $b$] en 2 intervalos \[$a$, $c$] y \[$c$, $b$], donde $c = \frac{a+b}{2}$ (en pocas palabras, vamos a dividir el intervalo por la mitad). Considerando que solamente existe 1 raíz que se encuentra en alguno de estos 2 intervalos, para saber en cual de los 2 intervalos se encuentra la raíz vamos a comprobar el teorema para ambos intervalos, es decir, vamos a ver si $f(a)f(c) < 0$ es verdadero o si $f(c)f(b)<0$ lo es. Después basta con comprobar si es que el resultado obtenido se asemeja a la tolerancia $\text{TOL}$ buscada para determinar si es que hay que volver a ejecutar el algoritmo para el nuevo intervalo buscado o si finalmente podemos decir que el valor de $c$ ya se aproxima lo suficiente a nuestra raíz deseada.

```pseudo
    \begin{algorithm}
    \caption{Biseccion}
    \begin{algorithmic}
      \Procedure{Biseccion}{$a, b, f, \text{TOL}$}
        \While{($\frac{b-a}{2} < \text{TOL}$)}
        \State $c \gets \frac{a+b}{2}$
        \If{($f(c)=0$)}
	        \Break
        \EndIf
        \If{($f(a)f(c)<0$)} 
	        \State $b \gets c$
	    \Else 
		    \State $a \gets c$ 
		\EndIf    
        \EndWhile
	  \Return $\frac{a+b}{2}$
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

Notar que el único problema que posee esta implementación es que no verifica que inicialmente $a$ o $b$ sean alguna raíz de nuestra función $f$, por lo que estaríamos perdiendo la oportunidad de obtener una raíz de $f$ con una precisión del 100%.

## Características del Método de Bisección

Por la forma en la que funciona el algoritmo sabemos que el intervalo inicial \[$a$, $b$] se irá reduciendo por la mitad por cada iteración que se tenga que realizar, lo que nos permite realizar el siguiente análisis de su error:
- Intervalo de largo inicial $(b-a)$.
- Intervalo de largo $\frac{b-a}{2}$ en la primera iteración.
- $\cdots$
- Intervalo de largo $\frac{b-a}{2^n}$ en la n-ésima iteración.  

Ahora, digamos que la aproximación inicial obtenida en la primera iteración del algoritmo equivale a $x^{(0)}_c = \frac{a+b}{2}$, y además, como sabemos que nuestra raíz efectivamente está en el intervalo \[$a$, $b$] podemos concluir que la diferencia entre la aproximación $x_c$ (que corresponde al punto medio calculado en la enésima iteración) y $r$ corresponde a:

$$|x_c^{(o)}-r| \leq \frac{b-a}{2}$$ ^e1244b

Esta expresión la podemos generalizar para la n-ésima iteración hecha por el algoritmo, por lo que finalmente podemos definir al [[2- Estándar de Punto Flotante y Pérdida de Importancia#^636068|error absoluto]] de esta iteración como:

$$Error\ Absoluto=|x_c^{(n)}-r| \leq \frac{b-a}{2^{n+1}}$$ ^e1f2b1

Gracias a esta expresión, sabemos que el error de la raíz encontrada va disminuyendo por la mitad cada vez que se realiza una nueva iteración, esto luego de realizar $n+2$ evaluaciones de $f(x)$.

A partir de este análisis pueden surgir 2 dudas:
- ¿Por que se realizan $n + 2$ iteraciones en vez de solo $n$ iteraciones? 
- ¿Por que razón el error absoluto cumple con $|x_c^{(n)}-r| \leq \frac{b-a}{2^{n+1}}$ y no con $|x_c^{(n)}-r| \leq \frac{b-a}{2^n}$?

La respuesta a la primera pregunta es de hecho bastante simple, supongamos que nosotros queremos aplicar bisección dentro de una función $f(x)$ en un intervalo \[$a$, $b$\] con 1 sola iteración (suponiendo por conveniencia que se cumple $f(a)f(b)<0$), y para lograrlo tenemos que realizar 3 evaluaciones, $f(a)$, $f(b)$ y $f(\frac{a-b}{2})$, lo que equivale a un total de $n + 2 = 3$ evaluaciones. Esto nos da a entender que ese 2 que aparece en la expresión corresponde a las evaluaciones de $f$ en los extremos $a$ y $b$ del intervalo inicial.
Con respecto a la segunda pregunta, primero recordemos que $x_c^{(n)}$ corresponde al valor de $c$ en la enésima iteración. Ahora, por definición tenemos que la expresión $|x_c^{(n)}-r|$ corresponde a la distancia que hay entre este término con la raíz que nosotros estamos buscando, mientras que la expresión $\frac{b-a}{2^{n}}$ nos indica el tamaño del intervalo que nosotros estamos revisando en la enésima iteración. El problema con tomar la expresión $\frac{b-a}{2^{n}}$ en vez de $\frac{b-a}{2^{n+1}}$ es que, suponiendo que en la enésima iteración estamos operando sobre un nuevo intervalo \[$a'$, $b'$\], estamos suponiendo que existe la posibilidad de que nuestro punto $x_c$ se encuentre en alguno de los extremos de este nuevo intervalo mientras que nuestra raíz buscada $r$ esté en el otro extremo, siendo que esto es falso debido a que sabemos que nuestro punto $x_c$ siempre se va a encontrar en el punto medio entre estos 2 extremos, por lo que la distancia real corresponde a $\frac{b-a}{2^{n}}\frac{1}{2} = \frac{b-a}{2^{n+1}}$.

## Precisión en Decimales para Métodos Iterativos de Raíces

Tal como se mencionó anteriormente, es posible darle al método de bisección una tolerancia de aceptación en vez de una $n$ cantidad de iteraciones para decidir en qué momento debiera detenerse el algoritmo, y de hecho, esto es posible hacerlo de cierto modo para otros algoritmos iterativos que estudiaremos un poco más adelante, es por esto que puede llegar a ser necesario el buscar una forma de encontrar un valor de $n$ lo suficientemente grande como para aceptar un margen de error lo suficientemente pequeño para una respuesta.

Se presenta a continuación la siguiente definición: 
*Se definirá que una solución es correcta en p decimales si el error absoluto es menor que $0.5*10^{-p}$*.  ^c6ffe3

Con esta definición que vamos a aplicar para el resto del curso podemos imponer un estándar para medir la eficiencia de estos algoritmos de búsqueda de raíces.

Tomemos este ejemplo usando el algoritmo de bisección: se nos pide determinar la cantidad de evaluaciones necesarias para encontrar una raíz de $f(x) = \cos{x}-x$ en el intervalo \[0, 1] con una precisión de 6 decimales. Aquí nosotros sabemos que:
$$|x_c-r| \leq \frac{1-0}{2^{n+1}} < 0.5*10^{-6}$$
Despejando el valor de $n$ obtenemos:
$$\begin{aligned}
	\frac{1}{2^{n+1}} &< \frac{1}{2} * 10^{-6} \\
	\frac{2}{10^{-6}} &< 2^{n+1} \\
	2 * 10^6 &< 2^{n+1} \\
	\log_2{(2*10^6)} &< n + 1 \\
	\log_2{2} - 1 + 6\log_2{10} &< n\\
	6\log_2{10} \approx 19.9 &< n
\end{aligned}$$
Por lo tanto, nuestro valor de $n$ es 20, y como en bisección habíamos mencionado que se realizan $n+2$ evaluaciones entonces para este problema se realizan $20+2=22$ evaluaciones. Notemos en este desarrollo que no es necesario realizar el algoritmo para poder saber la cantidad de evaluaciones necesarias en ella para encontrar la raíz! 

 
