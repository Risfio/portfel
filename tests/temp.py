import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from markets import MarketFORTS
from options import fromstring, Option
from markets import BrockerDeal, DEAL_POSITION_TYPE_SHORT, DEAL_POSITION_TYPE_LONG


if __name__ == "__main__":
    # String for test options
    s = 'Si66500BC0'
    opt = fromstring(s)
    bd = BrockerDeal(opt, 1000, DEAL_POSITION_TYPE_LONG, et=True)

    print(bd.execute_deal(67000))

