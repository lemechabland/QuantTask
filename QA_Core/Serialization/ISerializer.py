from abc import ABC, abstractmethod


class ISerializer(ABC):
    """
    <summary>
    Will ensure the uniqueness of objects.
    </summary>
    """
    def __init__(self) -> None:
        NotImplemented

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the name with which the object should be serialized.
        """
        NotImplemented
