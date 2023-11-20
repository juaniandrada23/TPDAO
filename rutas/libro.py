class Libro:
    def __init__(self, codigo, titulo, precio, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.estado = estado
    

    def getCodigo(self):
        return self.codigo

    def getTitulo(self):
        return self.titulo
    
    def getPrecio(self):
        return self.precio
    
    def getEstado(self):
        return self.estado
    
    def __str__(self):
        return f"{self.codigo} {self.titulo} {self.precio} {self.estado}"
