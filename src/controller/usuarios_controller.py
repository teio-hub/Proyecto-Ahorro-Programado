import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.Usuario import Usuario
import secret_config

class UsuariosController:

    def obtener_cursor():
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        cursor = connection.cursor()
        return cursor

    def crear_tabla():
        cursor = UsuariosController.obtener_cursor()
        with open("sql/crear-usuarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = UsuariosController.obtener_cursor()
        cursor.execute("drop table if exists usuarios;")
        cursor.connection.commit()

    def insertar(usuario: Usuario):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""insert into usuarios (cedula, nombre, apellido, telefono, correo, direccion)
                    values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}',
                    '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}')"""
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar(cedula):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"select cedula, nombre, apellido, telefono, correo, direccion from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = Usuario(cedula=fila[0], nombre=fila[1], apellido=fila[2], telefono=fila[3], correo=fila[4], direccion=fila[5])
        return resultado

    def modificar(usuario: Usuario):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""update usuarios set nombre='{usuario.nombre}', apellido='{usuario.apellido}',
                    telefono='{usuario.telefono}', correo='{usuario.correo}', direccion='{usuario.direccion}'
                    where cedula='{usuario.cedula}'"""
        cursor.execute(consulta)
        cursor.connection.commit()

    def eliminar(cedula):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"delete from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        cursor.connection.commit()