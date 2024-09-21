import os
from typing import Optional
from datetime import datetime, timedelta
from src.decorators import log_dataframe
import pandas as pd


@log_dataframe()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Функция принимает датафрейм, категорию и дату по которую будут выведены операции за последние 3 месяца
    """
    data = transactions.to_dict(orient="records", into=dict)
    if date:
        date_items = datetime.strptime(date, "%d.%m.%Y")
    else:
        date_items = datetime.now()
    delta = timedelta(days=90)
    result_list = []
    for transaction in data:
        transaction_date = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if (
            1 <= transaction_date.day <= date_items.day
            and (date_items - delta).month <= transaction_date.month <= date_items.month
            and transaction_date.year == date_items.year
            and transaction["Категория"] == category
        ):
            result_list.append(transaction)
    result = pd.DataFrame(result_list)
    return result


if __name__ == "__main__":
    print(spending_by_category(pd.DataFrame([{}]), ""))
