import unittest
from portfel.markets import Strategy, BrockerDeal
from portfel.options import fromstring
from portfel.periods import Period

import numpy as np


class TestNumpyForPeriods(unittest.TestCase):
    values = [-1, -1, -1,
              -0.75, -0.5, -0.25,
              0,
              0.25, 0.50, 0.75,
              1, 1, 1,
              0.75, 0.5, 0.25,
              0,
              -0.25, -0.5, -0.75,
              -1, -1, -1]
    
    def test_numpy(self):
        pass


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

