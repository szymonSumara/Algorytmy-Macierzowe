import time
import numpy as np


EPSILON = 10**(-4)

class TmpRow:
    def __init__(self, VAL, JCN):
        self.VAL = VAL
        self.JCN = JCN

    def mull_by_scalar(self, scalar):
        new_value = self.VAL[:]
        for i in range(len(new_value)):
            new_value[i] *= scalar
        return  TmpRow(new_value, self.JCN[:])

    def div_by_scalar(self, scalar):
        for i in range(len(self.VAL)):
            self.VAL[i] /= scalar

    def append(self, column_number, value):
        if EPSILON < abs(value):
            self.VAL.append(value)
            self.JCN.append(column_number)

    def sub(self, other):

        new_VAL = []
        new_JCN = []

        this_iterator = 0
        other_iterator = 0

        while this_iterator < len(self.VAL) or other_iterator < len(other.VAL):
            if this_iterator == len(self.VAL):

                new_VAL.append(other.VAL[other_iterator])
                new_JCN.append(other.JCN[other_iterator])
                other_iterator += 1

            elif other_iterator == len(other.VAL):

                new_VAL.append(self.VAL[this_iterator])
                new_JCN.append(self.JCN[this_iterator])
                this_iterator += 1

            elif self.JCN[this_iterator] == other.JCN[other_iterator]:

                if EPSILON < abs(self.VAL[this_iterator] - other.VAL[other_iterator]):
                    new_VAL.append(self.VAL[this_iterator] - other.VAL[other_iterator])
                    new_JCN.append(other.JCN[other_iterator])
                this_iterator += 1
                other_iterator += 1

            elif self.JCN[this_iterator] < other.JCN[other_iterator]:
                new_VAL.append(self.VAL[this_iterator])
                new_JCN.append(self.JCN[this_iterator])
                this_iterator += 1
            else:
                new_VAL.append(other.VAL[other_iterator])
                new_JCN.append(other.JCN[other_iterator])
                other_iterator += 1

        return TmpRow(new_VAL, new_JCN)






class CoordinateMatrix:
    #ordered by row
    def __init__(self, IRN, JCN, VAL, shape):
        self.IRN = IRN[:]
        self.JCN = JCN[:]
        self.VAL = VAL[:]
        self.shape = shape

    def update_row(self, row, tmpRow):

        tmp_IRN = [row for _ in tmpRow.VAL]

        start_index = 0

        while start_index < len(self.VAL) and self.IRN[start_index] < row:
            start_index += 1

        end_index = start_index
        if self.IRN[start_index] == row:
            while end_index < len(self.VAL) and self.IRN[end_index] == row:
                end_index += 1

        self.JCN = self.JCN[:start_index] + tmpRow.JCN + self.JCN[end_index:]
        self.IRN = self.IRN[:start_index] + tmp_IRN + self.IRN[end_index:]
        self.VAL = self.VAL[:start_index] + tmpRow.VAL + self.VAL[end_index:]


    def to_dense_matrix(self):
        mat = np.zeros(self.shape)
        for index in range(len(self.VAL)):
            mat[self.IRN[index]][self.JCN[index]] = self.VAL[index]
        return mat

    def __str__(self):


        return "JSN: {0} \n IRN: {1} \n VAL: {2} \n".format(self.JCN, self.IRN, self.VAL)

def execution_func_wrapper(func, label):

    start = time.time()
    f_result = func()
    end = time.time()
    print("Elapsed Time (" + label + " ):", end - start)
    return {
        "time": end - start,
        "result": f_result,
    }


def matrix_to_coordinate_format(matrix):

    IRN = []
    JCN = []
    VAL = []

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[row_index])):

            if EPSILON < abs(matrix[row_index][column_index]) :
                IRN.append(row_index)
                JCN.append(column_index)
                VAL.append(matrix[row_index][column_index])

    return CoordinateMatrix(IRN, JCN, VAL, matrix.shape)


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
            