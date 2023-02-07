from bookkeeping.application.db import people
from bookkeeping.application import salary
from _datetime import date


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    print(date.today())

