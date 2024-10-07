import json
import logging
import os

import pandas as pd

path = os.path.dirname(__file__)
log_path = os.path.join(path[:-3], "logs", "utils.log")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def read_xlsx(file_path: str) -> list:
    """
    Функция читает XlSX файл
    """
    try:
        app_logger.info("Чтение XLSX файла")
        result = pd.read_excel(file_path)
        result_list: list = result.to_dict(orient="records", into=dict)
    except Exception as e:
        app_logger.error(f"Неудачная попытка чтения файла: {e}")
        raise e
    else:
        return result_list


def return_dict_to_json(data: dict, file_path: str) -> None:
    """
    Функция записывает результат в JSON файл
    """
    try:
        app_logger.info("Выгрузка JSON файла")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception as e:
        app_logger.error(f"Неудачная попытка выгрузки файла: {e}")
        raise e
    else:
        return
