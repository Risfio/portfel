"""

Main BWS class.
"""

from .fileloader import FileLoader


class BWS:
    def __init__(self, path=""):
        self._fileloader = FileLoader(path=path)
        return super(BWS, self).__init__()


