import os

import pandas as pd

from src.services import cashback_categories
from src.utils import read_xlsx
from src.views import get_main_page
from src.reports import spending_by_category

path = os.path.abspath(__file__)
xlsx_path = os.path.join(path[:-12], "data", "operations.xlsx")


def main() -> None:
    """
    Через эту функцию происходит взаимодействие с программой
    """
    get_main_page()
    cashback_categories(read_xlsx(xlsx_path), input("Введите год "), input("Введите месяц "))
    print(
        spending_by_category(pd.DataFrame(read_xlsx(xlsx_path)), input("Введите категорию: "), input("Введите дату: "))
    )
    return


if __name__ == "__main__":
    main()
