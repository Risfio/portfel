import unittest
import os, sys
import pandas as pd

sys.path.append(os.getcwd())
import portfelcfg

TEST_DIR = os.path.join(portfelcfg.BASE_DIR, "tests", "TEMP")
os.path.isdir(TEST_DIR)

def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):

    def test_change_names(self):
        import re
        pat = re.compile('\[+.+\]')
        data  = pd.read_csv(os.path.join(TEST_DIR, "bws.txt"))
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
        # debug
        print_info(data['Name'][0])


if __name__ == '__main__':
    unittest.all()

