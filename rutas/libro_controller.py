import sqlite3 as sql
from libro import Libro

def createBd():
    conn = sql.connect("biblioteca.db")
    conn.commit()
    conn.close()

def createTableLibro():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Libros (
    codigo INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    precio_reposicion REAL NOT NULL,
    estado TEXT NOT NULL CHECK(estado IN ('disponible', 'prestado', 'extraviado'))
        )""")
    
    conn.commit()
    conn.close()

def registrarLibro(l: Libro):
    try:
        conn = sql.connect("biblioteca.db")
        cursor = conn.cursor()
        codigo = l.getCodigo()
        titulo = l.getTitulo()
        precio = l.getPrecio()
        estado = l.getEstado()
        query = f"INSERT INTO Libros VALUES (?,?,?,?)"
        cursor.execute(query,[codigo, titulo, precio, estado])
        conn.commit()
        conn.close()
    except sql.OperationalError as error:
        print("Error al abrir: ", error)

def leerDatosLibro():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Libros"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos


def insertarLibros(librosList):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Libros VALUES (?,?,?,?)"
    cursor.executemany(instruccion,librosList)
    conn.commit()
    conn.close()

def buscarLibroDisponible(codigo,estado):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Libros WHERE codigo = {codigo} AND estado='{estado}'"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(datos) > 0:
        return True
    else: 
        return False


def actualizarEstado(codigo,estado):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"UPDATE Libros SET estado = '{estado}' WHERE codigo = {codigo}"
    cursor.execute(query)
    conn.commit()
    conn.close() 
    


# if __name__ == "__main__":
#     #createBd()
#     #createTable()
#     #insertarLibro(1,"Harry Potter",980,"disponible")
#     libros = [(2,"G Beder",150,"prestado"),
#               (3,"Paren La Hand",431,"disponible"),
#               (4,"Don Quijote",1028,"disponible"),
#               (5,"Fisica 2",120,"extraviado")]
    
#     insertarLibros(libros)
    
    
#     leerDatosLibro()