"""
Получаем массив значений "прибыли" или еще чего.
Данный функционал предназначен для его анализа.

TODO:
    разбивать массив чисел на подмассивы по признакам;
    класс Period с какими-либо св-вами(определю позже);
"""

import numpy as np


PERIOD_TREND_LOWERING = lambda x: x > 1 and True or False
PERIOD_TREND_GROWING = lambda x: x < 1 and True or False
PERIOD_TREND_CONTINUOS = lambda x: x == 1 and True or False


class PeriodsContainer:

    def __init__(self, values):
        self.values = np.array(values)

    def _get_trend(self, arg):
        result = False
        for func in [PERIOD_TREND_CONTINUOS,
                     PERIOD_TREND_GROWING,
                     PERIOD_TREND_LOWERING]:
            if func(arg) == True:
                result = func
        return result

    def _get_periods(self):
        n = 0
        periods = []
        while n < (self.values.size -1):
            period = [n, ]
            trend = True
            trend_func = None
            try:
                trend_func = self._get_trend(self.values[n]/self.values[n+1])
            except Exception as e:
                trend_func = self._get_trend(self.values[n])
            while n < (self.values.size -1) and trend == True:
                try:
                    n += 1
                    trend = trend_func(self.values[n]/self.values[n+1])
                except IndexError as e:
                    pass
                except Exception as e:
                    trend = trend_func(self.value[n])
            period.append(n)
            periods.append(period)
        # debug
        print(periods)
        return periods


class Period(tuple):
    pass

