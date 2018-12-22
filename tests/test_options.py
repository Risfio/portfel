import unittest

from options import fromstring

class TestOptionClass(unittest.TestCase):
    option_string = 'Si66500BC0'
    opt = fromstring(option_string)


if __name__ == '__main__':
    unittest.main()