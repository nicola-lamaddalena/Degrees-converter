import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.conv = Converter()

    def test_celFah(self):
        self.assertEqual(self.conv.celFah(0), 32.0)
        self.assertEqual(self.conv.celFah(15.2), 59.36)

    def test_fahCel(self):
        self.assertEqual(self.conv.fahCel(0), -17.78)
        self.assertEqual(self.conv.fahCel(100), 37.78)

    def test_celKel(self):
        self.assertEqual(self.conv.celKel(0), 273.15)
        self.assertEqual(self.conv.celKel(100), 373.15)

    def test_kelCel(self):
        self.assertEqual(self.conv.kelCel(0), -273.15)
        self.assertEqual(self.conv.kelCel(100), -173.15)

    def test_fahKel(self):
        self.assertEqual(self.conv.fahKel(0), 255.37)
        self.assertEqual(self.conv.fahKel(100), 310.93)

    def test_kelFah(self):
        self.assertEqual(self.conv.kelFah(0), -459.67)
        self.assertEqual(self.conv.kelFah(100), -279.67)


if __name__ == "__main__":
    unittest.main()
