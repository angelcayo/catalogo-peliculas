from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARHCAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('Crear Registro', 'Se creo la tabla en la base de datos')
    except:
        messagebox.showwarning('Crear Registro', 'La tabla ya esta creada')

def borrar_tabla():
    conexion = ConexionDB()
    sql = '''
    DROP TABLE peliculas
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('Borrar Registro', 'La tabla de base de datos se borro con éxito')
    except:
        messagebox.showwarning('Borrar Registro', 'No hay tabla para borrar')

class Pelicula():
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def guardar(pelicula):
    conexion = ConexionDB()
    sql = f'''
    INSERT INTO peliculas(nombre, duracion, genero)
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Conexion al Registro', 'La tabla pelicula no esta creado en la base de datos')

def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = '''
    SELECT * FROM peliculas
    ORDER BY id_pelicula DESC
    '''
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showwarning('Conexion al Registro', 'Crea la tabla en la base de datos')
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f'''
    UPDATE peliculas
    SET nombre = '{pelicula.nombre}',
        duracion = '{pelicula.duracion}',
        genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Conexion al Registro', 'No se pudo editar este registro')

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'''
    DELETE FROM peliculas
    WHERE id_pelicula = {id_pelicula}
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Conexion al Registro', 'No se puedo eliminar el registro')