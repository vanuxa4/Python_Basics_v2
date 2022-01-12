"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Let's go")

    def stop(self):
        print("Stop")

    def turn(self, direction):
        print(f'Turn {direction}')

    def show_speed(self):
        print(f"Current speed is {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        print(f"Speed is over limit 60 km/h" if self.speed > 60 else f"Current speed is {self.speed} km/h")



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Speed is over limit 40 km/h" if self.speed > 40 else f"Current speed is {self.speed} km/h")


class PoliceCar(Car):
    pass


vehicle_1 = TownCar(40, 'black', TownCar)
vehicle_2 = SportCar(120, 'black', SportCar)
vehicle_3 = PoliceCar(120, 'black', PoliceCar, True)
