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
        # print this
        an.less_then(0)
        # or above
        # print("*" * 10, "\r\n", an.less_then(0), "\r\n", "*" * 10)

    def test_strategy_analize(self):
        class strategy(Strategy):
            range = (62000, 72000)
            step = 250
            buy_call = BrockerDeal(fromstring("Si65000BC0"), 1000)

        class analize(Analize):
            def less_then(self, arg, analized_item, lbl="less then %VAL%", msg="Here description"):
                revenues = analized_item.values.all()
                num_losses = len([x for x in revenues['revenues'] if x < arg])
                result = num_losses/revenues['revenues'].size
                return super(analize, self).less_then(result, analized_item, lbl, msg)

        an = analize(data = [strategy])
        print("Result of strategy analize:\r\n", an.get(less_then = 0))


if __name__ == "__main__":
    unittest.main()


