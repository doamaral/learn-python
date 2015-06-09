from unittest import TestCase
from pessoa import Pessoa

__author__ = 'Lucas Amaral'


class TestPessoa(TestCase):
    def test_getNome(self):
        p = Pessoa("asdf", "12345")
        self.assertEqual("asdf", p.getNome())

    def test_setNome(self):
        p = Pessoa("asdf", "12345")
        p.setNome("Lucas Amaral")
        self.assertEqual("Lucas Amaral", p.getNome())

    def test_isAlive(self):
        p = Pessoa("asdf", "12345")
        self.assertTrue(p.isAlive(), "opa... Deu errado")
