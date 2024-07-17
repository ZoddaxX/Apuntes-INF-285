En esta sección estudiaremos diversos algoritmos para poder descubrir las raíces de funciones que sean de 1D, es decir, vamos a buscar para funciones de la forma $f(x):\mathbb{R}\rightarrow\mathbb{R}$ cierto valores raíces que denotaremos como $r$ que posee un dominio en $\mathbb{R}$ tal que $f(r)=0$.

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

Para decidir si es que este algoritmo es el adecuado para identificar una raíz, definimos el siguiente teorema: *Sea $f$ una función continua en \[$a$, $b$] (o sea, en un intervalo acotado) para el cual se satisface que $f(a)f(b)<0\phantom{}$, entonces $f$ posee una raíz $r$ entre los valores $a$ y $b$, de modo que se satisface $a<r<b$ y que $f(r)=0$*. Esto quiere decir que si se llegara a cumplir $f(a)f(b)<0$ entonces sabemos al 100% de que hay una raíz en el intervalo abierto $(a, b)$ aunque todavía no sabemos cual es exactamente, sin embargo, que no se cumpla esta condición NO SIGNIFICA que no exista una raíz entre $a$ y $b$. 

Ahora, nuestro algoritmo va a recibir 3 parámetros: $a$, $b$ y $f$, o si queremos reducir el tiempo en el que el algoritmo encuentre una solución podemos implementar un cuarto parámetro $\text{TOL}$, en donde este último corresponde a una cantidad de tolerancia (o error) que se va a permitir para determinar en qué momento se detendrá el algoritmo (y con cuanta precisión habremos encontrado la raíz $r$). Dependiendo de la implementación del algoritmo que uno aplique, nosotros podemos asumir que se cumple $f(a)f(b) < 0$ o podemos corroborar durante la ejecución que se cumpla el teorema anterior. El primer paso a seguir consiste en dividir el intervalo \[$a$, $b$] en 2 intervalos \[$a$, $c$] y \[$c$, $b$], donde $c = \frac{a+b}{2}$ (en pocas palabras, vamos a dividir el intervalo por la mitad). Considerando que solamente existe 1 raíz que se encuentra en alguno de estos 2 intervalos, para saber en cual de los 2 intervalos se encuentra la raíz vamos a comprobar el teorema para ambos intervalos, es decir, vamos a ver si $f(a)f(c) < 0$ es verdadero o si $f(c)f(b)<0$ lo es. Después basta con comprobar si es que el resultado obtenido se asemeja a la tolerancia $\text{TOR}$ buscada para determinar si es que hay que volver a ejecutar el algoritmo para el nuevo intervalo buscado o si finalmente podemos decir que el valor de $c$ ya se aproxima lo suficiente a nuestra raíz deseada.

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

Ahora, digamos que la aproximación inicial obtenida en la primera iteración del algoritmo equivale a $x^{(0)}_c = \frac{a+b}{2}$, y además, como sabemos que nuestra raíz efectivamente está en el intervalo \[$a$, $b$] podemos concluir que la diferencia entre la aproximación $x_c$ y $r$ corresponde a:
$$|x_c^{(o)}-r| \leq \frac{b-a}{2}$$
Esta expresión la podemos generalizar para la n-ésima iteración hecha por el algoritmo, por lo que finalmente podemos definir al [[2- Estándar de Punto Flotante y Pérdida de Importancia#^636068|error absoluto]] de esta iteración como:
$$Error\ Absoluto=|x_c^{(n)}-r| \leq \frac{b-a}{2^{n+1}}$$
Gracias a esta expresión, sabemos que el error de la raíz encontrada va disminuyendo por la mitad cada vez que se realiza una nueva iteración, esto luego de realizar $n+2$ evaluaciones de $f(x)$.

Se presenta ahora la siguiente definición: *Se definirá que una solución es correcta en p decimales si el error absoluto es menor que $0.5*10^{-p}$*. Con esta definición que vamos a aplicar para el resto del curso podemos imponer un estándar para medir la eficiencia de estos algoritmos de búsqueda de raíces.

Tomemos este ejemplo usando el algoritmo de bisección: se nos pide determinar la cantidad de evaluaciones necesarias para encontrar una raíz de $f(x) = \cos{x}-x$ en el intervalo \[0, 1] con una precisión de 6 decimales. Aquí nosotros sabemos que:
$$|x_c-r| < \frac{1-0}{2^{n+1}} < 0.5*10^{-6}$$
Despejando el valor de $n$ obtenemos:
$$n > \frac{6}{\log_{10}2} \approx 19.9$$
Por lo tanto, nuestro valor de $n$ es 20, y como en bisección habíamos mencionado que se realizan $n+2$ evaluaciones entonces para este problema se realizan $20+2=22$ evaluaciones. Notemos en este desarrollo que no es necesario realizar el algoritmo para poder saber la cantidad de evaluaciones necesarias en ella para encontrar la raíz! 