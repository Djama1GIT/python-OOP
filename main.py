# getattr(obj, name, [, default]) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет наличие атрибута name у obj
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается)
# delattr(obj, name) - удаляет атрибут name у obj
#
# некоторые магические методы:
# метод __doc__ - возвращает строку с документацией
# метод __dict__ - возвращает набор атрибутов экземпляра класса

class MagicMethods:
    param = False
    forbidden = True

    def __call__(self, *args, **kwargs):
        """
        Магический метод __call__
        """

    def __new__(cls, *args, **kwargs):
        """
        Магический метод __new__ - вызывается перед созданием объекта класса
        """
        print("Магический метод __new__ сработал")
        return super().__new__(cls)  # Вызываем метод __new__ из суперкласса(object). Иначе __init__ не сработает

    def __init__(self):
        """
        Магический метод __init__ - Инициализатор - вызывается сразу после создания объекта класса
        """
        print("Магический метод __init__ сработал")

    def __del__(self):
        """
        Магический метод __del__ - Финализатор - вызывается перед удалением объекта класса
        """
        print("Магический метод __del__ сработал")

    def __getattribute__(self, item):
        """
        Магический метод __getattribute__ - Непременно вызывается при попытке доступа к атрибуту экземпляра класса.
        Метод должен вернуть вычисленное значение для указанного атрибута, либо поднять исключение AttributeError.

        self - Ссылка на экземпляр.
        item - Имя атрибута, к которому был затребован доступ.
        """
        # Пример использования:
        if item == 'forbidden':  # Атрибут, доступ к которому мы хотим запретить
            raise AttributeError(f"Доступ атрибуту '{item}' запрещен!")  # вызвать ошибку
        else:
            print("Магический метод __getattribute__ сработал")
            return object.__getattribute__(self, item)  # Метод возвращает вычисленное значение для указанного атрибута

    def __setattr__(self, key, value):
        """
        Магический метод __setattr_ - Вызывается при попытке присвоения объекту значения атрибута.
        """
        # Пример использования:
        if key == 'param':  # Атрибут, доступ к которому мы хотим запретить
            raise AttributeError(f"Доступ атрибуту '{key}' запрещен!")  # вызвать ошибку
        else:
            print("Магический метод __setattr__ сработал")
            return object.__setattr__(self, key, value)  # Изменить значение атрибута

    def __getattr__(self, item):
        """
        Магический метод __getattr__  - Вызывается при обращении к несуществующему атрибуту
        """
        print("Магический метод __getattr__ сработал")
        return None  # Если атрибут не существует, то вернуть None

    def __delattr__(self, item):
        """
        Магический метод __delattr - Вызывается при удалении объекта класса
        """
        print("Магический метод __delattr__ сработал")
        object.__delattr__(self, item)  # Удалить атрибут


class Singleton:  # Паттерн Singleton
    """
    Одиночка (англ. Singleton) — порождающий шаблон проектирования, гарантирующий,
    что в однопоточном приложении будет единственный экземпляр некоторого класса,
    и предоставляющий глобальную точку доступа к этому экземпляру.
    """
    __instance = None  # Ссылка на экземпляр класса

    def __call__(self, *args, **kwargs):  # без этого метода каждый раз при объявлении класса данные будут меняться
        pass  # будет описан позже

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance  # Возврат ссылки на экземпляр класса. Если его нет, то он создастся.

    def __del__(self):
        Singleton.__instance = None


