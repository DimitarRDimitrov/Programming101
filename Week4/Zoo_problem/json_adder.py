import json


class Animal_Add:
    def __init__(self, species, food_type, life_expectancy, gestation_period,
                 newborn_weight, max_weight, weight_per_month,
                 food_per_kilos):
        self.species = species
        self.food_type = food_type
        self.life_expectancy = life_expectancy
        self.gestation_period = gestation_period
        self.newborn_weight = newborn_weight
        self.max_weight = max_weight
        self.weight_per_month = weight_per_month
        self.food_per_kilos = food_per_kilos
        self.add_to_json()

    def add_to_json(self):
        file = open("species", "r+")
        species_dict = file.read()
        if file.read() == "":
            species_dict = {}
            species_dict[self.species] = {"food_type": self.food_type,
                                          "life_expectancy": self.life_expectancy,
                                          "gestation_period": self.gestation_period,
                                          "newborn_weight": self.newborn_weight,
                                          "max_weight": self.newborn_weight,
                                          "weight_per_month": self.weight_per_month,
                                          "food_per_kilos": self.food_per_kilos}
            file.write(json.dumps(species_dict))
            file.close()
        else:
            species_dict = file.read(json.loads)
            if self.species not in species_dict:
                print(species_dict)
                species_dict[self.species] = {"food_type": self.food_type,
                                              "life_expectancy": self.life_expectancy,
                                              "gestation_period": self.gestation_period,
                                              "newborn_weight": self.newborn_weight,
                                              "max_weight": self.newborn_weight,
                                              "weight_per_month": self.weight_per_month,
                                              "food_per_kilos": self.food_per_kilos}
                file.write(json.dumps(species_dict))
                file.close()


def main():
    Animal_Add("lion", "meat", 30, 6, 12,
               250, 12, 0.07)


if __name__ == '__main__':
    main()
