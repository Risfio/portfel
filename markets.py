"""
Main portfell class and additional functionality.
"""


class PortfelCreator:
    def __init__(self, market, portfel_name=""):
        if market is None:
            self.market = self._make_market(market)

    def _make_market(self, marketname="FORTS"):
        market = None
        if marketname == "FORTS":
            market = MarketFORTS()
        elif marketname == "MMVB":
            market = MarketMMVB()
        return market


class MarketFORTS:
    def __init__(self):
        self.options = OptionsPortfel()


class OptionsPortfel:
    def __init__(self):
        self._options = []

    def add(self, option):
        self._options.add(option)


class MarketMMVB:
    pass
