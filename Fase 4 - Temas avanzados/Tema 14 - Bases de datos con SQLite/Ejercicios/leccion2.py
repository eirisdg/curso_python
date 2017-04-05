import sqlite3
conexion = sqlite3.connect("ejemplo2.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
    dni VARCHAR (9) PRIMARY KEY,
    nombre VARCHAR (100), 
    edad INTEGER, 
    email VARCHAR (100)
    )
    ''')

usuarios = [
    ("45221478Z","Manolo", 39, "manolo@gmail.com"),
    ("99665544F","Felipe", 38, "eldormio@ejemplo.com"),
    ("44778855A","Juan", 18, "elmejon@ejemplo.com"),
]

cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?, ?)", usuarios)

conexion.commit()
conexion.close()