
Los algoritmos de GRM se unen junto a los ya vistos en el [[5- Sistemas de Ecuaciones Lineales|tema 5]] para poder resolver sistemas de ecuaciones lineales cuadrados de la forma $A\bm{\text{x}} = \bmt{b}$, los cuales funcionan de forma iterativa y además son capaces de llegar a la respuesta única de un sistema de ecuaciones de dimensiones $n \times n$ en a lo mucho $n$ iteraciones.

Antes de poder revisar los detalles sobre este tipo de algoritmo, es necesario revisar el siguiente teorema de Cayley-Hamilton: *Una matriz de dimensiones $n \times n$ es aniquilada (D:) por su polinomio característico $p(\lambda) = det(\lambda I - A)$, el cual es mónico de grado $n$*. 

El polinomio característico de una matriz $A \in \mathbb{R}^{n \times n}$ se expresa de la siguiente manera:
$$p(\lambda) =  det(\lambda I - A) = \lambda^n + \check{c}_{n-1}\lambda^{n-1} + \cdots + \check{c}_1\lambda + (-1)^n\ det(A)$$
donde $\lambda \in \mathbb{C}$, $det$ es el determinante e $I$ corresponde a la matriz identidad de dimensiones $n \times n$. Ahora, si evaluamos el polinomio característico con $A$ obtenemos:
$$p(A) = A^n + \check{c}_{n-1}A^{n-1} + \cdots + \check{c}_1A + (-1)^n\ det(A)I$$
Lo que nos indica el teorema de Cayley-Hamilton es que el resultado de esta evaluación corresponde a la matriz nula, es decir:
$$p(A) = A^n + \check{c}_{n-1}A^{n-1} + \cdots + \check{c}_1A + (-1)^n\ det(A)I = \underline{\underline{0}}$$
donde $\underline{\underline{0}}$ es la matriz hecha de 0´s de dimensiones $n \times n$. La ecuación anterior nos permite obtener el valor de la inversa de $A$ de la siguiente forma:
$$\begin{align}
	A^n + \check{c}_{n-1}A^{n-1} + \cdots + \check{c}_1A + (-1)^n\ det(A)I =&\ \underline{\underline{0}} \\
	A^n + \check{c}_{n-1}A^{n-1} + \cdots + \check{c}_1A =&\ (-1)^{n-1}\ det(A)I \\
	A^{n-1} + \check{c}_{n-1}A^{n-2} + \cdots + \check{c}_1I =&\ (-1)^{n-1}\ det(A)A^{-1}
\end{align}$$
Por lo que despejando $A^{-1}$ obtenemos:
$$A^{-1} = \frac{(-1)^{n-1}}{det(A)}(A^{n-1} + \check{c}_{n-1}A^{n-2} + \cdots + \check{c}_1I)$$
Tomemos ahora nuevamente nuestra forma base de un sistema de ecuaciones lineal:
$$A\bmt{x} = \bmt{b}$$
y ahora intentemos despejar $\bmt{x}$ usando la nueva definición de la inversa de $A$ que despejamos antes:
$$\begin{align}
	\bmt{x} =&\ A^{-1}\bmt{b} \\
	A^{-1}\bmt{b} =&\ \frac{(-1)^{n-1}}{det(A)}(A^{n-1} + \check{c}_{n-1}A^{n-2} + \cdots + \check{c}_1I)\bmt{b} \\
	=&\ \frac{(-1)^{n-1}}{det(A)}(A^{n-1}\bmt{b} + \check{c}_{n-1}A^{n-2}\bmt{b} + \cdots + \check{c}_1\bmt{b})\\
	\bmt{x} =&\ \sum_{i=1}^{n}\mathring{c}_iA^{i-1}\bmt{b}
\end{align}$$
Esta expresión nos demuestra que es posible representar la solución de un sistema de ecuaciones lineales mediante una combinación lineal de los vectores $\bmt{b}, A\bmt{b}, A^2\bmt{b}, \cdots, A^{n-1}\bmt{b}$. Cabe destacar además que el carácter $\mathring{c}$ además de incluir los valores $\check{c}_i$ del polinomio, también contiene al valor de $\frac{(-1)^{n-1}}{det(A)}$     


