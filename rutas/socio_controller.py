import sqlite3 as sql
from socio import Socio

def createTableSocio():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Socios (
    dni INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL
        )""")
    
    conn.commit()
    conn.close()

def registrarSocio(s: Socio):
    try:
        conn = sql.connect("biblioteca.db")
        cursor = conn.cursor()
        dni = s.getDni()
        nombre = s.getNombre()
        apellido = s.getApellido()
        query = f"INSERT INTO Socios VALUES (?,?,?)"
        cursor.execute(query,[dni,nombre, apellido])
        conn.commit()
        conn.close()
    except sql.OperationalError as error:
        print("Error al abrir: ", error)

def leerDatosSocio():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Socios"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def buscarSocio(dni):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Socios WHERE dni = {dni}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(datos) > 0:
        return True
    else: 
        return False

def eliminarSocio(dni):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"DELETE FROM Socios WHERE dni = {dni}"
    cursor.execute(query)
    conn.commit()
    conn.close()