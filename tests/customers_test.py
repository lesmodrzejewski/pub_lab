import unittest
from src.customers import Customer
from src.drinks import Drinks


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("JohnDoe", 100.00) 

    def test_has_name(self):
        self.assertEqual("JohnDoe", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_add_drink_to_customer(self):
       drink = Drinks("Beer", 5.00)
       self.customer.reduce_wallet_amount(drink.price)
       self.assertEqual(95.00, self.customer.wallet)
