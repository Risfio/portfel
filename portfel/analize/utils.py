"""
... somethig

Analize class have same usage:

>>> class analize(Analize):
>>>     def less_then(self, arg=0, msg="Revenues range less 0"):
>>>         result = super(analize, self).less_then(arg, msg)
>>>         return pd.DataFrame(data=result, index=msg)


"""


class Analize:
    pass

