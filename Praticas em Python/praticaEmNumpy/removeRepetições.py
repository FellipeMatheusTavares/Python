import numpy as np

# unique é a função usada para remover numeros repetidos
j = np.array([11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 18, 19, 20])
j = np.unique(j)
print(j)