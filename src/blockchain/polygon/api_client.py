from typing import Any
from requests import Session

from src.core.config import settings


class PolygonAPIClient:
    def __init__(
        self,
        api_key: str,
        contract_address: str,
        polygon_api_url: str = settings.polygon_config.polygonscan_api_url
    ):
        self.api_key = api_key
        self.contract_address = contract_address
        self.base_url = polygon_api_url
        self.session: Session = Session()

    def close(self):
        self.session.close()

    def request(self, params: dict[str, Any]) -> dict:
        params = params.copy()
        params["apikey"] = self.api_key
        response = self.session.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()


polygon_api_client: PolygonAPIClient = PolygonAPIClient(
    contract_address=settings.polygon_config.token_address,
    api_key=settings.polygon_config.polygonscan_api_key
)