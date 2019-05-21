"""

Predefined classes for loading data from files.
"""

import pandas as pd
import os


class FileLoaderBase:

    def __init__(self, directory="", names=(), file_name=""):
        self._directory = directory
        self._file_name = file_name

        # check columns names
        if not type(names) is tuple:
            raise Exception("names parameter must be tuple")
        else:
            self._names = names

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, arg):
        self._directory = arg

    def _get_file_path(self, directory, file_name, ext=".txt"):
        file_path = os.path.join(directory, "".join([file_name, ext]))
        if os.path.isdir(directory):
            if os.path.isfile(file_path):
                pass
            else:
                raise Exception("File {0} not found!".format(file_path))
        else:
            raise Exception("Directory {0} not found!".format(directory))
        return file_path

    def _load_pandas_data(self, path="", directory="", file_name="", sep=";", encoding="utf-8", ext=".txt", names=[]):
        if len(names)==0:
            names = self._names
        elif len(names) > 0:
            names = tuple(names)
        return pd.read_csv(path, encoding=encoding, sep=sep, header=None, names=names)

    def _construct_file_name(self, file_name):
        if file_name == "":
            file_name = self._file_name
        return file_name

    def read_data(self, file_name=""):
        return self._load_pandas_data(file_name=self._construct_file_name(file_name))


class FileLoaderQUIK(FileLoaderBase):
    """
    Для загрузки CSV из файла созданного копипастой из QUIK.
    Для создания файла следующие шаги:
    1) В таблице QUIK "Текущие торги" должны быть поля Имя, Дата торгов, Код, ISIN, Мин, Макс, Откр., Закрытие, Объем
    2) ПКМ - Компировать все
    3) Сохраняем в текстовый файл emitents_ddmmyyyy.txt
    4) Удаляем верхний ряд с названием колонок.
    """

    def __init__(self, directory="", names=(), file_name=""):
        names = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
        return super(FileLoaderQUIK, self).__init__(directory=directory, names=names, file_name=file_name)

    def _load_pandas_data(self, path="", directory="", file_name="", sep="\t", encoding="utf-8", ext=".txt", names=[]):
        if directory == "":
            directory = self._directory
        path = self._get_file_path(directory, file_name)
        encoding = 'cp1251'
        return super(FileLoaderQUIK, self)._load_pandas_data(path=path, encoding=encoding, sep=sep, names=names)

