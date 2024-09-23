from typing import Any
from unittest.mock import patch

from src.external_api import get_currency_rates, get_stock_prices


@patch("requests.get")
def test_get_currency_rates(mock_get: Any) -> None:
    get_currency_rates()
    mock_get.assert_called()


@patch("requests.get")
def tests_get_stock_prices(mock_get: Any) -> None:
    get_stock_prices()
    mock_get.assert_called()
