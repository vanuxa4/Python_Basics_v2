"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0:
            return f'{self.b}j'
        if self.b == 0:
            return f'{self.a}'
        if self.b > 0:
            return f'{self.a}+{self.b}j'
        if self.b < 0:
            return f'{self.a}{self.b}j'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


cn = Complex(1, -2)
cn1 = Complex(5, 3)
print(cn1)
print(cn)
print(cn + cn1)
print(complex(1, -2) + complex(5, 3))
