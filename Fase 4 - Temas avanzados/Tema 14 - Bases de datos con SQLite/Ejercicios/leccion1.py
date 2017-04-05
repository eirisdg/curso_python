import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuarios ("
#               "nombre VARCHAR (100), "
#               "edad INTEGER, "
#               "email VARCHAR (100))")

#cursor.execute("INSERT INTO usuarios VALUES ('Hector', 19, 'Hector@gmail.com')")

#cursor.execute("SELECT * FROM usuarios")

#print(cursor.fetchone())

#usuarios = [
#    ("Manolo", 39, "manolo@gmail.com"),
#    ("Felipe", 38, "eldormio@ejemplo.com"),
#    ("Juan", 18, "elmejon@ejemplo.com"),
#]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

#cursor.execute("SELECT * FROM usuarios")
#usuarios = cursor.fetchall()



conexion.commit()
conexion.close()