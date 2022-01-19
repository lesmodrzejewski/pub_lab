import unittest
from src.customers import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("JohnDoe", 100) 

    def test_has_name(self):
        self.assertEqual("JohnDoe", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    