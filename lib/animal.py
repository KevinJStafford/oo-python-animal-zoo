import ipdb
class Animal:
    all= []

    def __init__(self, species, weight, nickname, zoo_instance):
        self.nickname= nickname
        self.weight= weight
        self.species= species
        self.zoo = zoo_instance
        Animal.all.append(self)

    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, new_nickname):
        if not hasattr(self, '_nickname'):
            self._nickname = new_nickname
        else:
            print('Cannot change nickname')
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, new_species):
        if not hasattr(self, '_species'):
            self._species = new_species
        else:
            print('Cannot change species')

    @classmethod
    def find_by_species(cls, species):
        return [animal for animal in cls.all if animal.species == species]