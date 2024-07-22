Un correcto entendimiento del álgebra nos permitirá entender de forma matemática la aplicación correcta de diversos algoritmos que se verán a lo largo del curso en diferentes contextos que los requieran.
Las estructuras básicas con las que se trabaja en el álgebra son los vectores y matrices. Un vector columna posee la siguiente forma:
$$\bm{u} = \begin{bmatrix} u_{1} \\ \vdots \\ u_{n} \\ \end{bmatrix} \in \mathbb{R}^n$$El cual puede transformarse a un vector fila ocupando la operación traspuesta $^T$, es decir, $\bm{u}^T=\begin{bmatrix} a_{1}, & \cdots &, a_{n}\end{bmatrix}$. Es muy importante entender en qué momento usar qué tipo de vector al realizar operaciones matemáticas, ya que muchas veces se buscan expresiones que sean compatibles teóricamente hablando, por ejemplo, cuando se busca el producto interno entre 2 vectores $\bm{u}$ y $\bm{v}$ es necesario que ambos posean las mismas dimensiones, por ende ambos tienen que ser o bien vectores fila o vectores columna que pertenezcan al mismo $\mathbb{R}^n$ (en caso contrario, tendríamos que considerar realizar una transposición al alguno de los vectores si es que pertenecen al mismo $\mathbb{R}^n$).

Finalmente, podemos definir a una matriz $A\in \mathbb{R}^{m\times n}$ como un arreglo bidimensional de números de la siguiente forma:

$$ A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} $$Donde se denota a $A_{ij}$ el elemento de la i-ésima fila y la j-ésima columna de la matriz $A$, el cual también es posible denominarla como $a_{ij}$.

## Producto matriz-vector y matriz-matriz
 
Consideremos el siguiente producto matriz-vector entre la matriz $A\in\mathbb{R}^{m\times n}$ y el vector $\bm{u}\in\mathbb{R}^n$: ^c56fc2
$$
A\bm{u} = 
\begin{bmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{bmatrix}

\begin{bmatrix} 
u_{1} \\ 
u_{2} \\
\vdots \\ 
u_{n} \\ 
\end{bmatrix}

=

\begin{bmatrix}
a_{11}*u_1 + a_{12}*u_2 + \cdots + a_{1n}*u_n\\
\vdots \\
a_{m1}*u_1 + a_{m2}*u_2 + \cdots + a_{mn}*u_n
\end{bmatrix}
$$
Podemos notar que en este caso el valor de $m$ no es relevante para que el producto entre $A$ y $\bm{u}$ sea compatible (por supuesto, siempre siendo $m\geq 1$), sino que simplemente nos indica la cantidad de filas que compondrán el resultado final. Distinto seria el caso en el que $\bm{u}\in\mathbb{R}^m$ y este sea un vector fila, ya que $m$ pasaría a ser relevante para la compatibilidad de la operación.

Ahora, también es posible que nosotros interpretemos al vector $A$ como una serie de vectores columna:
$$A = 
\begin{bmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{bmatrix}
=
\begin{array}{c|c|c|c}
\bm{[}\ \bm{a}_{1} & \bm{a}_2 & \cdots & \bm{a}_n\ \bm{]}, 
\end{array}
$$
Donde $\bm{a}_k = \begin{bmatrix} \bm{a}_{1k} \\ \vdots \\ \bm{a}_{mk} \end{bmatrix}$. De esta forma es posible interpretar el matriz-vector como:
$$A\bm{u} = u_1\bm{a}_1 + u_2\bm{a}_2 + \cdots + u_n\bm{a}_n = \sum_{k=1} ^n u_k\bm{a}_k$$
Esto implica que es posible interpretar este producto como una [combinación lineal] de las columnas de $A$ sobre los coeficientes de $\bm{u}$. Esto es interesante ya que nos permite algoritmizar de manera sencilla este procedimiento con las librerías necesarias.


De forma similar podemos implementar el producto matriz-matriz entre 2 matrices $A\in\mathbb{R}^{m\times n}$ y $B\in\mathbb{R}^{n\times l}$ como:
$$
AB =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{bmatrix}

\begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1l} \\ 
b_{21} & b_{22} & \cdots & b_{2l} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
b_{n1} & b_{n2} & \cdots & b_{nl} 
\end{bmatrix}
=
$$

$$\begin{bmatrix}
a_{11}*b_{11} + a_{12}*b_{21} + \cdots + a_{1n}b_{n1} & a_{11}*b_{12} + a_{12}*b_{22} + \cdots + a_{1n}b_{n2} & \cdots & a_{11}*b_{1l} + a_{12}*b_{2l} + \cdots + a_{1n}b_{nl} \\ 
a_{21}*b_{11} + a_{22}*b_{21} + \cdots + a_{2n}b_{n1} & a_{21}*b_{12} + a_{22}*b_{22} + \cdots + a_{2n}b_{n2} & \cdots & a_{21}*b_{1l} + a_{22}*b_{2l} + \cdots + a_{2n}b_{nl}\\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1}*b_{11} + a_{m2}*b_{21} + \cdots + a_{mn}b_{n1} & a_{m1}*b_{12} + a_{m2}*b_{22} + \cdots + a_{mn}b_{n2} & \cdots & a_{m1}*b_{1l} + a_{m2}*b_{2l} + \cdots + a_{mn}b_{nl} 
\end{bmatrix}$$

