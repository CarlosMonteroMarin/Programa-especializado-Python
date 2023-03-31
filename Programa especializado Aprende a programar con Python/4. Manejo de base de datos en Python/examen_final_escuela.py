import sqlite3

# Crear la conexión a la base de datos
conn = sqlite3.connect('escuela.db')

# Crear la tabla de alumnos
conn.execute('''CREATE TABLE alumnos
            (id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            curso TEXT NOT NULL);''')

# Crear la tabla de profesores
conn.execute('''CREATE TABLE profesores
            (id_profesor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL);''')

# Crear la tabla de cursos
conn.execute('''CREATE TABLE cursos
            (id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL);''')

# Crear la tabla de horarios
conn.execute('''CREATE TABLE horarios
            (id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
            dia_semana TEXT NOT NULL,
            hora_desde TEXT NOT NULL,
            hora_hasta TEXT NOT NULL,
            id_profesor INTEGER NOT NULL,
            id_curso INTEGER NOT NULL,
            FOREIGN KEY(id_profesor) REFERENCES profesores(id_profesor),
            FOREIGN KEY(id_curso) REFERENCES cursos(id_curso));''')

    # Guardar los cambios y cerrar la conexión
conn.commit()


def agregar_alumno(nombre, curso):
    conn.execute("INSERT INTO alumnos (nombre, curso) VALUES (?, ?)", (nombre, curso))
    conn.commit()

# Agregar un profesor
def agregar_profesor(nombre):
    conn.execute("INSERT INTO profesores (nombre) VALUES (?)", (nombre,))
    conn.commit()

# Agregar un curso
def agregar_curso(nombre):
    conn.execute("INSERT INTO cursos (nombre) VALUES (?)", (nombre,))
    conn.commit()

# Asignar un profesor a un curso en un horario
def agregar_horario(dia_semana, hora_desde, hora_hasta, id_profesor, id_curso):
    conn.execute("INSERT INTO horarios (dia_semana, hora_desde, hora_hasta, id_profesor, id_curso) VALUES (?, ?, ?, ?, ?)", (dia_semana, hora_desde, hora_hasta, id_profesor, id_curso))
    conn.commit()

# Ejemplos de uso
agregar_alumno('Juan', 'Matemáticas')
agregar_profesor('María')
agregar_curso('Matemáticas')
agregar_horario('Lunes', '08:00', '10:00', 1, 1)



def obtener_alumnos_curso(nombre_curso):
    cursor = conn.execute("SELECT nombre FROM alumnos WHERE curso=?", (nombre_curso,))
    alumnos = [row[0] for row in cursor.fetchall()]
    return alumnos

# Obtener el horario de un profesor
def obtener_horario_profesor(nombre_profesor):
    cursor = conn.execute("SELECT horarios.dia_semana, horarios.hora_desde, horarios.hora_hasta, cursos.nombre FROM horarios JOIN profesores ON horarios.id_profesor = profesores.id_profesor JOIN cursos ON horarios.id_curso = cursos.id_curso WHERE profesores.nombre=?", (nombre_profesor,))
    horario = cursor.fetchall()
    return horario

# Obtener el horario de un curso
def obtener_horario_curso(nombre_curso):
    cursor = conn.execute("SELECT horarios.dia_semana, horarios.hora_desde, horarios.hora_hasta, profesores.nombre FROM horarios JOIN cursos ON horarios.id_curso = cursos.id_curso JOIN profesores ON horarios.id_profesor = profesores.id_profesor WHERE cursos.nombre=?", (nombre_curso,))
    horario = cursor.fetchall()
    return horario


print(obtener_alumnos_curso('Matemáticas'))
print(obtener_horario_profesor('María'))
print(obtener_horario_curso('Matemáticas'))

# Cerramar la conexion
conn.close()

