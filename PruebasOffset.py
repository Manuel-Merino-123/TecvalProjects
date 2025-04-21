import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk
from tkinter import ttk

def update_plot():
    try:
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

        # Generar posiciones de los agujeros
        angles = np.linspace(0, 2 * np.pi, num_Circles, endpoint=False)
        x_positions = Diameter_bolt_Circle/2 * np.cos(angles)
        y_positions = Diameter_bolt_Circle/2 * np.sin(angles)

        # Dibujar círculos principales
        Circle_Outside = plt.Circle((0,0), Outside_diameter/2, color='white', fill=False, ls='-', linewidth=0.5)
        Circle_Bolt = plt.Circle((0, 0), Diameter_bolt_Circle/2, color='red', fill=False, ls='-.', linewidth=0.5)
        ax.add_artist(Circle_Bolt)
        ax.add_artist(Circle_Outside)

        # Dibujar agujeros
        for x, y in zip(x_positions, y_positions):
            Circle_bolt_hole = plt.Circle((x, y), diameter_bolt_hole/2, color='blue', fill=False)
            ax.add_artist(Circle_bolt_hole)

        # Mostrar cota del radio del círculo de agujeros (solo si hay agujeros)
        if num_Circles > 0:
            # Tomar el primer agujero como referencia
            x0, y0 = x_positions[0], y_positions[0]
            
            # Configuración de estilo para la cota
            line_offset = 0.1 * Diameter_bolt_Circle  # Desplazamiento proporcional al tamaño
            text_offset = 0.15 * Diameter_bolt_Circle
            
            # Calcular vector perpendicular
            dx = x0 - 0
            dy = y0 - 0
            length = np.sqrt(dx**2 + dy**2)
            
            if length > 0:
                # Vector unitario perpendicular
                perp_x = -dy/length * line_offset
                perp_y = dx/length * line_offset
                
                # Puntos desplazados
                x_offset = x0 + perp_x
                y_offset = y0 + perp_y
                
                # Dibujar línea de cota desplazada
                ax.plot([0 + perp_x, x_offset], [0 + perp_y, y_offset], 
                        color='yellow', linestyle='-', linewidth=0.8)
                
                # Dibujar líneas de extensión
                ax.plot([0, 0 + perp_x], [0, 0 + perp_y], 
                        color='yellow', linestyle=':', linewidth=0.5)
                ax.plot([x0, x_offset], [y0, y_offset], 
                        color='yellow', linestyle=':', linewidth=0.5)
                
                # Flechas
                arrow_scale = min(0.2, length/3)
                ax.annotate('', xy=(x_offset, y_offset), 
                          xytext=(x_offset - dx*arrow_scale, y_offset - dy*arrow_scale),
                          arrowprops=dict(arrowstyle='->', color='yellow', lw=1))
                
                ax.annotate('', xy=(0 + perp_x, 0 + perp_y), 
                          xytext=(0 + perp_x + dx*arrow_scale, 0 + perp_y + dy*arrow_scale),
                          arrowprops=dict(arrowstyle='->', color='yellow', lw=1))
                
                # Texto de la cota
                midpoint_x = (0 + perp_x + x_offset)/2 + perp_x * text_offset/length
                midpoint_y = (0 + perp_y + y_offset)/2 + perp_y * text_offset/length
                
                ax.text(midpoint_x, midpoint_y, f'{length:.2f}', color='yellow',
                        fontsize=8, ha='center', va='center',
                        bbox=dict(facecolor='black', edgecolor='yellow', 
                                boxstyle='round,pad=0.2', alpha=0.8))

        ax.set_xlim(-Outside_diameter/2 * 1.5, Outside_diameter/2 * 1.5)
        ax.set_ylim(-Outside_diameter/2 * 1.5, Outside_diameter/2 * 1.5)
        ax.set_aspect('equal')
        canvas.draw()
    
    except ValueError as e:
        print(f"Error en los datos de entrada: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Visualización de Círculos Concéntricos")

# Marco para los controles
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.TOP, padx=10, pady=10)

# Campos de entrada
ttk.Label(control_frame, text="Diámetro del círculo mayor:").grid(row=0, column=0, padx=5, pady=5)
Outside_diameter_entry = ttk.Entry(control_frame)
Outside_diameter_entry.grid(row=0, column=1, padx=5, pady=5)
Outside_diameter_entry.insert(0, "2")

ttk.Label(control_frame, text="Diámetro del círculo de agujeros:").grid(row=1, column=0, padx=5, pady=5)
Diameter_bolt_Circle_entry = ttk.Entry(control_frame)
Diameter_bolt_Circle_entry.grid(row=1, column=1, padx=5, pady=5)
Diameter_bolt_Circle_entry.insert(0, "1.2")

ttk.Label(control_frame, text="Diámetro de los agujeros:").grid(row=2, column=0, padx=5, pady=5)
diameter_bolt_hole_entry = ttk.Entry(control_frame)
diameter_bolt_hole_entry.grid(row=2, column=1, padx=5, pady=5)
diameter_bolt_hole_entry.insert(0, "0.1")

ttk.Label(control_frame, text="Número de agujeros:").grid(row=3, column=0, padx=5, pady=5)
num_Circles_entry = ttk.Entry(control_frame)
num_Circles_entry.grid(row=3, column=1, padx=5, pady=5)
num_Circles_entry.insert(0, "5")

# Botón de actualización
update_button = ttk.Button(control_frame, text="Actualizar Gráfico", command=update_plot)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Configuración de la figura
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Canvas para el gráfico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()