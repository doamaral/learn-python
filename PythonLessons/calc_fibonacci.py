__author__ = 'M2M'

class Calculator:

    def __init__(self, name="Calculadora Maluca"):
        self.calc_name = name
    def serie_fibonacci(self, tamanho):
        "Dado o número de elementos, retorna a série de Fibonacci"
        fibo = [0, 1]
        count = 2
        if tamanho > 2:
            while count < tamanho:
                termo = fibo[count - 2] + fibo[count - 1]
                fibo.append(int(termo))
                count += 1
        return fibo