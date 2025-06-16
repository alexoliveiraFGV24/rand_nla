import numpy as np
import matplotlib.pyplot as plt
from utils import *

n = 500
norms = []
for m in range(2, 1000):
    A = gaussian_matrix(m,n)
    for j in range(n):
        norm = norm2(A[:, j])
        norms.append(norm)

plot_dist(norms, "Distribuição das normas 2 das colunas de matrizes gaussianas")