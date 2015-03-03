__author__ = 'Lucas'

import sort_methods

vetor = [10, 1, 3, 2, 15, 0, 13]
a = sort_methods.selection(vetor)
print("Selection: ", end="")
print(a)

vetor = [10, 1, 3, 2, 15, 0, 13]
a = sort_methods.insertion(vetor)
print("Insertion: ", end="")
print(a)

vetor = [10, 1, 3, 2, 15, 0, 13]
a = sort_methods.bubble(vetor)
print("Bubble:", end="")
print(a)