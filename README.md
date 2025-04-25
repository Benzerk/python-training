# Python

## General

- [Documentation](https://docs.python.org/3/)
- [Tutorial](https://docs.python.org/3/tutorial/)
- [Language Reference](https://docs.python.org/3/reference/)
- [Standard Library Reference](https://docs.python.org/3/library/)
- [Package Manager](https://docs.python.org/3/installing/)
- [Virtual Environments](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments)
- [Coding Conventions](https://peps.python.org/pep-0008)
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Video Tutorial](https://www.youtube.com/playlist?list=PLT98CRl2KxKGIazPd2nQEPbG7sQpT8LEj)
- [Python Notes for Professionals](https://books.goalkicker.com/PythonBook/)


## Standard Library

```python
import os # File Operations, Environment Variables, OS Commands (https://docs.python.org/3/library/os.html)
import argparse # CLI Arguments (https://docs.python.org/3/library/argparse.html)
import math # Mathematic Functions (https://docs.python.org/3/library/math.html)
import decimal # Decimal Arithmetic (https://docs.python.org/3/library/decimal.html)
from datetime import date, time, datetime # Date & Time (https://docs.python.org/3/library/datetime.html)
from dataclasses import dataclass # Data Classes (https://docs.python.org/3/library/dataclasses.html)
from collections import deque # Stacks/Queues (https://docs.python.org/3/library/collections.html#collections.deque)
from enum import Enum, IntEnum # Enumerations (https://docs.python.org/3/library/enum.html)
import itertools # Iterators (https://docs.python.org/3/library/itertools.html)
import unittest # Unit Tests (https://docs.python.org/3/library/unittest.html)
import logging # Logging (https://docs.python.org/3.13/library/logging.html)
from pathlib import Path # Logical Filesystem Paths (https://docs.python.org/3/library/pathlib.html)
import sqlite3 # SQLite Database (https://docs.python.org/3/library/sqlite3.html)
import csv # CSV Parsing (https://docs.python.org/3/library/csv.html)
import tomllib # TOML Parsing (https://docs.python.org/3/library/tomllib.html)
import json # JSON Parsing (https://docs.python.org/3/library/json.html)
import tarfile # TAR Archiving (https://docs.python.org/3.13/library/tarfile.html)
import gzip # GZIP Compression (https://docs.python.org/3/library/gzip.html)
import zipfile # ZIP Compression (https://docs.python.org/3/library/zipfile.html)
import re # Regular Expressions (https://docs.python.org/3/library/re.html)
import gettext # Internationalization/Localization (https://docs.python.org/3.13/library/gettext.html)
```

- [ArgParse How-To](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)
- [Logging How-To](https://docs.python.org/3/howto/logging.html)
- [Logging Examples](https://docs.python.org/3/howto/logging-cookbook.html)
- [Enumerations How-To](https://docs.python.org/3/howto/enum.html#enum-howto)
- [Regular Expressions How-To](https://docs.python.org/3/howto/regex.html#regex-howto)


## Additional Libraries

- [Requests](https://requests.readthedocs.io/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Apache Airflow](https://airflow.apache.org/docs/apache-airflow)


## Useful commands (Windows)

```powershell
# Display Python version 
py --version

# Create a virtual environment
py -m venv .venv

# Activate a virtual environment
.\.venv\Scripts\Activate.ps1

# Install & Upgrade package manager
py -m ensurepip --upgrade
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install packages
pip install <package>

# Upgrade packages to the latest from PyPI
pip install --upgrade <package>

# Deactivate virtual environment
deactivate
```
