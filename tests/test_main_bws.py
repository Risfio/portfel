import unittest
import os, sys
import pandas as pd

sys.path.append(os.getcwd())
import portfelcfg

from portfel.bws.base import BWSBase
from portfel.bws.base import Calendar


TEST_DIR = os.path.join(portfelcfg.BASE_DIR, "tests", "TEMP")
os.path.isdir(TEST_DIR)

def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):

    def test_change_names(self):
        import re
        pat = re.compile('\[+.+\]')
        data = pd.read_csv(os.path.join(TEST_DIR, "bws.txt"))
        s = data['Name'][0]

        def func(word):
            pat = re.compile('\[+.+\]')
            name = pat.split(word)[0].strip()
            if word.count(name) == 0:
                raise Exception("Troubles construct correct name from string {0}!".format(word))
            return name

        self.assertEqual(u'Сбербанк', func(s))
        self.assertEqual(len(func(s)), 8)

        data['Name'] = data['Name'].map(func)

    def test_select_emitent_data(self):
        dt1 = "29.05.2019"
        dt2 = "30.05.2019"
        data = pd.read_csv(os.path.join(TEST_DIR, "bws.txt"))
        test_isin = "RU0009029540"
        
        day_data = pd.DataFrame(data=data.values, index=data.Date, columns=data.columns)
        day_data = day_data.loc[dt1]

        emitents_data = pd.DataFrame(data=day_data.values, index=day_data.Code, columns=data.columns)
        emitent = emitents_data.loc["SBER"]
        el = float(".".join(emitent.Min.split(',')))
        print_info(el)

    def test_week_data(self):
        date = "29.05.2019"
        class BWS(BWSBase):
            db = os.path.join(TEST_DIR, "bws.txt")

        bws = BWS()
        calendar = Calendar()

        data = bws.week_data(calendar.get_week_dates(date))
        print_info(data.index.unique())


if __name__ == '__main__':
    unittest.all()

