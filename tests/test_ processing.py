from typing import Any
from unittest.mock import patch

from src.processing import count_categories


@patch("datetime.datetime")
def test_datetime(mock_datetime: Any, data: list) -> None:
    count_categories(data, "2019", "7")
    mock_datetime.assery_called()


def test_count_categories(data: list, data_result: dict) -> None:
    assert count_categories(data, "2019", "7") == data_result
