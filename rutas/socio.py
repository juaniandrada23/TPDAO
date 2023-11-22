class Socio:
    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.prestamos = []
    
    def getDni(self):
        return self.dni

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
    
    
    def __str__(self) -> str:
        return f"{self.dni} {self.nombre} {self.apellido}"