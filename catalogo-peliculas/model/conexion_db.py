import os
import sqlite3

class ConexionDB():
    def __init__(self):
        self.base_datos = os.path.join(os.path.dirname(__file__), '..', 'database/peliculas.db')
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
    