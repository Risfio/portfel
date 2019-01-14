import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from markets import MarketFORTS
from options import _fromstring, Option


if __name__ == "__main__":
    # String for test options
    # s = 'Si66500BC0'
    class Market1(MarketFORTS):
        pass

