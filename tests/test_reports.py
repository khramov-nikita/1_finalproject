from typing import Any
from unittest.mock import patch

import pandas as pd

from src.reports import spending_by_category


@patch("pandas.core.frame.DataFrame.to_dict")
def test_spending_by_category_to_dict(mock_to_dict: Any) -> None:
    a = spending_by_category(pd.DataFrame([{}]), '')
    mock_to_dict.assert_called_once()
