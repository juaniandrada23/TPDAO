from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from listado_libros import VentanaListadoLibros
from listado_extraviados import VentanaListadoExtraviados
from libro import Libro
from libro_controller import *

class VentanaCargaLibros():
    
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        
        self.ventana = Toplevel()
        self.ventana.title("Cargar Libro")
        self.ventana.geometry("600x300")

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

        Label(ingresos, text="Código", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=0, column=0, sticky=E, padx=2)
        Label(ingresos, text="Título", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=1, column=0, sticky=E, padx=2)
        Label(ingresos, text="Precio de reposición", font=('Monserrat', 9, 'bold'), bg='#778DA9').grid(row=2, column=0, sticky=E, padx=2)
        Label(ingresos, text="Estado", bg='#778DA9', font=('Monserrat', 9, 'bold')).grid(row=3, column=0, sticky=E, padx=2)

        self.codigo = IntVar()
        self.titulo = StringVar()
        self.precio = IntVar()
        self.estado = StringVar()

        Entry(ingresos, textvariable=self.codigo).grid(row=0, column=1)
        Entry(ingresos, textvariable=self.titulo).grid(row=1, column=1)
        Entry(ingresos, textvariable=self.precio).grid(row=2, column=1)
        self.combo = ttk.Combobox(ingresos, values=['disponible', 'prestado', 'extraviado'], state="readonly")
        self.combo.current(0)
        self.combo.grid(row=3, column=1)

        ttk.Button(botonera, text="Aceptar", command=self.aceptar).place(x=5, y=20)
        ttk.Button(botonera, text="Cancelar", command=self.ventana.destroy).place(x=154, y=20)
        ttk.Button(botonera, text="Listar", command=self.listar).place(x=300, y=20)
        ttk.Button(botonera, text="Listar Extraviados", command=self.listarExtraviados).place(x=440, y=20)
        #ttk.Button(botonera, text="Disponibilizar", command=self.disponible).place(x=400, y=20)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        createTableLibro()
        codigo = int(self.codigo.get())
        titulo = self.titulo.get()
        precio = self.precio.get()
        estado = self.combo.get()
        nuevoLibro = Libro(codigo, titulo, precio, estado)
        registrarLibro(nuevoLibro)
        messagebox.showinfo("Libro cargado", str(nuevoLibro))
        self.codigo.set("")
        self.titulo.set("")
        self.precio.set("")
        self.estado.set("")

    def listar(self):
        VentanaListadoLibros(self.biblioteca).mostrar()
    
    def listarExtraviados(self):
        VentanaListadoExtraviados(self.biblioteca).mostrar()
    
    #def disponible(self):
        #actualizarEstado(0,'disponible')