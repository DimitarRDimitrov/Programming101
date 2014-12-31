import unittest
from animals import Animals


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.panda = Animals("Pandio", 48, "panda", "male", 245)

    def test_init(self):
        self.assertEqual(self.panda.name, "Pandio")
        self.assertEqual(self.panda.age, 48)
        self.assertEqual(self.panda.species, "panda")
        self.assertEqual(self.panda.gender, "male")
        self.assertEqual(self.panda.weight, 245)

    def test_get_name(self):
        panda2 = Animals("Diva_Panda", 24, "panda", "female", 190)
        self.assertEqual(panda2.name, "Diva_Panda")
        tiger = Animals("Pesho", 26, "tiger", "male", 170)
        self.assertEqual(tiger.name, "Pesho")

    def test_grow(self):
        self.panda.grow()
        self.assertEqual(self.panda.weight, 260)

if __name__ == '__main__':
    unittest.main()
