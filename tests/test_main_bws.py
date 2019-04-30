import unittest
import os


from portfel.bws import load_emitent_data
from portfel.bws import read_file


def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):
    def test_complex(self):
        """
        Complex testing. Removed msut.
        :return:
        """
        dir_path = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        data = load_emitent_data(cls=None, directory=dir_path, ticker="ALRS")

    def test_read_data(self):
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        data = read_file(cls=None, directory=directory, file_name="emitents_29042019")

        print_info(data.values[0])


if __name__ == '__main__':
    unittest.all()

