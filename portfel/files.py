"""

Usefull functions for download from data from files.

"""

import pandas as pd

import os, sys

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

DATA_DIRS = (
    os.path.join(BASE_DIR, "data"),
)


class FileLoader:
    def __init__(self, filename="", ext="txt", files_storage=DATA_DIRS):
        """
        Use for search specified files in specified directories(files_storage)

        :param filename: Name for file
        :param ext: file extension , default is txt
        :param files_storage: tuple with array of directories for search
        """

        # Temp code
        self.filepath = os.path.join(DATA_DIRS[0], ".".join([filename, ext]))

        return super(FileLoader, self).__init__()

