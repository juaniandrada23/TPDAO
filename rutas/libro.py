class Libro:
    def __init__(self, codigo, titulo, precio, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.estado = estado
    
    def __str__(self):
        return f"{self.codigo} {self.titulo} {self.precio} {self.estado}"
