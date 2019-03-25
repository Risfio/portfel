import unittest
from portfel.strategy import StrategyBase
from portfel.markets import BrockerDeal
from portfel.options import fromstring


class TestBases(unittest.TestCase):
    str_CALL = "Si65000BC0"
    str_PUT = "Si65000BO0"

    def test_strategy_meta(self):
        class Strategy(StrategyBase):
            sell_call = BrockerDeal(fromstring(self.str_CALL), 1000)
        # debug
        print("Test strategy mera start")


if __name__ == "__main__":
    unittest.main()

