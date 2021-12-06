import numpy as np


def column_gauss_elimination(mat, iterations=-1):
    if iterations < 0:
        iterations = mat.shape[1]

    print(mat.shape)
    n = mat.shape[1]

    for k in range(iterations):
        mat[k:n, k] /= mat[k, k]
        for j in range(k+1, n):
            mat[k:n, j] -= mat[k:n, k]*mat[k, j]

    return mat


def schur_complement(mat, m):
    return column_gauss_elimination(mat, mat.shape[1] - m)
