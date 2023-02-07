from bookkeeping.application.db.people import *
from bookkeeping.application.salary import *
from _datetime import date


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(date.today())

