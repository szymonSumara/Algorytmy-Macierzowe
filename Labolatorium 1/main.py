import numpy as np
from esentials import *
from matrixMull import *

# -------------- 1 ------------------

base_matrix = read_matrix_from_file(np.zeros((81, 81)), 'FEM.txt')
A = extend_matrix(base_matrix, 7)

# -------------- 2 ------------------

save_matrix_to_file(A, 'A.txt')
C = execution_func_wrapper(lambda: matrix_mull_jip(A, A), "")['result']
save_matrix_to_file(C, 'C.txt')

# -------------- 3 ------------------

loopsTimes = CSVGenerator()
loopsTimes.set_header(['q', 'jip', 'ipj', 'jip', 'jpi', 'pij', 'pji'])

for q in range(2, 8):
    mat = extend_matrix(base_matrix, q)
    row = [q,
           execution_func_wrapper(lambda: matrix_mull_ijp(mat, mat), "ijp")['time'],
           execution_func_wrapper(lambda: matrix_mull_ipj(mat, mat), "ipj")['time'],
           execution_func_wrapper(lambda: matrix_mull_jip(mat, mat), "jip")['time'],
           execution_func_wrapper(lambda: matrix_mull_jpi(mat, mat), "jpi")['time'],
           execution_func_wrapper(lambda: matrix_mull_pij(mat, mat), "pij")['time'],
           execution_func_wrapper(lambda: matrix_mull_pji(mat, mat), "pji")['time'],
           ]
    loopsTimes.add_row(row)

loopsTimes.save_to_file('times.csv')

# ------------- 4 -----------------

blockTimes = CSVGenerator()
blockTimes.set_header(['q', 'jip', 'ipj', 'jip', 'jpi', 'pij', 'pji'])

mat = extend_matrix(base_matrix, 7)
for q in range(5, 151, 15):
    row = [q, execution_func_wrapper(lambda: matrix_mull_block(mat, mat, q), "block")['time'], ]
    print(q)
    blockTimes.add_row(row)

blockTimes.save_to_file('blocks.csv')
