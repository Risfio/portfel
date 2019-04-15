"""
... somethig

Analize class have same usage:

>>> class analize(Analize):
>>>     def less_then(self, arg=0, lbl="less then %VAL%" msg="Revenues range less 0"):
>>>         result = super(analize, self).less_then(arg, msg)
>>>         return pd.DataFrame(data=result, index=msg)


***************************** TRICK FOR JUPYTER *************************************
Must part:
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

Example code:
from pydataset import data
quakes = data('quakes')
quakes.head()
quakes.tail()

"""


import pandas as pd


class Analize:

    def __init__(self, data=[]):
        self._data = data

    def get(self, **kwargs):
        analize_methods = []
        for k, v in kwargs.items():
            if hasattr(self, k):
                analize_methods.append((k, v))

        result = None
        for method in analize_methods:
            name, arg = method
            for u in self._data:
                if result is None:
                    result = getattr(self, name)(arg, u)
                elif result is not None:
                    result.append(getattr(self, name)(arg, u))
        return result

    def less_then(self, arg, analized_item, lbl="less then %VAL%", msg="Here description"):
        return pd.DataFrame(data=[[arg, lbl, msg]], columns=["value", "name", "description"])

