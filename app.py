import sys
sys.path.append("src")

from flask import Flask, render_template, request
from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro

server = Flask(__name__)

@server.route("/")
def inicio():
    return render_template("planes.html")

# Crea las tablas en la base de datos
@server.route("/crear_tablas")
def crear_tablas():
    try:
        PlanesController.crear_tabla()
        return "Tablas creadas exitosamente. Ya puede usar la aplicación"
    except Exception as e:
        return "Las tablas ya existen. Ya puede usar la aplicación"

# Inserta un plan en la base de datos
@server.route("/insertar_plan")
def insertar_plan():
    plan = PlanAhorro(
        id_plan=None,
        cedula=request.args["cedula"],
        meta=float(request.args["meta"].replace(".", "")),
        tasa_interes=float(request.args["tasa_interes"]),
        plazo=int(request.args["plazo"]),
        cuota_mensual=float(request.args["cuota_mensual"].replace(".", "")),
        fecha_creacion=request.args["fecha_creacion"]
    )
    id_plan = PlanesController.insertar(plan)
    return f"Se guardó exitosamente el plan. Su ID es: {id_plan}"

# Busca un plan por ID y muestra sus datos
@server.route("/buscar_plan")
def buscar_plan():
    try:
        id_plan = int(request.args["id_plan"])
        plan = PlanesController.buscar(id_plan)
        return render_template("plan_buscado.html", plan=plan)
    except Exception as e:
        return "No se encontró ningún plan con ese ID."
    
if __name__ == '__main__':
    server.run(debug=True)