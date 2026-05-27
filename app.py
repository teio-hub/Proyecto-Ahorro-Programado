import sys
sys.path.append("src")

from flask import Flask, render_template, request
from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro
from controller.usuarios_controller import UsuariosController
from model.Usuario import Usuario

server = Flask(__name__)

#MODULO PLANES
@server.route("/")
def inicio():
    return render_template("planes.html")

@server.route("/planes")
def planes():
    return render_template("planes.html")

# Crea las tablas en la base de datos
@server.route("/crear_tablas")
def crear_tablas():
    try:
        PlanesController.crear_tabla()
        UsuariosController.crear_tabla()
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
    return f"Se guardó exitosamente el plan para la cédula: {request.args['cedula']} con el ID: {id_plan}.<br /><a href='/'>Volver al inicio</a>"

# Busca un plan por ID y muestra sus datos
@server.route("/buscar_plan")
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
@server.route("/modificar_plan")
def modificar_plan():
    try:
        id_plan = int(request.args["id_plan"])
        plan = PlanesController.buscar(id_plan)
        return render_template("plan_modificar.html", plan=plan)
    except Exception as e:
        return "No se encontró ningún plan con ese ID."

# Guarda los cambios del plan modificado
@server.route("/actualizar_plan")
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
@server.route("/eliminar_plan")
def eliminar_plan():
    id_plan = int(request.args["id_plan"])
    PlanesController.eliminar(id_plan)
    return "Plan eliminado exitosamente. <a href='/'>Volver al inicio</a>"

#MODULO USUARIOS

# Muestra el formulario de usuarios
@server.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

# Inserta un usuario en la base de datos
@server.route("/insertar_usuario")
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
@server.route("/buscar_usuario")
def buscar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuariosController.buscar(cedula)
        return render_template("usuario_buscado.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula."

# Muestra el formulario de modificar con los datos actuales
@server.route("/modificar_usuario")
def modificar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuariosController.buscar(cedula)
        return render_template("usuario_modificar.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula."

# Guarda los cambios del usuario modificado
@server.route("/actualizar_usuario")
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
    
if __name__ == '__main__':
    server.run(debug=True)