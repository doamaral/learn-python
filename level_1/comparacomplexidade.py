__author__ = 'Usuário'

import math

for i in range(45):
    a = 8 * math.pow(i, 2)
    b = 64 * i * math.log2(i)
    print("f({0:d}) = {1:d} --- {2:f}".format(i, a, b))
