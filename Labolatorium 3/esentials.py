import time
import numpy as np




def execution_func_wrapper(func, label):

    start = time.time()
    f_result = func()
    end = time.time()
    print("Elapsed Time (" + label + " ):", end - start)
    return {
        "time": end - start,
        "result": f_result,
    }


def matrix_to_CSC(matrix):

    IRN = []
    VAL = []
    COLPTR = [0]

    for column in matrix.T:
        for item_index in range(len(column)):
            if column[item_index] != 0:
                VAL.append(column[item_index])
                IRN.append(item_index)
        COLPTR.append(len(IRN))

    return IRN, VAL, COLPTR


def save_matrix_to_file(matrix, filename):

    data = ""

    for row in matrix:
        for value in row:
            data += str(value) + ','
        data += '\n'

    with open(filename, 'w') as f:
        f.write(data)


def read_matrix_from_file( filename):

    with open(filename, 'r') as f:
        data = f.read()
        row_number = 0
        col_number = 0

        for row in data.split('\n'):
            row_number+=1
            for cell in row.split(','):
                col_number +=1

        matrix = np.zeros((row_number - 1, int(col_number/row_number) + 1))


        it_row, it_col = 0, 0
        for row in data.split('\n'):
            for cell in row.split(','):
                if cell:
                    matrix[it_row][it_col] = float(cell)
                    it_col += 1
            it_row += 1
            it_col = 0
    return matrix



def extend_matrix(matrix, q):

    columns, rows = matrix.shape

    new_matrix = np.zeros((columns*q, rows * q))
    for c in range(columns):
        for r in range(rows):
            for i in range(q):
                for j in range(q):
                    new_matrix[i*columns + c][j*rows + r] = matrix[c][r]
    return new_matrix


class CSVGenerator:

    def __init__(self):
        self.header = []
        self.body = []

    def set_header(self, header):
        self.header = header[:]

    def add_row(self, new_row):
        self.body.append(new_row[:])

    def clear_body(self):
        self.body = []
        self.header = []

    def save_to_file(self, filename):

        with open(filename, 'w') as f:
            data = ""
            for label in self.header:
                data += label + ','
            data += '\n'

            for row in self.body:
                for item in row:
                    data += str(item) + ','
                data += '\n'

            f.write(data)
            