from tkinter import *
from tkinter.ttk import Treeview

class VentanaListadoLibros:
    
    def __init__(self, padron):
        
        self.ventana = Tk()
        
        grilla = Treeview(self.ventana,columns=("A", "B", "C", "D"), height=200)
        grilla.column("#0",width=0)
        grilla.column("A",width=50)
        grilla.column("B",width=150)
        grilla.column("C",width=150)
        grilla.column("D",width=50)
        grilla.heading("A",text="codigo")        
        grilla.heading("B",text="titulo")        
        grilla.heading("C",text="precio")        
        grilla.heading("D",text="estado")
        grilla.pack(fill=BOTH)
        
        for p in padron.libros:
            grilla.insert("", END, values = (p.codigo, p.titulo, p.precio, p.estado))        
        
        
    def mostrar(self):
        self.ventana.mainloop()
