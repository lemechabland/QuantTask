from QA_Core.Primitives.MarketObservables import MarketObservable
from QA_Core.Primitives.Currency import Currency
from QA_Core.Conventions.Tenors import Tenor


class FloatRateIndex(MarketObservable):
    """
    An object to describe a floating rate index such as SOFR, US.T-Bill, Ibor, etc...
    """

    def __init__(self, object_name: str, currency: Currency, tenor: Tenor):
        self._objectName = object_name
        self._ccy = currency
        self._tenor = tenor

    @property
    def Currency(self) -> Currency:
        return self._ccy

    @property
    def Tenor(self) -> Tenor:
        return self._tenor

    def __str__(self):
        return self._objectName
