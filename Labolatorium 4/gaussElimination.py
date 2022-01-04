import numpy as np
from esentials import *


def row_gauss_elimination(mat):
    operations_number = 0
    mat = mat.copy()
    n = len(mat)

    for k in range(n-1):
        for i in range(k,n):
            mat[k][i] /= mat[k][k]
            operations_number += 1
        for j in range(k+1, n):
            for i in range(k, n):
                mat[j][i] -= mat[k][i]*(mat[j][ k])
                operations_number += 2
    return mat




def row_sparse_coordinate_gauss_elimination(matrix):

    matrix = matrix.copy()
    n = matrix.shape[0]
    k_row_pointer = 0

    for k in range(n):
        while matrix.IRN[k_row_pointer] < k:
            k_row_pointer += 1

        k_row = TmpRow([], [])
        Akk = 0

        while k_row_pointer < len(matrix.VAL) and matrix.IRN[k_row_pointer] == k:
            k_row.append(matrix.JCN[k_row_pointer], matrix.VAL[k_row_pointer])
            if matrix.JCN[k_row_pointer] == k:
                Akk = matrix.VAL[k_row_pointer]

            k_row_pointer += 1

        if Akk == 0:
            print("Macierz jest osobliwa")
            exit(0)
            return matrix

        k_row.div_by_scalar(Akk)
        matrix.update_row(k, k_row)

        row_pointer = k_row_pointer

        for j in range(k + 1, n):
            start_index = row_pointer
            j_row = TmpRow([], [])

            while matrix.IRN[row_pointer] < j:
                row_pointer += 1

            if matrix.IRN[row_pointer] != j:
                continue

            Ajk = 0
            while row_pointer < len(matrix.VAL) and matrix.IRN[row_pointer] == j:
                if matrix.JCN[row_pointer] < k:
                    row_pointer += 1
                    continue
                j_row.append(matrix.JCN[row_pointer], matrix.VAL[row_pointer])
                if matrix.JCN[row_pointer] == k:
                    Ajk = matrix.VAL[row_pointer]

                row_pointer += 1

            if Ajk != 0:
                tmpRow = j_row.sub(k_row.mull_by_scalar(Ajk))
                matrix.update_row(j, tmpRow, start_index=start_index, end_index=row_pointer)
                row_pointer = start_index + len(tmpRow.VAL)
    return matrix

