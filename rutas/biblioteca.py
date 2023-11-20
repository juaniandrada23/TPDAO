from libro_controller import *

class Biblioteca():
    
    def __init__(self):
        self.libros = leerDatosLibro()
        
    def agregar(self,libro):
        self.libros.append(libro)
    

