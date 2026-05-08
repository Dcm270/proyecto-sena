import os
import sqlite3

# Ruta absoluta al archivo gestion.db (junto a este config.py)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gestion.db")


def conectar():
    """Abre y retorna una conexion a la base de datos SQLite 'gestion.db'."""
    try:
        conexion = sqlite3.connect(DB_PATH)
        conexion.row_factory = sqlite3.Row  # acceso por nombre de columna
        return conexion
    except sqlite3.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None


def desconectar(conexion):
    if conexion is not None:
        conexion.close()
        print("Conexion a la base de datos cerrada")


if __name__ == "__main__":
    conexion = conectar()
    if conexion is not None:
        print("Conexion a la base de datos establecida correctamente")
        desconectar(conexion)
    else:
        print("Error al conectar. No se pudo establecer la conexion.")
