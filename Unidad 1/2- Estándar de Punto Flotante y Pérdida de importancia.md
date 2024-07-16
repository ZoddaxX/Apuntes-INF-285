---
cssclasses:
  - t-c
---

## De Decimal a Binario

Los números binarios con decimales se representan de la forma:
$$(B)_2 =\ ...b_2b_1b_0.b_{-1}b_{-1}b_{-3}...$$Donde cada $b_i$ corresponde al i-ésimo bit de algún número en binario $B$.

Para transformar números de binario a base 10 se puede utilizar la siguiente fórmula:
$$((B)_2)_{10}=\sum_{-\infty} ^{\infty} b_i2^i$$Supongamos ahora que nos interesa transformar un número de binario a decimal:
$$(B)_2 = (1101)_2 = (1*2^0 + 0*2^1 + 1*2^2 + 1*2^3)_{10} = (13)_{10}$$

Para números con decimales es la misma historia:
$$(B)_2 = (101.001)_2 = (1*2^{-3} + 0*2^{-2} + 0*2^{-1} + 1*2^0 + 0*2^1 + 1*2^2)_{10} = (5.125)_{10}$$


Ahora, ¿Qué pasa con los valores en binario que son periódicos?
$$(B)_2 = (0.\overline{10})_2$$Intentemos aplicar la fórmula mencionada anteriormente para transformar el valor a decimal:
$$(0.\overline{10})_2 = (1*2^{-1} + 0*2^{-2} + 1*2^{-3} + 0*2^{-4} +\ ...)_{10}$$Podemos visualizar mejor el resultado si transformamos todo a su forma fraccionaria:
$$(0.\overline{10})_2 = \frac{1}{2^1} + \frac{0}{2^2} + \frac{1}{2^3} + \frac{0}{2^4} +\ ...\ = \frac{1}{2^1} + \frac{1}{2^3} + \frac{1}{2^5} +\ ...$$Aquí es evidente que estamos ante una serie geométrica con solución de la forma $S_n = a\frac{1-r^n}{1-r}$, donde $S_n$ es la n-ésima solución de la serie, $a$ es el primer término de la serie y $r$ es la razón común por la que varia la sumatoria. Sin embargo, nuestra n en este caso tiende a infinito, por lo que tenemos que desarrollar más esta fórmula para determinar si es que la solución va a converger en algún punto. 
Definiendo $|r| < 1$, supongamos que tenemos una serie geométrica cualquiera:
$$S = a + ar + ar^2 + ar^3 + \ ... \tag{1}$$
Para la cual podemos multiplicar todo por la razón $r$:
$$rS = ar + ar^2 + ar^3 + ar^4 + \ ... \tag{2}$$
Restando la ecuación 1 con 2:
$$S - rS = a \implies S = \frac{a}{1-r}$$
Dicho procedimiento es únicamente posible en el caso de que $|r| < 1$, esto es debido a que de lo contrario la sucesión infinita $ar^i$ no convergería en ningún punto, por lo que no seria posible hacer la resta de las ecuaciones. Y con esto hecho ya tenemos una expresión para la serie geométrica cuando $n$ tiende a infinito.
Notamos que la razón $r$ de la serie que obtuvimos anteriormente equivale a $\frac{1}{2^2}$ y con primer termino $a = \frac{1}{2^1}$, por lo que reemplazando estos valores en la ecuación anterior obtenida tenemos que:
$$S = \frac{\frac{1}{2}}{1-\frac{1}{2^2}} = \frac{2}{3}$$
Por lo tanto, el valor en decimal del número $(0.\overline{10})_2$ equivale a $(\frac{2}{3})_{10}$.

## Estándar de Punto Flotante

^14987e

En este curso se utilizará el *estándar de punto flotante IEEE 754*, el cual de forma simplista podemos denominarla como la forma de escribir en notación científica los números binarios.
La estructura que suele regir este estándar es la siguiente:
$$\underbrace{\pm}_{Signo}\ \underbrace{1}_{Siempre\ 1}.\underbrace{bbbbb\cdots}_{Mantisa}\ *2^{p\ \rightarrow\ Exponente}$$
Este tipo de estructura también se le denomina **normalizada** o bien **justificada a la izquierda**.
Por ejemplo, la forma justificada del número $9.5$ es:
$$(9.5)_{10} = (1001.1)_2 = +1.0011*2^3$$
Dependiendo del tipo de precisión usada vamos a usar más o menos memoria en bits:

| **Precisión** | **Signo** | **Exponente** | **Mantisa** | **Total** |
|:------------- | --------- | ------------- | ----------- | --------- |
| Single        | 1         | 8             | 23          | 32        |
| **Double**    | 1         | 11            | 52          | 64        |
| Long Double   | 1         | 15            | 64          | 80        |

^aeafae

Durante el transcurso del curso se utilizará de referencia la precisión doble de punto flotante a menos que se llegue a decir lo contrario.

### Machine Épsilon
El número machine épsilon, expresado como $\epsilon_{mach}$, consiste en el número más pequeño representable por un tipo de precisión que suceda al número 1, o sea, corresponde al menor número representable que sea mayor a uno. Por ejemplo, para precisión doble tenemos que su machine épsilon es de:
$$\epsilon_{mach} = 2^{-52} \approx 2*10^{-16}$$
Visualicemos mejor como es que se llegó a obtener este resultado:
$$1 = +1.000000\cdots000000\ *\ 2^0$$
$$1+2^{-52}=+1.000000\cdots000001\ *\ 2^0$$
Por lo que efectivamente $2^{-52}$ es el valor machine épsilon de la precisión doble de punto flotante.

## Pérdida de Precisión y Regla del más Cercano (Nearest Rule)

