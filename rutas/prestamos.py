import datetime
from datetime import timedelta

class Prestamo:
    def __init__(self, codigo_libro, id_socio, dias):
        self.codigo_libro = codigo_libro
        self.id_socio = id_socio
        self.dias = dias
        self.fecha_prestamo = datetime.datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=self.dias)
        self.dias_retraso = self.registrar_devolucion

    def getCodigoLibro(self):
        return self.codigo_libro


    def getIdSocio(self):
        return self.id_socio
    
    def getDias(self):
        return self.dias
    
    def getFechaPrestamo(self):
        return self.fecha_prestamo

    def getFechaDev(self):
        return self.fecha_devolucion
    
    def getDiasRetraso(self):
        return self.dias_retraso
    
    def registrar_devolucion(self):
        fecha_devolucion = datetime.datetime.now()
        fecha_prestamo = self.fecha_prestamo
        conv1 = fecha_devolucion.strftime('%Y-%m-%d')
        conv2 = fecha_prestamo.strftime('%Y-%m-%d')
        dias_retraso = ((fecha_devolucion-fecha_prestamo).days) - self.dias
        return dias_retraso

