import os

from src.services import cashback_categories
from src.utils import count_categories, read_xlsx, return_result

main_path = os.path.abspath(__file__)
xlsx_path = os.path.join(main_path[:-12], "data", "operations.xlsx")


def main():
    cashback_categories(read_xlsx(xlsx_path), input("Введите год "), input("Введите месяц "))
    return


main()
