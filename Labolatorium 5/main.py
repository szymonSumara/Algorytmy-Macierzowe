import random

import numpy as np
from esentials import *
from gaussElimination import *
from permutation import *

if __name__ == '__main__':
    matrix = np.array(read_matrix_from_file('4a_zepsuted.csv'))[0:10,0:10]

    for row_index in range(len(matrix)):
        matrix[0][row_index] = 1
        matrix[row_index][0] = 1

        # matrix = [
    #     [1, 1, 1, 1, 1],
    #     [1, 2, 0, 0, 0],
    #     [1, 0, 3, 0, 0],
    #     [1, 0, 0, 4, 0],
    #     [1, 0, 0, 0, 5],
    # ]


    build_elimination_graph(matrix)
    elimination_graph = build_elimination_graph(matrix)
    print(elimination_graph)
    permutation_matrix = get_permutation_minimum_degree_algorithm(elimination_graph)
    permuted_converted_matrix = matrix_to_coordinate_format(matrix_multiplication(matrix_multiplication(permutation_matrix, matrix),matrix_transposition(permutation_matrix)))
    permuted_matrix = np.array(permutation_matrix) @ np.array(matrix) @ np.array(permutation_matrix).T
    permuted_elimination_graph = build_elimination_graph(permuted_matrix)

    print(permuted_elimination_graph)
    print( np.array(permutation_matrix))
    elimination_graph = build_elimination_graph(matrix)

    graf_gauss_elimination(elimination_graph)
    graf_gauss_elimination(permuted_elimination_graph)

    #print(matrix_multiplication(matrix_multiplication(permutation_matrix, matrix),matrix_transposition(permutation_matrix)))


    # save_matrix_to_file(permuted_converted_matrix, 'permuted_3a.csv')
    # execution_func_wrapper(lambda: row_sparse_coordinate_gauss_elimination(converted_matrix), "Converted")
    # execution_func_wrapper(lambda: row_sparse_coordinate_gauss_elimination(converted_matrix), "Converted Permuted")


