"""

Predefined classes for loading data from files.
"""

import pandas as pd
import os


class FileLoaderBase:

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

    def _load_pandas_data(self, path="", directory="", file_name="", sep=";", encoding="utf-8", ext=".txt"):
        return pd.read_csv(path, encoding=encoding, sep=sep)

    def _construct_file_name(self, file_name):
        return file_name

    def read_data(self, file_name):
        return self._load_pandas_data(file_name=self._construct_file_name(file_name))


class FileLoaderQUIK(FileLoaderBase):
    def _load_pandas_data(self, path="", directory="", file_name="", sep="\t", encoding="utf-8", ext=".txt"):
        directory = self.directory
        path = self._get_file_path(directory, file_name)
        encoding = 'cp1251'
        return super(FileLoaderQUIK, self)._load_pandas_data(path=path, encoding=encoding, sep=sep)

