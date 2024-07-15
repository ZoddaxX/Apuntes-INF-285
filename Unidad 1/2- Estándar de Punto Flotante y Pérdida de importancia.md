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
$$S = a + ar + ar^2 + ar^3 + \ ...$$
Para la cual podemos multiplicar todo por la razón $r$:
$$rS = ar + ar^2 + ar^3 + ar^4 + \ ...$$
