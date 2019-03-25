"""
Получаем массив значений "прибыли" или еще чего.
Данный функционал предназначен для его анализа.

TODO:
    разбивать массив чисел на подмассивы по признакам;
    класс Period с какими-либо св-вами(определю позже);
"""

import numpy as np


PERIOD_TREND_LOWERING = lambda x, y: x > y and True or False
PERIOD_TREND_GROWING = lambda x, y: x < y and True or False
PERIOD_TREND_CONTINUOS = lambda x, y: x == y and True or False


class PeriodsContainer:

    def __init__(self, values):
        self.values = np.array(values)

    def _get_trend(self, arg1, arg2):
        result = None
        for func in [PERIOD_TREND_LOWERING,
                PERIOD_TREND_GROWING,
                PERIOD_TREND_CONTINUOS]:
            if func(arg1, arg2) == True:
                result = func
                break
        return result

    def _get_periods(self):
        periods = []
        period = []
        start_trend = self._get_trend(self.values[0], self.values[1])
        previos_value = 0
        period.append(previos_value)
        for x in range(self.values.size)[1:]:
            if start_trend(self.values[previos_value], self.values[x]) == False:
                period.append(x-1)
                periods.append(period)
                period = [x, ]
                start_trend = self._get_trend(self.values[previos_value], self.values[x])
            elif x == (self.values.size - 1):
                period.append(x)
                periods.append(period)
            previos_value = x
        return periods


class Period(tuple):
    pass

