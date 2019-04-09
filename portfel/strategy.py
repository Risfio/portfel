"""
Strategy classes
"""

import numpy as np
from pandas import Strategy


class StrategyBase(type):
    def __new__(cls, name, bases, attrs):

        _deals = {}

        new_attrs = {}
        _meta = {}

        if "range" not in attrs.keys():
            _meta.update({'range': []})
        else:
            _meta.update({'range': attrs.pop("range")})

        if "step" not in attrs.keys():
            _meta.update({"step": 0})
        else:
            _meta.update({'step': attrs.pop("step")})

        for key, value in attrs.items():
            if not key.startswith('__'):
                _deals.update({key: value})
        new_attrs.update({"deals": _deals})
        new_attrs.update({"_meta": type("Meta", (type,), _meta)})
        new_attrs.update(attrs)
        new_cls = super().__new__(cls, name, bases, new_attrs)

        return new_cls

    @property
    def values(self):
        return DealsSet(self.deals, attrs=self._meta)

    @values.setter
    def values(self):
        pass


class Strategy(metaclass=StrategyBase):
    pass


class DealsSet:
    def __init__(self, deals, attrs):
        self._deals = deals
        self.ba_min = attrs.range[0]
        self.ba_max = attrs.range[1]
        self.step = attrs.step


    def all(self):
        revenue = []
        ba_range = []
        for ba in range(self.ba_min, self.ba_max, self.step):
            ba_range.append(ba)
            rev = 0
            for name, deal in self._deals.items():
                rev += deal.execute_deal(ba)
            revenue.append(rev)

        return Series(data=revenue, index=ba_range)

