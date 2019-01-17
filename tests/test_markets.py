import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from markets import MarketFORTS


if __name__ == "__main__":
    market = MarketFORTS(name='test')
    print(market)

