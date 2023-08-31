import requests
import json
from Config import currency


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException("Невозможно перевести одинаковые валюты.")

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f"Некорректный ввод валюты {base}")

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f"Некорректный ввод валюты {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Некорректное кол-во Валюты.")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        prise = float(json.loads(r.content)[currency[quote]]) * amount

        return prise
