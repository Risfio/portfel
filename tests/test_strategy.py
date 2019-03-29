import unittest
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
            buy_call = BrockerDeal(fromstring(self.str_CALL), 1000)

        print("#" *10, strategy1.values, "#" *10)
        self.assertIsInstance(strategy1.values, DealsSet)


if __name__ == "__main__":
    unittest.main()

