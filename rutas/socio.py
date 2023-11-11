class Socio:
    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self) -> str:
        return f"{self.dni} {self.nombre} {self.apellido}"