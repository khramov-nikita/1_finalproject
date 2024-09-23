from typing import Any
from unittest.mock import patch

from src import processing


def test_count_categories(data: list, data_result: dict) -> None:
    assert processing.count_categories(data, "2019", "7") == data_result


def test_get_greeting() -> None:
    assert processing.get_greeting(10) == "Доброе утро"
    assert processing.get_greeting(16) == "Добрый день"
    assert processing.get_greeting(20) == "Добрый вечер"
    assert processing.get_greeting(4) == "Доброй ночи"
    assert processing.get_greeting(12343) == "Ошибка приветствия"


def test_get_last_digits() -> None:
    assert processing.get_last_digits("*1234") == "1234"
    assert processing.get_last_digits("1234123412341234") == "1234"
    assert processing.get_last_digits("sszergszgr") == "Ошибка номера карты"


def test_get_total_spent(spent_list: list) -> None:
    assert processing.get_total_spent(spent_list) == 6.3


def test_get_cashback() -> None:
    assert processing.get_cashback(123123.12) == 1231.23


def test_get_top_transactions(data: list, top_transactions: list) -> None:
    assert processing.get_top_transactions(data) == top_transactions


def test_get_cards(data: list, cards: list) -> None:
    assert processing.get_cards(data) == cards
