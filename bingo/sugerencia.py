import datetime

class Libro:
    def __init__(self, codigo, titulo, precio, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.estado = estado
        self.prestamos = []

    def registrar_prestamo(self, socio, dias):
        prestamo = Prestamo(self, socio, dias)
        self.prestamos.append(prestamo)
        socio.registrar_prestamo(prestamo)

    def registrar_devolucion(self, prestamo, dias_retraso):
        prestamo.registrar_devolucion(dias_retraso)
        if dias_retraso > 30:
            self.estado = 'extraviado'

    def esta_extraviado(self):
        return self.estado == 'extraviado'

class Socio:
    def __init__(self, numero):
        self.numero = numero
        self.prestamos = []

    def puede_tomar_prestado(self):
        if len(self.prestamos) >= 3:
            return False
        for prestamo in self.prestamos:
            if prestamo.libro.esta_extraviado():
                return False
        return True

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo.libro.titulo)

class Prestamo:
    def __init__(self, libro, socio, dias):
        self.libro = libro
        self.socio = socio
        self.dias = dias
        self.fecha_prestamo = datetime.now()

    def registrar_devolucion(self, dias_retraso):
        self.fecha_devolucion = datetime.now()
        self.dias_retraso = (self.fecha_devolucion - self.fecha_prestamo).days - self.dias

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.socios = []

    def administrar_libros(self):
        pass

    def administrar_socios(self):
        pass

    def registrar_prestamo(self, libro, socio, dias):
        libro.registrar_prestamo(socio, dias)

    def registrar_devolucion(self, prestamo, dias_retraso):
        prestamo.libro.registrar_devolucion(prestamo, dias_retraso)

    def listar_libros_extraviados(self):
        for libro in self.libros:
            if libro.esta_extraviado():
                print(libro.titulo)

    def listar_libros_por_estado(self):
        estados = {}
        for libro in self.libros:
            if libro.estado in estados:
                estados[libro.estado] += 1
            else:
                estados[libro.estado] = 1
        for estado, cantidad in estados.items():
            print(f'{cantidad} libros en estado {estado}')

    def sumatoria_precio_reposicion_libros_extraviados(self):
        total = 0
        for libro in self.libros:
            if libro.esta_extraviado():
                total += libro.precio
        print(f'Sumatoria del precio de reposición de todos los libros extraviados: {total}')
