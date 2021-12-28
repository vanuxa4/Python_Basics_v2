"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# с модулем googletranslate не разобрался, может есть более подходящий модуль?

with open('text_4.txt', 'r', encoding='utf-8') as f_1:
    for line in f_1:
        with (open('text_new', 'a', encoding='utf-8')) as f_new:
            # а как записать блок в каждый новый файл? text_[n], допустим, не работает
            line_list = line.split()
            line_list[0] = translate_dict.get(line_list[0])
            line_list.append('\n')
            f_new.writelines(line_list)

