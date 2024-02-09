import unittest
from datetime import date

from main import CompaniaAerea, Cliente, Paquete

class TestCompaniaAerea(unittest.TestCase):
    def setUp(self):
        self.cliente1 = Cliente("Cliente1")
        self.cliente2 = Cliente("Cliente2")

        self.compania = CompaniaAerea()

        self.paquete1 = Paquete(self.cliente1)
        self.paquete2 = Paquete(self.cliente2)

    def test_transportar_paquete(self):
        self.compania.transportar_paquete(self.paquete1)
        self.assertEqual(len(self.compania.paquetes_transportados), 1)
        self.assertEqual(self.compania.total_recaudado, 10)

    def test_generar_reporte_diario(self):
        # Transportar paquetes para tener datos en el informe
        self.compania.transportar_paquete(self.paquete1)
        self.compania.transportar_paquete(self.paquete2)

        # Utilizar una fecha específica para el informe
        fecha_informe = date(2024, 2, 9)  # Puedes ajustar la fecha según sea necesario

        reporte_diario = self.compania.generar_reporte_diario(fecha_informe)
        expected_report = f"Reporte del {fecha_informe}:\nTotal de paquetes transportados: 2\nTotal recaudado: $20"

        self.assertEqual(reporte_diario, expected_report)

if __name__ == "__main__":
    unittest.main()

