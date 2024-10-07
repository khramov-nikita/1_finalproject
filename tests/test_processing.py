import pandas as pd

from src import processing
from src.processing import get_cards, get_top_transactions


def test_count_categories(data: list, data_result: dict) -> None:
    assert processing.count_categories(data, "2019", "7") == data_result


def test_get_greeting() -> None:
    assert processing.get_greeting(10) == "Доброе утро"
    assert processing.get_greeting(16) == "Добрый день"
    assert processing.get_greeting(20) == "Добрый вечер"
    assert processing.get_greeting(4) == "Доброй ночи"
    assert processing.get_greeting(12343) == "Ошибка приветствия"


def test_get_cards(get_operations_df: pd.DataFrame):
    assert get_cards(get_operations_df) == [{"cashback": -1.64, "last_digits": "7197", "total_spent": -164.0}]


def test_get_top_transactions(get_operations_df: pd.DataFrame):
    assert get_top_transactions(get_operations_df) == [
        {"amount": -64.0, "category": "Супермаркеты", "date": "31.12.2021", "description": "Колхоз"},
        {"amount": -100.0, "category": "Фастфуд", "date": "07.04.2020", "description": "IP Yakubovskaya M. V."},
    ]
