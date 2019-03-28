"""
Strategy classes
"""


class StrategyBase(type):
    def __new__(cls, name, bases, attrs):

        _deals = {}

        new_attrs = {}

        if "range" not in attrs.keys():
            new_attrs.update({'range': []})
        else:
            new_attrs.update({'range': attrs.pop("range")})

        if "step" not in attrs.keys():
            new_attrs.update({"step": 0})
        else:
            new_attrs.update({'step': attrs.pop("step")})

        for key, value in attrs.items():
            if not key.startswith('__'):
                _deals.update({key: value})
        new_attrs.update({"deals": _deals})

        new_cls = super().__new__(cls, name, bases, new_attrs)

        # debug
        print(new_attrs)

        return new_cls


class Strategy(metaclass=StrategyBase):
    pass

