import random
import string
import time

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

ALPHAVANTAGE_API_KEY: str = "V2V43QAQ8RILGBOW"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

last_api_call_time = 0.0
cached_rate = None


def create_random_string(size: int) -> str:
    return "".join([random.choice(string.ascii_letters) for _ in range(size)])


@app.get("/generate-article")
async def get_information():
    """This endpoint returns the random information"""
    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


class Exchange(BaseModel):
    from_currency: str
    to_currency: str


@app.post("/exchange-rate")
async def get_current_market_state(rates: Exchange):
    global last_api_call_time, cached_rate

    if time.time() - last_api_call_time < 10 and cached_rate:
        return {"rate": cached_rate}

    from_currency = rates.from_currency
    to_currency = rates.to_currency
    url = (
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&to_currency={to_currency}&"
        f"apikey={ALPHAVANTAGE_API_KEY}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    rate = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]

    cached_rate = rate
    last_api_call_time = time.time()

    return {"rate": rate}
