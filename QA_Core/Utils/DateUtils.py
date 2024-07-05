from enum import Enum


class DayOfWeek(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class IllegalMonthError(ValueError):
    def __init__(self, month):
        self.month = month

    def __str__(self):
        return "bad month number %r; must be 1-12" % self.month


def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def monthrange(year, month):
    # Number of days per month (except for February in leap years)
    _mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= month <= 12:
        raise IllegalMonthError(month)
    n_days = _mdays[month] + (month == Month.February.value and isleap(year))
    return n_days
