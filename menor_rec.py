__author__ = 'Usuário'

def menor(vetor, i, f):
    if i == f:
        return vetor[i]
    else:
        meio = int((i+f)/2)
        m1 = menor(vetor, i, meio)
        m2 = menor(vetor, meio+1, f)
        if m1 < m2:
            return m1
        return m2

v = [112, 100, 3, 1, 80, 105]

print(menor(v, 0, 5))