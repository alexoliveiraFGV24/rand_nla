import numpy as np
import matplotlib.pyplot as plt

def norm2(x):
    return np.linalg.norm(x, ord=2)

def gaussian_matrix(m:int, n:int):
    return np.random.normal(0, 1, (m,n))

def plot_dist(data, title="", bins=100):
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.show()
    
def maxes(k=1000, m=100, n=300):
    maxes = []
    for _ in range(k):
        A = gaussian_matrix(m, n)
        values = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    A_i = A[:, i]
                    A_j = A[:, j]
                    value = np.inner(A_i, A_j) / (norm2(A_i) * norm2(A_j))
                    values.append(value)
        max = values[np.argmax(values)]
        maxes.append(max)
        
    return maxes