import entity
import weapon
import unittest


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.my_entity = entity.Entity("Gladiator", 99)
        self.my_axe = weapon.Weapon("Gladiator's Axe", 15, 0.5)

    def test_if_weapon_equipped(self):
        self.assertEqual(False, self.my_entity.has_weapon())

    def test_if_weapon_crit(self):
        self.my_entity.equip_weapon(self.my_axe)
        self.assertEqual(self.my_entity.attack(), 30)

if __name__ == '__main__':
    unittest.main()
