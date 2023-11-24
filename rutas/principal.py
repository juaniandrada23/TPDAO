from ventana_principal import VentanaPrincipal
from biblioteca import Biblioteca


biblioteca = Biblioteca()
VentanaPrincipal().mostrar()
cantidades = biblioteca.cantidadPorTipo()
print("Cantidad de libros disponibles: " + str(cantidades[0]))
print("Cantidad de libros prestados: " + str(cantidades[1]))
print("Cantidad de libros extraviados: " + str(cantidades[2]))
print(biblioteca.totalPrecioLibros())
print(biblioteca.listadoPrestamosSocio())
print(biblioteca.listadoPrestamosDemorados())


