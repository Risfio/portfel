import sys, os
import re
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from portfel.markets import MarketFORTS
from portfel.options import fromstring, Option
from portfel.markets import BrockerDeal, DEAL_POSITION_TYPE_SHORT, DEAL_POSITION_TYPE_LONG


if __name__ == "__main__":
    # Variables for testing volatility calculations
    data_range = []
    period_in = 5

    #loader = FileLoader("SiH9")
    #df = si_prices_volumes(loader.filepath)
    #print(df[['<DATE>', '<HIGH>']])

    s = "Si65000BC0"
    opt = fromstring(s)
    print(opt)
