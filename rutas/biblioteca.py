from libro_controller import *

class Biblioteca():
    
    def __init__(self):
        self.libros = leerDatosLibro()
        self.libros_extraviados = listarLibrosDemorados()
        self.socios = []
        
    def agregar(self,libro):
        self.libros.append(libro)
    

