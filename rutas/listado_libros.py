from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox
from libro_controller import *

class VentanaListadoLibros:
    
    def __init__(self, biblioteca):
        self.ventana = Tk()
        self.ventana.title("Listado de Libros")
        self.ventana.geometry("500x300")
        self.biblioteca = biblioteca

        self.configurar_estilos()

        self.grilla = Treeview(self.ventana, columns=("A", "B", "C", "D"), height=400)
        self.grilla.column("#0", width=0, stretch=NO)  # ancho en 0
        self.grilla.column("A", width=100)
        self.grilla.column("B", width=100)
        self.grilla.column("C", width=100)
        self.grilla.column("D", width=100)
        self.grilla.heading("#0", text="", anchor=W)  # encabezado vacio
        self.grilla.heading("A", text="Código")        
        self.grilla.heading("B", text="Título")        
        self.grilla.heading("C", text="Precio")        
        self.grilla.heading("D", text="Estado")
        self.grilla.pack(fill=BOTH)
        self.grilla.bind("<Double-1>",self.eliminarFila)

        for libro in self.biblioteca.libros:
            self.grilla.insert("", END, values=(libro[0], libro[1], libro[2], libro[3]))

    def configurar_estilos(self):
        style = ttk.Style()
        style.configure("Treeview.heading",
                        background="#E0E1DD",
                        foreground="black",
                        fieldbackground="#E0E1DD",
                        font=('Monserrat', 10, 'bold'))

        style.map("Treeview",
                  background=[('selected', '#2980b9')])

    def eliminarFila(self,event):
        item = self.grilla.focus()
        x = messagebox.askquestion('Información','¿Seguro que desea eliminar el libro?')
        cod_libro_seleccionado = self.grilla.item(item)['values'][0]
        if x == 'yes':
            self.grilla.delete(item)
            eliminarLibro(cod_libro_seleccionado)
    
    
    def mostrar(self):
        self.ventana.mainloop()