from libro_controller import *
from socio_controller import *
from prestamo_controller import *

class Biblioteca():
    
    def __init__(self):
        self.libros = leerDatosLibro()
        self.libros_extraviados = listarLibrosDemorados()
        self.socios = leerDatosSocio()
        self.prestamos = prestamosPorSocio()
        
    def cantidadPorTipo(self):
        l = [0,0,0]
        disponibles = 0
        prestados = 0
        extraviados = 0
        for e in self.libros:
            if e[3] == 'disponible':
                disponibles += 1
            elif e[3] == 'prestado':
                prestados += 1
            elif e[3] == 'extraviado':
                extraviados += 1
        l = [disponibles,prestados,extraviados]
        return l
    
    def convertir_array_de_arrays(self):
        array_solo = []
        for subarray in self.libros_extraviados:
            array_solo.extend(subarray)
        return array_solo
    
    
    def totalPrecioLibros(self):
        libros_ext = self.convertir_array_de_arrays()
        return sum([l[2] for l in libros_ext])
    
    def listadoPrestamosSocio(self):
        aux = f"Listado de prestamos por socio:\n"
        for socio in self.prestamos:
            aux += f"Socio de DNI:{socio[2]} Libro nro: {socio[1]}\n"
        return aux
    
    def listadoPrestamosDemorados(self):
        demorados = prestamosDemorados()
        aux = f"Listado de prestamos demorados:\n"
        for demorado in demorados:
            aux += f"Prestamo nro:{demorado[0]} Libro nro: {demorado[1]} DNI del socio: {demorado[2]} Días de retraso: {demorado[6]}\n"
        return aux


    

