import unittest

import numpy as np
from pandas import DataFrame

from portfel.strategy import Strategy, DealsSet
from portfel.markets import BrockerDeal
from portfel.options import fromstring


class TestBases(unittest.TestCase):
    str_CALL = "Si65000BC0"
    str_PUT = "Si65000BO0"

    def test_strategy_meta(self):
        class strategy1(Strategy):
            range = (62000, 72000)
            buy_call = BrockerDeal(fromstring(self.str_CALL), 1000)

        class strategy2(Strategy):
            range = (62000, 72000)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 1000, 0)

        # debug
        print("*"*10, "Test strategy start", "*"*10)

    def test_values(self):
        class strategy1(Strategy):
            range = (62000, 72000)
            buy_call = BrockerDeal(fromstring(self.str_CALL), 500)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 1000, 0)

        revenue = []
        ba_range = []
        for ba in range(strategy1.range[0], strategy1.range[1], 250):
            ba_range.append(ba)
            rev = 0
            for name, deal in strategy1.values._deals.items():
                rev += deal.execute_deal(ba)
            revenue.append(rev)

        df = DataFrame(data={'revenue': revenue, 'base active': ba_range})
        print("#" *10, df, "#" *10)
        self.assertIsInstance(strategy1.values, DealsSet)


if __name__ == "__main__":
    unittest.main()

