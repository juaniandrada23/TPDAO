from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from listado import VentanaListadoLibros
from libro import Libro

class VentanaCarga():
    
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        
        self.ventana = Toplevel()
        self.ventana.title("Cargar Libro")
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
        combo = ttk.Combobox(ingresos, values=['Disponible', 'Prestado', 'Extraviado'], state="readonly")
        combo.current(0)
        combo.grid(row=3, column=1)

        ttk.Button(botonera, text="Aceptar", command=self.aceptar).place(x=5, y=20)
        ttk.Button(botonera, text="Cancelar", command=self.ventana.destroy).place(x=154, y=20)
        ttk.Button(botonera, text="Listar", command=self.listar).place(x=300, y=20)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        codigo = int(self.codigo.get())
        titulo = self.titulo.get()
        precio = self.precio.get()
        estado = self.estado.get()
        nueva = Libro(codigo, titulo, precio, estado)
        messagebox.showinfo("Libro cargado", str(nueva))
        self.biblioteca.agregar(nueva)
        self.codigo.set("")
        self.titulo.set("")
        self.precio.set("")
        self.estado.set("")

    def listar(self):
        VentanaListadoLibros(self.biblioteca).mostrar()