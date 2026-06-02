import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.Abono import Abono
import secret_config

class AbonosController:

    def obtener_cursor():
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        cursor = connection.cursor()
        return cursor

    def crear_tabla():
        cursor = AbonosController.obtener_cursor()
        with open("sql/crear-abonos.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = AbonosController.obtener_cursor()
        cursor.execute("drop table if exists abonos;")
        cursor.connection.commit()

    def insertar(abono: Abono):
        cursor = AbonosController.obtener_cursor()
        consulta = f"""insert into abonos (id_plan, mes_abono, valor_abono, nueva_cuota)
                    values ({abono.id_plan}, {abono.mes_abono}, {abono.valor_abono}, {abono.nueva_cuota})
                    returning id_abono"""
        cursor.execute(consulta)
        cursor.connection.commit()
        return cursor.fetchone()[0]

    def buscar(id_abono):
        cursor = AbonosController.obtener_cursor()
        consulta = f"""select id_abono, id_plan, mes_abono, valor_abono, nueva_cuota
                    from abonos where id_abono = {id_abono}"""
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = Abono(id_abono=fila[0], id_plan=fila[1], mes_abono=fila[2], valor_abono=fila[3], nueva_cuota=fila[4])
        return resultado

    def buscar_por_plan(id_plan):
        cursor = AbonosController.obtener_cursor()
        consulta = f"""select id_abono, id_plan, mes_abono, valor_abono, nueva_cuota
                    from abonos where id_plan = {id_plan}"""
        cursor.execute(consulta)
        filas = cursor.fetchall()
        resultado = []
        for fila in filas:
            abono = Abono(id_abono=fila[0], id_plan=fila[1], mes_abono=fila[2], valor_abono=fila[3], nueva_cuota=fila[4])
            resultado.append(abono)
        return resultado

    def modificar(abono: Abono):
        cursor = AbonosController.obtener_cursor()
        consulta = f"""update abonos set mes_abono={abono.mes_abono}, valor_abono={abono.valor_abono},
                    nueva_cuota={abono.nueva_cuota}
                    where id_abono={abono.id_abono}"""
        cursor.execute(consulta)
        cursor.connection.commit()

    def eliminar(id_abono):
        cursor = AbonosController.obtener_cursor()
        consulta = f"delete from abonos where id_abono = {id_abono}"
        cursor.execute(consulta)
        cursor.connection.commit()
