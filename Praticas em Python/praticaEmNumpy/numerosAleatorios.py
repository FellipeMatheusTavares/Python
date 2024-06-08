# valores aleatorios entre zero e um
import numpy as np

ale = np.random.random((5))
print(ale)
print("------------------")

# "randn" é usado para numeros negativos
ale2 = np.random.randn((5))
print(ale2)
print("------------------")

# valores aleatorios 3 x 4
ale3 = (10*np.random.random((3,4)))
print(ale3)

# uso de semente
gnr = np.random.default_rng(1)
ale5 = gnr.random(3)
print(ale5)

# inteiros
ale6 = gnr.integers(10, size=(3, 4))
print(ale6)