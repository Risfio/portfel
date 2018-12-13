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
