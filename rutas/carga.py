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
        self.ventana.geometry("400x400")
        
        ingresos = Frame(self.ventana)
        ingresos.grid(row=0, column=0)
        
        botonera = Frame(self.ventana)
        botonera.grid(row=1, column=0)
        
        Label(ingresos, text="Código").grid(row=0, column=0,sticky=E)
        Label(ingresos, text="Título").grid(row=1, column=0,sticky=E)
        Label(ingresos, text="Precio de reposición").grid(row=2, column=0,sticky=E)
        Label(ingresos, text="Estado").grid(row=3, column=0,sticky=E)
        
        
        self.codigo = IntVar()
        self.titulo = StringVar()
        self.precio = IntVar()
        self.estado = StringVar()
                
        Entry(ingresos, textvariable=self.codigo).grid(row=0, column=1)
        Entry(ingresos, textvariable=self.titulo).grid(row=1, column=1)
        Entry(ingresos, textvariable=self.precio).grid(row=2, column=1)
        combo = ttk.Combobox(ingresos, values=['Disponible', 'Prestado', 'Extraviado'],state="readonly")
        combo.current(0)
        combo.grid(row=3, column=1)
        
        Button(botonera, text="Aceptar",command=self.aceptar).pack(side=LEFT)
        Button(botonera, text="Cancelar",command=self.ventana.destroy).pack(side=LEFT)
        Button(botonera, text="Listar",command=self.listar).pack(side=LEFT)
        
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

