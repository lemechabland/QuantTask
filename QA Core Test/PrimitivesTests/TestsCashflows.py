import unittest
from QA_Core.Primitives.Currency import Currency
from QA_Core.Primitives.Cashflow import Cashflow
from QA_Core.Conventions.Dates import Date


class TestCashflowConstructor(unittest.TestCase):

    def setUp(self):
        self._usd = Currency('usd')
        self._cf_date = Date(2024, 7, 4)
        self.cashflow = Cashflow(self._cf_date, 10000.0, self._usd)

    def test_cashflow_can_be_constructed(self):
        self.assertEqual(self.cashflow.Amount, 10000.0)
        self.assertEqual(self.cashflow.Currency, self._usd)
        self.assertEqual(self.cashflow.Date, self._cf_date)


if __name__ == '__main__':
    unittest.main()
