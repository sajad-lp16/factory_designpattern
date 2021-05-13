from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):

    @abstractmethod
    def num_of_pages(self):
        pass


class PythonHeadFirst(Book):

    def num_of_pages(self):
        print('500')

    def __repr__(self):
        return self.__class__.__name__


class PythonTricks(Book):

    def num_of_pages(self):
        print('400')

    def __repr__(self):
        return self.__class__.__name__


# Factory
class PublicationFactory:

    def publicator(self, object_type):
        return eval(object_type)().num_of_pages()


# Client
if __name__ == '__main__':
    pf = PublicationFactory()
    obj = pf.publicator(input('Which Book [PythonTricks or PythonHeadFirst]: '))
    print(obj)
