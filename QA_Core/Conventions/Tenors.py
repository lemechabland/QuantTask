from QA_Core.Utils.Exceptions import InvalidTenorRepresentation


class Tenor:
    """
    Tenor refers to the length of time until the maturity of a financial instrument.
    Will represent tenor from a string: e.g.: `1Y`, `3M`, `3Y3M`
    The string must be in decreasing order of tenor types: e.g.: `3Y3M` is OK but `2D1Y` is not OK
    """

    def __init__(self, tenor_str: str) -> None:
        self._tenor = tenor_str
        try:
            self._days, self._weeks, self._months, self._years = 0, 0, 0, 0
            parts = self._tenor.split('Y')
            if len(parts) > 1:
                self._years = int(parts[0])
                self._tenor = parts[1]
            parts = self._tenor.split('M')
            if len(parts) > 1:
                self._months = int(parts[0])
                self._tenor = parts[1]
            parts = self._tenor.split('W')
            if len(parts) > 1:
                self._weeks = int(parts[0])
                self._tenor = parts[1]
            parts = self._tenor.split('D')
            if len(parts) > 1:
                self._days = int(parts[0])
        except ValueError:
            raise InvalidTenorRepresentation(f"{tenor_str} is not OK.")

    @property
    def Days(self) -> int:
        return self._days

    @property
    def Weeks(self) -> int:
        return self._weeks

    @property
    def Months(self) -> int:
        return self._months

    @property
    def Years(self) -> int:
        return self._years

    @classmethod
    def tenor(cls, days: int, weeks: int, months: int, years: int) -> object:
        tenorStr = str(years) + "Y" + str(months) + "M" + str(weeks) + "W" + str(days) + "D"
        return cls(tenorStr)

    @staticmethod
    def from_years(years: int) -> object:
        return Tenor.tenor(0, 0, 0, years)

    @staticmethod
    def from_months(months: int) -> object:
        return Tenor.tenor(0, 0, months, 0)

    @staticmethod
    def from_weeks(weeks: int) -> object:
        return Tenor.tenor(0, weeks, 0, 0)

    @staticmethod
    def from_days(days: int) -> object:
        return Tenor.tenor(days, 0, 0, 0)

    def __str__(self):
        stringBuilder = ""
        if self._years > 0:
            stringBuilder += str(self._years) + "Y"
        if self._months > 0:
            stringBuilder += str(self._months) + "M"
        if self._weeks > 0:
            stringBuilder += str(self._weeks) + "W"
        if self._days > 0:
            stringBuilder += str(self._days) + "D"
        return stringBuilder

    def __eq__(self, other) -> bool:
        return (self._days + 7 * self._weeks == other._days + 7 * other._weeks and
                self._months + 12 * self._years == other._months + 12 * other._years)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self):
        """ 1 month is alias as 31 days"""
        return self._days + 7 * self._weeks + (self._months + 12 * self._years) * 31
