from unittest.mock import patch
import json
import os
from src.services import cashback_categories
from src.utils import read_xlsx, return_result, count_categories
from typing import Any
from pandas.core.frame import DataFrame


@patch("pandas.read_excel")
def test_read_xlsx(mock_read_excel: Any) -> None:
    read_xlsx("")
    mock_read_excel.assert_called_once()


@patch("json.dump")
def test_json_dump(mock_json_dump: Any) -> None:
    return_result({})
    mock_json_dump.assert_called_once()


@patch("datetime.datetime")
def test_datetime(mock_datetime: Any, data: list) -> None:
    count_categories(data, "2019", "7")
    mock_datetime.assery_called()


def test_count_categories(data: list, data_result: dict) -> None:
    assert count_categories(data, "2019", "7") == data_result
