import numpy as np


def column_gauss_elimination(mat, iterations=-1):
    if iterations < 0:
        iterations = mat.shape[1]

    n = iterations
    for k in range(n):
        mat[k:n,k] /= mat[k, k]
        for j in range(k+1, n):
            mat[k:n, j] -= mat[k:n, k]*mat[k, j]

    return mat
