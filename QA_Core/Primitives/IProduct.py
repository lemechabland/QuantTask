from abc import ABC, abstractmethod, abstractproperty
from QA_Core.Primitives.Currency import Currency
from QA_Core.Primitives.Cashflow import Cashflow
from QA_Core.Conventions.Dates import Date
from QA_Core.Primitives.MarketObservables import MarketObservable


class IProduct(ABC):
    """
    Product representation
    """
    def __init__(self) -> None:
        self._id = "Not Set"
        self._type = "Not Set"

    @abstractproperty
    def Id(self) -> str:
        """
        The identifier of the product instance
        """
        NotImplemented

    @abstractproperty
    def Type(self) -> str:
        """
        The type of product
        """
        NotImplemented

    @abstractmethod
    def set_value_date(self, value_date: Date) -> None:
        """
        Set the value date of the contract
        """
        NotImplemented

    @abstractmethod
    def reset(self) -> None:
        """
        Reset any previous index information, will be called before setting the indices
        """
        NotImplemented

    @abstractmethod
    def get_cashflow_currencies(self) -> list[Currency]:
        """
        A list of all possible currencies that cashflows may occur in. This will be used to make
        sure that there are simulators available to convert these to the value currency.
        """
        NotImplemented

    @abstractmethod
    def get_required_indices(self) -> list[MarketObservable]:
        """
        A list of all possible indices that can be required to get the cashflows on the product.
        """
        NotImplemented

    @abstractmethod
    def get_required_index_dates(self, index: MarketObservable) -> list[Date]:
        """
        The dates at which the provided index is required to calculate cashflows. This will be called
        repeatedly so if possible pre-calculate in <set_value_date(Date)>
        """
        NotImplemented

    @abstractmethod
    def get_cashflow_dates(self, currency: Currency) -> list[Date]:
        """
        The dates at which the cashflows in a given currency are likely to take place. It will be used to ensure that
        the numéraire and possible FX rates are available on these dates.
        It will be called once before the product has any MarketObservable set so if the timing of a cashflow depends on
        the realized value of market data a best guess need to be made here.

        :param currency: only return the dates for the cashflows in this provided currency.
        """
        NotImplemented

    @abstractmethod
    def set_index_values(self, index: MarketObservable, index_values: list[float]) -> None:
        """
        Precursor to calling <GetCFs>.
        """
        NotImplemented

    @abstractmethod
    def GetCFs(self) -> list[Cashflow]:
        """
        Call this after having set index values to get all the cashflows on or after the value date.
        """
        NotImplemented

    @abstractmethod
    def get_last_exposure_date(self) -> Date:
        """The last exposure date of the product"""
        NotImplemented
