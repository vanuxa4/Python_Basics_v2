"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def output(name, surname, y_birth, city, email, tel):
    print(f'{name} {surname} {y_birth} {city} {email} {tel}')

output(name = 'Вова', city = 'Омск', surname = 'Васильев', y_birth= '20.05.1985', email = 'vov@mail.ru', tel= '967 567 88 90')

