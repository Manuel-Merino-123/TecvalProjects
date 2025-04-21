'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 10])  # Dibuja una línea
plt.show()  # Muestra el gráfico'''
    # Ejemplo: mostrar cota del radio del círculo de agujeros
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk
from tkinter import ttk

def update_plot():
    Outside_diameter = float(Outside_diameter_entry.get())
    Diameter_bolt_Circle = float(Diameter_bolt_Circle_entry.get())
    diameter_bolt_hole = float(diameter_bolt_hole_entry.get())
    num_Circles = int(num_Circles_entry.get())

    ax.clear()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('yellow')
    ax.spines['top'].set_color('yellow')
    ax.spines['left'].set_color('yellow')
    ax.spines['right'].set_color('yellow')

    angles = np.linspace(0, 2 * np.pi, num_Circles, endpoint=False)
    x_positions = Diameter_bolt_Circle/2 * np.cos(angles)
    y_positions = Diameter_bolt_Circle/2 * np.sin(angles)

    Circle_Outside = plt.Circle((0,0), Outside_diameter/2, color='white', fill=False, ls='-', linewidth=0.5)
    Circle_Bolt = plt.Circle((0, 0), Diameter_bolt_Circle/2, color='red', fill=False, ls='-.', linewidth=0.5)
    ax.add_artist(Circle_Bolt)
    ax.add_artist(Circle_Outside)

    """for x, y in zip(x_positions, y_positions):
        Circle_bolt_hole = plt.Circle((x, y), diameter_bolt_hole/2, color='blue', fill=False)
        ax.add_artist(Circle_bolt_hole)
            # Ejemplo: mostrar cota del radio del círculo de agujeros
    if num_Circles > 0:
        # Solo toma el primer agujero para mostrar la cota
        x0, y0 = x_positions[0], y_positions[0]
        ax.plot([0, x0], [0, y0], 'yellow', linestyle='--', linewidth=0.8)  # línea de cota
        midpoint_x = (0 + x0) / 2
        midpoint_y = (0 + y0) / 2
        distance = np.sqrt(x0**2 + y0**2)
        ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow', fontsize=8, ha='center', va='center',
                bbox=dict(facecolor='black', edgecolor='yellow', boxstyle='round,pad=0.3'))"""
    """for x, y in zip(x_positions, y_positions):
        Circle_bolt_hole = plt.Circle((x, y), diameter_bolt_hole/2, color='blue', fill=False)
        ax.add_artist(Circle_bolt_hole)

        # Línea de cota individual
        ax.plot([0, x], [0, y], 'yellow', linestyle='--', linewidth=0.5)
        midpoint_x = (0 + x) / 2
        midpoint_y = (0 + y) / 2
        distance = np.sqrt(x**2 + y**2)
        ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow', fontsize=6, ha='center', va='center')"""
    if num_Circles > 0:
        # Coordenadas del primer círculo
        x0, y0 = x_positions[0], y_positions[0]
        
        # Línea de cota
        ax.plot([0, x0], [0, y0], color='yellow', linestyle='-', linewidth=0.1) # el grosor de aqui debe ser mas delgado que de la flecha, si
                                                                                # sino la flecha desaparece
        # Agregar flechas en los extremos
        ax.annotate('', xy=(x0, y0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='|-|', color='yellow', lw=1))

        # Calcular punto medio
        midpoint_x = (0 + x0) / 2
        midpoint_y = (0 + y0) / 2

        # Distancia (radio del círculo de agujeros)
        distance = np.sqrt(x0**2 + y0**2)

        # Mostrar texto con fondo
        #Para mostrar la cota dentro de un cuadrito
        ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow',
                fontsize=8, ha='center', va='center',
                bbox=dict(facecolor='black', edgecolor='yellow', boxstyle='roundtooth,pad=0.3'))
        # bbox=dict(boxstyle='round,pad=0.3,rounding_size=0.2', ...)
        # bbox=dict(boxstyle='square,pad=0.3', ...)
        # bbox=dict(boxstyle='circle,pad=0.3', ...)
        # bbox=dict(boxstyle='darrow,pad=0.3', ...)
        # bbox=dict(boxstyle='rarrow,pad=0.3', ...)
        # bbox=dict(boxstyle='sawtooth,pad=0.3', ...)
        # bbox=dict(boxstyle='roundtooth,pad=0.3', ...)
        
        #Para mostrar la cota limpia, que no este dentro de un cuadro
        """ax.text(midpoint_x, midpoint_y, f'{distance:.2f}', color='yellow',
        fontsize=8, ha='center', va='center')"""




    ax.set_xlim(-Outside_diameter/2 * 1.5, Outside_diameter/2 * 1.5)
    ax.set_ylim(-Outside_diameter/2 * 1.5, Outside_diameter/2 * 1.5)
    ax.set_aspect('equal')
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Aquasoft")

# Marco para los controles con mayores valores de padx y pady, es toda la ventana blanca
control_frame = ttk.Frame(root)
#el padx esta no cumple un rol aqui, solo el pady, ya que si colocamos padx=0 no hay cambios
#El pady ajusta el ancho total en el eje y. Podemos colocar pady=0 y la ventana se ajusta
control_frame.pack(side=tk.TOP, padx=0, pady=0)  # Aumentado de 100 a 30

# Crear campos de entrada con mayores espaciados
ttk.Label(control_frame, text="Diametro del círculo mayor:").grid(row=0, column=0, padx=50, pady=15)  # Aumentado de 10 a 100/15
Outside_diameter_entry = ttk.Entry(control_frame)
Outside_diameter_entry.grid(row=0, column=1, padx=50, pady=15)  # Aumentado de 5 a 15
Outside_diameter_entry.insert(0, "2")

ttk.Label(control_frame, text="Diametro del círculo de agujeros:").grid(row=1, column=0, padx=50, pady=15)
Diameter_bolt_Circle_entry = ttk.Entry(control_frame)
Diameter_bolt_Circle_entry.grid(row=1, column=1, padx=50, pady=15)
Diameter_bolt_Circle_entry.insert(0, "1.2")

ttk.Label(control_frame, text="Diametro del círculo pequeño:").grid(row=2, column=0, padx=50, pady=15)
diameter_bolt_hole_entry = ttk.Entry(control_frame)
diameter_bolt_hole_entry.grid(row=2, column=1, padx=50, pady=15)
diameter_bolt_hole_entry.insert(0, "0.1")

ttk.Label(control_frame, text="Número de círculos pequeños:").grid(row=3, column=0, padx=50, pady=15)
num_Circles_entry = ttk.Entry(control_frame)
num_Circles_entry.grid(row=3, column=1, padx=50, pady=15)
num_Circles_entry.insert(0, "5")

# Botón con mayor espaciado
update_button = ttk.Button(control_frame, text="Actualizar Gráfico", command=update_plot)
update_button.grid(row=4, column=0, columnspan=2, pady=25)  # Aumentado de 10 a 25

# Configuración de la figura
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Canvas para el gráfico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()