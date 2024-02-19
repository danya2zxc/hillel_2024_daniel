import requests
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

file_path = Path(__file__).resolve().parent
file_n = file_path / 'logs.json' 

ALPHAVANTAGE_API_KEY = "PHYESMU9NOE57A6K"
MIDDLE_CURRENCY = "CHF"


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    response: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = response.json()
    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    with open(file_n, 'a') as file:
        logs_data = {
            "currency_from": currency_from,
            "currency_to": currency_to,
            "rate": coefficient,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        json.dump(logs_data, file, indent=3)
        file.write('\n')  
    return value * coefficient


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="UAH")

total: Price = flight + hotel
print(total)
