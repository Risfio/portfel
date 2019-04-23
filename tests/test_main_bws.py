import unittest
import os

from portfel.bws import BWS
from portfel.bws import FileLoader

class TestBWS(unittest.TestCase):
    def test_fileloader(self):
        floader = FileLoader('/c/SHIT')


if __name__ == '__main__':
    unittest.all()


