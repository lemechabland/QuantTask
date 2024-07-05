# Creating an object `Dates` representation for QALib
from QA_Core.Utils.DateUtils import *
from QA_Core.Utils.Exceptions import *


class Date:

    def __init__(self, year, month, day):
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            if year >= 1899 and month in range(1, 13) and day in range(1, monthrange(year, month)+1):  # starting
                # point of the year: 1899
                self.year = year
                self.month = month
                self.day = day
            else:
                raise InvalidDateRepresentation(f"Date({year}, {month}, {day}) cannot be constructed.")
        else:
            raise InvalidDateRepresentation("Integers needed for inputs.")

    @classmethod
    def from_string(cls, date_string: str) -> object:
        # Construct a date from a string in ISO8601 format `yyyy-mm-dd`
        string_components = date_string.split("-")
        convert_components = list(map(int, string_components))
        return cls(convert_components[0], convert_components[1], convert_components[2])

    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        comparison_res = False
        if self.year > other.year:
            comparison_res = True
        if self.year == other.year and self.month > other.month:
            comparison_res = True
        if self.year == other.year and self.month == other.month and self.day > other.day:
            comparison_res = True
        return comparison_res

    def __lt__(self, other) -> bool:
        comparison_res = False
        if self.year < other.year:
            comparison_res = True
        if self.year == other.year and self.month < other.month:
            comparison_res = True
        if self.year == other.year and self.month == other.month and self.day < other.day:
            comparison_res = True
        return comparison_res


