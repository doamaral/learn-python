__author__ = 'Lucas'
import math

i = 1
a = math.pow(2, i)
b = 100 * math.pow(i, 2)

while b > a:
    i += 1
    a = math.pow(2, i)
    b = 100 * math.pow(i, 2)
    print("f(%d) : %d --- %d" % (i, a, b))
