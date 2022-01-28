"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


class OfficeApliance():
    """Офисная техника"""

    def __init__(self, title):
        self.title = title

    def turn_on(self):
        return f'{self.title} включен.'

    def turn_of(self):
        return f'{self.title} выключен.'


class Printer(OfficeApliance):
    """Принтер"""

    def __init__(self, name, model, pr_speed):
        self.name = name
        self.model = model
        self.pr_speed = pr_speed
        super().__init__(title='Принтер')


class Xerox(OfficeApliance):
    """Ксерокс"""

    def __init__(self, name, model, cop_speed):
        self.name = name
        self.model = model
        self.cop_speed = cop_speed
        super().__init__(title='Ксерокс')


class Scanner(OfficeApliance):
    """Сканер"""

    def __init__(self, name, model, sc_speed):
        self.name = name
        self.model = model
        self.sc_speed = sc_speed
        super().__init__(title='Сканнер')


class Stock():
    """Склад"""

    def __init__(self, name_div, capacity=0):
        self.capacity = capacity
        self.name_div = name_div  # наименование подразделения, где хранится техника
        self.apliance_in_stock = dict()  # техника на складе в конкретном подразделении

    def take(self, name, quantity):
        """Прием на склад"""
        if self.apliance_in_stock.get(name) is None:
            self.apliance_in_stock[name] = 0
            # присваиваем количество 0 новому экземпляру техники, которого еще нет на складе, иначе += работать не будет
        self.apliance_in_stock[name] += quantity
        # += для сложения количества, если экземляр техники на складе уже присутствует

    def give(self, name, quantity):
        """Выдача со склада"""
        if quantity == self.apliance_in_stock.get(name):  # удалить все еденицы на складе
            del self.apliance_in_stock[name]
        else:
            self.apliance_in_stock[name] -= quantity

    def in_stock(self):
        ls = [f'{item.name} {item.model}: {quantity} шт.' for item, quantity in self.apliance_in_stock.items()]
        print('_' * 50)
        print(f'Склад "{self.name_div}":')
        for item in ls:
            print(item)
        print(f'Осталось места для {self.capacity - sum(self.apliance_in_stock.values())} шт.')
        print('_' * 50)


printer_1 = Printer('Canon', 'PIXMA G1411', 8.8)
printer_2 = Printer('HP', 'LaserJet Pro M15w W2G51A', 18)
xerox_1 = Xerox('Xerox', 'B1022 MFP', 22)
xerox_2 = Xerox('Epson', 'L3151', 33)
scanner_1 = Scanner('Fujitsu', 'Fi-7160', 60)
scanner_2 = Scanner('Canon', 'ImageFormula DR-C130', 30)

office_aplience = [printer_1, printer_2, xerox_1, xerox_2, scanner_1, scanner_2]

stock_1 = Stock('Отдел кадров', 10)
while True:
    print('*' * 50)
    action = input('Выберите действие:\n 1 - принять на склад\n 2 - выдать со склада\n"Enter" - выход \n>>:')
    if action == '':  # выход из программы
        break

    if action == '1':  # принимаем на склад
        for number, item in enumerate(office_aplience):  # указываю перечень доступной техники
            print(f'{number + 1} - {item.title}: {item.name} {item.model}')
        print('_' * 50)
        applience_number = input('Укажите номер желаемой техники для перемещения на склад:\n"Enter" - выход \n>>:')
        if applience_number == '':  # выход из программы
            break
        if int(applience_number) not in range(1, len(office_aplience) + 1):
            print(f'\033[31m Введено недопустимое значение.\033[0;0m')
            continue
        print('_' * 50)
        applience_quantity = input('Укажите количество :\n"Enter" - выход \n>>:')
        if applience_quantity == '':  # выход из программы
            break
        if int(applience_quantity) > stock_1.capacity - sum(stock_1.apliance_in_stock.values()):
            print('\033[31m Места на складе недостаточно.\033[0;0m')
            continue
        stock_1.take(office_aplience[int(applience_number) - 1], int(applience_quantity))
        print(f'Вы переместили на склад "{stock_1.name_div}" {applience_quantity} ед.')
        stock_1.in_stock()

    if action == '2':  # вадача со склада
        if len(stock_1.apliance_in_stock) == 0:
            print('На складе нет техники.')
        print(f'Склад "{stock_1.name_div}"')
        for number, item in enumerate(stock_1.apliance_in_stock):
            print(f'{number + 1} - {item.title}: {item.name} {item.model} - {stock_1.apliance_in_stock.get(item)} шт.')
        aplience_for_give = []  # список ключей для удаления из словаря техника на складе
        for name in stock_1.apliance_in_stock.keys():
            aplience_for_give.append(name)
        print('_' * 50)
        applience_number = input('Укажите номер желаемой техники для для выдачи со склада:\n"Enter" - выход \n>>:')
        if applience_number == '':  # выход из программы
            break
        print('_' * 50)
        applience_quantity = input('Укажите количество :\n"Enter" - выход \n>>:')
        if applience_quantity == '':  # выход из программы
            break

        stock_1.give(aplience_for_give[int(applience_number) - 1], int(applience_quantity))
        print(f'Вы выдали со склада "{stock_1.name_div}" {applience_quantity} ед.')
        stock_1.in_stock()
