__author__ = 'Usuário'

print("Convertendo um real para inteiro: int(3.14) = ", int(3.14))

print("Convertendo um real para inteiro: float(5) = ", float(5))

print("Operações Real x Inteiro = Real: 5.0/2 + 3 = ", 5.0/2+3)

my_string = "palavra"

val = 10

print("a "+ my_string + " é string")

print("%d - A string '%s' tem tamanho %d" % (val, my_string, len(my_string)))

for char in my_string:
    print(char)

if my_string.startswith('p'):
    print(my_string.upper())

print(3*my_string)

