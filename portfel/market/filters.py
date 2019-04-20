import pandas as pd


class Filter:
    def __init__(self, data, **kwargs):
        self._data = data

    def _sort_data(self, ranges):
        """
        :ranges array: массив значений которые надо выбрать.
                        Например, после фильтрации получаем значение ranges
                        из которых формируем новый DataFrame
        :return DataFrame: возвращает новый DataFrame
        """
        result = []
        n = 0
        for val in self._data.iterrows():
            if n in ranges:
                result.append(self._data.values[n])
            n += 1
        return pd.DataFrame(data=result, columns=self._data.columns)


