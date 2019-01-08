import re

OPTION_TYPE_CALL = 1
OPTION_TYPE_PUT = 0


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
            self._strike = value

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        pat = re.compile(value)
        if pat.match(value) is None:
            self._month = None
            self.type = None
        elif pat.match(value) is not None:
            call_arg = ["A","B","C","D","E","F","G","H","I","J","K","L"]
            put_arg = ["M","N","O","P","Q","R","S","T","U","V","W","X"]
            if value in call_arg:
                self._month = call_arg.index(value)+1
                self.type = OPTION_TYPE_CALL
            elif value in put_arg:
                self._month = put_arg.index(value)+1
                self.type = OPTION_TYPE_PUT

    def __init__(self, *args, **kwargs):

        self.base_active, self.strike, self.settlement, self.month, self.year = args

        for k in kwargs.keys():
            if k in self.__dict__:
                self.__setattr__(k, kwargs[k])

        super(Option, self).__init__()

