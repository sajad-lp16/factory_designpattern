# Author Sajad

"""
This design pattern is used to create a family
of objects which they are connected together
"""

from abc import ABCMeta, abstractmethod


# main abstract class
class CoffeeFactory(metaclass=ABCMeta):

    @abstractmethod
    def coffee_without_milk(self):
        pass

    @abstractmethod
    def coffee_with_milk(self):
        pass


# This concrete class uses the main abstract class
class FrenchCoffeeFactory(CoffeeFactory):

    def coffee_without_milk(self):
        return FrenchEspresso()

    def coffee_with_milk(self):
        return FrenchCappuccino()


# The same as previous
class ItalianCoffeeFactory(CoffeeFactory):

    def coffee_without_milk(self):
        return ItalianEspresso()

    def coffee_with_milk(self):
        return ItalianCappuccino()


# Another abstract class which they are
# used inside previous classes objects
class CoffeeWithoutMilk(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self):
        pass


# The same as previous
class CoffeeWithMilk(metaclass=ABCMeta):

    @abstractmethod
    def serve(self):
        pass


class FrenchEspresso(CoffeeWithoutMilk):

    def prepare(self):
        print('preparing ', self.__class__.__name__)


class ItalianEspresso(CoffeeWithoutMilk):

    def prepare(self):
        print('preparing ', self.__class__.__name__)


class FrenchCappuccino(CoffeeWithMilk):

    def serve(self):
        print(self.__class__.__name__, ' is served with sheep\'s milk on ',
              CoffeeWithoutMilk.__name__)


class ItalianCappuccino(CoffeeWithMilk):
    def serve(self):
        print(type(self).__name__, ' is served with cow\'s milk on',
              CoffeeWithoutMilk.__name__)


# Client section
class CoffeeStore:

    def make_coffee(self):
        for factory in [ItalianCoffeeFactory(), FrenchCoffeeFactory()]:
            self.factory = factory
            self.coffee_without_milk = self.factory.coffee_without_milk()
            self.coffee_with_milk = self.factory.coffee_with_milk()
            self.coffee_without_milk.prepare()
            self.coffee_with_milk.serve()


coffee = CoffeeStore()
coffee.make_coffee()
