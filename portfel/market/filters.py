import pandas as pd


class Filter:
    def __init__(self, data, **kwargs):
        self._data = data

    def _sort_data(self, indexes):
        """
        :ranges array: массив значений которые надо выбрать.
                        Например, после фильтрации получаем значение ranges
                        из которых формируем новый DataFrame
        :return DataFrame: возвращает новый DataFrame
        """
        result = []
        n = 0
        for val in self._data.iterrows():
            if n in indexes:
                result.append(self._data.values[n])
            n += 1
        return pd.DataFrame(data=result, columns=self._data.columns)

    def less_then(self, arg, column):
        """
        Filter dataframe for val's less then arg in specified DataFrame
        column.
        :param arg: int value
        :param column: specified column in DataFrame object
        :return: array with indecies what matches the condition
        """
        n = 0
        indexes = []
        for val in self._data[column]:
            if val < arg:
                indexes.append(n)
            n += 1
        return indexes

    def __call__(self, **kwargs):
        result = None
        for name, arg in kwargs.items():
            if hasattr(self, name) is True:
                result = self.__getattribute__(name)(arg, column=kwargs['column'])
                break
        return self._sort_data(result)
