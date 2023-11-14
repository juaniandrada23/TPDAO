import sqlite3 as sql

def createBd():
    conn = sql.connect("biblioteca.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Libros (
    codigo INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    precio_reposicion REAL NOT NULL,
    estado TEXT NOT NULL CHECK(estado IN ('disponible', 'prestado', 'extraviado'))
        )""")
    
    conn.commit()
    conn.close()

def insertarLibro(codigo,titulo,precio_reposicion,estado):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Libros VALUES ({codigo},'{titulo}',{precio_reposicion},'{estado}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def leerDatosLibro():
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Libros"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print (datos)


def insertarLibros(librosList):
    conn = sql.connect("biblioteca.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Libros VALUES (?,?,?,?)"
    cursor.executemany(instruccion,librosList)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createBd()
    #createTable()
    #insertarLibro(1,"Harry Potter",980,"disponible")
    libros = [(2,"G Beder",150,"prestado"),
              (3,"Paren La Hand",431,"disponible"),
              (4,"Don Quijote",1028,"disponible"),
              (5,"Fisica 2",120,"extraviado")]
    
    insertarLibros(libros)
    
    
    leerDatosLibro()