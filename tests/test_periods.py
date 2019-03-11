import unittest
from portfel.markets import Strategy, BrockerDeal
from portfel.options import fromstring


class TestPeriodsMainFunc(unittest.TestCase):
    pass


class TestStrategyUsage(unittest.TestCase):
    def _get_deals_list(self):
        s = "Si65000BC0"
        opt = fromstring(s)
        s1 = "Si65000BO0"
        opt1 = fromstring(s1)

        deals = [
            BrockerDeal(opt, 1000),
            BrockerDeal(opt, 1000, 0),
            BrockerDeal(opt1, 1000),
            BrockerDeal(opt1, 1000, 0)
        ]
        return deals

    def test_strategy_init(self):
        strat = Strategy(self._get_deals_list())
        self.assertEqual(type(strat.values.all()), list)


if __name__ == '__main__':
    unittest.main()

