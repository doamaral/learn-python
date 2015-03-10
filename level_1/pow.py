__author__ = 'Usuário'

import math
a = b = 0
i = 1
while a >= b:
    a = 100 * math.pow(i, 2)
    b = math.pow(2, i)
    print("f(%d) = %d --- %d" % (i, a, b))
    i = i + 1
