class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix    
    def __add__(self, other):
        new_matrix = []
        other_matrix = []
        if len(self.matrix) == len(other.matrix):
            for x in range (len(self.matrix)):            
                for i in range(len(self.matrix[x])):
                    z = self.matrix[x][i] + other.matrix[x][i]
                    other_matrix.append(z)
                new_matrix.append(other_matrix)
                other_matrix = []
            return new_matrix
        else:
            return 'Разный размер матриц'
    def __str__(self):
        matrix_view = ''
        for el in self.matrix:
            matrix_view += ' '.join(str(x) for x in el) + '\n'
        return matrix_view

matrix_1 = Matrix([[31, 22],[37, 43], [51, 86]])
matrix_2 = Matrix([[29, 56],[22, 76], [89, 43]])
print(matrix_1) #вывод матрицы в нормальном виде
print(matrix_2) #вывод матрицы в нормальном виде
print(Matrix(matrix_1 + matrix_2)) #вывод матрицы в нормальном виде