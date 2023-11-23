import sqlite3 as sql
from prestamos import Prestamo

def createTablePrestamo():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Prestamos
             (
             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             codigo_libro INTEGER NOT NULL,
             id_socio INTEGER NOT NULL,
             dias INTEGER NOT NULL,
             fecha_prestamo TEXT NOT NULL,
             fecha_devolucion TEXT NOT NULL,
             dias_retraso INTEGER NOT NULL,
             FOREIGN KEY (codigo_libro) REFERENCES Libros(codigo),
             FOREIGN KEY (id_socio) REFERENCES Socios(dni));''')
    
    conn.commit()
    conn.close()

def deleteTable():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"DROP TABLE Prestamos"
    cursor.execute(query)
    conn.commit()
    conn.close()

def registrarPrestamo(p: Prestamo):
        try:
            conn = sql.connect("biblioteca.db")
            cursor = conn.cursor()
            codigo_libro = p.getCodigoLibro()
            id_socio = p.getIdSocio()
            dias = p.getDias()
            fecha_prestamo = p.getFechaPrestamo()
            fecha_devolucin = p.getFechaDev()
            dias_retraso = p.dias_retraso()
            query = f"INSERT INTO Prestamos VALUES (NULL,?,?,?,?,?,?)"
            cursor.execute(query,[codigo_libro,id_socio,dias,fecha_prestamo,fecha_devolucin,dias_retraso])
            conn.commit()
            conn.close()
        except sql.OperationalError as error:
            print("Error al abrir: ", error)

def leerDatosPrestamo():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Prestamos"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def puedeTomarPrestado(dni):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM Prestamos WHERE id_socio={dni}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(datos) < 3: 
        return True
    else: 
        return False
    
def getTituloLibroPrestado(codigo):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT codigo_libro FROM Prestamos WHERE codigo_libro={codigo}"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def eliminarPrestamo(codigo):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"DELETE FROM Prestamos WHERE codigo_libro={codigo}"
    cursor.execute(query)
    conn.commit()
    conn.close()

def getLibrosDemorados():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    query = f"SELECT codigo_libro FROM Prestamos WHERE dias_retraso > 30"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    array = [item[0] for item in datos]
    return array
