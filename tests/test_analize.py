import unittest


class TestAnalize(unittest.TestCase):
    def test_add_filter_method(self):
        print("*" * 10, "Start analize test", "*" * 10)
        class Analize:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    self.__setattr__(k, v)

            def less_then(self, arg):
                return "im less then"

        analize = Analize()

        self.assertTrue(hasattribute(analize, "less_then")

if __name__ == "__main__":
    unittest.main()


