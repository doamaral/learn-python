__author__ = 'Lucas Amaral'

import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_numerosMultiplos3(self):
        self.assertEqual(FizzBuzz(3),"fizz")
        self.assertEqual(FizzBuzz(9),"fizz")

    def test_numerosMultiplos5(self):
        self.assertEqual(FizzBuzz(5),"buzz")
        self.assertEqual(FizzBuzz(10),"buzz")

    def test_outrosNumeros(self):
        self.assertEqual(FizzBuzz(1),1)
        self.assertEqual(FizzBuzz(2),2)
        self.assertEqual(FizzBuzz(4),4)

if __name__ == '__main__':
	unittest.main()


