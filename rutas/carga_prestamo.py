from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from listado import VentanaListadoLibros
from prestamos import Prestamo
from prestamo_controller import *
from socio_controller import *
from libro_controller import *

class VentanaCargaPrestamos():
    
    def __init__(self):
        
        self.ventana = Toplevel()
        self.ventana.title("Cargar Prestamo de Libro")
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

        Label(ingresos, text="Código del Libro", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=0, column=0, sticky=E, padx=2)
        Label(ingresos, text="Dni del socio", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=1, column=0, sticky=E, padx=2)
        Label(ingresos, text="Días a ser prestado", bg='#778DA9', font=('Monserrat', 9, 'bold')).grid(row=2, column=0, sticky=E, padx=2)

        self.codigo = IntVar()
        self.dni = IntVar()
        self.dias = IntVar()

        Entry(ingresos, textvariable=self.codigo).grid(row=0, column=1)
        Entry(ingresos, textvariable=self.dni).grid(row=1, column=1)
        Entry(ingresos, textvariable=self.dias).grid(row=2, column=1)


        ttk.Button(botonera, text="Aceptar", command=self.aceptar).place(x=5, y=20)
        ttk.Button(botonera, text="Cancelar", command=self.ventana.destroy).place(x=154, y=20)
        ttk.Button(botonera, text="Listar").place(x=300, y=20)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        if buscarSocio(self.getInputDni()):
            if buscarLibroDisponible(self.getInputCodigo(),'disponible'):
                createTablePrestamo()
                codigo = int(self.codigo.get())
                dni = int(self.dni.get())
                dias = int(self.dias.get())
                nuevoPrestamo = Prestamo(codigo, dni, dias)
                registrarPrestamo(nuevoPrestamo)
                actualizarEstado(codigo,"prestado")
                messagebox.showinfo("", "Prestamo registrado con éxito")
                print(nuevoPrestamo.registrar_devolucion())
                self.codigo.set("")
                self.codigo.set("")
                self.dni.set("")
                self.dias.set("")
            else:
                messagebox.showinfo("Error","El libro no se encuentra disponible")   
        else:
            messagebox.showinfo("Error","No existe socio con ese dni")
    
    def getInputDni(self):
        return int(self.dni.get())
    
    def getInputCodigo(self):
        return int(self.codigo.get())