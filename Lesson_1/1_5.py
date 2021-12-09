'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

revenue = int(input('Введите значние выручки в тыс. руб.: '))
costs = int(input('Введите значение издержек в тыс. руб.: '))
if revenue < costs:
    print(f'Увы, компания отработала с убытком: {revenue - costs} тыс. руб.')
elif revenue == costs:
    print(f'Компания отработала в ноль')
else:
    profit = revenue - costs
    print(f'Компания отработала с прибылью {profit} тыс. руб.')
    profitability = int(profit / revenue * 100)
    print(f'Рентабельность продаж составила {profitability}%')
    staff = int(input('Введите количество сотрудников компании: '))
    print(f'Прибыль фирмы на каждого сотрудника составила: {int(profit / staff * 1000)} руб.')
    # на тысячу умножаем, т.к. выручка и издержки в тыс. руб., а прибыль на человека отражаем в руб.
