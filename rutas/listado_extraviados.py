from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk

class VentanaListadoExtraviados:
    
    def __init__(self, biblioteca):
        self.ventana = Tk()
        self.ventana.title("Listado de Libros")
        self.ventana.geometry("500x300")

        self.configurar_estilos()

        grilla = Treeview(self.ventana, columns=("A", "B", "C", "D"), height=400)
        grilla.column("#0", width=0, stretch=NO)  # ancho en 0
        grilla.column("A", width=100)
        grilla.column("B", width=100)
        grilla.column("C", width=100)
        grilla.column("D", width=100)
        grilla.heading("#0", text="", anchor=W)  # encabezado vacio
        grilla.heading("A", text="Código")        
        grilla.heading("B", text="Título")        
        grilla.heading("C", text="Precio")        
        grilla.heading("D", text="Estado")
        grilla.pack(fill=BOTH)

        for libro in biblioteca.libros_extraviados:
            grilla.insert("", END, values=(libro[0][0], libro[0][1], libro[0][2], libro[0][3]))

    def configurar_estilos(self):
        style = ttk.Style()
        style.configure("Treeview.heading",
                        background="#E0E1DD",
                        foreground="black",
                        fieldbackground="#E0E1DD",
                        font=('Monserrat', 10, 'bold'))

        style.map("Treeview",
                  background=[('selected', '#2980b9')])

    def mostrar(self):
        self.ventana.mainloop()