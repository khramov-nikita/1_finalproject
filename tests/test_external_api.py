from typing import Any
from unittest.mock import patch

from src.external_api import get_currency_rates, get_stock_prices


@patch("json.load")
@patch("requests.get")
def test_get_currency_rates(mock_get: Any, mock_load: Any) -> None:
    mock_load.return_value = {"user_currencies": ["USD", "EUR"]}
    api_answer = {"Valute": {"USD": {"Value": 55.552}, "EUR": {"Value": 77.7777}}}
    mock_get.return_value.json.return_value = api_answer

    expected_result = [{"currency": "USD", "rate": "55.55"}, {"currency": "EUR", "rate": "77.78"}]

    result = get_currency_rates()
    assert result == expected_result


@patch("json.load")
@patch("requests.get")
def test_get_stock_prices(mock_get: Any, mock_load: Any) -> None:
    mock_load.return_value = {"user_stocks": ["AAPL"]}
    api_answer = {"Global Quote": {"01. symbol": "AAPL", "05. price": 226.8}}
    mock_get.return_value.json.return_value = api_answer

    expected_result = [{"stock": "AAPL", "price": "226.8"}]

    result = get_stock_prices()
    assert result == expected_result
