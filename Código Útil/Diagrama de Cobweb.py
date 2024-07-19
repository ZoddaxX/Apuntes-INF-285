import matplotlib.pyplot as plt
import numpy as np

# Modo oscuro yay!
plt.style.use('dark_background')

# Define la función iterativa g(x)
def g(x):
    return -(1/2) * x + (3/2)

# Define la función identidad y=x
def identity(x):
    return x

# Función para plotear el diagrama de cobweb
def cobweb_plot(f, x0, n):
    x = np.linspace(0, 1, 400)
    y = f(x)
    plt.plot(x, y, label='$g(x)$')
    plt.plot(x, identity(x), label='$y=x$')

    # Dibujar las primeras n iteraciones del diagrama de cobweb
    x_old = x0
    for i in range(n):
        x_new = f(x_old)
        plt.plot([x_old, x_old], [x_old, x_new], 'r', lw=1)
        plt.plot([x_old, x_new], [x_new, x_new], 'r', lw=1)
        plt.arrow(x_old, x_old, 0, (x_new - x_old)/2, head_width=haw, head_length=hal, fc='r', ec='r')
        plt.arrow(x_old, x_new, (x_new - x_old)/2, 0, head_width=haw, head_length=hal, fc='r', ec='r')
        plt.arrow(x_old, x_new, 0, (x_old - x_new)/2, head_width=0, head_length=0, fc='r', ec='r')
        plt.arrow(x_new, x_new, (x_old - x_new)/2, 0, head_width=0, head_length=0, fc='r', ec='r')
        x_old = x_new

    plt.xlabel('$x$')
    plt.ylabel('$g(x)$')
    plt.title('Diagrama de Cobweb')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parámetros iniciales
x0 = 2.7  # Cambia esto según el valor inicial que desees
n = 6  # Número de iteraciones
haw = 0.04 # Ancho de la cabeza de la flecha
hal = 0.04 # Largo de la cabeza de la flecha

cobweb_plot(g, x0, n)