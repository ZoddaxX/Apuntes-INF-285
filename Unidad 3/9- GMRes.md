$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
\newcommand{\bmt}[1]{\bm{\text{#1}}}
\newcommand{\bmf}[1]{\mathbf{#1}}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}
$$
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
Esta expresión nos demuestra que es posible representar la solución de un sistema de ecuaciones lineales mediante una combinación lineal de los vectores $\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{n-1}\mathbf{b}$. Cabe destacar además que el carácter $\mathring{c}$ además de incluir los valores $\check{c}_i$ del polinomio característico, también contiene al valor de $\frac{(-1)^{n-1}}{det(A)}$. Cabe destacar además que se está considerando que la matriz $A$ no es una [[1- Breve Introducción al Álgebra Lineal#Matriz Singular|matriz singular]], por lo que $A^0 = I$. Supongamos ahora que queremos tomar los primeros $k$ vectores del conjunto de vectores $\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{n-1}\mathbf{b}$, el subespacio vectorial generado por ese conjunto es el siguiente:
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

>[!tip] Detalle del sub-espacio de Krylov con GMRes.
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

![[Apuntes_INF-285_2024-v0613.pdf#page=156&rect=60,605,292,727|Apuntes_INF-285_2024-v0613, p.155]] ^b11ff2

¿Y la solución? Construir una nueva base para el sub-espacio de Krylov $\mathcal{K}_k$ para el que todas sus filas sean linealmente independientes. Esto significa que nos interesa buscar una expresión como esta:
$$\begin{align}
\mathcal{K}_k =&\ \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b}) \tag{1}\\
=&\ \text{span}(\bmf{q}_1, \bmf{q}_2, \bmf{q}_3, \bmf{q}_4, \cdots, \bmf{q}_k) \tag{2}
\end{align}$$

^fb9b2a

donde por conveniencia vamos a considerar que todos los $\bmf{q}_i$ son ortonormales, es decir, poseen una [[1- Breve Introducción al Álgebra Lineal#Norma|norma-2]] equivalente a 1 y son ortogonales entre sí. ¿Norma-2 igual 1?¿Vectores ortogonales entre sí? Así es, estoy hablando del método de [[8- Mínimos Cuadrados#Ortonormalización de Gram-Schmidt|Ortonormalización de Gram-Schmid]], aunque para este caso hay que modificarla un poco...

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

^a1e2e9

Es por ello que de las [[9- GMRes#^fb9b2a|ecuaciones 1 y 2]] podemos concluir lo siguiente:
$$\begin{align}
	\text{span}({\bmf{b}}) =&\ \text{span}({\bmf{q}}_1) \\
	\text{span}({\bmf{b}}, A\bmf{b}) =&\ \text{span}({\bmf{q}}_1, \bmf{q}_2) \\
	\vdots \\
	\text{span}({\bmf{b}}, A\bmf{b}, A^2\bmf{b}, A^3\bmf{b},\cdots,A^{k-1}\bmf{b}) =&\ \text{span}({\bmf{q}}_1, \bmf{q}_2, \bmf{q}_3, \bmf{q}_4, \cdots, \bmf{q}_k)
\end{align}$$
lo que implica que $\bmf{q}_1 = \frac{\bmf{b}}{||\bmf{b}||}$ y que además:
$$\begin{align}
	A\bmf{b} =&\ \hat{h}_{11}\bmf{q}_1 + \hat{h}_{21}\bmf{q}_2 \\
	A^2\bmf{b} =&\ \hat{h}_{12}\bmf{q}_1 + \hat{h}_{22}\bmf{q}_2 + \hat{h}_{32}\bmf{q}_3 \\
	\vdots \\
	A^{k-1}\bmf{b} =&\ \sum_{j=1}^{k} \hat{h}_{j,k-1}\bmf{q}_j \\
\end{align}$$
Nótese la similitud de esta expresión con la de la [[8- Mínimos Cuadrados#Ortonormalización de Gram-Schmidt|ortonormalización de Gram-Schmid]], la cual ya nos está dando la idea de porque es tan conveniente usar este método resolviendo mediante GMRes, aunque todavía tenemos que trabajar un poco más esta expresión. 

La expresión anterior es posible mejorarla aún mas, para ello basta con añadir la nueva secuencia de vectores ya mencionada con la [[9- GMRes#^a1e2e9|iteración de Arnoldi]]:
$$\begin{align}
\mathcal{K}_k =&\ \text{span}(\mathbf{b}, A\mathbf{b}, A^2\mathbf{b}, \cdots, A^{k-1}\mathbf{b}) \\
=&\ \text{span}(\bmf{q}_1, \bmf{q}_2, \bmf{q}_3, \bmf{q}_4, \cdots, \bmf{q}_k) \\
=&\ \text{span}(\bmf{q}_1, A\bmf{q}_1, A\bmf{q}_2, \cdots, A\bmf{q}_{k-1})
\end{align}$$


Con esto es posible formar esta nueva implicancia:
$$\begin{align}
	A\bmf{q}_1 =&\ h_{11}\bmf{q}_1 + h_{21}\bmf{q}_2 \\
	A\bmf{q}_2 =&\ h_{12}\bmf{q}_1 + h_{22}\bmf{q}_2 + h_{32}\bmf{q}_3 \\
	\vdots \\
	A\bmf{q}_{k} =&\ \sum_{j=1}^{k+1} h_{j,k-1}\bmf{q}_j \\
\end{align}$$

^cab3f5

Nótese que en este caso al haber expresado la fórmula general en función de $\bmf{q}_k$ es necesario incluir la ecuación con el término $\bmf{q}_{k+1}$, siendo esta la razón por la que en esta expresión la sumatoria va hasta el término $k+1$. Las ecuaciones anteriores representadas en forma de vectores columna y matrices queda de la siguiente forma:
$$A\ \underbrace{
	\begin{bmatrix}
		A\bmf{q}_1, & A\bmf{q}_2, & \cdots, & A\bmf{q}_k
	\end{bmatrix}
}_{Q_k}
=
\underbrace{
	\begin{bmatrix}
		A\bmf{q}_1, & A\bmf{q}_2, & \cdots, & A\bmf{q}_{k+1}
	\end{bmatrix}
}_{Q_{k+1}}
\underbrace{
	\begin{bmatrix}
		h_{11} & h_{12} & \cdots & h_{1,k-1}   & h_{1,k}   \\
		h_{21} & h_{22} & \cdots & h_{2,k-1}   & h_{2,k}   \\
		0      & h_{32} & \ddots & h_{3,k-1}   & h_{3,k}   \\
		\vdots & \ddots & \ddots & \ddots      & \vdots    \\
		0      & \ddots & \ddots & h_{k,k-1}   & h_{k,k}   \\
		0      & \cdots & \cdots & h_{k+1,k-1} & h_{k+1,k} \\
	\end{bmatrix}
}_{\tilde{H}_{k}}$$
La cual corresponde a la reducción parcial de $A$ a una forma de Hessenberg, es decir:
$$AQ_k = Q_{k+1}\tilde{H}_k$$
Donde $Q_k$ es la matriz con $k$ columnas ortonormales, $Q_{k+1}$ es la matriz con $k + 1$ columnas ortonormales y $\tilde{H}_k \in \mathbb{R}^{(k+1) \times k}$ es una matriz *upper Hessenberg*. Este nuevo tipo de matriz es muy similar a una matriz [[1- Breve Introducción al Álgebra Lineal#Matriz Diagonal|diagonal superior]], con la peculiaridad adicional de que además posee coeficientes en la primera sub-diagonal como pueden apreciar en la matriz de la última ecuación resuelta. En resumidas  cuentas, hemos sido capaces de armar una nueva base del sub-espacio de Krylov.

Ahora que poseemos todas las expresiones necesarias para resolver el problema de mínimos cuadrados podemos usar nuestra [[9- GMRes#^a1e2e9|iteración de Arnoldi]] para poder obtener la solución de nuestro problema, para los cuales se usan pasos muy similares a la de la [[8- Mínimos Cuadrados#Ortonormalización de Gram-Schmidt|ortonormalización de Gram-Schmid]], con el detalle adicional de que tenemos que $\bmf{q}_1 = \frac{\bmf{b}}{||\bmf{b}||}$. Por ejemplo, tomando en cuenta [[9- GMRes#^cab3f5|este sistema de ecuaciones]]:
$$\begin{align}
	h_{11} =&\ \bmf{q}_1^TA\bmf{q}_1 \\
	h_{21} =&\ ||A\bmf{q}_1 - h_{11}\bmf{q}_1|| \\
	\bmf{q}_2 =&\ \frac{A\bmf{q}_1 - h_{11}\bmf{q}_1}{h_{21}} \\
	h_{12} =&\ \bmf{q}_1^TA\bmf{q}_2 \\
	h_{22} =&\ \bmf{q}_2^T(A\bmf{q}_2 - h_{12}\bmf{q}_1) \\
	h_{32} =&\ ||A\bmf{q}_2 - h_{12}\bmf{q}_1 - h_{22}\bmf{q}_2|| \\
	\bmf{q}_3 =&\ \frac{A\bmf{q}_2 - h_{12}\bmf{q}_1 - h_{22}\bmf{q}_2}{h_{32}}
\end{align}$$
y así sucesivamente obtenemos todos los valores del sistema de ecuaciones.

Retomando inicialmente la idea de resolver un sistema de ecuaciones de la forma $A\bmf{x} = \bmf{b}$ restringiéndolo al sub-espacio de Krylov $\mathcal{K}_k$ y minimizando su error cuadrático podemos construir nuevamente el problema de minimización cuadrática asociado que se había hecho presente con el ejemplo de [[9- GMRes#^b11ff2|esta foto]] la cual nosotros expresamos anteriormente de la siguiente forma: 
$$\overline{\tilde{\bmf{c}}}_k = \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - AK_k\tilde{\bmf{c}}_k||_2^2$$
Ahora que nosotros poseemos una base más conveniente para lo cual expresar el sub-espacio de Krylov tenemos la siguiente identidad:
$$K_k\tilde{\bmf{c}}_k = Q_k\bmf{c}_k$$
Esto quiere decir que tanto las columnas de $K_k$ como las de $Q_k$ generan $\mathcal{K}_k$. Nótese que para cualquier vector en $\mathcal{K}_k$ es posible encontrar las coordenadas $\tilde{\bmf{c}}_k$ si utilizamos $K_k$ , de la misma forma podemos hacerlo si utilizamos $Q_k$ con $\bmf{c}_k$, aunque las coordenadas no son necesariamente las mismas. Con esto dicho, el problema cuadrático puede transformarse a la siguiente forma:
$$\overline{\bmf{c}}_k = \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - AQ_k\bmf{c}_k||_2^2$$
La cual es una expresión que podemos mejorar todavía más, recordando la reducción parcial a la forma de Hessenberg realizada $AQ_k = Q_{k+1}\tilde{H}_k$ obtenemos:
$$\overline{\bmf{c}}_k = \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - Q_{k+1}\tilde{H}_k\bmf{c}_k||_2^2$$
El cual sigue siendo un problema de mínimos cuadrados de dimensión $n \times k$ ($n$ ecuaciones con $k$ incógnitas), aunque todavía nos faltan un par de casos clave. Recordando que $\bmf{q}_1 = \frac{\bmf{b}}{||\bmf{b}||}$ podemos re-escribir conveniente el vector $\bmf{b}$ de la siguiente forma:
$$\begin{align}
\bmf{b} =&\ ||\bmf{b}||\bmf{q}_1 \\
=&\ ||\bmf{b}||Q_{k+1}\bmf{e}_1,
\end{align}$$
donde $\bmf{e}_1$ corresponde al primer vector canónico de dimensión $k + 1$ que solo contiene un 1 en su primera componente y un 0 en los demás. Reemplazando esto en la última expresión del problema de cuadrados obtenemos:
$$\begin{align}
	\overline{\bmf{c}}_k =&\ \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - Q_{k+1}\tilde{H}_k\bmf{c}_k||_2^2 \\
	=&\ \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\ ||\bmf{b}||Q_{k+1}\bmf{e}_1 - Q_{k+1}\tilde{H}_k\bmf{c}_k||_2^2 \\
	=&\ \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||Q_{k+1}(||\bmf{b}||\bmf{e}_1 - \tilde{H}_k\bmf{c}_k)||_2^2
\end{align}$$
De donde podemos derivar la siguiente identidad:
$$ \begin{aligned} 
	\| Q_{k+1} (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k) \|_2^2 &= (Q_{k+1} (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k))^T (Q_{k+1} (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k)) \\ 
	&= (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \mathbf{c}_k)^T \underbrace{Q_{k+1}^T Q_{k+1}}_{I_{k+1}} (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k) \\ &= (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k)^T I_{k+1} (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k) \\ 
	&= (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k)^T (\|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k) \\ 
	&= \|\ \|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k \|_2^2 
\end{aligned} $$
Este desarrollo finalmente nos permite obtener la siguiente identidad:
$$\begin{aligned}
	\overline{\bmf{c}}_k &= \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k} ||\bmf{b} - AQ_{k}\bmf{c}_k||_2^2 \\
	&= \|\ \|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k \|_2^2 
\end{aligned}$$
La cual nos indica que para obtener $\overline{\bmf{c}}_k$ podemos resolver el problema de mínimos cuadrados $\|\bmf{b} - AQ_{k}\bmf{c}_k\|_2^2$ de dimensiones $n \times k$, o el problema equivalente de mínimos cuadrados $\|\ \|\bmf{b}\| \bmf{e}_1 - \tilde{H}_k \bmf{c}_k \|_2^2$ de dimensiones $(k+1) \times k$. Por supuesto, es más rápido resolver este último, el cual posee la siguiente estructura:
$$\overline{\bmf{c}}_k = \argmin_{\tilde{\bmf{c}}_k \in \mathbb{R}^k}
\left|\left|
	\begin{bmatrix}
		||\bmf{b}|| \\
		0 \\
		0 \\
		\vdots \\
		\vdots \\
		0 \\
		0 
	\end{bmatrix}
	-
	\begin{bmatrix}
		h_{11} & h_{12} & \cdots & h_{1,k-1} & h_{1,k}   \\
		h_{21} & h_{22} & \cdots & h_{2,k-1} & h_{2,k}   \\
		0      & h_{32} & \ddots & h_{3,k-1} & h_{3,k}   \\
		\vdots & \ddots & \ddots & \ddots    & \vdots    \\
		0      & \ddots & \ddots & h_{k,k-1} & h_{k,k}   \\
		0      & \cdots & \cdots & 0         & h_{k+1,k} \\
	\end{bmatrix}
	\begin{bmatrix}
		c_1 \\
		c_2 \\
		c_3 \\
		\vdots \\
		c_{k-1} \\
		c_k
	\end{bmatrix}
\right|\right|_2^2$$
El cual su desarrollo puede traducirse en el siguiente algoritmo:

```python
x_0 = "initial guess"
r_0 = b - A * x_0
q[1] = r_0 / norm_2(r_0)
for k in range(1, m+1):
	y = A * q[k]
	for j in range(1, k+1):
		h[j][k] = Transpose(q[j]) * y
		y -= h[j][k]* q[j]
	h[k+1][k] = norm_2(y)
	if h[k+1][k] > 0:
		q[k+1] = y / h[k+1][k]
	c̅[k] = argmin(norm_2(module(r_0) * e_1 - H̃[k] * c[k]))
	x[k] = Q[k] * c̅[k] + x_0
	
```

Por supuesto, como probablemente habrán notado hay algunos cambios con respecto a las formulaciones que se hicieron originalmente al explicar el desarrollo de los GMRes:
- Finalmente se ha incluido el *"initial guess"* que les había mencionado a principios de este tema pero que prácticamente no formulé junto con el desarrollo matemático del algoritmo. SI uno quiere resolver un sistema de ecuaciones lineales $A\bmf{x} = \bmf{b}$ en donde ya se conoce algo de la solución dada por nuestro *initial guess*, entonces es posible re-escribir el sistema de ecuaciones de la siguiente manera:
$$\begin{aligned}
	A\bmf{x} &= \bmf{b} \\
	A(\bmf{y} + \bmf{x}_0) &= \bmf{b} \\
	A\bmf{y} &= \bmf{b} - \bmf{x}_0 \\
	A\bmf{y} &= \tilde{\bmf{b}}
\end{aligned}$$
  Lo que quiere decir que se modifica el lado derecho de forma conveniente. Esto nos da la oportunidad de "reiniciar" nuestro algoritmo de GMRes cuando nosotros lo requiramos. Por ejemplo, si nosotros nos estamos quedando sin memoria para almacenar los valores de las matrices $Q_{k+1}$ y $\tilde{H}_k$ que aumentan de tamaño dependiendo de las iteraciones $k$ entonces podemos aplicar el "reinicio" con el valor de aproximación obtenida en la última iteración realizada para así volver a generar estas 2 matrices con un tamaño reducido.

- En la línea 9 del algoritmo se obtiene el coeficiente $h_{k+1,k}$ y en la línea 10 se verifica se su valor sea mayor a 0. En realidad lo que se está haciendo es verificar que este valor sea distinto a 0, solo que como se trata de una norma vectorial en el fondo sabemos que este resultado no puede ser negativo. En el momento en el que se dé efectivamente que $h_{k+1,k} = 0$ ocurre el evento de *GMRes breakdown*, esto implica, solamente ya que estamos considerando que la matriz $A$ es no singular, que hay una solución exacta para el problema de minimización de la línea 12, por lo que se podría convertir nuestro problema de mínimos cuadrados de $(k+1) \times k$ en un problema de sistemas de ecuaciones lineales de $k \times k$, por lo que nuestro sistema tendrá una solución exacta, incluso reduciendo a 0 error de esta misma. 



 