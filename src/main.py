import os

from src.services import cashback_categories
from src.utils import read_xlsx

main_path = os.path.abspath(__file__)
xlsx_path = os.path.join(main_path[:-12], "data", "operations.xlsx")


def main() -> None:
    """
    Через эту функцию происходит взаимодействие с программой
    """
    cashback_categories(read_xlsx(xlsx_path), input("Введите год "), input("Введите месяц "))
    return


main()
