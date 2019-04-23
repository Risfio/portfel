"""

Function for donload data from files.

"""

import os


class FileLoader:
    def __init__(self, path=""):
        if os.path.exists(path):
            self.base_dir = path
        else:
            raise Exception("Directory %s not found".format(path))
        return super(FileLoader, self).__init__()


