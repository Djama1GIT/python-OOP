import math
from functools import wraps


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
        Магический метод __call__ - вызывается при вызове экземпляра класса.
        Позволяет экземплярам пользовательских типов представляться объектами, поддерживающими вызов.

        Class.__call__() = Class()
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

    def __delete__(self, instance):
        """
        Магический метод __delete__ - используется в дескрипторах.
        Позволяет определить поведение при попытке удаления значения
        указывающему на дескриптор атрибуту класса-владельца.

        Различие с __del__:
        __del__ вызывается ПЕРЕД удалением класса и на него никак не влияет,
        __delete__ вызывается ДЛЯ удаления класса.

        Т.е. код который обычно пишется в __delete __:
        del self.value
        """

    def __get__(self, instance, owner):
        """
        Магический метод __get__ - используется в дескрипторах.
        Позволяет определить поведение при попытке получения значения
        указывающему на дескриптор атрибуту класса-владельца.

        Пример кода тут - getattr(instance, self.name)
        """

    def __set__(self, instance, value):
        """
        Магический метод __set__ - используется в дескрипторах.
        Позволяет определить поведение при попытке присвоения значения
        указывающему на дескриптор атрибуту класса-владельца.

        Пример кода тут - setattr(instance, self.name, value)
        """

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
        Метод должен возвращать значение (возможно вычисляемое) для атрибута,
        либо генерировать исключение AttributeError.
        """
        print("Магический метод __getattr__ сработал")
        return None  # Если атрибут не существует, то вернуть None

    def __delattr__(self, item):
        """
        Магический метод __delattr__ - Вызывается при удалении объекта класса
        """
        print("Магический метод __delattr__ сработал")
        object.__delattr__(self, item)  # Удалить атрибут

    def __str__(self):
        """
        Магический метод __str__

        Вызывается в случаях преобразования экземпляра класса к типу str при помощи функции-конструктора str.
        Должен возвращать объект типа str
        """
        print("Магический метод __str__ сработал")
        return "Magic methods are cool!"

    def __repr__(self):
        """
        Магический метод __repr__

        Вызывается функцией repr для получения строки «формального» представления объекта.
        Позволяет определить результат функции repr() при передаче в неё экземпляра данного класса.
        Также значение __repr__ будет возвращено при вызове из консоли.

        Должен возвращать объект типа str.
        Возвращаемое значение также будет использовано, если не определён __str__.
        """
        return self.__class__

    def __abs__(self):
        """
        Магический метод __abs__ - Вызывается функцией abs(), которая вычисляет модуль
        """
        return abs(1+1j)  # здесь могут быть элементы из self, например, return list(map(abs, self.xyz))

    def __len__(self):
        """
        Магический метод __len__ - Вызывается функцией len(), для подсчёта количества элементов в объекте класса,
        то есть для нахождения его длины.
        Должен возвращаться число целое большее, либо равное нулю.
        """
        return 0


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


class Counter:  # Functor
    """
    Функтор — это реализация некоего контекста, в котором находятся данные, причем эти данные можно достать,
    применить к ним функцию, и поместить обратно в контекст.
    Причем от функции требуется только умение работать с самими данными, но не с контекстом.
    """

    def __init__(self):
        self.__count = 0

    def __call__(self, *args, **kwargs):
        self.__count += 1

        return self.__count


class Monostate:
    """
    Паттерн моносостояние (класс Борга)
    Это способ реализации одноэлементного поведения, но вместо того, чтобы использовать только один экземпляр
    класса, существует несколько экземпляров, которые совместно используют одно и то же состояние.
    Другими словами, основное внимание уделяется совместному использованию состояния вместо совместного
    использования идентификатора экземпляра.

    Коротко - все экземпляры этого класса имеют общие атрибуты.
    """
    __attrs = {
        'key': 'value'
    }

    def __init__(self):
        self.__dict__ = self.__attrs


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
        Он указывает на класс, а не на объект этого класса.
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


def decorators():
    def decorator(symbols=''):
        def _decorator(func):
            @wraps(func)  # так декорируемая функция не потеряет свои аргументы(имя, документацию..)
            def wrapper(*args, **kwargs):
                print('Функция-обёртка!')
                print('Выполняем обёрнутую функцию...')
                _return = func(*args, **kwargs)
                for symbol in symbols:
                    _return = _return.replace(symbol, '')
                print('Выходим из обёртки')
                return _return

            wrapper.__func__ = func
            return wrapper

        return _decorator

    @decorator('n ')
    def function(text):
        return text

    print(function('among us'))  # -> amogus

    # print(function.__func__('among us')) -> among us

    # без @decorator('n '), но исполняется так же
    #
    # def function(text):
    #     return text
    # print(decorator('n ')(function)('among us')) -> amogus

    class Derivative:
        # Это простейший пример декоратора-класса, в реальных проектах всё может быть куда сложнее.
        # Короче, просто знай, что так тоже можно.
        def __init__(self, dx=0.001):
            self.dx = dx

        def __call__(self, func):
            @wraps(func)
            def wrapper(x, *args, **kwargs):
                return (func(x + self.dx, *args, **kwargs) - func(x, *args, **kwargs)) / self.dx  # производная

            return wrapper

    @Derivative(dx=0.000001)  # -> dx - точность вычисления производной. Чем меньше dx, тем точнее
    def sin(x):
        return math.sin(x)

    print(sin(math.pi / 3))  # ->> 0.4999995669718871


class Iterators:
    pass


def descriptor():
    class Descriptor:
        """
        Дескриптор это атрибут объекта со “связанным поведением”, то есть такой атрибут,
        при доступе к которому его поведение переопределяется методом протокола дескриптора.
        Эти методы  __get__, __set__ и __delete__.
        Если хотя бы один из этих методов определен в объекте, то можно сказать что этот метод дескриптор.
        """

        @staticmethod
        def verify(param):
            if type(param) is not int:
                raise TypeError('Это не число!')

        def __set_name__(self, owner, name):
            self.name = "_" + name

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            self.verify(value)
            setattr(instance, self.name, value)

    class Params:
        param1 = Descriptor()
        param2 = Descriptor()
        param3 = Descriptor()

        def __init__(self, param1, param2, param3):
            self.param1 = param1
            self.param2 = param2
            self.param3 = param3

        def __str__(self):
            return str(self.__dict__)

    params = Params(1, 2, 3)
    print(params)


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

        #  но работу сеттеров и геттеров можно реализовать и по-другому, с помощью @property
        @property
        def coord(self):  # геттер, срабатывает, при обращении к coord
            print('Геттер property сработал')
            return self.__x, self.__y

        @coord.setter
        def coord(self, coord):  # сеттер, срабатывает при попытке изменения атрибута класса coord
            x, y = coord
            if x != y:
                self.__x = x
                self.__y = y
                print('Сеттер property сработал!')
            else:
                raise Exception("Incorrect data!")

        # Также property можно реализовать и по-другому,
        # будет работать точно так же, но лучше использовать как ^
        # :: coord = property(getter, setter, deleter, docstring)

        @coord.deleter
        def coord(self):  # делитер, срабатывает при попытке удаления атрибута coord
            print('Делитер property сработал')
            del self.__x
            del self.__y

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
    print(magic)
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
    xy.coord = (1, 5)
    print(xy.coord)
    try:
        xy.coord = (1, 1)
    except Exception as s:
        print(s)
    del xy.coord


def test():
    oop_test()
    descriptor()
    decorators()
    c = Counter()  # c -> 0
    [c() for i in range(10)]  # c -> 10
    print(c())  # c -> 11


if __name__ == '__main__':
    test()
