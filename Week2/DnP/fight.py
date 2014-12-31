from random import random


class Fight():

    def __init__(self, ork4e, hero4e):
        self.ork4e = ork4e
        self.hero4e = hero4e
        self.victory = 0
        self._set_beginning(self.victory)

    def _set_beginning(self, victory):
        rnd = random()
        if rnd > 0.5:
            self.victory = 1

    def simulate_fight(self):
        while self.victory < 2:
            if self.victory == 0:
                self.ork4e.take_damage(self.hero4e.attack())
                if not self.ork4e.is_alive():
                    self.victory = 2
                    print("{} is Victorious".format(self.hero4e.nickname))
                else:
                    self.victory = 1
                    print("{} has {} health remaining".format(
                        self.ork4e.name, self.ork4e.get_health))
            if self.victory == 1:
                self.hero4e.take_damage(
                    self.ork4e.attack() * self.ork4e.berserk_factor)
                if not self.hero4e.is_alive():
                    self.victory = 2
                    print("{} is Victorious".format(self.ork4e.name))
                else:
                    self.victory = 0
                    print("{} has {} health remaining".format(
                        self.hero4e.name, self.hero4e.get_health))
        return self.victory
