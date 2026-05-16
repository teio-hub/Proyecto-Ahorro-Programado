import unittest
import sys
sys.path.append("src")

from model.PlanAhorro import PlanAhorro
from controller.planes_controller import PlanesController

class TestPlanes(unittest.TestCase):

    @staticmethod
    def setUpClass():
        PlanesController.borrar_tabla()
        PlanesController.crear_tabla()

    def test_1_insertar_1(self):
        plan = PlanAhorro(id_plan=None, cedula="123456", meta=10000000,
                      tasa_interes=0.01, plazo=24, cuota_mensual=370734.72,
                      fecha_creacion="2026-05-11")
        PlanesController.insertar(plan)
        buscados = PlanesController.buscar_por_cedula("123456")
        self.assertTrue(plan.is_equal(buscados[0]))

    def test_2_insertar_2(self):
        plan = PlanAhorro(id_plan=None, cedula="654321", meta=5000000,
                      tasa_interes=0.0075, plazo=12, cuota_mensual=399757.38,
                      fecha_creacion="2026-05-11")
        PlanesController.insertar(plan)
        buscados = PlanesController.buscar_por_cedula("654321")
        self.assertTrue(plan.is_equal(buscados[0]))

    def test_3_insertar_3(self):
        plan = PlanAhorro(id_plan=None, cedula="111111", meta=20000000,
                      tasa_interes=0.0083, plazo=36, cuota_mensual=478968.21,
                      fecha_creacion="2026-05-11")
        PlanesController.insertar(plan)
        buscados = PlanesController.buscar_por_cedula("111111")
        self.assertTrue(plan.is_equal(buscados[0]))

    def test_4_modificar_1(self):
        plan = PlanAhorro(id_plan=1, cedula="123456", meta=10000000,
                          tasa_interes=0.01, plazo=36, cuota_mensual=232062.38,
                          fecha_creacion="2026-05-11")
        PlanesController.modificar(plan)
        buscado = PlanesController.buscar(1)
        self.assertTrue(plan.is_equal(buscado))

    def test_5_modificar_2(self):
        plan = PlanAhorro(id_plan=2, cedula="654321", meta=8000000,
                          tasa_interes=0.0075, plazo=24, cuota_mensual=320000.00,
                          fecha_creacion="2026-05-11")
        PlanesController.modificar(plan)
        buscado = PlanesController.buscar(2)
        self.assertTrue(plan.is_equal(buscado))

    def test_6_modificar_3(self):
        plan = PlanAhorro(id_plan=3, cedula="111111", meta=25000000,
                          tasa_interes=0.0083, plazo=48, cuota_mensual=520000.00,
                          fecha_creacion="2026-05-11")
        PlanesController.modificar(plan)
        buscado = PlanesController.buscar(3)
        self.assertTrue(plan.is_equal(buscado))

    def test_7_buscar_1(self):
        buscado = PlanesController.buscar(1)
        self.assertEqual(buscado.cedula, "123456")

    def test_8_buscar_2(self):
        buscado = PlanesController.buscar(2)
        self.assertEqual(buscado.cedula, "654321")

    def test_9_buscar_3(self):
        buscado = PlanesController.buscar(3)
        self.assertEqual(buscado.cedula, "111111")

    def test_10_eliminar_1(self):
        PlanesController.eliminar(3)
        self.assertRaises(Exception, PlanesController.buscar, 3)

    def test_11_error_plan_inexistente(self):
        self.assertRaises(Exception, PlanesController.buscar, 9999)

if __name__ == '__main__':
    unittest.main()