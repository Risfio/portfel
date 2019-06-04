import unittest
from datetime import date

from portfel.bws.base import Calendar


def print_info(s):
    print("*" * 10, "\r\n", s, "\r\n", "*" * 10)


class TestCalendar(unittest.TestCase):
    def test_get_weeks_dates(self):
        s = "07.06.2019"
        etalon_list = ['03.06.2019', '04.06.2019', '05.06.2019', '06.06.2019', '07.06.2019']

        calendar = Calendar()
        self.assertEqual(etalon_list, calendar.get_week_dates(s))


if __name__ == "__main__":
    unittest.all()

