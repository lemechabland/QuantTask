import unittest
from QA_Core.Primitives.Currency import Currency


class TestCurrencyConstructor(unittest.TestCase):
    def setUp(self):
        self.usd_currency = Currency('usd')
        self.zar_currency = Currency('ZAR')
        self.another_usd_currency = Currency('usd')

    def test_currency_can_be_constructed(self):
        self.assertEqual(self.usd_currency.get_name(), 'USD')
        self.assertEqual(self.zar_currency.get_name(), 'ZAR')

    def test_two_currency_doesnt_have_same_hash(self):
        self.assertNotEqual(hash(self.usd_currency), hash(self.zar_currency))
        self.assertNotEqual(hash(self.usd_currency), hash(self.another_usd_currency))

    def test_neq(self):
        self.assertTrue(self.usd_currency != self.zar_currency)

    def test_eq(self):
        self.assertFalse(self.usd_currency == self.another_usd_currency)


if __name__ == '__main__':
    unittest.main()
