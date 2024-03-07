currency_exchange = {
    "USD": {
        "EUR": 0.93,
        "CHF": 0.88,
        "UAH": 37.98,
    },
    "EUR": {
        "USD": 1.08,
        "CHF": 0.94,
        "UAH": 40.89,
    },
    "CHF": {
        "USD": 1.14,
        "EUR": 1.06,
        "UAH": 43.36,
        "CHF": 1,
    },
    "UAH": {
        "USD": 0.02,
        "EUR": 0.02,
        "CHF": 0.02,
    },
}


class Price:
    def __init__(self, value: int | float, currency: str) -> None:
        self.value = value
        self.currency = currency

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )
        else:
            self_chf = self._convert_to_chf()
            other_chf = other._convert_to_chf()
            total_chf = self_chf + other_chf
            return self._convert_from_chf(total_chf)

    def __sub__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=self.value - other.value, currency=self.currency
            )
        else:
            self_chf = self._convert_to_chf()
            other_chf = other._convert_to_chf()
            total_chf = self_chf - other_chf

            return self._convert_from_chf(total_chf)

    def _convert_to_chf(self) -> float:
        return self.value * currency_exchange[self.currency]["CHF"]

    def _convert_from_chf(self, chf_value: float) -> "Price":
        converted_value = chf_value / currency_exchange[self.currency]["CHF"]
        rounded_value = round(converted_value, 2)
        return Price(value=rounded_value, currency=self.currency)

    def convert_to(self, target_currency: str) -> "Price":
        converted_value = (
            self.value * currency_exchange[self.currency][target_currency]
        )
        rounded_value = round(converted_value, 2)
        return Price(value=rounded_value, currency=self.currency)


# Пример использования

flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")

total = flight + hotel
print(total)

drive = Price(value=1000, currency="UAH")
hostel = Price(value=10, currency="USD")

total_1 = drive - hostel
print(total_1)

flight_ = Price(value=3800, currency="EUR")
hotel_ = Price(value=500, currency="CHF")

total_ = flight_ + hotel_
print(total_)

flight_2 = Price(value=5000, currency="CHF")
drive_2 = Price(value=1000, currency="UAH")

total_2 = flight_2 - drive_2
print(total_2)

# Пример конвертации

converted_price = flight.convert_to("UAH")
print(converted_price)


# class Product:
#     def __init__(self, name: str, price: Price):
#         self.name = name
#         self.price = price


# class PaymentProcessor:
#     def checkout(self, product: Product, price: Price):
#         pass
