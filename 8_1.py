"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
_______________________________________первое решение________________________________________________________________


class Data():
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_digit(cls, obj):
        is_date = cls.validation(obj)
        return f'День: {is_date[0]:02}, месяц: {is_date[1]:02}, год: {is_date[2]:02}'

    @staticmethod
    def validation(obj):
        day, month, year = map(int, obj.date.split('-'))
        return [day if day <= 31 else 'Некорректный день', month if month <= 12 else 'Некорректный месяц',
                year if year <= 2020 else 'Некорректный год']


data_1 = Data('01-02-2019')
print(data_1.date)
print(data_1.date_to_digit(data_1))

_______________________________________второе решение_________________________________________________________________

"""
Первое решение работает только с объектом, мне показалось это аротиворечит идеи классовых и статических методов 
(то что они от объекта то и не должны зависеть). Но хотелось бы, чтобы при создании объекта валидация все-таки
происходила, поэтому добавил второе решение. 
"""
class Data():
    def __init__(self, date):
        self.date = date
        print(self.date_to_digit(date))

    @classmethod
    def date_to_digit(cls, str_date):
        is_date = cls.validation(str_date)
        return f'День: {is_date[0]:02}, месяц: {is_date[1]:02}, год: {is_date[2]:02}'

    @staticmethod
    def validation(str_date):
        day, month, year = map(int, str_date.split('-'))
        return [day if day <= 31 else 'Некорректный день', month if month <= 12 else 'Некорректный месяц',
                year if year <= 2020 else 'Некорректный год']

print(Data.date_to_digit('01-02-2022'))
data_1 = Data('01-02-2013')