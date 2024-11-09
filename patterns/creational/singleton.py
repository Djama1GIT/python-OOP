from collections import defaultdict


class Connector:
    counter = defaultdict(int)

    def __init__(self, type_="Simple"):
        Connector.counter[type_] += 1
        print(f"{type_} Connection created [{self.counter[type_]=}]")


class SingletonConnection:
    _instances = {}
    counter = 0

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonConnection, cls).__new__(cls)
        return cls._instances[cls]

    def __init__(self):
        self.connector = Connector()
        SingletonConnection.counter += 1

    def __repr__(self):
        return f"SingletonConnection [{self.connector.counter['Simple']=}]"


def example_singleton():
    """
    >>> print(x1 := SingletonConnection())
    Simple Connection created [self.counter[type_]=1]
    SingletonConnection [self.connector.counter['Simple']=1]
    >>> print(x2 := SingletonConnection())
    Simple Connection created [self.counter[type_]=2]
    SingletonConnection [self.connector.counter['Simple']=2]
    >>> print(x3 := SingletonConnection())
    Simple Connection created [self.counter[type_]=3]
    SingletonConnection [self.connector.counter['Simple']=3]
    >>> print(x4 := SingletonConnection())
    Simple Connection created [self.counter[type_]=4]
    SingletonConnection [self.connector.counter['Simple']=4]
    >>> print(x1 is x2 is x3 is x4)
    True
    """
    SingletonConnection()  # Simple Connection created [self.counter[type_]=1]
    SingletonConnection()  # Simple Connection created [self.counter[type_]=2]
    SingletonConnection()  # Simple Connection created [self.counter[type_]=3]
    SingletonConnection()  # Simple Connection created [self.counter[type_]=4]


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class MetaSingletonConnection(metaclass=MetaSingleton):
    def __init__(self):
        self.connector = Connector('Meta')

    def __repr__(self):
        return f"MetaSingletonConnection [{self.connector.counter['Meta']=}]"


def example_meta_singleton():
    """
    >>> print(x1 := MetaSingletonConnection())
    Meta Connection created [self.counter[type_]=1]
    MetaSingletonConnection [self.connector.counter['Meta']=1]
    >>> print(x2 := MetaSingletonConnection())
    MetaSingletonConnection [self.connector.counter['Meta']=1]
    >>> print(x3 := MetaSingletonConnection())
    MetaSingletonConnection [self.connector.counter['Meta']=1]
    >>> print(x4 := MetaSingletonConnection())
    MetaSingletonConnection [self.connector.counter['Meta']=1]
    >>> x1 is x2 is x3 is x4
    True
    """
    MetaSingletonConnection()  # Meta Connection created [self.counter[type_]=1]
    MetaSingletonConnection()
    MetaSingletonConnection()
    MetaSingletonConnection()


def main():
    example_singleton()
    example_meta_singleton()


if __name__ == '__main__':
    main()
