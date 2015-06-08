__author__ = 'Lucas Amaral'

def FizzBuzz(numero):
    if not numero % 3 and not numero % 5:
        return "fizzbuzz"
    if not numero % 3:
        return "fizz"
    if not numero % 5:
        return "buzz"
    return numero