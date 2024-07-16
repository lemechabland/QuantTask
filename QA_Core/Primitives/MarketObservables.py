from QA_Core.Serialization.Serializable import SerializableViaName
from abc import abstractmethod


class MarketObservable(SerializableViaName):
    """
    Abstract class for MarketObservables.
    All MarketObservables will need to have a unique string value.
    """
    def __init__(self) -> None:
        NotImplemented

    @abstractmethod
    def __str__(self) -> str:
        NotImplemented

    def get_name(self) -> str:
        return self.__str__()

    def equals(self, other) -> bool:
        return self.__str__() == other.__str__()

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__str__())
