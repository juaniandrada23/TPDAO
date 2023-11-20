from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from listado import VentanaListadoLibros
from socio import Socio
from socio_controller import *

class VentanaCargaSocios():
    
    def __init__(self):
        # self.biblioteca = biblioteca
        
        self.ventana = Toplevel()
        self.ventana.title("Registrar Socios")
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

        Label(ingresos, text="Dni", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=0, column=0, sticky=E, padx=2)
        Label(ingresos, text="Nombre", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=1, column=0, sticky=E, padx=2)
        Label(ingresos, text="Apellido", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=2, column=0, sticky=E, padx=2)
    
        self.dni = IntVar()
        self.nombre = StringVar()
        self.apellido = StringVar()

        Entry(ingresos, textvariable=self.dni).grid(row=0, column=1)
        Entry(ingresos, textvariable=self.nombre).grid(row=1, column=1)
        Entry(ingresos, textvariable=self.apellido).grid(row=2, column=1)
        

        ttk.Button(botonera, text="Registrar", command=self.aceptar).place(x=5, y=20)
        ttk.Button(botonera, text="Cancelar", command=self.ventana.destroy).place(x=154, y=20)
        #ttk.Button(botonera, text="Listar", command=self.listar).place(x=300, y=20)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        createTable()
        dni = int(self.dni.get())
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        nuevoSocio = Socio(dni, nombre, apellido, )
        messagebox.showinfo("Socio registrado con éxito", str(nuevoSocio))
        registrarSocio(nuevoSocio)
        self.dni.set("")
        self.nombre.set("")
        self.apellido.set("")

    # def listar(self):
    #     VentanaListadoLibros(self.biblioteca).mostrar()