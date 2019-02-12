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
    deal = BrockerDeal(opt, 1000)
    print("Buy CALL option in money:", deal.execute_deal(66000))
    print("Buy CALL option not in money:", deal.execute_deal(64000))

    sell_call = BrockerDeal(opt, 1000, 0)
    print("Sell CALL option in money:", sell_call.execute_deal(66000))
    print("Sell CALL option not in money:", sell_call.execute_deal(64000))


    s1 = "Si65000BO0"
    opt1 = fromstring(s1)
    deal1 = BrockerDeal(opt1, 1000)
    print("Buy PUT option in money:", deal1.execute_deal(64000))
    print("Buy PUT option not in money:", deal1.execute_deal(66000))

    sell_put = BrockerDeal(opt1, 1000, 0)
    print("Sell PUT option in money:", sell_put.execute_deal(64000))
    print("Sell PUT option not in money:", sell_put.execute_deal(66000))
