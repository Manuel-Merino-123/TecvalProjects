from tkinter import *
ventana = Tk()
ventana.title("Frames en Tkinter")
#ventana.iconbitmap

#frame = LabelFrame(ventana, text='Esto es un LabelFrame') => Si deseamos ponerle marco
#frame.pack()

#frame = Frame(ventana) => Si no deseamos ponerle marco
#frame.pack()

#frame = Frame(ventana, bd = 5, relief = SUNKEN) => Con estilos de borde
#frame.pack

#relief = FLAT, RAISED, SUNKEN, GROOVE, RIDGE, SOLID, 

frame = Frame(ventana, bd = 2, relief = GROOVE,padx=100,pady=100) #padx=20, pady=20 => Para definir espaciado dentro del frame
frame.pack(padx=20, pady=20) #frame.pack(padx=100, pady=100) => Para definir espaciado con la ventana principal al ejecutarse al inicio

#Boton = Button(ventana,text= 'Click aqui')
#Boton.pack()

Boton = Button(frame,text= 'Click aqui')
Boton.grid(row=11, column=0)

Label1=Label(frame, text='Este texto esta dentro del Label')
Label1.grid(row=0, column=0)

#Label2 = Label(frame, text='Este texto tbm está dentro del Label')
#Label2.grid(row=10, column=1) => te obliga a tener elementos en la row = 9, 8, 7... sino lo coloca si o si en la fila 2
Label2 = Label(frame, text='Este texto tbm está dentro del Label')
Label2.grid(row=10, column=1)
               
ventana.mainloop()