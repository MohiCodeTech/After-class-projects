class Computer:
    def __init__(self, name):
        self.name = name
    def On(self):
        print(f"The computer {self.name} is turned on")
    def Off(self):
        print(f"The computer {self.name} is turned off")

class Windows(Computer):
    def __init__(self, name, version):
        super().__init__(name)
        self.version = version
    def Multitask(self):
        print(f"Windows {self.version} is multitasking... optimizing for better performance")

class Imac(Computer):
    def __init__(self, name, version):
        super().__init__(name)
        self.version = version
    def Connection(self):
        print(f"Imac {self.version} is using lot of internet... speeding up internet usage for better performance")

best_computer = Windows("Best_computer", "11")
best_computer.Multitask()

second_best_computer = Imac("second_best_computer", "Ios 18")
second_best_computer.Connection()

from abc import ABC, abstractmethod
class AnimalAbs(ABC):
    @abstractmethod
    def eat(self):
        pass
class dogabs(AnimalAbs):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} is now barking!")
    def eat(self):
        print(f"{self.name} is eating now")

class catabs(AnimalAbs):
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} is now meowing!")
    def eat(self):
        print(f"{self.name} is eating now")

buddy = dogabs("buddy")
buddy.bark()
buddy.eat()
bingo = catabs("bingo")
bingo.meow()
bingo.eat()
