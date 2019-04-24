import unittest
import os

from portfel.bws import BWS
from portfel.bws import FileLoader


def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):
    def test_fileloader(self):
        floader = FileLoader(path=os.path.join(os.path.expanduser('~'), 'documents', 'projects', 'BWS', 'tests', 'TEMP'))
        self.assertTrue(os.path.isdir(floader.base_dirs[0]))
        print_info(os.path.isfile(floader._construct_file_path('ALRS', floader.base_dirs[0], ext=".txt")))        


if __name__ == '__main__':
    unittest.all()


