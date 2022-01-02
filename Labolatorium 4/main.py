import numpy as np
from esentials import *
from gaussElimination import *


if __name__ == '__main__':

    mat = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 2.0, 3.0],
        [4.0, 0.0, 5.0]
    ])
    mat = read_matrix_from_file('3a.csv')
    data = execution_func_wrapper(
                               lambda : matrix_to_coordinate_format(mat),
                                "Non convert matrix mull with non convert matrix"
                            )

    converted = data['result']
    #print(mat)

    data1 = execution_func_wrapper(
                               lambda : row_sparse_coordinate_gauss_elimination(converted),
                                "Converted"
                            )
    print(data1['result'].to_dense_matrix())
    data2 = execution_func_wrapper(
                               lambda : row_gauss_elimination(mat),
                                "Not Converted"
                            )

    print(data1 == data2)

   # # matrix = read_matrix_from_file('3a.csv')
   #  output = row_sparse_coordinate_gauss_elimination(mat)
   #  print(data['result'].to_dense_matrix())
   #  #output = row_gauss_elimination(mat)
   #  #print(output)
   #  #save_matrix_to_file(output, "result.csv")
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
