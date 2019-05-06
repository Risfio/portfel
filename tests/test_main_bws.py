import unittest
import os
import pandas as pd

from portfel.bws import FileLoaderQUIK


def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):
    def test_complex(self):
        """
        Complex testing. Removed msut.
        :return:
        """
        dir_path = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")

    def test_read_data(self):
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")

        quik = FileLoaderQUIK()
        quik.directory = directory
        data = quik.read_data("emitents")
        print_info(data['Дата торгов'])


if __name__ == '__main__':
    unittest.all()

