import ipdb
from lib.animal import Animal

class Zoo:
    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)
    
    def animals(self):
        animals_list = []
        for animal in Animal.all:
            if animal.zoo == self:
                animals_list.append(animal)
        return animals_list
    
    def animal_species(self):
        new_list= []
        for a in self.animals():
            if a.species not in new_list:
                new_list.append(a.species)
        return new_list
        # return [a.species for a in Animal.all if a.zoo == self]

    def animal_nickname(self):
        return [animal.nickname for animal in Animal.all if animal.zoo == self]
    
    @classmethod
    def find_by_location(cls, location):
        return [zoo for zoo in Zoo.all if zoo.location == cls] 
