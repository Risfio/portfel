"""
UTILS package.

Using for download data from files and etc. resources
"""

import os, sys
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(SETTINGS_PATH)

# PyCharm тупит, но это работает
import settings as conf

from .filedownloaders import *

