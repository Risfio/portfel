import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from markets import MarketFORTS
from options import fromstring, Option
from markets import BrockerDeal, DEAL_POSITION_TYPE_SHORT, DEAL_POSITION_TYPE_LONG
from utils import utils
import settings as conf


if __name__ == "__main__":
    # Variables for testing volatility calculations
    data_range = []
    period_in = 5

    pd = utils.Si_from_CSV(os.path.join(conf.DATA_DIRS[0], "SiH9.txt"))

