import unittest
import sys
sys.path.append("src")

from model.Abono import Abono
from controller.abonos_controller import AbonosController

class TestAbonos(unittest.TestCase):

    @staticmethod
    def setUpClass():
        AbonosController.borrar_tabla()
        AbonosController.crear_tabla()

    def test_1_insertar_1(self):
        abono = Abono(id_abono=None, id_plan=1, mes_abono=24,
                      valor_abono=2000000, nueva_cuota=296587.78)
        AbonosController.insertar(abono)
        buscados = AbonosController.buscar_por_plan(1)
        self.assertTrue(abono.is_equal(buscados[0]))

    def test_2_insertar_2(self):
        abono = Abono(id_abono=None, id_plan=2, mes_abono=12,
                      valor_abono=1000000, nueva_cuota=319805.90)
        AbonosController.insertar(abono)
        buscados = AbonosController.buscar_por_plan(2)
        self.assertTrue(abono.is_equal(buscados[0]))

    def test_3_insertar_3(self):
        abono = Abono(id_abono=None, id_plan=1, mes_abono=36,
                      valor_abono=5000000, nueva_cuota=359226.16)
        AbonosController.insertar(abono)
        buscados = AbonosController.buscar_por_plan(1)
        self.assertTrue(abono.is_equal(buscados[1]))

    def test_4_modificar_1(self):
        buscados = AbonosController.buscar_por_plan(1)
        id_real = buscados[0].id_abono
        abono = Abono(id_abono=id_real, id_plan=1, mes_abono=24,
                  valor_abono=3000000, nueva_cuota=222440.84)
        AbonosController.modificar(abono)
        buscados = AbonosController.buscar_por_plan(1)
        self.assertTrue(abono.is_equal(buscados[0]))

    def test_5_eliminar_1(self):
        AbonosController.eliminar(3)
        self.assertRaises(Exception, AbonosController.buscar, 3)

    def test_6_error_abono_inexistente(self):
        self.assertRaises(Exception, AbonosController.buscar, 9999)

if __name__ == '__main__':
    unittest.main()