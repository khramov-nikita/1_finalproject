import os
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.utils import read_xlsx

path = os.path.dirname(__file__)
test_path = os.path.join(path[:-5], "data", "cashback.json")
test_operations_path = os.path.join(path[:-5], "data", "operations.xlsx")


@patch("pandas.read_excel")
def test_read_xlsx(mock_read_excel: Any, get_operations_df: pd.DataFrame) -> None:
    mock_read_excel.return_value = get_operations_df
    assert read_xlsx(test_operations_path) == [
        {
            "Дата операции": "31.12.2021 16:42:04",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -64.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -64.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Супермаркеты",
            "MCC": "5411",
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 1.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 64.0,
        },
        {
            "Дата операции": "07.04.2020 19:41:58",
            "Дата платежа": "07.04.2020",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -100.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -100.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Фастфуд",
            "MCC": "5814",
            "Описание": "IP Yakubovskaya M. V.",
            "Бонусы (включая кэшбэк)": 2.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 100.0,
        },
    ]
