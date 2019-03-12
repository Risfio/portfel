"""
Получаем массив значений "прибыли" или еще чего.
Данный функционал предназначен для его анализа.

TODO:
    разбивать массив чисел на подмассивы по признакам;
    класс Period с какими-либо св-вами(определю позже);
"""


PERIOD_TREND_LOWERING = lambda x: x > 0 and True or False
PERIOD_TREND_GROWING = lambda x: x < 0 and True or False
PERIOD_TREND_CONTINUOS = lambda x: x == 0 and True or False


class PeriodsContainer:
    def _get_trend_start(self, arg1, arg2):
        """
        Получаем направление тренда по двум значениям
        :param arg1:
        :param arg2:
        :return: одну из трех констант TREND
        """
        result = False
        trend = (arg1/arg2) - 1
        for func in [PERIOD_TREND_LOWERING,
                     PERIOD_TREND_GROWING,
                     PERIOD_TREND_CONTINUOS]:
            if func(trend) == True:
                result = func
        return result


class Period(tuple):
    pass

