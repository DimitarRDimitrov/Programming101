from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        self.name = name
        self.health = health
        self.berserk_factor = berserk_factor
        self._MAX_HEALTH = health
        self._set_selfberserk_factor(berserk_factor)

    def _set_selfberserk_factor(self, berserk_factor):
        if berserk_factor > 2.0:
            self.berserk_factor = 2
        elif berserk_factor < 1.0:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

