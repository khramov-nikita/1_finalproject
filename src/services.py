import logging
import os

from pandas.core.frame import DataFrame

from src.utils import count_categories, return_result

services_path = os.path.abspath(__file__)
services_log_path = os.path.join(services_path[:-16], "data", "utils.log")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=services_log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def cashback_categories(data: DataFrame, year: str, month: str) -> None:
    """
    Функция подсчитывает бонус по каждой категории в указанном диапазоне времени
    """
    try:
        app_logger.info("Начало работы функции подсчёта кешбека")
        data_list: list = data.to_dict(orient="records", into=dict)
        categories_dict = count_categories(data_list, year, month)
        return_result(categories_dict)
    except Exception as e:
        app_logger.error(f"Неудачная попытка подсчёта кешбека: {e}")
        raise e
    else:
        return
