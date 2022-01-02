import numpy as np

def dot_product(first_vector, second_vector):

    first_vector_length, = first_vector.shape
    second_vector_length, = second_vector.shape

    if first_vector_length != second_vector_length:
        raise Exception('Vectors sizes not equal '
                        + '( first length: ' + first_vector_length
                        + ' second length ' + second_vector_length)

    scalar = 0
    for i in range(first_vector_length):
        scalar += first_vector[i] * second_vector[i]

    return scalar

def matrix_mull_ijp(first, second):
    print(first.shape, second.shape )
    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    transpose_second = second.T

    result = np.zeros((first_row_number, second_column_number))

    for i in range(first_row_number):
        for j in range(second_column_number):
            result[i][j] = dot_product(first[i], transpose_second[j])
    return result

def matrix_mull_CSC(A, B):
    IRN, VAL,  COLPTR = A
    n = len(COLPTR)-1
    C = np.zeros([n,n])
    for p in range(len(B)):
        for j in range(len(B[0])):
            for i in range(COLPTR[p],COLPTR[p+1]):
                C[IRN[i]][j]+=VAL[i]*B[p][j]
    return C


