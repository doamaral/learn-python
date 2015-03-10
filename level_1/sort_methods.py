__author__ = 'Lucas'

def selection(v):
    for j in range(len(v)-1):
        menor = j
        for i in range(j, len(v)):
            if v[i] < v[menor]:
                menor = i
        v[j], v[menor] = v[menor], v[j]
    return v

def inverted_selection(v):
    for j in range(len(v)-1):
        menor = j
        for i in range(j, len(v)):
            if v[i] > v[menor]:
                menor = i
        v[j], v[menor] = v[menor], v[j]
    return v

def insertion(v):
    for i in range(1, len(v)):
        j = i - 1
        chave = v[i]
        while v[j] > chave and j >= 0:
            v[j], v[j+1] = v[j+1], v[j]
            j = j - 1
    return v

def inverted_insertion(v):
    for i in range(1, len(v)):
        j = i - 1
        chave = v[i]
        while v[j] < chave and j >= 0:
            v[j], v[j+1] = v[j+1], v[j]
            j = j - 1
    return v

def bubble(v):
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if(v[i] > v[j]):
                v[i], v[j] = v[j], v[i]
    return v

