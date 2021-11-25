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


def mult_and_add(c, a, b):
    size, = c.shape
    for i in range(size):
        c[i] += a*b[i]


def matrix_mull_ijp(first, second):

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


def matrix_mull_ipj(first, second):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    result = np.zeros((first_row_number, second_column_number))

    for i in range(first_row_number):
        for p in range(first_column_number):
            mult_and_add(result[i], first[i][p], second[p])
    return result


def matrix_mull_jip(first, second):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    transpose_second = second.T

    result = np.zeros((first_row_number, second_column_number))

    for j in range(first_row_number):
        for i in range(second_column_number):
            result[i][j] = dot_product(first[i], transpose_second[j])
    return result


def matrix_mull_jpi(first, second):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    result = np.zeros((first_row_number, second_column_number))

    for j in range(first_row_number):
        for p in range(first_column_number):
            mult_and_add(result[:, j], second[p][j], first[:, p])
    return result


def matrix_mull_pij(first, second):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    result = np.zeros((first_row_number, second_column_number))

    for p in range(first_column_number):
        for i in range(first_row_number):
            mult_and_add(result[i], first[i][p], second[p])
    return result


def matrix_mull_pji(first, second):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_row_number != second_column_number:
        raise Exception('Invalid matrix sizes')

    result = np.zeros((first_row_number, second_column_number))

    for p in range(second_row_number):
        for j in range(second_column_number):
            mult_and_add(result[:, j], second[p][j], first[:, p])
    return result


def matrix_mull_block(first, second, block_size):

    first_row_number, first_column_number = first.shape
    second_row_number, second_column_number = second.shape

    if first_column_number != second_row_number:
        raise Exception('Invalid matrix sizes')

    result = np.zeros((first_row_number, second_column_number))

    for j in range(0,second_column_number,block_size):
        for i in range(0,first_row_number, block_size):
            for p in range(0,first_column_number, block_size):
                for jb in range(j, min(j + block_size, second_column_number)):
                    for ib in range(i, min(i+block_size, first_row_number)):
                        for pb in range(p, min(p+block_size, first_column_number)):
                            result[ib][jb] += first[ib][pb] * second[pb][jb]
    return result




