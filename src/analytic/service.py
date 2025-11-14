from datetime import datetime, timezone
from typing import List, Tuple

from src.blockchain.polygon.api_client import polygon_api_client
from src.core.config import settings


class AnaliticService:
    @classmethod
    def get_top_holders(cls, offset: int, contract_address: str = settings.polygon_config.token_address) -> List[Tuple[str, int]]:
        params = {
            "module": "token",
            "action": "tokenholderlist",
            "contractaddress": contract_address,
            "page": 1,
            "offset": offset,
            "chainid": 137
        }
        data = polygon_api_client.request(params)
        holders = [
            (h["HolderAddress"], int(h["TokenHolderQuantity"]))
            for h in data.get("result", [])
        ]
        return holders

    @classmethod
    def get_last_tx_date(cls, address: str, contract_address: str = settings.polygon_config.token_address) -> datetime | None:
        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "contractaddress": contract_address,
            "page": 1,
            "offset": 1,
            "sort": "desc",
        }
        data = polygon_api_client.request(params)
        result = data.get("result")
        if result:
            ts = int(result[0]["timeStamp"])
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        return None

    @classmethod
    def get_top_with_transactions(cls, offset: int, contract_address: str = settings.polygon_config.token_address) -> List[Tuple[str, int, datetime | None]]:
        holders = cls.get_top_holders(contract_address, offset)
        result = []
        for addr, balance in holders:
            date = cls.get_last_tx_date(contract_address, addr)
            result.append((addr, balance, date))
        return result
