import numpy as np
from esentials import *

def row_gauss_elimination(mat):

    n = mat.shape[1]

    for k in range(n-1):
        mat[k, k:n] /= mat[k, k]
        print(k)
        for j in range(k+1, n):
            print(k, j)
            mat[j, k:n] -= mat[k, k:n]*(mat[j, k])
    return mat



def row_sparse_coordinate_gauss_elimination(matrix):

    n = matrix.shape[0]
    k_row_start = 0
    for k in range(n):
        #print(k)

        while k_row_start < len(matrix.VAL) and matrix.IRN[k_row_start] < k:
            k_row_start += 1

        k_row = TmpRow([], [])
        row_pointer = k_row_start

        Akk = 0

        while row_pointer < len(matrix.VAL) and matrix.IRN[row_pointer] == k:
            k_row.append(matrix.JCN[row_pointer], matrix.VAL[row_pointer])
            if matrix.JCN[row_pointer] == k:
                Akk = matrix.VAL[row_pointer]
            row_pointer += 1
        # if Akk == None:
        #     raise TypeError("Invalid Matrix format")

        k_row.div_by_scalar(Akk)
        matrix.update_row(k, k_row)
        last_row_end = k_row_start + len(k_row.VAL)
        for j in range(k + 1, n):
            print(k, j)
            row_pointer = last_row_end
            j_row = TmpRow([], [])

            while matrix.IRN[row_pointer] < j:
                row_pointer += 1

            if matrix.IRN[row_pointer] != j:
                continue

            Ajk = 0

            while row_pointer < len(matrix.VAL) and matrix.IRN[row_pointer] < j:
                if matrix.JCN[row_pointer] < k:
                    row_pointer += 1
                    continue
                j_row.append(matrix.JCN[row_pointer], matrix.VAL[row_pointer])
                if matrix.JCN[row_pointer] == k:
                    Ajk = matrix.VAL[row_pointer]
                row_pointer += 1
           # print("k_row: " ,len(k_row.VAL) , k_row.VAL)
            if Ajk != 0:
                matrix.update_row(j, j_row.sub( k_row.mull_by_scalar(Ajk)))
                last_row_end += len(j_row.VAL)

    return matrix



