import sys, os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from options import _fromstring, Option


if __name__ == "__main__":
    s = 'Si66500BC0'
    params = _fromstring(s)
    opt = Option(*params)

    s1 = params[0]
    pat = re.compile(r'\w{2,2}')
    print(pat.match(s1))

