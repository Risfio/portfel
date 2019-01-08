import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from options import _fromstring, Option


if __name__ == "__main__":
    # s = 'Si66500BC0'
    # params = _fromstring(s)
    # opt = Option(*params)
    # print(opt.base_active)

    wrng_s = 'Si66500AC0'
    params = _fromstring(wrng_s)
    opt = Option(*params)

    print("Option type :", opt.type, " and option month :", opt.month)

