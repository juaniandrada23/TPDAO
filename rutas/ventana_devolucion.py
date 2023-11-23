from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from prestamo_controller import *
from libro_controller import *

class VentanaCargaDevolucion():
    
    def __init__(self):
        
        self.ventana = Toplevel()
        self.ventana.title("Registrar Devolucion de Libro")
        self.ventana.geometry("400x200")

        style = ttk.Style()
        style.configure("TButton",
                        padding=5,
                        relief="flat",
                        background="#E0E1DD",
                        foreground="black",
                        font=('Monserrat', 10, 'bold'))

        style.map("TButton",
                  background=[('active', '#2980b9')])

        ingresos = Frame(self.ventana, bg='#778DA9')
        ingresos.pack(expand=True, fill='both')

        botonera = Frame(self.ventana, bg='#778DA9')
        botonera.pack(expand=True, fill='both')

        Label(ingresos, text="Código del libro", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=0, column=0, sticky=E, padx=2)
    
        self.codigo = StringVar()
        
        Entry(ingresos, textvariable=self.codigo).grid(row=0, column=1)
        

        ttk.Button(botonera, text="Registrar", command=self.aceptar).place(x=5, y=20)
        ttk.Button(botonera, text="Cancelar", command=self.ventana.destroy).place(x=154, y=20)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        codigo = self.codigo.get()
        codigo_libro_prestado = getTituloLibroPrestado(int(codigo))
        if len(codigo_libro_prestado) > 0:
            eliminarPrestamo(codigo_libro_prestado[0][0])
            actualizarEstado(codigo_libro_prestado[0][0],'disponible')
            messagebox.showinfo("","La devolucion del libro se resgistro correctamente")
        else:
            messagebox.showinfo("Error","El libro no esta prestado")
        self.codigo.set("")
