"""
"""

import argparse
import os
import sys

sys.path.append(os.getcwd())
import portfelcfg


def print_info(s):
    print("*" * 10, "\r\n", s, "\r\n", "*" * 10)


if __name__ == "__main__":
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers(help="List of available options:")

    append_parser = subparsers.add_parser("append", help="append new data to main database file")
    append_parser.add_argument("--source", type=str, help="Path to new -=DAY=- data in .txt file created with QUIK")

    delete_parser = subparsers.add_parser("delete", help="remove data for specified date")
    delete_parser.add_argument("--date", type=str, help="")

    main_parser.parse_args(sys.argv[1:])

