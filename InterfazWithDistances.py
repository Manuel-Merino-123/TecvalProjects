import matplotlib.pyplot as plt
import numpy as np
# Importa la clase FigureCanvasTkAgg desde módulo matplotlib.backends.backend_tkagg
# FigureCanvasTkAgg es una clase que permite integrar figuras de matplotlib en una interfaz gráfica de tkinter.
# Actúa como un puente entre matplotlib y tkinter, permitiendo que los gráficos se muestren en una ventana de tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk

#...ttk (Themed Tkinter) es una extensión de tkinter que proporciona widgets con un aspecto más moderno y personalizable...
#Incluye widgets como ttk.Button, ttk.Entry, ttk.Label, etc.
#Es útil para crear interfaces gráficas más atractivas...

from tkinter import ttk

# Función para actualizar el gráfico
def update_plot():
    # Obtener los valores de los parámetros desde la interfaz
    #Diameter_bolt_Circle = float(Diameter_bolt_Circle_entry.get())
    # CIRCULOS IZQUIERDA
    Outside_diameter1 = float(Outside_diameter1_entry.get())
    Diameter_bolt_Circle1 = float(Diameter_bolt_Circle1_entry.get())
    diameter_bolt_hole1 = float(diameter_bolt_hole1_entry.get())
    num_Circles1 = int(num_Circles1_entry.get())

    #CIRCULOS DERECHA
    Outside_diameter2 = float(Outside_diameter2_entry.get())
    Diameter_bolt_Circle2 = float(Diameter_bolt_Circle2_entry.get())
    diameter_bolt_hole2 = float(diameter_bolt_hole2_entry.get())
    num_Circles2 = int(num_Circles2_entry.get())

    # Limpiar el eje anterior
    ax.clear()

    # Cambiar el color del fondo de la figura y los ejes
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Cambiar el color del texto y las líneas de los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('yellow')
    ax.spines['top'].set_color('yellow')
    ax.spines['left'].set_color('yellow')
    ax.spines['right'].set_color('yellow')

    #CIRCULOS 1
    # Calcular las posiciones de los círculos pequeños
    angles1 = np.linspace(0, 2 * np.pi, num_Circles1, endpoint=False)
    #angles es un array
    # x_position & y_positions1 tambien son arrays(Se estan ubicando los centros)
    x_positions1 = Diameter_bolt_Circle1/2 * np.cos(angles1)
    y_positions1 = Diameter_bolt_Circle1/2 * np.sin(angles1)

    #CIRCULOS 2
    # Calcular las posiciones de los círculos pequeños(Se estan ubicando los centros)
    angles2 = np.linspace(0, 2 * np.pi, num_Circles2, endpoint=False)
    #angles es un array
    #x_position & y_positions1 tambien son arrays
    x_positions2 = Diameter_bolt_Circle2/2 * np.cos(angles2)
    y_positions2 = Diameter_bolt_Circle2/2 * np.sin(angles2)

    '''
    COLORES
    'white'       # Blanco puro (el mejor contraste)
    'yellow'      # Amarillo brillante
    'cyan'        # Cian (azul verdoso claro)
    'magenta'     # Magenta vibrante
    'lime'        # Verde lima intenso
    'deepskyblue' # Azul cielo profundo
    'orangered'   # Naranja-rojo intenso
    'springgreen' # Verde primavera brillante
    'violet'      # Violeta medio
    'gold'        # Dorado metálico
    'lightcoral'  # Coral claro
    'palegreen'   # Verde pálido (con línea gruesa)
    'aquamarine'  # Agua marina
    'hotpink'     # Rosa intenso
    '''

    # Dibujar el círculo grande (1) (trayectoria) 
    Circle_Outside1=plt.Circle((0,0),Outside_diameter1/2,color='springgreen',fill=False,ls='-',linewidth=0.5)
    Circle_Bolt1 = plt.Circle((0, 0), Diameter_bolt_Circle1/2, color='lime', fill=False, ls='-.', linewidth=0.5)
    ax.add_artist(Circle_Bolt1)
    ax.add_artist(Circle_Outside1)

    # Dibujar los círculos pequeños
    for x1, y1 in zip(x_positions1, y_positions1):
        Circle_bolt_hole1 = plt.Circle((x1, y1), diameter_bolt_hole1/2, color='aquamarine', fill=False)
        ax.add_artist(Circle_bolt_hole1)

    # Dibujar el círculo grande (2) (trayectoria) 
    Circle_Outside2=plt.Circle((0,0),Outside_diameter2/2,color='orangered',fill=False,ls='-',linewidth=0.5)
    Circle_Bolt2 = plt.Circle((0, 0), Diameter_bolt_Circle2/2, color='red', fill=False, ls='-.', linewidth=0.5)
    ax.add_artist(Circle_Bolt2)
    ax.add_artist(Circle_Outside2)

    # Dibujar los círculos pequeños
    for x2, y2 in zip(x_positions2, y_positions2):
        Circle_bolt_hole2 = plt.Circle((x2, y2), diameter_bolt_hole2/2, color='hotpink', fill=False)
        ax.add_artist(Circle_bolt_hole2)

    # Línea de codigo para dibujar las cotas

    if num_Circles1 and num_Circles2 > 0:
        # Coordenadas del primer círculo
        x1r, y1r = (x_positions1[0] + diameter_bolt_hole1/2.0), y_positions1[0]
        x2r, y2r = -(x_positions1[0] + diameter_bolt_hole1/2.0), y_positions2[0]
        # Línea de cota
        ax.plot([x1r, x2r], [y1r, y2r], color='yellow', linestyle='-', linewidth=0.7) # el grosor de aqui debe ser mas delgado que de la flecha, si
                                                                                        # sino la flecha desaparece
        # Agregar flechas en los extremos
        # xy=(x0, y0) Punto final de la linea de cota. En tu caso, es la ubicación del primer círculo (el agujero).
        #xytext=(0, 0) Punto inicial de la linea de cota. Es el centro del círculo grande.

        ax.annotate('', xy=(x2r, y2r), xytext=(x1r, y1r),arrowprops=dict(arrowstyle='|-|', color='yellow', lw=1,shrinkA=0,shrinkB=0))

        """
        '-'	Línea recta sin flecha
        '->'	Flecha unidireccional
        '<-'	Flecha apuntando hacia atrás
        '<->'	Flechas a ambos lados
        `'	-
        'fancy'	Flecha decorativa
        'simple'	Flecha simple y más gruesa
        'wedge'	Flecha con forma de cuña
        Prueba con arrowstyle='|-|' si prefieres líneas de cota tipo CAD sin puntas.
        """
        # Calcular punto medio
        midpoint_x = (x1r + x2r) / 2
        midpoint_y = (y1r + y2r) / 2

        # Distancia (radio del círculo de agujeros)
        distance = np.sqrt((x1r-x2r)**2 + (y1r-y2r)**2)

        # Mostrar texto con fondo
        #Para mostrar la cota dentro de un cuadrito
        # ha = horizontal alignment
        # va = vertical alignment
        # bbox = dict(...): crea un cuadro en el se ubicara la cota
        # facecolor = color de fondo negro
        # edgecolor = color de bordes negro
        # boxstyle = 'round,pad=0.3' Para que sea tipo redondeado
        ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow',
                fontsize=10, ha='center', va='center',
                bbox=dict(facecolor='black', edgecolor='black', boxstyle='round,pad=0.3'))
        
        #Para mostrar la cota limpia, que no este dentro de un cuadro
        """ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow',
        fontsize=8, ha='center', va='center')"""
    # Configurar los límites del eje
    axis_lim = np.maximum(Outside_diameter1,Outside_diameter2)
    ax.set_xlim(-axis_lim/2 * 1.1, axis_lim/2 * 1.1)
    ax.set_ylim(-axis_lim/2 * 1.1, axis_lim/2 * 1.1)

    # Asegurar que la relación de aspecto sea igual
    ax.set_aspect('equal')

    # Redibujar el canvas
    canvas.draw()

# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Aquasoft")

# Crear un marco para los controles control_frame1
control_frame1 = ttk.Frame(root)
control_frame1.pack(side=tk.LEFT, padx=20, pady=20, anchor='w')

''' "nw"	North-West	Esquina superior izquierda
    "n"	North	Centro superior
    "ne"	North-East	Esquina superior derecha
    "w"	West	Centro izquierdo
    "center"	Center	Centro exacto
    "e"	East	Centro derecho
    "sw"	South-West	Esquina inferior izquierda
    "s"	South	Centro inferior
    "se"	South-East	Esquina inferior derecha'''

# Crear campos de entrada para los parámetros
ttk.Label(control_frame1, text="Diametro del círculo mayor:").grid(row=0, column=0, padx=5, pady=5)
Outside_diameter1_entry = ttk.Entry(control_frame1)
Outside_diameter1_entry.grid(row=0, column=1, padx=5, pady=5)
Outside_diameter1_entry.insert(0, "200")  # Valor por defecto


ttk.Label(control_frame1, text="Diametro del círculo de agujeros:").grid(row=1, column=0, padx=5, pady=5)
Diameter_bolt_Circle1_entry = ttk.Entry(control_frame1)
Diameter_bolt_Circle1_entry.grid(row=1, column=1, padx=5, pady=5)
Diameter_bolt_Circle1_entry.insert(0, "160")  # Valor por defecto

