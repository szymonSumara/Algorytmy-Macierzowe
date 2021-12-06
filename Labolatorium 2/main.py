import numpy as np
from esentials import *
from gaussElimination import *
header = ["nxx", "time"]
tests = CSVGenerator()
tests.set_header(["type", "nxx", "div", "time"])
# -------------- 1 ------------------
for i in range(10, 20):
    for d in [2, 4, 8, 16]:
        for t in range(5):
            mat = read_matrix_from_file('Generator macierzy/fem' + str(i) + '.csv')
            tests.add_row([
                "fem",
                i,
                d,
                execution_func_wrapper(lambda: schur_complement(mat,int(mat.shape[0]/d)), 'fem' + str(i) +" n/" + str(d))['time']
            ])
# -------------- 2 ------------------
for i in range(15, 25):
    for d in [2, 4, 8, 16]:
        for t in range(5):
            mat = read_matrix_from_file('Generator macierzy/iga' + str(i) + '.csv')
            tests.add_row([
                "iga",
                i,
                d,
                execution_func_wrapper(lambda: schur_complement(mat,int(mat.shape[0]/d)), 'iga' + str(i) +" n/2")['time']
            ])

tests.save_to_file("tests.csv")