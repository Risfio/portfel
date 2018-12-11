"""
Main portfell class and additional functionality.
"""

from datetime import datetime


class MarketBase:
    """
    Это метакласс, а может и нет !!??
    Использовать примерно так :
    >>> class Market(MarketFORTSBase):
    >>>     deals = [
    >>>     {unit:[option class exemplary]; money:1000; deal_type:"SELL"; dt:"12.12.2018:19:45"; et=False},
    >>>     [[option class exemplary], 1000, "SELL", "12.12.2018:19:45", False],
    >>>     #here can be futures exemplary
    >>>     ]
    >>>
    >>> market = Market()
    """
    def __init__(self):
        pass


class LimitationsOnClientAccounts:
    pass


class PositionsOnClientAccounts:
    pass


class BrockerDeal:
    """
    Возращает экземпляр BrockerDeal.
    Он нужен, чтоб интерактивно добавлять/удалять сделки из стека,
    сохраняя при этом саму операцию в экземляре класса.

    Фактически - это просто структура данных для хранения сведений о проведенной(или нет)
    сделки. Класс сдесь нужен, только, для того, чтоб контролировать процесс создания и
    небольшого удобства в визуализации ( типа указывать BUY/SELL при использовании.

    :param unit : exemplary of classes like Option, Future
    :param money : allways POSITIVE number - sum of transaction
    :param type : int number 0 or 1 (sell or buy) or for visualize use "BUY" and "SELL"
    :param dt : date and time of transaction execution
    :param et : True or False - set if transaction was executed or not
    """
    def __init__(self, market_unit, money, deal_type=1, dt=datetime.now(), et=False):
        self._unit = market_unit
        self._money = money

        if deal_type == "BUY":
            self._type = 1
        elif deal_type == "SELL":
            self._type = 0
        else:
            self._type = deal_type

        self._dt = dt
        self._et = et

