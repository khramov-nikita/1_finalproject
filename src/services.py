from pandas.core.frame import DataFrame

from src.utils import count_categories, return_result


def cashback_categories(data: DataFrame, year: str, month: str) -> None:
    """
    Функция подсчитывает бонус по каждой категории в указанном диапазоне времени
    """
    data_list: list = data.to_dict(orient="records", into=dict)
    categories_dict = count_categories(data_list, year, month)
    return_result(categories_dict)
    return
