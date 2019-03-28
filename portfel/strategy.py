"""
Strategy classes
"""


class StrategyBase(type):
    def __new__(cls, name, bases, attrs):
        _deals = {}

        new_attrs = {}

        if "range" not in attrs.keys():
            raise Exception("[range] attribute must be setted")
        else:
            new_attrs.update({'range': attrs.pop("range")})

        if "step" not in attrs.keys():
            raise Exception("[step] value must be setted in Strategy declaration")
        else:
            new_attrs.update({'step': attrs.pop("step")})

        for key, value in attrs.items():
            if not key.startswith('__'):
                _deals.update({key: value})
        attrs = {"deals": _deals}
        return super().__new__(cls, name, bases, attrs)


class Strategy(metaclass=StrategyBase):
    def __init__(self):
        pass

