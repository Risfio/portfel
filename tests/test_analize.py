import unittest
from portfel.analize import Analize


class TestAnalize(unittest.TestCase):
    def test_add_filter_method(self):
        print("*" * 10, "Start analize test", "*" * 10)
        class analize(Analize):
            def less_then(self, arg, msg):
                return super(analize, self).less_then(arg, msg)

        an = analize()
        print("*" * 10, an.less_then(0, "on duty"), "*" * 10)


if __name__ == "__main__":
    unittest.main()


