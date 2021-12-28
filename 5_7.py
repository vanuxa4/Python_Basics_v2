"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

with open('text_7.txt', 'r', encoding='utf-8') as f_7:
    profit_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_7}
    print(profit_dict)
    profit_list = [val for val in profit_dict.values() if val > 0]
    av_profit = {'average profit': sum(profit_list) / len(profit_list)}
    final_list = [profit_dict, av_profit]
    print(final_list)

import json

with open('text_j.json', "w", encoding='utf-8') as f_j:
    json.dump(final_list, f_j, ensure_ascii=False, indent=4)