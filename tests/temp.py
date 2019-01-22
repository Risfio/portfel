import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from markets import MarketFORTS
from options import fromstring, Option
from markets import BrockerDeal, DEAL_POSITION_TYPE_SHORT, DEAL_POSITION_TYPE_LONG


if __name__ == "__main__":
    data_range = []
    period_in = 5

