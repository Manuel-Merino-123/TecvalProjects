import matplotlib.pyplot as plt
import numpy as np

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Cambiar el color del fondo de la figura y los ejes
fig.patch.set_facecolor('black')  # Fondo de la figura en negro, fondo principal
ax.set_facecolor('black')         # Fondo de los ejes en negro, lugar donde se ubica realmente el grafico

# Parámetros del array circular
num_circles = 5  # Número de círculos pequeños
radius_large = 1.2  # Radio del círculo grande (trayectoria)
radius_small = 0.1  # Radio de los círculos pequeños

# Cambiar el color del texto y las líneas de los ejes
ax.tick_params(axis='x', colors='white')  # Color del texto y marcas del eje X
ax.tick_params(axis='y', colors='white')  # Color del texto y marcas del eje Y
ax.spines['bottom'].set_color('yellow')    # Color de la línea del eje X
ax.spines['top'].set_color('yellow')       # Color de la línea superior
ax.spines['left'].set_color('yellow')      # Color de la línea del eje Y
ax.spines['right'].set_color('yellow')     # Color de la línea derecha

# Calcular las posiciones de los círculos pequeños
#linspace te genera un array de (6-1(endpoint=False)) valores de 0 a 2phi, 
angles = np.linspace(0, 2 * np.pi, num_circles, endpoint=False)  # Ángulos equidistantes
x_positions = radius_large * np.cos(angles)  # Posiciones x, x=rcos()
y_positions = radius_large * np.sin(angles)  # Posiciones y, y=rsen()

# Dibujar el círculo grande (trayectoria)
#circle_large = plt.Circle((0, 0), radius_large, color='red', fill=False)
#ls=linestyle  dashed o --(dashed), :(dotted), -.(dashdot), -(solid)
circle_large = plt.Circle((0, 0), radius_large, color='red', fill=False, ls='-.', linewidth=0.5)
ax.add_artist(circle_large)

# Dibujar los círculos pequeños
# zip combina los arrays x_positions & y_positions [(x1,y1),(x2,y2)...]
for x, y in zip(x_positions, y_positions):
    circle_small = plt.Circle((x, y), radius_small, color='blue', fill=False)
    ax.add_artist(circle_small)

# Configurar los límites del eje
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Asegurar que la relación de aspecto sea igual
ax.set_aspect('equal')

# Mostrar el gráfico
plt.show()