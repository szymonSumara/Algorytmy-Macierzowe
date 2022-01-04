import numpy as np
from esentials import *
from gaussElimination import *


if __name__ == '__main__':

    m400 = read_matrix_from_file('3a.csv')
    m1600 = read_matrix_from_file('4a.csv')

    csv = CSVGenerator()
    csv.set_header(["matrix", "method",  "size", "time", "memory_consumption"])

    for mat, mat_name in [(m400, "m400"), (m1600, "m1600")]:
        for size in [50, 100, 200, 400, 600, 800, 1200, 1600]:
            if size > len(mat):
                break
            for t in range(1):

                sliced_mat = [[mat[row_index][column_index] for column_index in range(size)] for row_index in range( size)]

                data = execution_func_wrapper(
                       lambda : matrix_to_coordinate_format(sliced_mat),
                        "Matrix({0}) conversion time".format(size)
                    )

                converted = data['result']

                data1 = execution_func_wrapper(
                    lambda: row_sparse_coordinate_gauss_elimination(converted),
                    "Converted {0} {1}".format(size, mat_name)
                )


                data2 = execution_func_wrapper(
                    lambda: row_gauss_elimination(sliced_mat),
                    "Non convert {0} {1}".format(size, mat_name)
                )

                csv.add_row([mat_name, "sparse", size, data1['time'], data1['memory']])
                csv.add_row([mat_name, "dense", size, data2['time'], data2['memory']])
        csv.save_to_file("tests.csv")



    #         converted = data['result']
    # #print(mat)
    #
    #
    #
    #
    #
    # converted = data['result']
    #
    # print(calulate_memory_usage(converted,row_sparse_coordinate_gauss_elimination))
    #
    # save_matrix_to_file(data1['result'].to_dense_matrix(), "result1.csv")
    #
    # print(data1['result'].to_dense_matrix())
    # data2 = execution_func_wrapper(
    #                            lambda : row_gauss_elimination(mat),
    #                             "Not Converted"
   #                          )
   #  print(calulate_memory_usage(mat, row_gauss_elimination))
   #  # for r in range(data2['result'].shape[0]):
   #  #     for c in range(data2['result'].shape[0]):
   #  #         if EPSILON >= abs(data2['result'][r][c]):
   #  #             data2['result'][r][c] = 0
   #
   #  save_matrix_to_file(data2['result'], "result2.csv")
   #  #print(data1 == data2)
   #
   # # # matrix = read_matrix_from_file('3a.csv')
   #  output = row_sparse_coordinate_gauss_elimination(mat)
   #  print(data['result'].to_dense_matrix())
   #  #output = row_gauss_elimination(mat)
   #  #print(output)
   #  #print(output == matrix)



    # csv = CSVGenerator()
    # csv.set_header(["TYPE","Matrix", "TIME"])
    # FEM = read_matrix_from_file('fem4.csv')
    # FEM = extend_matrix(FEM, 7)
    # save_matrix_to_file(FEM, "FEM.csv")
    # FEM_CSC = matrix_to_CSC(FEM)
    #
    # print(len(FEM)*len(FEM[0]))
    # print(len(FEM_CSC[1]))
    #
    #
    # #---------------------------TESTS-------------------------
    # data = None
    #
    # for i in range(5):
    #     data = execution_func_wrapper(
    #                        lambda : matrix_mull_ijp(FEM, FEM),
    #                         "Non convert matrix mull with non convert matrix"
    #                     )
    #     csv.add_row(['default', data['time']])
    #
    # save_matrix_to_file(data['result'], "FEMmullFEM.csv")
    #
    # for i in range(5):
    #     data = execution_func_wrapper(
    #                         lambda: matrix_mull_CSC(FEM_CSC, FEM),
    #                         "convert matrix  to SCS mull with non convert matrix"
    #                     )
    #     csv.add_row(['one converted', data['time']])
    #
    # save_matrix_to_file(data['result'], "FEM_CSCmullFEM.csv")
    #
    # csv.save_to_file("Tests.csv")
