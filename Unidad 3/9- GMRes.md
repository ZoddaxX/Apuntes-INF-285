
El algoritmo de GRM se unen junto a los ya vistos en el [[5- Sistemas de Ecuaciones Lineales|tema 5]] para poder resolver sistemas de ecuaciones lineales cuadrados de la forma $A\bm{\text{x}} = \bmt{b}$, el cual funciona de forma iterativa y además es capaz de llegar a la respuesta única de un sistema de ecuaciones de dimensiones $n \times n$ en a lo mucho $n$ iteraciones con una precisión perfecta (mientras no se vea restringida por la precisión usada, claro...).

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
$$A\mathbf{x} = \mathbf{b}$$
y ahora intentemos despejar $\bmt{x}$ usando la nueva definición de la inversa de $A$ que despejamos antes:
$$\begin{align}
	\mathbf{x} =&\ A^{-1}\mathbf{b} \\
	A^{-1}\mathbf{b} =&\ \frac{(-1)^{n-1}}{det(A)}(A^{n-1} + \check{c}_{n-1}A^{n-2} + \cdots + \check{c}_1I)\mathbf{b} \\
	=&\ \frac{(-1)^{n-1}}{det(A)}(A^{n-1}\mathbf{b} + \check{c}_{n-1}A^{n-2}\mathbf{b} + \cdots + \check{c}_1\mathbf{b})\\
	\bmt{x} =&\ \sum_{i=1}^{n}\mathring{c}_iA^{i-1}\mathbf{b}
\end{align}$$
Esta expresión nos demuestra que es posible representar la solución de un sistema de ecuaciones lineales mediante una combinación lineal de los vectores $\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{n-1}\mathbf{b}$. Cabe destacar además que el carácter $\mathring{c}$ además de incluir los valores $\check{c}_i$ del polinomio característico, también contiene al valor de $\frac{(-1)^{n-1}}{det(A)}$. Cabe destacar además que se está considerando que la matriz $A$ no es una [[|matriz singular]], por lo que $A^0 = I$. Supongamos ahora que queremos tomar los primeros $k$ vectores del conjunto de vectores $\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{n-1}\mathbf{b}$, el subespacio vectorial generado por ese conjunto es el siguiente:
$$\mathcal{K}_k = \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b})$$
donde $\mathcal{K}_k$ se le conoce como el sub-espacio de Krylov. Con esto puedo introducirles los GMRes como un algoritmo que busca una aproximación de $\bmt{x}$ restringiéndolo al sub-espacio de Krylov y resolviendo un problema de cuadrados equivalente.

## Derivación de GMRes

Antes de continuar con la explicación del funcionamiento del algoritmo, es conveniente recordar las dimensiones de los elementos con los que vamos a trabajar:
$$\begin{align}
	A &\in \mathbb{R}^{n \times n} \\
	\mathbf{x} &\in \mathbb{R}^{n} \\
	\mathbf{b} &\in \mathbb{R}^{n} \\
	A^{j}\mathbf{b} &\in \mathbb{R}^{n}, & j \in \{0,1,2,\cdots,k-1\}\\
\end{align}$$
Y también vuelvo a incluir el sub-espacio de Krylov:
$$\mathcal{K}_k = \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b})$$
donde aprovecho de añadir que consiste en un sub-espacio vectorial en $\mathbb{R}^n$ de dimensión $k$, por lo que cada elemento de $\mathcal{K}_k \in \mathbb{R}^n$, SIN EMBARGO, como en este sub-espacio tenemos únicamente $k$ filas linealmente independientes entre sí, eso significa que no se pueden representar todos los valores de $\mathbb{R}^n$, aunque evidentemente esto dejará de ser así cuando $k = n$.

>[!info] Detalle del sub-espacio de Krylov con GMRes.
>Un punto clave de los GMRes, es que al estar haciendo una búsqueda dentro de un sub-espacio de Krylov necesitamos que el valor de $\bmt{x}$ pertenezca efectivamente a él, de lo contrario el algoritmo no funcionará. Esto nos puede llevar a pensar de que nosotros podemos buscar una "cota" para la cual realizar la búsqueda de esta solución (algo así como una búsqueda binaria), solo que esta vez lo estaremos realizando en el mundo de un sub-espacio en vez de cotas dentro de un conjunto de valores.
>

Ahora, ¿Qué significa exactamente que $\bmt{x} \in \mathcal{K}_k$? La respuesta a esto es bastante simple, simplemente $\bmt{x}_k$ debe poder ser representado como una combinación lineal del conjunto de vectores basales que generen $\mathcal{K}_k$, donde en este caso $\bmt{x}_k$ está expresada de esta forma:
$$
\mathbf{x}_k = \tilde{c}_1 \mathbf{b} + \tilde{c}_2 \mathbf{A} \mathbf{b} + \cdots + \tilde{c}_k \mathbf{A}^{k-1} \mathbf{b}.
$$
Como sabemos que $\mathbf{x}$ está restringido al sub-espacio de Krylov, también podemos expresarlo de la siguiente forma:
$$\begin{align}
	\mathbf{x}_k =&\ \underbrace{\begin{bmatrix} \bmf{b}, & A\bmf{b}, & \cdots, & A^{k-1}\bmf{b} \end{bmatrix}}_{K_k}
	\underbrace{
		\begin{bmatrix}
			\tilde{c}_1 \\
			\tilde{c}_2 \\
			\vdots \\
			\tilde{c}_k \\
		\end{bmatrix}
	}_{\tilde{\bmf{c}}_k} \\
	=& K_c\ \tilde{\bmf{c}}_k
