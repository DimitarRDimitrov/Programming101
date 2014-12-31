import random
import json


class Animals:
    animals_name = {}

    def __init__(self, name, age, species, gender, weight):
        self.age = age
        self.species = species
        self.gender = gender
        self.weight = weight
        self.name = self._get_name(name)
        self.dead = False

    def _get_name(self, name):
        if (self.species in Animals.animals_name and
                name not in Animals.animals_name[self.species]):
            Animals.animals_name[self.species] = name
            return name
        elif(self.species in Animals.animals_name and
                name in Animals.animals_name[self.species]):
            return ValueError
        elif self.species not in Animals.animals_name:
            Animals.animals_name[self.species] = [name]
            return name

    def grow(self):
        self.age += 1
        file = open("species.json", "r")
        species_dict = json.loads(file.read())
        file.close()
        self.weight += species_dict[self.species]["weight_per_month"]

    def is_it_die(self):
        file = open("species.json", "r")
        species_dict = json.loads(file.read())
        file.close()
        life_expectancy = species_dict[self.species]["life_expectancy"]
        chance_of_die = self.age / life_expectancy
        if chance_of_die <= random.random():
            self.dead = True
            print("%s is DEAD!!!" % self.name)
            return True
        else:
            return False

    def eat(self):
        file = open("species.json", "r")
        species_dict = json.loads(file.read())
        consumation = species_dict[self.species]["food_per_kilos"]
        file.close()
        return consumation
