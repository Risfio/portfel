"""
"""


class BWSBase:
    """
    Main BWS class base.
    Declaration of this class instance:

    class BWS(BWSBase):
        db = bws.txt


    """
    def __init__(self):
        return  super(BWSBase, self).__init__()

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        """
        Warning!!! Here must be functional to set ablosute path to database file.
        :param value: database file name with extension(it's important)
        """
        self._db = value

    def _load_data(self, *args, **kwargs):
        self._data = pd.read_csv(self._db)


