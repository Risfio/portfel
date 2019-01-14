"""
Main portfell class and additional functionality.

TODO:
Add deals property to MarketBase class.
It must have method add.
"""

from datetime import datetime


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


    def calculate_deals(self):
        """
        Собственно просчитываем все сделки в поле deals.
        Этот метод прописывается для каждого вида рынка отдельно. Для
        ФОРТСА свой, для ММВБ свой
        :return: None (что возвращать пока не знаю)
        """
        pass


class MarketFORTS(MarketBase):
    def calculate_deals(self):
        """
        Вызов метода для вычисления значений для рынка ФОРТС.
        :return:
        """
        return None


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

    :param dealunit : exemplary of classes like Option, Future
    :param money : allways POSITIVE number - sum of transaction
    :param dealtype : int number 0 or 1 (sell or buy) or for visualize use "BUY" and "SELL"
    :param dt : date and time of transaction execution
    :param et : True or False - set if transaction was executed or not (et - transaction execution)
    """
    def __init__(self, market_unit, money, deal_type=1, dt=datetime.now(), et=False):
        self.dealunit = market_unit
        self.money = money

        if deal_type == "BUY":
            self.dealtype = 1
        elif deal_type == "SELL":
            self.dealtype = 0
        else:
            self.dealtype = deal_type

        self.dt = dt
        self.et = et

