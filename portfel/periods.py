"""
Получаем массив значений "прибыли" или еще чего.
Данный функционал предназначен для его анализа.

TODO:
    разбивать массив чисел на подмассивы по признакам;
    класс Period с какими-либо св-вами(определю позже);
"""

import numpy as np


PERIOD_TREND_LOWERING = lambda x: x > 0 and True or False
PERIOD_TREND_GROWING = lambda x: x < 0 and True or False
PERIOD_TREND_CONTINUOS = lambda x: x == 0 and True or False


class PeriodsContainer:

    def __init__(self, values):
        self.values = np.array(values)

    def _get_periods(self):
        # Все значения сдвигаем в положительную зону на асолютную величину
        # минимального значения. Например [-1, 0, 1] будет [0,1,2]
        _shift_value = np.abs(self.values.min())
        _values = (for x in np.nditer(self.values, op_flags=["readwrite"]) and x += _shift_value)


class Period(tuple):
    pass

