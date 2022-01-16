"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(item) for item in line) for line in self.matrix)

    def __add__(self, other):
        x = []
        for row in range(len(self.matrix)):
            x.append([])
            for column in range(len(self.matrix[0])):
                x[row].append((self.matrix[row][column]) + other.matrix[row][column])
        return '\n'.join(map(str, x))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[11, 12], [13, 14], [15, 16]])

print(matrix_1)
print('-'*50)
print(matrix_2)
print('-'*50)
print(matrix_1 + matrix_2)
