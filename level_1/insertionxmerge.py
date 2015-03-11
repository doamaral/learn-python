__author__ = 'Lucas'

import math

i = 0
#insertion > merge
while i < 45:
    i += 1
    insertion = 8 * math.pow(i, 2)
    merge = 64 * i * math.log(i, 2)
    if insertion < merge:
        print("Para n = %d : INSERTION é melhor que MERGE" % i)
    else:
        print("Para n = %d : MERGE é melhor que INSERTION" % i)
