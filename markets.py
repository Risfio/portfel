"""
Main portfell class and additional functionality.

TODO:

1)Add deals property to MarketBase class.
It must have method add.
2)Добавить функционал для рассчета баланса

"""

from datetime import datetime

from .options import Option, OPTION_TYPE_CALL, OPTION_TYPE_PUT

DEAL_POSITION_TYPE_SHORT = 0
DEAL_POSITION_TYPE_LONG = 1


class MarketBase:
    """
    Это метакласс, а может и нет !!??
    Использовать примерно так :
    >>> class Market(MarketFORTS):
    >>>     deals = [
    >>>     {unit:[option class exemplary]; money:1000; deal_type:"SELL"; dt:"12.12.2018:19:45"; et=False},
    >>>     [[option class exemplary], 1000, "SELL", "12.12.2018:19:45", False],
    >>>     #here can be futures exemplary
    >>>     ]
    >>>
    >>> market = Market()

    @:param name: str название для портфеля на случай , если будем в БД сохранять
    """
    def __init__(self, name):
        self.name = name


class MarketFORTS(MarketBase):

    def __init__(self, name):
        self.limitations = LimitationsOnClientAccountsBase()
        self.positions = PositionsOnClientAccountsBase()
        return super(MarketFORTS, self).__init__(name)

    def clearing(self):
        for deal in self.deals:
            pass

    def expiration(self):
        """
        Эмулирует результаты экспирации. Т.е. обращает опционы в фьючерсы. Высчитывает ГО.
        Вообщем полная эмуляция экспирации.
        :return:
        """
        pass


class MarketTradeReglaments:
    """
    Устанавливает порядок вычисления LimitationsOnClientAccounts и PositionsOnClientsAccounts по таймфрейму.
    """
    pass


class LimitationsOnClientAccountsBase:
    """
    Класс отражающий таблицу QUIK - ограничения по клиентским счетам/
    Отражает состояние счетов на текущую сессию между клирингами.

    :param LimitOfOpenPositions : 	Лимит открытых позиций - денежные ср-ва трейдера на
                                    срочном рынке (текущие лимиты открытых  позиций в денежном выражении);
    :param CurrentNetPosition : 	Текущая чистая позиция - денежные ср-ва трейдера , зарезервированные под
                                    гарантийное обеспечение по всем позициям трейдера на срочном рынке и на
                                    отрицательную вариационную маржу(при ее наличии);
    :param VariationMargin : 	Вариационная маржа - показывает значение вариационной маржи по всем позициям
                                трейдера по текущей торговой сессии;
    :param AccruedIncome : 	Накопленный доход - показывает значение денежных ср-в, которые трейдер заработал
                            донаступления клиринга;
    :param ExchangeFee : Биржевые сборы - отображает биржевые комиссионные сборы по всем сделкам клиента за
                        текущую торговую сессию.
    :return
    """
    pass


class PositionsOnClientAccountsBase:
    """
    Класс отражающий таблицу QUIK - позиции по клиентским счетам.
    Отражает состояние  клиентскиъ счетов после клиринга и соответственно экспирации.

    :param  ShortName: Краткое название - краткий код торгового инструмента;
    :param  IncomingLongPosition: Входящая длинная позиция - кол-во контрактов в длинных позициях по
                                    торговому инструменту срочного рынка на начало торгов;
    :param  IncomingShortPosition: Входящая короткая позиция - кол-во контрактов в коротких позициях
                                    по торговому инструменту срочного рынка на начало торгов
    :param  CurrentLongPosition: Текущая длинная позиция - количество текущих длинных позиций по торговому инструменту;
    :param  CurrentShortPosition: Текущая короткая позиция - количество текущих коротких позиций по
                                торговому инструменту;
    :param  VariationMargin: Вариационная маржа - текущая вариационная маржа по каждому инструменту;

    :return
    """
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
        Это НЕ ОБЩИЙ МЕТОД ДЛЯ ВСЕХ РЫНКОВ! ЭТО КОНКРЕТНО ДЛЯ ФОРТСА!
        Проводит операции над родительским объектом - MarketFORTS. Конкретно - изменяет показатели его
        полей limitations и posittions.
        :param ba:
        :return: int прибыль или убыток в результате экспирации опциона
        """
        result = 0
        result += (self.dealunit.calculate() + self.get_premy())
        return result

