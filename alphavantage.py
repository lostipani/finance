import requests
from typing import List

from exceptions import NoDataException
from authenticator import AuthenticatorToken


class AlphaVantage:

    API_URL = "https://www.alphavantage.co/"

    def __init__(self, authenticator: AuthenticatorToken):
        self.apikey = authenticator.token

    def get_daily(self, symbol: str, time_window: List[str] = None) -> dict:
        if data_json := self._get_json(
            function="TIME_SERIES_DAILY",
            symbol=symbol,
            outputsize=self._get_outputsize(time_window),
        ):
            return data_json
        else:
            raise NoDataException

    def _get_json(
        self,
        function: str,
        symbol: str,
        outputsize: str,
        datatype: str = "json",
    ) -> dict:
        url = (
            f"{self.API_URL}/query?"
            f"function={function}&"
            f"symbol={symbol}&"
            f"outputsize={outputsize}&"
            f"datatype={datatype}&"
            f"apikey={self.apikey}"
        )
        resp = requests.get(url)
        return resp.json()

    @staticmethod
    def _get_outputsize(time_window: List[str]) -> str:
        if time_window:
            raise NotImplementedError
        return "compact"
