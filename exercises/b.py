import numpy as np
import matplotlib.pyplot as plt
from utils import *

m = 100
ns = [100, 200, 500, 1000]
prods = []
for n in ns:
    A = gaussian_matrix(m, n)
    for i in range(n):
        for j in range(n):
            if i != j:
                prod = np.inner(A[:, i], A[:, j])
                prods.append(prod)

compare = []
for _ in range(1000):
    x = np.random.random(0, m)[0]
    compare.append(x)
    
    
plot_dist(prods, "Distribuição do produto interno das colunas de matrizes gaussianas")
plot_dist(compare)