Y antes de que me odien por poner la notación más bruta que hayan podido ver hasta ahora en estos apuntes, aquí les paso el mismo resultado en formato de vectores columna como en el caso anterior:
$$AB = 
\begin{array}{c|c|c|c}
\bm{[}\bm{a}_{1} & \bm{a}_2 & \cdots & \bm{a}_n \bm{]} 
\end{array}

\begin{array}{c|c|c|c}
\bm{[}\bm{b}_{1} & \bm{b}_2 & \cdots & \bm{b}_i & \cdots & \bm{b}_l \bm{]} 
\end{array}
= C\in\mathbb{R}^{m\times l}
$$
Todos esto por supuesto nos dice que el vector resultante entre el producto de los vectores $A$ y $B$ es de dimensiones $m\times l$ y que $n$ solo nos indica la cantidad de operadores suma a calcular para cada $c_{ij}$. Para computar de manera sencilla esta matriz $C$, podemos establecer una formula para calcular todos los vectores columna $\bm{c}_i$:
$$\bm{c}_i = \sum_{k=1} ^n b_{k,i}\bm{a}_k = A\bm{b}_i$$
Donde $i\in\{1,2,3,...,l\}$ y $b_{i,k}$ es el k-ésimo elemento del vector columna $\bm{b}_i$. En pocas palabras, es posible expresar de forma sencilla el producto entre estos 2 vectores como una sucesión de productos [[1- Breve Introducción al Álgebra Lineal#^c56fc2|matriz-vector]], donde se multiplica la matriz $A$ con todas las columnas $\bm{b}_i$.

## Espacios Vectoriales y Aplicaciones Lineales
### Espacio Vectorial

Un espacio vectorial es un conjunto $V$ no vacío de vectores en el cual están definidas las operaciones de adición y multiplicación por escalar. Sean $u$, $v$, $w$ todos los vectores pertenecientes a $V$ y para todos los escalares $c$ y $d$ se deben cumplir los siguientes axiomas para que $V$ efectivamente sea un espacio vectorial:
- El vector resultante de $u + v$ tiene que estar en $V$.
- Existe conmutatividad en $u+v$, o sea, $u+v = v+u$.
- Existe asociatividad en la suma, es decir, $(u+v)+w = u+(v+w)$.
- Existe un vector nulo $0$ en $V$ tal que $u + 0 = u$.
- Para cada $u$ en $V$, existe un vector $-u$ en $V$ tal que $u + (-u) = 0$.
- El múltiplo escalar $u * c$ está en $V$.
- Existe distributividad en la multiplicación, o sea, $c(u+v) = cu + cv$.
- Debe aplicarse que $c(du) = (cd)u$.
- Debe aplicarse que $1u = u$.

### Subespacio Vectorial

Un subespacio vectorial $H$ de un espacio vectorial $V$ además de ser un subconjunto de $V$ posee 3 características nuevas:
- El vector nulo de $V$ está en $H$.
- $H$ es cerrado para la adición, es decir, para cualquier par de vectores $u$ y $v$ que estén en $H$ se cumple que $u + v$ pertenezca también a $H$.
- $H$ es cerrado para la multiplicación escalar, es decir para cualquier vector $u$ y escalar $c$ se cumple que $c*u$ pertenece a $H$.

Por ejemplo, tomemos la siguiente figura:
![[Apuntes_INF-285_2024-v0613.pdf#page=13&rect=166,417,438,595|Apuntes_INF-285_2024-v0613, p.12]]

Aquí se está representando un subespacio vectorial del espacio vectorial $\mathbb{R}^3$ conformado por los vectores $u = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ y $v = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$, esto quiere decir que este subespacio son todos los valores que puedan ser obtenidos a través de la combinación lineal entre ambos vectores:
$$H=
\left\{
	a 
	\begin{bmatrix}
		1 \\
		0 \\
		1  
	\end{bmatrix}
	+ b
	\begin{bmatrix}
		0 \\
		1 \\
		1  
	\end{bmatrix}
	\;\middle|\;
	a,b\in\mathbb{R}
\right\}
=
\text{Span}\left(
	\begin{bmatrix}
		1 \\
		0 \\
		1  
	\end{bmatrix}
	,
	\begin{bmatrix}
		0 \\
		1 \\
		1  
	\end{bmatrix}
\right)$$
Donde podemos apreciar que esta expresión corresponde a la definición de $\text{Span}$.

### Cambio de Base

Definimos a la base canónica tal como una serie de vectores por los cuales se puede llegar a representar cualquier vector de un espacio vectorial mediante una combinación lineal de estos vectores canónicos. Por ejemplo, para un espacio vectorial $V$ equivalente a $\mathbb{R}^3$ tenemos que su base canónica corresponde a:
$$\bm{e}_1 = 
\begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix}
,\ \bm{e}_2 =
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix}
,\ \bm{e}_3 =
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$
También es posible tener una base canónica para los espacios de funciones, por ejemplo, la base canónica de los espacios vectoriales de la forma $\mathbb{P}^n$ posee la forma:
$$p(x) = a_0 + a_1x + a_2x^2+\cdots+a_nx^n$$

Ahora, hacer un cambio de base simplemente involucra determinar las coordenadas de un vector como una combinación lineal de un conjunto de vectores que idealmente sean linealmente independientes.

Tomemos como ejemplo el vector $\begin{bmatrix} 4 \\ 3 \end{bmatrix}$ en la siguiente figura: 

![[Apuntes_INF-285_2024-v0613.pdf#page=14&rect=196,549,418,716|Apuntes_INF-285_2024-v0613, p.13]]

Podemos apreciar en la imagen que las líneas rojas corresponden a una transformación lineal que involucran a la base canónica de $\mathbb{R}^2$, donde tenemos:
$$\left\{
	a 
	\begin{bmatrix}
		1 \\
		0  
	\end{bmatrix}
	+ b
	\begin{bmatrix}
		0 \\
		1  
	\end{bmatrix}
	\;\middle|\;
	a,b\in\mathbb{R}
\right\}
=
\begin{bmatrix}
	4\\
	3
\end{bmatrix}
$$
de donde obtenemos el siguiente sistema de ecuaciones:
$$ \begin{align}
a * 1 + b * 0 &= 4 \\ 
a * 0 + b * 1 &= 3 
\end{align} $$
Es fácil notar que las soluciones corresponden a $a = 4$  y $b = 3$, por lo que el cambio de base de nuestro vector objetivo en función de la base canónica del espacio vectorial en el que estamos es:  $$\left\{
	a 
	\begin{bmatrix}
		1 \\
		0  
	\end{bmatrix}
	+ b
	\begin{bmatrix}
		0 \\
		1  
	\end{bmatrix}
	\;\middle|\;
	a = 4,\ b = 3
\right\}
=
\begin{bmatrix}
	4\\
	3
\end{bmatrix}
$$Como podrán haber intuido en este punto, las líneas verdes y azul corresponden a cambios de base diferentes a la base canónica, y para poder obtenerlas podemos generalizar las bases a utilizar de esta forma:
$$\bm{u} = 
\begin{bmatrix}
u_1 \\
u_2
\end{bmatrix}
,\ \bm{v}=
\begin{bmatrix}
v_1 \\
v_2
\end{bmatrix}$$
donde podemos establecer una combinación lineal para el cambio de base:
$$\alpha\bm{u} + \beta\bm{v} = 
\alpha
\begin{bmatrix}
u_1 \\
u_2
\end{bmatrix}
+\beta
\begin{bmatrix}
v_1 \\
v_2
\end{bmatrix}
=
\begin{bmatrix}
4 \\
3
\end{bmatrix}$$
El cual se puede representar como un sistema de ecuaciones: ^af436c
$$ \underbrace{\begin{bmatrix} 
u_1 & v_1 \\ 
u_2 & v_2 
\end{bmatrix}}_{A}
\begin{bmatrix} 
\alpha \\ 
\beta
\end{bmatrix} 
= 
\underbrace{\begin{bmatrix} 
4 \\ 3 
\end{bmatrix}}_{\bm{b}} $$
Para este caso, el problema se convirtió en un sistema de ecuaciones lineales, el cual se resuelve de la forma:
$$A\bm{x} = \bm{b} \implies \bm{x}=A^{-1}\bm{b}$$
Donde $A^{-1}$ corresponde a la matriz inversa de $A$.

## Propiedades de las Matrices y Operadores Importantes
### Column Space, Row Space y Rank
- <u>Column Space</u>: Es el espacio generado por los vectores columna de una matriz, lo que coloquialmente hablando corresponde a la cantidad de columnas que posee una matriz, o matemáticamente hablando equivale a $\text{Range}(A)$.
- <u>Column Rank</u>: Corresponde a la dimensión del Column Space, es decir, equivale a la cantidad de columnas de una matriz que sean linealmente independientes entre sí.
- <u>Row Space</u>: Es el espacio generado por los vectores fila de una matriz, lo que coloquialmente hablando corresponde a la cantidad de filas que posee una matriz, o matemáticamente hablando equivale a $\text{Range}(A^T)$.
- <u>Row Rank</u>: Corresponde a la dimensión del Row Space, es decir, equivale a la cantidad de filas de una matriz que sean linealmente independientes entre sí.

Es bueno destacar que se cumplen para todas las matrices que sus Row Rank son el mismo que sus Column Rank, por lo que a partir de aquí me voy a referir a uno o al otro como *Rank*.

### Full Rank
A una matriz $A \in \mathbb{R}^{m \times n}$ se le denomina *Full Rank* si es que posee la mayor cantidad de Rank posible, el cual corresponde al mínimo entre sus dimensiones $m$ y $n$.
Por ejemplo, consideremos la siguiente matriz rectangular de dimensiones $2 \times 3$:
$$A = 
\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6
\end{bmatrix}$$
La mayor cantidad de Rank posible de obtener para esta matriz es de $\min(2,3) = 2$, sin embargo, notemos que la primera fila no es linealmente independiente de la segunda fila, debido a que si multiplicamos todos los valores de la primera fila por 2 obtendremos los mismos valores de la segunda fila, esto significa que el Rank de la matriz $A$ es de 1, y como $1 \neq 2$ entonces efectivamente esta matriz no es *Full Rank*.

### Inversa
Una matriz posee inversa si y solo si es cuadrada (o sea, es de dimensiones $n \times n$) y además es *Full Rank*. Esto significa que existe una matriz $Z$ que cumple la siguiente ecuación:
$$AZ = ZA = \underbrace{I}_{\text{Matriz Identidad}} =
\begin{bmatrix}
1      &      0 & \cdots & 0      & 0      \\
0      &      1 & \ddots & \vdots & \vdots \\
0      &      0 & \ddots & 0      & 0      \\
\vdots & \vdots & \ddots & 1      & 0      \\
0      &      0 & \cdots & 0      & 1      \\
\end{bmatrix}
$$
Donde $Z$ correspondería a la inversa de $A$.

### Determinante
El determinante corresponde a un escalar obtenible de una matriz $A \in \mathbb{R}^{n \times n}$ (es decir, tiene que ser una matriz cuadrada) la cual se puede calcular de la siguiente forma:
$$\text{det}(A) = \sum_{j\ =\ 1}^{n} (-1)^{i+j}A_{i,j}\text{det}(A_{|i|,|j|})$$
La cual cumple con las siguientes propiedades:
- $\text{det}(A^{-1}) = \frac{1}{\text{det}(A)}$.
- $\text{det}(AB) = \text{det}(A)\text{det}(B)$ donde $B \in \mathbb{R}^{n \times n}$.
- $\text{det}(\alpha A) = \alpha^n \text{det}(A)$, donde $\alpha$ corresponde a un escalar.
- $\text{det}(A^T) = \text{det}(A)$, donde $^T$ es el operador transpuesta.
- $\text{det}(A) = \prod_{i = 1}^{n}\lambda_i$, donde $\lambda_i$ para $i \in \{1,2,\cdots,n\}$ son los valores propios de $A$.

## Matrices Particulares
### Matriz Identidad
Esta matriz $I \in \mathbb{R}^{n \times n}$ es una matriz en la que todos los coeficientes de ella son 0, menos los elementos de su diagonal principal, los cuales son solamente 1´s.
$$I = 
\begin{bmatrix}
1      &      0 & \cdots & 0      & 0      \\
0      &      1 & \ddots & \vdots & \vdots \\
0      &      0 & \ddots & 0      & 0      \\
\vdots & \vdots & \ddots & 1      & 0      \\
0      &      0 & \cdots & 0      & 1      \\
\end{bmatrix}$$

### Matrices Triangulares
Una matriz triangular es un tipo de matriz tal que sus coeficientes son todos ceros debajo de su diagonal principal si es que se trata de una matriz triangular superior, y sus coeficientes son todos ceros arriba de su diagonal principal si es que se trata de una matriz triangular inferior.

Una matriz triangular superior se vería así:
$$\begin{bmatrix}
u_{11} & u_{12} & \cdots & \cdots      & u_{1n}    \\
0      & u_{22} & \cdots & \cdots      & u_{2n}    \\
\vdots & 0      & \ddots &             & \vdots    \\
\vdots & \vdots & \ddots & u_{n-1,n-1} & u_{n-1,n} \\
0      & \cdots & \cdots & 0           & u_{nn}
\end{bmatrix}$$
Mientras que una triangular inferior se vería así:
$$\begin{bmatrix}
u_{11} & 0      & \cdots & \cdots      & 0         \\
u_{21} & u_{22} & \cdots & \cdots      & \vdots    \\
\vdots & \vdots & \ddots &             & \vdots    \\
\vdots & \vdots & \ddots & u_{n-1,n-1} & 0         \\
u_{n1} & u_{n2} & \cdots & u_{n, n-1}  & u_{nn}
\end{bmatrix}$$

Cabe destacar que si es posible que alguno de los coeficientes $u_{i,j}$ de estas 2 matrices sean 0. 