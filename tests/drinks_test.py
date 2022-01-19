import unittest
from src.drinks import Drinks

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("Beer", 5.00)
    
    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drinks.price)

