'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

words = input('Введите несколько слов, разделенных пробелом: ')
words_list = words.split()
for index, value in enumerate(words_list):
    print(f'{index}: {value:.10}') # почему в коде форматирования мне нужно дополнительно указывать точку?
                                   # иначе не отрезает необходимое кол-во символов. Это особенность строки?