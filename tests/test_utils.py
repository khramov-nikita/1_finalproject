import os
from typing import Any
from unittest.mock import patch

from src.utils import read_xlsx, return_dict_to_json

path = os.path.dirname(__file__)
test_path = os.path.join(path[:-5], "data", "cashback.json")


@patch("pandas.read_excel")
def test_read_xlsx(mock_read_excel: Any) -> None:
    read_xlsx("")
    mock_read_excel.assert_called_once()


@patch("json.dump")
def test_json_dump(mock_json_dump: Any) -> None:
    return_dict_to_json({}, test_path)
    mock_json_dump.assert_called_once()
