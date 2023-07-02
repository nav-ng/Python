# create a abstract class car, mileage, and wheels
# tesla and suzuki


from abc import ABC, abstractmethod


class car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


class tesla(car):
    def name(self):
        print("Tesla")

    def mileage(self):
        print("204Km/h")

    def wheels(self):
        print("JK tyre")

class suzuki(car):
    def name(self):
        print("Suzuki")

    def mileage(self):
        print("25Km/h")

    def wheels(self):
        print("TVS tyre")


obj1 = tesla()
obj1.name()
obj1.mileage()
obj1.wheels()
obj2 = suzuki()
obj2.name()
obj2.mileage()
obj2.wheels()
