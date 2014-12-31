from animals import Animals
import json


class Zoo:

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def see_animals(self):
        return self.animals

    def accommodate(self, animal):
        if isinstance(animal, Animals):
            if len(self.animals) < self.capacity:
                self.animals.append(animal)
            else:
                print("Capacity is full. Animal was not added")
        else:
            print("This animal does not exist!")

    def zoo_daily_balance(self):
        file = open("species", "r")
        species_dict = json.loads(file.read())
        for animal in self.animals:
            self.budget += 60
            if species_dict[animal.species]["food_type"] == "meat":
                meat_cost = species_dict[animal.species]["food_per_kilos"]
                meat_cost *= animal.weight*4
                self.budget -= meat_cost
            else:
                gras_cost = species_dict[animal.species]["food_per_kilos"]
                gras_cost *= animal.weight * 2
                self.budget -= gras_cost
        return self.budget

    def can_the_animalas_reproduce(self):
        species_list = {}
        for animal in self.animals:
            if animal.species not in species_list:
                species_list[animal.species][animal.gender] = True
            elif species_list[animal.species][animal.gender] is not True:
                species_list[animal.species][animal.gender] = True
        species_list2 = {}
        for species in species_list:
            if species['male'] is True and species['female'] is True:
                species_list2 += species
        return species_list2

    def move_to_habitat(self, name, species):
        for index, animal in enumerate(self.animals):
            if (animal.species == species and
                    animal.name == name):
                self.animals.pop(index)
                print("%s the %s is free now!" % (name, species))
                return True
            else:
                print("There is no such an animal in this zoo!!!")
                return False
