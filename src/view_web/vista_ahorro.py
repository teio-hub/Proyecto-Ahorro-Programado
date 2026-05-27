import sys
sys.path.append("src")

from flask import Blueprint
from flask import render_template, request
from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro
from controller.usuarios_controller import UsuariosController
from model.Usuario import Usuario
from controller.abonos_controller import AbonosController
from model.Abono import Abono

#Para crear un blueprint, se indica por parametro:
# -Nombre del Blueprint (informativo)
#- Nombre del módulo con la variable __name__
#- Carpeta donde se almacenan los templates
blueprint = Blueprint("vista_ahorro",__name__)

#MODULO PLANES
@blueprint.route("/")
def inicio():
    return render_template("planes.html")

@blueprint.route("/planes")
def planes():
    return render_template("planes.html")

# Crea las tablas en la base de datos
@blueprint.route("/crear_tablas")
def crear_tablas():
    try:
        PlanesController.crear_tabla()
        UsuariosController.crear_tabla()
        AbonosController.crear_tabla()
        return "Tablas creadas exitosamente. Ya puede usar la aplicación"
    except Exception as e:
        return "Las tablas ya existen. Ya puede usar la aplicación"

# Inserta un plan en la base de datos
@blueprint.route("/insertar_plan")
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
    return f"Se guardó exitosamente el plan para la cédula: {request.args['cedula']} con el ID: {id_plan}.<br /><a href='/'>Volver al inicio</a>"

# Busca un plan por ID y muestra sus datos
@blueprint.route("/buscar_plan")
def buscar_plan():
    try:
        cedula = request.args["cedula"]
        planes = PlanesController.buscar_por_cedula(cedula)
        if len(planes) == 0:
            return "No se encontró ningún plan para esa cédula."
        return render_template("plan_buscado.html", planes=planes)
    except Exception as e:
        return "No se encontró ningún plan para esa cédula."
    
# Muestra el formulario de modificar con los datos actuales del plan
@blueprint.route("/modificar_plan")
def modificar_plan():
    try:
        id_plan = int(request.args["id_plan"])
        plan = PlanesController.buscar(id_plan)
        return render_template("plan_modificar.html", plan=plan)
    except Exception as e:
        return "No se encontró ningún plan con ese ID."

# Guarda los cambios del plan modificado
@blueprint.route("/actualizar_plan")
def actualizar_plan():
    plan = PlanAhorro(
        id_plan=int(request.args["id_plan"]),
        cedula=request.args["cedula"],
        meta=float(request.args["meta"].replace(".", "")),
        tasa_interes=float(request.args["tasa_interes"]),
        plazo=int(request.args["plazo"]),
        cuota_mensual=float(request.args["cuota_mensual"].replace(".", "")),
        fecha_creacion=request.args["fecha_creacion"]
    )
    PlanesController.modificar(plan)
    return f"Plan modificado exitosamente. <a href='/'>Volver al inicio</a>"

# Elimina un plan de la base de datos
@blueprint.route("/eliminar_plan")
def eliminar_plan():
    id_plan = int(request.args["id_plan"])
    PlanesController.eliminar(id_plan)
    return "Plan eliminado exitosamente. <a href='/'>Volver al inicio</a>"

#MODULO USUARIOS

# Muestra el formulario de usuarios
@blueprint.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

# Inserta un usuario en la base de datos
@blueprint.route("/insertar_usuario")
def insertar_usuario():
    usuario = Usuario(
        cedula=request.args["cedula"],
        nombre=request.args["nombre"],
        apellido=request.args["apellido"],
        telefono=request.args["telefono"],
        correo=request.args["correo"],
        direccion=request.args["direccion"]
    )
    UsuariosController.insertar(usuario)
    return f"Se guardó exitosamente el usuario con cédula: {request.args['cedula']}"

# Busca un usuario por cédula
@blueprint.route("/buscar_usuario")
def buscar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuariosController.buscar(cedula)
        return render_template("usuario_buscado.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula. <br /><a href='/'>Volver al inicio</a>"

# Muestra el formulario de modificar con los datos actuales
@blueprint.route("/modificar_usuario")
def modificar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuariosController.buscar(cedula)
        return render_template("usuario_modificar.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula. <br /><a href='/'>Volver al inicio</a>"

# Guarda los cambios del usuario modificado
@blueprint.route("/actualizar_usuario")
def actualizar_usuario():
    usuario = Usuario(
        cedula=request.args["cedula"],
        nombre=request.args["nombre"],
        apellido=request.args["apellido"],
        telefono=request.args["telefono"],
        correo=request.args["correo"],
        direccion=request.args["direccion"]
    )
    UsuariosController.modificar(usuario)
    return "Usuario modificado exitosamente."
    
#MODULO ABONOS
# Muestra el formulario de abonos
@blueprint.route("/abonos")
def abonos():
    return render_template("abonos.html")

# Inserta un abono en la base de datos
@blueprint.route("/insertar_abono")
def insertar_abono():
    abono = Abono(
        id_abono=None,
        id_plan=int(request.args["id_plan"]),
        mes_abono=int(request.args["mes_abono"]),
        valor_abono=float(request.args["valor_abono"].replace(".", "")),
        nueva_cuota=float(request.args["nueva_cuota"].replace(".", ""))
    )
    AbonosController.insertar(abono)
    return f"Se guardó exitosamente el abono para el plan ID: {request.args['id_plan']}.<br /><a href='/'>Volver al inicio</a>"

# Busca un abono por ID
@blueprint.route("/buscar_abono")
def buscar_abono():
    try:
        id_abono = int(request.args["id_abono"])
        abono = AbonosController.buscar(id_abono)
        return render_template("abono_buscado.html", abono=abono)
    except Exception as e:
        return "No se encontró ningún abono con ese ID. <br /><a href='/'>Volver al inicio</a>"

# Muestra el formulario de modificar con los datos actuales
@blueprint.route("/modificar_abono")
def modificar_abono():
    try:
        id_abono = int(request.args["id_abono"])
        abono = AbonosController.buscar(id_abono)
        return render_template("abono_modificar.html", abono=abono)
    except Exception as e:
        return "No se encontró ningún abono con ese ID. <br /><a href='/'>Volver al inicio</a>""

# Guarda los cambios del abono modificado
@blueprint.route("/actualizar_abono")
def actualizar_abono():
    abono = Abono(
        id_abono=int(request.args["id_abono"]),
        id_plan=int(request.args["id_plan"]),
        mes_abono=int(request.args["mes_abono"]),
        valor_abono=float(request.args["valor_abono"].replace(".", "")),
        nueva_cuota=float(request.args["nueva_cuota"].replace(".", ""))
    )
    AbonosController.modificar(abono)
    return "Abono modificado exitosamente. <br /><a href='/'>Volver al inicio</a>"

# Elimina un abono de la base de datos
@blueprint.route("/eliminar_abono")
def eliminar_abono():
    id_abono = int(request.args["id_abono"])
    AbonosController.eliminar(id_abono)
    return "Abono eliminado exitosamente. <br /><a href='/'>Volver al inicio</a>"

if __name__ == '__main__':
    blueprint.run(debug=True)