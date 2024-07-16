from abc import abstractmethod
from QA_Core.Serialization.ISerializer import ISerializer


class SerializableViaName(ISerializer):
    """
    Objects get serialized via their name.
    """

    def __init__(self):
        NotImplemented

    def equals(self, other) -> bool:
        if self is other:
            return True
        if not type(self) == type(other):
            return False
        return self.get_name() == other.get_name()

    @abstractmethod
    def get_name(self) -> str:
        pass