class Methods:
    z = 0

    def instance_method(self):
        """
        Это метод экземпляра класса.

        Это наиболее часто используемый вид методов. Методы экземпляра класса принимают объект класса как первый
        аргумент, который принято называть self(он указывает на сам экземпляр).
        Количество параметров метода не ограничено.

        Используя параметр self, мы можем менять состояние объекта и обращаться к другим его методам и параметрам.
        К тому же, используя атрибут self.__class__, мы получаем доступ к атрибутам класса и возможности менять
        состояние самого класса. То есть методы экземпляров класса позволяют менять
        как состояние определённого объекта, так и класса.
        """
        pass

    @classmethod
    def class_method(cls, x, y):
        """
        Методы класса принимают класс в качестве параметра, который принято обозначать как cls.
        Он указывает на класс ToyClass, а не на объект этого класса.
        При декларации методов этого вида используется декоратор classmethod.

        Методы класса привязаны к самому классу, а не его экземпляру. Они могут менять состояние класса,
        что отразится на всех объектах этого класса, но не могут менять конкретный объект.
        """
        return x + y + cls.z

    @staticmethod
    def static_method(x, y):
        """
        Статические методы декларируются при помощи декоратора staticmethod.
        Им не нужен определённый первый аргумент (ни self, ни cls).
        Их можно воспринимать как методы, которые “не знают, к какому классу относятся”.

        Таким образом, статические методы прикреплены к классу лишь для удобства и не могут менять состояние ни класса,
        ни его экземпляра.
        """
        return x + y


class Decorators:
    pass


class Iterators:
    pass


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

    def __init__(self, name, age, breed=None):  # self - имя для аргумента, представляющего текущий объект класса.
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

    class Encapsulation:
        """
        Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
        Инкапсуляция делает некоторые из компонент доступными только внутри класса.
        Инкапсуляция в Python работает лишь на уровне соглашения между программистами о том,
        какие атрибуты являются общедоступными, а какие — внутренними.
        """

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def get_coord(self):
            """
            Это геттер.
            Геттеры (получатели) в Python – это методы, которые используются
            в объектно-ориентированном программировании (ООП) для доступа к частным атрибутам класса.
            """
            return self.__x, self.__y

        def set_coord(self, x=0, y=0):
            """
            А это сеттер.
            Сеттер (установщик) в Python – это метод, который используется для установки значения свойства.
            В объектно-ориентированном программировании очень полезно устанавливать значение частных атрибутов в классе.
            Как правило, геттеры и сеттеры в основном используются для обеспечения инкапсуляции данных в ООП.
            """
            if x != y:
                self.__x = x
                self.__y = y
                print('Success!')
            else:
                raise Exception("Incorrect data!")

        @staticmethod
        def public():
            print('Это публичный метод!')

        @staticmethod
        def _protected():
            print('Это защищенный метод!')

        @staticmethod
        def __private(secret=""):
            print('Это приватный метод!', secret)

    def abstraction():
        """
        Абстракции - это конструкторы, позволяющие создавать последовательности из других последовательностей.

        Абстрактным называется класс, который содержит один и более абстрактных методов.
        Абстрактным называется объявленный, но не реализованный метод.
        Абстрактные классы не могут быть инстанциированы, от них нужно унаследовать,
        реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса.
        """

    def inheritance():
        """
        Наследование позволяет объявить класс, который дублирует функциональность уже существующего класса.
        С помощью этой концепции вы сможете расширить возможности своего класса.
        """
        # class Cat():
        #    pass
        # class Dog(Cat): класс Dog наследуется от класса Cat - более подробный пример в начале файла
        #    pass

    magic = MagicMethods()
    magic_param = magic.param
    try:
        magic_forbidden = magic.forbidden
    except Exception as s:
        print(f"{s.args[0]} ({s.__class__})")
    magic.forbidden = False
    try:
        magic.param = True
    except Exception as s:
        print(f"{s.args[0]} ({s.__class__})")
    print(magic.empty)
    del magic.forbidden
    del magic
    abstraction()
    inheritance()
    polymorphism()
    xy = Encapsulation()
    xy.public()
    xy._protected()  # тут PyCharm ругается, что неудивительно
    try:
        xy.__private()  # тут тоже, думаю понятно почему
    except Exception as s:
        print('Увы', s)
        print('Но......')
        xy._Encapsulation__private("Почти...")  # и тут
    try:
        xy.set_coord(1, 1)
    except Exception as exc:
        print(exc)
    xy.set_coord(1, 2)
    print(xy.get_coord())


if __name__ == '__main__':
    oop_test()
