from application import salary
from application.db import people
import dirty_main as dm
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    salary.calculate_salary()
    people.get_employees()
    dm.print_one()
    dm.print_two()