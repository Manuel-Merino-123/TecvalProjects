import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk
from tkinter import ttk

# Todo lo que esta dentro de def update_plot(): se ejecuta cuando pulso click al boton
# Actualizar grafico, lo que está fuera del def se ejecuta una sola vez y luego el root.mainloop() 
def update_plot():
    try:
        # Obtener los valores de los puntos
        Punto1x = float(Punto1x_entry.get())
        Punto1y = float(Punto1y_entry.get())
        Punto2x = float(Punto2x_entry.get())
        Punto2y = float(Punto2y_entry.get())

        ax.clear()
        
        # Configurar el estilo del gráfico
        #fig.patch.set_facecolor('black')
        #ax.set_facecolor('black')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('yellow')
        ax.spines['top'].set_color('yellow')
        ax.spines['left'].set_color('yellow')
        ax.spines['right'].set_color('yellow')
        
        # Dibujar los puntos
        ax.scatter([Punto1x, Punto2x], [Punto1y, Punto2y], color='red', s=50)
        
        # Dibujar la línea que une los puntos
        ax.plot([Punto1x, Punto2x], [Punto1y, Punto2y], color='white', linestyle='-', linewidth=1)
        
        # Calcular el vector entre los puntos
        dx = Punto2x - Punto1x
        dy = Punto2y - Punto1y
        length = np.sqrt(dx**2 + dy**2)
        
        # Configuración de las cotas
        line_offset = length * 0.2  # Distancia de desplazamiento de la línea de cota
        #text_offset = length * 0.1  # Desplazamiento adicional para el texto
        
        if length > 0:
            # Vector unitario perpendicular
            perp_x = -dy/length * line_offset
            perp_y = dx/length * line_offset
            
            # Puntos desplazados
            Punto1x_offset = Punto1x + perp_x
            Punto1y_offset = Punto1y + perp_y
            Punto2x_offset = Punto2x + perp_x
            Punto2y_offset = Punto2y + perp_y
            
            # Dibujar línea de cota desplazada (azul)
            #ax.plot([Punto1x_offset, Punto2x_offset], [Punto1y_offset, Punto2y_offset], 
            #        color='yellow', linestyle='-', linewidth=0.8)
            
            # Dibujar líneas de extensión (amarillas punteadas)
            ax.plot([Punto1x, Punto1x_offset], [Punto1y, Punto1y_offset], 
                    color='yellow', linestyle=':', linewidth=0.5)
            ax.plot([Punto2x, Punto2x_offset], [Punto2y, Punto2y_offset], 
                    color='yellow', linestyle=':', linewidth=0.5)
            
            # Flechas de cota
             
            # Con este codigo las puntas de las flecha no coincidian con los extremos de las lineas punteadas 
            #ax.annotate('',xy=(Punto1x_offset, Punto1y_offset), 
            #          xytext=(Punto2x_offset, Punto2y_offset),
            #          arrowprops=dict(arrowstyle='<->', color='blue', lw=1))

            ax.annotate('', 
                xy=(Punto2x_offset, Punto2y_offset), 
                xytext=(Punto1x_offset, Punto1y_offset),
                arrowprops=dict(
                    arrowstyle='<->', 
                    color='blue', 
                    lw=1,
                    shrinkA=0,  # No reducir en el punto A
                    shrinkB=0   # No reducir en el punto B
                ))
            
            # Texto de la cota (en el punto medio de la 2 línea de cota)
            midpoint_x = (Punto1x_offset + Punto2x_offset)/2 + perp_x * 0.2
            midpoint_y = (Punto1y_offset + Punto2y_offset)/2 + perp_y * 0.2

            # Aplha es transparencia 80% opaco
            # boxstyle='round,pad=0.1' Estilo redondeado y 0.1 de distancia del texto a la caja
            ax.text(midpoint_x, midpoint_y, f'{length:.2f}', color='yellow',
                    fontsize=8, ha='center', va='center',
                    bbox=dict(facecolor='black', edgecolor='black', 
                            boxstyle='round,pad=0.1', alpha=1))

        # Ajustar los límites del gráfico automáticamente
        min_x = min(Punto1x, Punto2x)
        max_x = max(Punto1x, Punto2x)
        min_y = min(Punto1y, Punto2y)
        max_y = max(Punto1y, Punto2y)
        
        # Añadir un margen alrededor de los puntos
        margin = max((max_x - min_x), (max_y - min_y)) * 0.5
        if margin == 0:  # En caso de que los puntos coincidan
            margin = 1
            
        ax.set_xlim(min_x - margin, max_x + margin)
        ax.set_ylim(min_y - margin, max_y + margin)
        ax.set_aspect('equal')
        canvas.draw()
    
    except ValueError as e:
        print(f"Error en los datos de entrada: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Visualización de línea con cotas")

# Marco para los controles
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.TOP, padx=5, pady=5)

# Campos de entrada
ttk.Label(control_frame, text="Coordenada x del punto 1:").grid(row=0, column=0, padx=5, pady=5)
Punto1x_entry = ttk.Entry(control_frame)
Punto1x_entry.insert(0, "1.0")  # Valor por defecto
Punto1x_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(control_frame, text="Coordenada y del punto 1:").grid(row=1, column=0, padx=5, pady=5)
Punto1y_entry = ttk.Entry(control_frame)
Punto1y_entry.insert(0, "1.0")  # Valor por defecto
Punto1y_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(control_frame, text="Coordenada x del punto 2:").grid(row=2, column=0, padx=5, pady=5)
Punto2x_entry = ttk.Entry(control_frame)
Punto2x_entry.insert(0, "-1.0")  # Valor por defecto
Punto2x_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(control_frame, text="Coordenada y del punto 2:").grid(row=3, column=0, padx=5, pady=5)
Punto2y_entry = ttk.Entry(control_frame)
Punto2y_entry.insert(0, "-1.0")  # Valor por defecto
Punto2y_entry.grid(row=3, column=1, padx=5, pady=5)

# Botón de actualización
# [ Etiqueta 1  ][ Campo Entrada 1 ]
# [ Etiqueta 2  ][ Campo Entrada 2 ]
# [ Etiqueta 3  ][ Campo Entrada 3 ]
# [       BOTÓN ANCHO COMPLETO      ] ← columnspan=2(hace que ocupe 2 espacios de columna) con espacio pady=10(5 arriba y 5 abajo)
update_button = ttk.Button(control_frame, text="Actualizar Gráfico", command=update_plot)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Configuración de la figura
fig, ax = plt.subplots() # Ventana inicial
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
root.state('zoomed')

# Canvas para el gráfico
# Esta linea de codigo es fundamental para integrar MatplotLib con Tkinter
# canvas = lienzo
canvas = FigureCanvasTkAgg(fig, master=root) # Indica que el lienzo pertenecerá a la ventana principal (root) de Tkinter.
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# side=tk.BOTTOM: Coloca el widget(grafico del matplotlib) en la parte inferior de la ventana.
# fill=tk.BOTH: Hace que el widget se expanda para llenar todo el espacio disponible tanto en horizontal como en vertical.
# expand=True: Permite que el widget se expanda si la ventana cambia de tamaño.

# Ejecutar la aplicación
root.mainloop()