import unittest

from portfel.market.markets import BrockerDeal
from portfel.market.options import fromstring


class TestPortfel(unittest.TestMain):
    """
    Тестируем создание стратегии и фильтр от начала и до конца.
    """
    class strategy1(Strategy):
        # шаг цены опциона
        step = 250
        # диапазон страйков
        range = (62000, 68000)

        # покупка опциона CALL вне денег
        buy_call = BrockerDeal(fromstring("Si64500FC0"), 209, dt=1, et=True)


if __name__ == '__main__':
    unittest.all()


