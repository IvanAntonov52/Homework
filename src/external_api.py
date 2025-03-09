import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_exchange_rate(currency):
    """Получает текущий курс валюты к рублю (RUB) через API."""
    if not API_KEY:
        raise ValueError("API_KEY не найден в переменных окружения.")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()["rates"]["RUB"]
    except (requests.RequestException, KeyError):
        return None


def convert_rub(transaction):
    """Конвертирует сумму транзакции в рубли (RUB)"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        rate = get_exchange_rate(currency)
        if rate:
            return float(amount) * rate
    return 0.0
