import sqlite3 as sql
from libro import Libro
from prestamo_controller import *

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

def buscarLibro(codigo,titulo):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Libros WHERE codigo = {codigo} AND titulo='{titulo}'"
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

def listarLibrosDemorados():
    codigosDemorados = getLibrosDemorados()
    array = []
    for c in codigosDemorados:
        conn = sql.connect("biblioteca.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM Libros WHERE codigo={c}"
        cursor.execute(query)
        array.append(cursor.fetchall())
        conn.commit()
        conn.close()
    return array


def eliminarLibro(codigo):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"DELETE FROM Libros WHERE codigo = {codigo}"
    cursor.execute(query)
    conn.commit()
    conn.close()