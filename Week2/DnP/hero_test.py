import hero
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 100, "DragonSlayer")
    
    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_hero_known_as(self):
        self.assertEqual("Bron the DragonSlayer", self.bron_hero.known_as())

    def test_hero_get_health(self):
        self.assertEqual(self.bron_hero.get_health(), 100)

    def test_hero_is_alive(self):
        self.assertEqual(self.bron_hero.is_alive(), True)
        self.bron_hero.health = 0
        self.assertEqual(self.bron_hero.is_alive(), False)

    def test_hero_get_damage(self):
        self.bron_hero.take_damage(20)
        self.assertEqual(self.bron_hero.get_health(), 80)
        self.bron_hero.take_damage(20.8)
        self.assertEqual(self.bron_hero.get_health(), 59.2)
        self.bron_hero.take_damage(99)
        self.assertEqual(self.bron_hero.get_health(), 0)

    def test_hero_healing(self):
        self.bron_hero.take_damage(30)
        self.assertEqual(self.bron_hero.take_healing(20), True)
        self.assertEqual(self.bron_hero.take_healing(40), True)
        self.bron_hero.take_damage(120)
        self.assertEqual(self.bron_hero.take_healing(20), False)

if __name__ == '__main__':
    unittest.main()

