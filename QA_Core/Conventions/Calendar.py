from abc import ABC, abstractmethod, abstractproperty


class AbstractCalendar(ABC):
    def __init__(self, calendar_name: str):
        self.calendar_name = calendar_name

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def is_business_day(self) -> bool:
        pass

    @abstractmethod
    def is_weekend(self, day_of_week: int) -> bool:
        pass

    _added_holidays = list()
    _removed_holidays = list()


# <summary>
# This class provides methods for determining whether a date is a
# business day or a holiday for a given market.
# </summary>

class Calendar(AbstractCalendar):
    def __init__(self, calendar_name: str):
        super().__init__(calendar_name)

    @property
    def name(self):
        return self.calendar_name

    def is_business_day(self, date) -> bool:
        pass

    def is_holiday(self, date) -> bool:
        return not self.is_business_day(date)

    def is_weekend(self, day_of_week) -> bool:
        pass

    def added_holidays(self):
        return self._added_holidays

    def removed_holidays(self):
        return self._removed_holidays
