"""
Strategy classes
"""

import numpy as np
from pandas import DataFrame

from .filters import Filter


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

    def _get_data_calculation_func(self):
        def func():
            revenue = []
            ba_range = []
            for ba in range(self._meta.range[0], self._meta.range[1], self._meta.step):
                ba_range.append(ba)
                rev = 0
                for name, deal in self.deals.items():
                    rev += deal.execute_deal(ba)
                revenue.append(rev)

            return DataFrame(data={'revenues': revenue, "base_active": ba_range})

        return func

    @property
    def values(self):
        _data_calculation = self._get_data_calculation_func()
        return DealSet(_data_calculation, attrs=self._meta)

    @values.setter
    def values(self):
        pass


class Strategy(metaclass=StrategyBase):
    pass


class DealSet:
    def __init__(self, deals, attrs):
        self._data = deals

    def filter(self, **kwargs):
        pass

    def all(self):
        return self._data()

