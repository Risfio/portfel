import unittest

import numpy as np
from pandas import DataFrame

from portfel.market.strategy import Strategy, DealSet
from portfel.market.markets import BrockerDeal
from portfel.market.options import fromstring


class TestBases(unittest.TestCase):
    str_CALL = "Si65000BC0"
    str_PUT = "Si65000BO0"

    def test_strategy_meta(self):
        class strategy1(Strategy):
            range = (62000, 72000)
            step = 250
            buy_call = BrockerDeal(fromstring(self.str_CALL), 1000)

        class strategy2(Strategy):
            range = (62000, 72000)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 1000, 0)

    def test_strategy_option_et_param(self):
        class strategy1(Strategy):
            step = 250
            range = (62000, 68000)
            buy_call = BrockerDeal(fromstring(self.str_CALL), 200, deal_type=1, et=True)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 200, deal_type=0, et=True)

        self.assertEqual(strategy1.values.all().values[20], 0)

        class strategy2(Strategy):
            step = 250
            range = (62000, 68000)
            buy_call = BrockerDeal(fromstring(self.str_CALL), 200, deal_type=1, et=True)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 200, deal_type=0, et=False)

        self.assertEqual(strategy2.values.all().values[20], 1800)

    def test_values(self):
        # test strategy values property with 2 and more deals
        class strategy1(Strategy):
            range = (62000, 72000)
            step = 250
            buy_call = BrockerDeal(fromstring(self.str_CALL), 500)
            sell_call = BrockerDeal(fromstring(self.str_CALL), 1000, 0)

        self.assertIsInstance(strategy1.values, DealSet)
        self.assertEqual(strategy1.values.all().size, 40)
        self.assertIsInstance(strategy1.values._source_data, DataFrame)


if __name__ == "__main__":
    unittest.main()

