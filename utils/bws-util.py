"""
"""

import os, sys
import argparse
import pandas as pd
from pandas.errors import EmptyDataError

sys.path.append(os.getcwd())
import portfelcfg


WORKING_DIR = os.path.join(portfelcfg.BASE_DIR, "tests", "TEMP")


def print_info(s):
    print("*" *10, "\r\n", s, "\r\n", "*" *10)


# Main functions
class ValidationError(Exception):
    pass


def validate(main_data=None, new_data=None, validators=[]):
    """
    Run multiple validators on specified data
    :param main_data: pandas.DataFrame returned by _get_main_data function. Default None if not validate this data.
    :param new_data: pandas.DataFrame usualy returned by _read_quik_csv data. Default None if not validate this data.
    :param validators: List of validators. Validator is function with 2 params "main_data" and "new_data".
                    If one of the parameters is None - validator can not validate this data.
    :return: False if one of validators raise ValidationError. If not - it returns True.
    """
    all_ok = True
    for val in validators:
        try:
            val(main_data, new_data)
        except ValidationError as err:
            print_info(err)
            all_ok = False
    return all_ok

def _get_working_dir():
    if not os.path.isdir(WORKING_DIR):
        raise Exception("Directory {} not setted!".format(WORKING_DIR))
    return WORKING_DIR


def _get_file(file_path):
    file_path = os.path.join(_get_working_dir(), file_path)
    if not os.path.isfile(file_path):
        raise Exception("File {} not found!".format(file_path))
    return file_path


def _get_main_file():
    """
    Get bws.txt absolute path.
    """
    main_file = _get_file("bws.txt")
    return main_file


def _read_main_data():
    return pd.read_csv(_get_main_file())


# Functions for append
def _read_quik_csv(file_path):
    """
    Read BCS QUIK file.
    :param file_path: file name without path , but with extension
    :return: pandas.DataFrame
    """
    fl = _get_file(file_path)
    names = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
    df = pd.read_csv(fl, sep='\t', encoding="cp1251", header=None, names=names)
    return df

def _is_date_unique(main, other):
    dates_main = main['Date'].unique()
    new_date = other['Date'].unique()
    for nd in new_date:
        if nd in dates_main:
            raise ValidationError("Validation Error!!! Date {0} not unique!".format(nd))


def _append_func(new_data, validators=[]):
    main_df = None
    try:
        main_df = pd.read_csv(_get_main_file())
    except EmptyDataError as err:
        new_data.to_csv(_get_main_file(), index=False)
    else:
        if validate(main_df, new_data, validators=validators) == True:
            main_df = main_df.append(new_data, ignore_index=True)
            main_df.to_csv(_get_main_file(), index=False)


def append_func(args):
    """
    Append new data to main file.
    :param args:
    :return:
    """
    new_data = _read_quik_csv(args.source)
    _append_func(new_data, validators=[_is_date_unique])


# Temp test parser
def test_func(args):
    main = _read_main_data()
    print_info(main['Date'].size)


#Parsers
main_parser = argparse.ArgumentParser(description="Processing files for BWS strategy")
subparsers = main_parser.add_subparsers()

append_parser = subparsers.add_parser("append", help="Append new =DAY= data from file to main database")
append_parser.add_argument("--source", type=str)
append_parser.set_defaults(func=append_func)

test_parser = subparsers.add_parser("test")
test_parser.set_defaults(func=test_func)
test_parser.add_argument("--param1", type=str)

if __name__ == "__main__":
    args = main_parser.parse_args(sys.argv[1:])
    args.func(args)

