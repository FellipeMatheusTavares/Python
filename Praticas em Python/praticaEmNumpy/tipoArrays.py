# arrays vazios tipificados
# empty significa que não são iniciados
import numpy as np

vazio = np.empty([3, 2], dtype=int)
print(vazio)
print("-----------")

# cria uma matriz 4x3 com valores zero
zeros = np.zeros([4, 3])
print(zeros)
print("-----------")

# com valores iguais a um
um = np.ones([5, 7])
print(um)
print("-----------")

# matriz quadrada com diagonal principal com valores 1 e os outros zero
diagonal = np.eye(5)
print(diagonal)
