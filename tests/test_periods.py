import unittest
from portfel.markets import BrockerDeal
from portfel.options import fromstring
from portfel.periods import PeriodsContainer

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
        ndarr = np.array(self.values)
        self.assertEqual(ndarr[1], -1.0)
        self.assertEqual(ndarr[1], -1)

    def test_periods_container(self):
        pcont = PeriodsContainer(self.values)
        periods = pcont._get_periods()
        print(periods)

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


if __name__ == '__main__':
    unittest.main()

