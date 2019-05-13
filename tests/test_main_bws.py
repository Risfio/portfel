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

    def test_fileload(self):
        columns = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019.txt"
        quik = FileLoaderQUIK(directory=directory, file_name="emitents_08052019", names=columns)
        data = quik.read_data()

    def test_wrong_num_columns(self):
        columns = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019.txt"
        quik = FileLoaderQUIK(directory=directory, file_name="emitents_08052019")
        data = quik.read_data()
        # Test columns names espetional for QUIK file loader
        self.assertEqual(columns, tuple(data.columns.tolist()))

    def test_change_names(self):
        import re
        pat = re.compile('\[+.+\]')
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019"
        quik = FileLoaderQUIK(directory=directory, file_name=file_name)
        data  = quik.read_data()
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
        print_info(data.values[0])


if __name__ == '__main__':
    unittest.all()

