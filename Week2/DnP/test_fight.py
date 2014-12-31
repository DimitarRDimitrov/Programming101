import orc
import hero
import fight
import weapon
import unittest


class FightTest(unittest.TestCase):
    def setUp(self):
        self.my_hero = hero.Hero("Dick", 100, "Dickenson")
        self.my_orc = orc.Orc("Zul", 150, 1.2)
        self.hero_wep = weapon.Weapon("Glorious pickle", 20, 0.5)
        self.orc_wep = weapon.Weapon("Murderous fist", 15, 0.3)
        self.my_hero.equip_weapon(self.hero_wep)
        self.my_orc.equip_weapon(self.orc_wep)
        self.fight = fight.Fight(self.my_orc, self.my_hero)

    def test_fight_scenario(self):
        self.fight.simulate_fight()
        self.assertEqual(self.fight.victory, 2)

if __name__ == '__main__':
    unittest.main()
