from abc import ABC, abstractmethod


class AbstractHouse(ABC):
    @abstractmethod
    def get_count_of_rooms(self) -> float:
        pass


class AbstractCar(ABC):
    @abstractmethod
    def get_horsepower(self) -> float:
        pass


class AbstractPhone(ABC):
    @abstractmethod
    def get_memory(self) -> float:
        pass


class AbstractManKitFactory(ABC):
    @abstractmethod
    def create_house(self) -> AbstractHouse:
        pass

    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_phone(self) -> AbstractPhone:
        pass


class RichManKitFactory(AbstractManKitFactory):
    def create_house(self) -> AbstractHouse:
        return RichHouse()

    def create_car(self) -> AbstractCar:
        return RichCar()

    def create_phone(self) -> AbstractPhone:
        return RichPhone()


class RichHouse(AbstractHouse):
    def get_count_of_rooms(self) -> float:
        return 5


class RichCar(AbstractCar):
    def get_horsepower(self) -> float:
        return 500


class RichPhone(AbstractPhone):
    def get_memory(self) -> float:
        return 12288


class PoorManKitFactory(AbstractManKitFactory):

    def create_house(self) -> AbstractHouse:
        return PoorHouse()

    def create_car(self) -> AbstractCar:
        return PoorCar()

    def create_phone(self) -> AbstractPhone:
        return PoorPhone()


class PoorHouse(AbstractHouse):
    def get_count_of_rooms(self) -> float:
        return 3


class PoorCar(AbstractCar):
    def get_horsepower(self) -> float:
        return 100


class PoorPhone(AbstractPhone):
    def get_memory(self) -> float:
        return 1024


class Man:
    def __init__(self, factory: AbstractManKitFactory):
        self.kit_factory = factory

    def buy_house(self) -> AbstractHouse:
        return self.kit_factory.create_house()

    def buy_car(self) -> AbstractCar:
        return self.kit_factory.create_car()

    def buy_phone(self) -> AbstractPhone:
        return self.kit_factory.create_phone()


def create_man(kit_factory: AbstractManKitFactory) -> Man:
    man = Man(kit_factory)
    house = man.buy_house()
    car = man.buy_car()
    phone = man.buy_phone()
    print(man)
    print(f"[{house}] Count of rooms in house: {house.get_count_of_rooms()}")
    print(f"[{car}] Horsepower in car: {car.get_horsepower()}")
    print(f"[{phone}] Memory in phone: {phone.get_memory()}")

    return man


if __name__ == "__main__":
    """
    Example:
    
    Which factory do you want? 1 - Rich, 2 - Poor: 1
    <__main__.Man object at 0x7f90f0553b60>
    [<__main__.RichHouse object at 0x7f90f0553bc0>] Count of rooms in house: 5
    [<__main__.RichCar object at 0x7f90f0553380>] Horsepower in car: 500
    [<__main__.RichPhone object at 0x7f90f0553a10>] Memory in phone: 12288
    """
    which_factory = int(input("Which factory do you want? 1 - Rich, 2 - Poor: "))
    if which_factory == 1:
        man_kit_factory = RichManKitFactory()
    elif which_factory == 2:
        man_kit_factory = PoorManKitFactory()
    else:
        raise Exception("Wrong input")

    man_ = create_man(man_kit_factory)
