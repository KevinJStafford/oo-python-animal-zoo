import ipdb
class Animal:
    all= []

    def __init__(self, species, weight, nickname, zoo_instance):
        self.nickname= nickname
        self.weight= weight
        self.species= species
        self.zoo = zoo_instance
        Animal.all.append(self)
