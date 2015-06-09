__author__ = 'Lucas Amaral'

class Pessoa:
    _nome = "asdf"
    _nascimento = "12345"

    def __init__(self, new_name, data_nasc):
        self._nome = new_name
        self._nascimento = data_nasc

    def setNome(self, new_name):
        self._nome = new_name

    def getNome(self):
        return self._nome