\end{align}$$
Ahora, ¿Cómo utilizamos esta representación para encontrar el valor de $\bmf{x}_k$ con mínimos cuadrados? Notemos que $\bmf{x} \approx \bmf{x}_k$, lo cual es evidente si consideramos que $\bmf{x}$ ya puede generar todos los valores de $\bmf{x}_k$, y además este último sigue la misma estructura que la primera (solo que con un error asociado, provocado de manera indirecta al no poseer todos los términos necesarios para generar una combinación lineal exacta para representar ciertos valores de $\bmf{x}$), por lo que podemos reemplazar esta expresión en el sistema de ecuaciones original:
$$\begin{align}
	A\bmf{x}_k \approx&\ b \\
	AK_k\tilde{\bmf{c}}_k \approx&\ b
\end{align}$$
Donde notamos un par de detalles:
- A$K_k$ es una matriz de dimensiones $n \times k$.
- $\tilde{\bmf{c}}_k \in \mathbb{R}^k$.
Esto quiere decir que estamos ante un sistema de ecuaciones sobre-determinado, es decir, poseemos un sistema de ecuaciones con una mayor cantidad de ecuaciones que de incógnitas al darse que $n > k$, lo que quiere decir que esta parte del problema se ha reducido a un problema de [[8- Mínimos Cuadrados|mínimos cuadrados]], lo que implica que podemos encontrar una solución al sistema de ecuaciones que minimice su error cuadrático de la siguiente forma:
$$\overline{\tilde{\bmf{c}}}_k = \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - AK_k\tilde{\bmf{c}}_k||_2^2$$
Ahora, muchos se estarán preguntando, ¿No basta con los mínimos cuadrados para obtener la solución de nuestro sistema? La respuesta es que no, ya que la matriz $K_k$ del sub-espacio de Krylov dentro de la ecuación anterior está mal condicionada, y esto es debido a que los vectores resultantes terminan convergiendo hacia el vector asociado al valor propio dominante, lo que se traduce en que los nuevos vectores que aparezcan para cada iteración del método se van a parecer cada vez más entre sí, lo que puede provocar que más de un par de filas de esta matriz resulten ser linealmente independientes.

![[Apuntes_INF-285_2024-v0613.pdf#page=156&rect=60,605,292,727|Apuntes_INF-285_2024-v0613, p.155]]

¿Y la solución? Construir una nueva base para el sub-espacio de Krylov $\mathcal{K}_k$ para el que todas sus filas sean linealmente independientes. Esto significa que nos interesa buscar una expresión como esta:
$$\begin{align}
\mathcal{K}_k =&\ \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b}) \\
=&\ \text{span}(\bmf{q}_1, \bmf{q}_2, \bmf{q}_3, \bmf{q}_4, \cdots, \bmf{q}_k)
\end{align}$$
donde por conveniencia vamos a considerar que todos los $\bmf{q}_i$ son ortonormales, es decir, poseen una [[|norma-2]] equivalente a 1 y son ortogonales entre sí. ¿Norma-2 de 1?¿Vectores ortogonales entre sí? Así es, estoy hablando del método de [[8- Mínimos Cuadrados#Ortonormalización de Gram-Schmidt|Ortonormalización de Gram-Schmid]], aunque para este caso hay que modificarla un poco...

>[!info] Iteración de Arnoldi
>La modificación del método de Ortonormalización de Gram-Schmid para funcionar con GMRes es llamada la iteración de Arnoldi.
>
>Recordemos que la Ortonormalización de Gram-Schmid consiste en que a partir de una secuencia de vectores indexados, digamos $\bmf{a}_i$ , que tradicionalmente se interpreta como las columnas de una matriz $A$, pero podría ser simplemente un conjunto de vectores, se obtiene otro conjunto de vectores $\bmf{q}_i$ tal que sean ortogonales entre sí, es decir, $\bmf{q}_i^* \bmf{q}_j = 0$ para $i \neq j$, y además que sean unitarios, o sea, $\bmf{q}_i^*\ \bmf{q}_i = ||\bmf{q}_1|| = 1$, lo que significa que deben ser ortonormales. Este método puede tomar en cuenta que se conocen de antemano la secuencia de vectores, aunque realmente no es necesario.
>
>La iteración de Arnoldi se puede interpretar como la ortonormalización de Gram-Schmid aplicada a una secuencia de vectores que no se conocen de antemano, pero que se pueden ir obteniendo por cada iteración de la ejecución de la ortonormalización. El algoritmo consiste en ortonormalizar el sub-espacio de Krylov $\mathcal{K}_k$:
>$$\mathcal{K}_k = \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b})$$
>es decir, se quiere construir la siguiente base ortonormal:
>$$\mathcal{K}_k = \text{span}(\bmf{q}_1, \bmf{q}_2, \bmf{q}_3, \bmf{q}_4, \cdots, \bmf{q}_k)$$
>y para ello, se genera la conexión con la siguiente secuencia de vectores que también general el sub-espacio de Krylov:
>$$\mathcal{K}_k = \text{span}(\bmf{q}_1, A\bmf{q}_1, A\bmf{q}_2, \cdots, A\bmf{q}_{k-1})$$
>Por lo que combinando la generación dinámica de los vectores anteriores con el algoritmo de ortonomalización de Gram-Schmid obtenemos la iteración de Arnoldi.









