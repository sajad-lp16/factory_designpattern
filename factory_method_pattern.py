from abc import ABCMeta, abstractmethod
import re


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonalInformationSection(Section):

    def describe(self):
        print('Personal information secion')


class AlbumSection(Section):

    def describe(self):
        print('Album section')


class PatentSection(Section):

    def describe(self):
        print('Patent section')


class PublicationSection(Section):

    def describe(self):
        print('Publication section')


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = list()
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)


class LinkedIn(Profile):

    def create_profile(self):
        self.add_section(PersonalInformationSection())
        self.add_section(PublicationSection())
        self.add_section(PatentSection())


class IranianNetwork(Profile):

    def create_profile(self):
        self.add_section(PersonalInformationSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    profile_name = input('Enter the name of social program? ')
    patt = r'.*{}.*'.format(profile_name)
    res = IranianNetwork if re.search(patt, 'IranianNetwork',re.I) else LinkedIn
    obj = res()
    print(obj.__class__.__name__)
    print(obj.get_sections())
