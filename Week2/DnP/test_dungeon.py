from dungeon import Dungeon
import hero
import orc
import weapon
import unittest


class DungeonTest(unittest.TestCase):
    def setUp(self):
        self.map4e = Dungeon("basic_dungeon.txt")
        self.my_hero = hero.Hero("Dick", 100, "Dickenson")
        self.my_orc = orc.Orc("Zul", 150, 1.2)
        self.hero_wep = weapon.Weapon("Glorious pickle", 20, 0.5)
        self.orc_wep = weapon.Weapon("Murderous fist", 15, 0.3)
        self.my_hero.equip_weapon(self.hero_wep)
        self.my_orc.equip_weapon(self.orc_wep)

    def test_dungeon_init(self):
        self.assertEqual(self.map4e.map_path, "basic_dungeon.txt")

    def test_printmap_working(self):
        self.assertTrue(self.map4e.print_map())

    # def test_actual_mapping(self):

    def test_spawnpoint(self):
        self.assertTrue(self.map4e.spawn("player_1", self.my_hero))
        self.assertTrue(self.map4e.spawn("player_2", self.my_orc))
        self.assertFalse(self.map4e.spawn("player_3", self.my_orc))
        print(self.map4e.print_map())





if __name__ == '__main__':
    unittest.main()
