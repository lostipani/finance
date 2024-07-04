import requests
from dotenv import load_dotenv, find_dotenv

from authorization import Auth

load_dotenv(find_dotenv)


class AlphaVantage:

    API_URL = "https://www.alphavantage.co/"

    def __init__(self, auth: Auth):
        self.token = auth.token

    def get_daily(self, symbol: str, size: str = "compact") -> dict:
        return self._get_fun(
            function="TIME_SERIES_DAILY",
            interval=None,
            symbol=symbol,
            size=size,
        )

    def _get_fun(
        self, function: str, interval: str, symbol: str, size: str
    ) -> dict:
        url = (
            f"{self.API_URL}/query?"
            f"function={function}&"
            f"interval={interval}&"
            f"symbol={symbol}&"
            f"outputsize={size}&"
            f"apikey={self.token}"
        )
        resp = requests.get(url)
        return resp.json()
