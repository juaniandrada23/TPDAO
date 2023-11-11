from tkinter import *
from tkinter import messagebox

class VentanaPrincipal():
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Biblioteca La Rioja")
        self.ventana.geometry("600x400")

        botonera = Frame()
        botonera.pack(side=BOTTOM)

        Button(botonera, text="Administrar Libros").pack(side=LEFT)
        Button(botonera, text="Administrar Socios").pack(side=LEFT)
        Button(botonera, text="Generar Reportes").pack(side=LEFT)

        self.ventana.mainloop()
    
    def mostrar(self):
        self.ventana.mainloop()
        
