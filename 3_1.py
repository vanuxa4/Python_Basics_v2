"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div(a, b):
    try:
        print(a / b)
    except:
        print('На ноль делить нельзя')


div(3, 4)
