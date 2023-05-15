class Calculadora:
    def somar(self, v1, v2):
        return v1 + v2

    def subtrair(self, v1, v2):
        return v1 - v2

    def multiplicar(self, v1, v2):
        return v1 * v2

    def dividir(self, v1, v2):
        try:
            return v1 / v2
        except:
            return "Erro! Divisão por zero"
