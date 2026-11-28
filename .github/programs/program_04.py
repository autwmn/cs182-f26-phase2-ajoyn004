# input: ints
import datetime
import sys


def is_leap(year):
    if year % 100 == 0:
        return year % 4 == 0
    return year % 4 == 0


def days_in_month(year, month):
    if month == 2:
        if is_leap(year):
            return 29
        return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


def days_left(year, month, day):
    end = datetime.date(year, month, days_in_month(year, month))
    return (end - datetime.date(year, month, day)).days


def main(argv):
    xs = [int(a) for a in argv[1:]]
    if len(xs) != 3:
        return -1
    year, month, day = xs
    if year < 1 or year > 9999:
        return -2
    if month < 1 or month > 12:
        return -3
    if day < 1 or day > days_in_month(year, month):
        return -4
    return days_left(year, month, day)


if __name__ == "__main__":
    main(sys.argv)