Muchas veces a la hora de computar valores con una gran cantidad de decimales ocurre que el tipo de precisión usada no posee la suficiente cantidad de bits para poder representar un número en su totalidad, es por esto que el estándar [[2- Estándar de Punto Flotante y Pérdida de Importancia#^14987e|IEEE]] posee una regla de redondeo para poder aproximar de la mejor forma posible el número que se buscar representar.
Tomemos por ejemplo el siguiente número que se quiere representar con precisión doble:
$$9.4 = (1001.\overline{0110})_2 = +1.\underbrace{\boxed{001010110\cdots011001100}}_{Mantisa}110\cdots*2^3$$
El estándar nos dice que tenemos que seguir 2 pasos para transformar el número a su forma representable para *x* precisión:
- Chopping: Se deben cortar todos los bits que vengan después al tamaño soportado por la mantisa.
- Rounding: Existen 3 casos que se deben estudiar para determinar de qué forma uno debe redondear la mantisa.
	- Si el bit que viene después del último bit de la mantisa es 1, a este último bit se le suma 1. Por ejemplo, en precisión doble el último bit de la mantisa es el 52, por lo que si el bit 53 del número al cual se le hizo chopping equivale a 1 entonces al bit 52 de la mantisa se le suma 1.
	- Si el bit que viene después del último bit de la mantisa es 0, entonces no hay que sumarle 1 al último bit de la mantisa.
	- Como caso particular, si es que sabemos que todos los bits a la derecha del bit que viene después del último bit de la mantisa son 0, y este bit es 1, entonces vamos a sumar 1 al último bit de la mantisa si y solo si este bit también es 1. Por ejemplo: $+1.\boxed{00000\cdots00001}1000\cdots\ *\ 2^0$, debido a que el último bit de la mantisa es 1, el bit que viene después de la mantisa también es 1 y todos los bits que suceden a este último son 0, entonces se tiene que sumar 1 al último bit de la mantisa  

Siguiendo estas reglas, tenemos que al último bit de la mantisa tenemos que sumarle 1 debido a que el bit que le sucede a este también es 1, además de que no todos los bits que le suceden son 0 ni el último bit de la mantisa es 1, por lo que el número queda como:
$$fl(9.4) =+1.001010110\cdots011001101\ * \ 2^3 = 9.4+0.2*2^{-49}$$
donde $fl(x)$ corresponde al número realmente almacenado luego de aplicar esta regla de aproximación a un número $x$.

## Error de aproximación

Como muchos habrán notado en el punto anterior, el tener que aproximar un valor para calzarlo con la precisión usada implica que varias veces no podremos almacenar un número completo dentro de una computadora, es por eso que pueden nacer ciertos errores de cálculo a la hora de resolver ciertos problemas de forma computarizada.

Definimos al error absoluto como el valor matemático perdido a la hora de hacer una aproximación de un número. Este error viene dado por:
$$Error\ absoluto=|fl(x)-x|$$
Por otro lado, el error relativo es definido como la relación que hay entre el error absoluto del número que se almacenó y el número real que se intentó almacenar, es decir, este error es relativo al tamaño del mismo número que se busca representar. Este tipo de error viene dado por:
$$Error\ relativo=\frac{Error\ absoluto}{|x|}=\frac{|fl(x)-x|}{|x|}$$
Ahora, dentro del contexto de los modelos de precisión [[2- Estándar de Punto Flotante y Pérdida de Importancia#^14987e|IEEE]] se cumple la siguiente propiedad:
$$Error\ relativo \leq \frac{1}{2}\epsilon_{mach}$$
$$\frac{|fl(x)-x|}{|x|} \leq \frac{1}{2}\epsilon_{mach} \implies |fl(x) - x| \leq \frac{1}{2}\epsilon_{mach}|x|$$
Esto quiere decir que el error obtenido al representar un número en este estándar es proporcional al tamaño original del número.

## Representación de Máquina

Hasta ahora hemos abordado la forma en la que se maneja la mantisa a nivel computacional, por lo que toca ver que es lo que sucede con el exponente y el signo para terminar de comprender como es que se almacena un número real en un computador.

Todavía enfocándonos en la estructura de [[2- Estándar de Punto Flotante y Pérdida de Importancia#^aeafae|precisión de punto flotante doble]], esta estructura representada en decimal sigue esta estructura:
$$\underbrace{0}_{Signo\ s}\ \ \ \ \underbrace{00000000000}_{Exponente\ e\ (11\ bits)}\underbrace{0000000000\cdots0000000}_{Mantisa\ m\ (52\ bits)}$$
donde el signo $s$ significa:
$$s = \begin{cases} 0 & \text{si el número es positivo}\\ 1 & \text{si el número es negativo} \end{cases} $$
El exponente $e$ en comparación al signo $s$ necesita una explicación un tanto más detallada:
- Al estar compuesto de 11 bits, se pueden representar $2^{11} = 2048$ números, los cuales corresponden a los números enteros pertenecientes al conjunto \[-1022, 1023]. Ahora mismo se estarán preguntando porque solo se representa el conjunto anterior compuesto de 2046 números en vez de los 2048 números que se pueden representar con 11 bits, esto se va a explicar en alguno de los siguientes incisos.
- Para poder obtener tanto exponentes positivos como negativos sin tener que representar el número en complemento 2 y tener que sacrificar un bit para representar el signo, se introdujo un *exponente sesgado* o *exponent bias* que servirá para calcular el exponente real. Para la precisión actual este valor equivale a $2^{bits\_exponente\ -\ 1}-1 = 2^{11-1}-1=1023$. Por lo tanto, el exponente real representado en el estándar se calcula como: $Exponente-bias=Exponente-1023$.
- 