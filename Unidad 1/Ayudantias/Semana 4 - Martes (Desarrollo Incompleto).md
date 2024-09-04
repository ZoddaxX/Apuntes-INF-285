El ejercicio a (intentar) resolver esta vez corresponde al adjunto en el archivo [[Ayudantía_Semana_4_Martes.pdf]]. Al igual que mi (intento) de explicar la solución de la ayudantía 2 del día Martes voy a pasar directamente a resolver las preguntas propuestas de esta semana.

# 1.
## a)
Recordemos primero que para aplicar el método de bisección se nos pide tener una función $f(x)$ tal que se cumpla:
$$f(x) = 0$$
es decir, la función tiene que formar parte directa de un problema de búsqueda de raíces. Sin embargo, la función que tenemos entre manos es la siguiente:
$$f(x,y) = x + y\sin\left(\log(y^2 + 1) - y\right) = 1$$
Aunque el problema nos dice que nosotros podemos asumir que ya conocemos el valor de $x$ aún tenemos que trabajar un poco más para que quede de la forma deseada. Haciendo una pequeña resta a ambos lados obtenemos:
$$x + y\sin\left(\log(y^2 + 1) - y\right) - 1 = 0$$
Aunque claro, a nuestro algoritmo todavía le falta algo esencial, necesitamos un intervalo de búsqueda inicial \[$a$, $b$\] para poder ingresar como parámetro dentro del algoritmo (o quizás como un valor fijo, pero de todas formas son importantes). Algo muy importante a tomar en cuenta a la hora de hacer este paso es que tenemos que analizar la posibilidad de que pueda existir más de una raíz dentro de algún intervalo que nosotros indiquemos, debido a que el algoritmo de bisección posee un comportamiento indefinido cuando se encuentra más de una raíz en un intervalo (este comportamiento puede provocar que el algoritmo se aproxime a una raíz distinta a la que estemos buscando o que directamente no converja en ningún punto), y de hecho es posible intuir que este va a ser el caso debido al comportamiento oscilatorio sobre el eje $y = 0$ de la función $\sin$. 

Asumiendo que no podemos usar herramientas de computación científica para poder graficar esta función (ya sea Matlab, Wólfram, etc...) para obtener una aproximación visual de la ubicación de esta raíz, no nos queda mejor opción que diseñar un algoritmo que nos permita estimar estos intervalos. Ahora, ¿Cómo lo podemos hacer? de forma greedy basta con evaluar la función entre ciertos intervalos lo suficientemente pequeños desde un punto de inicio y evaluar la función entre estos puntos hasta haber identificado un cambio de signo tal que se cumpla la condición $f(a)f(b) < 0$. Y esto lo podemos hacer de la siguiente manera:

```python

x = "Valor de x" # Aquí debiera insertarse el valor numérico requerido de x
f = lambda x,y: x + y * np.sin(np.log(np.power(y,2.) + 1) - y) - 1 
y_0 = 0
incremento = 0.1 # Este incremento es recomendable que tenga un valor lo suficientemente pequeño para evitar meter por accidente una segunda raíz dentro del intervalo que vamos a sacar

def BusquedaDeIntervalos(x, f, y_0, incremento)
	esPositivo = False
	esNegativo = False
	y = y_0
	
	while not esPositivo and not esNegativo:
		fxy = f(x,z)
		if not esPositivo and fxy > 0:
			esPositivo = True
			a = y
		elif not esNegativo and fxy < 0:
			esNegativo = True
			b = y
		y += incremento

	return a,b
		
```

En efecto, lo único que se hizo en este algoritmo greedy es evaluar nuestra función chanchamente en ciertas particiones de un $y_0$ inicial con un incremento dado. Es decir, en el fondo estamos discretizando un intervalo de búsqueda para evaluar nuestra función con el fin de determinar donde devuelve un valor positivo y cuando devuelve un valor negativo. En el ejemplo del código puse que iba a partir a evaluar la función en el punto $y = 0$ e iba a ir incrementando su valor por $0.1$ para cada iteración, o sea, voy a evaluar la función en los puntos $\{0,0.1,0.2,0.3\cdots\}$ hasta que encuentre 2 puntos en los que la función $f$ entregue 1 valor positivo (que corresponde al valor de $a$ en este caso) y un valor negativo (que corresponde al valor de $b$). 

Finalmente, nos queda determinar los parámetros que debiera recibir nuestro algoritmo final. Estos deben consistir en:
- La nueva función $f(x)$ sobre la que vamos a hacer la búsqueda.
- Nuestro intervalo \[$a$, $b$\] obtenido con el algoritmo anterior.
- Un índice de tolerancia para decidir cuando detener nuestro algoritmo (importante que no se les olvide poner esto, o sino el algoritmo no va a terminar nunca) (esto último aplica para cualquier método iterativo que veamos en el curso).

Y de lo demás ya se va a encargar el algoritmo de bisección mismo.

## b)
