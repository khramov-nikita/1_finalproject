import pytest
import pandas


@pytest.fixture
def data() -> list:
    return [
        {
            "Дата операции": "17.07.2019 15:01:15",
            "Дата платежа": "19.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -27.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -27.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Дом и ремонт",
            "MCC": 5200.0,
            "Описание": "OOO Nadezhda",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 27.0,
        },
        {
            "Дата операции": "16.07.2019 16:30:10",
            "Дата платежа": "18.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -49.8,
            "Валюта операции": "RUB",
            "Сумма платежа": -49.8,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "SPAR",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 49.8,
        },
        {
            "Дата операции": "16.07.2019 16:13:54",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -114.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -114.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Фастфуд",
            "MCC": 5814.0,
            "Описание": "IP Yakubovskaya M. V.",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 114.0,
        },
        {
            "Дата операции": "16.07.2019 13:27:53",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -148.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -148.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Транспорт",
            "MCC": 4121.0,
            "Описание": "Яндекс Такси",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 148.0,
        },
        {
            "Дата операции": "16.07.2019 00:00:00",
            "Дата платежа": "16.07.2019",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": 189.0,
            "Валюта операции": "RUB",
            "Сумма платежа": 189.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Бонусы",
            "MCC": None,
            "Описание": "Вознаграждение за операции покупок",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 189.0,
        },
        {
            "Дата операции": "16.07.2019 00:00:00",
            "Дата платежа": "16.07.2019",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": 258.3,
            "Валюта операции": "RUB",
            "Сумма платежа": 258.3,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Бонусы",
            "MCC": None,
            "Описание": "Проценты на остаток по счету",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 258.3,
        },
        {
            "Дата операции": "15.07.2019 23:37:42",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -77.36,
            "Валюта операции": "RUB",
            "Сумма платежа": -77.36,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "SPAR",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 77.36,
        },
        {
            "Дата операции": "15.07.2019 20:00:31",
            "Дата платежа": "15.07.2019",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -50000.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -50000.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": 'На р/с ООО "ФОРТУНА"',
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 50000.0,
        },
        {
            "Дата операции": "15.07.2019 16:55:34",
            "Дата платежа": "16.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -120.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -120.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Фастфуд",
            "MCC": 5814.0,
            "Описание": "IP Yakubovskaya M. V.",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 120.0,
        },
        {
            "Дата операции": "15.07.2019 16:50:10",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -114.19,
            "Валюта операции": "RUB",
            "Сумма платежа": -114.19,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5499.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 114.19,
        },
        {
            "Дата операции": "15.07.2019 13:43:11",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -200.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -200.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Ж/д билеты",
            "MCC": 4111.0,
            "Описание": "Метро Санкт-Петербург",
            "Бонусы (включая кэшбэк)": 4,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 200.0,
        },
        {
            "Дата операции": "15.07.2019 11:41:14",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -45.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -45.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Ж/д билеты",
            "MCC": 4111.0,
            "Описание": "Метро Санкт-Петербург",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 45.0,
        },
        {
            "Дата операции": "15.07.2019 09:43:16",
            "Дата платежа": "17.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -929.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -929.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Аптеки",
            "MCC": 5912.0,
            "Описание": "Apteka 7",
            "Бонусы (включая кэшбэк)": 18,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 929.0,
        },
        {
            "Дата операции": "14.07.2019 19:16:45",
            "Дата платежа": "16.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -101.37,
            "Валюта операции": "RUB",
            "Сумма платежа": -101.37,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Магнит",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 101.37,
        },
        {
            "Дата операции": "14.07.2019 19:08:09",
            "Дата платежа": "16.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -321.5,
            "Валюта операции": "RUB",
            "Сумма платежа": -321.5,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "SPAR",
            "Бонусы (включая кэшбэк)": 6,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 321.5,
        },
    ]


@pytest.fixture
def data_result() -> dict:
    return {
        "Дом и ремонт": 0,
        "Супермаркеты": 11,
        "Фастфуд": 4,
        "Транспорт": 2,
        "Бонусы": 0,
        "Переводы": 0,
        "Ж/д билеты": 4,
        "Аптеки": 18
    }
