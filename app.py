import sys
sys.path.append("src")

from flask import Flask 
from view_web import vista_ahorro
from flask import render_template, request
from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro
from controller.usuarios_controller import UsuariosController
from model.Usuario import Usuario
from controller.abonos_controller import AbonosController
from model.Abono import Abono



server = Flask(__name__)
server.register_blueprint(vista_ahorro.blueprint)

if __name__ == '__main__':
    server.run(debug=True) 