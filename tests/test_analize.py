import unittest
from portfel.analize import Analize
from portfel.markets import BrockerDeal
from portfel.options import fromstring

from portfel.strategy import Strategy

class TestAnalize(unittest.TestCase):

    def test_add_filter_method(self):
        # Переопределение матода less_then и есть то, что анализирует данная
        # функция
        class analize(Analize):
            def less_then(self, arg, lbl="less then %VAL%", msg="Here description"):
                return super(analize, self).less_then(arg, lbl, msg)

        an = analize()
        print("*" * 10, "\r\n", an.less_then(0), "\r\n", "*" * 10)

    def test_strategy_analize(self):
        class strategy(Strategy):
            range = (62000, 72000)
            step = 250
            buy_call = BrockerDeal(fromstring(self.str_CALL), 1000)

        class analize(Analize):
            def less_then(self, arg, lbl="less then %VAL%", msg="Here description"):
                revenues = self._items.values.all()
                num_losses = len(for x in revenues['revenues'] if x < arg)
                result = num_losses/revenues.size
                return result

        an = analize(strategy)
        print("Result of strategy analize:\r\n", an.get(less_then = 0))


if __name__ == "__main__":
    unittest.main()


