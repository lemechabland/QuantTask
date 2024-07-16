from QA_Core.Serialization.Serializable import SerializableViaName


class Currency(SerializableViaName):
    def __init__(self, code: str) -> None:
        self._code = code.upper()

    def get_name(self) -> str:
        return self._code

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return self._code

    def __hash__(self) -> int:
        return hash(self.__str__())
