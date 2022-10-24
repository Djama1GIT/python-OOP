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


class Dog(Cat):
    def __init__(self, name, age, breed=None, guide=False):
        super(self.__class__, self).__init__(name, age, breed)
        self.guide = guide

    def print(self):
        print(self.name, ": ", self.age, "y.o. (", self.breed, ")", " - Guide-dog" if self.guide else "", sep="")


cats = []
cats += [Cat('Alex', 3)]
cats += [Cat('George', 4, 'British')]
Cat.default_breed = 'Scottish'
cats += [Cat('Scott', 5)]
cats += [Cat('Will', 2)]
dogs = []
dogs += [Dog('Sharik', 10, 'Husky', True)]

animals = cats + dogs
if __name__ == '__main__':
    [animal.print() for animal in animals]  # а вот и полиморфизм в действии