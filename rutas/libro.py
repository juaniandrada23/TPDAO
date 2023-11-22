from prestamos import Prestamo
from socio import Socio
from prestamo_controller import *


class Libro:
    def __init__(self, codigo, titulo, precio, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.estado = estado
        # self.prestamos = leerDatosPrestamo()

    def getCodigo(self):
        return self.codigo

    def getTitulo(self):
        return self.titulo
    
    def getPrecio(self):
        return self.precio
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self,estado):
        self.estado = estado
    
    # def registrar_prestamo(self, socio: Socio, dias):
    #     prestamo = Prestamo(self, socio, dias)
    #     self.prestamos.append(prestamo)
    #     socio.registrar_prestamo(prestamo)


    def __str__(self):
        return f"{self.codigo} {self.titulo} {self.precio} {self.estado}"
