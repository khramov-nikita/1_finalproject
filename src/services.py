import pandas as pd
import os
import datetime
import logging
import json
from collections import Counter
from pandas.core.frame import DataFrame
from src.utils import count_categories, return_result


def cashback_categories(data: DataFrame, year: str, month: str):
    data_list: list = data.to_dict(orient="records", into=dict)
    categories_dict = count_categories(data_list, year, month)
    return_result(categories_dict)
    return
