import numpy as np
from esentials import *
from matrixMull import *

csv = CSVGenerator()
csv.set_header(["TYPE", "TIME"])
FEM = read_matrix_from_file('fem4.csv')
FEM = extend_matrix(FEM, 7)
save_matrix_to_file(FEM, "FEM.csv")
FEM_CSC = matrix_to_CSC(FEM)

print(len(FEM)*len(FEM[0]))
print(len(FEM_CSC[1]))


#---------------------------TESTS-------------------------
data = None

for i in range(5):
    data = execution_func_wrapper(
                       lambda : matrix_mull_ijp(FEM, FEM),
                        "Non convert matrix mull with non convert matrix"
                    )
    csv.add_row(['default', data['time']])

save_matrix_to_file(data['result'], "FEMmullFEM.csv")

for i in range(5):
    data = execution_func_wrapper(
                        lambda: matrix_mull_CSC(FEM_CSC, FEM),
                        "convert matrix  to SCS mull with non convert matrix"
                    )
    csv.add_row(['one converted', data['time']])

save_matrix_to_file(data['result'], "FEM_CSCmullFEM.csv")

csv.save_to_file("Tests.csv")
