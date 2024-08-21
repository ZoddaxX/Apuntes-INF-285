---

---
____
Sé lo que están pensando ahora mismo, ¿Por que te tomarías la molestia de hacer los desarrollos de los problemas de ayudantía si es que ya vienen con la pauta incluida? y la respuesta es bastante simple: me ayuda a estudiar. Intentar explicar este tipo de problemas me ayuda a saber hasta qué punto logro comprender teóricamente la materia que hemos visto, lo cual llega a ser un aspecto que toma mas relevancia de lo normal en este ramo de ~~Análisis Numérico~~ Computación Científica, por lo que trataré de explicar lo mejor posible los desarrollos de este tipo de ejercicios (siempre y cuando tenga tiempo...). También, recordar que es posible que me equivoque más de lo normal a la hora de hacer estos ejercicios, por lo que tómense estos desarrollos con un granito de sal (cualquier corrección a realizar es más que bienvenida). 
___
El ejercicio a resolver corresponde al propuesto en el archivo [[Ayudantía_Semana_2.pdf]], pueden abrirlo en una pestaña aparte para poder leer y entender que es lo que resolveré (por temas de tiempo no puedo tomarme mucho tiempo completando estos apuntes, por lo que me saltaré esos pequeños detalles jaja).

## A)
### 1)
Nos están dando como datos iniciales las siguientes afirmaciones:
$$\begin{aligned}
	\delta &= 0 \\
	x &\in \mathbb{N} \\
	x &> 0 \\
	g_0(x) &= 2^{-4x}
\end{aligned}$$
En resumidas cuentas, nos están pidiendo buscar el menor valor posible de $x$ tal que la expresión completa nos dé 0 en [[2- Estándar de Punto Flotante y Pérdida de Importancia#^aeafae|precisión doble]], donde la expresión que nos dan es la siguiente:
$$s - c = \left( \frac{2^x \left( 1+\sqrt{1+g_0(x)} \right) + 2^{-x}}{2} \right) - 2^x\sqrt{1+g_0(x)}$$
Reemplazando el valor de $g_0(x)$ obtenemos lo siguiente:
$$\left( \frac{2^x \left( 1+\sqrt{1+2^{-4x}} \right) + 2^{-x}}{2} \right) - 2^x\sqrt{1+2^{-4x}}$$
Ahora, como podrían haber intuido en este punto de la preguntan, NO nos están preguntando si es que esta expresión matemáticamente puede llegar a valer 0 para algún valor de $x > 0$, y  esto nos lo dejan claro recalcando el hecho de que tenemos que suponer el uso de [[2- Estándar de Punto Flotante y Pérdida de Importancia#^aeafae|precisión doble]], sino mas bien, como habremos visto en este punto del curso, este fenómeno ocurre gracias a un error que se puede derivar para algún valor de $x$ lo suficientemente grande. ¿Cómo podemos hacer esto? Recordemos que el número más grande que se puede representar con la precisión anteriormente mencionada corresponde a la siguiente:
$$+1.\underbrace{\boxed{1111\cdots1111}}_{\text{52 bits}} \times 2^{1023}$$
Para refrescarles la memoria con respecto a porque el exponente puede alcanzar este valor como máximo, recordemos que el *exponent bias* se calcula de la siguiente forma: $2^{bits\_exponente\ -\ 1}-1 = 2^{11-1}-1=1023$. Este valor corresponde el valor por el que vamos a "mover" el rango de valores que puede alcanzar nuestro exponente (esto es debido a que ninguno de los 11 bits del exponente ha sido asignado como un signo, por lo que este *exponent bias* nos permite alcanzar exponentes con valores decimales). El mayor número obtenible con un número de 11 bits corresponde al siguiente:
$$(11111111111)_2 = (2^{11}-1)_{10} = 2047$$
SIN EMBARGO, recordemos que hay un caso especial del número que se está representado cuando nuestro exponente está conformado de [[2- Estándar de Punto Flotante y Pérdida de Importancia#Caso Especial del Exponente 11111111111|solamente 1´s]], por lo que el verdadero valor que podemos usar para nuestro exponente es el siguiente:
$$(11111111110)_2 = (2^{11}-1-1)_{10} = 2046$$
Naturalmente, debido al *exponent bias* nuestro exponente real equivale a:
$$\text{Exponente} - \text{Bias} = 2046 - 1023 = 1023$$

Gracias al caso del exponente compuesto de [[2- Estándar de Punto Flotante y Pérdida de Importancia#Caso Especial del Exponente 00000000000|solamente 0´s]] podemos representar el 

