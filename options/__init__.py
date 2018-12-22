"""
Initial options package
"""

import re
from .base import Option


def _fromstring(input_string):
    temp = ""
    result = []

    ba_reg = re.compile(r'^\w{2,2}')
    result.append(ba_reg.findall(input_string)[0])
    temp = ba_reg.subn("", input_string, 1)[0]

    # Get strike price and deals type(marginal or premial)

    strike_reg = re.compile(r'^\d{2,}')
    result.append(strike_reg.findall(temp)[0])
    temp = strike_reg.subn("", temp, 1)[0]

    # Get type of settlement

    settlement_reg = re.compile(r'^[A|B]{1,1}')
    result.append(settlement_reg.findall(temp)[0])
    temp = settlement_reg.subn('', temp, 1)[0]

    # Get month

    month_reg = re.compile(r'^[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X]{1,1}')
    result.append(month_reg.findall(temp)[0])
    temp = month_reg.subn('', temp, 1)[0]

    # Get year

    result.append(temp)

    return result


def fromstring(input_string):
    """
    Creating Option class examplary from string.
    :param input_string: specionaly formated string
    :return: Option class exemplary or None
    """

    params = _fromstring(input_string)

    return Option(*params)
