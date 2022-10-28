# getattr(obj, name, [, default]) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет наличие атрибута name у obj
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается)
# delattr(obj, name) - удаляет атрибут name у obj
# метод __doc__ - возвращает строку с документацией
# метод __dict__ - возвращает набор атрибутов экземпляра класса

class MagicMethods:
    ...


# просто класс
# class Cat:
#     default_breed = None
#
#     def __init__(self, name, age, breed=default_breed):
#         self.name = name
#         self.age = age
#         self.breed = breed     -- изменение default_breed не приведет ни к чему

class Cat:
    default_breed = None

    def __init__(self, name, age, breed=None):
        self.name = name
        self.age = age
        self.breed = breed if breed else self.default_breed  # а тут норм

    def print(self):
        print(self.name, ": ", self.age, "y.o. (", self.breed, ")", sep="")


class Dog(Cat):  # наследование
    def __init__(self, name, age, breed=None, guide=False):
        super(self.__class__, self).__init__(name, age, breed)
        self.guide = guide

    def print(self):
        print(self.name, ": ", self.age, "y.o. (", self.breed, ")", " - Guide-dog" if self.guide else "", sep="")


def oop_test():
    def polymorphism():
        """
        Полиморфизм — очень важная идея в программировании.
        Она заключается в использовании единственной сущности(метод, оператор или объект)
        для представления различных типов в различных сценариях использования.
        """
        cats = []
        cats += [Cat('Alex', 3)]
        cats += [Cat('George', 4, 'British')]
        Cat.default_breed = 'Scottish'
        cats += [Cat('Scott', 5)]
        cats += [Cat('Will', 2)]
        dogs = []
        dogs += [Dog('Sharik', 10, 'Husky', True)]
        animals = cats + dogs

        [animal.print() for animal in animals]  # а вот и полиморфизм в действии

    def encapsulation():
        """
        Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
        Инкапсуляция делает некоторые из компонент доступными только внутри класса.
        Инкапсуляция в Python работает лишь на уровне соглашения между программистами о том,
        какие атрибуты являются общедоступными, а какие — внутренними.
        """

    def abstraction():
        """
        Абстракции - это конструкторы, позволяющие создавать последовательности из других последовательностей.

        Абстрактным называется класс, который содержит один и более абстрактных методов.
        Абстрактным называется объявленный, но не реализованный метод.
        Абстрактные классы не могут быть инстанциированы, от них нужно унаследовать,
        реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса.
        """

    def inheritance():
        # class Cat():
        #    pass
        # class Dog(Cat): класс Dog наследуется от класса Cat - более подробный пример в начале файла
        #    pass
        """
        Наследование позволяет объявить класс, который дублирует функциональность уже существующего класса.
        С помощью этой концепции вы сможете расширить возможности своего класса.
        """

    abstraction()
    inheritance()
    polymorphism()
    encapsulation()


if __name__ == '__main__':
    oop_test()
