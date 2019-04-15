"""
... somethig

Analize class have same usage:

>>> class analize(Analize):
>>>     def less_then(self, arg=0, lbl="less then %VAL%" msg="Revenues range less 0"):
>>>         result = super(analize, self).less_then(arg, msg)
>>>         return pd.DataFrame(data=result, index=msg)


"""


import pandas as pd


class Analize:

    def __init__(self, items=[]):
        self._items = items

    def get(self, **kwargs):
        analize_methods = []
        for k, v in kwargs.items():
            if hasattr(self, k):
                analize_methods.append((k, v))

        result = pd.DataFrame()
        for method in analize_methods:
            name, arg = method
            result.append(self.__dict__(name)(arg))
        return result

    def less_then(self, arg, lbl="less then %VAL%", msg="Here description"):
        return pd.DataFrame(data=[[arg, lbl, msg]], columns=["value", "name", "description"])

