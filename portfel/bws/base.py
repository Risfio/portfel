"""
"""

import pandas as pd

from datetime import date
from datetime import timedelta


class CalendarDayValidationError(Exception):
	pass


class Calendar:

	def _get_date_fromstring(self, s):
		day, month, year = [int(x) for x in s.split(".")]
		return date(day=day, month=month, year=year)

	def _get_week_dates_bystr(self, s):
		_dates = []
		day, month, year = [int(x) for x in s.split(".")]
		dt = date(day=day, month=month, year=year)
		day_of_week = dt.weekday()

		if day_of_week == 0:
			n = 0
			while n+1 < 6:
				_dates.append((dt + timedelta(days=n)).strftime("%d.%m.%Y"))
				n += 1
		elif day_of_week == 4:
			new_dt = dt - timedelta(days=4)
			n = 0
			while n+1 < 6:
				_dates.append((new_dt + timedelta(days=n)).strftime("%d.%m.%Y"))
				n += 1
		else:
			new_dt = dt - timedelta(day_of_week)
			n = 0
			while n+1 < 6:
				_dates.append((new_dt + timedelta(days=n)).strftime("%d.%m.%Y"))
				n += 1
		return _dates

	def get_week_dates(self, dt):
		_dates = []
		if type(dt) is list:
			_dates = dt
		elif type(dt) is int:
			pass
		elif type(dt) is str:
			_dates = self._get_week_dates_bystr(dt)
		return _dates

	def get_previous_week_dates(self, dt):
		current_week_dates = self.get_week_dates(dt)
		monday = min(current_week_dates)
		previous_friday = self._get_date_fromstring(monday)-timedelta(days=3)
		return self._get_week_dates_bystr(previous_friday.strftime("%d.%m.%Y"))


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

	def week_data(self, dates_list):
		"""
		Return data for ALL emitents for specified dates.
		:param dates_list: list with dates string in format "%d%m%Y"
		:return:
		"""
		result = None

		# TODO: fix string below to self._load_data()
		df = pd.read_csv(self.db)
		# Make Date values as index
		df_reindexed = pd.DataFrame(data=df.values, index=df.Date, columns=df.columns)
		# Get data for specified dates
		result = df_reindexed.loc[dates_list]
		return result

	def get_groups(self, groups=3, maxnum=10, current_date=date.today().strftime("%d.%m.%Y")):
		"""
		Call stack:
		load data from main database
		...


		"""

		# Create dates lists
		calendar = Calendar()
		current_week_dates_list = calendar.get_week_dates(current_date)
		previous_week_dates_list = calendar.get_previous_week_dates(current_date)

		current_week_data = self.week_data(current_week_dates_list)


		
