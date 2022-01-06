"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки - ручка.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки - карандаш.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки - маркер.')

stationery = Stationery('Канцелярские товары')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')


list_of_stationery = [stationery, pen, pencil, handle]
for item in list_of_stationery:
    print(item.title)
    item.draw()
    print('-' * 50)
