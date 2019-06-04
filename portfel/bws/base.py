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

    def emitents_progression_formula(emitent_data_previous, emitent_data_current):
        """
        This is editable function.
        It gets emitent data by 2 week - previous week and current(more info in functions params declaration).
        'Name', 'ISIN', 'Date'(not needed), 'Open', 'Min', 'Max', 'Close', 'Volume'
        """
        pass

    def _get_emitents_progression(self, data, week_previous=None, week_current=0):
        pass

    def get_groups(self, groups=3, maxnum=10):
        """
        Call stack:
        load data from main database
        ...


        """
        data = self._load_data()
        sorted_data = self._get_emitents_progression((data)
        # to be continue...

