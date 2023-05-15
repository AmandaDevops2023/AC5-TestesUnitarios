#Amanda Pagani Lima - 2200564
from calculadora import Calculadora
from unittest import TestCase, main

class Testes (TestCase):
    def test_soma(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.somar(10,5), 15)

    def test_subtracao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.subtrair(1, 2), -1)

    def test_multiplicacao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.multiplicar(6, 6), 36)
    
    def test_divisao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.dividir(10, 5), 2)
    
    def test_divisao_por_zero(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.dividir(10, 0), "Erro! Divisão por zero")
        

if __name__ == "__main__":
    main()