ttk.Label(control_frame1, text="Diametro del círculo pequeño:").grid(row=2, column=0, padx=5, pady=5)
diameter_bolt_hole1_entry = ttk.Entry(control_frame1)
diameter_bolt_hole1_entry.grid(row=2, column=1, padx=5, pady=5)
diameter_bolt_hole1_entry.insert(0, "19")  # Valor por defecto

ttk.Label(control_frame1, text="Número de círculos pequeños:").grid(row=3, column=0, padx=5, pady=5)
num_Circles1_entry = ttk.Entry(control_frame1)
num_Circles1_entry.grid(row=3, column=1, padx=5, pady=5)
num_Circles1_entry.insert(0, "8")  # Valor por defecto

# Botón para actualizar el gráfico (1)
update_button1 = ttk.Button(control_frame1, text="Actualizar Gráfico", command=update_plot)
update_button1.grid(row=4, column=0, columnspan=2, pady=10)


# Crear un marco para los controles control_frame2
control_frame2 = ttk.Frame(root)
control_frame2.pack(side=tk.RIGHT, padx=20, pady=20, anchor='e')

''' "nw"	North-West	Esquina superior izquierda
    "n"	North	Centro superior
    "ne"	North-East	Esquina superior derecha
    "w"	West	Centro izquierdo
    "center"	Center	Centro exacto
    "e"	East	Centro derecho
    "sw"	South-West	Esquina inferior izquierda
    "s"	South	Centro inferior
    "se"	South-East	Esquina inferior derecha'''

# Crear campos de entrada para los parámetros: control frame 2
ttk.Label(control_frame2, text="Diametro del círculo mayor:").grid(row=0, column=0, padx=5, pady=5)
Outside_diameter2_entry = ttk.Entry(control_frame2)
Outside_diameter2_entry.grid(row=0, column=1, padx=5, pady=5)
Outside_diameter2_entry.insert(0, "210")  # Valor por defecto


ttk.Label(control_frame2, text="Diametro del círculo de agujeros:").grid(row=1, column=0, padx=5, pady=5)
Diameter_bolt_Circle2_entry = ttk.Entry(control_frame2)
Diameter_bolt_Circle2_entry.grid(row=1, column=1, padx=5, pady=5)
Diameter_bolt_Circle2_entry.insert(0, "168.3")  # Valor por defecto

ttk.Label(control_frame2, text="Diametro del círculo pequeño:").grid(row=2, column=0, padx=5, pady=5)
diameter_bolt_hole2_entry = ttk.Entry(control_frame2)
diameter_bolt_hole2_entry.grid(row=2, column=1, padx=5, pady=5)
diameter_bolt_hole2_entry.insert(0, "22.23")  # Valor por defecto

ttk.Label(control_frame2, text="Número de círculos pequeños:").grid(row=3, column=0, padx=5, pady=5)
num_Circles2_entry = ttk.Entry(control_frame2)
num_Circles2_entry.grid(row=3, column=1, padx=5, pady=5)
num_Circles2_entry.insert(0, "8")  # Valor por defecto

# Botón para actualizar el gráfico
update_button2 = ttk.Button(control_frame2, text="Actualizar Gráfico", command=update_plot)
update_button2.grid(row=4, column=0, columnspan=2, pady=10)


# Crear una figura de matplotlib
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
root.state('zoomed')
# Integrar la figura de matplotlib en la interfaz de tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Mostrar la ventana
root.mainloop()