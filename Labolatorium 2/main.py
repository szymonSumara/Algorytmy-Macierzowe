import numpy as np
from esentials import *
from gaussElimination import *

# -------------- 1 ------------------

for i in range(20,25):
    mat = read_matrix_from_file('Generator macierzy/fem' + str(i) + '.csv')
    execution_func_wrapper(lambda: column_gauss_elimination(mat,int(mat.shape[0]/2)), 'fem' + str(i) +"n/2")
    execution_func_wrapper(lambda: column_gauss_elimination(mat,int(mat.shape[0]/4)),'fem' + str(i) +"n/4")


matrix = np.mat([
    [1.0,2.0,3.0,4.0],
    [5.0,6.0,5.0,8.0],
    [9.0,10.0,21.0,12.0],
    [13.0,14.0,15.0,76.0]
])

print(matrix)
column_gauss_elimination(matrix)
