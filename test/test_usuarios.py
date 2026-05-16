import unittest
import sys
sys.path.append("src")

from model.Usuario import Usuario
from controller.usuarios_controller import UsuariosController

class TestUsuarios(unittest.TestCase):

    @staticmethod
    def setUpClass():
        UsuariosController.borrar_tabla()
        UsuariosController.crear_tabla()

    def test_1_insertar_1(self):
        usuario = Usuario(cedula="123456", nombre="Maria", apellido="Ospina",
                          telefono="3001234567", correo="maria@correo.com", direccion="Calle 1")
        UsuariosController.insertar(usuario)
        buscado = UsuariosController.buscar("123456")
        self.assertTrue(usuario.is_equal(buscado))

    def test_2_insertar_2(self):
        usuario = Usuario(cedula="654321", nombre="Alejandro", apellido="Tello",
                          telefono="3107654321", correo="ale@correo.com", direccion="Carrera 2")
        UsuariosController.insertar(usuario)
        buscado = UsuariosController.buscar("654321")
        self.assertTrue(usuario.is_equal(buscado))

    def test_3_insertar_3(self):
        usuario = Usuario(cedula="111111", nombre="Karen", apellido="Londoño",
                          telefono="3209876543", correo="karen@correo.com", direccion="Avenida 3")
        UsuariosController.insertar(usuario)
        buscado = UsuariosController.buscar("111111")
        self.assertTrue(usuario.is_equal(buscado))

    def test_4_modificar_1(self):
        usuario = Usuario(cedula="654321", nombre="Alejandro José", apellido="Tello",
                         telefono="3107654321", correo="ale@correo.com", direccion="Carrera 2")
        UsuariosController.modificar(usuario)
        buscado = UsuariosController.buscar("654321")
        self.assertTrue(usuario.is_equal(buscado))

    def test_5_modificar_2(self):
        usuario = Usuario(cedula="123456", nombre="Maria Paula", apellido="Ospina",
                         telefono="3001111111", correo="mariapaula@correo.com", direccion="Calle 1 #2-3")
        UsuariosController.modificar(usuario)
        buscado = UsuariosController.buscar("123456")
        self.assertTrue(usuario.is_equal(buscado))

    def test_6_modificar_3(self):
        usuario = Usuario(cedula="111111", nombre="Karen Sofía", apellido="Londoño",
                         telefono="3209999999", correo="karensofía@correo.com", direccion="Avenida 3 #10-20")
        UsuariosController.modificar(usuario)
        buscado = UsuariosController.buscar("111111")
        self.assertTrue(usuario.is_equal(buscado))

    def test_7_buscar_1(self):
        buscado = UsuariosController.buscar("123456")
        self.assertEqual(buscado.cedula, "123456")

    def test_8_buscar_2(self):
        buscado = UsuariosController.buscar("654321")
        self.assertEqual(buscado.cedula, "654321")

    def test_9_buscar_3(self):
        buscado = UsuariosController.buscar("111111")
        self.assertEqual(buscado.cedula, "111111")

    def test_10_eliminar_1(self):
        UsuariosController.eliminar("111111")
        self.assertRaises(Exception, UsuariosController.buscar, "111111")

    def test_11_error_cedula_duplicada(self):
        usuario = Usuario(cedula="123456", nombre="Otro", apellido="Usuario",
                          telefono="300", correo="otro@correo.com", direccion="Otra")
        self.assertRaises(Exception, UsuariosController.insertar, usuario)

if __name__ == '__main__':
    unittest.main()