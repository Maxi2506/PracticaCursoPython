import unittest
from emisiones import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    """Conjunto de pruebas automatizadas para validar la precisión y control de errores."""
    
    def test_calculo_nominal_default(self):
        # 100 kWh con factor por defecto 0.4 -> 40.0 kg CO2
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    def test_calculo_nominal_personalizado(self):
        # 200 kWh con factor 0.5 -> 100.0 kg CO2
        resultado = calcular_emisiones_carbono(200, factor_emision=0.5)
        self.assertEqual(resultado, 100.0)

    def test_consumo_negativo_lanza_excepcion(self):
        # Valida que consumos negativos eleven ValueError
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

if __name__ == "__main__":
    unittest.main()