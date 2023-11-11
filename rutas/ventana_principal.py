from tkinter import *
from tkinter import messagebox
from carga import VentanaCarga
from biblioteca import Biblioteca
biblioteca = Biblioteca()

class VentanaPrincipal():
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Biblioteca La Rioja")
        self.ventana.geometry("600x400")

        botonera = Frame()
        botonera.pack(side=LEFT)
        Button(botonera, text="Administrar Libros",command=self.abrir_ventana_carga).grid(row=0, column=0)
        Button(botonera, text="Administrar Socios").grid(row=1, column=0)
        Button(botonera, text="Generar Reportes").grid(row=2, column=0)

   
    def abrir_ventana_carga(self):
        ventana_carga = VentanaCarga(biblioteca)
        ventana_carga.mostrar()
    
    def mostrar(self):
        self.ventana.mainloop()
        
