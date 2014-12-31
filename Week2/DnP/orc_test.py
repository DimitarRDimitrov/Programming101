import orc
import unittest


class OrcTest(unittest.TestCase):
    def setUp(self):
        self.zul_orc = orc.Orc("Zul", 100, 1.66)

    # def test_orc_health(self):
    #     self.assertEqual(self.zul_orc.get_health(), 100)

    def test_orc_berserker_value(self):
        self.assertEqual(self.zul_orc.berserk_factor, 1.66)
        self.zul_orc._set_selfberserk_factor(2.5)
        self.assertEqual(self.zul_orc.berserk_factor, 2)
        self.zul_orc._set_selfberserk_factor(0.5)
        self.assertEqual(self.zul_orc.berserk_factor, 1)

    def test_orc_get_health(self):
        self.assertEqual(self.zul_orc.get_health(), 100)

    def test_orc_is_alive(self):
        self.assertEqual(self.zul_orc.is_alive(), True)
        self.zul_orc.health = 0
        self.assertEqual(self.zul_orc.is_alive(), False)

    def test_orc_get_damage(self):
        self.zul_orc.take_damage(20)
        self.assertEqual(self.zul_orc.get_health(), 80)
        self.zul_orc.take_damage(20.8)
        self.assertEqual(self.zul_orc.get_health(), 59.2)
        self.zul_orc.take_damage(99)
        self.assertEqual(self.zul_orc.get_health(), 0)

    def test_orc_healing(self):
        self.zul_orc.take_damage(30)
        self.assertEqual(self.zul_orc.take_healing(20), True)
        self.assertEqual(self.zul_orc.take_healing(40), True)
        self.zul_orc.take_damage(120)
        self.assertEqual(self.zul_orc.take_healing(20), False)

if __name__ == '__main__':
    unittest.main()
