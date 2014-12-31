import weapon
import unittest


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.my_axe = weapon.Weapon("Mighty Axe", 20, 0.5)

    def test_critical_strike_chance(self):
        my_list = []
        for i in range(1000):
            my_list.append(self.my_axe.critical_hit())
        self.assertTrue(True in my_list)
        self.assertTrue(False in my_list)

if __name__ == '__main__':
    unittest.main()
