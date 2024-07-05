from abc import ABC, abstractmethod, abstractproperty
from QA_Core.Primitives.Currency import Currency
from QA_Core.Conventions.Dates import Date


class Product(ABC):
    def __init__(self):
        self._id = "Not Set"
        self._type = "Not Set"

    @abstractproperty
    def id(self) -> str:
        return self._id

    @abstractproperty
    def type(self) -> str:
        return self._type

    @id.setter
    def id(self, value):
        self._id = value

    @type.setter
    def type(self, value):
        self._type = value

    @abstractmethod
    def set_value_date(self, value_date) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def get_cashflow_currencies(self) -> list:
        pass

    @abstractmethod
    def get_required_indices(self) -> list:
        pass

    @abstractmethod
    def get_required_index_dates(self, date: Date, index) -> list:
        pass

    @abstractmethod
    def get_cashflow_dates(self, currency: Currency) -> list:
        pass

    @abstractmethod
    def set_index_values(self, index, index_values) -> None:
        pass

    @abstractmethod
    def GetCFs(self) -> list:
        pass
