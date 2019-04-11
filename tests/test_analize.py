import unittest
from portfel.analize import Analize


class TestAnalize(unittest.TestCase):
    def test_add_filter_method(self):
        print("*" * 10, "Start analize test", "*" * 10)
        class analize(Analize):
            pass

if __name__ == "__main__":
    unittest.main()


