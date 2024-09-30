import json
import logging
import os
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta


from src.decorators import log_dataframe


path = os.path.dirname(__file__)
log_path = os.path.join(path[:-3], "logs", "services.log")
json_path = os.path.join(path[:-3], "data", "cashback.json")
operations_path = os.path.join(path[:-3], "data", "operations.xlsx")


app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


@log_dataframe()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> json:
    """Function for filter transactions by category of spending"""
    app_logger.info('Попытка фильтрации транзакций по категории')
    last_day = pd.to_datetime(date, dayfirst=True) if date else datetime.today()
    first_day = last_day - relativedelta(months=3)
    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    filtered_trans_by_date = transactions[
        (transactions["Дата операции"] >= first_day) & (transactions["Дата операции"] <= last_day)
    ]
    filtered_trans_by_cat = pd.DataFrame(filtered_trans_by_date[filtered_trans_by_date["Категория"] == category])
    return filtered_trans_by_cat


if __name__ == "__main__":
    print(spending_by_category(pd.read_excel(operations_path), "Супермаркеты", "31.12.2021").head())
