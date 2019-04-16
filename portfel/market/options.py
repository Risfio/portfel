import re
from datetime import datetime
from math import fabs

OPTION_TYPE_CALL = 1
OPTION_TYPE_PUT = 0


def _fromstring(input_string):
    temp = ""
    result = []

    # Базовый актив. 2 буквы
    ba_reg = re.compile(r'^\w{2,2}')
    result.append(ba_reg.findall(input_string)[0])
    temp = ba_reg.subn("", input_string, 1)[0]

    # Get strike price and deals type(marginal or premial)
    strike_reg = re.compile(r'^\d{2,}')
    result.append(strike_reg.findall(temp)[0])
    temp = strike_reg.subn("", temp, 1)[0]

    # Get type of settlement

    settlement_reg = re.compile(r'^[A|B]{1,1}')
    result.append(settlement_reg.findall(temp)[0])
    temp = settlement_reg.subn('', temp, 1)[0]

    # Get month and option type(CALL or PUT)
    # От A до L включительно - для опционов CALL
    # Соответственно от M до X - для опционов PUT
    month_reg = re.compile(r'^[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X]{1,1}')
    result.append(month_reg.findall(temp)[0])
    temp = month_reg.subn('', temp, 1)[0]

    # Get year

    result.append(temp)

    return result


def fromstring(input_string):
    """
    Creating Option class examplary from string.
    :param input_string: specionaly formated string
    :return: Option class exemplary or None
    """

    params = _fromstring(input_string)

    return Option(*params)


class OptionOld:
    def __init__(self, strike, premium, type):
        self._strike = strike
        self._premium = premium
        self._type = type

    def _buy_call_revenue(self, ba):
        result = None
        if self._strike >= ba:
            result = 0
        elif self._strike < ba:
            result = ba - self._strike
        return result

    def _buy_call_balance(self, ba):
        return self._buy_call_revenue(ba) - self._premium

    def _buy_put_revenue(self, ba):
        result = None
        if self._strike <= ba:
            result = 0
        elif self._strike > ba:
            result = self._strike - ba
        return result

    def _buy_put_balance(self, ba):
        return self._buy_put_revenue(ba) - self._premium

    def _sell_call_revenue(self, ba):
        result = None
        if self._strike >= ba:
            return 0
        elif self._strike < ba:
            result = self._strike - ba
        return result

    def _sell_call_balance(self, ba):
        return self._premium + self._sell_call_revenue(ba)

    def _sell_put_revenue(self, ba):
        result = None
        if self._strike <= ba:
            return 0
        elif self._strike > ba:
            result = ba - self._strike
        return result

    def _sell_put_balance(self, ba):
        return self._premium + self._sell_put_revenue(ba)

    def get_revenue(self, ba):
        result = None
        if self._type == 'BUY_CALL':
            result = self._buy_call_revenue(ba)
        elif self._type == 'BUY_PUT':
            result = self._buy_put_revenue(ba)
        elif self._type == 'SELL_CALL':
            result = self._sell_call_revenue(ba)
        elif self._type == 'SELL_PUT':
            result = self._sell_put_revenue(ba)
        return result

    def get_balance_revenue(self, ba):
        result = None
        if self._type == 'BUY_CALL':
            result = self._buy_call_balance(ba)
        elif self._type == 'BUY_PUT':
            result = self._buy_put_balance(ba)
        elif self._type == 'SELL_CALL':
            result = self._sell_call_balance(ba)
        elif self._type == 'SELL_PUT':
            result = self._sell_put_balance(ba)
        return result


class Option:

    @property
    def base_active(self):
        return self._base_active

    @base_active.setter
    def base_active(self, value):
        # Verification here
        pat = re.compile(r"[a-zA-Z]{2,2}")
        # If verify value - set base_active equal to value
        if pat.match(value) is None:
            self._base_active = None
        elif pat.match(value) is not None:
            self._base_active = value

    @property
    def strike(self):
        return self._strike

    @strike.setter
    def strike(self, value):
        pat = re.compile(r'\d{2,}')
        if pat.match(value) is None:
            self._strike = None
        elif pat.match(value) is not None:
            self._strike = int(value)

    @property
    def settlement(self):
        return self._settlement

    @settlement.setter
    def settlement(self, value):
        pat = re.compile(r'[A|B]{1,1}')
        if pat.match(value) is None:
            self._settlement = None
        elif pat.match(value) is not None:
            self._settlement = value

    @property
    def otype(self):
        return self._type

    @otype.setter
    def otype(self, value):
        self._type = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        pat = re.compile(value)
        if pat.match(value) is None:
            self._month = None
            self.otype = None
        elif pat.match(value) is not None:
            call_arg = ["A","B","C","D","E","F","G","H","I","J","K","L"]
            put_arg = ["M","N","O","P","Q","R","S","T","U","V","W","X"]
            if value in call_arg:
                self._month = call_arg.index(value)+1
                self.otype = OPTION_TYPE_CALL
            elif value in put_arg:
                self._month = put_arg.index(value)+1
                self.otype = OPTION_TYPE_PUT

    def __init__(self, *args, **kwargs):

        self.base_active, self.strike, self.settlement, self.month, self.year = args

        for k in kwargs.keys():
            if k in self.__dict__:
                self.__setattr__(k, kwargs[k])

        super(Option, self).__init__()

    def __str__(self):
        base_active = "".join(["Базовый актив:", self.base_active])
        strike = "".join(["Цена исполнения (страйк)", str(self.strike)])
        # Код опциона
        # А - американский на фьючерс с уплатой премии
        # В - американский на фьючерс маржируемый (обычно для мосбиржи)
        temp = ""
        if self.settlement == "A":
            temp = "Американский с уплатой премии"
        elif self.settlement == "B":
            temp = "Американский маржируемый"
        settlement = "".join(["Тип рассчетов :", temp])
        month = "".join(["Месяц :", ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
                 "ноябрь", "декабрь"][self.month-1]])
        temp = ""
        if self.otype == OPTION_TYPE_PUT:
            temp = "PUT"
        elif self.otype == OPTION_TYPE_CALL:
            temp = "CALL"
        otype = "".join(["Тип опциона:", temp])

        dt = datetime.now().year
        if self.year == 0:
            dt = "2020"
        year = "".join(["Год :", str(dt)])
        return "\r\n".join([base_active, strike, settlement, month, otype, year])

    def _inmoney(self, ba):
        result = False
        if self.otype == OPTION_TYPE_PUT:
            if self.strike > ba:
                result = True
        elif self.otype == OPTION_TYPE_CALL:
            if self.strike < ba:
                result = True
        return result

    def calculate(self, ba):
        result = 0
        if self._inmoney(ba):
            result = int(fabs(self.strike - ba))
        return result

  















