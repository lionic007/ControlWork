from math import pi
from abc import ABC, abstractmethod


# Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0: raise ValueError("Возраст не может быть отрицательным")
        self._age = age

    def get_age(self):
        return self._age


# Пример использования: 

p = Person()
try:
    p.set_age(25)
    print(p.get_age())  # Вывод: 25
    p.set_age(-5)  # Должна быть ошибка или предупреждение
except ValueError as e:
    print(e)

# Наследие
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
# Пример использования:
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow

# Задание 3. Полиморфизм
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

# Пример использования:
car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling