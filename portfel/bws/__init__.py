"""

Best Weekly Stats stock exchange strategy.

"""

import os
import pandas as pd


EMITENTS_LIST = ("ALRS", "GAZP", "SNGS",)

def _get_dir(cls=None, directory=""):
    if os.path.isdir(directory) is False:
        raise IOError("Directory {0} not found".format(directory))
    return directory

def load_emitent_data(cls, directory, ticker, ext=".txt"):
    data = None
    file_path = os.path.join(_get_dir(directory=directory), "".join([ticker, ext]))
    if os.path.isfile(file_path):
        data = pd.read_csv(file_path, sep=";")
    else:
        raise IOError("File {0} not found".format(ticker))
    return data

