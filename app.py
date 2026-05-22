import sys
sys.path.append("src")

# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo
from flask import Flask, render_template, request

from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro

# Flask constructor
app = Flask(__name__)

# Muestra el menú principal de la aplicación
@app.route("/")
def index():
    return render_template("index.html")

# Muestra el formulario para crear un nuevo plan de ahorro
@app.route("/planes/nuevo")
def formulario_plan():
    return render_template("plan_nuevo.html")

# Recibe los datos del formulario e inserta un nuevo plan en la base de datos
@app.route("/planes/insertar")
def insertar_plan():
    cedula = request.args["cedula"]
    meta = float(request.args["meta"])
    tasa_interes = float(request.args["tasa_interes"])
    plazo = int(request.args["plazo"])
    cuota_mensual = float(request.args["cuota_mensual"])
    fecha_creacion = request.args["fecha_creacion"]
    plan = PlanAhorro(id_plan=None, cedula=cedula, meta=meta,
                      tasa_interes=tasa_interes, plazo=plazo,
                      cuota_mensual=cuota_mensual, fecha_creacion=fecha_creacion)
    PlanesController.insertar(plan)
    return render_template("plan_insertado.html", cedula=cedula, meta=meta)

# Muestra el formulario para buscar un plan por ID
@app.route("/planes/buscar")
def formulario_buscar_plan():
    return render_template("plan_buscar.html")

# Recibe el ID del plan y muestra sus datos
@app.route("/planes/resultado")
def resultado_plan():
    id_plan = int(request.args["id_plan"])
    plan = PlanesController.buscar(id_plan)
    return render_template("plan_resultado.html", plan=plan)

if __name__ == '__main__':
    app.run(debug=True)