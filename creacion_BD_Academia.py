# --------------------------------
# CONEXIÓN Y CREACIÓN DE LA BD
# --------------------------------

import sqlite3

try:
conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

# Crear la tabla de cursos
cursor.execute("""
CREATE TABLE IF NOT EXISTS T_CURSOS (
id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
nombre VARCHAR(100) NOT NULL,
descripcion TEXT,
precio REAL NOT NULL,
horario VARCHAR(25) NOT NULL

)
""")

# Datos iniciales
cursor.execute(
"INSERT OR IGNORE INTO T_CURSOS VALUES (null,?,?,?,?)",
("Python Básico", "Curso de Python iniciación",300,'Mañanas')
)

cursor.execute(
"INSERT OR IGNORE INTO T_CURSOS VALUES (null,?,?,?,?)",
("Python Avanzado", "Curso de Python Avanzado",500,'Tardes')
)




conexion.commit()

print("Base de datos creada correctamente.")

except sqlite3.Error as error:
print("Se ha producido un error con la base de datos:", error)

finally:
try:
conexion.close()
except NameError:
pass