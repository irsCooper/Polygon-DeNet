from web3.exceptions import BadFunctionCallOutput
from web3 import Web3
from typing import Dict, List

from src.blockchain.polygon.base_contract_client import BaseContractClient


class ERC20Contract(BaseContractClient):
    """
    Асинхронный клиент верхнего уровня для работы с ERC-20 контрактами.
    Предоставляет удобные методы (decimals, balance, balance_batch),
    абстрагируя низкоуровневые вызовы BaseContractClient.

    Класс содержит базовый функционал для решения тестового ззадания
    и будет расширён в будущем.
    """
    def __init__(self, w3_client: Web3, contract_address: str, abi_path: str, default_sender: str = None):
        super().__init__(
            w3_client=w3_client,
            contract_address=contract_address, 
            contract_json_path=abi_path, 
            default_sender=default_sender
        )
    
    def get_decimals(self) -> int:
        return self.call("decimals")

    def get_balance(self, address: str) -> float:
        try:
            raw = self.call("balanceOf", [address])
            decimals = self.get_decimals()
            return raw / (10 ** decimals)
        except BadFunctionCallOutput as e:
            print(e)
            return 0

    def get_balance_batch(self, addresses: List[str]) -> List[float]:
        return [self.get_balance(addr) or 0 for addr in addresses]
    
    def get_token_info(self) -> dict:
        try:
            symbol = self.call_sync("symbol")
            name = self.call_sync("name")
            total_supply = self.call_sync("totalSupply")
            decimals = self.call_sync("decimals")
            total_supply_adjusted = total_supply / (10 ** decimals) if decimals else total_supply
            return {
                "symbol": symbol,
                "name": name,
                "totalSupply": total_supply_adjusted
            }
        except Exception as e:
            return {"error": str(e)}
    
    
