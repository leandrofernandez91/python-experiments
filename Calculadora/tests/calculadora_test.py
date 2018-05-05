import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase, Calculadora):
    def test_restar_3menos2_devuelve1(self):
        calc = Calculadora()
        resultado = calc.restar(3, 2)
        self.assertEqual(1, resultado)

    def test_sumar_3mas2_devuelve5(self):
        calc = Calculadora()
        resultado = calc.sumar(3, 2)
        self.assertEqual(5, resultado)
    
    def test_edad_siNacio01101990_debeTener27anios(self):
        calc = Calculadora()
        resultado = calc.edad(1,10,1990)
        self.assertEqual(27, resultado)

    def test_edad_siNacio07111991_debeTener26anios(self):
        calc = Calculadora()
        resultado = calc.edad(7,11,1991)
        self.assertEqual(26, resultado)


    