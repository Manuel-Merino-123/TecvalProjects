"""import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#ax.plot(x, y)
ax.set_title("Gráfico")
ax.set_xlabel("Eje X")
plt.show()"""

"""import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots()

# Dibujar un círculo
#circle = plt.Circle((x0,y0), r, color='blue', fill=False)
circle = plt.Circle((0, 0), 1, color='black', fill=False)

# Añadir el círculo al eje, para que se dibuje en la figura
ax.add_artist(circle)

# Configurar los límites del eje
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Mostrar el gráfico
plt.gca().set_aspect('equal', adjustable='box')
plt.show()"""

import matplotlib.pyplot as plt

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Cambiar el color del fondo de la figura y los ejes
fig.patch.set_facecolor('black')  # Fondo de la figura en negro, fondo principal
ax.set_facecolor('black')         # Fondo de los ejes en negro, lugar donde se ubica realmente el grafico

# Cambiar el color del texto y las líneas de los ejes
ax.tick_params(axis='x', colors='white')  # Color del texto y marcas del eje X
ax.tick_params(axis='y', colors='white')  # Color del texto y marcas del eje Y
ax.spines['bottom'].set_color('yellow')    # Color de la línea del eje X
ax.spines['top'].set_color('yellow')       # Color de la línea superior
ax.spines['left'].set_color('yellow')      # Color de la línea del eje Y
ax.spines['right'].set_color('yellow')     # Color de la línea derecha

# Dibujar un círculo con borde blanco
circle1 = plt.Circle((0,0), 0.5, color='red', fill=False)
circle2 = plt.Circle((0,0), 0.25,color='blue', fill=False )
ax.add_artist(circle1)
ax.add_artist(circle2)

# Configurar los límites del eje
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Cambiar el color del título y las etiquetas
ax.set_title("Aquasoft", color='magenta')  # Título en blanco
ax.set_xlabel("Eje X", color='white')                 # Etiqueta del eje X en blanco
ax.set_ylabel("Eje Y", color='white')                 # Etiqueta del eje Y en blanco

# Mostrar el gráfico
plt.gca().set_aspect('equal', adjustable='box')
plt.show()