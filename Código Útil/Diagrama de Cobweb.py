import matplotlib.pyplot as plt
import numpy as np

# Modo oscuro yay!
plt.style.use('dark_background')

# Define la función iterativa g(x)
def g(x):
    return -(3/2) * x + (5/2)

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
        plt.plot([x_old, x_old], [x_old, x_new], 'k', lw=0.5)
        plt.plot([x_old, x_new], [x_new, x_new], 'k', lw=0.5)
        plt.arrow(x_old, x_old, 0, x_new - x_old, head_width=0.02, head_length=0.02, fc='r', ec='r')
        plt.arrow(x_old, x_new, x_new - x_old, 0, head_width=0.02, head_length=0.02, fc='r', ec='r')
        x_old = x_new

    plt.xlabel('$x$')
    plt.ylabel('$g(x)$')
    plt.title('Diagrama de Cobweb')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parámetros iniciales
x0 = 1.1  # Cambia esto según el valor inicial que desees
n = 6  # Número de iteraciones

cobweb_plot(g, x0, n)