import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.PlanAhorro import PlanAhorro
import secret_config

class PlanesController:

    def obtener_cursor():
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        cursor = connection.cursor()
        return cursor

    def crear_tabla():
        cursor = PlanesController.obtener_cursor()
        with open("sql/crear-planes.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = PlanesController.obtener_cursor()
        cursor.execute("drop table if exists planes_ahorro;")
        cursor.connection.commit()

    def insertar(plan: PlanAhorro):
        cursor = PlanesController.obtener_cursor()
        consulta = f"""insert into planes_ahorro (cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion)
                    values ('{plan.cedula}', {plan.meta}, {plan.tasa_interes}, {plan.plazo},
                    {plan.cuota_mensual}, '{plan.fecha_creacion}')"""
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar(id_plan):
        cursor = PlanesController.obtener_cursor()
        consulta = f"""select id_plan, cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion
                    from planes_ahorro where id_plan = {id_plan}"""
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = PlanAhorro(id_plan=fila[0], cedula=fila[1], meta=fila[2], tasa_interes=fila[3], plazo=fila[4], cuota_mensual=fila[5], fecha_creacion=fila[6])
        return resultado

    def buscar_por_cedula(cedula):
        cursor = PlanesController.obtener_cursor()
        consulta = f"""select id_plan, cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion
                    from planes_ahorro where cedula = '{cedula}'"""
        cursor.execute(consulta)
        filas = cursor.fetchall()
        resultado = []
        for fila in filas:
            plan = PlanAhorro(id_plan=fila[0], cedula=fila[1], meta=fila[2], tasa_interes=fila[3], plazo=fila[4], cuota_mensual=fila[5], fecha_creacion=fila[6])
            resultado.append(plan)
        return resultado

    def modificar(plan: PlanAhorro):
        cursor = PlanesController.obtener_cursor()
        consulta = f"""update planes_ahorro set meta={plan.meta}, tasa_interes={plan.tasa_interes},
                    plazo={plan.plazo}, cuota_mensual={plan.cuota_mensual}
                    where id_plan={plan.id_plan}"""
        cursor.execute(consulta)
        cursor.connection.commit()

    def eliminar(id_plan):
        cursor = PlanesController.obtener_cursor()
        consulta = f"delete from planes_ahorro where id_plan = {id_plan}"
        cursor.execute(consulta)
        cursor.connection.commit()