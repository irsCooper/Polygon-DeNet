from web3 import AsyncWeb3
from web3.contract import AsyncContract
from web3.contract.async_contract import AsyncContractFunctions
from web3.exceptions import ContractLogicError
from pathlib import Path
import json


class BaseContractClient:
    def __init__(self, w3_client: AsyncWeb3, contract_address: str, contract_json_path: str, default_sender: str):
        with open(Path(contract_json_path)) as f:
            config = json.load(f)

        self.w3: AsyncWeb3 = w3_client
        self._default_sender = self.w3.to_checksum_address(default_sender)
        self.contract: AsyncContract = w3_client.eth.contract(
            address=contract_address,
            abi=config["abi"]
        )
        
    async def set_sender(self, sender: str):
        self._default_sender = self.w3.to_checksum_address(sender)
        
    async def call(self, method_name: str, args: list | None = None):
        method: AsyncContractFunctions = getattr(self.contract.functions, method_name)
        tx_params: dict = {'from': self._default_sender}
        
        try:
            if args:
                return await method(*args).call(tx_params)  
            
            return await method().call(tx_params)
        except ContractLogicError as e:
            return e
        except Exception as e:
            return e

    async def transact(self, method_name: str, args: list | None = None):
        method: AsyncContractFunctions = getattr(self.contract.functions, method_name)
        tx_params: dict = {'from': self._default_sender}

        try:
            if args:
                return await method(*args).transact(tx_params)  
                
            return await method().transact(tx_params)
        except ContractLogicError as e:
            return e
        except Exception as e:
            return e
        
