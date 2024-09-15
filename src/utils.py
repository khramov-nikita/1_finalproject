import datetime
import json
import logging
import os
from collections import defaultdict

import pandas as pd
from pandas.core.frame import DataFrame

utils_path = os.path.abspath(__file__)
json_path = os.path.join(utils_path[:-13], "data", "cashback.json")
utils_log_path = os.path.join(utils_path[:-13], "data", "utils.log")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=utils_log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def read_xlsx(path: str) -> DataFrame:
    """
    Функция читает XlSX файл
    """
    try:
        app_logger.info("Чтение XLSX файла")
        result = pd.read_excel(path)
    except Exception as e:
        app_logger.error(f"Неудачная попытка чтения файла: {e}")
        raise e
    else:
        return result


def count_categories(data: list, year: str, month: str) -> dict:
    """
    Функция подсчитывает бонус по категориям
    """
    app_logger.info("Подсчёт бонуса по категориям")
    categories: defaultdict = defaultdict()
    categories_result = dict()
    for transaction in data:
        date_obj = datetime.datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))] = []
    for transaction in data:
        date_obj = datetime.datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))].append(int(transaction.get("Бонусы (включая кэшбэк)")))
    for category in categories:
        my_list: list = categories.get(category)
        categories_result[category] = sum(my_list)
    return dict(categories_result)


def return_result(data: dict) -> None:
    """
    Функция записывает результат в JSON файл
    """
    try:
        app_logger.info("Выгрузка JSON файла")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception as e:
        app_logger.error(f"Неудачная попытка выгрузки файла: {e}")
        raise e
    else:
        return
