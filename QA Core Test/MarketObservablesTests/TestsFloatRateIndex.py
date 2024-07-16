import unittest
from QA_Core.Market_Observables.FloatingRateIndex import FloatRateIndex
from QA_Core.Primitives.Currency import Currency
from QA_Core.Conventions.Tenors import Tenor


class TestFloatRateIndexConstructor(unittest.TestCase):
    def setUp(self):
        self.usd = Currency('usd')
        self.fedFund = FloatRateIndex("FEDFUND.1B", self.usd, Tenor.from_days(1))
        self.sofr = FloatRateIndex("SOFR.1B", self.usd, Tenor.from_days(1))

    def test_FloatingRate_Can_Get_Currency(self):
        self.assertEqual(self.fedFund.Currency, self.usd)
        self.assertEqual(self.sofr.Currency.get_name(), 'USD')

    def test_FloatingRate_Can_Be_Compared(self):
        self.assertNotEqual(self.fedFund, self.sofr)

    def test_FloatingRate_Can_Get_Tenor(self):
        self.assertEqual(self.fedFund.Tenor, self.sofr.Tenor)

    def test_FloatingRate_Can_Be_Represented(self):
        self.assertEqual(str(self.sofr), "SOFR.1B")


if __name__ == '__main__':
    unittest.main()
