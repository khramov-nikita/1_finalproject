import os
from functools import wraps
from typing import Any

path = os.path.dirname(__file__)
log_path = os.path.join(path[:-3], "data", "log_dataframe.csv")


def log_dataframe(file_path: str = log_path) -> Any:
    """
    Декоратор записывает полученный датафрейм в csv файл
    """

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*arg: Any, **kwargs: Any) -> Any:
            try:
                result = func(*arg, **kwargs)
            except Exception as e:
                raise e
            else:
                result.to_csv(file_path)
                return result

        return wrapper

    return decorator
