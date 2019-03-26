"""
Strategy classes
"""


class StrategyBase(type):
    def __new__(cls, name, bases, attrs):
        _deals = {}
        for key, value in attrs.items():
            if not key.startswith('__'):
                _deals.update({key: value})
        attrs = {"deals": _deals}
        return super().__new__(cls, name, bases, attrs)


class Strategy(metaclass=StrategyBase):
    def __init__(self):
        pass

