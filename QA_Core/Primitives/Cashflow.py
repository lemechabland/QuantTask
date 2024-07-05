from QA_Core.Conventions.Dates import Date
from . import Currency


class Cashflow:
    def __init__(self, date: Date, amount: float, currency: Currency):
        self._date = date
        self._amount = amount
        self._currency = currency

    @property
    def Amount(self) -> float:
        return self._amount

    @property
    def Currency(self) -> Currency:
        return self._currency

    @property
    def Date(self) -> Date:
        return self._date

