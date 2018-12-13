"""
Initial options package
"""

import re


def fromstring(str):

    temp = ""
    result = []

    ba_reg = re.compile(r'^\w{2,2}')
    result.append(ba_reg.findall(str)[0])
    temp = ba_reg.subn("", str, 1)[0]


    # Get strike price and deals type(marginal or premial)
    strike_reg = re.compile(r'^\d{2,}')
    result.append(strike_reg.findall(temp)[0])
    temp = strike_reg.subn("", temp, 1)[0]

    #Get type of settlement
    settlement_reg = re.compile(r'^[A|B]{1,1}')
    result.append(settlement_reg.findall(temp)[0])
    temp = settlement_reg.subn('', temp, 1)[0]

    #Get month
    month_reg = re.compile(r'^[L]{1,1}')
    result.append(month_reg.findall(temp)[0])
    temp = month_reg.subn('', temp, 1)[0]

    #Get year
    result.append(temp)

    return result

