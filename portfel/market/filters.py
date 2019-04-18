


class Filter:
    def __init__(self, data, **kwargs):
        # check filters param
        self._data = data
        self.result = None
        for name, arg in kwargs.items():
            if name in self.__dict__.keys():
                result = self.__dict__[name](arg)

    def less_then(self, arg):
        result = pd.DataFrame(data={"revenues":[], "base active":[]})
        for x in range(0, self._data.size):
            rev, ba = self._data[x]
            if rev < 0:
                result.update([rev, data])
        return result

