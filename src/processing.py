import logging
import os
from collections import defaultdict
from datetime import datetime
from typing import Optional

log_path = os.path.abspath("../data/processing.log")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def count_categories(data: list, year: str, month: str) -> dict:
    """
    Функция подсчитывает бонус по категориям
    """
    app_logger.info("Подсчёт бонуса по категориям")
    categories: defaultdict = defaultdict()
    categories_result = dict()
    for transaction in data:
        date_obj = datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))] = []
    for transaction in data:
        date_obj = datetime.strptime(str(transaction.get("Дата операции")), "%d.%m.%Y %H:%M:%S")
        if str(date_obj.year) == year and str(date_obj.month) == month:
            categories[(transaction.get("Категория"))].append(int(transaction.get("Бонусы (включая кэшбэк)")))
    for category in categories:
        my_list: list = categories.get(category)
        categories_result[category] = sum(my_list)
    return dict(categories_result)


def get_greeting(hour: int) -> str:
    """
    Функция возвращает приветствие в зависимости от времени суток
    """
    app_logger.info("получаем приветствие")
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    elif 0 <= hour < 6:
        return "Доброй ночи"
    else:
        app_logger.error("Ошибка приветствия")
        return "Ошибка приветствия"


def get_last_digits(card_number: str) -> str:
    """
    Функция выводит последние 4 цифры номера карты
    """
    app_logger.info("Получаем номер карты")
    if card_number[-4:].isdigit():
        return card_number[-4:]
    else:
        app_logger.error("Ошибка номера карты")
        return "Ошибка номера карты"


def get_total_spent(data: list) -> float:
    """
    Функция возвращает сумму платежей
    """
    app_logger.info("Получаем сумму платежей")
    result = 0.0
    for transaction in data:
        if transaction >= 0:
            result += transaction
    result = round(result, 2)
    return result


def get_cashback(spent: float) -> float:
    """
    Функция возвращает кешбек на основе суммы платежей
    """
    app_logger.info("Получаем кешбек")
    return round(spent / 100.0, 2)


def get_top_transactions(data: list) -> list:
    """
    Функция возвращает список последних пяти транзакций
    """
    app_logger.info("Получаем последние транзакции")
    result = []
    for transaction in data[:5]:
        result.append(
            {
                "date": transaction["Дата платежа"],
                "amount": -float(transaction["Сумма платежа"]),
                "category": transaction["Категория"],
                "description": transaction["Описание"],
            }
        )
    return result


def get_cards(data: list) -> list:
    """
    Функция возвращает список словарей с номером карты, сумме платежей по конкретной карте и кешбек по конкретной карте
    """
    app_logger.info("Получаем траты по картам")
    cards = []
    cards_spend: dict = {}
    result = []
    app_logger.info("Получаем список карт")
    for transaction in data:
        if transaction["Номер карты"] not in cards and type(transaction["Номер карты"]) is str:
            cards.append(transaction["Номер карты"])
    for card in cards:
        cards_spend[card] = []
    app_logger.info("Получаем списки трат по картам")
    for transaction in data:
        for card in cards:
            if transaction["Номер карты"] is card:
                cards_spend[card].append(transaction["Сумма операции"])
    app_logger.info("Генерация вывода")
    for card, spent in cards_spend.items():
        result.append(
            {
                "last_digits": get_last_digits(card),
                "total_spent": get_total_spent(spent),
                "cashback": get_cashback(get_total_spent(spent)),
            }
        )
    return result


def set_date(data: list, date: Optional[str] = None) -> list:
    """
    Функция возвращает список транзакций в текущем месяце, если не указана другая дата
    """
    result = []
    if date:
        date_items = datetime.strptime(date, "%d.%m.%Y")
        app_logger.info(f"Получаем транзакции за {date_items.month} месяц {date_items.year} года")
    else:
        date_items = datetime.now()
        app_logger.info("Получаем транзакции за текущий месяц")
    for transaction in data:
        transaction_date = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if (
            1 <= transaction_date.day <= date_items.day
            and transaction_date.month == date_items.month
            and transaction_date.year == date_items.year
        ):
            result.append(transaction)
    return result


if __name__ == "__main__":
    import os

    from src.utils import read_xlsx

    print(set_date(read_xlsx(os.path.abspath("../data/operations.xlsx")), date=input()))
