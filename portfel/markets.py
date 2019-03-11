"""
Main portfell class and additional functionality.

"""

from datetime import datetime


DEAL_POSITION_TYPE_SHORT = 0
DEAL_POSITION_TYPE_LONG = 1


class Strategy:
    def __init__(self, deals, ba=[0, 1]):
        """
        :deals list: list of instances BrokerDeal
        :ba list: list of numbers returned usualy by function range(x, y, step)
        """
        self._deals = deals
        return super(Strategy, self).__init__()

    @property
    def values(self):
        values = []
        # TODO: here will be function for deals execution
        class Temp:
            def all(sub):
                return self._deals
        return Temp()

    @values.setter
    def values(self, *args, **kwargs):
        pass


class BrockerDeal:
    """
    Возращает экземпляр BrockerDeal.
    Он нужен, чтоб интерактивно добавлять/удалять сделки из стека,
    сохраняя при этом саму операцию в экземляре класса.

    Фактически - это просто структура данных для хранения сведений о проведенной(или нет)
    сделки. Класс сдесь нужен, только, для того, чтоб контролировать процесс создания и
    небольшого удобства в визуализации ( типа указывать BUY/SELL при использовании.

    Usage:
    >>> s = 'Si66500BC0'
    >>> opt = fromstring(s)
    >>> bd = BrockerDeal([Option exemplary], 1000, DEAL_POSITION_TYPE_LONG, et=True)

    :param dealunit : exemplary of classes like Option, Future
    :param money : allways POSITIVE number - sum of transaction
    :param dealtype : int number 0 or 1 (sell or buy) or for visualize use "BUY" and "SELL"
    :param dt : date and time of transaction execution
    :param et : True or False - set if transaction was executed or not (et - transaction execution)
    """
    def __init__(self, market_unit, money, deal_type=1, dt=datetime.now(), et=False):
        self.dealunit = market_unit
        self.money = money

        if deal_type == "BUY" or deal_type == 1:
            self.dealtype = DEAL_POSITION_TYPE_LONG
        elif deal_type == "SELL" or deal_type == 0:
            self.dealtype = DEAL_POSITION_TYPE_SHORT
        else:
            raise Exception("Deal type must SELL, PUT, 1 or 0")

        self.dt = dt
        self.et = et

    def get_premy(self):
        # Возвращает сумму премии. Если была покупка опциона - сумма
        # Иначе - положительная.
        if self.dealtype == DEAL_POSITION_TYPE_LONG:
            return self.money * (-1)
        elif self.dealtype == DEAL_POSITION_TYPE_SHORT:
            return self.money

    def execute_deal(self, ba):
        """
        Вычисляет прибыль/убыток по сделке.
        :param ba: цена базового актива текущая (по рынку)
        :return: int прибыль или убыток в результате экспирации опциона
        """
        result = 0
        if self.dealtype ==  DEAL_POSITION_TYPE_SHORT:
            result += (self.dealunit.calculate(ba)*(-1) + self.get_premy())
        elif self.dealtype == DEAL_POSITION_TYPE_LONG:
            result += (self.dealunit.calculate(ba) + self.get_premy())
        return result

