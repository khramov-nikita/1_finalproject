import os
import json
import pandas as pd
from pandas.core.frame import DataFrame
import datetime
from collections import defaultdict


utils_path = os.path.abspath(__file__)
json_path = os.path.join(utils_path[:-13], "data", "cashback.json")


def read_xlsx(path: str) -> DataFrame:
    result = pd.read_excel(path)
    print(result.head())
    return result


def count_categories(data: list, year: str, month: str) -> dict:
    """
    Функция подсчитывает количество категорий транзакций
    """
    categories = defaultdict()
    categories_result = dict()
    for transaction in data:
        date_obj = datetime.datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))] = []
    for transaction in data:
        date_obj = datetime.datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))].append(transaction.get("Бонусы (включая кэшбэк)"))
    for category in categories:
        categories_result[category] = sum(categories.get(category))
    return dict(categories_result)


def return_result(data: dict):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return


