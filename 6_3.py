'''
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {wage: wage,
                       bonus: bonus}  # вот это вообще не понятно из условия. Понял, увидев решение,
                                      # может условие дополнить?


class Position(Worker):

    def get_full_name(self):
        print(f'{self.position}: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход {self.position} составляет {sum(self.income.values())} USD')


worker_1 = Position('Ted', 'Bronx', 'CEO', 20000, 5000)
worker_2 = Position('Tom', 'Baffith', 'уборщик', 1000, 500)

worker_1.get_full_name()
worker_1.get_total_income()
print('_'*50)

worker_2.get_full_name()
worker_2.get_total_income()
print('_'*50)