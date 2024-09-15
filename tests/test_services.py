import os
from typing import Any
from unittest.mock import patch

from src.services import cashback_categories
from src.utils import read_xlsx

test_path = os.path.abspath(__file__)
xlsx_test_path = os.path.join(test_path[:-23], "data", "operations.xlsx")


@patch("pandas.core.frame.DataFrame.to_dict")
def test_cashback_categories(mock_to_dict: Any, data: list) -> None:
    mock_to_dict.return_value.list.return_value = data
    cashback_categories(read_xlsx(xlsx_test_path), "2019", "7")
    mock_to_dict.assert_called_once()
